#!/usr/bin/env python3
"""Verify the row-303 orientation/Hall-product descent packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_hall_product_descent_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_hall_product_descent_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_HALL_PRODUCT_DESCENT_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-descent-hall-product"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_hall_product_descent")

E_QUOTIENT_FIXTURE = Path("certificates/orientation/rhomred_orientation_e_quotient_descent")
ORIENTATION_TS_FIXTURE = Path("certificates/orientation/rhomred_orientation_thom_sebastiani_compatibility")
EXTENSION_FIXTURE = Path("certificates/orientation/rhomred_orientation_extension_multiplicativity")
THETA_MU_FIXTURE = Path("certificates/hybrid/quotient_after_correspondence_theta_mu_comparison")
QUOTIENT_TS_FIXTURE = Path("certificates/hybrid/quotient_after_correspondence_thom_sebastiani")
TRANSITION_PRODUCT_FIXTURE = Path("certificates/hall/transition_hall_product_preservation")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

E_QUOTIENT_STATUS = "RHOMRED_ORIENTATION_E_QUOTIENT_DESCENT_OBSTRUCTION_VERIFIED"
ORIENTATION_TS_STATUS = "RHOMRED_ORIENTATION_THOM_SEBASTIANI_COMPATIBILITY_OBSTRUCTION_VERIFIED"
EXTENSION_STATUS = "RHOMRED_ORIENTATION_EXTENSION_MULTIPLICATIVITY_OBSTRUCTION_VERIFIED"
THETA_MU_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED"
QUOTIENT_TS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED"
TRANSITION_PRODUCT_STATUS = "TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "theta_mu_rows_available": 1,
    "quotient_ts_rows_available": 1,
    "pushforward_descent_rows_available": 1,
    "quotient_orientation_rows_supplied": 0,
    "orientation_ts_rows_supplied": 0,
    "extension_cocycle_comparison_rows_supplied": 0,
    "source_hall_product_matrix_rows_supplied": 0,
    "hall_product_descent_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "quotient_orientation_rows",
    "extension_cocycle_comparison",
    "oriented_ts_isomorphism",
    "determinant_square_compatibility",
    "two_step_flag_pentagon",
    "source_hall_product_row",
    "operation_descent_interface",
    "compact_support_pushforward_descent",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "theta_mu_only",
    "quotient_Thom_Sebastiani_only",
    "zero_class_only",
    "empty_product_matrix",
    "scalar_trace",
    "denominator_product",
    "pfaffian_product",
    "orientation_line_only",
    "vanishing_cycle_transport_only",
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
            "quotient_orientation_required",
            "extension_cocycle_comparison_required",
            "oriented_ts_required",
            "external_product_descent_required",
            "compact_support_pushforward_descent_required",
            "theta_mu_required",
            "two_step_flag_pentagon_required",
            "source_hall_product_row_required",
            "criterion_recorded",
            "hall_product_descent_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "imported_status_rows.csv",
        (
            "import_id",
            "import_path",
            "import_status",
            "positive_input",
            "missing_input",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "product_descent_obstruction_rows.csv",
        (
            "obstruction_id",
            "quotient_orientation_status",
            "extension_cocycle_comparison_status",
            "orientation_ts_status",
            "external_product_descent_status",
            "compact_support_pushforward_status",
            "theta_mu_status",
            "source_product_matrix_status",
            "two_step_flag_pentagon_status",
            "hall_product_descent_proved",
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
            "hall_product_descent_status",
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


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"json root is not an object: {path}")
    return value


def read_table_path(
    path: Path,
    columns: tuple[str, ...] | None = None,
    *,
    allow_empty: bool = False,
) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if columns is not None and tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = []
        for row in reader:
            normalized = {
                key: (value or "").strip()
                for key, value in row.items()
                if key is not None
            }
            if any(normalized.values()):
                rows.append(normalized)
    if not rows and not allow_empty:
        raise ValueError(f"{path}: expected at least one row")
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
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def count_data_rows(path: Path) -> int:
    return len(read_table_path(path, None, allow_empty=True))


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "e_quotient_descent_imported",
        "orientation_thom_sebastiani_imported",
        "orientation_extension_multiplicativity_imported",
        "theta_mu_comparison_imported",
        "quotient_thom_sebastiani_imported",
        "transition_hall_product_imported",
        "compact_hall_source_imported",
        "hall_product_descent_criterion_recorded",
        "theta_mu_available_for_supplied_operation_rows",
        "quotient_thom_sebastiani_available_for_supplied_ts_rows",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "quotient_orientation_rows_supplied",
        "extension_cocycle_comparison_supplied",
        "oriented_ts_isomorphism_supplied",
        "source_hall_product_rows_supplied",
        "hall_product_descent",
        "transition_compatibility",
        "protected_integration",
        "aggregate_hybrid_population",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(E_QUOTIENT_FIXTURE),
            str(ORIENTATION_TS_FIXTURE),
            str(EXTENSION_FIXTURE),
            str(THETA_MU_FIXTURE),
            str(QUOTIENT_TS_FIXTURE),
            str(TRANSITION_PRODUCT_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    e_manifest = read_json(E_QUOTIENT_FIXTURE / "manifest.json")
    require_equal(e_manifest.get("status"), E_QUOTIENT_STATUS, "E quotient status")
    require_equal(e_manifest.get("quotient_orientation"), False, "E quotient orientation")
    require_equal(e_manifest.get("quotient_borel_rows_supplied"), False, "quotient Borel rows")
    require_equal(e_manifest.get("finite_stabilizer_rows_supplied"), False, "finite stabilizer rows")

    ts_manifest = read_json(ORIENTATION_TS_FIXTURE / "manifest.json")
    require_equal(ts_manifest.get("status"), ORIENTATION_TS_STATUS, "orientation TS status")
    require_equal(ts_manifest.get("orientation_ts_isomorphism_supplied"), False, "orientation TS row")
    require_equal(ts_manifest.get("coefficient_system_compatibility_supplied"), False, "coefficient TS row")
    require_equal(ts_manifest.get("quotient_descent"), False, "orientation TS quotient descent")
    require_equal(ts_manifest.get("two_step_flag_pentagon_supplied"), False, "TS pentagon row")

    ext_manifest = read_json(EXTENSION_FIXTURE / "manifest.json")
    require_equal(ext_manifest.get("status"), EXTENSION_STATUS, "extension status")
    require_equal(ext_manifest.get("extension_stack_rows_supplied"), False, "extension stack rows")
    require_equal(ext_manifest.get("extension_ts_isomorphism_supplied"), False, "extension TS rows")
    require_equal(ext_manifest.get("quotient_descent"), False, "extension quotient descent")

    theta_manifest = read_json(THETA_MU_FIXTURE / "manifest.json")
    require_equal(theta_manifest.get("status"), THETA_MU_STATUS, "theta_mu status")
    require_equal(theta_manifest.get("operation_comparison_constructed"), True, "theta_mu comparison")
    require_equal(theta_manifest.get("theta_mu_defect_rank"), 0, "theta_mu defect")
    require_equal(theta_manifest.get("protected_integration_certification"), False, "theta_mu integration")
    require_equal(theta_manifest.get("aggregate_hybrid_population"), False, "theta_mu aggregate")

    quotient_ts_manifest = read_json(QUOTIENT_TS_FIXTURE / "manifest.json")
    require_equal(quotient_ts_manifest.get("status"), QUOTIENT_TS_STATUS, "quotient TS status")
    require_equal(quotient_ts_manifest.get("thom_sebastiani_preservation_proved"), True, "quotient TS proved")
    require_equal(quotient_ts_manifest.get("orientation_existence_certification"), False, "orientation existence")
    require_equal(quotient_ts_manifest.get("compact_support_pushforward_base_change"), False, "compact support base change")
    require_equal(quotient_ts_manifest.get("aggregate_hybrid_population"), False, "quotient TS aggregate")

    transition_manifest = read_json(TRANSITION_PRODUCT_FIXTURE / "manifest.json")
    require_equal(transition_manifest.get("status"), TRANSITION_PRODUCT_STATUS, "transition product status")
    require_equal(transition_manifest.get("hall_product_transition_certification"), False, "product transition")
    require_equal(transition_manifest.get("mathematical_certification"), False, "transition product math")

    compact_manifest = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_manifest.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_equal(compact_manifest.get("empty_blocked"), True, "compact source empty")
    require_equal(compact_manifest.get("compact_source_recognition"), False, "compact source recognition")
    require_equal(compact_manifest.get("mathematical_certification"), False, "compact source math")

    compact_blocked = rows_by(
        read_table_path(COMPACT_SOURCE_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "compact source obligations",
    )
    if "hall_product_M" not in compact_blocked:
        raise ValueError("compact source ledger missing hall_product_M")
    require_equal(
        compact_blocked["hall_product_M"]["source_status"],
        "missing_open_obligation",
        "hall_product_M source_status",
    )
    require_equal(compact_blocked["hall_product_M"]["check_status"], "verified", "hall_product_M check")

    return {
        "theta_mu_rows": count_data_rows(THETA_MU_FIXTURE / "theta_mu_rows.csv"),
        "quotient_ts_rows": count_data_rows(QUOTIENT_TS_FIXTURE / "thom_sebastiani_rows.csv"),
        "pushforward_descent_rows": count_data_rows(THETA_MU_FIXTURE / "pushforward_descent_rows.csv"),
        "m_entries": count_data_rows(COMPACT_SOURCE_FIXTURE / "M_entries.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "e_quotient_descent": E_QUOTIENT_STATUS,
        "orientation_thom_sebastiani": ORIENTATION_TS_STATUS,
        "orientation_extension_multiplicativity": EXTENSION_STATUS,
        "theta_mu_comparison": THETA_MU_STATUS,
        "quotient_thom_sebastiani": QUOTIENT_TS_STATUS,
        "transition_hall_product": TRANSITION_PRODUCT_STATUS,
        "compact_hall_source": COMPACT_SOURCE_STATUS,
        "hall_product_descent_criterion": "proved_criterion",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"orientation_hall_product_descent"}, "criterion ids")
    row = rows["orientation_hall_product_descent"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "quotient_orientation_required",
        "extension_cocycle_comparison_required",
        "oriented_ts_required",
        "external_product_descent_required",
        "compact_support_pushforward_descent_required",
        "theta_mu_required",
        "two_step_flag_pentagon_required",
        "source_hall_product_row_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "hall_product_descent_proved"), False, "product descent proved")


def verify_imported_status_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["imported_status_rows.csv"], "import_id", "imported rows")
    expected = {
        "row302_quotient_orientation": E_QUOTIENT_STATUS,
        "row301_oriented_ts": ORIENTATION_TS_STATUS,
        "row300_extension_ts": EXTENSION_STATUS,
        "theta_mu": THETA_MU_STATUS,
        "quotient_TS": QUOTIENT_TS_STATUS,
        "transition_product": TRANSITION_PRODUCT_STATUS,
        "compact_source": COMPACT_SOURCE_STATUS,
    }
    require_equal(set(rows), set(expected), "import ids")
    for import_id, status in expected.items():
        row = rows[import_id]
        require_equal(row["import_status"], status, f"{import_id} status")
        check_verified(row, "imported_status_rows.csv")
        if not row["positive_input"] or not row["missing_input"]:
            raise ValueError(f"{import_id}: missing positive or missing input description")


def verify_obstruction_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["product_descent_obstruction_rows.csv"], "obstruction_id", "obstruction rows")
    require_equal(set(rows), {"orientation_hall_product_descent"}, "obstruction ids")
    row = rows["orientation_hall_product_descent"]
    check_verified(row, "product_descent_obstruction_rows.csv")
    for key in (
        "quotient_orientation_status",
        "extension_cocycle_comparison_status",
        "orientation_ts_status",
        "source_product_matrix_status",
        "two_step_flag_pentagon_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(row["external_product_descent_status"], "available_conditional_input", "external product descent")
    require_equal(row["compact_support_pushforward_status"], "available_conditional_input", "compact support")
    require_equal(row["theta_mu_status"], "available_for_supplied_operation_rows", "theta_mu")
    require_equal(bool_cell(row, "hall_product_descent_proved"), False, "descent proved")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["theta_mu_rows_available"] = counts["theta_mu_rows"]
    computed["quotient_ts_rows_available"] = counts["quotient_ts_rows"]
    computed["pushforward_descent_rows_available"] = counts["pushforward_descent_rows"]
    computed["source_hall_product_matrix_rows_supplied"] = counts["m_entries"]
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(int_cell(row, "computed_value"), computed[coverage_id], f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(row["hall_product_descent_status"], "missing_open_obligation", f"{row['obligation_id']} status")
        require_equal(row["check_status"], "verified", f"{row['obligation_id']} check")
        if not row["mathematical_payload"] or not row["why_required"]:
            raise ValueError(f"{row['obligation_id']}: missing payload or reason")


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
    verify_imported_status_rows(tables)
    verify_obstruction_rows(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ORIENTATION_HALL_PRODUCT_DESCENT_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
