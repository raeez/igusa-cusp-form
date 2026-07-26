#!/usr/bin/env python3
"""Verify the row-294 second cyclic restriction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_klein_four_b02.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_klein_four_b02"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B02_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-klein-four-b02"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b02")
CLASS_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_class")
B11_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_klein_four_b11")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
CLASS_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_CLASS_VERIFIED"
B11_STATUS = "RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B11_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "restriction_map_count": 1,
    "b02_identity_count": 1,
    "row293_deferred_marker_count": 1,
    "retained_second_cyclic_row_count": 0,
    "r2_value_count": 0,
    "b02_value_count": 0,
    "beta_vanishing_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_e2_edge_row",
    "second_cyclic_restriction_row",
    "r2_value",
    "b02_value",
    "beta_vanishing",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "missing_second_cyclic_row",
    "missing_r2_value",
    "missing_b02_value",
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
            "b02_status",
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

B11_DEFERRED_COLUMNS = (
    "deferred_id",
    "row_number",
    "coefficient_identity",
    "deferred",
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
        "b11_packet_imported",
        "second_cyclic_restriction_recorded",
        "restriction_map_computed",
        "b02_identity_verified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "retained_e2_edge_row_supplied",
        "second_cyclic_restriction_row_supplied",
        "r2_value_supplied",
        "b02_value_supplied",
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
        {str(CLASS_FIXTURE), str(B11_FIXTURE), str(ORIENTATION_FIXTURE)},
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

    b11_manifest = read_json(B11_FIXTURE / "manifest.json")
    require_equal(b11_manifest.get("status"), B11_STATUS, "b11 packet status")
    require_equal(b11_manifest.get("b11_identity_verified"), True, "b11 identity")
    require_equal(
        b11_manifest.get("standalone_b02_identity_deferred"),
        True,
        "b11 deferred b02",
    )
    require_equal(b11_manifest.get("r_values_supplied"), False, "b11 r values")
    require_equal(b11_manifest.get("b02_value_supplied"), False, "b11 b02 value")
    require_equal(b11_manifest.get("beta_vanishing_verified"), False, "b11 beta vanishing")

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
    class_row = class_by_id["beta_E2_edge_class"]
    require_equal(
        class_row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "class formula",
    )
    require_equal(bool_cell(class_row, "coefficients_supplied"), False, "class coefficients")
    require_equal(bool_cell(class_row, "local_class_form_verified"), True, "class form verified")

    deferred_rows = read_table_path(B11_FIXTURE / "deferred_coefficient_rows.csv", B11_DEFERRED_COLUMNS)
    deferred_by_id = rows_by(deferred_rows, "deferred_id", "b11 deferred rows")
    row = deferred_by_id["b02_standalone_identity"]
    require_equal(row["row_number"], "row_294", "b11 deferred row number")
    require_equal(row["coefficient_identity"], "b02_equals_r2", "b11 deferred identity")
    require_equal(bool_cell(row, "deferred"), True, "b11 deferred flag")
    require_equal(row["check_status"], "verified", "b11 deferred check")

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
            "klein_four_b11_packet",
            "orientation_obstruction_ledger",
            "klein_four_lemma",
        },
        "source ids",
    )
    require_equal(rows["klein_four_class_packet"]["source_status"], CLASS_STATUS, "class source")
    require_equal(rows["klein_four_b11_packet"]["source_status"], B11_STATUS, "b11 source")
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
    require_equal(set(rows), {"second_cyclic_restriction"}, "restriction ids")
    row = rows["second_cyclic_restriction"]
    check_verified(row, "restriction_map_rows.csv")
    require_equal(row["source_group"], "E2", "restriction source group")
    require_equal(row["target_group"], "cyclic_e2", "restriction target group")
    require_equal(row["subgroup_generator"], "e2", "restriction generator")
    require_equal(row["target_generator"], "t", "target generator")
    require_equal(row["source_basis"], "x1_x2", "source basis")
    require_equal(row["target_basis"], "t", "target basis")
    require_equal(row["pullback_x1"], "iota2_x1_equals_0", "x1 pullback")
    require_equal(row["pullback_x2"], "iota2_x2_equals_t", "x2 pullback")
    require_equal(row["pullback_x1_square"], "0", "x1 square pullback")
    require_equal(row["pullback_x1x2"], "0", "x1x2 pullback")
    require_equal(row["pullback_x2_square"], "t_square", "x2 square pullback")
    require_equal(bool_cell(row, "restriction_map_verified"), True, "restriction verified")


def verify_coefficient_identity(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["coefficient_identity_rows.csv"], "identity_id", "identity rows")
    require_equal(set(rows), {"b02_equals_r2"}, "identity ids")
    row = rows["b02_equals_r2"]
    check_verified(row, "coefficient_identity_rows.csv")
    require_equal(row["restriction_id"], "second_cyclic_restriction", "identity restriction")
    require_equal(
        row["class_formula"],
        "b20_x1_square_plus_b11_x1x2_plus_b02_x2_square",
        "identity class formula",
    )
    require_equal(row["restricted_class_formula"], "b02_t_square", "restricted class")
    require_equal(row["cyclic_restriction_formula"], "r2_t_square", "cyclic restriction")
    require_equal(row["coefficient_identity"], "b02_equals_r2", "coefficient identity")
    require_equal(bool_cell(row, "identity_verified"), True, "identity verified")
    require_equal(row["retained_restriction_row_id"], "missing", "retained restriction")
    require_equal(bool_cell(row, "r_value_supplied"), False, "r value supplied")
    require_equal(bool_cell(row, "coefficient_value_supplied"), False, "coefficient value supplied")


def verify_inspected(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "klein_four_class_rows": (1, True),
        "b11_deferred_rows": (1, True),
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
        require_equal(row["b02_status"], "remaining_open_obligation", f"{row['obligation_id']} status")


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
    verify_inspected(tables)
    verify_coverage(tables)
    verify_remaining(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_KLEIN_FOUR_B02_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
