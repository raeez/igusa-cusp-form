#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for O2 wall-atlas packets.

This script checks only the retained type-II wall-atlas packet.  It
does not construct the atlas, prove (O2), or identify scalar
normalizations with orientation data.  A positive result is schema-only
completeness for the table packet.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCHEMA_COMPLETE_O2_KIND = "type_ii_wall_atlas_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {"check_status", "charge_match_status", "semistability_status", "notes"}
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "generic_chart_only",
        "local_only",
        "maass_character_only",
        "mock",
        "op_scalar_only",
        "placeholder",
        "scalar_only",
        "signed_only",
        "status_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_CHARGE_MATCH_STATUSES = frozenset({"charge_match_verified", "verified"})
ACCEPTABLE_SEMISTABILITY_STATUSES = frozenset({"semistability_verified", "verified"})


@dataclass(frozen=True)
class TableSpec:
    path: str
    gate: str
    columns: tuple[str, ...]
    require_rows: bool = True


@dataclass
class CsvTable:
    spec: TableSpec
    rows: list[dict[str, str]]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "wall_objects.csv",
        "retained type-II wall objects",
        (
            "wall_id",
            "delta_id",
            "hn_height",
            "charge_match_status",
            "semistability_status",
            "self_ext_splitting_id",
            "rank_one_block_id",
            "invariant_unit_id",
            "quotient_orientation_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "wall_charts.csv",
        "rank-one Pfaffian wall charts",
        (
            "chart_id",
            "wall_id",
            "coordinate_id",
            "tangent_chart_id",
            "tangent_pfaffian_line_id",
            "normal_block_id",
            "normal_rank",
            "divisor_order",
            "unit_invariant",
            "reflection_flips_coordinate",
            "local_sign",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "overlaps.csv",
        "wall-atlas overlap Cech/cochain identities",
        (
            "overlap_id",
            "left_chart_id",
            "right_chart_id",
            "transition_isomorphism_id",
            "cech_2cocycle_value",
            "cochain_id",
            "coboundary_defect_rank",
            "unit_overlap_defect_rank",
            "orientation_overlap_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "orbit_transport.csv",
        "Weyl orbit transport of wall charts",
        (
            "transport_id",
            "from_wall_id",
            "to_wall_id",
            "weyl_word",
            "weyl_lift_id",
            "orientation_transport_id",
            "pfaffian_transport_defect_rank",
            "rank_preservation_defect_rank",
            "sign_preservation_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "half_hilbert_orbit.csv",
        "half-Hilbert orbit sign assignment",
        (
            "orbit_id",
            "hn_height",
            "binary_coordinate_count",
            "orbit_cardinality",
            "component_count",
            "boundary_count",
            "sign_assignment_matrix_id",
            "coverage_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "compatibilities.csv",
        "O2 compatibility identities",
        (
            "check_id",
            "compatibility_type",
            "wall_id",
            "source_data_ids",
            "defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_separation.csv",
        "O2 scalar separation firewall",
        (
            "check_id",
            "separation_type",
            "operator_value",
            "automorphic_value",
            "equality_value",
            "excluded_identification",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_COMPATIBILITY_TYPES = frozenset(
    {
        "boundary",
        "component",
        "hn_transition",
        "protected_integration",
        "quotient_orientation",
        "thom_sebastiani",
        "weyl_lift",
    }
)
REQUIRED_SCALAR_SEPARATION_TYPES = frozenset(
    {
        "maass_character_not_atlas",
        "op_scalar_not_orientation",
        "wall_count_vs_squared_theta_leading",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a retained O2 wall-atlas fixture packet without proving O2."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="O2 fixture directory")
    parser.add_argument("--check", action="store_true", help="explicit check-only mode")
    parser.add_argument(
        "--schema-only-ok",
        action="store_true",
        help="return process success for schema-only completeness",
    )
    return parser.parse_args(argv)


def load_manifest(fixture: Path, issues: list[str]) -> dict[str, object]:
    manifest_path = fixture / MANIFEST_NAME
    if not manifest_path.is_file():
        issues.append(f"missing required manifest: {manifest_path}")
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"manifest is not valid JSON: {manifest_path}: {exc}")
        return {}
    if not isinstance(manifest, dict):
        issues.append(f"manifest root is not an object: {manifest_path}")
        return {}
    return manifest


def check_manifest(manifest: dict[str, object], issues: list[str]) -> None:
    o2_kind = manifest.get("o2_atlas_kind")
    if o2_kind != SCHEMA_COMPLETE_O2_KIND:
        issues.append(
            "manifest o2_atlas_kind is "
            f"{o2_kind!r}, not {SCHEMA_COMPLETE_O2_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("local_only") is True:
        issues.append("manifest marks this packet as local-only; O2 requires a wall atlas")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; O2 forbids scalar-only data")
    if manifest.get("op_scalar_only") is True:
        issues.append("manifest marks this packet as OP-scalar-only; O2 is orientation data")


def check_readme(fixture: Path, issues: list[str]) -> None:
    readme_path = fixture / README_NAME
    if not readme_path.is_file():
        issues.append(f"missing required README: {readme_path}")


def nonempty_rows(reader: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in reader:
        normalized = {
            key: (value or "").strip()
            for key, value in row.items()
            if key is not None
        }
        if any(normalized.values()):
            rows.append(normalized)
    return rows


def payload_columns(spec: TableSpec) -> tuple[str, ...]:
    return tuple(column for column in spec.columns if column not in NON_PAYLOAD_COLUMNS)


def row_has_payload(spec: TableSpec, row: dict[str, str]) -> bool:
    return any(row.get(column, "") for column in payload_columns(spec))


def load_csv_table(fixture: Path, spec: TableSpec, issues: list[str]) -> CsvTable | None:
    table_path = fixture / spec.path
    if not table_path.is_file():
        issues.append(f"{spec.gate}: missing table {spec.path}")
        return None
    with table_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != spec.columns:
            issues.append(
                f"{spec.gate}: header mismatch in {spec.path}; "
                f"expected {','.join(spec.columns)}"
            )
            return CsvTable(spec, nonempty_rows(reader))
        rows = nonempty_rows(reader)
    if spec.require_rows and not any(row_has_payload(spec, row) for row in rows):
        issues.append(f"{spec.gate}: {spec.path} has no supplied rows with mathematical payload")
    return CsvTable(spec, rows)


def check_statuses(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        status = row.get("check_status", "")
        if status != "verified":
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"has check_status={status!r}, not 'verified'"
            )
        if "charge_match_status" in table.spec.columns:
            charge = row.get("charge_match_status", "")
            if charge not in ACCEPTABLE_CHARGE_MATCH_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has charge_match_status={charge!r}"
                )
        if "semistability_status" in table.spec.columns:
            semistability = row.get("semistability_status", "")
            if semistability not in ACCEPTABLE_SEMISTABILITY_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has semistability_status={semistability!r}"
                )


def check_payload(table: CsvTable, issues: list[str]) -> None:
    columns = payload_columns(table.spec)
    for index, row in enumerate(table.rows, start=2):
        missing = [column for column in columns if not row.get(column, "")]
        if missing:
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"missing mathematical payload columns: {','.join(missing)}"
            )


def check_provenance(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        for column in PROVENANCE_COLUMNS:
            value = row.get(column, "")
            if not value:
                continue
            normalized = re.sub(r"[^0-9a-z]+", "_", value.lower()).strip("_")
            tokens = {
                token for token in re.split(r"[^0-9A-Za-z]+", value.lower()) if token
            }
            forbidden = sorted(
                token
                for token in FORBIDDEN_PROVENANCE_TOKENS
                if token in tokens or token in normalized
            )
            if forbidden:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"column {column!r} contains non-proof provenance tokens: "
                    f"{','.join(forbidden)}"
                )


def parse_int(
    table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]
) -> int | None:
    value = row.get(column, "")
    if not re.fullmatch(r"[+-]?\d+", value):
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"column {column!r} has non-integral value {value!r}"
        )
        return None
    return int(value)


def require_zero(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value != 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column}=0, got {value}"
        )


def require_int(
    table: CsvTable,
    index: int,
    row: dict[str, str],
    column: str,
    expected: int,
    issues: list[str],
) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value != expected:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}={expected}, got {value}"
        )


def require_nonnegative(
    table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]
) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value < 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}>=0, got {value}"
        )


def require_bool_text(
    table: CsvTable, index: int, row: dict[str, str], column: str, expected: str, issues: list[str]
) -> None:
    value = row.get(column, "").lower()
    if value != expected:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}={expected!r}, got {row.get(column, '')!r}"
        )


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        if table.spec.path == "wall_charts.csv":
            require_int(table, index, row, "normal_rank", 1, issues)
            require_int(table, index, row, "divisor_order", 1, issues)
            require_bool_text(table, index, row, "unit_invariant", "true", issues)
            require_bool_text(table, index, row, "reflection_flips_coordinate", "true", issues)
            require_int(table, index, row, "local_sign", -1, issues)
        elif table.spec.path == "overlaps.csv":
            if row.get("cech_2cocycle_value", "") not in {"-1", "1"}:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    "requires cech_2cocycle_value in {-1,1}"
                )
            require_zero(table, index, row, "coboundary_defect_rank", issues)
            require_zero(table, index, row, "unit_overlap_defect_rank", issues)
            require_zero(table, index, row, "orientation_overlap_defect_rank", issues)
        elif table.spec.path == "orbit_transport.csv":
            require_zero(table, index, row, "pfaffian_transport_defect_rank", issues)
            require_zero(table, index, row, "rank_preservation_defect_rank", issues)
            require_zero(table, index, row, "sign_preservation_defect_rank", issues)
        elif table.spec.path == "half_hilbert_orbit.csv":
            require_int(table, index, row, "binary_coordinate_count", 12, issues)
            require_int(table, index, row, "orbit_cardinality", 4096, issues)
            require_nonnegative(table, index, row, "component_count", issues)
            require_nonnegative(table, index, row, "boundary_count", issues)
            require_zero(table, index, row, "coverage_defect_rank", issues)
        elif table.spec.path == "compatibilities.csv":
            require_zero(table, index, row, "defect_rank", issues)
        elif table.spec.path == "scalar_separation.csv":
            require_bool_text(table, index, row, "excluded_identification", "true", issues)
            if row.get("separation_type") == "wall_count_vs_squared_theta_leading":
                require_int(table, index, row, "operator_value", 4096, issues)
                require_int(table, index, row, "automorphic_value", 4096, issues)
                require_int(table, index, row, "equality_value", 4096, issues)


def check_compatibility_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "compatibilities.csv" or not table.rows:
        return
    present = {row.get("compatibility_type", "") for row in table.rows}
    missing = sorted(REQUIRED_COMPATIBILITY_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: compatibilities.csv missing compatibility_type rows: "
            f"{','.join(missing)}"
        )


def check_scalar_separation_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "scalar_separation.csv" or not table.rows:
        return
    present = {row.get("separation_type", "") for row in table.rows}
    missing = sorted(REQUIRED_SCALAR_SEPARATION_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: scalar_separation.csv missing separation_type rows: "
            f"{','.join(missing)}"
        )


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.exists():
        return False, [f"fixture path does not exist: {fixture}"]
    if not fixture.is_dir():
        return False, [f"fixture path is not a directory: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_readme(fixture, issues)

    tables: list[CsvTable] = []
    for spec in TABLE_SPECS:
        table = load_csv_table(fixture, spec, issues)
        if table is not None:
            tables.append(table)

    for table in tables:
        check_statuses(table, issues)
        check_payload(table, issues)
        check_provenance(table, issues)
        check_semantics(table, issues)
        check_compatibility_coverage(table, issues)
        check_scalar_separation_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("O2 wall-atlas fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("o2_certification: false")
    print("mathematical_certification: false")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    schema_only_complete, issues = run(args.fixture)
    print_report(args.fixture, schema_only_complete, issues)
    return 0 if schema_only_complete and args.schema_only_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
