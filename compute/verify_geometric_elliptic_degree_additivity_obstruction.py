#!/usr/bin/env python3
"""Verify the geometric elliptic-degree additivity obstruction packet.

The verifier checks that row 202 is represented as a criterion with
explicit missing rows.  It also imports the row-201 degree-map packet
and the retained-extension-closure packet, because retained word closure
is necessary but not sufficient for additivity of the pushed-forward
one-cycle degree.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "GEOMETRIC_ELLIPTIC_DEGREE_ADDITIVITY_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "geometric_elliptic_degree_additivity_obstruction.v1"
EXPECTED_KIND = "geometric_elliptic_degree_additivity_obstruction"
DEFINITION_COLUMNS = (
    "criterion_id",
    "extension_source",
    "cycle_additivity_formula",
    "pushforward_formula",
    "degree_formula",
    "retained_window_condition",
    "transition_condition",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "extension_pairs.csv": (
        "extension_pair_id",
        "window_id",
        "left_class_id",
        "right_class_id",
        "middle_class_id",
        "extension_row_id",
        "retained_middle_term",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "cycle_additivity_rows.csv": (
        "cycle_additivity_id",
        "extension_pair_id",
        "left_cycle_class",
        "right_cycle_class",
        "middle_cycle_class",
        "cycle_additivity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "pushforward_additivity_rows.csv": (
        "pushforward_additivity_id",
        "extension_pair_id",
        "left_pushforward",
        "right_pushforward",
        "middle_pushforward",
        "pushforward_additivity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "degree_additivity_rows.csv": (
        "degree_additivity_id",
        "extension_pair_id",
        "left_degree",
        "right_degree",
        "middle_degree",
        "degree_additivity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "extension_pair_id",
        "source_degree_defect_rank",
        "target_degree_defect_rank",
        "transition_additivity_defect_rank",
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
    "additivity_status",
    "proof_reference",
    "check_status",
    "notes",
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
REQUIRED_OBLIGATIONS = frozenset(
    {
        "retained_extension_pairs",
        "cycle_class_population",
        "cycle_additivity_rows",
        "proper_pushforward_rows",
        "pushforward_additivity_rows",
        "integer_degree_rows",
        "integer_degree_additivity_rows",
        "transition_additivity_rows",
        "extension_flag_stack_context",
        "degree_map_rows",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "retained_extension_closure_only",
        "extension_word_closure_only",
        "K0_symbol_only",
        "pr3_overlinePi_X",
        "Borcherds_s_degree",
        "ordinary_Ran_locality",
        "positive_support_claim_only",
        "empty_degree_map",
        "scalar_trace",
        "transition_rows_without_extension_pairs",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check geometric elliptic-degree additivity obstruction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/geometric_elliptic_degree_additivity"),
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
        "fixture_name": "geometric_elliptic_degree_additivity",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "additivity_criterion_defined": True,
        "additivity_certification": False,
        "mathematical_certification": False,
        "degree_map_definition_imported": True,
        "retained_extension_closure_imported": True,
        "retained_extension_closure_sufficient": False,
        "borcherds_coordinate_substitute": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "definition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected additivity tables")
    expected_imports = {
        "certificates/hybrid/geometric_elliptic_degree_map",
        "certificates/moduli/retained_extension_closure",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected additivity imports")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one criterion row")
        return
    row = table.rows[0]
    expected = {
        "criterion_id": "b_geom_R_additivity",
        "extension_source": "retained_exact_triangle_or_short_exact_sequence",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"definition row {key}: expected {value!r}, got {row.get(key)!r}")
    combined = " ".join(row.values())
    for needle in (
        "cyc_1(gamma)",
        "(p_E)_*cyc_1(gamma)",
        "b_R^geom(gamma)",
        "compatible for R to Rprime",
    ):
        if needle not in combined:
            issues.append(f"definition row missing {needle!r}")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until additivity rows are supplied")


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
        if row.get("additivity_status") != "missing_open_obligation":
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


def check_imports(fixture: Path, issues: list[str]) -> None:
    certificates_dir = fixture.parent.parent
    degree_map = load_json(
        certificates_dir / "hybrid" / "geometric_elliptic_degree_map" / MANIFEST_NAME,
        issues,
    )
    if degree_map:
        expected = {
            "status": "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED",
            "degree_map_defined": True,
            "populated_degree_map_certification": False,
            "additivity_certification": False,
            "borcherds_coordinate_substitute": False,
        }
        for key, value in expected.items():
            if degree_map.get(key) != value:
                issues.append(
                    f"degree-map manifest {key}: expected {value!r}, got {degree_map.get(key)!r}"
                )
    retained_closure = load_json(
        certificates_dir / "moduli" / "retained_extension_closure" / MANIFEST_NAME,
        issues,
    )
    if retained_closure:
        expected = {
            "status": None,
            "certified": True,
            "extension_closure": True,
            "extension_closure_defects_zero": True,
            "extension_flag_stacks": False,
            "transitions": False,
            "compact_hall_stage": False,
        }
        for key, value in expected.items():
            if key == "status":
                continue
            if retained_closure.get(key) != value:
                issues.append(
                    "retained-extension manifest "
                    f"{key}: expected {value!r}, got {retained_closure.get(key)!r}"
                )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_definition(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("GEOMETRIC_ELLIPTIC_DEGREE_ADDITIVITY_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
