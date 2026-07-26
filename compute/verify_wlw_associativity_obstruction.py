#!/usr/bin/env python3
"""Verify the WLW associativity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "wlw_associativity.v1"
EXPECTED_KIND = "word_associativity"

ASSOCIATIVITY_COLUMNS = (
    "associativity_id",
    "word",
    "flag_stack_id",
    "left_comparison_id",
    "right_comparison_id",
    "left_composite_id",
    "right_composite_id",
    "uses_wrapped_wrapped_product",
    "conditional_on_functorial_rows",
    "associativity_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ASSOCIATIVITY = {
    "associativity_id": "assoc_WLW_R",
    "word": "WLW",
    "flag_stack_id": "F2_WLW_R",
    "left_comparison_id": "lambda_WLW",
    "right_comparison_id": "rho_WLW",
    "left_composite_id": "m_WW_zeta12_eta2_after_m_WL_eta1_alpha",
    "right_composite_id": "m_WW_eta1_zeta23_after_m_LW_alpha_eta2",
    "uses_wrapped_wrapped_product": "true",
    "conditional_on_functorial_rows": "true",
    "associativity_defect_rank": "0",
    "check_status": "verified",
}

FUNCTORIAL_COLUMNS = (
    "input_id",
    "lane",
    "required_input",
    "required_for",
    "available_as_hypothesis",
    "discharged_here",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_FUNCTORIAL = {
    "wlw_flag_stack": ("flag_stack", "true"),
    "wlw_left_right_maps": ("flag_stack", "true"),
    "wlw_mixed_base_change": ("base_change", "true"),
    "wlw_mixed_projection_formula": ("projection_formula", "true"),
    "wlw_mixed_ts": ("vanishing_cycles", "true"),
    "wlw_ww_target_admissibility": ("proper_target", "true"),
    "wlw_ww_base_change": ("base_change", "false"),
    "wlw_ww_projection_formula": ("projection_formula", "false"),
    "wlw_ww_ts": ("vanishing_cycles", "false"),
}
WW_HYPOTHESIS_ROWS = frozenset(
    {
        "wlw_ww_base_change",
        "wlw_ww_projection_formula",
        "wlw_ww_ts",
    }
)

REMAINING_COLUMNS = (
    "word",
    "required_row",
    "scheduled_correction",
    "associativity_supplied_here",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_REMAINING = {
    "WWL": "236",
    "WWW": "237",
}

EMPTY_TABLES = {
    "pentagon_rows.csv": (
        "pentagon_id",
        "word",
        "four_input_word",
        "pentagon_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "word",
        "flag_stack_id",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "word",
        "associativity_transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "associativity_id",
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
    "wlw_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "ww_functorial_rows",
        "remaining_word_rows",
        "pentagon_rows",
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
        "flag_stack_only",
        "LWW_only",
        "mixed_functoriality_only",
        "ww_target_admissibility_only",
        "pentagon_claim",
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
    parser = argparse.ArgumentParser(description="Check WLW associativity packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wlw_associativity"),
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
        "fixture_name": "wlw_associativity",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "word": "WLW",
        "uses_local_local_product": False,
        "uses_mixed_lw_product": True,
        "uses_mixed_wl_product": True,
        "uses_wrapped_wrapped_product": True,
        "associativity_proved": True,
        "conditional_on_functorial_rows": True,
        "ww_functorial_rows_supplied": False,
        "uses_two_step_flag_stack": True,
        "uses_left_right_comparison_maps": True,
        "uses_base_change": True,
        "uses_projection_formula": True,
        "uses_reduced_thom_sebastiani": True,
        "associativity_defect_rank": 0,
        "remaining_word_associativity_count": 2,
        "pentagon_certification": False,
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
        "associativity_rows.csv",
        "functorial_input_rows.csv",
        "remaining_word_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected WLW associativity tables")
    expected_imports = {
        "certificates/hybrid/eight_word_two_step_flag_stacks",
        "certificates/hybrid/mixed_correspondence_base_change",
        "certificates/hybrid/mixed_correspondence_projection_formula",
        "certificates/hybrid/mixed_correspondence_thom_sebastiani",
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/hybrid/wrapped_wrapped_extension_admissibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected WLW imports")


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


def check_functorial_inputs(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "functorial_input_rows.csv", FUNCTORIAL_COLUMNS, issues)
    by_id = {row.get("input_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_FUNCTORIAL):
        missing = sorted(set(EXPECTED_FUNCTORIAL) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_FUNCTORIAL))
        if missing:
            issues.append("missing functorial input rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected functorial input rows: " + ", ".join(extra))
    for input_id, (lane, discharged) in EXPECTED_FUNCTORIAL.items():
        row = by_id.get(input_id)
        if row is None:
            continue
        expected = {
            "lane": lane,
            "available_as_hypothesis": "true",
            "discharged_here": discharged,
            "defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"functorial input {input_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"functorial input {input_id} lacks proof_reference")
    for input_id in WW_HYPOTHESIS_ROWS:
        row = by_id.get(input_id)
        if row and "hypothesis" not in row.get("notes", ""):
            issues.append(f"WW functorial row {input_id} must be marked as a hypothesis")


def check_remaining_words(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "remaining_word_rows.csv", REMAINING_COLUMNS, issues)
    by_word = {row.get("word", ""): row for row in table.rows}
    if set(by_word) != set(EXPECTED_REMAINING):
        missing = sorted(set(EXPECTED_REMAINING) - set(by_word))
        extra = sorted(set(by_word) - set(EXPECTED_REMAINING))
        if missing:
            issues.append("missing remaining words: " + ", ".join(missing))
        if extra:
            issues.append("unexpected remaining words: " + ", ".join(extra))
    for word, correction in EXPECTED_REMAINING.items():
        row = by_word.get(word)
        if row is None:
            continue
        if row.get("scheduled_correction") != correction:
            issues.append(f"remaining word {word} has wrong scheduled correction")
        if row.get("associativity_supplied_here") != "false":
            issues.append(f"remaining word {word} must not be supplied here")
        if row.get("check_status") != "verified":
            issues.append(f"remaining word {word} is not verified")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until later rows are supplied")


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
        status = row.get("wlw_status")
        if row.get("obligation_id") == "ww_functorial_rows":
            if status != "hypothesis_not_discharged_here":
                issues.append(f"blocked_obligations.csv:{index} has wrong WW hypothesis status")
        elif status != "missing_open_obligation":
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
        "eight_word_two_step_flag_stacks": "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED",
        "mixed_correspondence_base_change": "MIXED_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        "mixed_correspondence_projection_formula": "MIXED_CORRESPONDENCE_PROJECTION_FORMULA_VERIFIED",
        "mixed_correspondence_thom_sebastiani": "MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED",
        "wrapped_wrapped_correspondence_definition": "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        "wrapped_wrapped_extension_admissibility": "WRAPPED_WRAPPED_ADMISSIBILITY_VERIFIED",
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
    check_single_row(
        fixture,
        "associativity_rows.csv",
        ASSOCIATIVITY_COLUMNS,
        EXPECTED_ASSOCIATIVITY,
        issues,
    )
    check_functorial_inputs(fixture, issues)
    check_remaining_words(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("WLW_ASSOCIATIVITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
