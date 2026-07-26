#!/usr/bin/env python3
"""Verify the geometric elliptic-degree map obstruction packet.

The verifier checks that b_R^geom is defined as a proper pushforward
degree of retained one-cycle classes and that the rows needed to
populate the finite-stage map remain fail-closed.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "geometric_elliptic_degree_map_obstruction.v1"
EXPECTED_KIND = "geometric_elliptic_degree_map_obstruction"
DEFINITION_COLUMNS = (
    "definition_id",
    "domain",
    "cycle_map",
    "target_group",
    "pushforward_formula",
    "degree_formula",
    "nonnegative_condition",
    "local_condition",
    "wrapped_condition",
    "excluded_substitute",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "domain_classes.csv": (
        "class_id",
        "R_id",
        "hn_type_id",
        "numerical_class_id",
        "moduli_component_id",
        "effective_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "cycle_class_rows.csv": (
        "cycle_row_id",
        "class_id",
        "cycle_class_id",
        "n1_k3_component",
        "n1_e_component",
        "cycle_effective",
        "cycle_constancy_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "pushforward_rows.csv": (
        "pushforward_id",
        "class_id",
        "cycle_class_id",
        "pushforward_cycle",
        "degree_value",
        "integrality_defect_rank",
        "nonnegativity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "local_wrapped_split.csv": (
        "split_id",
        "class_id",
        "degree_value",
        "local_status",
        "wrapped_status",
        "split_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "class_id",
        "source_degree_value",
        "target_degree_value",
        "degree_compatibility_defect_rank",
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
    "degree_map_status",
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
        "retained_hn_domain",
        "one_cycle_class",
        "class_constancy",
        "proper_pushforward",
        "integer_degree_extraction",
        "nonnegativity_effectivity",
        "local_wrapped_partition",
        "transition_compatibility",
        "no_borcherds_coordinate_substitution",
        "row202_additivity_separate",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "Borcherds_s_degree",
        "pr3_overlinePi_X",
        "ordinary_Ran_locality",
        "determinant_anchor_only",
        "target_window_only",
        "Hilbert_polynomial_only",
        "empty_hybrid_carrier",
        "scalar_trace",
        "pfaffian_product",
        "positive_support_claim_only",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check geometric elliptic-degree map obstruction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/geometric_elliptic_degree_map"),
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
        "fixture_name": "geometric_elliptic_degree_map",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "degree_map_defined": True,
        "populated_degree_map_certification": False,
        "additivity_certification": False,
        "mathematical_certification": False,
        "hybrid_carrier_packet_imported": True,
        "moduli_packet_imported": True,
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
        issues.append("manifest tables do not match expected geometric degree-map tables")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one definition row")
        return
    row = table.rows[0]
    expected = {
        "definition_id": "b_geom_R",
        "domain": "Gamma_sigma_S_HN_R",
        "target_group": "N_1_E=ZZ[E]",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"definition row {key}: expected {value!r}, got {row.get(key)!r}")
    combined = " ".join(row.values())
    for needle in ("cyc_1", "(p_E)_*cyc_1", "b_R^geom", "pr_3 overlinePi_X"):
        if needle not in combined:
            issues.append(f"definition row missing {needle!r}")
    if row.get("local_condition") != "local iff b_R^geom(gamma)=0":
        issues.append("definition row local condition mismatch")
    if row.get("wrapped_condition") != "wrapped iff b_R^geom(gamma)>0":
        issues.append("definition row wrapped condition mismatch")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until degree-map rows are supplied")


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
        if row.get("degree_map_status") != "missing_open_obligation":
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
    if issues:
        print("GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
