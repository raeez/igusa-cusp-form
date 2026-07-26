#!/usr/bin/env python3
"""Verify the source/target anchor-memory definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "source_target_anchor_memory_definition.v1"
EXPECTED_KIND = "source_target_anchor_memory_definition"
DEFINITION_COLUMNS = (
    "anchor_memory_id",
    "order",
    "correspondence_definition_id",
    "wrapped_source_anchors",
    "wrapped_target_anchors",
    "anchor_map",
    "anchor_formula",
    "relative_anchor_formula",
    "quotient_timing",
    "determinant_anchor_used",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_DEFINITION_ROWS = {
    "anchor_memory_LW_R": {
        "order": "LW",
        "correspondence_definition_id": "mixed_LW_R_correspondence",
        "wrapped_source_anchors": "lambda_eta_R_on_W_eta",
        "wrapped_target_anchors": "lambda_zeta_R_on_B_zeta",
        "anchor_map": "a_LW_to_E2",
        "anchor_formula": "xi_maps_to_lambda_eta_W_eta__lambda_zeta_B_zeta",
        "relative_anchor_formula": "lambda_zeta_minus_lambda_eta",
        "quotient_timing": "before_E_quotient",
        "determinant_anchor_used": "false",
        "check_status": "verified",
    },
    "anchor_memory_WL_R": {
        "order": "WL",
        "correspondence_definition_id": "mixed_WL_R_correspondence",
        "wrapped_source_anchors": "lambda_eta_R_on_W_eta",
        "wrapped_target_anchors": "lambda_zeta_R_on_B_zeta",
        "anchor_map": "a_WL_to_E2",
        "anchor_formula": "xi_maps_to_lambda_eta_W_eta__lambda_zeta_B_zeta",
        "relative_anchor_formula": "lambda_zeta_minus_lambda_eta",
        "quotient_timing": "before_E_quotient",
        "determinant_anchor_used": "false",
        "check_status": "verified",
    },
    "anchor_memory_WW_R": {
        "order": "WW",
        "correspondence_definition_id": "wrapped_wrapped_R_correspondence",
        "wrapped_source_anchors": "lambda_eta1_R_on_W1__lambda_eta2_R_on_W2",
        "wrapped_target_anchors": "lambda_zeta_R_on_B_zeta",
        "anchor_map": "a_WW_to_E3",
        "anchor_formula": "xi_maps_to_lambda_eta1_W1__lambda_eta2_W2__lambda_zeta_B_zeta",
        "relative_anchor_formula": "lambda_zeta_minus_lambda_eta1_minus_lambda_eta2",
        "quotient_timing": "before_E_quotient",
        "determinant_anchor_used": "false",
        "check_status": "verified",
    },
    "anchor_memory_LWL_R": {
        "order": "LWL",
        "correspondence_definition_id": "two_sided_mixed_R_correspondence",
        "wrapped_source_anchors": "lambda_eta_R_on_W_eta",
        "wrapped_target_anchors": "lambda_zeta_R_on_C_zeta",
        "anchor_map": "a_LWL_to_E2",
        "anchor_formula": "xi_maps_to_lambda_eta_W_eta__lambda_zeta_C_zeta",
        "relative_anchor_formula": "lambda_zeta_minus_lambda_eta",
        "quotient_timing": "before_E_quotient",
        "determinant_anchor_used": "false",
        "check_status": "verified",
    },
}
LOCAL_LOCAL_EXCLUSION_COLUMNS = (
    "exclusion_id",
    "correspondence_definition_id",
    "wrapped_inputs_present",
    "anchor_memory_defined",
    "reason",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "determinant_anchor_rows.csv": (
        "anchor_row_id",
        "R_id",
        "wrapped_colour_id",
        "anchor_formula",
        "translation_weight",
        "construction_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "translation_weight_rows.csv": (
        "weight_row_id",
        "R_id",
        "wrapped_colour_id",
        "chi_value",
        "translation_weight",
        "weight_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "chi_zero_degeneracy_rows.csv": (
        "degeneracy_id",
        "R_id",
        "wrapped_colour_id",
        "chi_value",
        "degeneracy_model_id",
        "degeneracy_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "extra_anchor_data_rows.csv": (
        "extra_anchor_id",
        "R_id",
        "wrapped_colour_id",
        "distinguished_pair_id",
        "extra_anchor_payload",
        "separation_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_residual_rows.csv": (
        "residual_id",
        "R_id",
        "residual_component",
        "residual_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_losslessness_rows.csv": (
        "losslessness_id",
        "R_id",
        "wrapped_colour_id",
        "test_pair_id",
        "loss_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "descent_id",
        "R_id",
        "anchor_memory_id",
        "quotient_pseudofunctor_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "anchor_memory_morphism_id",
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
    "anchor_memory_status",
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
        "translation_weight_rows",
        "chi_zero_degeneracy_rows",
        "extra_anchor_data_rows",
        "anchor_residual_rows",
        "anchor_losslessness_rows",
        "quotient_descent_rows",
        "transition_rows",
        "populated_correspondence_anchor_rows",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "quotient_first_hall_product",
        "determinant_anchor_only",
        "scalar_Fock_factor",
        "Borcherds_s_degree",
        "degree_shadow_only",
        "anchor_after_quotient",
        "local_local_anchor_memory",
        "empty_hybrid_carrier",
        "ordinary_Ran_only",
        "target_anchor_forgotten",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check source/target anchor-memory definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/source_target_anchor_memory_definition"),
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
        "fixture_name": "source_target_anchor_memory_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "source_target_anchor_memory_defined": True,
        "before_quotient": True,
        "determinant_anchor_construction": False,
        "translation_weight_certification": False,
        "chi_zero_degeneracy_certification": False,
        "extra_anchor_data_certification": False,
        "anchor_residual_certification": False,
        "anchor_losslessness_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "definition_rows.csv",
        "local_local_exclusion.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected source/target anchor-memory tables")
    expected_imports = {
        "certificates/hybrid/hybrid_ran_prestack_definition",
        "certificates/hybrid/local_stratum_b0_prestack_definition",
        "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition",
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/hybrid/local_local_correspondence_definition",
        "certificates/hybrid/two_sided_mixed_correspondence_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected source/target anchor-memory imports")


def check_definition(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "definition_rows.csv", DEFINITION_COLUMNS, issues)
    if len(table.rows) != len(EXPECTED_DEFINITION_ROWS):
        issues.append("definition_rows.csv must contain exactly LW, WL, WW, and LWL anchor-memory rows")
        return
    by_id = {row.get("anchor_memory_id", ""): row for row in table.rows}
    missing = sorted(set(EXPECTED_DEFINITION_ROWS) - set(by_id))
    extra = sorted(set(by_id) - set(EXPECTED_DEFINITION_ROWS))
    if missing:
        issues.append("missing definition rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected definition rows: " + ", ".join(extra))
    for anchor_memory_id, expected in EXPECTED_DEFINITION_ROWS.items():
        row = by_id.get(anchor_memory_id)
        if row is None:
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"definition row {anchor_memory_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"definition row {anchor_memory_id} lacks proof_reference")


def check_local_local_exclusion(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "local_local_exclusion.csv", LOCAL_LOCAL_EXCLUSION_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("local_local_exclusion.csv must contain exactly one exclusion row")
        return
    row = table.rows[0]
    expected = {
        "exclusion_id": "local_local_has_no_wrapped_anchor",
        "correspondence_definition_id": "local_local_R_correspondence",
        "wrapped_inputs_present": "false",
        "anchor_memory_defined": "false",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"local-local exclusion {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("reason"):
        issues.append("local-local exclusion row lacks reason")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until later anchor rows are supplied")


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
        if row.get("anchor_memory_status") != "missing_open_obligation":
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
            "local_stratum_b0_prestack_definition",
            "LOCAL_STRATUM_B0_PRESTACK_DEFINITION_VERIFIED",
        ),
        (
            "wrapped_stratum_bpositive_prestack_definition",
            "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED",
        ),
        (
            "mixed_local_wrapped_correspondence_definition",
            "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
        (
            "wrapped_wrapped_correspondence_definition",
            "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
        (
            "local_local_correspondence_definition",
            "LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
        (
            "two_sided_mixed_correspondence_definition",
            "TWO_SIDED_MIXED_CORRESPONDENCE_DEFINITION_VERIFIED",
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
    check_local_local_exclusion(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
