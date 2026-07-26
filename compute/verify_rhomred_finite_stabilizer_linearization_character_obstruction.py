#!/usr/bin/env python3
"""Verify the row-288 finite-stabilizer linearization-character obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_linearization_character_obstruction.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_linearization_character_obstruction"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_LINEARIZATION_CHARACTER_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-linearization-character-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_linearization_character")
NULL_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta_nulltrivialization")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
ANCHOR_WEIGHT_FIXTURE = Path("certificates/hybrid/determinant_anchor_translation_weight")
NULL_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_NULLTRIVIALIZATION_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
ANCHOR_WEIGHT_STATUS = "DETERMINANT_ANCHOR_TRANSLATION_WEIGHT_VERIFIED"

EXPECTED_ROWS = {
    "lambda_H_R0_s3": (
        "null_beta_H_R0_s3",
        "vanish_beta_H_R0_s3",
        "beta_H_R0_s3",
        "Ires_R0_s3",
        "Mss_R0_s3",
        "H_R0_s3",
    ),
    "lambda_H_R0_s2": (
        "null_beta_H_R0_s2",
        "vanish_beta_H_R0_s2",
        "beta_H_R0_s2",
        "Ires_R0_s2",
        "Mss_R0_s2",
        "H_R0_s2",
    ),
    "lambda_H_R0_s1": (
        "null_beta_H_R0_s1",
        "vanish_beta_H_R0_s1",
        "beta_H_R0_s1",
        "Ires_R0_s1",
        "Mss_R0_s1",
        "H_R0_s1",
    ),
}

EXPECTED_COVERAGE = {
    "retained_residual_group_count": 3,
    "linearization_obstruction_count": 3,
    "finite_linearization_row_count": 0,
    "orientation_line_action_count": 0,
    "generator_basis_count": 0,
    "character_value_count": 0,
    "h1_coordinate_count": 0,
    "lambda_computed_claim": 0,
    "lambda_vanishing_claim": 0,
    "transition_compatibility_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "orientation_line_action",
    "beta_nulltrivialization",
    "finite_linearization_row",
    "generator_basis",
    "character_value",
    "h1_coordinate",
    "all_retained_h_coverage",
    "lambda_character",
    "lambda_vanishing",
    "anchor_stabilizer_linearization",
    "quotient_borel_row",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "beta_zero_claim_only",
    "beta_nulltrivialization",
    "residual_group_order_one",
    "determinant_anchor_translation_weight",
    "stabilizer_restriction_formula",
    "class_invariance",
    "cyclic_quadratic_restrictions",
    "subgroup_nulltrivialization",
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
            "orientation_line_action_required",
            "nulltrivialization_required",
            "generator_basis_required",
            "character_values_required",
            "h1_coordinate_formula",
            "row288_computation_required",
            "row289_vanishing_required_for_row288",
            "linearization_character_computed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "linearization_character_obstruction_rows.csv",
        (
            "linearization_id",
            "nulltrivialization_id",
            "vanishing_id",
            "beta_row_id",
            "inertia_id",
            "substack_id",
            "residual_group_id",
            "residual_group_order",
            "orientation_line_action_id",
            "generator_basis_id",
            "h1_bh_template",
            "character_value_id",
            "lambda_value",
            "lambda_character_computed",
            "lambda_vanishing_verified",
            "finite_linearization_row_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "basis_restriction_obstruction_rows.csv",
        (
            "basis_check_id",
            "group_type",
            "required_generators",
            "restriction_values_required",
            "coordinate_formula",
            "basis_provenance_id",
            "all_generators_covered",
            "character_values_supplied",
            "h1_coordinates_computed",
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
            "linearization_status",
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

NULL_ROW_COLUMNS = (
    "nulltrivialization_id",
    "vanishing_id",
    "beta_row_id",
    "inertia_id",
    "substack_id",
    "residual_group_id",
    "residual_group_order",
    "beta_cocycle_id",
    "beta_zero_verified",
    "one_cochain_id",
    "coboundary_equation_id",
    "coboundary_defect_rank_zero",
    "nulltrivialization_supplied",
    "subgroup_compatibility_supplied",
    "linearization_computed",
    "quotient_borel_row_id",
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

ANCHOR_LINEARIZATION_COLUMNS = (
    "linearization_id",
    "R_id",
    "wrapped_colour_id",
    "stabilizer_id",
    "character_formula",
    "linearization_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)

ANCHOR_RESTRICTION_COLUMNS = (
    "restriction_id",
    "weight_row_id",
    "stabilizer_id",
    "restriction_formula",
    "invariance_condition",
    "linearization_status",
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
        "beta_nulltrivialization_imported",
        "orientation_obstruction_ledger_imported",
        "determinant_anchor_translation_weight_inspected",
        "linearization_character_criterion_recorded",
        "h1_basis_criterion_recorded",
        "three_residual_groups_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "finite_linearization_rows_supplied",
        "orientation_line_action_rows_supplied",
        "generator_basis_rows_supplied",
        "character_values_supplied",
        "h1_coordinates_computed",
        "all_retained_lambda_computed",
        "lambda_vanishing_verified",
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
        {str(NULL_FIXTURE), str(ORIENTATION_FIXTURE), str(ANCHOR_WEIGHT_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    null_manifest = read_json(NULL_FIXTURE / "manifest.json")
    require_equal(null_manifest.get("status"), NULL_STATUS, "nulltrivialization packet status")
    for key in (
        "beta_null_trivializations_supplied",
        "linearization_rows_supplied",
        "quotient_orientation",
        "transition_compatibility",
    ):
        require_equal(null_manifest.get(key), False, f"null manifest {key}")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    anchor_manifest = read_json(ANCHOR_WEIGHT_FIXTURE / "manifest.json")
    require_equal(anchor_manifest.get("status"), ANCHOR_WEIGHT_STATUS, "anchor weight status")
    require_equal(anchor_manifest.get("translation_weight_certified"), True, "anchor weight certified")
    require_equal(
        anchor_manifest.get("stabilizer_linearization_certification"),
        False,
        "anchor stabilizer linearization",
    )

    null_rows = read_table_path(
        NULL_FIXTURE / "beta_nulltrivialization_obstruction_rows.csv",
        NULL_ROW_COLUMNS,
    )
    null_by_id = rows_by(null_rows, "nulltrivialization_id", "imported null rows")
    require_equal(
        set(null_by_id),
        {values[0] for values in EXPECTED_ROWS.values()},
        "imported null ids",
    )
    for null_id, row in null_by_id.items():
        require_equal(int_cell(row, "residual_group_order"), 1, f"{null_id} order")
        require_equal(row["beta_cocycle_id"], "missing", f"{null_id} beta cocycle")
        require_equal(row["one_cochain_id"], "missing", f"{null_id} one cochain")
        require_equal(row["quotient_borel_row_id"], "missing", f"{null_id} quotient row")
        for key in (
            "beta_zero_verified",
            "coboundary_defect_rank_zero",
            "nulltrivialization_supplied",
            "subgroup_compatibility_supplied",
            "linearization_computed",
        ):
            require_equal(bool_cell(row, key), False, f"{null_id} {key}")
        require_equal(row["check_status"], "verified", f"{null_id} check")

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
    anchor_linearization_rows = read_table_path(
        ANCHOR_WEIGHT_FIXTURE / "stabilizer_linearization_rows.csv",
        ANCHOR_LINEARIZATION_COLUMNS,
        allow_empty=True,
    )
    anchor_restriction_rows = read_table_path(
        ANCHOR_WEIGHT_FIXTURE / "stabilizer_restriction_rows.csv",
        ANCHOR_RESTRICTION_COLUMNS,
    )
    require_equal(len(finite_rows), 0, "finite stabilizer rows")
    require_equal(len(quotient_rows), 0, "quotient Borel rows")
    require_equal(len(blocked_rows), 26, "orientation blocked obligations")
    require_equal(len(anchor_linearization_rows), 0, "anchor stabilizer linearization rows")
    require_equal(len(anchor_restriction_rows), 1, "anchor stabilizer restriction rows")
    restriction = anchor_restriction_rows[0]
    require_equal(
        restriction["restriction_id"],
        "det_anchor_translation_weight_H",
        "anchor restriction id",
    )
    require_equal(
        restriction["linearization_status"],
        "linearization_not_certified",
        "anchor restriction linearization status",
    )
    require_equal(restriction["check_status"], "verified", "anchor restriction check")
    return null_by_id


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "beta_nulltrivialization_packet",
            "orientation_obstruction_ledger",
            "determinant_anchor_translation_weight",
            "linearization_definition",
            "h1_coordinate_definition",
        },
        "source ids",
    )
    require_equal(rows["beta_nulltrivialization_packet"]["source_status"], NULL_STATUS, "null source")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source",
    )
    require_equal(
        rows["determinant_anchor_translation_weight"]["source_status"],
        ANCHOR_WEIGHT_STATUS,
        "anchor source",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criteria(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    expected_flags = {
        "linearization_character_definition": (True, True),
        "trivial_or_odd_h1_template": (False, False),
        "klein_four_h1_coordinates": (True, True),
        "two_primary_h1_coordinates": (True, True),
        "translation_weight_not_linearization": (True, True),
    }
    require_equal(set(rows), set(expected_flags), "criterion ids")
    for criterion_id, row in rows.items():
        check_verified(row, "criterion_rows.csv")
        require_equal(
            bool_cell(row, "orientation_line_action_required"),
            True,
            f"{criterion_id} action",
        )
        require_equal(
            bool_cell(row, "nulltrivialization_required"),
            True,
            f"{criterion_id} null",
        )
        basis_required, values_required = expected_flags[criterion_id]
        require_equal(
            bool_cell(row, "generator_basis_required"),
            basis_required,
            f"{criterion_id} basis",
        )
        require_equal(
            bool_cell(row, "character_values_required"),
            values_required,
            f"{criterion_id} values",
        )
        require_equal(
            bool_cell(row, "row288_computation_required"),
            True,
            f"{criterion_id} row288",
        )
        require_equal(
            bool_cell(row, "row289_vanishing_required_for_row288"),
            False,
            f"{criterion_id} row289",
        )
        require_equal(
            bool_cell(row, "linearization_character_computed"),
            False,
            f"{criterion_id} computed",
        )


def verify_linearization_rows(
    tables: dict[str, list[dict[str, str]]],
    null_by_id: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(
        tables["linearization_character_obstruction_rows.csv"],
        "linearization_id",
        "linearization rows",
    )
    require_equal(set(rows), set(EXPECTED_ROWS), "linearization row ids")
    for linearization_id, (
        null_id,
        vanishing_id,
        beta_row_id,
        inertia_id,
        substack_id,
        residual_group_id,
    ) in EXPECTED_ROWS.items():
        row = rows[linearization_id]
        null_row = null_by_id[null_id]
        check_verified(row, "linearization_character_obstruction_rows.csv")
        require_equal(row["nulltrivialization_id"], null_id, f"{linearization_id} null")
        require_equal(row["vanishing_id"], vanishing_id, f"{linearization_id} vanishing")
        require_equal(row["beta_row_id"], beta_row_id, f"{linearization_id} beta")
        require_equal(row["inertia_id"], inertia_id, f"{linearization_id} inertia")
        require_equal(row["substack_id"], substack_id, f"{linearization_id} substack")
        require_equal(row["residual_group_id"], residual_group_id, f"{linearization_id} group")
        require_equal(null_row["vanishing_id"], vanishing_id, f"{null_id} imported vanishing")
        require_equal(null_row["beta_row_id"], beta_row_id, f"{null_id} imported beta")
        require_equal(null_row["inertia_id"], inertia_id, f"{null_id} imported inertia")
        require_equal(null_row["substack_id"], substack_id, f"{null_id} imported substack")
        require_equal(null_row["residual_group_id"], residual_group_id, f"{null_id} imported group")
        require_equal(int_cell(row, "residual_group_order"), 1, f"{linearization_id} order")
        require_equal(row["orientation_line_action_id"], "missing", f"{linearization_id} action")
        require_equal(row["generator_basis_id"], "missing", f"{linearization_id} basis")
        require_equal(row["h1_bh_template"], "H1_B1_zero_template", f"{linearization_id} template")
        require_equal(row["character_value_id"], "missing", f"{linearization_id} character")
        require_equal(row["lambda_value"], "missing", f"{linearization_id} lambda")
        require_equal(row["finite_linearization_row_id"], "missing", f"{linearization_id} finite row")
        for key in ("lambda_character_computed", "lambda_vanishing_verified"):
            require_equal(bool_cell(row, key), False, f"{linearization_id} {key}")


def verify_basis_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(
        tables["basis_restriction_obstruction_rows.csv"],
        "basis_check_id",
        "basis rows",
    )
    require_equal(
        set(rows),
        {"trivial_or_odd_template", "klein_four_basis", "two_primary_basis"},
        "basis row ids",
    )
    expected_types = {
        "trivial_or_odd_template": "trivial_or_odd",
        "klein_four_basis": "E2",
        "two_primary_basis": "two_primary_rank_two",
    }
    for basis_id, row in rows.items():
        check_verified(row, "basis_restriction_obstruction_rows.csv")
        require_equal(row["group_type"], expected_types[basis_id], f"{basis_id} type")
        require_equal(row["basis_provenance_id"], "missing", f"{basis_id} basis provenance")
        for key in ("all_generators_covered", "character_values_supplied", "h1_coordinates_computed"):
            require_equal(bool_cell(row, key), False, f"{basis_id} {key}")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(
        set(rows),
        {
            "beta_nulltrivialization_obstruction_rows",
            "finite_stabilizers",
            "quotient_borel",
            "determinant_anchor_stabilizer_linearization_rows",
            "determinant_anchor_stabilizer_restriction_rows",
            "orientation_blocked_obligations",
        },
        "inspected ids",
    )
    expected_counts = {
        "beta_nulltrivialization_obstruction_rows": (3, False),
        "finite_stabilizers": (0, False),
        "quotient_borel": (0, False),
        "determinant_anchor_stabilizer_linearization_rows": (0, False),
        "determinant_anchor_stabilizer_restriction_rows": (1, False),
        "orientation_blocked_obligations": (26, True),
    }
    for table_id, (row_count, supplied) in expected_counts.items():
        row = rows[table_id]
        check_verified(row, "inspected_orientation_tables.csv")
        require_equal(int_cell(row, "row_count"), row_count, f"{table_id} row count")
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


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        require_equal(
            row["linearization_status"],
            "missing_open_obligation",
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
    null_by_id = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criteria(tables)
    verify_linearization_rows(tables, null_by_id)
    verify_basis_rows(tables)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_LINEARIZATION_CHARACTER_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
