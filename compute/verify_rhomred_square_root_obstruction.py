#!/usr/bin/env python3
"""Verify the row-278 square-root obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_square_root_obstruction.v1"
EXPECTED_KIND = "rhomred_square_root_obstruction"
SUCCESS_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:rhomred-square-root-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
DETERMINANT_FIXTURE = Path("certificates/orientation/rhomred_determinant")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
DETERMINANT_STATUS = "RHOMRED_DETERMINANT_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_ROWS = {
    "sqroot_R0_s3": ("det_R0_s3", "Ldet_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "sqroot_R0_s2": ("det_R0_s2", "Ldet_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "sqroot_R0_s1": ("det_R0_s1", "Ldet_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}

EXPECTED_COVERAGE = {
    "determinant_line_count": 3,
    "square_root_obstruction_count": 3,
    "orientation_line_rows_supplied": 0,
    "square_root_claim": 0,
    "w2_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "orientation_square_root",
    "orientation_class_zero",
    "w2_determinant",
    "quotient_orientation",
    "ts_multiplicativity",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "determinant_line_only",
    "squared_determinant",
    "w2_zero_only",
    "Ext1_determinant_expression",
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
            "determinant_line_required",
            "orientation_line_required",
            "square_isomorphism_required",
            "picard_divisibility_required",
            "choices_torsor",
            "topological_w2_necessary",
            "algebraic_square_root_supplied",
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
        "square_root_obstruction_rows.csv",
        (
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
            "square_root_status",
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

ORIENTATION_LINE_COLUMNS = (
    "line_id",
    "stratum_id",
    "det_complex_id",
    "square_root_id",
    "square_defect_rank",
    "orientation_class_rank",
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


def read_table_path(path: Path, columns: tuple[str, ...], allow_empty: bool = False) -> list[dict[str, str]]:
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
        "rhomred_determinant_imported",
        "orientation_obstruction_ledger_imported",
        "square_root_criterion_recorded",
        "three_determinant_lines_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "square_root_rows_supplied",
        "square_defect_zero",
        "orientation_class_zero",
        "mathematical_certification",
        "w2_computed",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(DETERMINANT_FIXTURE), str(ORIENTATION_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    det_manifest = read_json(DETERMINANT_FIXTURE / "manifest.json")
    require_equal(det_manifest.get("status"), DETERMINANT_STATUS, "determinant status")
    require_equal(det_manifest.get("determinant_lines_defined"), True, "determinant lines defined")
    require_equal(det_manifest.get("orientation_square_root"), False, "determinant packet square root")

    orient_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(orient_manifest.get("obstruction_ledger_status"), ORIENTATION_LEDGER_STATUS, "orientation ledger")
    require_equal(orient_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orient_manifest.get("empty_blocked"), True, "orientation empty blocked")
    orientation_rows = read_table_path(
        ORIENTATION_FIXTURE / "orientation_lines.csv",
        ORIENTATION_LINE_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(orientation_rows), 0, "orientation line row count")

    rows = read_table_path(DETERMINANT_FIXTURE / "determinant_rows.csv", DETERMINANT_COLUMNS)
    indexed = rows_by(rows, "determinant_id", "imported determinant rows")
    for row in indexed.values():
        require_equal(bool_cell(row, "determinant_defined"), True, f"{row['determinant_id']} determinant")
        require_equal(bool_cell(row, "square_root_constructed"), False, f"{row['determinant_id']} square root")
        require_equal(bool_cell(row, "w2_computed"), False, f"{row['determinant_id']} w2")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {"rhomred_determinant", "orientation_obstruction_ledger", "picard_square_root_criterion"},
        "source ids",
    )
    require_equal(rows["rhomred_determinant"]["source_status"], DETERMINANT_STATUS, "det source status")
    require_equal(rows["orientation_obstruction_ledger"]["source_status"], ORIENTATION_LEDGER_STATUS, "orientation source status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"square_root_picard_criterion"}, "criterion ids")
    row = rows["square_root_picard_criterion"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "determinant_line_required",
        "orientation_line_required",
        "square_isomorphism_required",
        "picard_divisibility_required",
        "topological_w2_necessary",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(row["choices_torsor"], "Picard_two_torsion", "choices torsor")
    require_equal(bool_cell(row, "algebraic_square_root_supplied"), False, "square root supplied")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(set(rows), {"orientation_lines", "orientation_blocked_obligations", "orientation_manifest"}, "inspected ids")
    require_equal(int_cell(rows["orientation_lines"], "row_count"), 0, "orientation lines count")
    require_equal(bool_cell(rows["orientation_lines"], "supplied"), False, "orientation lines supplied")
    require_equal(bool_cell(rows["orientation_blocked_obligations"], "supplied"), True, "blocked ledger supplied")
    require_equal(bool_cell(rows["orientation_manifest"], "supplied"), True, "manifest supplied")
    for row in rows.values():
        check_verified(row, "inspected_orientation_tables.csv")


def verify_obstruction_rows(
    tables: dict[str, list[dict[str, str]]],
    determinant_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["square_root_obstruction_rows.csv"], "obstruction_id", "square-root rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "square-root obstruction ids")
    for obstruction_id, (determinant_id, line_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[obstruction_id]
        det = determinant_rows[determinant_id]
        check_verified(row, "square_root_obstruction_rows.csv")
        require_equal(row["determinant_id"], determinant_id, f"{obstruction_id} determinant")
        require_equal(row["determinant_line_id"], line_id, f"{obstruction_id} line")
        require_equal(row["substack_id"], substack_id, f"{obstruction_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{obstruction_id} derived")
        require_equal(det["determinant_line_id"], line_id, f"{determinant_id} imported line")
        require_equal(row["orientation_line_id"], "missing", f"{obstruction_id} orientation line")
        require_equal(row["square_isomorphism_id"], "missing", f"{obstruction_id} square isomorphism")
        require_equal(bool_cell(row, "square_root_supplied"), False, f"{obstruction_id} square root")
        require_equal(bool_cell(row, "square_defect_rank_zero"), False, f"{obstruction_id} square defect")
        require_equal(bool_cell(row, "orientation_class_zero"), False, f"{obstruction_id} orientation class")
        require_equal(bool_cell(row, "w2_computed"), False, f"{obstruction_id} w2")


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
        require_equal(row["square_root_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    verify_criterion(tables)
    verify_inspected_tables(tables)
    verify_obstruction_rows(tables, determinant_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_SQUARE_ROOT_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
