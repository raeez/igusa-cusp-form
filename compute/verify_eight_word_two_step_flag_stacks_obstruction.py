#!/usr/bin/env python3
"""Verify the eight-word two-step flag-stack construction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "eight_word_two_step_flag_stacks.v1"
EXPECTED_KIND = "eight_word_two_step_flag_stacks"

FLAG_COLUMNS = (
    "flag_id",
    "word",
    "flag_stack_id",
    "epsilon_1",
    "epsilon_2",
    "epsilon_3",
    "left_intermediate_type",
    "right_intermediate_type",
    "final_type",
    "retained_flag_quot_model",
    "finite_type",
    "retained_intermediates",
    "wrapped_rigidifications_retained",
    "before_e_quotient",
    "associativity_certified",
    "pentagon_certified",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_FLAGS = {
    "flag_LLL": ("LLL", "F2_LLL_R", "L", "L", "L", "L", "L", "L", "false"),
    "flag_LLW": ("LLW", "F2_LLW_R", "L", "L", "W", "L", "W", "W", "true"),
    "flag_LWL": ("LWL", "F2_LWL_R", "L", "W", "L", "W", "W", "W", "true"),
    "flag_WLL": ("WLL", "F2_WLL_R", "W", "L", "L", "W", "L", "W", "true"),
    "flag_LWW": ("LWW", "F2_LWW_R", "L", "W", "W", "W", "W", "W", "true"),
    "flag_WLW": ("WLW", "F2_WLW_R", "W", "L", "W", "W", "W", "W", "true"),
    "flag_WWL": ("WWL", "F2_WWL_R", "W", "W", "L", "W", "W", "W", "true"),
    "flag_WWW": ("WWW", "F2_WWW_R", "W", "W", "W", "W", "W", "W", "true"),
}

COMPARISON_COLUMNS = (
    "comparison_id",
    "word",
    "map_symbol",
    "parenthesization",
    "domain_stack_id",
    "target_fibre_product_id",
    "inner_pair_type",
    "outer_pair_type",
    "constructed",
    "before_e_quotient",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_COMPARISONS = {
    "lambda_LLL": ("LLL", "lambda", "left", "F2_LLL_R", "E_LL_x_M_L_E_LL", "LL", "LL"),
    "rho_LLL": ("LLL", "rho", "right", "F2_LLL_R", "E_LL_x_M_L_E_LL", "LL", "LL"),
    "lambda_LLW": ("LLW", "lambda", "left", "F2_LLW_R", "E_LW_x_M_L_E_LL", "LL", "LW"),
    "rho_LLW": ("LLW", "rho", "right", "F2_LLW_R", "E_LW_x_M_W_E_LW", "LW", "LW"),
    "lambda_LWL": ("LWL", "lambda", "left", "F2_LWL_R", "E_WL_x_M_W_E_LW", "LW", "WL"),
    "rho_LWL": ("LWL", "rho", "right", "F2_LWL_R", "E_LW_x_M_W_E_WL", "WL", "LW"),
    "lambda_WLL": ("WLL", "lambda", "left", "F2_WLL_R", "E_WL_x_M_W_E_WL", "WL", "WL"),
    "rho_WLL": ("WLL", "rho", "right", "F2_WLL_R", "E_WL_x_M_L_E_LL", "LL", "WL"),
    "lambda_LWW": ("LWW", "lambda", "left", "F2_LWW_R", "E_WW_x_M_W_E_LW", "LW", "WW"),
    "rho_LWW": ("LWW", "rho", "right", "F2_LWW_R", "E_LW_x_M_W_E_WW", "WW", "LW"),
    "lambda_WLW": ("WLW", "lambda", "left", "F2_WLW_R", "E_WW_x_M_W_E_WL", "WL", "WW"),
    "rho_WLW": ("WLW", "rho", "right", "F2_WLW_R", "E_WW_x_M_W_E_LW", "LW", "WW"),
    "lambda_WWL": ("WWL", "lambda", "left", "F2_WWL_R", "E_WL_x_M_W_E_WW", "WW", "WL"),
    "rho_WWL": ("WWL", "rho", "right", "F2_WWL_R", "E_WW_x_M_W_E_WL", "WL", "WW"),
    "lambda_WWW": ("WWW", "lambda", "left", "F2_WWW_R", "E_WW_x_M_W_E_WW", "WW", "WW"),
    "rho_WWW": ("WWW", "rho", "right", "F2_WWW_R", "E_WW_x_M_W_E_WW", "WW", "WW"),
}

EMPTY_TABLES = {
    "associativity_rows.csv": (
        "associativity_id",
        "word",
        "left_comparison_id",
        "right_comparison_id",
        "associativity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
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
        "flag_stack_id",
        "flag_stack_transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "flag_stack_id",
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
    "flag_stack_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "associativity_rows",
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
        "vocabulary_only",
        "associativity_claim",
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
    parser = argparse.ArgumentParser(
        description="Check eight-word two-step flag-stack construction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/eight_word_two_step_flag_stacks"),
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
        "fixture_name": "eight_word_two_step_flag_stacks",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "word_count": 8,
        "flag_stack_rows_constructed": True,
        "comparison_map_rows_constructed": True,
        "comparison_map_count": 16,
        "finite_type_flag_quot_model": True,
        "retained_intermediate_colours": True,
        "before_e_quotient": True,
        "associativity_certification": False,
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
        "flag_stack_rows.csv",
        "comparison_map_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected flag-stack tables")
    expected_imports = {
        "certificates/hybrid/eight_word_binary_vocabulary",
        "certificates/hybrid/local_local_correspondence_definition",
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/moduli/retained_extension_closure",
        "certificates/moduli/retained_universal_complexes",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected flag-stack imports")


def check_flags(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "flag_stack_rows.csv", FLAG_COLUMNS, issues)
    by_id = {row.get("flag_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_FLAGS):
        missing = sorted(set(EXPECTED_FLAGS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_FLAGS))
        if missing:
            issues.append("missing flag rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected flag rows: " + ", ".join(extra))
    for flag_id, values in EXPECTED_FLAGS.items():
        row = by_id.get(flag_id)
        if row is None:
            continue
        word, stack_id, e1, e2, e3, left, right, final, wrapped = values
        expected = {
            "word": word,
            "flag_stack_id": stack_id,
            "epsilon_1": e1,
            "epsilon_2": e2,
            "epsilon_3": e3,
            "left_intermediate_type": left,
            "right_intermediate_type": right,
            "final_type": final,
            "retained_flag_quot_model": "true",
            "finite_type": "true",
            "retained_intermediates": "true",
            "wrapped_rigidifications_retained": wrapped,
            "before_e_quotient": "true",
            "associativity_certified": "false",
            "pentagon_certified": "false",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"flag row {flag_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"flag row {flag_id} lacks proof_reference")


def check_comparisons(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "comparison_map_rows.csv", COMPARISON_COLUMNS, issues)
    by_id = {row.get("comparison_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_COMPARISONS):
        missing = sorted(set(EXPECTED_COMPARISONS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_COMPARISONS))
        if missing:
            issues.append("missing comparison rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected comparison rows: " + ", ".join(extra))
    for comparison_id, values in EXPECTED_COMPARISONS.items():
        row = by_id.get(comparison_id)
        if row is None:
            continue
        word, symbol, parenthesization, domain, target, inner, outer = values
        expected = {
            "word": word,
            "map_symbol": symbol,
            "parenthesization": parenthesization,
            "domain_stack_id": domain,
            "target_fibre_product_id": target,
            "inner_pair_type": inner,
            "outer_pair_type": outer,
            "constructed": "true",
            "before_e_quotient": "true",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"comparison row {comparison_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"comparison row {comparison_id} lacks proof_reference")


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
        if row.get("flag_stack_status") != "missing_open_obligation":
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
        "eight_word_binary_vocabulary": "EIGHT_WORD_BINARY_VOCABULARY_DEFINED",
        "local_local_correspondence_definition": "LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED",
        "mixed_local_wrapped_correspondence_definition": "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        "wrapped_wrapped_correspondence_definition": "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
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
    extension_manifest = load_json(
        repo_root / "certificates" / "moduli" / "retained_extension_closure" / MANIFEST_NAME,
        issues,
    )
    if extension_manifest:
        if extension_manifest.get("certified") is not True:
            issues.append("retained extension closure manifest is not certified")
        if extension_manifest.get("extension_closure") is not True:
            issues.append("retained extension closure manifest lacks extension_closure")
    universal_manifest = load_json(
        repo_root / "certificates" / "moduli" / "retained_universal_complexes" / MANIFEST_NAME,
        issues,
    )
    if universal_manifest:
        if universal_manifest.get("certified") is not True:
            issues.append("retained universal complexes manifest is not certified")
        if universal_manifest.get("universal_complexes") is not True:
            issues.append("retained universal complexes manifest lacks universal complexes")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_flags(fixture, issues)
    check_comparisons(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("EIGHT_WORD_TWO_STEP_FLAG_STACKS_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
