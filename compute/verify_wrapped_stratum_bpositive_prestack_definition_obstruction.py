#!/usr/bin/env python3
"""Verify the wrapped b>0 stratum prestack definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "wrapped_stratum_bpositive_prestack_definition.v1"
EXPECTED_KIND = "wrapped_stratum_bpositive_prestack_definition"
DEFINITION_COLUMNS = (
    "definition_id",
    "parent_prestack",
    "subprestack_symbol",
    "test_object",
    "cut_condition",
    "colour_condition",
    "wrapped_family_condition",
    "anchor_condition",
    "functor_formula",
    "local_excluded",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "component_rows.csv": (
        "component_id",
        "R_id",
        "index_set_id",
        "wrapped_colour_map_id",
        "component_formula",
        "symmetric_action",
        "component_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_rows.csv": (
        "anchor_row_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "anchor_id",
        "anchor_formula",
        "translation_weight",
        "anchor_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "support_realization_rows.csv": (
        "support_row_id",
        "R_id",
        "wrapped_colour_id",
        "object_id",
        "degree_value",
        "support_realization_defect_rank",
        "projection_conclusion",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "descent_rows.csv": (
        "descent_id",
        "R_id",
        "topology",
        "cover_id",
        "component_id",
        "effective_descent_defect_rank",
        "stackification_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "wrapped_prestack_morphism_id",
        "colour_compatibility_defect_rank",
        "anchor_compatibility_defect_rank",
        "descent_compatibility_defect_rank",
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
    "wrapped_status",
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
        "component_rows",
        "wrapped_prequotient_rows",
        "anchor_rows",
        "support_realization_rows",
        "positive_degree_partition",
        "descent_rows",
        "transition_rows",
        "local_exclusion",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "degree_shadow_only",
        "ordinary_Ran_uncoloured",
        "local_inputs_in_wrapped_stratum",
        "anchorless_wrapped_points",
        "wrapped_sheaf_as_carrier",
        "stack_claim_without_descent",
        "Borcherds_s_degree",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check wrapped b>0 stratum prestack definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_stratum_bpositive_prestack_definition"),
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
        "fixture_name": "wrapped_stratum_bpositive_prestack_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "wrapped_subprestack_defined": True,
        "wrapped_prequotient_certification": False,
        "anchor_certification": False,
        "support_realization_certification": False,
        "descent_certification": False,
        "transition_certification": False,
        "local_input_allowed": False,
        "degree_shadow_only": False,
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
        issues.append("manifest tables do not match expected wrapped-stratum tables")
    expected_imports = {
        "certificates/hybrid/hybrid_ran_prestack_definition",
        "certificates/hybrid/geometric_elliptic_degree_map",
        "certificates/hybrid/positive_elliptic_degree_projection",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected wrapped-stratum imports")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("definition_rows.csv must contain exactly one definition row")
        return
    row = table.rows[0]
    expected = {
        "definition_id": "wrapped_bpositive_R_prestack",
        "parent_prestack": "Ran_hyb_R_pre_E",
        "subprestack_symbol": "Ran_wr_R_pre_E",
        "test_object": "T",
        "cut_condition": "I_empty",
        "colour_condition": "Gamma_R_wr_equals_b_R_geom_positive",
        "wrapped_family_condition": "T_families_in_M_eta_R_wr_rig",
        "anchor_condition": "anchor_maps_lambda_eta_R_to_E",
        "functor_formula": "colim_over_(J_eta)_prod_j_M_eta_j_R_wr_rig",
        "local_excluded": "true",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"definition row {key}: expected {value!r}, got {row.get(key)!r}")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until wrapped-stratum rows are supplied")


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
        if row.get("wrapped_status") != "missing_open_obligation":
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
            "geometric_elliptic_degree_map",
            "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED",
        ),
        (
            "positive_elliptic_degree_projection",
            "POSITIVE_ELLIPTIC_DEGREE_PROJECTION_VERIFIED",
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
        print("WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
