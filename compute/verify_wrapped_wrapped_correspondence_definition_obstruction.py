#!/usr/bin/env python3
"""Verify the wrapped/wrapped correspondence definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "wrapped_wrapped_correspondence_definition.v1"
EXPECTED_KIND = "wrapped_wrapped_correspondence_definition"
DEFINITION_COLUMNS = (
    "definition_id",
    "order",
    "wrapped_left_input",
    "wrapped_right_input",
    "target_colour",
    "source_carrier",
    "target_carrier",
    "extension_convention",
    "source_map",
    "target_map",
    "quotient_timing",
    "excluded_substitutes",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "extension_stack_rows.csv": (
        "stack_row_id",
        "R_id",
        "wrapped_left_colour_id",
        "wrapped_right_colour_id",
        "target_colour_id",
        "extension_stack_id",
        "exact_sequence_convention",
        "finite_type_defect_rank",
        "admissibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "source_target_map_rows.csv": (
        "map_row_id",
        "R_id",
        "extension_stack_id",
        "source_map_formula",
        "target_map_formula",
        "wrapped_left_anchor_map",
        "wrapped_right_anchor_map",
        "wrapped_target_anchor_map",
        "map_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_memory_rows.csv": (
        "anchor_memory_id",
        "R_id",
        "extension_stack_id",
        "left_source_anchor_id",
        "right_source_anchor_id",
        "target_anchor_id",
        "relative_anchor_id",
        "anchor_memory_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "admissibility_rows.csv": (
        "admissibility_id",
        "R_id",
        "extension_stack_id",
        "compact_support_model_id",
        "exceptional_pushforward_defect_rank",
        "properness_substitute_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "thom_sebastiani_rows.csv": (
        "ts_id",
        "R_id",
        "extension_stack_id",
        "vanishing_cycle_source_id",
        "vanishing_cycle_target_id",
        "ts_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "wrapped_wrapped_correspondence_morphism_id",
        "colour_compatibility_defect_rank",
        "map_compatibility_defect_rank",
        "anchor_compatibility_defect_rank",
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
    "wrapped_wrapped_status",
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
        "extension_stack_rows",
        "source_target_map_rows",
        "target_wrapped_colour_rows",
        "anchor_memory_rows",
        "admissibility_rows",
        "thom_sebastiani_rows",
        "transition_rows",
        "symmetric_descent_rows",
        "mixed_separate",
        "local_local_separate",
        "two_sided_mixed_separate",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "ordinary_Ran_only",
        "quotient_first_hall_product",
        "mixed_as_wrapped_wrapped",
        "local_local_as_wrapped_wrapped",
        "two_sided_mixed_as_wrapped_wrapped",
        "unordered_symmetric_product",
        "scalar_Fock_factor",
        "determinant_anchor_only",
        "Borcherds_s_degree",
        "degree_shadow_only",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check wrapped/wrapped correspondence definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_wrapped_correspondence_definition"),
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
        "fixture_name": "wrapped_wrapped_correspondence_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "wrapped_wrapped_correspondence_defined": True,
        "ordered_source_pair": True,
        "extension_stack_certification": False,
        "source_target_map_certification": False,
        "anchor_memory_certification": False,
        "admissibility_certification": False,
        "thom_sebastiani_certification": False,
        "transition_certification": False,
        "symmetric_descent_certification": False,
        "mixed_certification": False,
        "local_local_certification": False,
        "two_sided_certification": False,
        "quotient_first": False,
        "scalar_only": False,
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
        issues.append("manifest tables do not match expected wrapped/wrapped tables")
    expected_imports = {
        "certificates/hybrid/hybrid_ran_prestack_definition",
        "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition",
        "certificates/hybrid/geometric_elliptic_degree_map",
        "certificates/hybrid/geometric_elliptic_degree_additivity",
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected wrapped/wrapped imports")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one wrapped/wrapped row")
        return
    row = table.rows[0]
    expected = {
        "definition_id": "wrapped_wrapped_R_correspondence",
        "order": "WW",
        "wrapped_left_input": "eta_1_in_Gamma_R_wr",
        "wrapped_right_input": "eta_2_in_Gamma_R_wr",
        "target_colour": "zeta_equals_eta_1_plus_eta_2_in_Gamma_R_wr",
        "source_carrier": "Ran_wr_R_pre_E_times_Ran_wr_R_pre_E",
        "target_carrier": "Ran_wr_R_pre_E",
        "extension_convention": "zero_to_W_eta_2_to_B_zeta_to_W_eta_1_to_zero",
        "source_map": "p_WW_to_M_eta_1_R_wr_rig_times_M_eta_2_R_wr_rig",
        "target_map": "q_WW_to_M_zeta_R_wr_rig",
        "quotient_timing": "before_E_quotient",
        "excluded_substitutes": "no_quotient_first_no_scalar_factor",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"definition row {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append("definition row lacks proof_reference")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until wrapped/wrapped rows are supplied")


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
        if row.get("wrapped_wrapped_status") != "missing_open_obligation":
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
    for relative, expected_status in (
        (
            "hybrid_ran_prestack_definition",
            "HYBRID_RAN_PRESTACK_DEFINITION_VERIFIED",
        ),
        (
            "wrapped_stratum_bpositive_prestack_definition",
            "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED",
        ),
        (
            "geometric_elliptic_degree_map",
            "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED",
        ),
        (
            "geometric_elliptic_degree_additivity",
            "GEOMETRIC_ELLIPTIC_DEGREE_ADDITIVITY_OBSTRUCTION_VERIFIED",
        ),
        (
            "mixed_local_wrapped_correspondence_definition",
            "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
    ):
        manifest = load_json(fixture.parent / relative / MANIFEST_NAME, issues)
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
    check_definition(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
