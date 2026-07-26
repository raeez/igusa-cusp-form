#!/usr/bin/env python3
"""Verify the finite protected integration Gram-degree packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PROTECTED_INTEGRATION_GRAM_DEGREE_VERIFIED"
EXPECTED_SCHEMA = "protected_integration_gram_degree.v1"
EXPECTED_KIND = "protected_integration_gram_degree"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:protected-integration-gram-degree"

GRAM_LABEL_COLUMNS = (
    "gram_label_id",
    "height",
    "label_family_id",
    "formal_gram_monoid_id",
    "gram_coordinate_map_id",
    "q_coordinate_id",
    "r_coordinate_id",
    "s_coordinate_id",
    "gram_label_defect_rank",
    "pi_x_identification_status",
    "proof_reference",
    "check_status",
    "notes",
)
MONOMIAL_COLUMNS = (
    "monomial_degree_id",
    "height",
    "label_family_id",
    "monomialization_id",
    "target_monomial_family",
    "q_exponent_id",
    "r_exponent_id",
    "s_exponent_id",
    "monomialization_defect_rank",
    "pi_x_identification_status",
    "proof_reference",
    "check_status",
    "notes",
)
INTEGRATION_COLUMNS = (
    "degree_id",
    "height",
    "integration_id",
    "source_charge_family_id",
    "target_label_family_id",
    "target_monomial_family",
    "s_degree_id",
    "integration_degree_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "integration_status",
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
        "transition_compatibility",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "gram_degree_only",
        "Pi_X_vs_b_geom_claim",
        "b_R_geom_as_gram_degree",
        "protected_integration_transition_claim",
        "level_Z_protected_trace",
        "pfaffian_line_or_section",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite protected integration Gram-degree packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/protected_integration_gram_degree"),
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
        "fixture_name": "protected_integration_gram_degree",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "protected_integration_defined": True,
        "product_compatibility_imported": True,
        "coproduct_compatibility_imported": True,
        "primitive_compatibility_imported": True,
        "gram_degree_certification": True,
        "gram_label_defect_rank": 0,
        "monomialization_defect_rank": 0,
        "integration_degree_defect_rank": 0,
        "pi_x_degree_certification": False,
        "transition_compatibility_certification": False,
        "protected_trace_certification": False,
        "pfaffian_line_certification": False,
        "aggregate_hybrid_population": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "gram_label_rows.csv",
        "monomial_degree_rows.csv",
        "integration_degree_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected Gram-degree tables")
    expected_imports = {
        "certificates/hybrid/protected_integration_definition",
        "certificates/hybrid/protected_integration_product_compatibility",
        "certificates/hybrid/protected_integration_coproduct_compatibility",
        "certificates/hybrid/protected_integration_primitive_compatibility",
        "certificates/hybrid/geometric_borcherds_degree_separation",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected Gram-degree imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    defect_key: str,
    issues: list[str],
) -> dict[str, str] | None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return None
    row = table.rows[0]
    if row.get(expected_id_key) != expected_id:
        issues.append(
            f"{table_name} {expected_id_key}: expected {expected_id!r}, "
            f"got {row.get(expected_id_key)!r}"
        )
    if row.get(defect_key) != "0":
        issues.append(f"{table_name} {defect_key} must be zero")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {PROOF_LABEL}")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    gram = require_one_row(
        fixture,
        "gram_label_rows.csv",
        GRAM_LABEL_COLUMNS,
        "gram_label_id",
        "I_prot_gram_labels_R",
        "gram_label_defect_rank",
        issues,
    )
    if gram:
        expected = {
            "label_family_id": "omega_R_labels",
            "formal_gram_monoid_id": "G_R_subset_Z3",
            "gram_coordinate_map_id": "g_R",
            "q_coordinate_id": "n_R",
            "r_coordinate_id": "l_R",
            "s_coordinate_id": "m_R",
            "pi_x_identification_status": "supplied_by_protected_integration_pi_x_separation",
        }
        for key, value in expected.items():
            if gram.get(key) != value:
                issues.append(f"gram row {key}: expected {value!r}, got {gram.get(key)!r}")

    monomial = require_one_row(
        fixture,
        "monomial_degree_rows.csv",
        MONOMIAL_COLUMNS,
        "monomial_degree_id",
        "I_prot_monomialization_R",
        "monomialization_defect_rank",
        issues,
    )
    if monomial:
        expected = {
            "label_family_id": "omega_R_labels",
            "monomialization_id": "chi_R",
            "target_monomial_family": "q_n_r_l_s_m_family",
            "q_exponent_id": "n_R",
            "r_exponent_id": "l_R",
            "s_exponent_id": "m_R",
            "pi_x_identification_status": "supplied_by_protected_integration_pi_x_separation",
        }
        for key, value in expected.items():
            if monomial.get(key) != value:
                issues.append(
                    f"monomial row {key}: expected {value!r}, got {monomial.get(key)!r}"
                )

    degree = require_one_row(
        fixture,
        "integration_degree_rows.csv",
        INTEGRATION_COLUMNS,
        "degree_id",
        "I_prot_gram_degree_R",
        "integration_degree_defect_rank",
        issues,
    )
    if degree:
        expected = {
            "integration_id": "I_R_prot",
            "source_charge_family_id": "Gamma_R",
            "target_label_family_id": "omega_R_labels",
            "target_monomial_family": "q_n_r_l_s_m_family",
            "s_degree_id": "m_R",
        }
        for key, value in expected.items():
            if degree.get(key) != value:
                issues.append(
                    f"integration degree row {key}: expected {value!r}, got {degree.get(key)!r}"
                )


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
        if row.get("integration_status") != "missing_open_obligation":
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
    expected_statuses = {
        "protected_integration_definition": "PROTECTED_INTEGRATION_DEFINITION_VERIFIED",
        "protected_integration_product_compatibility": "PROTECTED_INTEGRATION_PRODUCT_COMPATIBILITY_VERIFIED",
        "protected_integration_coproduct_compatibility": "PROTECTED_INTEGRATION_COPRODUCT_COMPATIBILITY_VERIFIED",
        "protected_integration_primitive_compatibility": "PROTECTED_INTEGRATION_PRIMITIVE_COMPATIBILITY_VERIFIED",
        "geometric_borcherds_degree_separation": "GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED",
    }
    for directory, status in expected_statuses.items():
        manifest = load_json(fixture.parent / directory / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != status:
            issues.append(f"import {directory} status is not {status}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_positive_rows(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("PROTECTED_INTEGRATION_GRAM_DEGREE_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
