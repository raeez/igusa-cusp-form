#!/usr/bin/env python3
"""Verify the first-window anchor-residual obstruction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "ANCHOR_RESIDUAL_FIRST_WINDOW_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "anchor_residual_first_window_obstruction.v1"
EXPECTED_KIND = "anchor_residual_first_window_obstruction"
FIRST_WINDOW_FIXTURE = Path("certificates/first_window/k3e_relation_closed_window")
ANCHOR_RESIDUAL_FIXTURE = Path("certificates/hybrid/anchor_residual_definition")
CRITERION_COLUMNS = (
    "criterion_id",
    "row_id",
    "window_id",
    "residual_id",
    "zero_condition",
    "component_count",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_CRITERION = {
    "criterion_id": "fw_anchor_residual_zero_criterion",
    "row_id": "218",
    "window_id": "W1_first_relation_closed",
    "residual_id": "o_lambda_R",
    "zero_condition": "all_five_anchor_residual_components_zero",
    "component_count": "5",
    "check_status": "verified",
}
COMPONENT_COLUMNS = (
    "component_id",
    "residual_component",
    "required_first_window_artifact",
    "required_table",
    "required_row_type",
    "zero_payload",
    "current_status",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_COMPONENTS = {
    "fw_o_lambda_ex": ("o_lambda_ex", "finite_stage_population_rows.csv", "population_row"),
    "fw_o_lambda_unit": ("o_lambda_unit", "first_window_anchor_unit_rows.csv", "unit_weight_row"),
    "fw_o_lambda_loss": ("o_lambda_loss", "first_window_anchor_losslessness_rows.csv", "losslessness_row"),
    "fw_o_lambda_multi": ("o_lambda_multi", "first_window_anchor_multiplicativity_rows.csv", "multiplicativity_row"),
    "fw_o_lambda_tr": ("o_lambda_tr", "first_window_anchor_transition_rows.csv", "transition_row"),
}
IMPORT_COLUMNS = (
    "import_id",
    "fixture_path",
    "imported_status",
    "first_window_kind",
    "stage",
    "certified",
    "mathematical_certification",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_IMPORT = {
    "import_id": "fw_scaffold_import",
    "fixture_path": str(FIRST_WINDOW_FIXTURE),
    "imported_status": "FIRST_WINDOW_OBSTRUCTION_LEDGER_VERIFIED",
    "first_window_kind": "first_window_scalar_firewall_blocked",
    "stage": "scalar_firewall_only",
    "certified": "false",
    "mathematical_certification": "false",
    "check_status": "verified",
}
MISSING_COLUMNS = (
    "missing_id",
    "fixture_path",
    "missing_table",
    "why_needed_for_anchor_residual",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_MISSING_TABLES = {
    "window_closure.csv",
    "target_source_representatives.csv",
    "first_window_theorems.csv",
    "transitions.csv",
}
VANISHING_COLUMNS = (
    "vanishing_id",
    "window_id",
    "residual_id",
    "component_id",
    "vanishing_status",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "first_window_anchor_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "first_window_population",
        "first_window_unit",
        "first_window_loss",
        "first_window_multiplicativity",
        "first_window_transition",
        "first_window_theorem_row",
    }
)
FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
REQUIRED_FIREWALL = frozenset(
    {
        "anchor_residual_definition_only",
        "first_window_obstruction_ledger_only",
        "target_labels_only",
        "signed_dimensions_only",
        "determinant_anchor_only",
        "extra_anchor_data_only",
        "scalar_trace",
        "pfaffian_product",
        "status_only_rows",
    }
)
FIRST_WINDOW_EMPTY_TABLES = (
    "window_closure.csv",
    "target_source_representatives.csv",
    "first_window_theorems.csv",
    "transitions.csv",
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check first-window anchor-residual obstruction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/anchor_residual_first_window_obstruction"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def nonempty_rows(reader: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in reader:
        normalized = {
            key: (value or "").strip()
            for key, value in row.items()
            if key is not None
        }
        if any(normalized.values()):
            rows.append(normalized)
    return rows


def load_csv(path: Path, columns: tuple[str, ...], issues: list[str]) -> CsvTable:
    if not path.is_file():
        issues.append(f"missing table: {path}")
        return CsvTable(path, [])
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            issues.append(f"header mismatch in {path}; expected {','.join(columns)}")
        rows = nonempty_rows(reader)
    return CsvTable(path, rows)


def load_json(path: Path, issues: list[str]) -> dict[str, object]:
    if not path.is_file():
        issues.append(f"missing JSON file: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {path}")
        return {}
    return value


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "anchor_residual_first_window_obstruction",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "row": 218,
        "first_window_vanishing_proved": False,
        "criterion_defined": True,
        "first_window_scaffold_imported": True,
        "first_window_scaffold_status": "FIRST_WINDOW_OBSTRUCTION_LEDGER_VERIFIED",
        "anchor_residual_definition_imported": True,
        "missing_component_rows_certified": True,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "criterion_rows.csv",
        "component_requirement_rows.csv",
        "first_window_import_rows.csv",
        "missing_first_window_rows.csv",
        "vanishing_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected first-window obstruction tables")
    expected_imports = {
        str(ANCHOR_RESIDUAL_FIXTURE),
        str(FIRST_WINDOW_FIXTURE),
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected first-window obstruction imports")


def check_single_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected: dict[str, str],
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"{table_name} {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append(f"{table_name} row lacks proof_reference")


def check_components(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "component_requirement_rows.csv", COMPONENT_COLUMNS, issues)
    ids = {row.get("component_id", "") for row in table.rows}
    missing = sorted(set(EXPECTED_COMPONENTS) - ids)
    extra = sorted(ids - set(EXPECTED_COMPONENTS))
    if missing:
        issues.append("missing component requirement rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected component requirement rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        expected = EXPECTED_COMPONENTS.get(row.get("component_id", ""))
        if expected is None:
            continue
        residual_component, required_table, required_row_type = expected
        checks = {
            "residual_component": residual_component,
            "required_table": required_table,
            "required_row_type": required_row_type,
            "current_status": "missing_open_obligation",
            "check_status": "verified",
        }
        for key, value in checks.items():
            if row.get(key) != value:
                issues.append(
                    f"component_requirement_rows.csv:{index} {key}: "
                    f"expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("zero_payload"):
            issues.append(f"component_requirement_rows.csv:{index} lacks zero_payload")


def check_missing_tables(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "missing_first_window_rows.csv", MISSING_COLUMNS, issues)
    missing_tables = {row.get("missing_table", "") for row in table.rows}
    missing = sorted(REQUIRED_MISSING_TABLES - missing_tables)
    extra = sorted(missing_tables - REQUIRED_MISSING_TABLES)
    if missing:
        issues.append("missing missing-table rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected missing-table rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("check_status") != "verified":
            issues.append(f"missing_first_window_rows.csv:{index} is not verified")
        if not row.get("why_needed_for_anchor_residual"):
            issues.append(f"missing_first_window_rows.csv:{index} lacks reason")


def check_empty_vanishing(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "vanishing_rows.csv", VANISHING_COLUMNS, issues)
    if table.rows:
        issues.append("vanishing_rows.csv must remain empty until row 218 is actually proved")


def check_obligations(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "blocked_obligations.csv", OBLIGATION_COLUMNS, issues)
    ids = {row.get("obligation_id", "") for row in table.rows}
    missing = sorted(REQUIRED_OBLIGATIONS - ids)
    extra = sorted(ids - REQUIRED_OBLIGATIONS)
    if missing:
        issues.append("missing obligation rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected obligation rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("first_window_anchor_status") != "missing_open_obligation":
            issues.append(f"blocked_obligations.csv:{index} has non-missing status")
        if row.get("check_status") != "verified":
            issues.append(f"blocked_obligations.csv:{index} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"blocked_obligations.csv:{index} lacks mathematical payload")


def check_firewall(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "scalar_firewall.csv", FIREWALL_COLUMNS, issues)
    substitutes = {row.get("forbidden_substitute", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL - substitutes)
    extra = sorted(substitutes - REQUIRED_FIREWALL)
    if missing:
        issues.append("missing firewall rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected firewall rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("excluded") != "true":
            issues.append(f"scalar_firewall.csv:{index} excluded is not true")
        if row.get("defect_rank") != "0":
            issues.append(f"scalar_firewall.csv:{index} defect_rank is not zero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_firewall.csv:{index} is not verified")


def check_imports(issues: list[str]) -> None:
    residual_manifest = load_json(ANCHOR_RESIDUAL_FIXTURE / MANIFEST_NAME, issues)
    if residual_manifest and residual_manifest.get("status") != (
        "ANCHOR_RESIDUAL_DEFINITION_VERIFIED"
    ):
        issues.append("anchor_residual_definition import is not verified")
    first_window_manifest = load_json(FIRST_WINDOW_FIXTURE / MANIFEST_NAME, issues)
    if first_window_manifest:
        expected = {
            "first_window_kind": "first_window_scalar_firewall_blocked",
            "stage": "scalar_firewall_only",
            "obstruction_ledger_status": "FIRST_WINDOW_OBSTRUCTION_LEDGER_VERIFIED",
            "first_window_certification": False,
            "mathematical_certification": False,
        }
        for key, value in expected.items():
            if first_window_manifest.get(key) != value:
                issues.append(
                    f"first-window manifest {key}: expected {value!r}, "
                    f"got {first_window_manifest.get(key)!r}"
                )
    for table_name in FIRST_WINDOW_EMPTY_TABLES:
        table_path = FIRST_WINDOW_FIXTURE / table_name
        if not table_path.is_file():
            issues.append(f"missing imported first-window table: {table_path}")
            continue
        with table_path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"imported first-window table {table_name} now has rows; "
                "retire the obstruction packet before claiming it"
            )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "criterion_rows.csv", CRITERION_COLUMNS, EXPECTED_CRITERION, issues)
    check_components(fixture, issues)
    check_single_row(fixture, "first_window_import_rows.csv", IMPORT_COLUMNS, EXPECTED_IMPORT, issues)
    check_missing_tables(fixture, issues)
    check_empty_vanishing(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(issues)
    if issues:
        print("ANCHOR_RESIDUAL_FIRST_WINDOW_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
