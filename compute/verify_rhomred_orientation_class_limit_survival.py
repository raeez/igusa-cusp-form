#!/usr/bin/env python3
"""Verify row-339 orientation-class inverse-limit survival packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_class_limit_survival_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_class_limit_survival_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_CLASS_LIMIT_SURVIVAL_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-class-inverse-limit-survival"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_class_limit_survival")

REDUCED_ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")
ROW338_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_pairing_nondegeneracy")

REDUCED_ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"
ROW338_STATUS = "RHOMRED_ORIENTATION_CY3_PAIRING_NONDEGENERACY_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "reduced_orientation_line_rows": 0,
    "reduced_orientation_transition_rows": 0,
    "square_root_obstruction_rows": 3,
    "square_root_constructed_rows": 0,
    "orientation_transition_rows": 0,
    "transition_defect_rows": 0,
    "null_trivialization_transport_rows": 0,
    "multiplicative_weyl_transport_rows": 0,
    "row338_orientation_limit_claim": 0,
    "limit_survival_rows": 0,
    "row340_no_new_class_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "finite_orientation_line_rows",
    "square_root_rows",
    "orientation_class_zero_rows",
    "picard_transition_rows",
    "determinant_square_transition_rows",
    "quotient_orientation_transition_rows",
    "thom_sebastiani_transition_rows",
    "weyl_coxeter_transition_rows",
    "strict_picard_composition",
    "orientation_mittag_leffler",
    "limit_class_row",
    "row338_not_survival",
    "row340_no_new_class",
}

REQUIRED_FIREWALL = {
    "reduced_orientation_empty_ledger",
    "square_root_obstruction_only",
    "transition_orientation_obstruction_only",
    "row338_CY3_pairing_nondegeneracy",
    "scalar_trace",
    "squared_determinant",
    "op_scalar_branch",
    "maass_character_value",
    "pfaffian_product",
    "target_root_window",
    "row340_no_new_class_claim",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]
    allow_empty: bool = False


TABLE_SPECS = (
    TableSpec(
        "source_rows.csv",
        (
            "source_id",
            "source_kind",
            "source_path_or_key",
            "source_status",
            "input_payload",
            "output_payload",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "criterion_rows.csv",
        (
            "criterion_id",
            "finite_orientation_lines_required",
            "square_root_required",
            "orientation_class_zero_required",
            "picard_transition_required",
            "determinant_square_transition_required",
            "quotient_orientation_transition_required",
            "thom_sebastiani_transition_required",
            "weyl_coxeter_transition_required",
            "strict_composition_required",
            "orientation_mittag_leffler_required",
            "limit_class_row_required",
            "row340_no_new_class_separate",
            "reduced_orientation_ledger_as_survival_allowed",
            "square_root_obstruction_as_survival_allowed",
            "transition_orientation_ledger_as_survival_allowed",
            "criterion_recorded",
            "survival_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "limit_survival_rows.csv",
        (
            "limit_survival_row_id",
            "cofinal_system_id",
            "orientation_tower_id",
            "finite_orientation_line_rows_id",
            "square_root_rows_id",
            "orientation_class_zero_rows_id",
            "picard_transition_rows_id",
            "strict_composition_row_id",
            "orientation_ml_row_id",
            "r1lim_rank",
            "limit_class_id",
            "projection_defect_rank",
            "survival_verified",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "coverage_rows.csv",
        (
            "coverage_id",
            "claim_kind",
            "computed_value",
            "expected_value",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "blocked_obligations.csv",
        (
            "obligation_id",
            "lane",
            "required_artifact",
            "required_table",
            "required_row_type",
            "mathematical_payload",
            "why_required",
            "compatibility_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        (
            "firewall_id",
            "forbidden_substitute",
            "excluded",
            "defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"json root is not an object: {path}")
    return value


def read_table_path(
    path: Path,
    columns: tuple[str, ...] | None = None,
    *,
    allow_empty: bool = False,
) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if columns is not None and tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = []
        for row in reader:
            normalized = {
                key: (value or "").strip()
                for key, value in row.items()
                if key is not None
            }
            if any(normalized.values()):
                rows.append(normalized)
    if not rows and not allow_empty:
        raise ValueError(f"{path}: expected at least one row")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns, allow_empty=spec.allow_empty)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_true(value: object, label: str) -> None:
    require_equal(value, True, label)


def require_false(value: object, label: str) -> None:
    require_equal(value, False, label)


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"{key}: expected integer cell, got {row.get(key)!r}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row.get(key)
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key}: expected boolean cell, got {value!r}")


def require_table_empty(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    if rows:
        raise ValueError(f"{path}: expected no source rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")

    for key in (
        "reduced_orientation_ledger_imported",
        "square_root_obstruction_imported",
        "transition_orientation_ledger_imported",
        "cy3_pairing_nondegeneracy_imported",
        "limit_survival_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "finite_orientation_line_rows_supplied",
        "square_root_rows_supplied",
        "orientation_class_zero_rows_supplied",
        "picard_transition_rows_supplied",
        "determinant_square_transition_rows_supplied",
        "quotient_orientation_transition_rows_supplied",
        "thom_sebastiani_transition_rows_supplied",
        "weyl_coxeter_transition_rows_supplied",
        "strict_composition_rows_supplied",
        "orientation_mittag_leffler_rows_supplied",
        "limit_class_rows_supplied",
        "orientation_class_survival_proved",
        "row340_no_new_class_claimed",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(
        set(manifest.get("tables", [])),
        {spec.path for spec in TABLE_SPECS},
        "manifest tables",
    )
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(REDUCED_ORIENTATION_FIXTURE),
            str(SQUARE_ROOT_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
            str(ROW338_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion_rows count")
    row = criterion[0]
    for key in (
        "finite_orientation_lines_required",
        "square_root_required",
        "orientation_class_zero_required",
        "picard_transition_required",
        "determinant_square_transition_required",
        "quotient_orientation_transition_required",
        "thom_sebastiani_transition_required",
        "weyl_coxeter_transition_required",
        "strict_composition_required",
        "orientation_mittag_leffler_required",
        "limit_class_row_required",
        "row340_no_new_class_separate",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "reduced_orientation_ledger_as_survival_allowed",
        "square_root_obstruction_as_survival_allowed",
        "transition_orientation_ledger_as_survival_allowed",
        "survival_proved",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-339 proposition")

    require_equal(len(tables["limit_survival_rows.csv"]), 0, "limit_survival_rows count")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        crow = coverage[coverage_id]
        require_equal(int_cell(crow, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(crow, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(crow, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(crow.get("check_status"), "verified", f"{coverage_id} status")

    obligations = {row["obligation_id"]: row for row in tables["blocked_obligations.csv"]}
    require_equal(set(obligations), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, orow in obligations.items():
        require_equal(orow.get("compatibility_status"), "missing_open_obligation", obligation_id)
        require_equal(orow.get("check_status"), "verified", f"{obligation_id} status")
        if PROOF_LABEL not in orow.get("proof_reference", ""):
            raise ValueError(f"{obligation_id}: proof reference does not point to proposition")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, frow in firewall.items():
        require_equal(frow.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(frow, "defect_rank"), 0, f"{substitute} defect")
        require_equal(frow.get("check_status"), "verified", f"{substitute} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{substitute}: proof reference does not point to proposition")


def check_imports() -> None:
    reduced = read_json(REDUCED_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        reduced.get("obstruction_ledger_status"),
        REDUCED_ORIENTATION_STATUS,
        "reduced orientation status",
    )
    require_false(reduced.get("orientation_certification"), "reduced orientation certification")
    require_false(reduced.get("mathematical_certification"), "reduced orientation mathematical certification")
    for rel_path in (
        "orientation_lines.csv",
        "transitions.csv",
        "ts_multiplicativity.csv",
        "quotient_borel.csv",
        "weyl_lifts.csv",
        "coxeter_cocycles.csv",
    ):
        require_table_empty(REDUCED_ORIENTATION_FIXTURE / rel_path)

    square = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_false(square.get("square_root_rows_supplied"), "square-root rows supplied")
    require_false(square.get("orientation_class_zero"), "square-root orientation class zero")
    require_false(square.get("transition_compatibility"), "square-root transition compatibility")
    rows = read_table_path(SQUARE_ROOT_FIXTURE / "square_root_obstruction_rows.csv")
    require_equal(len(rows), 3, "square-root obstruction rows")
    for row in rows:
        require_false(bool_cell(row, "square_root_supplied"), f"{row['obstruction_id']} square root")
        require_false(bool_cell(row, "orientation_class_zero"), f"{row['obstruction_id']} class zero")

    transition = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(transition.get("status"), TRANSITION_ORIENTATION_STATUS, "transition orientation status")
    require_false(transition.get("orientation_transition_certification"), "transition orientation certification")
    require_false(transition.get("mathematical_certification"), "transition orientation mathematical certification")
    for rel_path in (
        "orientation_transition_maps.csv",
        "null_trivialization_transport.csv",
        "multiplicative_weyl_transport.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANSITION_ORIENTATION_FIXTURE / rel_path)

    row338 = read_json(ROW338_FIXTURE / "manifest.json")
    require_equal(row338.get("status"), ROW338_STATUS, "row338 status")
    require_false(row338.get("inverse_limit_nondegeneracy_rows_supplied"), "row338 inverse limit rows")
    require_false(row338.get("row339_orientation_limit_claimed"), "row338 row339 claim")
    require_false(row338.get("cy3_pairing_nondegeneracy_proved"), "row338 proof")


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
    return SUCCESS_STATUS


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        status = verify(args.fixture)
    except Exception as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
