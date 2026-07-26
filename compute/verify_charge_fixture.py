#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for finite charge windows.

This script checks only the finite charge-window packet: active Igusa
support, downward saturation, Liu HN bounds, Gram map, cocycle,
normal-ordered lifts, target windows, primitive lifts, transitions, and
scalar firewall.  It does not construct the charge window.  A positive
result is schema-only completeness for the table packet.
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


SCHEMA_COMPLETE_CHARGE_KIND = "finite_charge_window_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "active_status",
        "check_status",
        "finite_type_status",
        "ml_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "source_formula_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "hilbert_scheme_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "rank_only",
        "scalar_only",
        "signed_only",
        "status_only",
        "target_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_ACTIVE_STATUSES = frozenset({"active_verified", "verified"})
ACCEPTABLE_FINITE_TYPE_STATUSES = frozenset({"finite_type_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
ACCEPTABLE_STRICT_STATUSES = frozenset({"strict_verified", "verified"})


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
        "active_support.csv",
        "Igusa active support",
        (
            "degree_id",
            "n",
            "l",
            "m",
            "nm",
            "elliptic_l",
            "coefficient",
            "active_status",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "window_saturation.csv",
        "downward saturated target window",
        (
            "window_id",
            "hn_height",
            "degree_id",
            "parent_degree_id",
            "order_relation_id",
            "difference_positive",
            "downward_closed",
            "coverage_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "liu_hn_window.csv",
        "Liu HN charge-height window",
        (
            "hntype_id",
            "hn_height",
            "charge_id",
            "liu_charge_id",
            "height_value",
            "retained_in_window",
            "finite_type_status",
            "height_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "gram_map.csv",
        "Mukai-Gram map rows",
        (
            "charge_id",
            "q_square_half",
            "qp_pairing",
            "p_square_half",
            "gram_degree_id",
            "integrality_defect_rank",
            "formula_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cocycle_identities.csv",
        "symmetric bilinear Gram cocycle",
        (
            "identity_id",
            "left_charge_id",
            "right_charge_id",
            "b_qq",
            "b_qp",
            "b_pp",
            "delta_b_defect_rank",
            "polarization_defect_rank",
            "bilinearity_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "normal_ordered_lifts.csv",
        "normal-ordered lift orbit",
        (
            "lift_id",
            "charge_id",
            "decomposition_id",
            "t_translate_id",
            "hat_charge_id",
            "orbit_membership",
            "additivity_defect_rank",
            "central_extension_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "target_windows.csv",
        "normal-ordered target test windows",
        (
            "target_window_id",
            "source_lift_id",
            "gram_degree_id",
            "test_window_id",
            "image_membership",
            "transition_compatibility_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "primitive_lifts.csv",
        "formal primitive lifts of Gram triples",
        (
            "lift_id",
            "gram_degree_id",
            "formal_charge_id",
            "lift_map_id",
            "lift_residual_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "charge-window transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "window_id",
            "lift_transition_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "active_support_defect_rank",
            "saturation_defect_rank",
            "cocycle_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "charge-window scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_charge_window",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "hilbert_scheme_scalar",
        "pfaffian_product",
        "signed_exponent_only",
        "source_rank_only",
        "target_presentation_only",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite charge-window fixture shape without proving the window."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="charge fixture directory")
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
    charge_kind = manifest.get("charge_kind")
    if charge_kind != SCHEMA_COMPLETE_CHARGE_KIND:
        issues.append(
            "manifest charge_kind is "
            f"{charge_kind!r}, not {SCHEMA_COMPLETE_CHARGE_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    for key in (
        "hilbert_scheme_scalar",
        "pfaffian_product",
        "signed_exponent_only",
        "source_rank_only",
        "target_presentation_only",
        "scalar_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"manifest marks this packet as {key}; charge-window rows are required")


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
        status_checks = (
            ("active_status", ACCEPTABLE_ACTIVE_STATUSES),
            ("finite_type_status", ACCEPTABLE_FINITE_TYPE_STATUSES),
            ("ml_status", ACCEPTABLE_ML_STATUSES),
            ("strict_status", ACCEPTABLE_STRICT_STATUSES),
        )
        for column, acceptable in status_checks:
            if column in table.spec.columns:
                value = row.get(column, "")
                if value not in acceptable:
                    issues.append(
                        f"{table.spec.gate}: {table.spec.path}:{index} "
                        f"has {column}={value!r}"
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


def require_nonzero(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value == 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column} nonzero"
        )


def require_nonnegative(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value < 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column}>=0, got {value}"
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
    zero_columns_by_table = {
        "window_saturation.csv": ("coverage_defect_rank",),
        "liu_hn_window.csv": ("height_defect_rank",),
        "gram_map.csv": ("integrality_defect_rank", "formula_defect_rank"),
        "cocycle_identities.csv": (
            "delta_b_defect_rank",
            "polarization_defect_rank",
            "bilinearity_defect_rank",
        ),
        "normal_ordered_lifts.csv": (
            "additivity_defect_rank",
            "central_extension_defect_rank",
        ),
        "target_windows.csv": ("transition_compatibility_defect_rank",),
        "primitive_lifts.csv": ("lift_residual_rank",),
        "transitions.csv": (
            "r1lim_rank",
            "active_support_defect_rank",
            "saturation_defect_rank",
            "cocycle_defect_rank",
        ),
    }
    integer_columns_by_table = {
        "active_support.csv": ("n", "l", "m", "nm", "elliptic_l", "coefficient"),
        "window_saturation.csv": ("hn_height",),
        "liu_hn_window.csv": ("hn_height", "height_value"),
        "gram_map.csv": ("q_square_half", "qp_pairing", "p_square_half"),
        "cocycle_identities.csv": ("b_qq", "b_qp", "b_pp"),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        for column in integer_columns_by_table.get(table.spec.path, ()):
            parse_int(table, index, row, column, issues)

        if table.spec.path == "active_support.csv":
            require_nonzero(table, index, row, "coefficient", issues)
        elif table.spec.path == "window_saturation.csv":
            require_nonnegative(table, index, row, "hn_height", issues)
            require_bool_text(table, index, row, "difference_positive", "true", issues)
            require_bool_text(table, index, row, "downward_closed", "true", issues)
        elif table.spec.path == "liu_hn_window.csv":
            require_nonnegative(table, index, row, "hn_height", issues)
            require_nonnegative(table, index, row, "height_value", issues)
            require_bool_text(table, index, row, "retained_in_window", "true", issues)
        elif table.spec.path == "normal_ordered_lifts.csv":
            require_bool_text(table, index, row, "orbit_membership", "true", issues)
        elif table.spec.path == "target_windows.csv":
            require_bool_text(table, index, row, "image_membership", "true", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_charge_window", "true", issues)


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
        check_statuses(table, issues)
        check_payload(table, issues)
        check_provenance(table, issues)
        check_semantics(table, issues)
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite charge-window fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("charge_window_certification: false")
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
