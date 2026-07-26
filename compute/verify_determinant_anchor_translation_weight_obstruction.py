#!/usr/bin/env python3
"""Verify the determinant-anchor translation-weight packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "DETERMINANT_ANCHOR_TRANSLATION_WEIGHT_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "determinant_anchor_translation_weight.v1"
EXPECTED_KIND = "determinant_anchor_translation_weight"
TRANSLATION_COLUMNS = (
    "weight_row_id",
    "R_id",
    "wrapped_colour_id",
    "determinant_anchor_id",
    "translation_action_model",
    "translated_family_formula",
    "determinant_line_translation",
    "relative_picard_identity",
    "translation_weight",
    "sign_convention",
    "weight_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_TRANSLATION = {
    "weight_row_id": "det_anchor_translation_weight_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "determinant_anchor_id": "lambda_det_eta_R",
    "translation_action_model": "support_translation_pushforward_tau_a",
    "translated_family_formula": "a_dot_F_equals_id_S_times_tau_a_pushforward_F",
    "determinant_line_translation": "det_Rpi_star_a_dot_F_equals_tau_minus_a_star_det_Rpi_star_F",
    "relative_picard_identity": "lambda_det_a_dot_F_equals_lambda_det_F_tensor_O_E_chi_eta_a_minus_zero_E",
    "translation_weight": "chi_eta",
    "sign_convention": "positive_for_pushforward_support_translation",
    "weight_defect_rank": "0",
    "check_status": "verified",
}
KERNEL_COLUMNS = (
    "kernel_row_id",
    "weight_row_id",
    "nonzero_chi_kernel",
    "zero_chi_kernel",
    "degeneracy_status",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_KERNEL = {
    "kernel_row_id": "det_anchor_translation_kernel_R",
    "weight_row_id": "det_anchor_translation_weight_R",
    "nonzero_chi_kernel": "ker_[chi_eta]=E[chi_eta]",
    "zero_chi_kernel": "all_E_when_chi_eta_equals_0",
    "degeneracy_status": "chi_zero_degeneracy_not_repaired",
    "check_status": "verified",
}
STABILIZER_COLUMNS = (
    "restriction_id",
    "weight_row_id",
    "stabilizer_id",
    "restriction_formula",
    "invariance_condition",
    "linearization_status",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_STABILIZER = {
    "restriction_id": "det_anchor_translation_weight_H",
    "weight_row_id": "det_anchor_translation_weight_R",
    "stabilizer_id": "H_subset_E_N",
    "restriction_formula": "h_maps_to_chi_eta_h",
    "invariance_condition": "H_lies_in_E[chi_eta]_for_class_invariance",
    "linearization_status": "linearization_not_certified",
    "check_status": "verified",
}
EMPTY_TABLES = {
    "unit_weight_rows.csv": (
        "unit_row_id",
        "R_id",
        "wrapped_colour_id",
        "finite_cover_id",
        "unit_weight_defect_rank",
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
        "anchor_map",
        "quotient_pseudofunctor_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "stabilizer_linearization_rows.csv": (
        "linearization_id",
        "R_id",
        "wrapped_colour_id",
        "stabilizer_id",
        "character_formula",
        "linearization_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "determinant_anchor_weight_morphism_id",
        "weight_compatibility_defect_rank",
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
    "translation_weight_status",
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
        "unit_weight_rows",
        "chi_zero_degeneracy_rows",
        "extra_anchor_data_rows",
        "anchor_residual_rows",
        "anchor_losslessness_rows",
        "quotient_descent_rows",
        "stabilizer_linearization_rows",
        "transition_rows",
        "populated_wrapped_prequotient_rows",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "determinant_anchor_construction_only",
        "pullback_translation_sign_without_convention",
        "unit_weight_claim",
        "chi_zero_repair",
        "extra_anchor_data",
        "anchor_residual",
        "anchor_losslessness",
        "quotient_descent",
        "stabilizer_linearization",
        "mod2_orientation_character",
        "scalar_Fock_factor",
        "Borcherds_s_degree",
        "ordinary_Ran_only",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check determinant-anchor translation-weight packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/determinant_anchor_translation_weight"),
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
        "fixture_name": "determinant_anchor_translation_weight",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "determinant_anchor_construction_imported": True,
        "translation_action_imported": True,
        "translation_weight_certified": True,
        "translation_weight": "chi_eta",
        "support_translation_convention": "pushforward_by_tau_a",
        "unit_weight_certification": False,
        "chi_zero_degeneracy_certification": False,
        "extra_anchor_data_certification": False,
        "anchor_residual_certification": False,
        "anchor_losslessness_certification": False,
        "quotient_descent_certification": False,
        "stabilizer_linearization_certification": False,
        "transition_certification": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "translation_weight_rows.csv",
        "kernel_rows.csv",
        "stabilizer_restriction_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected translation-weight tables")
    expected_imports = {
        "certificates/hybrid/determinant_anchor_construction",
        "certificates/moduli/retained_e_translation_rigidifications",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected translation-weight imports")


def check_single_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected: dict[str, str],
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one verified row")
        return
    row = table.rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"{table_name} {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append(f"{table_name} row lacks proof_reference")


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
        if row.get("translation_weight_status") != "missing_open_obligation":
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
    determinant_manifest = load_json(
        fixture.parent / "determinant_anchor_construction" / MANIFEST_NAME,
        issues,
    )
    if determinant_manifest and determinant_manifest.get("status") != (
        "DETERMINANT_ANCHOR_CONSTRUCTION_VERIFIED"
    ):
        issues.append("determinant_anchor_construction import is not verified")
    moduli_manifest = load_json(
        fixture.parents[1] / "moduli" / "retained_e_translation_rigidifications" / MANIFEST_NAME,
        issues,
    )
    if moduli_manifest:
        expected = {
            "certified": True,
            "e_translation_rigidifications": True,
            "translations_removed": True,
        }
        for key, value in expected.items():
            if moduli_manifest.get(key) != value:
                issues.append(
                    f"retained_e_translation_rigidifications {key}: "
                    f"expected {value!r}, got {moduli_manifest.get(key)!r}"
                )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(
        fixture,
        "translation_weight_rows.csv",
        TRANSLATION_COLUMNS,
        EXPECTED_TRANSLATION,
        issues,
    )
    check_single_row(fixture, "kernel_rows.csv", KERNEL_COLUMNS, EXPECTED_KERNEL, issues)
    check_single_row(
        fixture,
        "stabilizer_restriction_rows.csv",
        STABILIZER_COLUMNS,
        EXPECTED_STABILIZER,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("DETERMINANT_ANCHOR_TRANSLATION_WEIGHT_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
