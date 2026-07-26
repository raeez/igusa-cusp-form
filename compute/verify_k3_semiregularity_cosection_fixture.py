#!/usr/bin/env python3
"""Verify K3 semiregularity cosections on retained finite substacks."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "K3_SEMIREGULARITY_COSECTION_VERIFIED"
EXPECTED_SCHEMA = "k3_semiregularity_cosection.v1"
EXPECTED_KIND = "k3_semiregularity_cosection_input"
DEFAULT_FIXTURE = Path("certificates/orientation/k3_semiregularity_cosection")
PTVV_FIXTURE = Path("certificates/orientation/ptvv_finite_substack_symplectic")
DCRITICAL_FIXTURE = Path("certificates/orientation/joyce_dcritical_truncation")
PTVV_STATUS = "PTVV_FINITE_SUBSTACK_SYMPLECTIC_VERIFIED"
DCRITICAL_STATUS = "JOYCE_DCRITICAL_TRUNCATION_VERIFIED"
PROOF_LABEL = "prop:k3-semiregularity-cosection"
FORMULA_ID = "k3_semiregularity_formula"
EXPECTED_ROWS = {
    "cs_R0_s3": ("dcrit_R0_s3", "ptvv_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "cs_R0_s2": ("dcrit_R0_s2", "ptvv_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "cs_R0_s1": ("dcrit_R0_s1", "ptvv_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}
EXPECTED_COVERAGE = {
    "cosection_row_count": 3,
    "construction_defects": 0,
    "source_count": 2,
    "dcritical_import_count": 3,
    "surjectivity_claim": 0,
    "rhomred_claim": 0,
    "orientation_claim": 0,
    "hall_additivity_claim": 0,
    "protected_integration_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "cosection_surjectivity",
    "filtered_hall_additivity",
    "rhom_red",
    "perfect_reduced_obstruction",
    "det_rhom_red",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}
REQUIRED_FIREWALL = {
    "holomorphic_two_form_only",
    "dcritical_structure_only",
    "cosection_surjectivity",
    "filtered_hall_additivity",
    "RHomred",
    "det_RHomred",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
    "scalar_trace",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


DCRITICAL_COLUMNS = (
    "truncation_id",
    "ptvv_row_id",
    "substack_id",
    "derived_stack_id",
    "classical_truncation_id",
    "dcritical_structure_id",
    "shifted_symplectic_form_id",
    "dcritical_defect_rank",
    "vanishing_cycle_constructed",
    "orientation_constructed",
    "proof_reference",
    "check_status",
    "notes",
)

TABLE_SPECS = (
    TableSpec(
        "source_rows.csv",
        (
            "source_id",
            "citation_key",
            "source_result",
            "input_data",
            "output_map",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "formula_rows.csv",
        (
            "formula_id",
            "domain",
            "target",
            "holomorphic_form",
            "atiyah_class",
            "trace_pairing",
            "integration_target",
            "construction_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cosection_rows.csv",
        (
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
            "cosection_status",
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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if proof_required and PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key}={value}")
        indexed[value] = row
    return indexed


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("base_field"), "CC", "base_field")
    for key in (
        "ptvv_finite_substack_input_imported",
        "joyce_dcritical_truncation_imported",
        "holomorphic_two_form_input",
        "cosections_constructed",
        "three_substacks_verified",
        "cosection_construction_defect_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "cosection_surjectivity",
        "filtered_hall_additivity",
        "rhom_red",
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
    require_equal(
        set(manifest.get("imports", [])),
        {str(PTVV_FIXTURE), str(DCRITICAL_FIXTURE)},
        "imports",
    )


def verify_imports() -> dict[str, dict[str, str]]:
    ptvv_manifest = read_json(PTVV_FIXTURE / "manifest.json")
    require_equal(ptvv_manifest.get("status"), PTVV_STATUS, "PTVV import status")
    dcritical_manifest = read_json(DCRITICAL_FIXTURE / "manifest.json")
    require_equal(dcritical_manifest.get("status"), DCRITICAL_STATUS, "d-critical import status")
    dcritical_rows = read_table_path(
        DCRITICAL_FIXTURE / "dcritical_truncation_rows.csv",
        DCRITICAL_COLUMNS,
    )
    indexed = rows_by(dcritical_rows, "truncation_id", "dcritical import rows")
    require_equal(set(indexed), {value[0] for value in EXPECTED_ROWS.values()}, "imported d-critical rows")
    for truncation_id, row in indexed.items():
        if row.get("check_status") != "verified":
            raise ValueError(f"{truncation_id}: imported d-critical row is not verified")
        require_equal(int_cell(row, "dcritical_defect_rank"), 0, f"{truncation_id} d-critical defect")
        require_equal(bool_cell(row, "vanishing_cycle_constructed"), False, f"{truncation_id} vanishing cycle")
        require_equal(bool_cell(row, "orientation_constructed"), False, f"{truncation_id} orientation")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(set(rows), {"kiem_li_cosection_definition", "maulik_toda_semiregularity"}, "source ids")
    require_equal(rows["kiem_li_cosection_definition"]["citation_key"], "KiemLi2013", "Kiem-Li citation")
    require_equal(rows["maulik_toda_semiregularity"]["citation_key"], "MaulikTodaGV", "Maulik-Toda citation")
    for row in rows.values():
        check_verified(row, "source_rows.csv", proof_required=False)
        if PROOF_LABEL not in row["source_reference"]:
            raise ValueError(f"source row missing proof label: {row}")


def verify_formula(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["formula_rows.csv"], "formula_id", "formula rows")
    require_equal(set(rows), {FORMULA_ID}, "formula ids")
    row = rows[FORMULA_ID]
    check_verified(row, "formula_rows.csv")
    require_equal(row["domain"], "Ext2_X_F_F", "formula domain")
    require_equal(row["target"], "C", "formula target")
    require_equal(row["holomorphic_form"], "pS_star_sigmaS", "holomorphic form")
    require_equal(row["atiyah_class"], "At_F", "Atiyah class")
    require_equal(row["trace_pairing"], "Tr_xi_AtF", "trace pairing")
    require_equal(row["integration_target"], "H3_X_KX", "integration target")
    require_equal(int_cell(row, "construction_defect_rank"), 0, "formula defect")


def verify_cosection_rows(
    tables: dict[str, list[dict[str, str]]],
    dcritical_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["cosection_rows.csv"], "cosection_id", "cosection rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "cosection ids")
    for cosection_id, (truncation_id, ptvv_row_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[cosection_id]
        imported = dcritical_rows[truncation_id]
        check_verified(row, "cosection_rows.csv")
        require_equal(row["dcritical_truncation_id"], truncation_id, f"{cosection_id} truncation")
        require_equal(row["ptvv_row_id"], ptvv_row_id, f"{cosection_id} PTVV row")
        require_equal(row["substack_id"], substack_id, f"{cosection_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{cosection_id} derived stack")
        require_equal(imported["ptvv_row_id"], ptvv_row_id, f"{truncation_id} imported PTVV")
        require_equal(imported["substack_id"], substack_id, f"{truncation_id} imported substack")
        require_equal(imported["derived_stack_id"], derived_stack_id, f"{truncation_id} imported derived stack")
        require_equal(row["formula_id"], FORMULA_ID, f"{cosection_id} formula")
        require_equal(row["holomorphic_two_form_id"], "pS_star_sigmaS", f"{cosection_id} two-form")
        require_equal(int_cell(row, "construction_defect_rank"), 0, f"{cosection_id} defect")
        require_equal(bool_cell(row, "surjectivity_verified"), False, f"{cosection_id} surjectivity")
        require_equal(bool_cell(row, "hall_additivity_verified"), False, f"{cosection_id} Hall additivity")
        if not row["obstruction_sheaf_id"].startswith("Ob_"):
            raise ValueError(f"{cosection_id}: obstruction sheaf id is not explicit: {row}")
        if not row["target_line_id"].startswith("O_Mcl_"):
            raise ValueError(f"{cosection_id}: target line id is not the structure sheaf: {row}")


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
        require_equal(row["cosection_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    dcritical_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_formula(tables)
    verify_cosection_rows(tables, dcritical_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"K3_SEMIREGULARITY_COSECTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
