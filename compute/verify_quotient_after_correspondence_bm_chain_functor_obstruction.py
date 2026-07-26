#!/usr/bin/env python3
"""Verify the quotient-after-correspondence Borel--Moore chain functor packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_bm_chain_functor.v1"
EXPECTED_KIND = "quotient_after_correspondence_bm_chain_functor"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-borel-moore-chain-functor"
THETA_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-comparison"
ASSOC_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-associativity"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

BM_COLUMNS = (
    "bm_id",
    "R_id",
    "pseudofunctor_id",
    "Q_E_R_id",
    "bm_chain_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
OBJECT_COLUMNS = (
    "object_id",
    "R_id",
    "source_object",
    "source_coefficient",
    "quotient_object",
    "quotient_coefficient",
    "source_chain_complex",
    "target_chain_complex",
    "object_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
MORPHISM_COLUMNS = (
    "morphism_id",
    "R_id",
    "equivariant_morphism",
    "descended_morphism",
    "chain_map",
    "descent_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
FUNCTORIALITY_COLUMNS = (
    "functoriality_id",
    "R_id",
    "identity_defect_rank",
    "composition_defect_rank",
    "chain_functor",
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
THETA_COLUMNS = (
    "theta_id",
    "R_id",
    "pseudofunctor_id",
    "operation_id",
    "theta_mu_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
FLAG_COLUMNS = (
    "flag_id",
    "R_id",
    "pseudofunctor_id",
    "flag_defect_rank",
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
        "bm_chain_functor_component_only",
        "q_bang_trace",
        "theta_mu_component_only",
        "pull_push_operation_comparison_component_only",
        "compact_support_pushforward_base_change_claim",
        "flag_coherence_component_only",
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
        description="Check quotient-after-correspondence Borel--Moore chain functor packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/quotient_after_correspondence_bm_chain_functor"),
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
        "fixture_name": "quotient_after_correspondence_bm_chain_functor",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "bm_chain_functor_constructed": True,
        "quotient_after_correspondence_imported": True,
        "quotient_first_exclusion_imported": True,
        "coefficient_descent_required": True,
        "quotient_stack_descent_used": True,
        "verdier_dual_bm_definition_used": True,
        "bm_chain_defect_rank": 0,
        "compact_support_pushforward_base_change": False,
        "flag_certification": True,
        "theta_mu_certification": True,
        "operation_comparison_constructed": True,
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
        "bm_chain_functor_rows.csv",
        "bm_object_rows.csv",
        "coefficient_morphism_rows.csv",
        "functoriality_rows.csv",
        "theta_mu_rows.csv",
        "flag_coherence_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected BM chain functor tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition",
        "certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected BM chain functor imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    defect_keys: tuple[str, ...],
    issues: list[str],
) -> dict[str, str] | None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return None
    row = table.rows[0]
    if row.get(expected_id_key) != expected_id:
        issues.append(
            f"{table_name} {expected_id_key}: expected {expected_id!r}, got {row.get(expected_id_key)!r}"
        )
    for defect_key in defect_keys:
        if row.get(defect_key) != "0":
            issues.append(f"{table_name} {defect_key} must be zero")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {PROOF_LABEL}")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    bm = require_one_row(
        fixture,
        "bm_chain_functor_rows.csv",
        BM_COLUMNS,
        "bm_id",
        "quotient_bm_chain_functor_R",
        ("bm_chain_defect_rank",),
        issues,
    )
    if bm and bm.get("Q_E_R_id") != "Q_E_R":
        issues.append("BM row must name Q_E_R")

    obj = require_one_row(
        fixture,
        "bm_object_rows.csv",
        OBJECT_COLUMNS,
        "object_id",
        "bm_object_quotient_presented_R",
        ("object_defect_rank",),
        issues,
    )
    if obj and obj.get("quotient_object") != "bar_Y_equals_bracket_Y_slash_E":
        issues.append("BM object row must use the quotient stack [Y/E]")
    if obj:
        source_chain = obj.get("source_chain_complex", "")
        target_chain = obj.get("target_chain_complex", "")
        if "equals" not in source_chain or target_chain not in source_chain:
            issues.append("BM object row must define equivariant chains by the quotient chain complex")

    morphism = require_one_row(
        fixture,
        "coefficient_morphism_rows.csv",
        MORPHISM_COLUMNS,
        "morphism_id",
        "bm_coefficient_morphism_R",
        ("descent_defect_rank",),
        issues,
    )
    if morphism and morphism.get("descended_morphism") != "bar_alpha_KbarY_to_LbarY":
        issues.append("coefficient morphism row must name the descended morphism")

    functoriality = require_one_row(
        fixture,
        "functoriality_rows.csv",
        FUNCTORIALITY_COLUMNS,
        "functoriality_id",
        "bm_functoriality_R",
        ("identity_defect_rank", "composition_defect_rank"),
        issues,
    )
    if functoriality and functoriality.get("chain_functor") != "Q_E_R":
        issues.append("functoriality row must name Q_E_R")
    theta = load_csv(fixture / "theta_mu_rows.csv", THETA_COLUMNS, issues)
    if len(theta.rows) != 1:
        issues.append("theta_mu_rows.csv must contain exactly one row")
    else:
        row = theta.rows[0]
        if row.get("theta_id") != "quotient_theta_mu_R":
            issues.append("theta_mu_rows.csv theta_id must be quotient_theta_mu_R")
        if row.get("theta_mu_defect_rank") != "0":
            issues.append("theta_mu_rows.csv theta_mu_defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("theta_mu_rows.csv row is not verified")
        if THETA_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("theta_mu_rows.csv row does not point to the row-252 theorem")
    flag = load_csv(fixture / "flag_coherence_rows.csv", FLAG_COLUMNS, issues)
    if len(flag.rows) != 1:
        issues.append("flag_coherence_rows.csv must contain exactly one row")
    else:
        row = flag.rows[0]
        if row.get("flag_id") != "quotient_theta_associativity_flags_R":
            issues.append("flag_coherence_rows.csv flag_id must be quotient_theta_associativity_flags_R")
        if row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("flag_coherence_rows.csv must name the quotient-after-correspondence pseudofunctor")
        if row.get("flag_defect_rank") != "0":
            issues.append("flag_coherence_rows.csv flag_defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("flag_coherence_rows.csv row is not verified")
        if ASSOC_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("flag_coherence_rows.csv row does not point to the row-253 theorem")
    transition = load_csv(fixture / "transition_rows.csv", TRANSITION_COLUMNS, issues)
    if len(transition.rows) != 1:
        issues.append("transition_rows.csv must contain exactly one row")
    else:
        row = transition.rows[0]
        if row.get("transition_id") != "Q_E_R_hn_transition_Rprime_R":
            issues.append("transition_rows.csv transition_id must be Q_E_R_hn_transition_Rprime_R")
        if row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition_rows.csv must name the quotient-after-correspondence pseudofunctor")
        if row.get("transition_defect_rank") != "0":
            issues.append("transition_rows.csv transition_defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("transition_rows.csv row is not verified")
        if TRANSITION_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("transition_rows.csv row does not point to the row-256 theorem")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the BM chain functor packet")


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
        "quotient_after_correspondence_pseudofunctor_definition": "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED",
        "quotient_after_correspondence_quotient_first_exclusion": "QUOTIENT_AFTER_CORRESPONDENCE_QUOTIENT_FIRST_EXCLUSION_VERIFIED",
        "quotient_after_correspondence_theta_mu_comparison": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED",
        "quotient_after_correspondence_theta_mu_associativity": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED",
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
        print("QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
