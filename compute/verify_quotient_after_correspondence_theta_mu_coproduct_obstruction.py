#!/usr/bin/env python3
"""Verify theta_mu coproduct compatibility for quotient-after-correspondence."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COPRODUCT_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_theta_mu_coproduct.v1"
EXPECTED_KIND = "quotient_after_correspondence_theta_mu_coproduct"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-coproduct"
PRIMITIVE_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-primitives"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

COPRODUCT_COLUMNS = (
    "coproduct_id",
    "R_id",
    "theta_id",
    "coproduct_family",
    "coproduct_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
COPRODUCT_COMPARISON_COLUMNS = (
    "comparison_id",
    "R_id",
    "source_coproduct_id",
    "reduced_coproduct_id",
    "theta_delta_id",
    "coproduct_comparison_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
BIALGEBRA_COLUMNS = (
    "square_id",
    "R_id",
    "source_product_id",
    "source_coproduct_id",
    "reduced_product_id",
    "reduced_coproduct_id",
    "source_bialgebra_identity",
    "reduced_bialgebra_identity",
    "theta_mu_id",
    "theta_delta_id",
    "square_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
PRIMITIVE_COLUMNS = (
    "primitive_id",
    "R_id",
    "theta_id",
    "primitive_projection",
    "primitive_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
TRANSITION_COLUMNS = (
    "transition_id",
    "from_R",
    "to_R",
    "pseudofunctor_id",
    "transition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "protected_integration_rows.csv": (
        "integration_id",
        "R_id",
        "Q_E_R_id",
        "I_prot_id",
        "integration_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "row_type",
        "population_status",
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
    "quotient_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "protected_integration_rows",
        "aggregate_population_rows",
    }
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
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "theta_coproduct_component_only",
        "theta_mu_component_only",
        "theta_associativity_component_only",
        "source_hall_bialgebra_matrix",
        "theta_primitive_component_only",
        "Q_E_R_transition_component_only",
        "protected_integration_claim",
        "scalar_trace",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check quotient theta_mu coproduct compatibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(
            "certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct"
        ),
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
        "fixture_name": "quotient_after_correspondence_theta_mu_coproduct",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "theta_mu_coproduct_compatible": True,
        "quotient_after_correspondence_imported": True,
        "theta_mu_comparison_imported": True,
        "theta_mu_associativity_imported": True,
        "coproduct_certification": True,
        "coproduct_defect_rank": 0,
        "bialgebra_square_defect_rank": 0,
        "primitive_certification": True,
        "transition_certification": True,
        "protected_integration_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "coproduct_rows.csv",
        "coproduct_comparison_rows.csv",
        "bialgebra_square_rows.csv",
        "primitive_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected theta coproduct tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_composition",
        "certificates/hybrid/quotient_after_correspondence_base_change",
        "certificates/hybrid/quotient_after_correspondence_thom_sebastiani",
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_primitives",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected theta coproduct imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    defect_key: str,
    issues: list[str],
    proof_label: str = PROOF_LABEL,
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
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    if proof_label not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {proof_label}")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    coproduct = require_one_row(
        fixture,
        "coproduct_rows.csv",
        COPRODUCT_COLUMNS,
        "coproduct_id",
        "theta_mu_coproduct_R",
        "coproduct_defect_rank",
        issues,
    )
    if coproduct:
        if coproduct.get("theta_id") != "quotient_theta_mu_R":
            issues.append("coproduct row must name quotient_theta_mu_R")
        if coproduct.get("coproduct_family") != "finite_hall_collision_coproduct_rows":
            issues.append("coproduct row must name the finite Hall collision coproduct rows")

    comparison = require_one_row(
        fixture,
        "coproduct_comparison_rows.csv",
        COPRODUCT_COMPARISON_COLUMNS,
        "comparison_id",
        "theta_delta_coproduct_R",
        "coproduct_comparison_defect_rank",
        issues,
    )
    if comparison:
        if comparison.get("source_coproduct_id") != "Delta_R":
            issues.append("coproduct comparison row must name Delta_R")
        if comparison.get("reduced_coproduct_id") != "bar_Delta_R":
            issues.append("coproduct comparison row must name bar_Delta_R")
        if comparison.get("theta_delta_id") != "theta_Q_Delta_R":
            issues.append("coproduct comparison row must name theta_Q_Delta_R")

    square = require_one_row(
        fixture,
        "bialgebra_square_rows.csv",
        BIALGEBRA_COLUMNS,
        "square_id",
        "theta_mu_coproduct_bialgebra_square_R",
        "square_defect_rank",
        issues,
    )
    if square:
        if square.get("theta_mu_id") != "quotient_theta_mu_R":
            issues.append("bialgebra square must name quotient_theta_mu_R")
        if square.get("theta_delta_id") != "theta_Q_Delta_R":
            issues.append("bialgebra square must name theta_Q_Delta_R")
        if square.get("source_bialgebra_identity") != "Delta_mu_equals_m_m_Delta_Delta":
            issues.append("bialgebra square must record the source product-coproduct identity")
        if square.get("reduced_bialgebra_identity") != "bar_Delta_bar_mu_equals_bar_m_bar_m_bar_Delta_bar_Delta":
            issues.append("bialgebra square must record the reduced product-coproduct identity")
    primitive = require_one_row(
        fixture,
        "primitive_rows.csv",
        PRIMITIVE_COLUMNS,
        "primitive_id",
        "theta_mu_primitives_R",
        "primitive_defect_rank",
        issues,
        PRIMITIVE_PROOF_LABEL,
    )
    if primitive:
        if primitive.get("theta_id") != "quotient_theta_mu_R":
            issues.append("primitive row must name quotient_theta_mu_R")
        if primitive.get("primitive_projection") != "primitive_projection_P_R":
            issues.append("primitive row must name primitive_projection_P_R")
    transition = require_one_row(
        fixture,
        "transition_rows.csv",
        TRANSITION_COLUMNS,
        "transition_id",
        "Q_E_R_hn_transition_Rprime_R",
        "transition_defect_rank",
        issues,
        TRANSITION_PROOF_LABEL,
    )
    if transition and transition.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
        issues.append("transition row must name the quotient-after-correspondence pseudofunctor")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the theta coproduct packet")


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
        if row.get("quotient_status") != "missing_open_obligation":
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


def check_import_statuses(fixture: Path, issues: list[str]) -> None:
    repo_root = fixture.parents[2]
    expected_hybrid_statuses = {
        "quotient_after_correspondence_composition": "QUOTIENT_AFTER_CORRESPONDENCE_COMPOSITION_VERIFIED",
        "quotient_after_correspondence_base_change": "QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        "quotient_after_correspondence_thom_sebastiani": "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED",
        "quotient_after_correspondence_bm_chain_functor": "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED",
        "quotient_after_correspondence_theta_mu_comparison": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED",
        "quotient_after_correspondence_theta_mu_associativity": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED",
        "quotient_after_correspondence_theta_mu_primitives": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_PRIMITIVES_VERIFIED",
        "quotient_after_correspondence_hn_transition_compatibility": "QUOTIENT_AFTER_CORRESPONDENCE_HN_TRANSITION_COMPATIBILITY_VERIFIED",
    }
    for relative, expected_status in expected_hybrid_statuses.items():
        manifest = load_json(
            repo_root / "certificates" / "hybrid" / relative / MANIFEST_NAME,
            issues,
        )
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
    check_positive_rows(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COPRODUCT_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
