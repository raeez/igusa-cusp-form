#!/usr/bin/env python3
"""Verify the higher-coloured residual vanishing criterion packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "HIGHER_COLOURED_RESIDUAL_CONDITIONAL_CRITERION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "higher_coloured_residual_vanishing_criterion.v1"
EXPECTED_KIND = "higher_coloured_residual_vanishing_criterion"

CRITERION_COLUMNS = (
    "criterion_id",
    "residual_symbol",
    "component_count",
    "tree_component_source",
    "non_tree_inputs_required",
    "conditional_vanishing_defect_rank",
    "unconditional_vanishing_claimed",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_CRITERION = {
    "criterion_id": "ocol_conditional_criterion",
    "residual_symbol": "o_col_R",
    "component_count": "6",
    "tree_component_source": "four_input_pentagon_coherence",
    "non_tree_inputs_required": "unit_sym_ref_des_ov_rows",
    "conditional_vanishing_defect_rank": "0",
    "unconditional_vanishing_claimed": "false",
    "check_status": "verified",
}

COMPONENT_COLUMNS = (
    "component_id",
    "residual_symbol",
    "component_source",
    "required_input",
    "available_now",
    "discharged_here",
    "defect_rank_if_supplied",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_COMPONENTS = {
    "tree": ("o_tree_R", "true", "true"),
    "unit": ("o_unit_R", "true", "true"),
    "symmetry": ("o_sym_R", "true", "true"),
    "refinement": ("o_ref_R", "false", "false"),
    "descent": ("o_des_R", "false", "false"),
    "overlap": ("o_ov_R", "false", "false"),
}

MISSING_INPUT_COLUMNS = (
    "input_id",
    "lane",
    "required_artifact",
    "scheduled_correction",
    "available_now",
    "why_required",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_MISSING_INPUTS = frozenset(
    {
        "unit_definition",
        "local_unit_compatibility",
        "wrapped_unit_compatibility",
        "symmetric_descent",
        "wrapped_order",
        "refinement_rows",
        "overlap_rows",
    }
)
EXPECTED_MISSING_INPUT_AVAILABILITY = {
    "unit_definition": "true",
    "local_unit_compatibility": "true",
    "wrapped_unit_compatibility": "true",
    "symmetric_descent": "true",
    "wrapped_order": "true",
    "refinement_rows": "false",
    "overlap_rows": "false",
}

EMPTY_TABLES = {
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "residual_symbol",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "residual_symbol",
        "transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "residual_symbol",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
}

OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "criterion_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "refinement_rows",
        "overlap_rows",
        "quotient_descent_rows",
        "transition_rows",
        "aggregate_population_rows",
    }
)

SCALAR_FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "tree_component_only",
        "category_definition_as_vanishing",
        "unit_component_only",
        "symmetry_component_only",
        "wrapped_order_convention_only",
        "quotient_first",
        "scalar_trace",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check higher-coloured residual criterion packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/higher_coloured_residual_vanishing_criterion"),
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
        "fixture_name": "higher_coloured_residual_vanishing_criterion",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "criterion_only": True,
        "conditional_vanishing_proved": True,
        "unconditional_vanishing_proved": False,
        "tree_component_discharged_here": True,
        "non_tree_components_discharged_here": False,
        "residual_component_count": 6,
        "residual_defect_rank_if_hypotheses_supplied": 0,
        "unit_certification": True,
        "symmetric_descent_certification": True,
        "wrapped_order_certification": True,
        "refinement_certification": False,
        "overlap_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "criterion_rows.csv",
        "component_vanishing_rows.csv",
        "missing_input_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected residual criterion tables")
    expected_imports = {
        "certificates/hybrid/higher_coloured_tree_category_definition",
        "certificates/hybrid/four_input_pentagon_coherence",
        "certificates/hybrid/lll_associativity",
        "certificates/hybrid/llw_associativity",
        "certificates/hybrid/lwl_associativity",
        "certificates/hybrid/wll_associativity",
        "certificates/hybrid/lww_associativity",
        "certificates/hybrid/wlw_associativity",
        "certificates/hybrid/wwl_associativity",
        "certificates/hybrid/www_associativity",
        "certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences",
        "certificates/hybrid/local_unit_compatibility",
        "certificates/hybrid/wrapped_unit_compatibility",
        "certificates/hybrid/local_configuration_symmetric_descent",
        "certificates/hybrid/wrapped_insertion_order_conventions",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected residual criterion imports")


def check_criterion(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "criterion_rows.csv", CRITERION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("criterion_rows.csv must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in EXPECTED_CRITERION.items():
        if row.get(key) != value:
            issues.append(f"criterion {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append("criterion row lacks proof_reference")


def check_components(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "component_vanishing_rows.csv", COMPONENT_COLUMNS, issues)
    by_id = {row.get("component_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_COMPONENTS):
        missing = sorted(set(EXPECTED_COMPONENTS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_COMPONENTS))
        if missing:
            issues.append("missing component rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected component rows: " + ", ".join(extra))
    for component_id, (symbol, available, discharged) in EXPECTED_COMPONENTS.items():
        row = by_id.get(component_id)
        if row is None:
            continue
        expected = {
            "residual_symbol": symbol,
            "available_now": available,
            "discharged_here": discharged,
            "defect_rank_if_supplied": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"component {component_id} {key}: expected {value!r}, got {row.get(key)!r}")
        if available == "false" and "required" not in row.get("notes", ""):
            issues.append(f"component {component_id} must remain marked as required")


def check_missing_inputs(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "missing_input_rows.csv", MISSING_INPUT_COLUMNS, issues)
    ids = {row.get("input_id", "") for row in table.rows}
    missing = sorted(REQUIRED_MISSING_INPUTS - ids)
    extra = sorted(ids - REQUIRED_MISSING_INPUTS)
    if missing:
        issues.append("missing input rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected missing input rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        input_id = row.get("input_id", "")
        expected_available = EXPECTED_MISSING_INPUT_AVAILABILITY.get(input_id)
        if expected_available is not None and row.get("available_now") != expected_available:
            issues.append(
                f"missing_input_rows.csv:{index} available_now: "
                f"expected {expected_available!r}, got {row.get('available_now')!r}"
            )
        if row.get("check_status") != "verified":
            issues.append(f"missing_input_rows.csv:{index} is not verified")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this criterion packet")


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
        if row.get("criterion_status") != "missing_open_obligation":
            issues.append(f"blocked_obligations.csv:{index} has non-missing status")
        if row.get("check_status") != "verified":
            issues.append(f"blocked_obligations.csv:{index} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"blocked_obligations.csv:{index} lacks mathematical payload")


def check_firewall(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "scalar_firewall.csv", SCALAR_FIREWALL_COLUMNS, issues)
    substitutes = {row.get("forbidden_substitute", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_ROWS - substitutes)
    extra = sorted(substitutes - REQUIRED_FIREWALL_ROWS)
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


def check_import_statuses(fixture: Path, issues: list[str]) -> None:
    repo_root = fixture.parents[2]
    expected_hybrid_statuses = {
        "higher_coloured_tree_category_definition": "HIGHER_COLOURED_TREE_CATEGORY_DEFINED",
        "four_input_pentagon_coherence": "FOUR_INPUT_PENTAGON_CONDITIONAL_VERIFIED",
        "lll_associativity": "LLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "llw_associativity": "LLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lwl_associativity": "LWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wll_associativity": "WLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lww_associativity": "LWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wlw_associativity": "WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wwl_associativity": "WWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "www_associativity": "WWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "hybrid_unit_object_and_vacuum_correspondences": "HYBRID_UNIT_OBJECT_AND_VACUUM_CORRESPONDENCES_DEFINED",
        "local_unit_compatibility": "LOCAL_UNIT_COMPATIBILITY_VERIFIED",
        "wrapped_unit_compatibility": "WRAPPED_UNIT_COMPATIBILITY_VERIFIED",
        "local_configuration_symmetric_descent": "LOCAL_CONFIGURATION_SYMMETRIC_DESCENT_VERIFIED",
        "wrapped_insertion_order_conventions": "WRAPPED_INSERTION_ORDER_CONVENTIONS_VERIFIED",
    }
    for relative, expected_status in expected_hybrid_statuses.items():
        manifest = load_json(
            repo_root / "certificates" / "hybrid" / relative / MANIFEST_NAME,
            issues,
        )
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_criterion(fixture, issues)
    check_components(fixture, issues)
    check_missing_inputs(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("HIGHER_COLOURED_RESIDUAL_CRITERION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
