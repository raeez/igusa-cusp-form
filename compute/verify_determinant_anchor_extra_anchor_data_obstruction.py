#!/usr/bin/env python3
"""Verify the determinant-anchor extra-anchor-data packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "DETERMINANT_ANCHOR_EXTRA_ANCHOR_DATA_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "determinant_anchor_extra_anchor_data.v1"
EXPECTED_KIND = "determinant_anchor_extra_anchor_data"
EXTRA_ANCHOR_COLUMNS = (
    "extra_anchor_id",
    "R_id",
    "wrapped_colour_id",
    "elliptic_pushforward_row",
    "semistable_degree_zero_status",
    "rank_symbol",
    "extra_anchor_payload",
    "target",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_EXTRA_ANCHOR = {
    "extra_anchor_id": "extra_anchor_jh_divisor_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "elliptic_pushforward_row": "V_eta_R_equals_Rpi_E_star_F_eta_on_vector_bundle_row",
    "semistable_degree_zero_status": "semistable_degree_zero_vector_bundle",
    "rank_symbol": "r_eta",
    "extra_anchor_payload": "degree_zero_jordan_holder_divisor",
    "target": "Sym^r_eta_Pic0_E",
    "check_status": "verified",
}
REFINEMENT_COLUMNS = (
    "refinement_id",
    "extra_anchor_id",
    "abel_sum_map",
    "determinant_formula",
    "refinement_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_REFINEMENT = {
    "refinement_id": "extra_anchor_ab_sum_refines_det",
    "extra_anchor_id": "extra_anchor_jh_divisor_R",
    "abel_sum_map": "Sym^r_Pic0_E_to_Pic0_E_sum",
    "determinant_formula": "sum_i_L_i_equals_det_V",
    "refinement_defect_rank": "0",
    "check_status": "verified",
}
SEPARATION_COLUMNS = (
    "separation_id",
    "extra_anchor_id",
    "left_bundle",
    "right_bundle",
    "condition",
    "determinant_left",
    "determinant_right",
    "extra_anchor_left",
    "extra_anchor_right",
    "separation_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_SEPARATION = {
    "separation_id": "rank_two_O2_vs_L_Linv",
    "extra_anchor_id": "extra_anchor_jh_divisor_R",
    "left_bundle": "O_E_oplus_2",
    "right_bundle": "L_plus_L_inverse",
    "condition": "L_not_equal_O_E",
    "determinant_left": "O_E",
    "determinant_right": "O_E",
    "extra_anchor_left": "2[O_E]",
    "extra_anchor_right": "[L]+[L_inverse]",
    "separation_defect_rank": "0",
    "check_status": "verified",
}
EMPTY_TABLES = {
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
    "anchor_residual_rows.csv": (
        "residual_id",
        "R_id",
        "residual_component",
        "residual_defect_rank",
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
        "extra_anchor_morphism_id",
        "extra_anchor_compatibility_defect_rank",
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
    "extra_anchor_status",
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
        "anchor_losslessness_rows",
        "anchor_residual_rows",
        "quotient_descent_rows",
        "stabilizer_linearization_rows",
        "transition_rows",
        "populated_wrapped_prequotient_rows",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "determinant_anchor_only",
        "chi_zero_degeneracy_only",
        "translation_weight_only",
        "anchor_losslessness",
        "anchor_residual",
        "quotient_descent",
        "stabilizer_linearization",
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
        description="Check determinant-anchor extra-anchor-data packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/determinant_anchor_extra_anchor_data"),
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
        "fixture_name": "determinant_anchor_extra_anchor_data",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "chi_zero_degeneracy_imported": True,
        "extra_anchor_data_defined": True,
        "extra_anchor_payload": "degree_zero_jordan_holder_divisor",
        "target": "Sym^r_Pic0_E",
        "determinant_refinement_certified": True,
        "rank_two_test_pair_separated": True,
        "test_pair": "O_E^oplus2_vs_L_plus_L_inverse",
        "losslessness_certification": False,
        "anchor_residual_certification": False,
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
        "extra_anchor_rows.csv",
        "determinant_refinement_rows.csv",
        "rank_two_separation_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected extra-anchor tables")
    expected_imports = {
        "certificates/hybrid/determinant_anchor_chi_zero_degeneracy"
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected extra-anchor imports")


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
        if row.get("extra_anchor_status") != "missing_open_obligation":
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
    chi_zero_manifest = load_json(
        fixture.parent / "determinant_anchor_chi_zero_degeneracy" / MANIFEST_NAME,
        issues,
    )
    if chi_zero_manifest and chi_zero_manifest.get("status") != (
        "DETERMINANT_ANCHOR_CHI_ZERO_DEGENERACY_VERIFIED"
    ):
        issues.append("determinant_anchor_chi_zero_degeneracy import is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(
        fixture,
        "extra_anchor_rows.csv",
        EXTRA_ANCHOR_COLUMNS,
        EXPECTED_EXTRA_ANCHOR,
        issues,
    )
    check_single_row(
        fixture,
        "determinant_refinement_rows.csv",
        REFINEMENT_COLUMNS,
        EXPECTED_REFINEMENT,
        issues,
    )
    check_single_row(
        fixture,
        "rank_two_separation_rows.csv",
        SEPARATION_COLUMNS,
        EXPECTED_SEPARATION,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("DETERMINANT_ANCHOR_EXTRA_ANCHOR_DATA_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
