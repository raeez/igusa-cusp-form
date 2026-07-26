#!/usr/bin/env python3
"""Verify the row-280 reduced-gerbe alpha_red obstruction ledger."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_alpha_red_obstruction.v1"
EXPECTED_KIND = "rhomred_alpha_red_obstruction"
SUCCESS_STATUS = "RHOMRED_ALPHA_RED_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:alpha-red-vanishing-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_alpha_red")
W2_FIXTURE = Path("certificates/orientation/rhomred_w2")
COSECTION_FIXTURE = Path("certificates/orientation/k3_cosection_surjectivity")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
W2_STATUS = "RHOMRED_W2_FORMULA_OBSTRUCTION_VERIFIED"
COSECTION_STATUS = "K3_COSECTION_SURJECTIVITY_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_ROWS = {
    "alpha_red_R0_s3": ("Mss_R0_s3", "DerStack_R0_s3", "w2_R0_s3"),
    "alpha_red_R0_s2": ("Mss_R0_s2", "DerStack_R0_s2", "w2_R0_s2"),
    "alpha_red_R0_s1": ("Mss_R0_s1", "DerStack_R0_s1", "w2_R0_s1"),
}

EXPECTED_COVERAGE = {
    "retained_strata_count": 3,
    "criterion_count": 2,
    "determinant_w2_value_count": 0,
    "cokernel_rank_zero_count": 0,
    "cokernel_w2_value_count": 0,
    "alpha_red_value_count": 0,
    "alpha_red_vanishing_claim": 0,
    "null_homotopy_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "determinant_w2_value",
    "cokernel_rank_zero",
    "cokernel_w2_value",
    "cosection_pullback",
    "alpha_red_zero_sum",
    "alpha_red_quotient_borel_row",
    "null_homotopy",
    "orientation_square_root",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "determinant_w2_formula_only",
    "cosection_constructed_only",
    "cokernel_obstruction_only",
    "empty_quotient_borel_table",
    "claimed_null_homotopy_without_zero_class",
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
            "determinant_w2_required",
            "cokernel_rank_or_w2_required",
            "cosection_pullback_required",
            "zero_sum_required",
            "null_homotopy_required_for_row280",
            "alpha_red_value_supplied",
            "alpha_red_vanishing_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "alpha_red_obstruction_rows.csv",
        (
            "alpha_red_id",
            "substack_id",
            "derived_stack_id",
            "determinant_w2_id",
            "determinant_w2_value",
            "cokernel_row_id",
            "cokernel_rank_zero",
            "cokernel_w2_id",
            "cokernel_w2_value",
            "cosection_pullback_row_id",
            "alpha_red_value",
            "alpha_red_computed",
            "alpha_red_vanishing_verified",
            "null_homotopy_supplied",
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
            "alpha_red_status",
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

W2_COLUMNS = (
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
)

COSECTION_COKERNEL_COLUMNS = (
    "cokernel_row_id",
    "cosection_id",
    "substack_id",
    "cokernel_sheaf_id",
    "cokernel_rank",
    "rank_defect",
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
        "rhomred_w2_imported",
        "cosection_surjectivity_obstruction_imported",
        "orientation_obstruction_ledger_imported",
        "alpha_red_formula_recorded",
        "alpha_red_zero_criterion_recorded",
        "three_retained_strata_inspected",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "determinant_w2_values_supplied",
        "cokernel_rank_zero_rows_supplied",
        "cokernel_w2_values_supplied",
        "alpha_red_values_computed",
        "alpha_red_vanishing_verified",
        "null_homotopy_supplied",
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
        {str(W2_FIXTURE), str(COSECTION_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, dict[str, str]]:
    w2_manifest = read_json(W2_FIXTURE / "manifest.json")
    require_equal(w2_manifest.get("status"), W2_STATUS, "w2 status")
    require_equal(w2_manifest.get("w2_values_computed"), False, "w2 values computed")
    require_equal(w2_manifest.get("w2_vanishing_verified"), False, "w2 vanishing")

    cosection_manifest = read_json(COSECTION_FIXTURE / "manifest.json")
    require_equal(cosection_manifest.get("status"), COSECTION_STATUS, "cosection status")
    require_equal(cosection_manifest.get("cokernel_rows_empty"), True, "cokernel rows empty")
    require_equal(cosection_manifest.get("surjectivity_certification"), False, "surjectivity")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_LEDGER_STATUS,
        "orientation ledger",
    )
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty blocked")

    w2_rows = read_table_path(W2_FIXTURE / "w2_obstruction_rows.csv", W2_COLUMNS)
    indexed = rows_by(w2_rows, "w2_id", "imported w2 rows")
    for row in indexed.values():
        require_equal(row["w2_value"], "missing", f"{row['w2_id']} value")
        require_equal(bool_cell(row, "w2_computed"), False, f"{row['w2_id']} computed")
        require_equal(bool_cell(row, "w2_vanishing_verified"), False, f"{row['w2_id']} vanishing")

    cokernel_rows = read_table_path(
        COSECTION_FIXTURE / "cokernel_rows.csv",
        COSECTION_COKERNEL_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(cokernel_rows), 0, "cosection cokernel rows")

    quotient_borel_rows = read_table_path(
        ORIENTATION_FIXTURE / "quotient_borel.csv",
        QUOTIENT_BOREL_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(quotient_borel_rows), 0, "quotient Borel rows")

    orientation_rows = read_table_path(
        ORIENTATION_FIXTURE / "orientation_lines.csv",
        ORIENTATION_LINE_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(orientation_rows), 0, "orientation line rows")
    return indexed


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "rhomred_w2",
            "k3_cosection_surjectivity",
            "orientation_obstruction_ledger",
            "alpha_red_formula",
        },
        "source ids",
    )
    require_equal(rows["rhomred_w2"]["source_status"], W2_STATUS, "w2 source status")
    require_equal(
        rows["k3_cosection_surjectivity"]["source_status"],
        COSECTION_STATUS,
        "cosection source status",
    )
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source status",
    )
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criteria(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"alpha_red_zero_sum_criterion", "cokernel_zero_shortcut"}, "criterion ids")
    main = rows["alpha_red_zero_sum_criterion"]
    shortcut = rows["cokernel_zero_shortcut"]
    for row in rows.values():
        check_verified(row, "criterion_rows.csv")
        require_equal(bool_cell(row, "determinant_w2_required"), True, f"{row['criterion_id']} det w2")
        require_equal(bool_cell(row, "cokernel_rank_or_w2_required"), True, f"{row['criterion_id']} coker")
        require_equal(bool_cell(row, "zero_sum_required"), True, f"{row['criterion_id']} zero sum")
        require_equal(bool_cell(row, "null_homotopy_required_for_row280"), False, f"{row['criterion_id']} null")
        require_equal(bool_cell(row, "alpha_red_value_supplied"), False, f"{row['criterion_id']} value")
        require_equal(bool_cell(row, "alpha_red_vanishing_supplied"), False, f"{row['criterion_id']} vanish")
    require_equal(bool_cell(main, "cosection_pullback_required"), True, "main pullback")
    require_equal(bool_cell(shortcut, "cosection_pullback_required"), False, "shortcut pullback")


def verify_obstruction_rows(
    tables: dict[str, list[dict[str, str]]],
    w2_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["alpha_red_obstruction_rows.csv"], "alpha_red_id", "alpha-red rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "alpha-red obstruction ids")
    for alpha_id, (substack_id, derived_stack_id, w2_id) in EXPECTED_ROWS.items():
        row = rows[alpha_id]
        w2_row = w2_rows[w2_id]
        check_verified(row, "alpha_red_obstruction_rows.csv")
        require_equal(row["substack_id"], substack_id, f"{alpha_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{alpha_id} derived")
        require_equal(row["determinant_w2_id"], w2_id, f"{alpha_id} w2 id")
        require_equal(w2_row["substack_id"], substack_id, f"{w2_id} imported substack")
        for key in (
            "determinant_w2_value",
            "cokernel_row_id",
            "cokernel_w2_id",
            "cokernel_w2_value",
            "cosection_pullback_row_id",
            "alpha_red_value",
        ):
            require_equal(row[key], "missing", f"{alpha_id} {key}")
        require_equal(bool_cell(row, "cokernel_rank_zero"), False, f"{alpha_id} coker zero")
        require_equal(bool_cell(row, "alpha_red_computed"), False, f"{alpha_id} computed")
        require_equal(bool_cell(row, "alpha_red_vanishing_verified"), False, f"{alpha_id} vanishing")
        require_equal(bool_cell(row, "null_homotopy_supplied"), False, f"{alpha_id} null")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    require_equal(
        set(rows),
        {"quotient_borel", "orientation_lines", "cokernel_rows", "w2_obstruction_rows"},
        "inspected ids",
    )
    for table_id in ("quotient_borel", "orientation_lines", "cokernel_rows"):
        require_equal(int_cell(rows[table_id], "row_count"), 0, f"{table_id} count")
        require_equal(bool_cell(rows[table_id], "supplied"), False, f"{table_id} supplied")
    require_equal(int_cell(rows["w2_obstruction_rows"], "row_count"), 3, "w2 row count")
    require_equal(bool_cell(rows["w2_obstruction_rows"], "supplied"), False, "w2 supplied")
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
        require_equal(row["alpha_red_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    w2_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criteria(tables)
    verify_obstruction_rows(tables, w2_rows)
    verify_inspected_tables(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ALPHA_RED_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
