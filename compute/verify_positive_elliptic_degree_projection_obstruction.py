#!/usr/bin/env python3
"""Verify the positive elliptic-degree projection packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "POSITIVE_ELLIPTIC_DEGREE_PROJECTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "positive_elliptic_degree_projection.v1"
EXPECTED_KIND = "positive_elliptic_degree_projection"
THEOREM_COLUMNS = (
    "theorem_id",
    "cycle_input",
    "pushforward_condition",
    "positive_condition",
    "component_conclusion",
    "projection_conclusion",
    "proof_reference",
    "check_status",
    "notes",
)
SUPPORT_COLUMNS = (
    "support_row_id",
    "R_id",
    "object_id",
    "class_id",
    "cycle_class_id",
    "effective_cycle_expression",
    "degree_value",
    "support_realization_defect_rank",
    "projection_conclusion",
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
    "projection_status",
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
        "retained_object_row",
        "effective_cycle_realization",
        "support_equals_cycle_support",
        "positive_degree_value",
        "projection_application",
        "transition_compatibility",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "numerical_degree_without_effective_cycle",
        "virtual_ch2_with_cancellation",
        "Borcherds_s_degree",
        "pr3_overlinePi_X",
        "ordinary_Ran_locality",
        "empty_degree_map",
        "Hilbert_polynomial_only",
        "scalar_trace",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check positive elliptic-degree projection packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/positive_elliptic_degree_projection"),
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
        "fixture_name": "positive_elliptic_degree_projection",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "curve_theorem_certified": True,
        "object_support_certification": False,
        "degree_map_definition_imported": True,
        "effective_cycle_required": True,
        "borcherds_coordinate_substitute": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "theorem_rows.csv",
        "support_realization_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected projection tables")
    if set(manifest.get("imports", [])) != {
        "certificates/hybrid/geometric_elliptic_degree_map"
    }:
        issues.append("manifest imports do not match expected projection imports")


def check_theorem(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "theorem_rows.csv", THEOREM_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("theorem_rows.csv must contain exactly one theorem row")
        return
    row = table.rows[0]
    expected = {
        "theorem_id": "positive_effective_cycle_projects",
        "cycle_input": "effective_one_cycle_Z=sum_i_m_i_C_i_with_m_i_positive",
        "pushforward_condition": "(p_E)_*Z=b[E]",
        "positive_condition": "b>0",
        "component_conclusion": "some_component_C_i_maps_dominantly_to_E",
        "projection_conclusion": "p_E(|Z|)=E",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"theorem row {key}: expected {value!r}, got {row.get(key)!r}")


def check_support_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "support_realization_rows.csv", SUPPORT_COLUMNS, issues)
    if table.rows:
        issues.append("support_realization_rows.csv must remain empty until object rows are supplied")


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
        if row.get("projection_status") != "missing_open_obligation":
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
    check_theorem(fixture, issues)
    check_support_rows(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("POSITIVE_ELLIPTIC_DEGREE_PROJECTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
