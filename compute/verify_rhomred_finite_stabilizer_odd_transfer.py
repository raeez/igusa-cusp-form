#!/usr/bin/env python3
"""Verify the row-298 odd-order transfer packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_odd_transfer.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_odd_transfer"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_ODD_TRANSFER_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-odd-transfer"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_odd_transfer")
BETA_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta")
BETA_VANISHING_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta_vanishing")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
BETA_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_OBSTRUCTION_VERIFIED"
BETA_VANISHING_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_VANISHING_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "transfer_count": 1,
    "template_import_count": 2,
    "retained_odd_edge_row_count": 0,
    "all_retained_coverage_count": 0,
    "null_trivialization_claim": 0,
    "quotient_orientation_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_odd_edge_row",
    "equivariant_beta_representative",
    "edge_reduction",
    "all_retained_h_coverage",
    "beta_null_trivialization",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "missing_edge_row",
    "missing_all_retained_coverage",
    "beta_representative",
    "null_trivialization",
    "even_stabilizer_cases",
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
        "transfer_rows.csv",
        (
            "transfer_id",
            "group_condition",
            "coefficient_ring",
            "order_invertible",
            "positive_degree_cohomology",
            "degree_two_beta_target",
            "degree_one_linearization_target",
            "edge_reduction_required",
            "transfer_verified",
            "retained_edge_row_supplied",
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
            "odd_transfer_status",
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

BETA_VANISHING_CRITERION_COLUMNS = (
    "criterion_id",
    "beta_value_required",
    "edge_reduction_required",
    "coordinate_payload",
    "zero_condition",
    "all_retained_h_required",
    "linearization_required_for_row286",
    "nulltrivialization_required_for_row286",
    "vanishing_supplied",
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
        "beta_vanishing_obstruction_imported",
        "orientation_obstruction_ledger_imported",
        "odd_order_transfer_verified",
        "positive_degree_group_cohomology_zero",
        "edge_target_beta_zero",
        "edge_target_linearization_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_odd_edge_row_supplied",
        "equivariant_beta_representative_supplied",
        "edge_reduction_rows_supplied",
        "all_retained_coverage_supplied",
        "beta_null_trivializations_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(BETA_FIXTURE), str(BETA_VANISHING_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    beta_manifest = read_json(BETA_FIXTURE / "manifest.json")
    require_equal(beta_manifest.get("status"), BETA_STATUS, "beta packet status")
    require_equal(beta_manifest.get("group_cohomology_templates_recorded"), True, "beta templates")
    require_equal(beta_manifest.get("edge_reduction_rows_supplied"), False, "beta edge rows")
    require_equal(beta_manifest.get("beta_class_values_computed"), False, "beta computed")

    vanishing_manifest = read_json(BETA_VANISHING_FIXTURE / "manifest.json")
    require_equal(
        vanishing_manifest.get("status"),
        BETA_VANISHING_STATUS,
        "beta vanishing packet status",
    )
    require_equal(vanishing_manifest.get("vanishing_criterion_recorded"), True, "vanishing criterion")
    require_equal(vanishing_manifest.get("beta_zero_rows_supplied"), False, "beta zero rows")
    require_equal(
        vanishing_manifest.get("all_retained_beta_vanishing_verified"),
        False,
        "all retained beta vanishing",
    )

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    templates = read_table_path(BETA_FIXTURE / "template_rows.csv", BETA_TEMPLATE_COLUMNS)
    odd_template = rows_by(templates, "template_id", "beta templates")["odd_or_trivial"]
    require_equal(odd_template["cohomology_basis"], "H2_BH_F2_zero", "odd cohomology")
    require_equal(odd_template["beta_form"], "beta_equals_zero_after_edge_reduction", "odd beta")
    require_equal(bool_cell(odd_template, "edge_reduction_required"), True, "odd edge")
    require_equal(bool_cell(odd_template, "cyclic_only_orientation_row"), False, "odd cyclic-only")
    require_equal(odd_template["check_status"], "verified", "odd template check")

    criteria = read_table_path(
        BETA_VANISHING_FIXTURE / "criterion_rows.csv",
        BETA_VANISHING_CRITERION_COLUMNS,
    )
    odd_criterion = rows_by(criteria, "criterion_id", "vanishing criteria")["odd_or_trivial_zero"]
    require_equal(odd_criterion["coordinate_payload"], "H2_BH_F2_zero", "odd criterion payload")
    require_equal(
        odd_criterion["zero_condition"],
        "H2_BH_zero_after_edge_reduction",
        "odd zero condition",
    )
    require_equal(bool_cell(odd_criterion, "edge_reduction_required"), True, "odd criterion edge")
    require_equal(bool_cell(odd_criterion, "vanishing_supplied"), False, "odd vanishing supplied")

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
            "beta_vanishing_packet",
            "orientation_obstruction_ledger",
            "odd_transfer_theorem",
        },
        "source ids",
    )
    expected_status = {
        "finite_stabilizer_beta_packet": BETA_STATUS,
        "beta_vanishing_packet": BETA_VANISHING_STATUS,
        "orientation_obstruction_ledger": ORIENTATION_LEDGER_STATUS,
        "odd_transfer_theorem": "proved",
    }
    for source_id, status in expected_status.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_transfer(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["transfer_rows.csv"], "transfer_id", "transfer rows")
    require_equal(set(rows), {"odd_order_transfer"}, "transfer ids")
    row = rows["odd_order_transfer"]
    check_verified(row, "transfer_rows.csv")
    require_equal(row["group_condition"], "order_odd", "group condition")
    require_equal(row["coefficient_ring"], "F2", "coefficient ring")
    require_equal(bool_cell(row, "order_invertible"), True, "order invertible")
    require_equal(row["positive_degree_cohomology"], "H_positive_degree_zero", "positive degree")
    require_equal(row["degree_two_beta_target"], "H2_BH_F2_zero", "beta target")
    require_equal(row["degree_one_linearization_target"], "H1_BH_F2_zero", "linearization target")
    require_equal(bool_cell(row, "edge_reduction_required"), True, "edge required")
    require_equal(bool_cell(row, "transfer_verified"), True, "transfer verified")
    require_equal(bool_cell(row, "retained_edge_row_supplied"), False, "retained row")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "row285_template_rows": (3, True),
        "row286_criterion_rows": (4, True),
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
            row["odd_transfer_status"],
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
    verify_transfer(tables)
    verify_inspected(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_ODD_TRANSFER_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
