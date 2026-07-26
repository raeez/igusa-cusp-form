#!/usr/bin/env python3
"""Verify the PTVV (-1)-shifted symplectic input on finite substacks."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "PTVV_FINITE_SUBSTACK_SYMPLECTIC_VERIFIED"
EXPECTED_SCHEMA = "ptvv_finite_substack_symplectic.v1"
EXPECTED_KIND = "ptvv_finite_substack_symplectic_input"
DEFAULT_FIXTURE = Path("certificates/orientation/ptvv_finite_substack_symplectic")
DERIVED_FIXTURE = Path("certificates/moduli/retained_derived_enhancements")
PROOF_LABEL = "prop:ptvv-finite-substack-symplectic"
EXPECTED_ROWS = {
    "ptvv_R0_s3": ("Mss_R0_s3", "DerStack_R0_s3", "PTVV_omega_R0_s3"),
    "ptvv_R0_s2": ("Mss_R0_s2", "DerStack_R0_s2", "PTVV_omega_R0_s2"),
    "ptvv_R0_s1": ("Mss_R0_s1", "DerStack_R0_s1", "PTVV_omega_R0_s1"),
}
EXPECTED_COVERAGE = {
    "ptvv_row_count": 3,
    "shifted_degree": -1,
    "cotangent_amplitude": 3,
    "symplectic_defects": 0,
    "joyce_dcritical_claim": 0,
    "cosection_claim": 0,
    "orientation_square_root_claim": 0,
    "quotient_orientation_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "joyce_dcritical_truncation",
    "k3_semiregularity_cosection",
    "cosection_surjectivity",
    "rhom_red",
    "perfect_reduced_obstruction",
    "det_rhom_red",
    "orientation_square_root",
    "quotient_orientation",
    "protected_integration",
}
REQUIRED_FIREWALL = {
    "joyce_dcritical_truncation",
    "k3_semiregularity_cosection",
    "cosection_surjectivity",
    "RHomred",
    "det_RHomred",
    "orientation_square_root",
    "quotient_orientation",
    "o2_wall_atlas",
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
DERIVED_COLUMNS = (
    "enhancement_id",
    "substack_id",
    "derived_stack_id",
    "shifted_symplectic_form_id",
    "quasi_smooth_status",
    "cotangent_amplitude",
    "tor_amplitude_defect_rank",
    "symplectic_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
SYMPLECTIC_COLUMNS = (
    "symplectic_id",
    "enhancement_id",
    "shifted_symplectic_form_id",
    "shifted_degree",
    "restriction_status",
    "symplectic_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)


TABLE_SPECS = (
    TableSpec("ptvv_rows.csv", PTVV_COLUMNS),
    TableSpec(
        "orientation_input_rows.csv",
        (
            "input_id",
            "source_packet",
            "source_status",
            "source_theorem",
            "imported_rows",
            "expected_rows",
            "defect_rank",
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
            "ptvv_status",
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
        "ptvv_source_theorem_imported",
        "retained_derived_enhancements_imported",
        "finite_substack_symplectic_forms",
        "three_substacks_verified",
        "quasi_smooth_amplitude_verified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "joyce_dcritical_truncation",
        "k3_semiregularity_cosection",
        "cosection_surjectivity",
        "rhom_red",
        "det_rhom_red",
        "orientation_square_root",
        "quotient_orientation",
        "o2_wall_atlas",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "tables")
    require_equal(manifest.get("imports"), [str(DERIVED_FIXTURE)], "imports")


def verify_import_manifest() -> None:
    manifest = read_json(DERIVED_FIXTURE / "manifest.json")
    require_equal(manifest.get("certified"), True, "derived packet certified")
    require_equal(manifest.get("quasi_smooth_derived_enhancements"), True, "quasi-smooth imports")
    require_equal(manifest.get("cosection_atlas"), False, "derived packet cosection firewall")
    require_equal(manifest.get("pfaffian_orientation"), False, "derived packet orientation firewall")


def verify_ptvv_rows(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "row_id", "ptvv_rows.csv")
    require_equal(set(indexed), set(EXPECTED_ROWS), "PTVV row coverage")
    derived_rows = rows_by(
        read_table_path(DERIVED_FIXTURE / "derived_enhancements.csv", DERIVED_COLUMNS),
        "substack_id",
        "derived_enhancements.csv",
    )
    symplectic_by_form = rows_by(
        read_table_path(DERIVED_FIXTURE / "symplectic_rows.csv", SYMPLECTIC_COLUMNS),
        "shifted_symplectic_form_id",
        "symplectic_rows.csv",
    )
    for row_id, (substack_id, derived_stack_id, form_id) in EXPECTED_ROWS.items():
        row = indexed[row_id]
        check_verified(row, "ptvv_rows.csv")
        require_equal(row["substack_id"], substack_id, f"{row_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{row_id} derived stack")
        require_equal(row["shifted_symplectic_form_id"], form_id, f"{row_id} form")
        require_equal(int_cell(row, "shifted_degree"), -1, f"{row_id} shifted degree")
        require_equal(row["cotangent_amplitude"], "[-1,0]", f"{row_id} amplitude")
        require_equal(int_cell(row, "symplectic_defect_rank"), 0, f"{row_id} symplectic defect")
        require_equal(bool_cell(row, "orientation_input"), True, f"{row_id} orientation input")

        derived = derived_rows[substack_id]
        require_equal(derived["derived_stack_id"], derived_stack_id, f"{row_id} imported derived stack")
        require_equal(derived["shifted_symplectic_form_id"], form_id, f"{row_id} imported form")
        require_equal(derived["quasi_smooth_status"], "quasi_smooth_verified", f"{row_id} quasi smooth")
        require_equal(derived["cotangent_amplitude"], "[-1,0]", f"{row_id} imported amplitude")
        require_equal(int_cell(derived, "tor_amplitude_defect_rank"), 0, f"{row_id} tor defect")
        require_equal(int_cell(derived, "symplectic_defect_rank"), 0, f"{row_id} imported symplectic defect")
        symplectic = symplectic_by_form[form_id]
        require_equal(int_cell(symplectic, "shifted_degree"), -1, f"{row_id} imported shifted degree")
        require_equal(symplectic["restriction_status"], "restricted_verified", f"{row_id} restriction")
        require_equal(int_cell(symplectic, "symplectic_defect_rank"), 0, f"{row_id} imported restriction defect")


def verify_inputs(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "input_id", "orientation_input_rows.csv")
    require_equal(
        set(indexed),
        {"ptvv_source_theorem", "retained_derived_rows", "retained_symplectic_rows"},
        "orientation input rows",
    )
    expected_counts = {
        "ptvv_source_theorem": 1,
        "retained_derived_rows": 3,
        "retained_symplectic_rows": 3,
    }
    for input_id, expected in expected_counts.items():
        row = indexed[input_id]
        check_verified(row, "orientation_input_rows.csv")
        require_equal(row["source_packet"], str(DERIVED_FIXTURE), f"{input_id} source")
        require_equal(row["source_status"], "RETAINED_DERIVED_ENHANCEMENTS_VERIFIED", f"{input_id} status")
        require_equal(int_cell(row, "imported_rows"), expected, f"{input_id} imported")
        require_equal(int_cell(row, "expected_rows"), expected, f"{input_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{input_id} defect")


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
        require_equal(row["ptvv_status"], "missing_open_obligation", f"{obligation_id} status")


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
    verify_ptvv_rows(tables["ptvv_rows.csv"])
    verify_inputs(tables["orientation_input_rows.csv"])
    verify_coverage(tables["coverage_rows.csv"])
    verify_blocked(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"PTVV_FINITE_SUBSTACK_SYMPLECTIC_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
