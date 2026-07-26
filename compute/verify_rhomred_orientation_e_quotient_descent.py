#!/usr/bin/env python3
"""Verify the row-302 E-quotient orientation descent packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_e_quotient_descent_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_e_quotient_descent_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_E_QUOTIENT_DESCENT_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-e-quotient-descent"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_e_quotient_descent")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
ALPHA_NULL_FIXTURE = Path("certificates/orientation/rhomred_alpha_red_nullhomotopy")
FREE_E_NULL_FIXTURE = Path("certificates/orientation/rhomred_free_e_nulltrivialization")
FINITE_BETA_NULL_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta_nulltrivialization")
LINEARIZATION_VANISH_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_linearization_vanishing")
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
ALPHA_NULL_STATUS = "RHOMRED_ALPHA_RED_NULLHOMOTOPY_OBSTRUCTION_VERIFIED"
FREE_E_NULL_STATUS = "RHOMRED_FREE_E_NULLTRIVIALIZATION_OBSTRUCTION_VERIFIED"
FINITE_BETA_NULL_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_NULLTRIVIALIZATION_OBSTRUCTION_VERIFIED"
LINEARIZATION_VANISH_STATUS = "RHOMRED_FINITE_STABILIZER_LINEARIZATION_VANISHING_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "orientation_line_rows_supplied": 0,
    "quotient_borel_rows_supplied": 0,
    "finite_stabilizer_rows_supplied": 0,
    "alpha_red_nullhomotopy_claim": 0,
    "free_e_nulltrivialization_claim": 0,
    "finite_beta_nulltrivialization_claim": 0,
    "linearization_zero_claim": 0,
    "quotient_orientation_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "orientation_square_root",
    "alpha_red_nullhomotopy",
    "free_e_nulltrivialization",
    "finite_beta_nulltrivialization",
    "finite_linearization_zero",
    "subgroup_compatibility",
    "overlap_compatibility",
    "extension_flag_compatibility",
    "quotient_orientation_row",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "zero_class_only",
    "alpha_red_formula_only",
    "free_E_vanishing_only",
    "beta_vanishing_only",
    "missing_linearization_character",
    "cyclic_restrictions_only",
    "scalar_trace",
    "maass_character_value",
    "op_scalar_branch",
    "protected_integration",
}

REQUIRED_ORIENTATION_BLOCKED = {
    "orientation_square_root",
    "borel_reduced_gerbe",
    "borel_free_E",
    "borel_finite_stabilizer",
    "borel_linearization",
    "finite_edge_reduction",
    "finite_two_primary_quadratic",
    "finite_two_primary_linear",
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
            "orientation_square_root_required",
            "alpha_red_nulltrivialization_required",
            "free_e_nulltrivialization_required",
            "finite_beta_nulltrivialization_required",
            "linearization_zero_required",
            "subgroup_compatibility_required",
            "overlap_compatibility_required",
            "quotient_borel_row_required",
            "finite_stabilizer_row_required",
            "criterion_recorded",
            "e_quotient_descent_proved",
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
        "descent_obstruction_rows.csv",
        (
            "obstruction_id",
            "orientation_square_root_status",
            "alpha_red_nullhomotopy_status",
            "free_e_nulltrivialization_status",
            "finite_beta_nulltrivialization_status",
            "linearization_zero_status",
            "subgroup_compatibility_status",
            "quotient_borel_row_status",
            "finite_stabilizer_row_status",
            "e_quotient_descent_proved",
            "mathematical_certification",
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
            "e_quotient_status",
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

ORIENTATION_LINE_COLUMNS = (
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

FINITE_STABILIZER_COLUMNS = (
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
)

ORIENTATION_BLOCKED_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "cohomology_or_rank_payload",
    "why_required",
    "orientation_status",
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
        "orientation_obstruction_ledger_imported",
        "square_root_obstruction_imported",
        "alpha_red_nullhomotopy_imported",
        "free_e_nulltrivialization_imported",
        "finite_stabilizer_nulltrivialization_imported",
        "finite_stabilizer_linearization_vanishing_imported",
        "quotient_descent_criterion_recorded",
        "orientation_tables_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_square_roots_supplied",
        "alpha_red_nullhomotopies_supplied",
        "free_e_nulltrivializations_supplied",
        "finite_stabilizer_nulltrivializations_supplied",
        "linearization_zero_rows_supplied",
        "quotient_borel_rows_supplied",
        "finite_stabilizer_rows_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ORIENTATION_FIXTURE),
            str(SQUARE_ROOT_FIXTURE),
            str(ALPHA_NULL_FIXTURE),
            str(FREE_E_NULL_FIXTURE),
            str(FINITE_BETA_NULL_FIXTURE),
            str(LINEARIZATION_VANISH_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    orient_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(orient_manifest.get("obstruction_ledger_status"), ORIENTATION_LEDGER_STATUS, "orientation ledger")
    require_equal(orient_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orient_manifest.get("empty_blocked"), True, "orientation empty blocked")

    square_manifest = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square_manifest.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_equal(square_manifest.get("square_root_rows_supplied"), False, "square-root rows")

    alpha_manifest = read_json(ALPHA_NULL_FIXTURE / "manifest.json")
    require_equal(alpha_manifest.get("status"), ALPHA_NULL_STATUS, "alpha null status")
    require_equal(alpha_manifest.get("nullhomotopy_criterion_recorded"), True, "alpha criterion")
    require_equal(alpha_manifest.get("null_homotopies_supplied"), False, "alpha nullhomotopies")
    require_equal(alpha_manifest.get("quotient_orientation"), False, "alpha quotient orientation")

    free_manifest = read_json(FREE_E_NULL_FIXTURE / "manifest.json")
    require_equal(free_manifest.get("status"), FREE_E_NULL_STATUS, "free E null status")
    require_equal(free_manifest.get("nulltrivialization_criterion_recorded"), True, "free E criterion")
    require_equal(free_manifest.get("nulltrivializations_supplied"), False, "free E nulltriv")
    require_equal(free_manifest.get("quotient_orientation"), False, "free E quotient orientation")

    beta_manifest = read_json(FINITE_BETA_NULL_FIXTURE / "manifest.json")
    require_equal(beta_manifest.get("status"), FINITE_BETA_NULL_STATUS, "finite beta null status")
    require_equal(beta_manifest.get("nulltrivialization_criterion_recorded"), True, "beta criterion")
    require_equal(beta_manifest.get("beta_null_trivializations_supplied"), False, "beta nulltriv")
    require_equal(beta_manifest.get("linearization_rows_supplied"), False, "beta linearization")
    require_equal(beta_manifest.get("quotient_orientation"), False, "beta quotient orientation")

    lin_manifest = read_json(LINEARIZATION_VANISH_FIXTURE / "manifest.json")
    require_equal(lin_manifest.get("status"), LINEARIZATION_VANISH_STATUS, "linearization vanish status")
    require_equal(lin_manifest.get("linearization_vanishing_criterion_recorded"), True, "linearization criterion")
    require_equal(lin_manifest.get("lambda_zero_rows_supplied"), False, "lambda zero rows")
    require_equal(lin_manifest.get("quotient_orientation"), False, "linearization quotient orientation")

    orientation_rows = read_table_path(
        ORIENTATION_FIXTURE / "orientation_lines.csv",
        ORIENTATION_LINE_COLUMNS,
        allow_empty=True,
    )
    quotient_rows = read_table_path(
        ORIENTATION_FIXTURE / "quotient_borel.csv",
        QUOTIENT_BOREL_COLUMNS,
        allow_empty=True,
    )
    finite_rows = read_table_path(
        ORIENTATION_FIXTURE / "finite_stabilizers.csv",
        FINITE_STABILIZER_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(orientation_rows), 0, "orientation line row count")
    require_equal(len(quotient_rows), 0, "quotient Borel row count")
    require_equal(len(finite_rows), 0, "finite stabilizer row count")

    blocked_rows = read_table_path(
        ORIENTATION_FIXTURE / "blocked_obligations.csv",
        ORIENTATION_BLOCKED_COLUMNS,
    )
    blocked = rows_by(blocked_rows, "obligation_id", "orientation blocked obligations")
    missing = REQUIRED_ORIENTATION_BLOCKED - set(blocked)
    if missing:
        raise ValueError("orientation ledger missing required obligations: " + ", ".join(sorted(missing)))
    for obligation_id in REQUIRED_ORIENTATION_BLOCKED:
        row = blocked[obligation_id]
        require_equal(row["orientation_status"], "missing_open_obligation", f"{obligation_id} status")
        require_equal(row["check_status"], "verified", f"{obligation_id} check")

    return {
        "orientation_lines": len(orientation_rows),
        "quotient_borel": len(quotient_rows),
        "finite_stabilizers": len(finite_rows),
        "orientation_blocked": len(blocked_rows),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "orientation_obstruction_ledger",
            "rhomred_square_root",
            "alpha_red_nullhomotopy",
            "free_e_nulltrivialization",
            "finite_stabilizer_nulltrivialization",
            "finite_stabilizer_linearization_vanishing",
            "e_quotient_descent_criterion",
        },
        "source ids",
    )
    expected_status = {
        "orientation_obstruction_ledger": ORIENTATION_LEDGER_STATUS,
        "rhomred_square_root": SQUARE_ROOT_STATUS,
        "alpha_red_nullhomotopy": ALPHA_NULL_STATUS,
        "free_e_nulltrivialization": FREE_E_NULL_STATUS,
        "finite_stabilizer_nulltrivialization": FINITE_BETA_NULL_STATUS,
        "finite_stabilizer_linearization_vanishing": LINEARIZATION_VANISH_STATUS,
        "e_quotient_descent_criterion": "proved_criterion",
    }
    for source_id, status in expected_status.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"e_quotient_picard_groupoid_descent"}, "criterion ids")
    row = rows["e_quotient_picard_groupoid_descent"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "orientation_square_root_required",
        "alpha_red_nulltrivialization_required",
        "free_e_nulltrivialization_required",
        "finite_beta_nulltrivialization_required",
        "linearization_zero_required",
        "subgroup_compatibility_required",
        "overlap_compatibility_required",
        "quotient_borel_row_required",
        "finite_stabilizer_row_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "e_quotient_descent_proved"), False, "E quotient descent proved")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "orientation_lines": (counts["orientation_lines"], False),
        "quotient_borel": (counts["quotient_borel"], False),
        "finite_stabilizers": (counts["finite_stabilizers"], False),
        "orientation_blocked_obligations": (counts["orientation_blocked"], True),
        "alpha_red_nullhomotopy": (3, True),
        "free_e_nulltrivialization": (3, True),
        "finite_beta_nulltrivialization": (3, True),
    }
    require_equal(set(rows), set(expected), "inspected table ids")
    for table_id, (count, supplied) in expected.items():
        row = rows[table_id]
        check_verified(row, "inspected_orientation_tables.csv")
        require_equal(int_cell(row, "row_count"), count, f"{table_id} count")
        require_equal(bool_cell(row, "supplied"), supplied, f"{table_id} supplied")


def verify_descent_obstructions(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["descent_obstruction_rows.csv"], "obstruction_id", "descent rows")
    require_equal(set(rows), {"e_quotient_orientation_descent"}, "descent obstruction ids")
    row = rows["e_quotient_orientation_descent"]
    check_verified(row, "descent_obstruction_rows.csv")
    for key in (
        "orientation_square_root_status",
        "alpha_red_nullhomotopy_status",
        "free_e_nulltrivialization_status",
        "finite_beta_nulltrivialization_status",
        "linearization_zero_status",
        "subgroup_compatibility_status",
        "quotient_borel_row_status",
        "finite_stabilizer_row_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(bool_cell(row, "e_quotient_descent_proved"), False, "E quotient proved")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


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
        require_equal(row["e_quotient_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_inspected_tables(tables, counts)
    verify_descent_obstructions(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ORIENTATION_E_QUOTIENT_DESCENT_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
