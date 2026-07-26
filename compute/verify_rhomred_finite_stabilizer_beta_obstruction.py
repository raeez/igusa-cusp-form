#!/usr/bin/env python3
"""Verify the row-285 finite-stabilizer beta-class obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_finite_stabilizer_beta_obstruction.v1"
EXPECTED_KIND = "rhomred_finite_stabilizer_beta_obstruction"
SUCCESS_STATUS = "RHOMRED_FINITE_STABILIZER_BETA_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-stabilizer-beta-class-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_beta")
INERTIA_FIXTURE = Path("certificates/moduli/retained_rigidification_inertia")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
INERTIA_STATUS = "RETAINED_RIGIDIFICATION_INERTIA_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_ROWS = {
    "beta_H_R0_s3": ("Ires_R0_s3", "Rig_R0_s3", "Mss_R0_s3", "H_R0_s3"),
    "beta_H_R0_s2": ("Ires_R0_s2", "Rig_R0_s2", "Mss_R0_s2", "H_R0_s2"),
    "beta_H_R0_s1": ("Ires_R0_s1", "Rig_R0_s1", "Mss_R0_s1", "H_R0_s1"),
}

EXPECTED_COVERAGE = {
    "retained_residual_group_count": 3,
    "template_count": 3,
    "finite_stabilizer_orientation_row_count": 0,
    "edge_reduction_count": 0,
    "beta_representative_count": 0,
    "beta_coefficient_count": 0,
    "beta_value_count": 0,
    "beta_vanishing_claim": 0,
    "linearization_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "finite_closed_inertia_stratification",
    "finite_stabilizer_orientation_row",
    "equivariant_beta_representative",
    "edge_reduction",
    "odd_transfer_edge_row",
    "klein_four_coefficients",
    "two_primary_coefficients",
    "beta_value",
    "beta_vanishing",
    "beta_null_trivialization",
    "linearization_character",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "residual_inertia_finite",
    "residual_group_order_one",
    "finite_closed_stratification_only",
    "cyclic_restrictions_only",
    "connected_free_E_class",
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
        "template_rows.csv",
        (
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
        ),
    ),
    TableSpec(
        "criterion_rows.csv",
        (
            "criterion_id",
            "finite_group_type_required",
            "beta_representative_required",
            "edge_reduction_required",
            "coefficient_payload_required",
            "linearization_required_for_row285",
            "beta_value_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "residual_group_beta_rows.csv",
        (
            "beta_row_id",
            "inertia_id",
            "rigidification_id",
            "substack_id",
            "residual_group_id",
            "residual_group_order",
            "residual_inertia_finite",
            "finite_closed_inertia_stratum_id",
            "finite_stabilizer_orientation_row_id",
            "beta_representative_id",
            "edge_reduction_row_id",
            "group_type_for_beta",
            "h2_bh_template",
            "beta_value",
            "beta_class_computed",
            "beta_vanishing_verified",
            "linearization_computed",
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
            "beta_status",
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

RESIDUAL_INERTIA_COLUMNS = (
    "inertia_id",
    "rigidification_id",
    "substack_id",
    "residual_group_id",
    "residual_group_order",
    "residual_inertia_finite",
    "inertia_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)

GROUP_SEQUENCE_COLUMNS = (
    "sequence_id",
    "rigidification_id",
    "substack_id",
    "automorphism_group_id",
    "scalar_group_id",
    "residual_group_id",
    "residual_group_order",
    "exactness_defect_rank",
    "source_reference",
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
        "residual_inertia_imported",
        "orientation_obstruction_ledger_imported",
        "group_cohomology_templates_recorded",
        "beta_computation_criterion_recorded",
        "three_residual_groups_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "finite_closed_inertia_stratifications_supplied",
        "finite_stabilizer_orientation_rows_supplied",
        "equivariant_beta_representatives_supplied",
        "edge_reduction_rows_supplied",
        "beta_coefficients_supplied",
        "beta_class_values_computed",
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
        {str(INERTIA_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    inertia_manifest = read_json(INERTIA_FIXTURE / "manifest.json")
    require_equal(inertia_manifest.get("moduli_kind"), "retained_rigidification_inertia", "inertia kind")
    require_equal(inertia_manifest.get("certified"), True, "inertia certified")
    require_equal(inertia_manifest.get("finite_residual_inertia_after_rigidification"), True, "finite inertia")
    require_equal(inertia_manifest.get("finite_inertia_stratifications"), False, "finite stratifications")
    require_equal(inertia_manifest.get("pfaffian_orientation"), False, "pfaffian orientation")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    residual_rows = read_table_path(INERTIA_FIXTURE / "residual_inertia.csv", RESIDUAL_INERTIA_COLUMNS)
    residual_by_id = rows_by(residual_rows, "inertia_id", "residual inertia")
    require_equal(set(residual_by_id), {row[0] for row in EXPECTED_ROWS.values()}, "residual inertia ids")
    for inertia_id, row in residual_by_id.items():
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{inertia_id} finite")
        require_equal(int_cell(row, "residual_group_order"), 1, f"{inertia_id} order")
        require_equal(int_cell(row, "inertia_defect_rank"), 0, f"{inertia_id} defect")
        require_equal(row["check_status"], "verified", f"{inertia_id} check")

    sequence_rows = read_table_path(INERTIA_FIXTURE / "group_exact_sequences.csv", GROUP_SEQUENCE_COLUMNS)
    sequence_by_substack = rows_by(sequence_rows, "substack_id", "group sequences")
    for row in sequence_by_substack.values():
        require_equal(row["scalar_group_id"], "G_m", f"{row['sequence_id']} scalar")
        require_equal(int_cell(row, "residual_group_order"), 1, f"{row['sequence_id']} order")
        require_equal(int_cell(row, "exactness_defect_rank"), 0, f"{row['sequence_id']} exactness")
        require_equal(row["check_status"], "verified", f"{row['sequence_id']} check")

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
    require_equal(len(finite_rows), 0, "finite stabilizer orientation rows")
    require_equal(len(quotient_rows), 0, "quotient Borel rows")
    return residual_by_id


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "retained_rigidification_inertia",
            "orientation_obstruction_ledger",
            "finite_stabilizer_e_descent",
            "klein_four_two_primary_lemmas",
        },
        "source ids",
    )
    require_equal(
        rows["retained_rigidification_inertia"]["source_status"],
        INERTIA_STATUS,
        "inertia source status",
    )
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source status",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_templates(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["template_rows.csv"], "template_id", "template rows")
    require_equal(set(rows), {"odd_or_trivial", "klein_four", "two_primary_rank_two"}, "template ids")
    require_equal(rows["odd_or_trivial"]["cohomology_basis"], "H2_BH_F2_zero", "odd basis")
    require_equal(rows["klein_four"]["cohomology_basis"], "x1_square_x1x2_x2_square", "E2 basis")
    require_equal(rows["two_primary_rank_two"]["cohomology_basis"], "y1_x1x2_y2", "two-primary basis")
    require_equal(bool_cell(rows["klein_four"], "cyclic_restrictions_determine_quadratic"), True, "E2 cyclic")
    require_equal(
        bool_cell(rows["two_primary_rank_two"], "cyclic_restrictions_determine_quadratic"),
        False,
        "two-primary cyclic",
    )
    for row in rows.values():
        check_verified(row, "template_rows.csv")
        require_equal(bool_cell(row, "edge_reduction_required"), True, f"{row['template_id']} edge")
        require_equal(bool_cell(row, "cyclic_only_orientation_row"), False, f"{row['template_id']} cyclic only")


def verify_criteria(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(
        set(rows),
        {
            "finite_stabilizer_beta_class",
            "residual_inertia_not_enough",
            "cyclic_only_not_enough",
            "vanishing_is_later_row",
        },
        "criterion ids",
    )
    for row in rows.values():
        check_verified(row, "criterion_rows.csv")
        for key in (
            "finite_group_type_required",
            "beta_representative_required",
            "edge_reduction_required",
            "coefficient_payload_required",
        ):
            require_equal(bool_cell(row, key), True, f"{row['criterion_id']} {key}")
        require_equal(
            bool_cell(row, "linearization_required_for_row285"),
            False,
            f"{row['criterion_id']} linearization",
        )
        require_equal(bool_cell(row, "beta_value_supplied"), False, f"{row['criterion_id']} supplied")


def verify_beta_rows(
    tables: dict[str, list[dict[str, str]]],
    residual_by_id: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["residual_group_beta_rows.csv"], "beta_row_id", "beta rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "beta row ids")
    for beta_row_id, (inertia_id, rigidification_id, substack_id, residual_group_id) in EXPECTED_ROWS.items():
        row = rows[beta_row_id]
        imported = residual_by_id[inertia_id]
        check_verified(row, "residual_group_beta_rows.csv")
        require_equal(row["inertia_id"], inertia_id, f"{beta_row_id} inertia")
        require_equal(row["rigidification_id"], rigidification_id, f"{beta_row_id} rigidification")
        require_equal(row["substack_id"], substack_id, f"{beta_row_id} substack")
        require_equal(row["residual_group_id"], residual_group_id, f"{beta_row_id} group")
        require_equal(imported["rigidification_id"], rigidification_id, f"{inertia_id} imported rigidification")
        require_equal(imported["substack_id"], substack_id, f"{inertia_id} imported substack")
        require_equal(imported["residual_group_id"], residual_group_id, f"{inertia_id} imported group")
        require_equal(int_cell(row, "residual_group_order"), 1, f"{beta_row_id} order")
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{beta_row_id} finite")
        for key in (
            "finite_closed_inertia_stratum_id",
            "finite_stabilizer_orientation_row_id",
            "beta_representative_id",
            "edge_reduction_row_id",
            "beta_value",
        ):
            require_equal(row[key], "missing", f"{beta_row_id} {key}")
        require_equal(row["group_type_for_beta"], "trivial_residual_group", f"{beta_row_id} type")
        require_equal(row["h2_bh_template"], "H2_B1_zero_if_edge_supplied", f"{beta_row_id} template")
        for key in ("beta_class_computed", "beta_vanishing_verified", "linearization_computed"):
            require_equal(bool_cell(row, key), False, f"{beta_row_id} {key}")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(
        set(rows),
        {
            "finite_stabilizers",
            "quotient_borel",
            "orientation_blocked_obligations",
            "residual_inertia",
            "group_exact_sequences",
        },
        "inspected ids",
    )
    require_equal(int_cell(rows["finite_stabilizers"], "row_count"), 0, "finite table count")
    require_equal(bool_cell(rows["finite_stabilizers"], "supplied"), False, "finite supplied")
    require_equal(int_cell(rows["quotient_borel"], "row_count"), 0, "quotient count")
    require_equal(bool_cell(rows["quotient_borel"], "supplied"), False, "quotient supplied")
    require_equal(int_cell(rows["orientation_blocked_obligations"], "row_count"), 26, "blocked count")
    require_equal(bool_cell(rows["orientation_blocked_obligations"], "supplied"), True, "blocked supplied")
    for table_id in ("residual_inertia", "group_exact_sequences"):
        require_equal(int_cell(rows[table_id], "row_count"), 3, f"{table_id} count")
        require_equal(bool_cell(rows[table_id], "supplied"), True, f"{table_id} supplied")
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
        require_equal(row["beta_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    residual_by_id = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_templates(tables)
    verify_criteria(tables)
    verify_beta_rows(tables, residual_by_id)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FINITE_STABILIZER_BETA_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
