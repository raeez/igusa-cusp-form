#!/usr/bin/env python3
"""Verify the row-292 first cyclic restriction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_klein_four_b20.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_klein_four_b20"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B20_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-klein-four-b20"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b20")
CLASS_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_class")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
CLASS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_CLASS_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "restriction_map_count": 1,
    "b20_identity_count": 1,
    "deferred_remaining_coefficient_count": 2,
    "retained_first_cyclic_row_count": 0,
    "r1_value_count": 0,
    "b20_value_count": 0,
    "beta_vanishing_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_e2_edge_row",
    "first_cyclic_restriction_row",
    "r1_value",
    "b20_value",
    "b11_identity",
    "b02_identity",
    "beta_vanishing",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "missing_first_cyclic_row",
    "missing_r1_value",
    "missing_b20_value",
    "b11_identity",
    "b02_identity",
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
        "restriction_map_rows.csv",
        (
            "restriction_id",
            "source_group",
            "target_group",
            "subgroup_generator",
            "target_generator",
            "source_basis",
            "target_basis",
            "pullback_x1",
            "pullback_x2",
            "pullback_x1_square",
            "pullback_x1x2",
            "pullback_x2_square",
            "restriction_map_verified",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coefficient_identity_rows.csv",
        (
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
        ),
    ),
    TableSpec(
        "deferred_coefficient_rows.csv",
        (
            "deferred_id",
            "row_number",
            "coefficient_identity",
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
            "b20_status",
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
        "first_cyclic_restriction_recorded",
        "restriction_map_computed",
        "b20_identity_verified",
        "remaining_coefficient_identities_deferred",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_e2_edge_row_supplied",
        "first_cyclic_restriction_row_supplied",
        "r1_value_supplied",
        "b20_value_supplied",
        "b11_identity_verified",
        "b02_identity_verified",
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
        {str(CLASS_FIXTURE), str(ORIENTATION_FIXTURE)},
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
    require_equal(
        class_manifest.get("cyclic_restriction_values_supplied"),
        False,
        "class cyclic values",
    )

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    class_rows = read_table_path(CLASS_FIXTURE / "klein_four_class_rows.csv", CLASS_ROW_COLUMNS)
    class_by_id = rows_by(class_rows, "class_id", "class rows")
    row = class_by_id["beta_E2_edge_class"]
    require_equal(row["group_id"], "E2", "class group")
    require_equal(row["basis_id"], "BE2_mod2_basis", "class basis")
    require_equal(bool_cell(row, "edge_reduction_required"), True, "class edge required")
    require_equal(
        row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "class formula",
    )
    require_equal(row["retained_edge_row_id"], "missing", "class retained edge")
    require_equal(row["coefficient_names"], "b20_b11_b02", "class coefficient names")
    require_equal(bool_cell(row, "coefficients_supplied"), False, "class coefficients supplied")
    require_equal(bool_cell(row, "local_class_form_verified"), True, "class form verified")
    require_equal(row["check_status"], "verified", "class row check")

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
            "orientation_obstruction_ledger",
            "klein_four_lemma",
        },
        "source ids",
    )
    require_equal(
        rows["klein_four_class_packet"]["source_status"],
        CLASS_STATUS,
        "class source",
    )
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source",
    )
    require_equal(rows["klein_four_lemma"]["source_status"], "proved", "lemma source")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_restriction_map(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["restriction_map_rows.csv"], "restriction_id", "restriction rows")
    require_equal(set(rows), {"first_cyclic_restriction"}, "restriction ids")
    row = rows["first_cyclic_restriction"]
    check_verified(row, "restriction_map_rows.csv")
    require_equal(row["source_group"], "E2", "restriction source group")
    require_equal(row["target_group"], "cyclic_e1", "restriction target group")
    require_equal(row["subgroup_generator"], "e1", "restriction generator")
    require_equal(row["target_generator"], "t", "target generator")
    require_equal(row["source_basis"], "x1_x2", "source basis")
    require_equal(row["target_basis"], "t", "target basis")
    require_equal(row["pullback_x1"], "iota1_x1_equals_t", "x1 pullback")
    require_equal(row["pullback_x2"], "iota1_x2_equals_0", "x2 pullback")
    require_equal(row["pullback_x1_square"], "t_square", "x1 square pullback")
    require_equal(row["pullback_x1x2"], "0", "x1x2 pullback")
    require_equal(row["pullback_x2_square"], "0", "x2 square pullback")
    require_equal(bool_cell(row, "restriction_map_verified"), True, "restriction verified")


def verify_coefficient_identity(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["coefficient_identity_rows.csv"], "identity_id", "identity rows")
    require_equal(set(rows), {"b20_equals_r1"}, "identity ids")
    row = rows["b20_equals_r1"]
    check_verified(row, "coefficient_identity_rows.csv")
    require_equal(row["restriction_id"], "first_cyclic_restriction", "identity restriction")
    require_equal(
        row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "identity class formula",
    )
    require_equal(row["restricted_class_formula"], "b20_t_square", "restricted class")
    require_equal(row["cyclic_restriction_formula"], "r1_t_square", "cyclic restriction")
    require_equal(row["coefficient_identity"], "b20_equals_r1", "coefficient identity")
    require_equal(bool_cell(row, "identity_verified"), True, "identity verified")
    require_equal(row["retained_restriction_row_id"], "missing", "retained restriction")
    require_equal(bool_cell(row, "r_value_supplied"), False, "r value supplied")
    require_equal(bool_cell(row, "coefficient_value_supplied"), False, "coefficient value supplied")


def verify_deferred(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["deferred_coefficient_rows.csv"], "deferred_id", "deferred rows")
    expected = {
        "b11_identity": ("row_293", "b11_equals_r1_plus_r2_plus_r3"),
        "b02_identity": ("row_294", "b02_equals_r2"),
    }
    require_equal(set(rows), set(expected), "deferred ids")
    for deferred_id, (row_number, identity) in expected.items():
        row = rows[deferred_id]
        require_equal(row["row_number"], row_number, f"{deferred_id} row")
        require_equal(row["coefficient_identity"], identity, f"{deferred_id} identity")
        require_equal(bool_cell(row, "deferred"), True, f"{deferred_id} deferred")
        require_equal(row["check_status"], "verified", f"{deferred_id} check")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "klein_four_class_rows": (1, True),
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
        require_equal(row["b20_status"], "remaining_open_obligation", f"{row['obligation_id']} status")


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
    verify_restriction_map(tables)
    verify_coefficient_identity(tables)
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
        print(f"RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B20_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
