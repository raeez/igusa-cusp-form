#!/usr/bin/env python3
"""Verify the row-299 direct-sum orientation multiplicativity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_direct_sum_multiplicativity_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_direct_sum_multiplicativity_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_DIRECT_SUM_MULTIPLICATIVITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-direct-sum-multiplicativity"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_direct_sum_multiplicativity")
DETERMINANT_FIXTURE = Path("certificates/orientation/rhomred_determinant")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
DETERMINANT_STATUS = "RHOMRED_DETERMINANT_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "determinant_packet_count": 1,
    "determinant_line_count": 3,
    "square_root_obstruction_packet_count": 1,
    "orientation_line_rows_supplied": 0,
    "ts_multiplicativity_rows_supplied": 0,
    "direct_sum_ts_row_count": 0,
    "cross_trivialization_count": 0,
    "direct_sum_multiplicativity_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "reduced_cone_direct_sum_decomposition",
    "orientation_square_root",
    "orientation_class_zero",
    "hyperbolic_cross_trivialization",
    "direct_sum_ts_isomorphism",
    "symmetric_functoriality",
    "ts_pentagon",
    "extension_multiplicativity",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "determinant_line_only",
    "determinant_product",
    "square_root_existence_only",
    "euler_characteristic_additivity",
    "hall_product_without_orientation",
    "scalar_trace",
    "maass_character_value",
    "op_scalar_branch",
    "protected_integration",
}

REQUIRED_ORIENTATION_BLOCKED = {
    "orientation_square_root",
    "orientation_class_zero",
    "ts_multiplicativity",
    "ts_pentagon",
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
            "block_decomposition_required",
            "reduced_cone_additivity_required",
            "orientation_square_roots_required",
            "hyperbolic_cross_trivialization_required",
            "direct_sum_ts_isomorphism_required",
            "picard_groupoid_isomorphism_required",
            "symmetric_functoriality_required",
            "pentagon_coherence_required",
            "criterion_recorded",
            "direct_sum_multiplicativity_proved",
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
        "direct_sum_obstruction_rows.csv",
        (
            "obstruction_id",
            "block_decomposition_status",
            "reduced_cone_additivity_status",
            "orientation_square_roots_status",
            "cross_term_square_root_status",
            "direct_sum_ts_isomorphism_id",
            "multiplicativity_row_supplied",
            "pentagon_defect_rank_zero",
            "extension_multiplicativity_supplied",
            "mathematical_certification",
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
            "direct_sum_status",
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

TS_COLUMNS = (
    "check_id",
    "extension_stack_id",
    "left_line_id",
    "right_line_id",
    "target_line_id",
    "ts_isomorphism_id",
    "pentagon_defect_rank",
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

SQUARE_ROOT_BLOCKED_COLUMNS = (
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
        "rhomred_determinant_imported",
        "rhomred_square_root_obstruction_imported",
        "orientation_obstruction_ledger_imported",
        "direct_sum_criterion_recorded",
        "orientation_tables_inspected",
        "missing_ts_rows_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_square_roots_supplied",
        "reduced_cone_direct_sum_decomposition_supplied",
        "direct_sum_ts_isomorphism_supplied",
        "hyperbolic_cross_trivialization_supplied",
        "pentagon_coherence_supplied",
        "extension_multiplicativity_supplied",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(DETERMINANT_FIXTURE), str(SQUARE_ROOT_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    det_manifest = read_json(DETERMINANT_FIXTURE / "manifest.json")
    require_equal(det_manifest.get("status"), DETERMINANT_STATUS, "determinant status")
    require_equal(det_manifest.get("determinant_lines_defined"), True, "determinant lines defined")
    require_equal(det_manifest.get("orientation_square_root"), False, "determinant packet square root")

    square_manifest = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square_manifest.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_equal(square_manifest.get("square_root_criterion_recorded"), True, "square-root criterion")
    require_equal(square_manifest.get("square_root_rows_supplied"), False, "square-root rows")
    require_equal(square_manifest.get("mathematical_certification"), False, "square-root certification")

    orient_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(orient_manifest.get("obstruction_ledger_status"), ORIENTATION_LEDGER_STATUS, "orientation ledger")
    require_equal(orient_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orient_manifest.get("empty_blocked"), True, "orientation empty blocked")

    determinant_rows = read_table_path(DETERMINANT_FIXTURE / "determinant_rows.csv", DETERMINANT_COLUMNS)
    require_equal(len(determinant_rows), 3, "determinant row count")
    for row in determinant_rows:
        require_equal(bool_cell(row, "determinant_defined"), True, f"{row['determinant_id']} determinant")
        require_equal(bool_cell(row, "square_root_constructed"), False, f"{row['determinant_id']} square root")
        require_equal(bool_cell(row, "orientation_constructed"), False, f"{row['determinant_id']} orientation")

    orientation_rows = read_table_path(
        ORIENTATION_FIXTURE / "orientation_lines.csv",
        ORIENTATION_LINE_COLUMNS,
        allow_empty=True,
    )
    ts_rows = read_table_path(
        ORIENTATION_FIXTURE / "ts_multiplicativity.csv",
        TS_COLUMNS,
        allow_empty=True,
    )
    require_equal(len(orientation_rows), 0, "orientation line row count")
    require_equal(len(ts_rows), 0, "ts multiplicativity row count")

    blocked_rows = read_table_path(
        ORIENTATION_FIXTURE / "blocked_obligations.csv",
        ORIENTATION_BLOCKED_COLUMNS,
    )
    blocked = rows_by(blocked_rows, "obligation_id", "orientation blocked obligations")
    missing = REQUIRED_ORIENTATION_BLOCKED - set(blocked)
    if missing:
        raise ValueError("orientation ledger missing required obligations: " + ", ".join(sorted(missing)))
    for obligation_id in REQUIRED_ORIENTATION_BLOCKED:
        row = blocked[obligation_id]
        require_equal(row["orientation_status"], "missing_open_obligation", f"{obligation_id} status")
        require_equal(row["check_status"], "verified", f"{obligation_id} check")

    square_blocked = read_table_path(
        SQUARE_ROOT_FIXTURE / "blocked_obligations.csv",
        SQUARE_ROOT_BLOCKED_COLUMNS,
    )
    square_blocked_index = rows_by(square_blocked, "obligation_id", "square-root blocked obligations")
    require_equal(
        square_blocked_index["orientation_square_root"]["square_root_status"],
        "missing_open_obligation",
        "square-root obligation status",
    )
    require_equal(
        square_blocked_index["ts_multiplicativity"]["square_root_status"],
        "missing_open_obligation",
        "square-root TS status",
    )

    return {
        "determinant_rows": len(determinant_rows),
        "orientation_lines": len(orientation_rows),
        "ts_multiplicativity": len(ts_rows),
        "orientation_blocked": len(blocked_rows),
        "square_root_blocked": len(square_blocked),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {"rhomred_determinant", "rhomred_square_root", "orientation_obstruction_ledger", "direct_sum_criterion"},
        "source ids",
    )
    require_equal(rows["rhomred_determinant"]["source_status"], DETERMINANT_STATUS, "det source status")
    require_equal(rows["rhomred_square_root"]["source_status"], SQUARE_ROOT_STATUS, "square source status")
    require_equal(
        rows["orientation_obstruction_ledger"]["source_status"],
        ORIENTATION_LEDGER_STATUS,
        "orientation source status",
    )
    require_equal(rows["direct_sum_criterion"]["source_status"], "proved_criterion", "criterion status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"direct_sum_picard_groupoid_criterion"}, "criterion ids")
    row = rows["direct_sum_picard_groupoid_criterion"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "block_decomposition_required",
        "reduced_cone_additivity_required",
        "orientation_square_roots_required",
        "hyperbolic_cross_trivialization_required",
        "direct_sum_ts_isomorphism_required",
        "picard_groupoid_isomorphism_required",
        "symmetric_functoriality_required",
        "pentagon_coherence_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "direct_sum_multiplicativity_proved"), False, "direct-sum proved")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "rhomred_determinant_rows": (counts["determinant_rows"], True),
        "rhomred_square_root_blocked": (counts["square_root_blocked"], True),
        "orientation_lines": (counts["orientation_lines"], False),
        "ts_multiplicativity": (counts["ts_multiplicativity"], False),
        "orientation_blocked_obligations": (counts["orientation_blocked"], True),
    }
    require_equal(set(rows), set(expected), "inspected table ids")
    for table_id, (count, supplied) in expected.items():
        row = rows[table_id]
        check_verified(row, "inspected_orientation_tables.csv")
        require_equal(int_cell(row, "row_count"), count, f"{table_id} count")
        require_equal(bool_cell(row, "supplied"), supplied, f"{table_id} supplied")


def verify_direct_sum_obstructions(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["direct_sum_obstruction_rows.csv"], "obstruction_id", "direct-sum rows")
    require_equal(set(rows), {"direct_sum_orientation_multiplicativity"}, "direct-sum obstruction ids")
    row = rows["direct_sum_orientation_multiplicativity"]
    check_verified(row, "direct_sum_obstruction_rows.csv")
    require_equal(row["block_decomposition_status"], "criterion_only", "block decomposition status")
    for key in (
        "reduced_cone_additivity_status",
        "orientation_square_roots_status",
        "cross_term_square_root_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(row["direct_sum_ts_isomorphism_id"], "missing", "TS isomorphism id")
    for key in (
        "multiplicativity_row_supplied",
        "pentagon_defect_rank_zero",
        "extension_multiplicativity_supplied",
        "mathematical_certification",
    ):
        require_equal(bool_cell(row, key), False, key)


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
            row["direct_sum_status"],
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
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_inspected_tables(tables, counts)
    verify_direct_sum_obstructions(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ORIENTATION_DIRECT_SUM_MULTIPLICATIVITY_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
