#!/usr/bin/env python3
"""Verify the row-279 w2 formula and obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_w2_formula_obstruction.v1"
EXPECTED_KIND = "rhomred_w2_formula_obstruction"
SUCCESS_STATUS = "RHOMRED_W2_FORMULA_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:rhomred-w2-formula"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_w2")
DETERMINANT_FIXTURE = Path("certificates/orientation/rhomred_determinant")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
DETERMINANT_STATUS = "RHOMRED_DETERMINANT_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"

EXPECTED_ROWS = {
    "w2_R0_s3": ("det_R0_s3", "Ldet_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "w2_R0_s2": ("det_R0_s2", "Ldet_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "w2_R0_s1": ("det_R0_s1", "Ldet_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}

EXPECTED_COVERAGE = {
    "determinant_line_count": 3,
    "w2_formula_count": 2,
    "w2_obstruction_count": 3,
    "c1_row_count": 0,
    "grr_row_count": 0,
    "mod2_reduction_row_count": 0,
    "w2_value_count": 0,
    "w2_vanishing_claim": 0,
    "square_root_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "c1_determinant_line",
    "grr_universal_kernel",
    "mod2_reduction",
    "w2_determinant",
    "topological_square_root",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "determinant_line_only",
    "determinant_defect_zero",
    "square_root_obstruction_only",
    "c1_formula_without_class",
    "w2_zero_assumption",
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
        "formula_rows.csv",
        (
            "formula_id",
            "formula_kind",
            "input_line_or_complex",
            "formula_payload",
            "integral_c1_required",
            "grr_expansion_required",
            "mod2_reduction_required",
            "value_supplied",
            "vanishing_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "w2_obstruction_rows.csv",
        (
            "w2_id",
            "determinant_id",
            "determinant_line_id",
            "substack_id",
            "derived_stack_id",
            "c1_row_id",
            "grr_row_id",
            "mod2_reduction_row_id",
            "w2_value",
            "w2_computed",
            "w2_vanishing_verified",
            "topological_square_root_necessary_condition",
            "square_root_supplied",
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
            "w2_status",
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

DETERMINANT_COLUMNS = (
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
)

SQUARE_ROOT_COLUMNS = (
    "obstruction_id",
    "determinant_id",
    "determinant_line_id",
    "substack_id",
    "derived_stack_id",
    "orientation_line_id",
    "square_isomorphism_id",
    "square_root_supplied",
    "square_defect_rank_zero",
    "orientation_class_zero",
    "w2_computed",
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
        "rhomred_determinant_imported",
        "square_root_obstruction_imported",
        "w2_formula_recorded",
        "determinant_cohomology_formula_recorded",
        "three_determinant_lines_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "c1_rows_supplied",
        "grr_rows_supplied",
        "mod2_reduction_rows_supplied",
        "w2_values_computed",
        "w2_vanishing_verified",
        "topological_square_root_certified",
        "orientation_square_root",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(DETERMINANT_FIXTURE), str(SQUARE_ROOT_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    det_manifest = read_json(DETERMINANT_FIXTURE / "manifest.json")
    require_equal(det_manifest.get("status"), DETERMINANT_STATUS, "determinant status")
    require_equal(det_manifest.get("determinant_lines_defined"), True, "determinant lines defined")
    require_equal(det_manifest.get("w2_computed"), False, "determinant packet w2")

    square_manifest = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square_manifest.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_equal(square_manifest.get("square_root_rows_supplied"), False, "square-root rows supplied")
    require_equal(square_manifest.get("w2_computed"), False, "square-root packet w2")

    det_rows = read_table_path(DETERMINANT_FIXTURE / "determinant_rows.csv", DETERMINANT_COLUMNS)
    indexed = rows_by(det_rows, "determinant_id", "imported determinant rows")
    for row in indexed.values():
        require_equal(bool_cell(row, "determinant_defined"), True, f"{row['determinant_id']} determinant")
        require_equal(bool_cell(row, "w2_computed"), False, f"{row['determinant_id']} w2")
        require_equal(bool_cell(row, "square_root_constructed"), False, f"{row['determinant_id']} square root")

    square_rows = read_table_path(
        SQUARE_ROOT_FIXTURE / "square_root_obstruction_rows.csv",
        SQUARE_ROOT_COLUMNS,
    )
    for row in square_rows:
        require_equal(bool_cell(row, "w2_computed"), False, f"{row['obstruction_id']} imported w2")
        require_equal(bool_cell(row, "square_root_supplied"), False, f"{row['obstruction_id']} imported square root")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "rhomred_determinant",
            "rhomred_square_root",
            "complex_line_characteristic_class",
            "determinant_of_cohomology_formula",
        },
        "source ids",
    )
    require_equal(rows["rhomred_determinant"]["source_status"], DETERMINANT_STATUS, "det source status")
    require_equal(rows["rhomred_square_root"]["source_status"], SQUARE_ROOT_STATUS, "square source status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_formulae(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["formula_rows.csv"], "formula_id", "formula rows")
    require_equal(set(rows), {"w2_c1_mod2", "determinant_c1_grr"}, "formula ids")
    w2_row = rows["w2_c1_mod2"]
    grr_row = rows["determinant_c1_grr"]
    check_verified(w2_row, "formula_rows.csv")
    check_verified(grr_row, "formula_rows.csv")
    require_equal(bool_cell(w2_row, "integral_c1_required"), True, "w2 integral c1")
    require_equal(bool_cell(w2_row, "mod2_reduction_required"), True, "w2 mod2")
    require_equal(bool_cell(w2_row, "value_supplied"), False, "w2 value supplied")
    require_equal(bool_cell(w2_row, "vanishing_supplied"), False, "w2 vanishing supplied")
    require_equal(bool_cell(grr_row, "integral_c1_required"), True, "grr integral c1")
    require_equal(bool_cell(grr_row, "grr_expansion_required"), True, "grr expansion")
    require_equal(bool_cell(grr_row, "value_supplied"), False, "grr value supplied")
    require_equal(bool_cell(grr_row, "vanishing_supplied"), False, "grr vanishing supplied")


def verify_obstruction_rows(
    tables: dict[str, list[dict[str, str]]],
    determinant_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["w2_obstruction_rows.csv"], "w2_id", "w2 rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "w2 obstruction ids")
    for w2_id, (determinant_id, line_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[w2_id]
        det = determinant_rows[determinant_id]
        check_verified(row, "w2_obstruction_rows.csv")
        require_equal(row["determinant_id"], determinant_id, f"{w2_id} determinant")
        require_equal(row["determinant_line_id"], line_id, f"{w2_id} line")
        require_equal(row["substack_id"], substack_id, f"{w2_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{w2_id} derived")
        require_equal(det["determinant_line_id"], line_id, f"{determinant_id} imported line")
        for key in ("c1_row_id", "grr_row_id", "mod2_reduction_row_id", "w2_value"):
            require_equal(row[key], "missing", f"{w2_id} {key}")
        require_equal(bool_cell(row, "w2_computed"), False, f"{w2_id} computed")
        require_equal(bool_cell(row, "w2_vanishing_verified"), False, f"{w2_id} vanishing")
        require_equal(bool_cell(row, "topological_square_root_necessary_condition"), True, f"{w2_id} necessary")
        require_equal(bool_cell(row, "square_root_supplied"), False, f"{w2_id} square root")


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
        require_equal(row["w2_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    determinant_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_formulae(tables)
    verify_obstruction_rows(tables, determinant_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_W2_FORMULA_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
