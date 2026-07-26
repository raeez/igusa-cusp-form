#!/usr/bin/env python3
"""Verify the row-297 two-primary mixed-term detector packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_two_primary_mixed_term_detection.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_two_primary_mixed_term_detection"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_TWO_PRIMARY_MIXED_TERM_DETECTION_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-two-primary-mixed-term"
DEFAULT_FIXTURE = Path(
    "certificates/orientation/rhomred_finite_stabilizer_two_primary_mixed_term_detection"
)
TWO_PRIMARY_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_two_primary_class")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
TWO_PRIMARY_STATUS = "RHOMRED_FINITE_STABILIZER_TWO_PRIMARY_CLASS_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "detector_count": 1,
    "cyclic_annihilation_count": 2,
    "retained_A12_value_count": 0,
    "coefficient_value_count": 0,
    "cyclic_substitute_claim": 0,
    "beta_vanishing_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_two_primary_edge_row",
    "A12_value",
    "coefficient_values",
    "beta_vanishing",
    "zero_linearization",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "cyclic_restrictions_only",
    "coordinate_cyclic_restrictions",
    "missing_A12_value",
    "residual_group_type_only",
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
        "detector_rows.csv",
        (
            "detector_id",
            "group_id",
            "basis_id",
            "input_class",
            "detector_formula",
            "detector_y1",
            "detector_x1x2",
            "detector_y2",
            "detected_coefficient",
            "detector_verified",
            "retained_value_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cyclic_annihilation_rows.csv",
        (
            "annihilation_id",
            "cyclic_subgroup_type",
            "restriction_x1",
            "restriction_x2",
            "restriction_x1x2",
            "reason",
            "annihilation_verified",
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
            "mixed_term_status",
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

TWO_PRIMARY_CLASS_COLUMNS = (
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
        "two_primary_class_imported",
        "orientation_obstruction_ledger_imported",
        "rank_two_detector_recorded",
        "cyclic_annihilation_verified",
        "cyclic_restrictions_excluded_for_A12",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_two_primary_edge_row_supplied",
        "A12_value_supplied",
        "coefficient_values_supplied",
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
        {str(TWO_PRIMARY_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    two_primary_manifest = read_json(TWO_PRIMARY_FIXTURE / "manifest.json")
    require_equal(two_primary_manifest.get("status"), TWO_PRIMARY_STATUS, "two-primary packet status")
    require_equal(two_primary_manifest.get("two_primary_class_form_recorded"), True, "class form")
    require_equal(
        two_primary_manifest.get("mixed_term_detection_deferred_to_row_297"),
        True,
        "mixed detection deferred",
    )
    require_equal(
        two_primary_manifest.get("retained_two_primary_edge_row_supplied"),
        False,
        "two-primary retained edge",
    )
    require_equal(
        two_primary_manifest.get("coefficient_values_supplied"),
        False,
        "two-primary coefficient values",
    )

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    class_rows = read_table_path(
        TWO_PRIMARY_FIXTURE / "two_primary_class_rows.csv",
        TWO_PRIMARY_CLASS_COLUMNS,
    )
    class_row = rows_by(class_rows, "class_id", "two-primary class rows")[
        "beta_two_primary_edge_class"
    ]
    require_equal(class_row["basis_id"], "BZ2a_square_mod2_basis", "basis id")
    require_equal(
        class_row["class_formula"],
        "A1_y1_plus_A12_x1x2_plus_A2_y2",
        "class formula",
    )
    require_equal(class_row["coefficient_names"], "A1_A12_A2", "coefficient names")
    require_equal(class_row["retained_edge_row_id"], "missing", "retained edge row")
    require_equal(bool_cell(class_row, "coefficients_supplied"), False, "coefficients supplied")
    require_equal(bool_cell(class_row, "local_class_form_verified"), True, "class form verified")

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
            "two_primary_class_packet",
            "orientation_obstruction_ledger",
            "two_primary_lemma",
        },
        "source ids",
    )
    require_equal(
        rows["two_primary_class_packet"]["source_status"],
        TWO_PRIMARY_STATUS,
        "two-primary source",
    )
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source",
    )
    require_equal(rows["two_primary_lemma"]["source_status"], "proved", "two-primary lemma")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_detector(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["detector_rows.csv"], "detector_id", "detector rows")
    require_equal(set(rows), {"pi12_rank_two_detector"}, "detector ids")
    row = rows["pi12_rank_two_detector"]
    check_verified(row, "detector_rows.csv")
    require_equal(row["group_id"], "Z2a_square", "detector group")
    require_equal(row["basis_id"], "BZ2a_square_mod2_basis", "detector basis")
    require_equal(
        row["input_class"],
        "A1_y1_plus_A12_x1x2_plus_A2_y2",
        "detector input",
    )
    require_equal(row["detector_formula"], "coefficient_projection_to_x1x2", "detector formula")
    require_equal(row["detector_y1"], "0", "detector y1")
    require_equal(row["detector_x1x2"], "1", "detector x1x2")
    require_equal(row["detector_y2"], "0", "detector y2")
    require_equal(row["detected_coefficient"], "A12", "detected coefficient")
    require_equal(bool_cell(row, "detector_verified"), True, "detector verified")
    require_equal(bool_cell(row, "retained_value_supplied"), False, "retained value supplied")


def verify_cyclic_annihilation(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(
        tables["cyclic_annihilation_rows.csv"],
        "annihilation_id",
        "cyclic annihilation rows",
    )
    expected = {
        "order_two_cyclic": (
            "order_two_subgroup",
            "0",
            "0",
            "0",
            "order_two_subgroups_lie_in_2Z2a_square_for_a_ge_2",
        ),
        "order_at_least_four_cyclic": (
            "cyclic_order_at_least_four",
            "scalar_u",
            "scalar_u",
            "0",
            "u_square_equals_zero_in_Lambda_u_tensor_F2_v",
        ),
    }
    require_equal(set(rows), set(expected), "cyclic annihilation ids")
    for row_id, (subgroup_type, x1, x2, x1x2, reason) in expected.items():
        row = rows[row_id]
        check_verified(row, "cyclic_annihilation_rows.csv")
        require_equal(row["cyclic_subgroup_type"], subgroup_type, f"{row_id} subgroup")
        require_equal(row["restriction_x1"], x1, f"{row_id} x1")
        require_equal(row["restriction_x2"], x2, f"{row_id} x2")
        require_equal(row["restriction_x1x2"], x1x2, f"{row_id} x1x2")
        require_equal(row["reason"], reason, f"{row_id} reason")
        require_equal(bool_cell(row, "annihilation_verified"), True, f"{row_id} verified")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "two_primary_class_rows": (1, True),
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
            row["mixed_term_status"],
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
    verify_detector(tables)
    verify_cyclic_annihilation(tables)
    verify_inspected(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(
            f"RHOMRED_FINITE_STABILIZER_TWO_PRIMARY_MIXED_TERM_DETECTION_BLOCKED: {exc}",
            file=sys.stderr,
        )
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
