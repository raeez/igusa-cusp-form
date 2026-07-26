#!/usr/bin/env python3
"""Verify the geometric/Borcherds degree separation obstruction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "geometric_borcherds_degree_separation_obstruction.v1"
EXPECTED_KIND = "geometric_borcherds_degree_separation_obstruction"
DEFINITION_COLUMNS = (
    "separation_id",
    "geometric_map",
    "geometric_domain",
    "geometric_target",
    "geometric_construction",
    "borcherds_map",
    "borcherds_domain",
    "borcherds_target",
    "borcherds_construction",
    "allowed_relation_condition",
    "proof_reference",
    "check_status",
    "notes",
)
BRANCH_COMPARISON_COLUMNS = (
    "comparison_id",
    "branch_id",
    "hn_class_id",
    "lifted_charge_id",
    "geometric_degree",
    "borcherds_coordinate",
    "comparison_formula",
    "comparison_defect_rank",
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
    "separation_status",
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
        "branch_domain",
        "lifted_charge_map",
        "cycle_degree_row",
        "gram_coordinate_row",
        "comparison_formula_row",
        "transition_compatibility",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "pr3_overlinePi_X_as_b_geom",
        "Borcherds_s_degree_as_geometric_degree",
        "branch_local_relation_globalized",
        "rank_one_OP_formula_as_definition",
        "empty_degree_map_as_comparison",
        "scalar_trace_as_support_degree",
        "target_window_as_support_degree",
        "Hilbert_polynomial_as_support_degree",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check geometric/Borcherds degree separation obstruction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/geometric_borcherds_degree_separation"),
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
        "fixture_name": "geometric_borcherds_degree_separation",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "separation_certified": True,
        "equality_certification": False,
        "branch_comparison_certification": False,
        "degree_map_definition_imported": True,
        "borcherds_coordinate_substitute": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "definition_rows.csv",
        "branch_comparison_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected separation tables")
    if set(manifest.get("imports", [])) != {
        "certificates/hybrid/geometric_elliptic_degree_map"
    }:
        issues.append("manifest imports do not match expected separation imports")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one separation row")
        return
    row = table.rows[0]
    expected = {
        "separation_id": "geom_vs_bch_degree",
        "geometric_map": "b_R^geom",
        "geometric_target": "ZZ_ge0",
        "borcherds_map": "m_R^Bch",
        "borcherds_target": "ZZ",
        "allowed_relation_condition": "requires_branch_comparison_rows",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"definition row {key}: expected {value!r}, got {row.get(key)!r}")
    combined = " ".join(row.values())
    for needle in (
        "coefficient_of_[E]_in_(p_E)_*cyc_1",
        "pr_3_overlinePi_X",
        "requires_branch_comparison_rows",
    ):
        if needle not in combined:
            issues.append(f"definition row missing {needle!r}")


def check_branch_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(
        fixture / "branch_comparison_rows.csv",
        BRANCH_COMPARISON_COLUMNS,
        issues,
    )
    if table.rows:
        issues.append("branch_comparison_rows.csv must remain empty until comparison rows are supplied")


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
        if row.get("separation_status") != "missing_open_obligation":
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
    degree_map = load_json(
        fixture.parent / "geometric_elliptic_degree_map" / MANIFEST_NAME,
        issues,
    )
    if not degree_map:
        return
    expected = {
        "status": "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED",
        "degree_map_defined": True,
        "populated_degree_map_certification": False,
        "borcherds_coordinate_substitute": False,
    }
    for key, value in expected.items():
        if degree_map.get(key) != value:
            issues.append(
                f"degree-map manifest {key}: expected {value!r}, got {degree_map.get(key)!r}"
            )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_definition(fixture, issues)
    check_branch_rows(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
