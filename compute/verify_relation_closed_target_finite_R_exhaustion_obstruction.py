#!/usr/bin/env python3
"""Verify the row-200 finite-R target-exhaustion obstruction packet.

The verifier imports the target relation-closure packet, the symbolic
tail packet, and the finite-test-window definition packet.  It checks
that the proof tables needed to realize every relation-closed target
degree in some Gamma_R^test remain empty and that the missing
obligations are recorded explicitly.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "RELATION_CLOSED_TARGET_FINITE_R_EXHAUSTION_OBSTRUCTION_VERIFIED"
FINITE_TEST_STATUS = "FINITE_TEST_WINDOW_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "relation_closed_target_finite_R_exhaustion_obstruction.v1"
EXPECTED_KIND = "relation_closed_target_finite_R_exhaustion_obstruction"
EMPTY_TABLES = {
    "target_degree_to_R.csv": (
        "row_id",
        "target_degree_id",
        "degree_family",
        "n",
        "l",
        "m",
        "beta_c1",
        "beta_c2",
        "beta_c3",
        "R_id",
        "test_window_id",
        "membership_witness_id",
        "relation_closed_source",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "hn_witnesses.csv": (
        "witness_id",
        "target_degree_id",
        "R_id",
        "charge_id",
        "hn_membership_row",
        "translate_id",
        "hat_charge_id",
        "pi_x_n",
        "pi_x_l",
        "pi_x_m",
        "t_n",
        "t_l",
        "t_m",
        "image_n",
        "image_l",
        "image_m",
        "image_equality_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "symbolic_tail_R_witnesses.csv": (
        "family_id",
        "parameter_condition",
        "target_degree_formula",
        "R_formula",
        "charge_formula",
        "translate_formula",
        "image_formula",
        "equality_defect_rank",
        "finite_R_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_compatibility.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "target_degree_id",
        "source_witness_id",
        "target_witness_id",
        "inclusion_defect_rank",
        "image_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "coverage_defects.csv": (
        "coverage_id",
        "target_scope",
        "finite_prefix_covered",
        "symbolic_tail_covered",
        "missing_degree_count",
        "missing_symbolic_family_count",
        "coverage_defect_rank",
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
    "finite_R_status",
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
        "target_scope_index",
        "finite_prefix_degree_to_R",
        "symbolic_tail_R_formula",
        "hn_charge_witnesses",
        "translate_witnesses",
        "image_equality_rows",
        "finite_R_bounds",
        "transition_compatibility",
        "coverage_zero",
        "source_compatibility",
        "no_target_only_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "wrel_finite_prefix_only",
        "wrel_tail_staircase_only",
        "target_degree_closure_only",
        "finite_test_window_definition_only",
        "active_root_exhaustion_only",
        "downward_root_windows_only",
        "empty_charge_window",
        "source_compact_support_only",
        "target_source_compatibility_only",
        "signed_multiplicity_only",
        "pfaffian_product",
        "protected_trace",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check relation-closed target finite-R exhaustion obstruction."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/charge/relation_closed_target_finite_R_exhaustion"),
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


def repo_root_from_fixture(fixture: Path) -> Path:
    resolved = fixture.resolve()
    return resolved.parents[2]


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "relation_closed_target_finite_R_exhaustion",
        "charge_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "finite_R_exhaustion_certification": False,
        "mathematical_certification": False,
        "finite_test_window_definition_imported": True,
        "wrel_degree_closure_imported": True,
        "wrel_tail_staircase_imported": True,
        "target_tail_infinite": True,
        "finite_target_prefix_sufficient": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {"blocked_obligations.csv", "scalar_firewall.csv"}
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected relation-closed finite-R tables")


def check_imports(repo_root: Path, issues: list[str]) -> None:
    finite_test = load_json(
        repo_root / "certificates/charge/finite_test_window/manifest.json", issues
    )
    if finite_test:
        if finite_test.get("status") != FINITE_TEST_STATUS:
            issues.append("finite_test_window manifest status mismatch")
        if finite_test.get("relation_closed_target_exhaustion") is not False:
            issues.append("finite_test_window must not certify row-200 exhaustion")
    wrel = load_json(
        repo_root / "certificates/targets/delta5_gn_kac/wrel_degree_closure/manifest.json",
        issues,
    )
    if wrel:
        if wrel.get("schema_version") != "wrel_target_degree_closure.v1":
            issues.append("wrel_degree_closure schema mismatch")
        if wrel.get("certified") is not True:
            issues.append("wrel_degree_closure must be certified")
        if wrel.get("target_only") is not True:
            issues.append("wrel_degree_closure must remain target_only")
        if wrel.get("primitive_recognition") is not False:
            issues.append("wrel_degree_closure must not certify primitive recognition")
    tail = load_json(
        repo_root / "certificates/targets/delta5_gn_kac/wrel_tail_staircase/manifest.json",
        issues,
    )
    if tail:
        if tail.get("schema_version") != "wrel_tail_staircase.v1":
            issues.append("wrel_tail_staircase schema mismatch")
        if tail.get("certified") is not True:
            issues.append("wrel_tail_staircase must be certified")
        if tail.get("infinite_tail") is not True:
            issues.append("wrel_tail_staircase must certify an infinite tail")
        if tail.get("finite_target_degree_enumeration_closed") is not False:
            issues.append("tail manifest must record that finite enumeration is not closed")
        if tail.get("target_only") is not True:
            issues.append("tail manifest must remain target_only")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until finite-R witnesses are supplied")


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
        if row.get("finite_R_status") != "missing_open_obligation":
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
    check_imports(repo_root_from_fixture(fixture), issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    if issues:
        print("RELATION_CLOSED_TARGET_FINITE_R_EXHAUSTION_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
