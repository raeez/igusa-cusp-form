#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for finite Pfaffian packets.

This script checks only the finite geometric Pfaffian datum packet.  It
does not construct Pfaffian lines, derive Borcherds products, or certify
the Pfaffian--Dirac theorem.  A positive result is schema-only
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


SCHEMA_COMPLETE_PFIN_KIND = "finite_geometric_pfaffian_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {"check_status", "retained_status", "closed_image_status", "ml_status", "notes"}
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "scalar_only",
        "signed_only",
        "status_only",
        "target_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_RETAINED_STATUSES = frozenset({"retained_verified", "verified"})
ACCEPTABLE_CLOSED_IMAGE_STATUSES = frozenset({"closed_image_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})


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
        "strata.csv",
        "retained Pfaffian strata",
        (
            "stratum_id",
            "hn_height",
            "quotient_chart_id",
            "retained_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "skew_complexes.csv",
        "cosection-reduced skew perfect complexes",
        (
            "complex_id",
            "stratum_id",
            "amplitude",
            "rank_even",
            "rank_odd",
            "skew_self_duality_matrix_id",
            "obstruction_theory_id",
            "quotient_compatibility_id",
            "defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pfaffian_lines.csv",
        "Pfaffian lines and determinant square isomorphisms",
        (
            "line_id",
            "complex_id",
            "orientation_id",
            "determinant_line_id",
            "square_isomorphism_id",
            "square_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pfaffian_sections.csv",
        "finite Pfaffian sections",
        (
            "section_id",
            "line_id",
            "degree_id",
            "active_support",
            "even_rank",
            "odd_rank",
            "borcherds_exponent",
            "exponent_residual",
            "skew_block_id",
            "section_matrix_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "wall_charts.csv",
        "type-II Pfaffian wall charts",
        (
            "wall_id",
            "chart_id",
            "delta_id",
            "wall_coordinate_id",
            "unit_id",
            "tangent_section_id",
            "normal_rank",
            "divisor_order",
            "type_i_excluded",
            "reflection_unit_invariant",
            "sign_value",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "automorphic_comparisons.csv",
        "Pfaffian-to-automorphic line comparisons",
        (
            "comparison_id",
            "line_id",
            "automorphic_line_id",
            "cusp_frame_id",
            "leading_coefficient",
            "weight",
            "character",
            "square_compatibility_id",
            "leading_residual",
            "square_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "Pfaffian line and section transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "line_id",
            "section_id",
            "line_transition_id",
            "section_transition_id",
            "closed_image_status",
            "ml_status",
            "r1lim_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_pfin",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_FIREWALL_TYPES = frozenset(
    {"scalar_borcherds_product", "squared_determinant", "op_scalar_trace", "exponent_table"}
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a finite Pfaffian fixture packet without proving P_fin."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="Pfaffian fixture directory")
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
    pfaffian_kind = manifest.get("pfaffian_kind")
    if pfaffian_kind != SCHEMA_COMPLETE_PFIN_KIND:
        issues.append(
            "manifest pfaffian_kind is "
            f"{pfaffian_kind!r}, not {SCHEMA_COMPLETE_PFIN_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; P_fin forbids scalar-only data")


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


def check_status(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        status = row.get("check_status", "")
        if status != "verified":
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"has check_status={status!r}, not 'verified'"
            )
        if "retained_status" in table.spec.columns:
            retained = row.get("retained_status", "")
            if retained not in ACCEPTABLE_RETAINED_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has retained_status={retained!r}"
                )
        if "closed_image_status" in table.spec.columns:
            closed = row.get("closed_image_status", "")
            if closed not in ACCEPTABLE_CLOSED_IMAGE_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has closed_image_status={closed!r}"
                )
        if "ml_status" in table.spec.columns:
            ml_status = row.get("ml_status", "")
            if ml_status not in ACCEPTABLE_ML_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has ml_status={ml_status!r}"
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


def parse_int(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> int | None:
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


def require_int(table: CsvTable, index: int, row: dict[str, str], column: str, expected: int, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value != expected:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}={expected}, got {value}"
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


def check_pfaffian_semantics(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        if table.spec.path == "skew_complexes.csv":
            require_zero(table, index, row, "defect_rank", issues)
            parse_int(table, index, row, "rank_even", issues)
            parse_int(table, index, row, "rank_odd", issues)
        elif table.spec.path == "pfaffian_lines.csv":
            require_zero(table, index, row, "square_defect_rank", issues)
        elif table.spec.path == "pfaffian_sections.csv":
            require_zero(table, index, row, "exponent_residual", issues)
            parse_int(table, index, row, "even_rank", issues)
            parse_int(table, index, row, "odd_rank", issues)
            parse_int(table, index, row, "borcherds_exponent", issues)
            if row.get("active_support") not in {"active", "inactive"}:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has active_support={row.get('active_support')!r}"
                )
        elif table.spec.path == "wall_charts.csv":
            require_int(table, index, row, "normal_rank", 1, issues)
            require_int(table, index, row, "divisor_order", 1, issues)
            require_int(table, index, row, "sign_value", -1, issues)
            require_bool_text(table, index, row, "type_i_excluded", "true", issues)
            require_bool_text(table, index, row, "reflection_unit_invariant", "true", issues)
        elif table.spec.path == "automorphic_comparisons.csv":
            require_int(table, index, row, "leading_coefficient", 64, issues)
            require_int(table, index, row, "weight", 5, issues)
            require_zero(table, index, row, "leading_residual", issues)
            require_zero(table, index, row, "square_defect_rank", issues)
            if row.get("character") != "nu_delta5":
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires character='nu_delta5', got {row.get('character')!r}"
                )
        elif table.spec.path == "transitions.csv":
            require_zero(table, index, row, "r1lim_rank", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_pfin", "true", issues)


def check_scalar_firewall_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "scalar_firewall.csv" or not table.rows:
        return
    present = {row.get("firewall_type", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: scalar_firewall.csv missing firewall_type rows: "
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
        check_status(table, issues)
        check_payload(table, issues)
        check_provenance(table, issues)
        check_pfaffian_semantics(table, issues)
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite Pfaffian fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("pfaffian_certification: false")
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
