#!/usr/bin/env python3
"""Verify the row-282 connected free-E Borel obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_free_e_borel_obstruction.v1"
EXPECTED_KIND = "rhomred_free_e_borel_obstruction"
SUCCESS_STATUS = "RHOMRED_FREE_E_BOREL_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:free-e-borel-class-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_free_e_borel")
TRANSLATION_FIXTURE = Path("certificates/moduli/retained_e_translation_rigidifications")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
TRANSLATION_STATUS = "RETAINED_E_TRANSLATION_RIGIDIFICATIONS_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_ROWS = {
    "free_E_R0_s3": ("Eact_R0_s3", "Mss_R0_s3", "MErig_R0_s3"),
    "free_E_R0_s2": ("Eact_R0_s2", "Mss_R0_s2", "MErig_R0_s2"),
    "free_E_R0_s1": ("Eact_R0_s1", "Mss_R0_s1", "MErig_R0_s1"),
}

EXPECTED_COVERAGE = {
    "retained_strata_count": 3,
    "translation_action_count": 3,
    "basis_count": 1,
    "equivariant_borel_representative_count": 0,
    "edge_reduction_count": 0,
    "coefficient_row_count": 0,
    "free_e_value_count": 0,
    "free_e_vanishing_claim": 0,
    "free_e_null_trivialization_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "equivariant_borel_representative",
    "edge_reduction",
    "a1_a2_coefficients",
    "quotient_borel_free_e_row",
    "free_e_vanishing",
    "free_e_null_trivialization",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "H1_BE_zero",
    "free_E_action_only",
    "quotient_stack_only",
    "empty_quotient_borel_table",
    "finite_stabilizer_bits",
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
        "basis_rows.csv",
        (
            "basis_id",
            "group_id",
            "cohomology_group",
            "basis_payload",
            "h1_vanishes",
            "degree_two_basis_rank",
            "degree_two_class_form",
            "vanishing_condition",
            "coefficient_rows_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "free_e_obstruction_rows.csv",
        (
            "free_e_id",
            "translation_action_id",
            "substack_id",
            "quotient_stack_id",
            "equivariant_borel_row_id",
            "edge_reduction_row_id",
            "incoming_d2_status",
            "a1_value",
            "a2_value",
            "free_e_class_computed",
            "free_e_vanishing_verified",
            "null_trivialization_supplied",
            "quotient_borel_row_id",
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
            "free_e_status",
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

TRANSLATION_ACTION_COLUMNS = (
    "translation_action_id",
    "substack_id",
    "elliptic_curve_id",
    "origin_id",
    "action_defined",
    "action_free_on_retained_row",
    "action_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)

E_RIGIDIFICATION_COLUMNS = (
    "translation_rigidification_id",
    "substack_id",
    "scalar_rigidification_id",
    "universal_id",
    "elliptic_curve_id",
    "translation_action_id",
    "quotient_stack_id",
    "translation_removed",
    "action_free_on_retained_row",
    "translation_defect_rank",
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
        "retained_e_translation_imported",
        "orientation_obstruction_ledger_imported",
        "connected_e_basis_recorded",
        "edge_class_criterion_recorded",
        "three_free_actions_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "equivariant_borel_representatives_supplied",
        "edge_reduction_rows_supplied",
        "coefficient_rows_supplied",
        "free_e_class_values_computed",
        "free_e_vanishing_verified",
        "free_e_null_trivialization_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(TRANSLATION_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> tuple[dict[str, dict[str, str]], dict[str, dict[str, str]]]:
    translation_manifest = read_json(TRANSLATION_FIXTURE / "manifest.json")
    require_equal(translation_manifest.get("certified"), True, "translation certified")
    require_equal(translation_manifest.get("e_translation_rigidifications"), True, "translation rigidifications")
    require_equal(translation_manifest.get("translations_removed"), True, "translations removed")
    require_equal(translation_manifest.get("translation_defects_zero"), True, "translation defects zero")
    require_equal(translation_manifest.get("pfaffian_orientation"), False, "translation orientation")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    actions = read_table_path(TRANSLATION_FIXTURE / "translation_actions.csv", TRANSLATION_ACTION_COLUMNS)
    actions_by_id = rows_by(actions, "translation_action_id", "translation actions")
    for action_id, row in actions_by_id.items():
        require_equal(row["elliptic_curve_id"], "E", f"{action_id} curve")
        require_equal(row["origin_id"], "0_E", f"{action_id} origin")
        require_equal(bool_cell(row, "action_defined"), True, f"{action_id} defined")
        require_equal(bool_cell(row, "action_free_on_retained_row"), True, f"{action_id} free")
        require_equal(int_cell(row, "action_defect_rank"), 0, f"{action_id} defect")
        require_equal(row["check_status"], "verified", f"{action_id} check")

    rigidifications = read_table_path(
        TRANSLATION_FIXTURE / "e_translation_rigidifications.csv",
        E_RIGIDIFICATION_COLUMNS,
    )
    rigid_by_action = rows_by(rigidifications, "translation_action_id", "translation rigidifications")
    for action_id, row in rigid_by_action.items():
        require_equal(row["elliptic_curve_id"], "E", f"{action_id} rigid curve")
        require_equal(bool_cell(row, "translation_removed"), True, f"{action_id} removed")
        require_equal(bool_cell(row, "action_free_on_retained_row"), True, f"{action_id} rigid free")
        require_equal(int_cell(row, "translation_defect_rank"), 0, f"{action_id} rigid defect")
        require_equal(row["check_status"], "verified", f"{action_id} rigid check")

    quotient_rows = read_table_path(
        ORIENTATION_FIXTURE / "quotient_borel.csv",
        QUOTIENT_BOREL_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(quotient_rows), 0, "quotient Borel rows")
    return actions_by_id, rigid_by_action


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {"retained_e_translation", "orientation_obstruction_ledger", "connected_e_descent_lemma"},
        "source ids",
    )
    require_equal(rows["retained_e_translation"]["source_status"], TRANSLATION_STATUS, "translation source status")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source status",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_basis(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["basis_rows.csv"], "basis_id", "basis rows")
    require_equal(set(rows), {"BE_connected_basis"}, "basis ids")
    row = rows["BE_connected_basis"]
    check_verified(row, "basis_rows.csv")
    require_equal(row["group_id"], "E", "basis group")
    require_equal(row["cohomology_group"], "H2_BE_F2", "basis cohomology")
    require_equal(row["basis_payload"], "u1_u2", "basis payload")
    require_equal(bool_cell(row, "h1_vanishes"), True, "H1 vanishes")
    require_equal(int_cell(row, "degree_two_basis_rank"), 2, "basis rank")
    require_equal(row["degree_two_class_form"], "alpha_E_free_equals_a1_u1_plus_a2_u2", "class form")
    require_equal(row["vanishing_condition"], "a1_equals_0_and_a2_equals_0", "vanishing condition")
    require_equal(bool_cell(row, "coefficient_rows_supplied"), False, "coefficients supplied")


def verify_obstruction_rows(
    tables: dict[str, list[dict[str, str]]],
    actions_by_id: dict[str, dict[str, str]],
    rigid_by_action: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["free_e_obstruction_rows.csv"], "free_e_id", "free-E rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "free-E row ids")
    for free_e_id, (action_id, substack_id, quotient_stack_id) in EXPECTED_ROWS.items():
        row = rows[free_e_id]
        action = actions_by_id[action_id]
        rigid = rigid_by_action[action_id]
        check_verified(row, "free_e_obstruction_rows.csv")
        require_equal(row["translation_action_id"], action_id, f"{free_e_id} action")
        require_equal(row["substack_id"], substack_id, f"{free_e_id} substack")
        require_equal(row["quotient_stack_id"], quotient_stack_id, f"{free_e_id} quotient")
        require_equal(action["substack_id"], substack_id, f"{action_id} imported substack")
        require_equal(rigid["quotient_stack_id"], quotient_stack_id, f"{action_id} imported quotient")
        for key in (
            "equivariant_borel_row_id",
            "edge_reduction_row_id",
            "incoming_d2_status",
            "a1_value",
            "a2_value",
            "quotient_borel_row_id",
        ):
            require_equal(row[key], "missing", f"{free_e_id} {key}")
        require_equal(bool_cell(row, "free_e_class_computed"), False, f"{free_e_id} computed")
        require_equal(bool_cell(row, "free_e_vanishing_verified"), False, f"{free_e_id} vanishing")
        require_equal(bool_cell(row, "null_trivialization_supplied"), False, f"{free_e_id} null")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(
        set(rows),
        {
            "quotient_borel",
            "orientation_blocked_obligations",
            "translation_actions",
            "e_translation_rigidifications",
        },
        "inspected ids",
    )
    require_equal(int_cell(rows["quotient_borel"], "row_count"), 0, "quotient count")
    require_equal(bool_cell(rows["quotient_borel"], "supplied"), False, "quotient supplied")
    require_equal(int_cell(rows["orientation_blocked_obligations"], "row_count"), 26, "blocked count")
    require_equal(bool_cell(rows["orientation_blocked_obligations"], "supplied"), True, "blocked supplied")
    for table_id in ("translation_actions", "e_translation_rigidifications"):
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
        require_equal(row["free_e_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    actions_by_id, rigid_by_action = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_basis(tables)
    verify_obstruction_rows(tables, actions_by_id, rigid_by_action)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_FREE_E_BOREL_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
