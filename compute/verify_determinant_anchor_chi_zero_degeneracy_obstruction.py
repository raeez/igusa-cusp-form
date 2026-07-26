#!/usr/bin/env python3
"""Verify the determinant-anchor chi-zero degeneracy packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "DETERMINANT_ANCHOR_CHI_ZERO_DEGENERACY_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "determinant_anchor_chi_zero_degeneracy.v1"
EXPECTED_KIND = "determinant_anchor_chi_zero_degeneracy"
DEGENERACY_COLUMNS = (
    "degeneracy_id",
    "R_id",
    "wrapped_colour_id",
    "determinant_anchor_id",
    "chi_value",
    "translation_weight",
    "orbit_kernel",
    "orbit_behavior",
    "separation_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_DEGENERACY = {
    "degeneracy_id": "det_anchor_chi_zero_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "determinant_anchor_id": "lambda_det_eta_R",
    "chi_value": "0",
    "translation_weight": "0",
    "orbit_kernel": "all_E",
    "orbit_behavior": "lambda_det_constant_on_E_translation_orbits",
    "separation_defect_rank": "1",
    "check_status": "verified",
}
ORBIT_COLUMNS = (
    "witness_id",
    "degeneracy_id",
    "translation_action_id",
    "free_action_status",
    "distinctness_condition",
    "anchor_equality",
    "loss_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ORBIT = {
    "witness_id": "det_anchor_chi_zero_orbit_witness",
    "degeneracy_id": "det_anchor_chi_zero_R",
    "translation_action_id": "retained_E_translation_action",
    "free_action_status": "free_on_retained_row",
    "distinctness_condition": "a_nonzero_gives_F_not_equal_a_dot_F",
    "anchor_equality": "lambda_det_F_equals_lambda_det_a_dot_F",
    "loss_defect_rank": "1",
    "check_status": "verified",
}
REPAIR_COLUMNS = (
    "requirement_id",
    "degeneracy_id",
    "required_next_row",
    "required_payload",
    "repair_status",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_REPAIR = {
    "requirement_id": "det_anchor_chi_zero_extra_anchor_required",
    "degeneracy_id": "det_anchor_chi_zero_R",
    "required_next_row": "row_216_extra_anchor_data",
    "required_payload": "determinant_refining_extra_anchor_data_on_chi_zero_branch",
    "repair_status": "not_constructed_here",
    "check_status": "verified",
}
EMPTY_TABLES = {
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
        "chi_zero_anchor_morphism_id",
        "chi_zero_compatibility_defect_rank",
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
    "chi_zero_status",
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
        "determinant_anchor_only",
        "translation_weight_only",
        "extra_anchor_data_constructed",
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
        description="Check determinant-anchor chi-zero degeneracy packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/determinant_anchor_chi_zero_degeneracy"),
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
        "fixture_name": "determinant_anchor_chi_zero_degeneracy",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "translation_weight_imported": True,
        "translation_action_imported": True,
        "chi_zero_degeneracy_certified": True,
        "chi_zero_weight": "0",
        "orbit_kernel": "all_E",
        "determinant_anchor_orbit_constant": True,
        "free_orbit_separation_defect_rank": 1,
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
        "degeneracy_rows.csv",
        "orbit_witness_rows.csv",
        "repair_requirement_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected chi-zero tables")
    expected_imports = {
        "certificates/hybrid/determinant_anchor_translation_weight",
        "certificates/moduli/retained_e_translation_rigidifications",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected chi-zero imports")


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
        if row.get("chi_zero_status") != "missing_open_obligation":
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
    weight_manifest = load_json(
        fixture.parent / "determinant_anchor_translation_weight" / MANIFEST_NAME,
        issues,
    )
    if weight_manifest and weight_manifest.get("status") != (
        "DETERMINANT_ANCHOR_TRANSLATION_WEIGHT_VERIFIED"
    ):
        issues.append("determinant_anchor_translation_weight import is not verified")
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
        "degeneracy_rows.csv",
        DEGENERACY_COLUMNS,
        EXPECTED_DEGENERACY,
        issues,
    )
    check_single_row(
        fixture,
        "orbit_witness_rows.csv",
        ORBIT_COLUMNS,
        EXPECTED_ORBIT,
        issues,
    )
    check_single_row(
        fixture,
        "repair_requirement_rows.csv",
        REPAIR_COLUMNS,
        EXPECTED_REPAIR,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("DETERMINANT_ANCHOR_CHI_ZERO_DEGENERACY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
