#!/usr/bin/env python3
"""Verify Joyce d-critical truncations of retained finite derived substacks."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "JOYCE_DCRITICAL_TRUNCATION_VERIFIED"
EXPECTED_SCHEMA = "joyce_dcritical_truncation.v1"
EXPECTED_KIND = "joyce_dcritical_truncation_input"
DEFAULT_FIXTURE = Path("certificates/orientation/joyce_dcritical_truncation")
PTVV_FIXTURE = Path("certificates/orientation/ptvv_finite_substack_symplectic")
PROOF_LABEL = "prop:joyce-dcritical-truncation"
EXPECTED_ROWS = {
    "dcrit_R0_s3": ("ptvv_R0_s3", "Mss_R0_s3", "DerStack_R0_s3", "PTVV_omega_R0_s3"),
    "dcrit_R0_s2": ("ptvv_R0_s2", "Mss_R0_s2", "DerStack_R0_s2", "PTVV_omega_R0_s2"),
    "dcrit_R0_s1": ("ptvv_R0_s1", "Mss_R0_s1", "DerStack_R0_s1", "PTVV_omega_R0_s1"),
}
EXPECTED_COVERAGE = {
    "dcritical_row_count": 3,
    "dcritical_defects": 0,
    "bbdjs_source_count": 1,
    "ptvv_import_count": 3,
    "vanishing_cycle_claim": 0,
    "cosection_claim": 0,
    "orientation_claim": 0,
    "transition_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "vanishing_cycle_complex",
    "k3_semiregularity_cosection",
    "cosection_surjectivity",
    "rhom_red",
    "perfect_reduced_obstruction",
    "det_rhom_red",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "protected_integration",
}
REQUIRED_FIREWALL = {
    "ptvv_form_only",
    "vanishing_cycle_complex",
    "k3_semiregularity_cosection",
    "cosection_surjectivity",
    "RHomred",
    "det_RHomred",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "protected_integration",
    "scalar_trace",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


PTVV_COLUMNS = (
    "row_id",
    "substack_id",
    "derived_stack_id",
    "shifted_symplectic_form_id",
    "shifted_degree",
    "cotangent_amplitude",
    "symplectic_defect_rank",
    "orientation_input",
    "proof_reference",
    "check_status",
    "notes",
)


TABLE_SPECS = (
    TableSpec(
        "bbdjs_source_rows.csv",
        (
            "source_id",
            "citation_key",
            "source_theorem",
            "input_shifted_degree",
            "output_structure",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "dcritical_truncation_rows.csv",
        (
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
            "dcritical_status",
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
    for key in (
        "ptvv_finite_substack_input_imported",
        "bbdjs_source_theorem_imported",
        "dcritical_truncations_constructed",
        "three_substacks_verified",
        "dcritical_defect_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "vanishing_cycle_complex",
        "k3_semiregularity_cosection",
        "cosection_surjectivity",
        "rhom_red",
        "det_rhom_red",
        "orientation_square_root",
        "quotient_orientation",
        "transition_compatibility",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "tables")
    require_equal(manifest.get("imports"), [str(PTVV_FIXTURE)], "imports")


def verify_import_manifest() -> None:
    manifest = read_json(PTVV_FIXTURE / "manifest.json")
    require_equal(manifest.get("status"), "PTVV_FINITE_SUBSTACK_SYMPLECTIC_VERIFIED", "PTVV packet status")
    require_equal(manifest.get("finite_substack_symplectic_forms"), True, "PTVV forms")
    require_equal(manifest.get("joyce_dcritical_truncation"), False, "PTVV packet d-critical firewall")


def verify_source(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "BBDJS source row count")
    row = rows[0]
    check_verified(row, "bbdjs_source_rows.csv")
    require_equal(row["citation_key"], "BBDJS2015", "citation key")
    require_equal(row["source_theorem"], "Theorem_6_9", "source theorem")
    require_equal(int_cell(row, "input_shifted_degree"), -1, "input shifted degree")
    require_equal(row["output_structure"], "Joyce_dcritical_structure_on_classical_truncation", "output")


def verify_truncations(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "truncation_id", "dcritical_truncation_rows.csv")
    require_equal(set(indexed), set(EXPECTED_ROWS), "d-critical row coverage")
    ptvv_rows = rows_by(read_table_path(PTVV_FIXTURE / "ptvv_rows.csv", PTVV_COLUMNS), "row_id", "ptvv_rows.csv")
    for truncation_id, (ptvv_row_id, substack_id, derived_stack_id, form_id) in EXPECTED_ROWS.items():
        row = indexed[truncation_id]
        check_verified(row, "dcritical_truncation_rows.csv")
        require_equal(row["ptvv_row_id"], ptvv_row_id, f"{truncation_id} PTVV row")
        require_equal(row["substack_id"], substack_id, f"{truncation_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{truncation_id} derived stack")
        require_equal(row["classical_truncation_id"], f"t0_{derived_stack_id}", f"{truncation_id} truncation id")
        require_equal(row["dcritical_structure_id"], f"s_{derived_stack_id}", f"{truncation_id} d-critical id")
        require_equal(row["shifted_symplectic_form_id"], form_id, f"{truncation_id} form")
        require_equal(int_cell(row, "dcritical_defect_rank"), 0, f"{truncation_id} defect")
        require_equal(bool_cell(row, "vanishing_cycle_constructed"), False, f"{truncation_id} vanishing cycle")
        require_equal(bool_cell(row, "orientation_constructed"), False, f"{truncation_id} orientation")

        ptvv = ptvv_rows[ptvv_row_id]
        require_equal(ptvv["substack_id"], substack_id, f"{truncation_id} imported substack")
        require_equal(ptvv["derived_stack_id"], derived_stack_id, f"{truncation_id} imported derived stack")
        require_equal(ptvv["shifted_symplectic_form_id"], form_id, f"{truncation_id} imported form")
        require_equal(int_cell(ptvv, "shifted_degree"), -1, f"{truncation_id} imported degree")
        require_equal(int_cell(ptvv, "symplectic_defect_rank"), 0, f"{truncation_id} imported symplectic defect")


def verify_coverage(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = indexed[coverage_id]
        check_verified(row, "coverage_rows.csv")
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_blocked(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "obligation_id", "blocked_obligations.csv")
    require_equal(set(indexed), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, row in indexed.items():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        require_equal(row["dcritical_status"], "missing_open_obligation", f"{obligation_id} status")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect")
    require_equal(seen, REQUIRED_FIREWALL, "firewall substitutes")


def verify_fixture(fixture: Path) -> None:
    verify_manifest(fixture)
    verify_import_manifest()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_source(tables["bbdjs_source_rows.csv"])
    verify_truncations(tables["dcritical_truncation_rows.csv"])
    verify_coverage(tables["coverage_rows.csv"])
    verify_blocked(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"JOYCE_DCRITICAL_TRUNCATION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
