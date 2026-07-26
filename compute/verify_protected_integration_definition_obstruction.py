#!/usr/bin/env python3
"""Verify the finite protected integration definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PROTECTED_INTEGRATION_DEFINITION_VERIFIED"
EXPECTED_SCHEMA = "protected_integration_definition.v1"
EXPECTED_KIND = "protected_integration_definition"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:protected-integration-definition"
DEFINITION_LABEL = "def:finite-protected-integration-datum"

INTEGRATION_COLUMNS = (
    "integration_id",
    "height",
    "domain_id",
    "codomain_id",
    "charge_decomposition_id",
    "chain_map_id",
    "definition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
FUNCTIONAL_COLUMNS = (
    "functional_id",
    "height",
    "charge_family_id",
    "source_summand_id",
    "target_line_id",
    "chain_degree",
    "chain_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
LABEL_COLUMNS = (
    "label_id",
    "height",
    "charge_family_id",
    "monoid_id",
    "label_map_id",
    "target_basis_id",
    "gram_identification_status",
    "pi_x_identification_status",
    "proof_reference",
    "check_status",
    "notes",
)
COMPATIBILITY_COLUMNS = (
    "compatibility_id",
    "compatibility_type",
    "defect_rank",
    "certification_status",
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
        "level_Z_protected_trace",
        "pfaffian_line_or_section",
        "scalar_borcherds_product",
        "borcherds_s_degree_only",
        "b_R_geom_as_trace_degree",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite protected integration definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/protected_integration_definition"),
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
        "fixture_name": "protected_integration_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "protected_integration_defined": True,
        "chain_map_certification": True,
        "definition_defect_rank": 0,
        "chargewise_functionals_supplied": True,
        "abstract_monomial_labels": True,
        "product_compatibility_certification": False,
        "coproduct_compatibility_certification": False,
        "primitive_compatibility_certification": False,
        "transition_compatibility_certification": False,
        "gram_degree_certification": False,
        "pi_x_degree_certification": False,
        "protected_trace_certification": False,
        "pfaffian_line_certification": False,
        "aggregate_hybrid_population": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "integration_rows.csv",
        "charge_functional_rows.csv",
        "monomial_label_rows.csv",
        "compatibility_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected protected integration tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
        "certificates/hybrid/geometric_borcherds_degree_separation",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected protected integration imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    defect_key: str | None,
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
    if defect_key is not None and row.get(defect_key) != "0":
        issues.append(f"{table_name} {defect_key} must be zero")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    integration = require_one_row(
        fixture,
        "integration_rows.csv",
        INTEGRATION_COLUMNS,
        "integration_id",
        "I_R_prot_definition",
        "definition_defect_rank",
        issues,
    )
    if integration:
        if PROOF_LABEL not in integration.get("proof_reference", ""):
            issues.append("integration row does not point to protected integration proposition")
        expected = {
            "domain_id": "Q_E_R_F_hyb_X_sigma_S_le_R",
            "codomain_id": "C_T_R_le_R",
            "charge_decomposition_id": "Gamma_R_charge_decomposition",
            "chain_map_id": "chargewise_direct_sum_chain_map",
        }
        for key, value in expected.items():
            if integration.get(key) != value:
                issues.append(
                    f"integration row {key}: expected {value!r}, got {integration.get(key)!r}"
                )

    functional = require_one_row(
        fixture,
        "charge_functional_rows.csv",
        FUNCTIONAL_COLUMNS,
        "functional_id",
        "chargewise_protected_integrals_R",
        "chain_defect_rank",
        issues,
    )
    if functional:
        if functional.get("chain_degree") != "0":
            issues.append("charge functional row must have chain_degree=0")
        if DEFINITION_LABEL not in functional.get("proof_reference", ""):
            issues.append("charge functional row does not point to the definition")

    label = require_one_row(
        fixture,
        "monomial_label_rows.csv",
        LABEL_COLUMNS,
        "label_id",
        "abstract_integration_labels_R",
        None,
        issues,
    )
    if label:
        if label.get("gram_identification_status") != "not_certified":
            issues.append("monomial labels must leave Gram identification uncertified")
        if label.get("pi_x_identification_status") != "not_certified":
            issues.append("monomial labels must leave Pi_X identification uncertified")
        if DEFINITION_LABEL not in label.get("proof_reference", ""):
            issues.append("monomial label row does not point to the definition")


def check_compatibility_rows_empty(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "compatibility_rows.csv", COMPATIBILITY_COLUMNS, issues)
    if table.rows:
        issues.append("compatibility_rows.csv must remain empty for row 257")


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
    bm = load_json(
        fixture.parent / "quotient_after_correspondence_bm_chain_functor" / MANIFEST_NAME,
        issues,
    )
    if bm and bm.get("status") != "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED":
        issues.append("BM chain functor import is not verified")
    sep = load_json(
        fixture.parent / "geometric_borcherds_degree_separation" / MANIFEST_NAME,
        issues,
    )
    if sep:
        expected = {
            "status": "GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED",
            "separation_certified": True,
            "equality_certification": False,
        }
        for key, value in expected.items():
            if sep.get(key) != value:
                issues.append(
                    f"degree-separation manifest {key}: expected {value!r}, got {sep.get(key)!r}"
                )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_positive_rows(fixture, issues)
    check_compatibility_rows_empty(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("PROTECTED_INTEGRATION_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
