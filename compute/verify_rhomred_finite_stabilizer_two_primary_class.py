#!/usr/bin/env python3
"""Verify the row-296 even two-primary class packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_two_primary_class.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_two_primary_class"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_TWO_PRIMARY_CLASS_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-two-primary-class"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_two_primary_class")
BETA_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
BETA_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "cohomology_basis_count": 1,
    "two_primary_class_form_count": 1,
    "deferred_detection_count": 2,
    "retained_two_primary_edge_row_count": 0,
    "coefficient_value_count": 0,
    "cyclic_detection_claim": 0,
    "beta_vanishing_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_two_primary_edge_row",
    "equivariant_beta_representative",
    "edge_reduction",
    "coefficient_values",
    "mixed_term_detection",
    "beta_vanishing",
    "zero_linearization",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "residual_group_type_only",
    "missing_edge_row",
    "missing_coefficients",
    "cyclic_restrictions_only",
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
        "cohomology_basis_rows.csv",
        (
            "basis_id",
            "group_id",
            "group_isomorphism",
            "cohomology_ring",
            "generator_degrees",
            "h2_basis",
            "h2_dimension",
            "ordered_basis_verified",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "two_primary_class_rows.csv",
        (
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
        ),
    ),
    TableSpec(
        "deferred_detection_rows.csv",
        (
            "deferred_id",
            "row_number",
            "detection_payload",
            "deferred",
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
            "two_primary_status",
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

BETA_TEMPLATE_COLUMNS = (
    "template_id",
    "stabilizer_type",
    "group_order_condition",
    "two_primary_rank",
    "cohomology_basis",
    "beta_form",
    "coefficient_rows_required",
    "edge_reduction_required",
    "cyclic_restrictions_determine_quadratic",
    "cyclic_only_orientation_row",
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
        "finite_stabilizer_beta_imported",
        "orientation_obstruction_ledger_imported",
        "two_primary_group_identified",
        "cohomology_ring_computed",
        "h2_basis_recorded",
        "two_primary_class_form_recorded",
        "mixed_term_detection_deferred_to_row_297",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_two_primary_edge_row_supplied",
        "equivariant_beta_representative_supplied",
        "edge_reduction_rows_supplied",
        "coefficient_values_supplied",
        "cyclic_restriction_detection_supplied",
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
        {str(BETA_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    beta_manifest = read_json(BETA_FIXTURE / "manifest.json")
    require_equal(beta_manifest.get("status"), BETA_STATUS, "beta packet status")
    require_equal(beta_manifest.get("group_cohomology_templates_recorded"), True, "beta templates")
    require_equal(beta_manifest.get("beta_coefficients_supplied"), False, "beta coefficients")
    require_equal(beta_manifest.get("beta_class_values_computed"), False, "beta computed")
    require_equal(beta_manifest.get("beta_vanishing_verified"), False, "beta vanishing")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    templates = read_table_path(BETA_FIXTURE / "template_rows.csv", BETA_TEMPLATE_COLUMNS)
    templates_by_id = rows_by(templates, "template_id", "beta templates")
    row = templates_by_id["two_primary_rank_two"]
    require_equal(row["stabilizer_type"], "E2a_rank_two", "two-primary stabilizer")
    require_equal(row["group_order_condition"], "order_power_of_two_rank_two", "two-primary order")
    require_equal(int_cell(row, "two_primary_rank"), 2, "two-primary rank")
    require_equal(row["cohomology_basis"], "y1_x1x2_y2", "two-primary basis")
    require_equal(
        row["beta_form"],
        "A1_y1_plus_A12_x1x2_plus_A2_y2",
        "two-primary beta form",
    )
    require_equal(row["coefficient_rows_required"], "A1_A12_A2", "two-primary coefficients")
    require_equal(bool_cell(row, "edge_reduction_required"), True, "two-primary edge")
    require_equal(
        bool_cell(row, "cyclic_restrictions_determine_quadratic"),
        False,
        "two-primary cyclic detection",
    )
    require_equal(bool_cell(row, "cyclic_only_orientation_row"), False, "two-primary cyclic-only")
    require_equal(row["check_status"], "verified", "two-primary template check")

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
            "finite_stabilizer_beta_packet",
            "orientation_obstruction_ledger",
            "two_primary_lemma",
            "finite_stabilizer_e_descent",
        },
        "source ids",
    )
    require_equal(rows["finite_stabilizer_beta_packet"]["source_status"], BETA_STATUS, "beta source")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source",
    )
    require_equal(rows["two_primary_lemma"]["source_status"], "proved", "two-primary lemma")
    require_equal(rows["finite_stabilizer_e_descent"]["source_status"], "proved", "setup lemma")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_basis(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["cohomology_basis_rows.csv"], "basis_id", "basis rows")
    require_equal(set(rows), {"BZ2a_square_mod2_basis"}, "basis ids")
    row = rows["BZ2a_square_mod2_basis"]
    check_verified(row, "cohomology_basis_rows.csv")
    require_equal(row["group_id"], "Z2a_square", "basis group")
    require_equal(row["group_isomorphism"], "a_ge_2", "basis group condition")
    require_equal(row["cohomology_ring"], "Lambda_x1_x2_tensor_F2_y1_y2", "basis ring")
    require_equal(
        row["generator_degrees"],
        "deg_x1_equals_1_deg_x2_equals_1_deg_y1_equals_2_deg_y2_equals_2",
        "basis degrees",
    )
    require_equal(row["h2_basis"], "y1_x1x2_y2", "basis h2")
    require_equal(int_cell(row, "h2_dimension"), 3, "h2 dimension")
    require_equal(bool_cell(row, "ordered_basis_verified"), True, "ordered basis")


def verify_class_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["two_primary_class_rows.csv"], "class_id", "class rows")
    require_equal(set(rows), {"beta_two_primary_edge_class"}, "class ids")
    row = rows["beta_two_primary_edge_class"]
    check_verified(row, "two_primary_class_rows.csv")
    require_equal(row["group_id"], "Z2a_square", "class group")
    require_equal(row["basis_id"], "BZ2a_square_mod2_basis", "class basis")
    require_equal(bool_cell(row, "edge_reduction_required"), True, "edge required")
    require_equal(
        row["class_formula"],
        "A1_y1_plus_A12_x1x2_plus_A2_y2",
        "class formula",
    )
    require_equal(row["coefficient_names"], "A1_A12_A2", "coefficient names")
    require_equal(row["retained_edge_row_id"], "missing", "edge row")
    require_equal(row["equivariant_beta_representative_id"], "missing", "beta representative")
    require_equal(bool_cell(row, "coefficients_supplied"), False, "coefficients supplied")
    require_equal(bool_cell(row, "local_class_form_verified"), True, "class form verified")


def verify_deferred(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["deferred_detection_rows.csv"], "deferred_id", "deferred rows")
    expected = {
        "mixed_term_detection": ("row_297", "A12_not_detected_by_cyclic_restrictions"),
        "coefficient_vanishing": ("row_286", "A1_A12_A2_equal_zero"),
    }
    require_equal(set(rows), set(expected), "deferred ids")
    for deferred_id, (row_number, payload) in expected.items():
        row = rows[deferred_id]
        require_equal(row["row_number"], row_number, f"{deferred_id} row")
        require_equal(row["detection_payload"], payload, f"{deferred_id} payload")
        require_equal(bool_cell(row, "deferred"), True, f"{deferred_id} deferred")
        require_equal(row["check_status"], "verified", f"{deferred_id} check")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "row285_template_rows": (3, True),
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
        require_equal(
            row["two_primary_status"],
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
    verify_basis(tables)
    verify_class_rows(tables)
    verify_deferred(tables)
    verify_inspected(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_TWO_PRIMARY_CLASS_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
