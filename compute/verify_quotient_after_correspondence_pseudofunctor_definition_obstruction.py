#!/usr/bin/env python3
"""Verify the quotient-after-correspondence pseudofunctor definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED"
EXPECTED_SCHEMA = "quotient_after_correspondence_pseudofunctor_definition.v1"
EXPECTED_KIND = "quotient_after_correspondence_pseudofunctor_definition"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
COMPOSITION_PROOF_LABEL = "prop:quotient-after-correspondence-preserves-composition"
BASE_CHANGE_PROOF_LABEL = "prop:quotient-after-correspondence-preserves-base-change"
TS_PROOF_LABEL = "prop:quotient-after-correspondence-preserves-thom-sebastiani"
QFIRST_PROOF_LABEL = "prop:quotient-after-correspondence-excludes-quotient-first"
BM_PROOF_LABEL = "prop:quotient-after-correspondence-borel-moore-chain-functor"
THETA_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-comparison"
ASSOC_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-associativity"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

OBJECT_COLUMNS = (
    "object_assignment_id",
    "R_id",
    "source_object_family",
    "quotient_object_family",
    "quotient_map_id",
    "e_action_required",
    "coefficient_descent_interface",
    "definition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
ARROW_COLUMNS = (
    "arrow_assignment_id",
    "R_id",
    "source_arrow_family",
    "source_correspondence",
    "reduced_correspondence",
    "pseudofunctor_arrow",
    "quotient_after_not_first",
    "definition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
COEFFICIENT_COLUMNS = (
    "interface_id",
    "R_id",
    "coefficient_source",
    "coefficient_target",
    "pullback_identity",
    "linearization_required",
    "orientation_descent_required",
    "bm_chain_functor_constructed",
    "definition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
RESIDUAL_COLUMNS = (
    "component_id",
    "symbol",
    "component_type",
    "measures",
    "vanishing_claimed",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_RESIDUALS = {
    "quotient_form": ("o_Q_form", "true"),
    "quotient_composition": ("o_Q_comp", "true"),
    "quotient_base_change": ("o_Q_bc", "true"),
    "quotient_thom_sebastiani": ("o_Q_TS", "true"),
    "quotient_flag": ("o_Q_flag", "true"),
    "quotient_bm": ("o_Q_BM", "true"),
    "quotient_theta": ("o_Q_theta", "true"),
    "quotient_transition": ("o_Q_tr", "true"),
}
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
    "composition_rows.csv": (
        "composition_id",
        "R_id",
        "pseudofunctor_id",
        "composition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "base_change_rows.csv": (
        "base_change_id",
        "R_id",
        "pseudofunctor_id",
        "base_change_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "thom_sebastiani_rows.csv": (
        "ts_id",
        "R_id",
        "pseudofunctor_id",
        "thom_sebastiani_defect_rank",
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
EXCLUSION_COLUMNS = (
    "exclusion_id",
    "R_id",
    "forbidden_model",
    "exclusion_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
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
REQUIRED_OBLIGATIONS = frozenset(
    {
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
        "quotient_first",
        "object_quotient_only",
        "composition_component_only",
        "base_change_component_only",
        "compact_support_pushforward_base_change_claim",
        "thom_sebastiani_component_only",
        "unreduced_bbdjs_ts_construction_claim",
        "bm_chain_functor_component_only",
        "theta_mu_component_only",
        "flag_coherence_component_only",
        "Q_E_R_transition_component_only",
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
        description="Check quotient-after-correspondence pseudofunctor definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition"),
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
        "fixture_name": "quotient_after_correspondence_pseudofunctor_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "definition_only": True,
        "quotient_after_correspondence_defined": True,
        "object_assignment_defined": True,
        "arrow_assignment_defined": True,
        "coefficient_descent_interface_defined": True,
        "residual_components_defined": True,
        "residual_component_count": 8,
        "composition_certification": True,
        "base_change_certification": True,
        "thom_sebastiani_certification": True,
        "flag_certification": True,
        "bm_chain_functor_certification": True,
        "theta_mu_certification": True,
        "quotient_first_exclusion_theorem": True,
        "transition_certification": True,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "object_assignment_rows.csv",
        "arrow_assignment_rows.csv",
        "coefficient_descent_interface_rows.csv",
        "residual_component_rows.csv",
        "quotient_first_exclusion_rows.csv",
        "bm_chain_functor_rows.csv",
        "theta_mu_rows.csv",
        "flag_coherence_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected quotient-pseudofunctor tables")
    expected_imports = {
        "certificates/hybrid/source_target_anchor_memory_definition",
        "certificates/hybrid/anchor_residual_definition",
        "certificates/hybrid/compact_support_exceptional_pushforward_model",
        "certificates/hybrid/quotient_after_correspondence_composition",
        "certificates/hybrid/quotient_after_correspondence_base_change",
        "certificates/hybrid/quotient_after_correspondence_thom_sebastiani",
        "certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion",
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected quotient-pseudofunctor imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    issues: list[str],
) -> dict[str, str] | None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return None
    row = table.rows[0]
    if row.get(expected_id_key) != expected_id:
        issues.append(f"{table_name} {expected_id_key}: expected {expected_id!r}, got {row.get(expected_id_key)!r}")
    if row.get("definition_defect_rank") != "0":
        issues.append(f"{table_name} definition_defect_rank must be zero")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    if "def:quotient-after-correspondence-pseudofunctor" not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to the row-246 definition")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    object_row = require_one_row(
        fixture,
        "object_assignment_rows.csv",
        OBJECT_COLUMNS,
        "object_assignment_id",
        "quotient_objects_R",
        issues,
    )
    if object_row and object_row.get("quotient_object_family") != "bar_Y_equals_stack_quotient_Y_slash_E":
        issues.append("object assignment does not use stack quotient notation")
    arrow_row = require_one_row(
        fixture,
        "arrow_assignment_rows.csv",
        ARROW_COLUMNS,
        "arrow_assignment_id",
        "quotient_arrows_R",
        issues,
    )
    if arrow_row and arrow_row.get("quotient_after_not_first") != "true":
        issues.append("arrow assignment must mark quotient_after_not_first true")
    coefficient_row = require_one_row(
        fixture,
        "coefficient_descent_interface_rows.csv",
        COEFFICIENT_COLUMNS,
        "interface_id",
        "coefficient_descent_interface_R",
        issues,
    )
    if coefficient_row and coefficient_row.get("bm_chain_functor_constructed") != "true":
        issues.append("coefficient interface must mark the row-251 BM chain functor as constructed")
    exclusion_table = load_csv(fixture / "quotient_first_exclusion_rows.csv", EXCLUSION_COLUMNS, issues)
    if len(exclusion_table.rows) != 1:
        issues.append("quotient_first_exclusion_rows.csv must contain exactly one row")
    else:
        exclusion_row = exclusion_table.rows[0]
        if exclusion_row.get("exclusion_id") != "quotient_first_exclusion_R":
            issues.append("quotient_first_exclusion_rows.csv exclusion_id must be quotient_first_exclusion_R")
        if exclusion_row.get("exclusion_defect_rank") != "0":
            issues.append("quotient_first_exclusion_rows.csv exclusion_defect_rank must be zero")
        if exclusion_row.get("check_status") != "verified":
            issues.append("quotient_first_exclusion_rows.csv row is not verified")
        if QFIRST_PROOF_LABEL not in exclusion_row.get("proof_reference", ""):
            issues.append("quotient_first_exclusion_rows.csv row does not point to the row-250 theorem")
    bm_table = load_csv(fixture / "bm_chain_functor_rows.csv", BM_COLUMNS, issues)
    if len(bm_table.rows) != 1:
        issues.append("bm_chain_functor_rows.csv must contain exactly one row")
    else:
        bm_row = bm_table.rows[0]
        if bm_row.get("bm_id") != "quotient_bm_chain_functor_R":
            issues.append("bm_chain_functor_rows.csv bm_id must be quotient_bm_chain_functor_R")
        if bm_row.get("Q_E_R_id") != "Q_E_R":
            issues.append("bm_chain_functor_rows.csv must name Q_E_R")
        if bm_row.get("bm_chain_defect_rank") != "0":
            issues.append("bm_chain_functor_rows.csv bm_chain_defect_rank must be zero")
        if bm_row.get("check_status") != "verified":
            issues.append("bm_chain_functor_rows.csv row is not verified")
        if BM_PROOF_LABEL not in bm_row.get("proof_reference", ""):
            issues.append("bm_chain_functor_rows.csv row does not point to the row-251 theorem")
    theta_table = load_csv(fixture / "theta_mu_rows.csv", THETA_COLUMNS, issues)
    if len(theta_table.rows) != 1:
        issues.append("theta_mu_rows.csv must contain exactly one row")
    else:
        theta_row = theta_table.rows[0]
        if theta_row.get("theta_id") != "quotient_theta_mu_R":
            issues.append("theta_mu_rows.csv theta_id must be quotient_theta_mu_R")
        if theta_row.get("theta_mu_defect_rank") != "0":
            issues.append("theta_mu_rows.csv theta_mu_defect_rank must be zero")
        if theta_row.get("check_status") != "verified":
            issues.append("theta_mu_rows.csv row is not verified")
        if THETA_PROOF_LABEL not in theta_row.get("proof_reference", ""):
            issues.append("theta_mu_rows.csv row does not point to the row-252 theorem")
    flag_table = load_csv(fixture / "flag_coherence_rows.csv", FLAG_COLUMNS, issues)
    if len(flag_table.rows) != 1:
        issues.append("flag_coherence_rows.csv must contain exactly one row")
    else:
        flag_row = flag_table.rows[0]
        if flag_row.get("flag_id") != "quotient_theta_associativity_flags_R":
            issues.append("flag_coherence_rows.csv flag_id must be quotient_theta_associativity_flags_R")
        if flag_row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("flag_coherence_rows.csv must name the quotient-after-correspondence pseudofunctor")
        if flag_row.get("flag_defect_rank") != "0":
            issues.append("flag_coherence_rows.csv flag_defect_rank must be zero")
        if flag_row.get("check_status") != "verified":
            issues.append("flag_coherence_rows.csv row is not verified")
        if ASSOC_PROOF_LABEL not in flag_row.get("proof_reference", ""):
            issues.append("flag_coherence_rows.csv row does not point to the row-253 theorem")
    transition_table = load_csv(fixture / "transition_rows.csv", TRANSITION_COLUMNS, issues)
    if len(transition_table.rows) != 1:
        issues.append("transition_rows.csv must contain exactly one row")
    else:
        transition_row = transition_table.rows[0]
        if transition_row.get("transition_id") != "Q_E_R_hn_transition_Rprime_R":
            issues.append("transition_rows.csv transition_id must be Q_E_R_hn_transition_Rprime_R")
        if transition_row.get("from_R") != "Rprime" or transition_row.get("to_R") != "R":
            issues.append("transition_rows.csv must record Rprime -> R")
        if transition_row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition_rows.csv must name the quotient-after-correspondence pseudofunctor")
        if transition_row.get("transition_defect_rank") != "0":
            issues.append("transition_rows.csv transition_defect_rank must be zero")
        if transition_row.get("check_status") != "verified":
            issues.append("transition_rows.csv row is not verified")
        if TRANSITION_PROOF_LABEL not in transition_row.get("proof_reference", ""):
            issues.append("transition_rows.csv row does not point to the row-256 theorem")


def check_residuals(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "residual_component_rows.csv", RESIDUAL_COLUMNS, issues)
    by_id = {row.get("component_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_RESIDUALS):
        missing = sorted(set(EXPECTED_RESIDUALS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_RESIDUALS))
        if missing:
            issues.append("missing residual rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected residual rows: " + ", ".join(extra))
    for component_id, (symbol, vanishing) in EXPECTED_RESIDUALS.items():
        row = by_id.get(component_id)
        if row is None:
            continue
        if row.get("symbol") != symbol:
            issues.append(f"{component_id} symbol: expected {symbol!r}, got {row.get('symbol')!r}")
        if row.get("vanishing_claimed") != vanishing:
            issues.append(
                f"{component_id} vanishing_claimed: expected {vanishing!r}, got {row.get('vanishing_claimed')!r}"
            )
        if row.get("check_status") != "verified":
            issues.append(f"{component_id} is not verified")
        proof_reference = row.get("proof_reference", "")
        if component_id == "quotient_composition":
            if COMPOSITION_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-247 composition theorem")
        elif component_id == "quotient_base_change":
            if BASE_CHANGE_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-248 base-change theorem")
        elif component_id == "quotient_thom_sebastiani":
            if TS_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-249 Thom--Sebastiani theorem")
        elif component_id == "quotient_bm":
            if BM_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-251 BM chain functor theorem")
        elif component_id == "quotient_theta":
            if THETA_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-252 theta_mu theorem")
        elif component_id == "quotient_flag":
            if ASSOC_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-253 associativity theorem")
        elif component_id == "quotient_transition":
            if TRANSITION_PROOF_LABEL not in proof_reference:
                issues.append(f"{component_id} does not point to the row-256 transition theorem")
        elif "def:quotient-after-correspondence-pseudofunctor" not in proof_reference:
            issues.append(f"{component_id} does not point to the row-246 definition")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this definition packet")


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
        "source_target_anchor_memory_definition": "SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED",
        "anchor_residual_definition": "ANCHOR_RESIDUAL_DEFINITION_VERIFIED",
        "compact_support_exceptional_pushforward_model": "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED",
        "quotient_after_correspondence_composition": "QUOTIENT_AFTER_CORRESPONDENCE_COMPOSITION_VERIFIED",
        "quotient_after_correspondence_base_change": "QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        "quotient_after_correspondence_thom_sebastiani": "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED",
        "quotient_after_correspondence_quotient_first_exclusion": "QUOTIENT_AFTER_CORRESPONDENCE_QUOTIENT_FIRST_EXCLUSION_VERIFIED",
        "quotient_after_correspondence_bm_chain_functor": "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED",
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
    check_residuals(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
