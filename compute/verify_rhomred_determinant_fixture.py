#!/usr/bin/env python3
"""Verify the determinant line of the perfect reduced self-Ext complex."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_determinant.v1"
EXPECTED_KIND = "rhomred_determinant_input"
SUCCESS_STATUS = "RHOMRED_DETERMINANT_VERIFIED"
PROOF_LABEL = "def:rhomred-determinant-line"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_determinant")
PERFECTNESS_FIXTURE = Path("certificates/orientation/rhomred_perfectness")
PERFECTNESS_STATUS = "RHOMRED_PERFECTNESS_VERIFIED"
FORMULA_ID = "rhomred_det_formula"

EXPECTED_ROWS = {
    "det_R0_s3": ("perfect_R0_s3", "rhomred_R0_s3", "Mss_R0_s3", "DerStack_R0_s3", "Ldet_R0_s3"),
    "det_R0_s2": ("perfect_R0_s2", "rhomred_R0_s2", "Mss_R0_s2", "DerStack_R0_s2", "Ldet_R0_s2"),
    "det_R0_s1": ("perfect_R0_s1", "rhomred_R0_s1", "Mss_R0_s1", "DerStack_R0_s1", "Ldet_R0_s1"),
}

EXPECTED_COVERAGE = {
    "determinant_row_count": 3,
    "formula_count": 1,
    "determinant_defects": 0,
    "square_root_claim": 0,
    "w2_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "cosection_surjectivity",
    "orientation_square_root",
    "w2_determinant",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "perfectness_only",
    "euler_characteristic",
    "squared_determinant",
    "orientation_square_root",
    "w2_class",
    "scalar_trace",
    "maass_character_value",
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
        "determinant_formula_rows.csv",
        (
            "formula_id",
            "input_complex_kind",
            "determinant_functor",
            "local_formula",
            "km_signs_included",
            "quasi_isomorphism_invariant",
            "pullback_functorial",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "determinant_rows.csv",
        (
            "determinant_id",
            "perfectness_id",
            "rhomred_id",
            "substack_id",
            "derived_stack_id",
            "determinant_line_id",
            "formula_id",
            "input_perfect",
            "determinant_defined",
            "determinant_defect_rank",
            "square_root_constructed",
            "w2_computed",
            "orientation_constructed",
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
            "determinant_status",
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

PERFECTNESS_COLUMNS = (
    "perfectness_id",
    "rhomred_id",
    "substack_id",
    "derived_stack_id",
    "input_id",
    "target_id",
    "theta_map_id",
    "input_perfect",
    "target_perfect",
    "fibre_closure",
    "theorem_tag",
    "perfectness_defect_rank",
    "cosection_surjectivity_required_for_cone",
    "cosection_surjectivity_supplied",
    "determinant_defined",
    "orientation_constructed",
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


def read_table_path(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
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
        "rhomred_perfectness_imported",
        "determinant_functor_imported",
        "determinant_lines_defined",
        "three_substacks_verified",
        "determinant_defect_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_square_root",
        "w2_computed",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(PERFECTNESS_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    manifest = read_json(PERFECTNESS_FIXTURE / "manifest.json")
    require_equal(manifest.get("status"), PERFECTNESS_STATUS, "perfectness status")
    require_equal(manifest.get("perfect_cones"), True, "perfect cones")
    require_equal(manifest.get("det_rhom_red"), False, "perfectness packet determinant")
    rows = read_table_path(PERFECTNESS_FIXTURE / "perfectness_rows.csv", PERFECTNESS_COLUMNS)
    indexed = rows_by(rows, "perfectness_id", "imported perfectness rows")
    for row in indexed.values():
        require_equal(bool_cell(row, "input_perfect"), True, f"{row['perfectness_id']} input perfect")
        require_equal(bool_cell(row, "target_perfect"), True, f"{row['perfectness_id']} target perfect")
        require_equal(bool_cell(row, "fibre_closure"), True, f"{row['perfectness_id']} fibre closure")
        require_equal(int_cell(row, "perfectness_defect_rank"), 0, f"{row['perfectness_id']} perfectness defect")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {"rhomred_perfectness", "knudsen_mumford_determinant", "deligne_determinant"},
        "source ids",
    )
    require_equal(rows["rhomred_perfectness"]["source_status"], PERFECTNESS_STATUS, "perfectness source status")
    require_equal(rows["knudsen_mumford_determinant"]["source_path_or_key"], "KnudsenMumfordDet", "KM key")
    require_equal(rows["deligne_determinant"]["source_path_or_key"], "DeligneDetCohomology", "Deligne key")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_formula(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["determinant_formula_rows.csv"], "formula_id", "formula rows")
    require_equal(set(rows), {FORMULA_ID}, "formula ids")
    row = rows[FORMULA_ID]
    check_verified(row, "determinant_formula_rows.csv")
    require_equal(row["input_complex_kind"], "perfect_RHomred_complex", "formula input")
    require_equal(row["determinant_functor"], "Knudsen_Mumford_Det", "determinant functor")
    require_equal(row["local_formula"], "tensor_i_det_K_i_power_minus_one_i", "local formula")
    require_equal(bool_cell(row, "km_signs_included"), True, "KM signs")
    require_equal(bool_cell(row, "quasi_isomorphism_invariant"), True, "quasi-isomorphism invariant")
    require_equal(bool_cell(row, "pullback_functorial"), True, "pullback functorial")


def verify_determinant_rows(
    tables: dict[str, list[dict[str, str]]],
    perfectness_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["determinant_rows.csv"], "determinant_id", "determinant rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "determinant ids")
    for determinant_id, (
        perfectness_id,
        rhomred_id,
        substack_id,
        derived_stack_id,
        line_id,
    ) in EXPECTED_ROWS.items():
        row = rows[determinant_id]
        imported = perfectness_rows[perfectness_id]
        check_verified(row, "determinant_rows.csv")
        require_equal(row["perfectness_id"], perfectness_id, f"{determinant_id} perfectness")
        require_equal(row["rhomred_id"], rhomred_id, f"{determinant_id} rhomred")
        require_equal(row["substack_id"], substack_id, f"{determinant_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{determinant_id} derived")
        require_equal(row["determinant_line_id"], line_id, f"{determinant_id} line id")
        require_equal(row["formula_id"], FORMULA_ID, f"{determinant_id} formula")
        require_equal(imported["rhomred_id"], rhomred_id, f"{perfectness_id} rhomred")
        require_equal(imported["substack_id"], substack_id, f"{perfectness_id} substack")
        require_equal(imported["derived_stack_id"], derived_stack_id, f"{perfectness_id} derived")
        require_equal(bool_cell(row, "input_perfect"), True, f"{determinant_id} input perfect")
        require_equal(bool_cell(row, "determinant_defined"), True, f"{determinant_id} determinant")
        require_equal(int_cell(row, "determinant_defect_rank"), 0, f"{determinant_id} defect")
        require_equal(bool_cell(row, "square_root_constructed"), False, f"{determinant_id} square root")
        require_equal(bool_cell(row, "w2_computed"), False, f"{determinant_id} w2")
        require_equal(bool_cell(row, "orientation_constructed"), False, f"{determinant_id} orientation")


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
        require_equal(row["determinant_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    perfectness_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_formula(tables)
    verify_determinant_rows(tables, perfectness_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_DETERMINANT_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
