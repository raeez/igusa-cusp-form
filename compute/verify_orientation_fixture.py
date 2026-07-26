#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for orientation packets.

This script checks only finite reduced-orientation and Weyl-lift packet
shape.  It does not construct orientations and does not prove (O1) or
(O1)+.  A positive result is schema-only completeness.
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


SCHEMA_COMPLETE_ORIENTATION_KIND = "reduced_orientation_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {"check_status", "edge_reduction_status", "strict_status", "ml_status", "notes"}
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "cyclic_only",
        "mock",
        "picard_line_only",
        "placeholder",
        "scalar_only",
        "status_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_EDGE_REDUCTION_STATUSES = frozenset({"edge_reduced", "verified"})
ACCEPTABLE_STRICT_STATUSES = frozenset({"strict_verified", "verified"})
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
        "orientation_lines.csv",
        "orientation lines and square roots",
        (
            "line_id",
            "stratum_id",
            "det_complex_id",
            "square_root_id",
            "square_defect_rank",
            "orientation_class_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "ts_multiplicativity.csv",
        "Thom-Sebastiani multiplicativity",
        (
            "check_id",
            "extension_stack_id",
            "left_line_id",
            "right_line_id",
            "target_line_id",
            "ts_isomorphism_id",
            "pentagon_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "quotient_borel.csv",
        "quotient Cech-Borel classes",
        (
            "check_id",
            "stratum_id",
            "class_type",
            "class_value_rank",
            "null_trivialization_id",
            "edge_reduction_status",
            "defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "finite_stabilizers.csv",
        "finite-stabilizer edge calculations",
        (
            "check_id",
            "stratum_id",
            "stabilizer_type",
            "group_order",
            "two_primary_rank",
            "edge_reduction_status",
            "b20",
            "b11",
            "b02",
            "a1",
            "a12",
            "a2",
            "lambda1",
            "lambda2",
            "cyclic_only",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "weyl_lifts.csv",
        "Weyl determinant-line lifts",
        (
            "lift_id",
            "delta_id",
            "source_stratum_id",
            "target_stratum_id",
            "lift_matrix_id",
            "tau_square_defect_rank",
            "torsor_defect_rank",
            "quotient_cocycle_transport_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coxeter_cocycles.csv",
        "projective cocycle and Coxeter coherence",
        (
            "check_id",
            "orbit_id",
            "generator_word",
            "cocycle_matrix_id",
            "cocycle_defect_rank",
            "cochain_id",
            "cochain_defect_rank",
            "coxeter_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "orientation transition and ML identities",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "orientation_line_id",
            "quotient_datum_id",
            "weyl_lift_id",
            "strict_status",
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
        "orientation scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_orientation",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_QUOTIENT_CLASS_TYPES = frozenset(
    {"reduced_gerbe", "free_E", "finite_stabilizer_borel", "linearization"}
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {"scalar_trace", "squared_determinant", "op_scalar_branch", "maass_character_value"}
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a reduced-orientation fixture packet without proving (O1)."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="orientation fixture directory")
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
    orientation_kind = manifest.get("orientation_kind")
    if orientation_kind != SCHEMA_COMPLETE_ORIENTATION_KIND:
        issues.append(
            "manifest orientation_kind is "
            f"{orientation_kind!r}, not {SCHEMA_COMPLETE_ORIENTATION_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("picard_line_only") is True:
        issues.append("manifest marks this packet as Picard-line-only; (O1) forbids this")


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
        if "edge_reduction_status" in table.spec.columns:
            edge = row.get("edge_reduction_status", "")
            if edge not in ACCEPTABLE_EDGE_REDUCTION_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has edge_reduction_status={edge!r}"
                )
        if "strict_status" in table.spec.columns:
            strict = row.get("strict_status", "")
            if strict not in ACCEPTABLE_STRICT_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has strict_status={strict!r}"
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
            tokens = {token for token in re.split(r"[^0-9A-Za-z]+", value.lower()) if token}
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


def require_false(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = row.get(column, "").lower()
    if value != "false":
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}='false', got {row.get(column, '')!r}"
        )


def require_true(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = row.get(column, "").lower()
    if value != "true":
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}='true', got {row.get(column, '')!r}"
        )


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        if table.spec.path == "orientation_lines.csv":
            require_zero(table, index, row, "square_defect_rank", issues)
            require_zero(table, index, row, "orientation_class_rank", issues)
        elif table.spec.path == "ts_multiplicativity.csv":
            require_zero(table, index, row, "pentagon_defect_rank", issues)
        elif table.spec.path == "quotient_borel.csv":
            require_zero(table, index, row, "class_value_rank", issues)
            require_zero(table, index, row, "defect_rank", issues)
        elif table.spec.path == "finite_stabilizers.csv":
            require_false(table, index, row, "cyclic_only", issues)
            for column in (
                "b20",
                "b11",
                "b02",
                "a1",
                "a12",
                "a2",
                "lambda1",
                "lambda2",
            ):
                require_zero(table, index, row, column, issues)
            group_order = parse_int(table, index, row, "group_order", issues)
            two_primary_rank = parse_int(table, index, row, "two_primary_rank", issues)
            if group_order is not None and group_order <= 0:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires positive group_order, got {group_order}"
                )
            if two_primary_rank is not None and two_primary_rank not in {0, 1, 2}:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires two_primary_rank in {{0,1,2}}, got {two_primary_rank}"
                )
        elif table.spec.path == "weyl_lifts.csv":
            require_zero(table, index, row, "tau_square_defect_rank", issues)
            require_zero(table, index, row, "torsor_defect_rank", issues)
            require_zero(table, index, row, "quotient_cocycle_transport_defect_rank", issues)
        elif table.spec.path == "coxeter_cocycles.csv":
            require_zero(table, index, row, "cocycle_defect_rank", issues)
            require_zero(table, index, row, "cochain_defect_rank", issues)
            require_zero(table, index, row, "coxeter_defect_rank", issues)
        elif table.spec.path == "transitions.csv":
            require_zero(table, index, row, "r1lim_rank", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_true(table, index, row, "excluded_from_orientation", issues)


def check_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path == "quotient_borel.csv" and table.rows:
        present = {row.get("class_type", "") for row in table.rows}
        missing = sorted(REQUIRED_QUOTIENT_CLASS_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: quotient_borel.csv missing class_type rows: "
                f"{','.join(missing)}"
            )
    if table.spec.path == "scalar_firewall.csv" and table.rows:
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
        check_statuses(table, issues)
        check_payload(table, issues)
        check_provenance(table, issues)
        check_semantics(table, issues)
        check_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("reduced-orientation fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("orientation_certification: false")
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
