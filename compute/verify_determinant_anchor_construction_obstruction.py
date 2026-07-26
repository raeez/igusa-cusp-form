#!/usr/bin/env python3
"""Verify the determinant-anchor construction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "DETERMINANT_ANCHOR_CONSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "determinant_anchor_construction.v1"
EXPECTED_KIND = "determinant_anchor_construction"
CONSTRUCTION_COLUMNS = (
    "construction_id",
    "R_id",
    "wrapped_colour_id",
    "universal_family_id",
    "projection_map",
    "determinant_line_formula",
    "normalization_divisor",
    "euler_characteristic_symbol",
    "target_picard",
    "anchor_map",
    "translation_weight_claimed",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_CONSTRUCTION = {
    "construction_id": "det_anchor_lambda_F_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "universal_family_id": "F_eta_R_universal_perfect_complex",
    "projection_map": "pi_E_T_X_times_T_to_E_times_T",
    "determinant_line_formula": "det_Rpi_E_T_star_F_eta_R_tensor_O_E_minus_chi_eta_zero_E",
    "normalization_divisor": "chi_eta_zero_E",
    "euler_characteristic_symbol": "chi_eta",
    "target_picard": "Pic0_E_isomorphic_E",
    "anchor_map": "lambda_det_eta_R",
    "translation_weight_claimed": "false",
    "check_status": "verified",
}
DEGREE_COLUMNS = (
    "degree_id",
    "construction_id",
    "determinant_degree",
    "normalization_degree",
    "target_component",
    "degree_zero_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_DEGREE = {
    "degree_id": "det_anchor_degree_zero_R",
    "construction_id": "det_anchor_lambda_F_R",
    "determinant_degree": "chi_eta",
    "normalization_degree": "minus_chi_eta",
    "target_component": "Pic0_E",
    "degree_zero_defect_rank": "0",
    "check_status": "verified",
}
FUNCTORIALITY_COLUMNS = (
    "functoriality_id",
    "construction_id",
    "morphism_type",
    "base_change_identity",
    "determinant_functor_source",
    "functoriality_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_FUNCTORIALITY = {
    "functoriality_id": "det_anchor_T_pullback",
    "construction_id": "det_anchor_lambda_F_R",
    "morphism_type": "Tprime_to_T",
    "base_change_identity": "pullback_det_Rpi_star_F_equals_det_Rpi_star_pullback_F_mod_base_line",
    "determinant_functor_source": "Knudsen_Mumford_Deligne_determinant_of_cohomology",
    "functoriality_defect_rank": "0",
    "check_status": "verified",
}
EMPTY_TABLES = {
    "translation_weight_rows.csv": (
        "weight_row_id",
        "R_id",
        "wrapped_colour_id",
        "translation_action_model",
        "translation_weight",
        "weight_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
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
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "determinant_anchor_morphism_id",
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
    "determinant_anchor_status",
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
        "unit_weight_rows",
        "chi_zero_degeneracy_rows",
        "extra_anchor_data_rows",
        "anchor_residual_rows",
        "anchor_losslessness_rows",
        "quotient_descent_rows",
        "transition_rows",
        "populated_wrapped_prequotient_rows",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "translation_weight_claim",
        "unit_weight_claim",
        "chi_zero_repair",
        "extra_anchor_data",
        "anchor_residual",
        "anchor_losslessness",
        "quotient_descent",
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
        description="Check determinant-anchor construction packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/determinant_anchor_construction"),
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
        "fixture_name": "determinant_anchor_construction",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "determinant_anchor_constructed": True,
        "pic0_valued": True,
        "degree_normalization_defined": True,
        "determinant_functoriality_certified": True,
        "translation_weight_certification": False,
        "unit_weight_certification": False,
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
        "construction_rows.csv",
        "degree_rows.csv",
        "functoriality_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected determinant-anchor tables")
    expected_imports = {
        "certificates/moduli/retained_universal_complexes",
        "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition",
        "certificates/hybrid/source_target_anchor_memory_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected determinant-anchor imports")


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
        if row.get("determinant_anchor_status") != "missing_open_obligation":
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
    retained_manifest = load_json(
        fixture.parents[1] / "moduli" / "retained_universal_complexes" / MANIFEST_NAME,
        issues,
    )
    if retained_manifest and retained_manifest.get("certified") is not True:
        issues.append("retained_universal_complexes is not certified")
    for relative, expected_status in (
        (
            "wrapped_stratum_bpositive_prestack_definition",
            "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED",
        ),
        (
            "source_target_anchor_memory_definition",
            "SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED",
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
    check_single_row(
        fixture,
        "construction_rows.csv",
        CONSTRUCTION_COLUMNS,
        EXPECTED_CONSTRUCTION,
        issues,
    )
    check_single_row(fixture, "degree_rows.csv", DEGREE_COLUMNS, EXPECTED_DEGREE, issues)
    check_single_row(
        fixture,
        "functoriality_rows.csv",
        FUNCTORIALITY_COLUMNS,
        EXPECTED_FUNCTORIALITY,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("DETERMINANT_ANCHOR_CONSTRUCTION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
