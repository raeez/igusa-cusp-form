#!/usr/bin/env python3
"""Verify the wrapped insertion order conventions packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_INSERTION_ORDER_CONVENTIONS_VERIFIED"
EXPECTED_SCHEMA = "wrapped_insertion_order_conventions.v1"
EXPECTED_KIND = "wrapped_insertion_order_conventions"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"

ORDER_COLUMNS = (
    "order_id",
    "R_id",
    "profile_rule",
    "binary_vertex_rule",
    "ww_extension_convention",
    "wrapped_order_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ORDER = {
    "order_id": "wrapped_planar_order_R",
    "wrapped_order_defect_rank": "0",
    "check_status": "verified",
}

FLAG_COLUMNS = (
    "flag_order_id",
    "word",
    "left_comparison_id",
    "right_comparison_id",
    "ordered_wrapped_subsequence",
    "left_order_defect_rank",
    "right_order_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_FLAGS = {
    "flag_order_LLL": ("LLL", "empty"),
    "flag_order_LLW": ("LLW", "eta3"),
    "flag_order_LWL": ("LWL", "eta2"),
    "flag_order_WLL": ("WLL", "eta1"),
    "flag_order_LWW": ("LWW", "eta2_eta3"),
    "flag_order_WLW": ("WLW", "eta1_eta3"),
    "flag_order_WWL": ("WWL", "eta1_eta2"),
    "flag_order_WWW": ("WWW", "eta1_eta2_eta3"),
}

EMPTY_TABLES = {
    "unordered_wrapped_descent_rows.csv": (
        "descent_id",
        "R_id",
        "ordered_wrapped_profile",
        "unordered_target",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "ordered_colimit_descent_rows.csv": (
        "descent_id",
        "R_id",
        "ordered_chart_family",
        "symmetric_colimit_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "overlap_rows.csv": (
        "overlap_id",
        "R_id",
        "local_wrapped_chart_pair",
        "common_refinement_id",
        "overlap_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "R_id",
        "wrapped_order_id",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "wrapped_order_id",
        "transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "row_type",
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
    "wrapped_order_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "unordered_wrapped_descent",
        "ordered_colimit_descent",
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
        "braiding_operator",
        "unordered_wrapped_symmetric_descent",
        "ordered_colimit_descent",
        "overlap_claim",
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
        description="Check wrapped insertion order convention packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_insertion_order_conventions"),
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
        "fixture_name": "wrapped_insertion_order_conventions",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "wrapped_order_conventions_proved": True,
        "ordered_wrapped_profiles": True,
        "binary_vertex_order_rule": True,
        "ww_quotient_subobject_convention": True,
        "flag_comparison_order_preserved": True,
        "flag_word_count": 8,
        "braid_operator_used": False,
        "unordered_wrapped_descent": False,
        "ordered_colimit_descent": False,
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
        "wrapped_order_rows.csv",
        "flag_order_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected wrapped order tables")
    expected_imports = {
        "certificates/hybrid/higher_coloured_tree_category_definition",
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/hybrid/eight_word_two_step_flag_stacks",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected wrapped order imports")


def check_order_row(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "wrapped_order_rows.csv", ORDER_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("wrapped_order_rows.csv must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in EXPECTED_ORDER.items():
        if row.get(key) != value:
            issues.append(f"wrapped_order_rows.csv {key}: expected {value!r}, got {row.get(key)!r}")
    if "WW_source_order_eta1_eta2" not in row.get("ww_extension_convention", ""):
        issues.append("wrapped order row does not record the WW quotient/subobject convention")
    if "prop:wrapped-insertion-order-conventions" not in row.get("proof_reference", ""):
        issues.append("wrapped order row does not point to the row-245 proposition")


def check_flag_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "flag_order_rows.csv", FLAG_COLUMNS, issues)
    by_id = {row.get("flag_order_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_FLAGS):
        missing = sorted(set(EXPECTED_FLAGS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_FLAGS))
        if missing:
            issues.append("missing flag order rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected flag order rows: " + ", ".join(extra))
    for flag_id, (word, subsequence) in EXPECTED_FLAGS.items():
        row = by_id.get(flag_id)
        if row is None:
            continue
        expected = {
            "word": word,
            "ordered_wrapped_subsequence": subsequence,
            "left_order_defect_rank": "0",
            "right_order_defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{flag_id} {key}: expected {value!r}, got {row.get(key)!r}")
        if "prop:wrapped-insertion-order-conventions" not in row.get("proof_reference", ""):
            issues.append(f"{flag_id} does not point to the row-245 proposition")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this order-convention packet")


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
        if row.get("wrapped_order_status") != "missing_open_obligation":
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
        "wrapped_wrapped_correspondence_definition": "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        "eight_word_two_step_flag_stacks": "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED",
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
    check_order_row(fixture, issues)
    check_flag_rows(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("WRAPPED_INSERTION_ORDER_CONVENTIONS_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
