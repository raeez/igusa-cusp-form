#!/usr/bin/env python3
"""Verify the row-290 gerbe/linearization independence firewall."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_gerbe_linearization_independence.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_gerbe_linearization_independence"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_GERBE_LINEARIZATION_INDEPENDENCE_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-gerbe-linearization-independence"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_gerbe_linearization_independence")
VANISHING_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_linearization_vanishing")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
VANISHING_STATUS = "RHOMRED_FINITE_STABILIZER_LINEARIZATION_VANISHING_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "degree_separation_count": 3,
    "counterexample_count": 2,
    "false_implication_claim_count": 0,
    "row289_lambda_vanishing_claim": 0,
    "current_retained_order_one_count": 3,
    "protected_integration_claim": 0,
}

REQUIRED_REMAINING = {
    "lambda_value",
    "lambda_vanishing",
    "quotient_borel_row",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "beta_zero_claim_only",
    "beta_vanishing_row",
    "beta_nulltrivialization",
    "missing_lambda_value",
    "residual_group_order_one",
    "determinant_anchor_translation_weight",
    "class_invariance",
    "cyclic_quadratic_restrictions",
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
        "degree_separation_rows.csv",
        (
            "separation_id",
            "group_type",
            "gerbe_group",
            "linearization_group",
            "gerbe_degree",
            "linearization_degree",
            "gerbe_basis",
            "linearization_basis",
            "independent_graded_pieces",
            "zero_gerbe_forces_zero_linearization",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "counterexample_rows.csv",
        (
            "counterexample_id",
            "group_type",
            "gerbe_coordinates",
            "lambda_coordinates",
            "gerbe_vanishing",
            "lambda_vanishing",
            "cyclic_linearization_values",
            "false_implication_witness",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "current_packet_firewall_rows.csv",
        (
            "firewall_check_id",
            "imported_packet",
            "imported_field_or_table",
            "imported_value",
            "required_value",
            "false_implication_claimed",
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
        "remaining_obligations.csv",
        (
            "obligation_id",
            "lane",
            "required_artifact",
            "required_table",
            "required_row_type",
            "mathematical_payload",
            "why_required",
            "independence_status",
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

VANISHING_ROW_COLUMNS = (
    "vanishing_id",
    "linearization_id",
    "nulltrivialization_id",
    "inertia_id",
    "substack_id",
    "residual_group_id",
    "residual_group_order",
    "h1_bh_template",
    "lambda_value",
    "lambda_character_computed",
    "zero_condition",
    "zero_coordinates_verified",
    "lambda_vanishing_verified",
    "finite_linearization_row_id",
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
        "linearization_vanishing_imported",
        "orientation_obstruction_ledger_imported",
        "degree_separation_proved",
        "klein_four_counterexample_recorded",
        "two_primary_counterexample_recorded",
        "trivial_or_odd_zero_target_recorded",
        "false_implication_excluded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "beta_vanishing_implies_lambda_vanishing",
        "nulltrivialization_implies_lambda_vanishing",
        "determinant_anchor_weight_implies_lambda_vanishing",
        "linearization_vanishing_verified",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(VANISHING_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    vanishing_manifest = read_json(VANISHING_FIXTURE / "manifest.json")
    require_equal(vanishing_manifest.get("status"), VANISHING_STATUS, "row 289 packet status")
    for key in (
        "lambda_values_supplied",
        "lambda_character_computed",
        "lambda_zero_rows_supplied",
        "all_retained_lambda_vanishing_verified",
        "beta_vanishing_implies_lambda_vanishing",
        "nulltrivialization_implies_lambda_vanishing",
    ):
        require_equal(vanishing_manifest.get(key), False, f"row 289 manifest {key}")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    vanishing_rows = read_table_path(
        VANISHING_FIXTURE / "linearization_vanishing_obstruction_rows.csv",
        VANISHING_ROW_COLUMNS,
    )
    require_equal(len(vanishing_rows), 3, "row 289 vanishing rows")
    for row in vanishing_rows:
        require_equal(int_cell(row, "residual_group_order"), 1, f"{row['vanishing_id']} order")
        require_equal(row["lambda_value"], "missing", f"{row['vanishing_id']} lambda value")
        require_equal(row["finite_linearization_row_id"], "missing", f"{row['vanishing_id']} finite row")
        for key in ("lambda_character_computed", "zero_coordinates_verified", "lambda_vanishing_verified"):
            require_equal(bool_cell(row, key), False, f"{row['vanishing_id']} {key}")
        require_equal(row["check_status"], "verified", f"{row['vanishing_id']} check")

    finite_rows = read_table_path(
        ORIENTATION_FIXTURE / "finite_stabilizers.csv",
        FINITE_STABILIZER_COLUMNS,
        allow_empty=True,
    )
    quotient_rows = read_table_path(
        ORIENTATION_FIXTURE / "quotient_borel.csv",
        QUOTIENT_BOREL_COLUMNS,
        allow_empty=True,
    )
    blocked_rows = read_table_path(
        ORIENTATION_FIXTURE / "blocked_obligations.csv",
        ORIENTATION_BLOCKED_COLUMNS,
    )
    require_equal(len(finite_rows), 0, "finite stabilizer rows")
    require_equal(len(quotient_rows), 0, "quotient Borel rows")
    require_equal(len(blocked_rows), 26, "orientation blocked obligations")


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "linearization_vanishing_packet",
            "orientation_obstruction_ledger",
            "klein_four_lemma",
            "two_primary_lemma",
            "translation_linearization_remark",
        },
        "source ids",
    )
    require_equal(rows["linearization_vanishing_packet"]["source_status"], VANISHING_STATUS, "row 289 source")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_degree_separation(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["degree_separation_rows.csv"], "separation_id", "degree separation rows")
    require_equal(
        set(rows),
        {"klein_four_degree_separation", "two_primary_degree_separation", "trivial_or_odd_zero_target"},
        "degree separation ids",
    )
    for row in rows.values():
        check_verified(row, "degree_separation_rows.csv")
        require_equal(int_cell(row, "gerbe_degree"), 2, f"{row['separation_id']} gerbe degree")
        require_equal(int_cell(row, "linearization_degree"), 1, f"{row['separation_id']} linearization degree")
        require_equal(bool_cell(row, "independent_graded_pieces"), True, f"{row['separation_id']} independent")
        require_equal(
            bool_cell(row, "zero_gerbe_forces_zero_linearization"),
            False,
            f"{row['separation_id']} implication",
        )


def verify_counterexamples(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["counterexample_rows.csv"], "counterexample_id", "counterexample rows")
    require_equal(
        set(rows),
        {
            "klein_four_beta_zero_lambda_nonzero",
            "two_primary_beta_zero_lambda_nonzero",
            "trivial_or_odd_no_counterexample",
        },
        "counterexample ids",
    )
    for counterexample_id in ("klein_four_beta_zero_lambda_nonzero", "two_primary_beta_zero_lambda_nonzero"):
        row = rows[counterexample_id]
        check_verified(row, "counterexample_rows.csv")
        require_equal(bool_cell(row, "gerbe_vanishing"), True, f"{counterexample_id} gerbe")
        require_equal(bool_cell(row, "lambda_vanishing"), False, f"{counterexample_id} lambda")
        require_equal(bool_cell(row, "false_implication_witness"), True, f"{counterexample_id} witness")
    trivial = rows["trivial_or_odd_no_counterexample"]
    check_verified(trivial, "counterexample_rows.csv")
    require_equal(bool_cell(trivial, "false_implication_witness"), False, "trivial witness")
    require_equal(bool_cell(trivial, "lambda_vanishing"), True, "trivial lambda target")


def verify_current_packet_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(
        tables["current_packet_firewall_rows.csv"],
        "firewall_check_id",
        "current packet firewall rows",
    )
    require_equal(
        set(rows),
        {
            "row289_beta_implication_field",
            "row289_null_implication_field",
            "row289_lambda_zero_field",
            "row289_vanishing_rows",
        },
        "current packet firewall ids",
    )
    for row in rows.values():
        check_verified(row, "current_packet_firewall_rows.csv")
        require_equal(row["imported_value"], row["required_value"], f"{row['firewall_check_id']} value")
        require_equal(bool_cell(row, "false_implication_claimed"), False, f"{row['firewall_check_id']} false")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "linearization_vanishing_obstruction_rows": (3, False),
        "finite_stabilizers": (0, False),
        "quotient_borel": (0, False),
        "orientation_blocked_obligations": (26, True),
    }
    require_equal(set(rows), set(expected), "inspected table ids")
    for table_id, (count, supplied) in expected.items():
        row = rows[table_id]
        check_verified(row, "inspected_orientation_tables.csv")
        require_equal(int_cell(row, "row_count"), count, f"{table_id} count")
        require_equal(bool_cell(row, "supplied"), supplied, f"{table_id} supplied")


def verify_coverage(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        check_verified(row, "coverage_rows.csv", proof_required=False)
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_remaining(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["remaining_obligations.csv"], "obligation_id", "remaining obligations")
    require_equal(set(rows), REQUIRED_REMAINING, "remaining obligations")
    for row in rows.values():
        check_verified(row, "remaining_obligations.csv", proof_required=False)
        require_equal(
            row["independence_status"],
            "remaining_open_obligation",
            f"{row['obligation_id']} status",
        )


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
    verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_degree_separation(tables)
    verify_counterexamples(tables)
    verify_current_packet_firewall(tables)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_GERBE_LINEARIZATION_INDEPENDENCE_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
