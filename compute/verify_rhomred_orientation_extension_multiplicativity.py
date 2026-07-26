#!/usr/bin/env python3
"""Verify the row-300 extension orientation multiplicativity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_extension_multiplicativity_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_extension_multiplicativity_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_EXTENSION_MULTIPLICATIVITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-extension-multiplicativity"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_extension_multiplicativity")
EXTENSION_FIXTURE = Path("certificates/moduli/retained_extension_closure")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
DIRECT_SUM_FIXTURE = Path("certificates/orientation/rhomred_orientation_direct_sum_multiplicativity")
MIXED_TS_FIXTURE = Path("certificates/hybrid/mixed_correspondence_thom_sebastiani")
ORIENTATION_LEDGER_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
DIRECT_SUM_STATUS = "RHOMRED_ORIENTATION_DIRECT_SUM_MULTIPLICATIVITY_OBSTRUCTION_VERIFIED"
MIXED_TS_STATUS = "MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "retained_extension_closure_rows": 4,
    "orientation_line_rows_supplied": 0,
    "ts_multiplicativity_rows_supplied": 0,
    "extension_ts_row_count": 0,
    "mixed_ts_orientation_hypotheses": 2,
    "mixed_ts_orientation_existence_claim": 0,
    "extension_multiplicativity_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "extension_stack",
    "reduced_dcritical_chart",
    "orientation_square_root",
    "determinant_comparison",
    "extension_ts_isomorphism",
    "coefficient_ts_compatibility",
    "ts_pentagon",
    "quotient_descent",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "compact_support_admissibility",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "retained_extension_closure_only",
    "direct_sum_orientation",
    "determinant_line_only",
    "conditional_mixed_thom_sebastiani",
    "vanishing_cycle_TS_without_orientation",
    "hall_product_formula",
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
            "extension_stack_required",
            "reduced_dcritical_chart_required",
            "orientation_square_roots_required",
            "determinant_comparison_required",
            "extension_ts_isomorphism_required",
            "coefficient_ts_compatibility_required",
            "two_step_flag_pentagon_required",
            "quotient_descent_required",
            "criterion_recorded",
            "extension_multiplicativity_proved",
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
        "extension_obstruction_rows.csv",
        (
            "obstruction_id",
            "retained_extension_closure_status",
            "extension_stack_status",
            "reduced_dcritical_chart_status",
            "orientation_square_roots_status",
            "determinant_comparison_status",
            "extension_ts_isomorphism_id",
            "coefficient_ts_status",
            "two_step_flag_pentagon_status",
            "extension_multiplicativity_proved",
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
            "extension_status",
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

EXTENSION_CLOSURE_COLUMNS = (
    "extension_closure_id",
    "window_id",
    "left_hn_type_id",
    "right_hn_type_id",
    "middle_hn_type_id",
    "middle_object_id",
    "extension_word_id",
    "retained_middle_term",
    "extension_closure_defect_rank",
    "geometric_source_id",
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

ORIENTATION_HYPOTHESIS_COLUMNS = (
    "hypothesis_id",
    "R_id",
    "order",
    "orientation_source",
    "orientation_transport_required",
    "orientation_existence_constructed",
    "o1_discharged",
    "orientation_defect_rank",
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
        "retained_extension_closure_imported",
        "orientation_obstruction_ledger_imported",
        "rhomred_square_root_obstruction_imported",
        "direct_sum_multiplicativity_obstruction_imported",
        "mixed_thom_sebastiani_packet_imported",
        "extension_multiplicativity_criterion_recorded",
        "orientation_tables_inspected",
        "extension_closure_rows_verified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "extension_stack_rows_supplied",
        "orientation_square_roots_supplied",
        "extension_ts_isomorphism_supplied",
        "determinant_comparison_supplied",
        "coefficient_system_ts_certified",
        "two_step_flag_pentagon_supplied",
        "quotient_descent",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(EXTENSION_FIXTURE),
            str(ORIENTATION_FIXTURE),
            str(SQUARE_ROOT_FIXTURE),
            str(DIRECT_SUM_FIXTURE),
            str(MIXED_TS_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    ext_manifest = read_json(EXTENSION_FIXTURE / "manifest.json")
    require_equal(ext_manifest.get("certified"), True, "extension closure certification")
    require_equal(ext_manifest.get("extension_closure"), True, "extension closure")
    require_equal(ext_manifest.get("extension_closure_defects_zero"), True, "extension closure defects")
    require_equal(ext_manifest.get("extension_flag_stacks"), False, "extension flag stacks")
    require_equal(ext_manifest.get("compact_hall_stage"), False, "compact hall stage")
    require_equal(ext_manifest.get("pfaffian_orientation"), False, "pfaffian orientation")

    orient_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(orient_manifest.get("obstruction_ledger_status"), ORIENTATION_LEDGER_STATUS, "orientation ledger")
    require_equal(orient_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orient_manifest.get("empty_blocked"), True, "orientation empty blocked")

    square_manifest = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square_manifest.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_equal(square_manifest.get("square_root_rows_supplied"), False, "square-root rows")

    direct_manifest = read_json(DIRECT_SUM_FIXTURE / "manifest.json")
    require_equal(direct_manifest.get("status"), DIRECT_SUM_STATUS, "direct-sum status")
    require_equal(direct_manifest.get("direct_sum_ts_isomorphism_supplied"), False, "direct-sum TS")

    mixed_manifest = read_json(MIXED_TS_FIXTURE / "manifest.json")
    require_equal(mixed_manifest.get("status"), MIXED_TS_STATUS, "mixed TS status")
    require_equal(mixed_manifest.get("conditional_on_orientation_transport"), True, "mixed TS orientation condition")
    require_equal(mixed_manifest.get("orientation_existence_certification"), False, "mixed TS orientation existence")
    require_equal(mixed_manifest.get("o1_discharge"), False, "mixed TS O1")

    extension_rows = read_table_path(
        EXTENSION_FIXTURE / "extension_closure.csv",
        EXTENSION_CLOSURE_COLUMNS,
    )
    require_equal(len(extension_rows), 4, "extension closure row count")
    for row in extension_rows:
        require_equal(bool_cell(row, "retained_middle_term"), True, f"{row['extension_closure_id']} retained")
        require_equal(int_cell(row, "extension_closure_defect_rank"), 0, f"{row['extension_closure_id']} defect")
        require_equal(row["check_status"], "verified", f"{row['extension_closure_id']} check")

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

    orientation_hypotheses = read_table_path(
        MIXED_TS_FIXTURE / "orientation_hypotheses.csv",
        ORIENTATION_HYPOTHESIS_COLUMNS,
    )
    require_equal(len(orientation_hypotheses), 2, "mixed TS orientation hypothesis count")
    for row in orientation_hypotheses:
        require_equal(bool_cell(row, "orientation_transport_required"), True, f"{row['hypothesis_id']} required")
        require_equal(bool_cell(row, "orientation_existence_constructed"), False, f"{row['hypothesis_id']} existence")
        require_equal(bool_cell(row, "o1_discharged"), False, f"{row['hypothesis_id']} O1")
        require_equal(int_cell(row, "orientation_defect_rank"), 0, f"{row['hypothesis_id']} defect")
        require_equal(row["check_status"], "verified", f"{row['hypothesis_id']} check")

    return {
        "extension_closure": len(extension_rows),
        "orientation_lines": len(orientation_rows),
        "ts_multiplicativity": len(ts_rows),
        "orientation_blocked": len(blocked_rows),
        "mixed_ts_orientation_hypotheses": len(orientation_hypotheses),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "retained_extension_closure",
            "orientation_obstruction_ledger",
            "rhomred_square_root",
            "direct_sum_multiplicativity",
            "mixed_thom_sebastiani",
            "extension_multiplicativity_criterion",
        },
        "source ids",
    )
    expected_status = {
        "retained_extension_closure": "RETAINED_EXTENSION_CLOSURE_VERIFIED",
        "orientation_obstruction_ledger": ORIENTATION_LEDGER_STATUS,
        "rhomred_square_root": SQUARE_ROOT_STATUS,
        "direct_sum_multiplicativity": DIRECT_SUM_STATUS,
        "mixed_thom_sebastiani": MIXED_TS_STATUS,
        "extension_multiplicativity_criterion": "proved_criterion",
    }
    for source_id, status in expected_status.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"extension_picard_groupoid_criterion"}, "criterion ids")
    row = rows["extension_picard_groupoid_criterion"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "extension_stack_required",
        "reduced_dcritical_chart_required",
        "orientation_square_roots_required",
        "determinant_comparison_required",
        "extension_ts_isomorphism_required",
        "coefficient_ts_compatibility_required",
        "two_step_flag_pentagon_required",
        "quotient_descent_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "extension_multiplicativity_proved"), False, "extension proved")


def verify_inspected_tables(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["inspected_orientation_tables.csv"], "table_id", "inspected tables")
    expected = {
        "retained_extension_closure": (counts["extension_closure"], True),
        "orientation_lines": (counts["orientation_lines"], False),
        "ts_multiplicativity": (counts["ts_multiplicativity"], False),
        "orientation_blocked_obligations": (counts["orientation_blocked"], True),
        "mixed_ts_orientation_hypotheses": (counts["mixed_ts_orientation_hypotheses"], True),
    }
    require_equal(set(rows), set(expected), "inspected table ids")
    for table_id, (count, supplied) in expected.items():
        row = rows[table_id]
        check_verified(row, "inspected_orientation_tables.csv")
        require_equal(int_cell(row, "row_count"), count, f"{table_id} count")
        require_equal(bool_cell(row, "supplied"), supplied, f"{table_id} supplied")


def verify_extension_obstructions(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["extension_obstruction_rows.csv"], "obstruction_id", "extension rows")
    require_equal(set(rows), {"extension_orientation_multiplicativity"}, "extension obstruction ids")
    row = rows["extension_orientation_multiplicativity"]
    check_verified(row, "extension_obstruction_rows.csv")
    require_equal(row["retained_extension_closure_status"], "verified_middle_terms_only", "closure status")
    for key in (
        "extension_stack_status",
        "reduced_dcritical_chart_status",
        "orientation_square_roots_status",
        "determinant_comparison_status",
        "two_step_flag_pentagon_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(row["extension_ts_isomorphism_id"], "missing", "TS id")
    require_equal(row["coefficient_ts_status"], "conditional_not_orientation_certification", "coefficient TS")
    require_equal(bool_cell(row, "extension_multiplicativity_proved"), False, "extension proved")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


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
        require_equal(row["extension_status"], "missing_open_obligation", f"{row['obligation_id']} status")


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
    verify_extension_obstructions(tables)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ORIENTATION_EXTENSION_MULTIPLICATIVITY_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
