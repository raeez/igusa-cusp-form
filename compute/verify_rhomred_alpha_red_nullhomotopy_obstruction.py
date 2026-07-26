#!/usr/bin/env python3
"""Verify the row-281 alpha_red null-homotopy obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_alpha_red_nullhomotopy_obstruction.v1"
EXPECTED_KIND = "rhomred_alpha_red_nullhomotopy_obstruction"
SUCCESS_STATUS = "RHOMRED_ALPHA_RED_NULLHOMOTOPY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:alpha-red-nullhomotopy-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_alpha_red_nullhomotopy")
ALPHA_FIXTURE = Path("certificates/orientation/rhomred_alpha_red")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
ALPHA_STATUS = "RHOMRED_ALPHA_RED_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_ROWS = {
    "null_alpha_red_R0_s3": ("alpha_red_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "null_alpha_red_R0_s2": ("alpha_red_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "null_alpha_red_R0_s1": ("alpha_red_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}

EXPECTED_COVERAGE = {
    "retained_strata_count": 3,
    "criterion_count": 2,
    "alpha_red_cocycle_count": 0,
    "alpha_red_zero_count": 0,
    "one_cochain_count": 0,
    "coboundary_defect_zero_count": 0,
    "nullhomotopy_claim": 0,
    "quotient_orientation_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "alpha_red_cocycle",
    "alpha_red_zero_class",
    "one_cochain",
    "coboundary_equation",
    "quotient_borel_row",
    "torsor_choice",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "alpha_red_formula_only",
    "alpha_red_zero_claim_only",
    "empty_quotient_borel_table",
    "scalar_trace",
    "maass_character_value",
    "op_scalar_branch",
    "protected_integration",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


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
            "cocycle_representative_required",
            "zero_class_required",
            "one_cochain_required",
            "coboundary_equation_required",
            "choices_torsor",
            "quotient_orientation_supplied",
            "nullhomotopy_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "nullhomotopy_obstruction_rows.csv",
        (
            "nullhomotopy_id",
            "alpha_red_id",
            "substack_id",
            "derived_stack_id",
            "alpha_red_cocycle_id",
            "alpha_red_value",
            "alpha_red_zero_verified",
            "one_cochain_id",
            "coboundary_equation_id",
            "coboundary_defect_rank_zero",
            "nullhomotopy_supplied",
            "quotient_borel_row_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "inspected_orientation_tables.csv",
        (
            "table_id",
            "table_path",
            "row_count",
            "required_payload",
            "supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
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
            "nullhomotopy_status",
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

ALPHA_COLUMNS = (
    "alpha_red_id",
    "substack_id",
    "derived_stack_id",
    "determinant_w2_id",
    "determinant_w2_value",
    "cokernel_row_id",
    "cokernel_rank_zero",
    "cokernel_w2_id",
    "cokernel_w2_value",
    "cosection_pullback_row_id",
    "alpha_red_value",
    "alpha_red_computed",
    "alpha_red_vanishing_verified",
    "null_homotopy_supplied",
    "proof_reference",
    "check_status",
    "notes",
)

QUOTIENT_BOREL_COLUMNS = (
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
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_table_path(
    path: Path,
    columns: tuple[str, ...],
    *,
    allow_empty: bool = False,
) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows and not allow_empty:
        raise ValueError(f"{path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{path}: unparsed CSV fields in row {row}")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "alpha_red_obstruction_imported",
        "orientation_obstruction_ledger_imported",
        "nullhomotopy_criterion_recorded",
        "three_retained_strata_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "alpha_red_cocycles_supplied",
        "alpha_red_zero_class_supplied",
        "one_cochains_supplied",
        "coboundary_defect_zero",
        "null_homotopies_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(ALPHA_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    alpha_manifest = read_json(ALPHA_FIXTURE / "manifest.json")
    require_equal(alpha_manifest.get("status"), ALPHA_STATUS, "alpha-red status")
    require_equal(alpha_manifest.get("alpha_red_vanishing_verified"), False, "alpha-red vanishing")
    require_equal(alpha_manifest.get("null_homotopy_supplied"), False, "alpha-red null")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    alpha_rows = read_table_path(ALPHA_FIXTURE / "alpha_red_obstruction_rows.csv", ALPHA_COLUMNS)
    indexed = rows_by(alpha_rows, "alpha_red_id", "imported alpha-red rows")
    for row in indexed.values():
        require_equal(row["alpha_red_value"], "missing", f"{row['alpha_red_id']} value")
        require_equal(bool_cell(row, "alpha_red_computed"), False, f"{row['alpha_red_id']} computed")
        require_equal(bool_cell(row, "alpha_red_vanishing_verified"), False, f"{row['alpha_red_id']} vanishing")
        require_equal(bool_cell(row, "null_homotopy_supplied"), False, f"{row['alpha_red_id']} null")

    quotient_rows = read_table_path(
        ORIENTATION_FIXTURE / "quotient_borel.csv",
        QUOTIENT_BOREL_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(quotient_rows), 0, "quotient Borel rows")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {"rhomred_alpha_red", "orientation_obstruction_ledger", "nullhomotopy_definition"},
        "source ids",
    )
    require_equal(rows["rhomred_alpha_red"]["source_status"], ALPHA_STATUS, "alpha source status")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source status",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criteria(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"cech_borel_nullhomotopy", "zero_class_not_enough"}, "criterion ids")
    for row in rows.values():
        check_verified(row, "criterion_rows.csv")
        for key in (
            "cocycle_representative_required",
            "zero_class_required",
            "one_cochain_required",
            "coboundary_equation_required",
        ):
            require_equal(bool_cell(row, key), True, f"{row['criterion_id']} {key}")
        require_equal(row["choices_torsor"], "H1_F2", f"{row['criterion_id']} torsor")
        require_equal(bool_cell(row, "quotient_orientation_supplied"), False, f"{row['criterion_id']} quotient")
        require_equal(bool_cell(row, "nullhomotopy_supplied"), False, f"{row['criterion_id']} null")


def verify_obstruction_rows(
    tables: dict[str, list[dict[str, str]]],
    alpha_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["nullhomotopy_obstruction_rows.csv"], "nullhomotopy_id", "null rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "nullhomotopy ids")
    for null_id, (alpha_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[null_id]
        alpha_row = alpha_rows[alpha_id]
        check_verified(row, "nullhomotopy_obstruction_rows.csv")
        require_equal(row["alpha_red_id"], alpha_id, f"{null_id} alpha id")
        require_equal(row["substack_id"], substack_id, f"{null_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{null_id} derived")
        require_equal(alpha_row["substack_id"], substack_id, f"{alpha_id} imported substack")
        for key in (
            "alpha_red_cocycle_id",
            "alpha_red_value",
            "one_cochain_id",
            "coboundary_equation_id",
            "quotient_borel_row_id",
        ):
            require_equal(row[key], "missing", f"{null_id} {key}")
        require_equal(bool_cell(row, "alpha_red_zero_verified"), False, f"{null_id} zero")
        require_equal(bool_cell(row, "coboundary_defect_rank_zero"), False, f"{null_id} defect")
        require_equal(bool_cell(row, "nullhomotopy_supplied"), False, f"{null_id} supplied")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(
        set(rows),
        {
            "quotient_borel",
            "alpha_red_obstruction_rows",
            "alpha_red_blocked_obligations",
            "orientation_manifest",
        },
        "inspected ids",
    )
    require_equal(int_cell(rows["quotient_borel"], "row_count"), 0, "quotient count")
    require_equal(bool_cell(rows["quotient_borel"], "supplied"), False, "quotient supplied")
    require_equal(int_cell(rows["alpha_red_obstruction_rows"], "row_count"), 3, "alpha rows")
    require_equal(bool_cell(rows["alpha_red_obstruction_rows"], "supplied"), False, "alpha supplied")
    require_equal(int_cell(rows["alpha_red_blocked_obligations"], "row_count"), 11, "blocked rows")
    require_equal(bool_cell(rows["alpha_red_blocked_obligations"], "supplied"), True, "blocked supplied")
    require_equal(bool_cell(rows["orientation_manifest"], "supplied"), True, "manifest supplied")
    for row in rows.values():
        check_verified(row, "inspected_orientation_tables.csv")


def verify_coverage(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        check_verified(row, "coverage_rows.csv", proof_required=False)
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        require_equal(row["nullhomotopy_status"], "missing_open_obligation", f"{row['obligation_id']} status")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        check_verified(row, "scalar_firewall.csv")
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def verify_fixture(fixture: Path) -> None:
    if not fixture.is_dir():
        raise ValueError(f"fixture is not a directory: {fixture}")
    verify_manifest(fixture)
    alpha_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criteria(tables)
    verify_obstruction_rows(tables, alpha_rows)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ALPHA_RED_NULLHOMOTOPY_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
