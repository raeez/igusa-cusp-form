#!/usr/bin/env python3
"""Verify the eight-word local/wrapped binary vocabulary packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "EIGHT_WORD_BINARY_VOCABULARY_DEFINED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "eight_word_binary_vocabulary.v1"
EXPECTED_KIND = "eight_word_binary_vocabulary"

ALPHABET_COLUMNS = (
    "symbol",
    "meaning",
    "elliptic_degree_condition",
    "rigidification_required",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ALPHABET = {
    "L": {
        "meaning": "projection_finite_local_input",
        "elliptic_degree_condition": "b_geom_equals_0",
        "rigidification_required": "false",
        "check_status": "verified",
    },
    "W": {
        "meaning": "rigidified_wrapped_input",
        "elliptic_degree_condition": "b_geom_positive",
        "rigidification_required": "true",
        "check_status": "verified",
    },
}

WORD_COLUMNS = (
    "word_id",
    "word",
    "epsilon_1",
    "epsilon_2",
    "epsilon_3",
    "left_intermediate_type",
    "right_intermediate_type",
    "final_type",
    "left_parenthesization_id",
    "right_parenthesization_id",
    "flag_stack_constructed",
    "associativity_defect_certified",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_WORDS = {
    "word_LLL": ("LLL", "L", "L", "L", "L", "L", "L"),
    "word_LLW": ("LLW", "L", "L", "W", "L", "W", "W"),
    "word_LWL": ("LWL", "L", "W", "L", "W", "W", "W"),
    "word_WLL": ("WLL", "W", "L", "L", "W", "L", "W"),
    "word_LWW": ("LWW", "L", "W", "W", "W", "W", "W"),
    "word_WLW": ("WLW", "W", "L", "W", "W", "W", "W"),
    "word_WWL": ("WWL", "W", "W", "L", "W", "W", "W"),
    "word_WWW": ("WWW", "W", "W", "W", "W", "W", "W"),
}

EMPTY_TABLES = {
    "flag_stack_rows.csv": (
        "flag_id",
        "word",
        "flag_stack_id",
        "left_parenthesization_id",
        "right_parenthesization_id",
        "flag_stack_constructed",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "associativity_rows.csv": (
        "associativity_id",
        "word",
        "left_parenthesization_id",
        "right_parenthesization_id",
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
        "word_transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "word_or_flag_id",
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
    "vocabulary_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "flag_stack_rows",
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
        "two_sided_LWL_only",
        "flag_stack_claim",
        "associativity_claim",
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
        description="Check eight-word local/wrapped binary vocabulary packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/eight_word_binary_vocabulary"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def product(left: str, right: str) -> str:
    return "L" if left == "L" and right == "L" else "W"


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
        "fixture_name": "eight_word_binary_vocabulary",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "alphabet_defined": True,
        "type_product_defined": True,
        "word_length": 3,
        "word_count": 8,
        "parenthesizations_defined": True,
        "left_right_intermediate_types_defined": True,
        "flag_stacks_constructed": False,
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
        "alphabet_rows.csv",
        "word_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected vocabulary tables")
    expected_imports = {
        "certificates/hybrid/mixed_correspondence_thom_sebastiani",
        "certificates/moduli/retained_extension_closure",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected vocabulary imports")


def check_alphabet(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "alphabet_rows.csv", ALPHABET_COLUMNS, issues)
    by_symbol = {row.get("symbol", ""): row for row in table.rows}
    if set(by_symbol) != set(EXPECTED_ALPHABET):
        issues.append("alphabet rows must be exactly L and W")
    for symbol, expected in EXPECTED_ALPHABET.items():
        row = by_symbol.get(symbol)
        if row is None:
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"alphabet row {symbol} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"alphabet row {symbol} lacks proof_reference")


def check_words(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "word_rows.csv", WORD_COLUMNS, issues)
    by_id = {row.get("word_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_WORDS):
        missing = sorted(set(EXPECTED_WORDS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_WORDS))
        if missing:
            issues.append("missing word rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected word rows: " + ", ".join(extra))
    for word_id, expected_tuple in EXPECTED_WORDS.items():
        row = by_id.get(word_id)
        if row is None:
            continue
        word, e1, e2, e3, left, right, final = expected_tuple
        expected = {
            "word": word,
            "epsilon_1": e1,
            "epsilon_2": e2,
            "epsilon_3": e3,
            "left_intermediate_type": left,
            "right_intermediate_type": right,
            "final_type": final,
            "flag_stack_constructed": "false",
            "associativity_defect_certified": "false",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"word row {word_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        computed_left = product(e1, e2)
        computed_right = product(e2, e3)
        computed_final = product(computed_left, e3)
        if (computed_left, computed_right, computed_final) != (left, right, final):
            issues.append(f"word row {word_id} has incorrect computed product types")
        if not row.get("left_parenthesization_id") or not row.get("right_parenthesization_id"):
            issues.append(f"word row {word_id} lacks parenthesization ids")
        if not row.get("proof_reference"):
            issues.append(f"word row {word_id} lacks proof_reference")


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
        if row.get("vocabulary_status") != "missing_open_obligation":
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
    ts_manifest = load_json(
        repo_root
        / "certificates"
        / "hybrid"
        / "mixed_correspondence_thom_sebastiani"
        / MANIFEST_NAME,
        issues,
    )
    if ts_manifest and ts_manifest.get("status") != "MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED":
        issues.append("mixed Thom--Sebastiani packet status is not verified")
    extension_manifest = load_json(
        repo_root / "certificates" / "moduli" / "retained_extension_closure" / MANIFEST_NAME,
        issues,
    )
    if extension_manifest:
        if extension_manifest.get("certified") is not True:
            issues.append("retained extension closure manifest is not certified")
        if extension_manifest.get("extension_closure") is not True:
            issues.append("retained extension closure manifest lacks extension_closure")
        if extension_manifest.get("two_step_flag_stacks") is not False:
            issues.append("retained extension closure must not claim two-step flag stacks here")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_alphabet(fixture, issues)
    check_words(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("EIGHT_WORD_BINARY_VOCABULARY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
