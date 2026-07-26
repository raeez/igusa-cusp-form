#!/usr/bin/env python3
"""Verify the finite test-window definition obstruction packet.

This verifier checks that Gamma_R^test has a precise definition and that
the missing membership, finiteness, transition, and target-exhaustion
rows are recorded fail-closed.  It does not prove that a populated
finite test window has been constructed.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "FINITE_TEST_WINDOW_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "finite_test_window_definition.v1"
EXPECTED_KIND = "finite_test_window_definition"

DEFINITION_COLUMNS = (
    "definition_id",
    "parameter",
    "source_domain",
    "normal_ordered_lift",
    "target_map",
    "formula",
    "target_lattice",
    "finite_when",
    "transition_rule",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "test_window_membership.csv": (
        "row_id",
        "R_id",
        "charge_id",
        "t_translate_id",
        "hat_charge_id",
        "gram_degree_id",
        "n",
        "l",
        "m",
        "image_membership",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "test_window_transitions.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "source_window_id",
        "target_window_id",
        "inclusion_defect_rank",
        "transition_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "test_window_finiteness.csv": (
        "finiteness_id",
        "R_id",
        "hn_charge_count",
        "translate_count_bound",
        "test_window_count_bound",
        "finite_type_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "target_exhaustion_rows.csv": (
        "exhaustion_id",
        "target_degree_id",
        "R_id",
        "membership_witness",
        "relation_closed_status",
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
    "test_window_status",
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
        "finite_hn_charge_rows",
        "translate_orbit_rows",
        "hat_gamma_rows",
        "target_image_membership_rows",
        "gram_coordinate_rows",
        "finiteness_witness",
        "transition_inclusion_rows",
        "downward_saturation_comparison",
        "active_support_compatibility",
        "relation_closed_target_exhaustion",
        "compact_source_compatibility",
        "no_orientation_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "O1_orientation_data",
        "target_degree_closure_Wrel",
        "active_support_only",
        "HN_height_only",
        "Gram_map_only",
        "normal_ordered_formula_only",
        "source_compact_support_only",
        "target_source_compatibility_only",
        "pfaffian_product",
        "scalar_trace",
        "protected_trace",
        "empty_charge_window",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite test-window definition obstruction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/charge/finite_test_window"),
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
            issues.append(
                f"header mismatch in {path}; expected {','.join(columns)}"
            )
        rows = nonempty_rows(reader)
    return CsvTable(path, rows)


def load_manifest(fixture: Path, issues: list[str]) -> dict[str, object]:
    path = fixture / MANIFEST_NAME
    if not path.is_file():
        issues.append(f"missing manifest: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"manifest is not valid JSON: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append("manifest root is not an object")
        return {}
    return value


def check_manifest(manifest: dict[str, object], issues: list[str]) -> None:
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "finite_test_window",
        "charge_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key} is {manifest.get(key)!r}, not {value!r}")
    booleans = {
        "finite_test_window_defined": True,
        "populated_window_certification": False,
        "relation_closed_target_exhaustion": False,
        "charge_window_packet_imported": True,
        "mukai_gram_packet_imported": True,
        "orientation_definition_substitute": False,
    }
    for key, value in booleans.items():
        if manifest.get(key) is not value:
            issues.append(f"manifest {key} is {manifest.get(key)!r}, not {value!r}")


def check_definition(table: CsvTable, issues: list[str]) -> None:
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one definition row")
        return
    row = table.rows[0]
    required_values = {
        "definition_id": "gamma_test_r",
        "parameter": "R",
        "source_domain": "Gamma_R^HN",
        "target_map": "overlinePi_X(c,T)=Pi_X(c)+T",
        "target_lattice": "Gamma_gram",
        "check_status": "verified",
    }
    for key, value in required_values.items():
        if row.get(key) != value:
            issues.append(f"definition row {key} is {row.get(key)!r}, not {value!r}")
    for needle in ("hatGamma_R", "Pi_X(c)+T", "Gamma_R^test"):
        if needle not in row.get("formula", "") + row.get("normal_ordered_lift", ""):
            issues.append(f"definition row does not contain {needle!r}")
    if "finite" not in row.get("finite_when", "").lower():
        issues.append("definition row does not record finite hypotheses")
    if "Gamma_R^test subset" not in row.get("transition_rule", ""):
        issues.append("definition row does not record transition inclusion")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the obstruction packet")


def check_obligations(table: CsvTable, issues: list[str]) -> None:
    ids = {row.get("obligation_id", "") for row in table.rows}
    missing = sorted(REQUIRED_OBLIGATIONS - ids)
    extra = sorted(ids - REQUIRED_OBLIGATIONS)
    if missing:
        issues.append(f"missing obligation rows: {', '.join(missing)}")
    if extra:
        issues.append(f"unexpected obligation rows: {', '.join(extra)}")
    for index, row in enumerate(table.rows, start=2):
        if row.get("test_window_status") != "missing_open_obligation":
            issues.append(f"blocked_obligations.csv:{index} has non-missing status")
        if row.get("check_status") != "verified":
            issues.append(f"blocked_obligations.csv:{index} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"blocked_obligations.csv:{index} has no payload")


def check_firewall(table: CsvTable, issues: list[str]) -> None:
    rows = {row.get("forbidden_substitute", ""): row for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_ROWS - set(rows))
    extra = sorted(set(rows) - REQUIRED_FIREWALL_ROWS)
    if missing:
        issues.append(f"missing firewall rows: {', '.join(missing)}")
    if extra:
        issues.append(f"unexpected firewall rows: {', '.join(extra)}")
    for index, row in enumerate(table.rows, start=2):
        if row.get("excluded") != "true":
            issues.append(f"scalar_firewall.csv:{index} is not excluded=true")
        if row.get("defect_rank") != "0":
            issues.append(f"scalar_firewall.csv:{index} defect_rank is not zero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_firewall.csv:{index} is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    issues: list[str] = []
    fixture = args.fixture
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    definition = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    check_definition(definition, issues)
    check_empty_tables(fixture, issues)
    obligations = load_csv(fixture / "blocked_obligations.csv", OBLIGATION_COLUMNS, issues)
    check_obligations(obligations, issues)
    firewall = load_csv(fixture / "scalar_firewall.csv", SCALAR_FIREWALL_COLUMNS, issues)
    check_firewall(firewall, issues)

    if issues:
        print("FINITE_TEST_WINDOW_DEFINITION_OBSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
