#!/usr/bin/env python3
"""Verify the row-295 Klein-four zero-restriction obstruction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_klein_four_zero_restrictions.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_klein_four_zero_restrictions"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_ZERO_RESTRICTIONS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-klein-four-zero-restrictions"
DEFAULT_FIXTURE = Path(
    "certificates/orientation/rhomred_finite_stabilizer_klein_four_zero_restrictions"
)
CLASS_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_class")
B20_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b20")
B11_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b11")
B02_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b02")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
CLASS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_CLASS_VERIFIED"
B20_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B20_VERIFIED"
B11_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B11_VERIFIED"
B02_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B02_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "zero_criterion_count": 1,
    "coefficient_identity_import_count": 3,
    "retained_zero_row_count": 0,
    "r_value_count": 0,
    "r_zero_verified_count": 0,
    "beta_vanishing_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_e2_edge_row",
    "cyclic_zero_restriction_rows",
    "r_values",
    "finite_beta_zero",
    "linearization_zero",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "missing_zero_rows",
    "missing_r_values",
    "beta_vanishing",
    "linearization_character",
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
        "zero_criterion_rows.csv",
        (
            "criterion_id",
            "class_formula",
            "restriction_values",
            "coefficient_identities",
            "zero_condition",
            "coefficient_zero_condition",
            "equivalence_verified",
            "zero_rows_supplied",
            "r_values_supplied",
            "beta_vanishing_claimed",
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
            "zero_status",
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

CLASS_ROW_COLUMNS = (
    "class_id",
    "group_id",
    "basis_id",
    "edge_reduction_required",
    "class_formula",
    "coefficient_names",
    "retained_edge_row_id",
    "equivariant_beta_representative_id",
    "coefficients_supplied",
    "local_class_form_verified",
    "proof_reference",
    "check_status",
    "notes",
)

B20_IDENTITY_COLUMNS = (
    "identity_id",
    "restriction_id",
    "class_formula",
    "restricted_class_formula",
    "cyclic_restriction_formula",
    "coefficient_identity",
    "identity_verified",
    "retained_restriction_row_id",
    "r_value_supplied",
    "coefficient_value_supplied",
    "proof_reference",
    "check_status",
    "notes",
)

B11_IDENTITY_COLUMNS = (
    "identity_id",
    "restriction_inputs",
    "class_formula",
    "second_restricted_class_formula",
    "diagonal_restricted_class_formula",
    "cyclic_restriction_formulas",
    "prior_identity",
    "auxiliary_identity",
    "coefficient_identity",
    "identity_verified",
    "retained_restriction_row_id",
    "r_values_supplied",
    "coefficient_value_supplied",
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
        "klein_four_class_imported",
        "coefficient_identities_imported",
        "zero_criterion_verified",
        "beta_zero_equivalence_verified",
        "missing_zero_rows_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_e2_edge_row_supplied",
        "cyclic_restriction_rows_supplied",
        "r_values_supplied",
        "r_values_zero_verified",
        "b_coefficients_zero_verified",
        "beta_vanishing_verified",
        "linearization_rows_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(CLASS_FIXTURE), str(B20_FIXTURE), str(B11_FIXTURE), str(B02_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    class_manifest = read_json(CLASS_FIXTURE / "manifest.json")
    require_equal(class_manifest.get("status"), CLASS_STATUS, "class packet status")
    require_equal(class_manifest.get("klein_four_class_form_recorded"), True, "class form")
    require_equal(class_manifest.get("retained_e2_edge_row_supplied"), False, "class edge row")
    require_equal(class_manifest.get("coefficient_values_supplied"), False, "class coefficients")

    b20_manifest = read_json(B20_FIXTURE / "manifest.json")
    require_equal(b20_manifest.get("status"), B20_STATUS, "b20 packet status")
    require_equal(b20_manifest.get("b20_identity_verified"), True, "b20 identity")
    require_equal(b20_manifest.get("r1_value_supplied"), False, "b20 r1 value")

    b11_manifest = read_json(B11_FIXTURE / "manifest.json")
    require_equal(b11_manifest.get("status"), B11_STATUS, "b11 packet status")
    require_equal(b11_manifest.get("b11_identity_verified"), True, "b11 identity")
    require_equal(b11_manifest.get("r_values_supplied"), False, "b11 r values")

    b02_manifest = read_json(B02_FIXTURE / "manifest.json")
    require_equal(b02_manifest.get("status"), B02_STATUS, "b02 packet status")
    require_equal(b02_manifest.get("b02_identity_verified"), True, "b02 identity")
    require_equal(b02_manifest.get("r2_value_supplied"), False, "b02 r2 value")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    class_rows = read_table_path(CLASS_FIXTURE / "klein_four_class_rows.csv", CLASS_ROW_COLUMNS)
    class_row = rows_by(class_rows, "class_id", "class rows")["beta_E2_edge_class"]
    require_equal(
        class_row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "class formula",
    )
    require_equal(bool_cell(class_row, "coefficients_supplied"), False, "class coefficients")
    require_equal(bool_cell(class_row, "local_class_form_verified"), True, "class form verified")

    b20_rows = read_table_path(B20_FIXTURE / "coefficient_identity_rows.csv", B20_IDENTITY_COLUMNS)
    b20_row = rows_by(b20_rows, "identity_id", "b20 rows")["b20_equals_r1"]
    require_equal(b20_row["coefficient_identity"], "b20_equals_r1", "b20 identity row")
    require_equal(bool_cell(b20_row, "identity_verified"), True, "b20 verified")
    require_equal(bool_cell(b20_row, "r_value_supplied"), False, "b20 r value")

    b11_rows = read_table_path(B11_FIXTURE / "coefficient_identity_rows.csv", B11_IDENTITY_COLUMNS)
    b11_row = rows_by(b11_rows, "identity_id", "b11 rows")["b11_equals_r1_plus_r2_plus_r3"]
    require_equal(b11_row["coefficient_identity"], "b11_equals_r1_plus_r2_plus_r3", "b11 identity row")
    require_equal(bool_cell(b11_row, "identity_verified"), True, "b11 verified")
    require_equal(bool_cell(b11_row, "r_values_supplied"), False, "b11 r values")

    b02_rows = read_table_path(B02_FIXTURE / "coefficient_identity_rows.csv", B20_IDENTITY_COLUMNS)
    b02_row = rows_by(b02_rows, "identity_id", "b02 rows")["b02_equals_r2"]
    require_equal(b02_row["coefficient_identity"], "b02_equals_r2", "b02 identity row")
    require_equal(bool_cell(b02_row, "identity_verified"), True, "b02 verified")
    require_equal(bool_cell(b02_row, "r_value_supplied"), False, "b02 r value")

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
            "klein_four_class_packet",
            "klein_four_b20_packet",
            "klein_four_b11_packet",
            "klein_four_b02_packet",
            "orientation_obstruction_ledger",
            "row295_local_criterion",
        },
        "source ids",
    )
    expected_status = {
        "klein_four_class_packet": CLASS_STATUS,
        "klein_four_b20_packet": B20_STATUS,
        "klein_four_b11_packet": B11_STATUS,
        "klein_four_b02_packet": B02_STATUS,
        "orientation_obstruction_ledger": ORIENTATION_LEDGER_STATUS,
        "row295_local_criterion": "proved",
    }
    for source_id, status in expected_status.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_zero_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["zero_criterion_rows.csv"], "criterion_id", "zero criterion")
    require_equal(set(rows), {"klein_four_zero_restrictions"}, "criterion ids")
    row = rows["klein_four_zero_restrictions"]
    check_verified(row, "zero_criterion_rows.csv")
    require_equal(
        row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "class formula",
    )
    require_equal(row["restriction_values"], "r1_r2_r3", "restriction values")
    require_equal(
        row["coefficient_identities"],
        "b20_equals_r1__b02_equals_r2__b11_equals_r1_plus_r2_plus_r3",
        "coefficient identities",
    )
    require_equal(row["zero_condition"], "r1_equals_r2_equals_r3_equals_0", "zero condition")
    require_equal(
        row["coefficient_zero_condition"],
        "b20_equals_b11_equals_b02_equals_0",
        "coefficient zero",
    )
    require_equal(bool_cell(row, "equivalence_verified"), True, "equivalence")
    require_equal(bool_cell(row, "zero_rows_supplied"), False, "zero rows supplied")
    require_equal(bool_cell(row, "r_values_supplied"), False, "r values supplied")
    require_equal(bool_cell(row, "beta_vanishing_claimed"), False, "beta vanishing claimed")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "klein_four_class_rows": (1, True),
        "b20_identity_rows": (1, True),
        "b11_identity_rows": (1, True),
        "b02_identity_rows": (1, True),
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
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "remaining obligations")
    for row in rows.values():
        check_verified(row, "remaining_obligations.csv", proof_required=False)
        require_equal(row["zero_status"], "remaining_open_obligation", f"{row['obligation_id']} status")


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
    verify_zero_criterion(tables)
    verify_inspected(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_ZERO_RESTRICTIONS_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
