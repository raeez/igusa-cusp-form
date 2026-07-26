#!/usr/bin/env python3
"""Verify the four-input pentagon coherence packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "FOUR_INPUT_PENTAGON_CONDITIONAL_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "four_input_pentagon_coherence.v1"
EXPECTED_KIND = "four_input_pentagon_coherence"
WORDS = (
    "LLLL",
    "LLLW",
    "LLWL",
    "LWLL",
    "WLLL",
    "LLWW",
    "LWLW",
    "LWWL",
    "WLLW",
    "WLWL",
    "WWLL",
    "LWWW",
    "WLWW",
    "WWLW",
    "WWWL",
    "WWWW",
)
SINGLE_WRAPPED_WORDS = frozenset({"LLLW", "LLWL", "LWLL", "WLLL"})

FOUR_STEP_COLUMNS = (
    "flag_id",
    "four_input_word",
    "flag_stack_id",
    "epsilon_1",
    "epsilon_2",
    "epsilon_3",
    "epsilon_4",
    "final_type",
    "retained_flag_quot_model",
    "finite_type",
    "retained_intermediates",
    "wrapped_rigidifications_retained",
    "before_e_quotient",
    "proof_reference",
    "check_status",
    "notes",
)

PENTAGON_COLUMNS = (
    "pentagon_id",
    "four_input_word",
    "flag_stack_id",
    "left_path_id",
    "right_path_id",
    "uses_wrapped_wrapped_product",
    "conditional_on_functorial_rows",
    "pentagon_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)

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
    "four_step_flag_rows": ("flag_stack", "true"),
    "length_three_associativity_rows": ("associativity", "false"),
    "mixed_functorial_rows": ("six_functor", "false"),
    "ww_target_admissibility": ("proper_target", "false"),
    "ww_functorial_rows": ("wrapped_wrapped_functoriality", "false"),
    "ts_orientation_pentagon": ("vanishing_cycles", "false"),
}

EMPTY_TABLES = {
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "four_input_word",
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
        "four_input_word",
        "pentagon_transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "pentagon_id",
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
    "pentagon_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "ww_functorial_rows",
        "higher_coloured_tree_category",
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
        "three_word_associativity_only",
        "flag_stack_only",
        "ww_target_admissibility_only",
        "higher_coloured_claim",
        "unit_claim",
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
    parser = argparse.ArgumentParser(description="Check four-input pentagon packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/four_input_pentagon_coherence"),
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


def has_wrapped_wrapped(word: str) -> bool:
    return word.count("W") >= 2


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "four_input_pentagon_coherence",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "length_four_word_count": 16,
        "four_step_flag_rows_constructed": True,
        "pentagon_rows_proved": True,
        "pentagon_defect_rank_max": 0,
        "all_length_three_words_supplied": True,
        "conditional_on_functorial_rows": True,
        "ww_functorial_rows_supplied": False,
        "before_e_quotient": True,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "higher_coloured_tree_category": False,
        "unit_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "four_step_flag_rows.csv",
        "pentagon_rows.csv",
        "functorial_input_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected pentagon tables")
    expected_imports = {
        "certificates/hybrid/eight_word_two_step_flag_stacks",
        "certificates/hybrid/lll_associativity",
        "certificates/hybrid/llw_associativity",
        "certificates/hybrid/lwl_associativity",
        "certificates/hybrid/wll_associativity",
        "certificates/hybrid/lww_associativity",
        "certificates/hybrid/wlw_associativity",
        "certificates/hybrid/wwl_associativity",
        "certificates/hybrid/www_associativity",
        "certificates/hybrid/mixed_correspondence_base_change",
        "certificates/hybrid/mixed_correspondence_projection_formula",
        "certificates/hybrid/mixed_correspondence_thom_sebastiani",
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/hybrid/wrapped_wrapped_extension_admissibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected pentagon imports")


def check_four_step_flags(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "four_step_flag_rows.csv", FOUR_STEP_COLUMNS, issues)
    by_word = {row.get("four_input_word", ""): row for row in table.rows}
    if tuple(by_word) != WORDS:
        if set(by_word) != set(WORDS):
            missing = sorted(set(WORDS) - set(by_word))
            extra = sorted(set(by_word) - set(WORDS))
            if missing:
                issues.append("missing four-step flag rows: " + ", ".join(missing))
            if extra:
                issues.append("unexpected four-step flag rows: " + ", ".join(extra))
        else:
            issues.append("four-step flag rows are not in canonical word order")
    for word in WORDS:
        row = by_word.get(word)
        if row is None:
            continue
        expected_type = "L" if word == "LLLL" else "W"
        if row.get("flag_id") != f"flag4_{word}":
            issues.append(f"{word} flag_id mismatch")
        if row.get("flag_stack_id") != f"F3_{word}_R":
            issues.append(f"{word} flag_stack_id mismatch")
        for index, letter in enumerate(word, start=1):
            if row.get(f"epsilon_{index}") != letter:
                issues.append(f"{word} epsilon_{index} mismatch")
        expected = {
            "final_type": expected_type,
            "retained_flag_quot_model": "true",
            "finite_type": "true",
            "retained_intermediates": "true",
            "wrapped_rigidifications_retained": "false" if word == "LLLL" else "true",
            "before_e_quotient": "true",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{word} {key}: expected {value!r}, got {row.get(key)!r}")
        if not row.get("proof_reference"):
            issues.append(f"{word} four-step flag lacks proof_reference")


def check_pentagon_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "pentagon_rows.csv", PENTAGON_COLUMNS, issues)
    by_word = {row.get("four_input_word", ""): row for row in table.rows}
    if tuple(by_word) != WORDS:
        if set(by_word) != set(WORDS):
            missing = sorted(set(WORDS) - set(by_word))
            extra = sorted(set(by_word) - set(WORDS))
            if missing:
                issues.append("missing pentagon rows: " + ", ".join(missing))
            if extra:
                issues.append("unexpected pentagon rows: " + ", ".join(extra))
        else:
            issues.append("pentagon rows are not in canonical word order")
    for word in WORDS:
        row = by_word.get(word)
        if row is None:
            continue
        expected = {
            "pentagon_id": f"pent_{word}",
            "flag_stack_id": f"F3_{word}_R",
            "uses_wrapped_wrapped_product": "true" if has_wrapped_wrapped(word) else "false",
            "conditional_on_functorial_rows": "true",
            "pentagon_defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{word} pentagon {key}: expected {value!r}, got {row.get(key)!r}")
        if not row.get("left_path_id") or not row.get("right_path_id"):
            issues.append(f"{word} pentagon row lacks path ids")
        if word in SINGLE_WRAPPED_WORDS and row.get("notes") != "single_wrapped_mac_lane_pentagon":
            issues.append(f"{word} single wrapped note mismatch")
        if has_wrapped_wrapped(word) and "WW_functoriality_hypothesis" not in row.get("notes", ""):
            issues.append(f"{word} WW note must mention WW functoriality hypothesis")


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
    ww_row = by_id.get("ww_functorial_rows")
    if ww_row and "hypothesis" not in ww_row.get("notes", ""):
        issues.append("WW functorial row must be marked as hypothesis")


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
        status = row.get("pentagon_status")
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
        "lll_associativity": "LLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "llw_associativity": "LLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lwl_associativity": "LWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wll_associativity": "WLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lww_associativity": "LWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wlw_associativity": "WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wwl_associativity": "WWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "www_associativity": "WWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
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
    check_four_step_flags(fixture, issues)
    check_pentagon_rows(fixture, issues)
    check_functorial_inputs(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("FOUR_INPUT_PENTAGON_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
