#!/usr/bin/env python3
"""Verify the RHom_red cone definition on retained finite substacks."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "RHOMRED_DEFINITION_VERIFIED"
EXPECTED_SCHEMA = "rhomred_definition.v1"
EXPECTED_KIND = "rhomred_definition_input"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_definition")
COSECTION_FIXTURE = Path("certificates/orientation/k3_semiregularity_cosection")
SURJECTIVITY_FIXTURE = Path("certificates/orientation/k3_cosection_surjectivity")
COSECTION_STATUS = "K3_SEMIREGULARITY_COSECTION_VERIFIED"
SURJECTIVITY_STATUS = "K3_COSECTION_SURJECTIVITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "def:rhom-red-self-ext-cone"
FORMULA_ID = "rhomred_cone_formula"
EXPECTED_ROWS = {
    "rhomred_R0_s3": ("cs_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "rhomred_R0_s2": ("cs_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "rhomred_R0_s1": ("cs_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}
EXPECTED_COVERAGE = {
    "rhomred_row_count": 3,
    "definition_defects": 0,
    "formula_count": 1,
    "surjectivity_supplied_count": 0,
    "perfectness_claim": 0,
    "determinant_claim": 0,
    "orientation_claim": 0,
    "protected_integration_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "cosection_surjectivity",
    "perfect_reduced_obstruction",
    "amplitude_bounds",
    "det_rhom_red",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}
SUPPLIED_BY_LATER_ROWS = {
    "perfect_reduced_obstruction": "supplied_by_rhomred_perfectness",
    "amplitude_bounds": "supplied_by_rhomred_perfectness",
    "det_rhom_red": "supplied_by_rhomred_determinant",
}
REQUIRED_FIREWALL = {
    "cosection_formula_only",
    "surjectivity_obstruction_only",
    "dcritical_structure",
    "PTVV_form_only",
    "perfectness_claim",
    "det_RHomred",
    "orientation_square_root",
    "scalar_trace",
    "protected_integration",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


COSECTION_COLUMNS = (
    "cosection_id",
    "dcritical_truncation_id",
    "ptvv_row_id",
    "substack_id",
    "derived_stack_id",
    "obstruction_sheaf_id",
    "holomorphic_two_form_id",
    "formula_id",
    "target_line_id",
    "construction_defect_rank",
    "surjectivity_verified",
    "hall_additivity_verified",
    "proof_reference",
    "check_status",
    "notes",
)

TABLE_SPECS = (
    TableSpec(
        "source_rows.csv",
        (
            "source_id",
            "source_packet",
            "source_status",
            "input_payload",
            "output_payload",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cone_formula_rows.csv",
        (
            "formula_id",
            "input_complex",
            "trace_component",
            "cosection_component",
            "target_complex",
            "cone_shift",
            "definition_defect_rank",
            "perfectness_proved",
            "determinant_defined",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "rhomred_rows.csv",
        (
            "rhomred_id",
            "cosection_id",
            "substack_id",
            "derived_stack_id",
            "input_complex_id",
            "theta_map_id",
            "trace_target_id",
            "cosection_target_id",
            "cone_formula_id",
            "cone_shift",
            "definition_defect_rank",
            "surjectivity_required",
            "surjectivity_supplied",
            "perfectness_proved",
            "determinant_defined",
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
            "rhomred_status",
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
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"missing JSON file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root is not an object: {path}")
    return value


def read_table_path(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            raise ValueError(f"{path}: expected columns {columns}, got {actual}")
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
    if not rows:
        raise ValueError(f"{path}: expected at least one data row")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns)


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key}={value}")
        indexed[value] = row
    return indexed


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if proof_required and PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("mathematical_certification"), False, "mathematical_certification")
    for key in (
        "k3_semiregularity_cosection_packet_imported",
        "k3_cosection_surjectivity_obstruction_imported",
        "rhomred_cones_defined",
        "three_substacks_recorded",
        "definition_defect_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "cosection_surjectivity_proved",
        "perfect_reduced_obstruction",
        "det_rhom_red",
        "orientation_square_root",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(COSECTION_FIXTURE), str(SURJECTIVITY_FIXTURE)}, "imports")


def verify_imports() -> dict[str, dict[str, str]]:
    cosection_manifest = read_json(COSECTION_FIXTURE / "manifest.json")
    require_equal(cosection_manifest.get("status"), COSECTION_STATUS, "cosection import status")
    surjectivity_manifest = read_json(SURJECTIVITY_FIXTURE / "manifest.json")
    require_equal(surjectivity_manifest.get("status"), SURJECTIVITY_STATUS, "surjectivity import status")
    rows = read_table_path(COSECTION_FIXTURE / "cosection_rows.csv", COSECTION_COLUMNS)
    indexed = rows_by(rows, "cosection_id", "imported cosection rows")
    require_equal({value[0] for value in EXPECTED_ROWS.values()}, set(indexed), "imported cosection ids")
    for row in indexed.values():
        require_equal(int_cell(row, "construction_defect_rank"), 0, f"{row['cosection_id']} construction defect")
        require_equal(bool_cell(row, "surjectivity_verified"), False, f"{row['cosection_id']} surjectivity")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(set(rows), {"k3_semiregularity_cosection", "k3_cosection_surjectivity_obstruction"}, "source ids")
    require_equal(rows["k3_semiregularity_cosection"]["source_status"], COSECTION_STATUS, "cosection source status")
    require_equal(rows["k3_cosection_surjectivity_obstruction"]["source_status"], SURJECTIVITY_STATUS, "surjectivity source status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_formula(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["cone_formula_rows.csv"], "formula_id", "formula rows")
    require_equal(set(rows), {FORMULA_ID}, "formula ids")
    row = rows[FORMULA_ID]
    check_verified(row, "cone_formula_rows.csv")
    require_equal(row["input_complex"], "RHom_X_F_F", "input complex")
    require_equal(row["trace_component"], "tr", "trace component")
    require_equal(row["cosection_component"], "CS_F", "cosection component")
    require_equal(row["target_complex"], "RGamma_X_OX_plus_H2_S_OS_shift_minus1", "target complex")
    require_equal(int_cell(row, "cone_shift"), -1, "cone shift")
    require_equal(int_cell(row, "definition_defect_rank"), 0, "definition defect")
    require_equal(bool_cell(row, "perfectness_proved"), False, "perfectness")
    require_equal(bool_cell(row, "determinant_defined"), False, "determinant")


def verify_rhomred_rows(
    tables: dict[str, list[dict[str, str]]],
    cosection_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["rhomred_rows.csv"], "rhomred_id", "RHomred rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "RHomred ids")
    for rhomred_id, (cosection_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[rhomred_id]
        imported = cosection_rows[cosection_id]
        check_verified(row, "rhomred_rows.csv")
        require_equal(row["cosection_id"], cosection_id, f"{rhomred_id} cosection")
        require_equal(row["substack_id"], substack_id, f"{rhomred_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{rhomred_id} derived stack")
        require_equal(imported["substack_id"], substack_id, f"{cosection_id} imported substack")
        require_equal(imported["derived_stack_id"], derived_stack_id, f"{cosection_id} imported derived stack")
        require_equal(row["cone_formula_id"], FORMULA_ID, f"{rhomred_id} formula")
        require_equal(row["trace_target_id"], "RGamma_X_OX", f"{rhomred_id} trace target")
        require_equal(row["cosection_target_id"], "H2_S_OS_shift_minus1", f"{rhomred_id} cosection target")
        require_equal(int_cell(row, "cone_shift"), -1, f"{rhomred_id} shift")
        require_equal(int_cell(row, "definition_defect_rank"), 0, f"{rhomred_id} defect")
        require_equal(bool_cell(row, "surjectivity_required"), False, f"{rhomred_id} surjectivity required")
        require_equal(bool_cell(row, "surjectivity_supplied"), False, f"{rhomred_id} surjectivity supplied")
        require_equal(bool_cell(row, "perfectness_proved"), False, f"{rhomred_id} perfectness")
        require_equal(bool_cell(row, "determinant_defined"), False, f"{rhomred_id} determinant")
        if not row["theta_map_id"].startswith("Theta_"):
            raise ValueError(f"{rhomred_id}: theta map id is not explicit: {row}")


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
        expected_status = SUPPLIED_BY_LATER_ROWS.get(
            row["obligation_id"],
            "missing_open_obligation",
        )
        require_equal(row["rhomred_status"], expected_status, f"{row['obligation_id']} status")


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
    cosection_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_formula(tables)
    verify_rhomred_rows(tables, cosection_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_DEFINITION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
