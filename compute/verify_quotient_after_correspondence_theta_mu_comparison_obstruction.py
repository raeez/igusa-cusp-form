#!/usr/bin/env python3
"""Verify the quotient-after-correspondence theta_mu comparison packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_theta_mu_comparison.v1"
EXPECTED_KIND = "quotient_after_correspondence_theta_mu_comparison"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-comparison"
ASSOC_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-associativity"
COPRODUCT_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-coproduct"
PRIMITIVE_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-primitives"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

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
OPERATION_DESCENT_COLUMNS = (
    "operation_descent_id",
    "R_id",
    "operation_family",
    "input_descent",
    "middle_descent",
    "target_descent",
    "external_product_descent",
    "descent_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
PULLBACK_TS_COLUMNS = (
    "pullback_ts_id",
    "R_id",
    "source_pullback_comparison",
    "thom_sebastiani_comparison",
    "extension_coefficient",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
PUSHFORWARD_DESCENT_COLUMNS = (
    "pushforward_descent_id",
    "R_id",
    "target_map",
    "source_coefficient",
    "reduced_pushforward",
    "quotient_pushforward_descent",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
BM_COMPARISON_COLUMNS = (
    "comparison_id",
    "R_id",
    "Q_E_R_id",
    "source_chain",
    "target_chain",
    "chain_isomorphism",
    "comparison_defect_rank",
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
ASSOCIATIVITY_COLUMNS = (
    "associativity_id",
    "R_id",
    "theta_id",
    "flag_family",
    "associativity_defect_rank",
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
        "theta_mu_component_only",
        "bm_chain_functor_component_only",
        "compact_support_pushforward_base_change_claim",
        "theta_associativity_component_only",
        "theta_coproduct_component_only",
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
        description="Check quotient-after-correspondence theta_mu comparison packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/quotient_after_correspondence_theta_mu_comparison"),
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
        "fixture_name": "quotient_after_correspondence_theta_mu_comparison",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "theta_mu_comparison_constructed": True,
        "quotient_after_correspondence_imported": True,
        "base_change_packet_imported": True,
        "thom_sebastiani_packet_imported": True,
        "bm_chain_functor_imported": True,
        "compact_support_model_imported": True,
        "quotient_first_exclusion_imported": True,
        "external_product_descent_required": True,
        "compact_support_pushforward_descent_required": True,
        "operation_comparison_constructed": True,
        "theta_mu_defect_rank": 0,
        "associativity_certification": True,
        "coproduct_certification": True,
        "primitive_certification": True,
        "flag_certification": True,
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
        "theta_mu_rows.csv",
        "operation_descent_rows.csv",
        "pullback_ts_rows.csv",
        "pushforward_descent_rows.csv",
        "bm_chain_comparison_rows.csv",
        "associativity_rows.csv",
        "coproduct_rows.csv",
        "primitive_rows.csv",
        "flag_coherence_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected theta_mu comparison tables")
    expected_imports = {
        "certificates/hybrid/compact_support_exceptional_pushforward_model",
        "certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition",
        "certificates/hybrid/quotient_after_correspondence_base_change",
        "certificates/hybrid/quotient_after_correspondence_thom_sebastiani",
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
        "certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_primitives",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected theta_mu comparison imports")


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
    theta = require_one_row(
        fixture,
        "theta_mu_rows.csv",
        THETA_COLUMNS,
        "theta_id",
        "quotient_theta_mu_R",
        "theta_mu_defect_rank",
        issues,
    )
    if theta and theta.get("operation_id") != "Q_E_R_q_bang_TS_p_star_vs_bar_q_bang_bar_TS_bar_p_star":
        issues.append("theta_mu row must name the reduced pull-push comparison")

    operation = require_one_row(
        fixture,
        "operation_descent_rows.csv",
        OPERATION_DESCENT_COLUMNS,
        "operation_descent_id",
        "operation_descent_R",
        "descent_defect_rank",
        issues,
    )
    if operation and operation.get("external_product_descent") != "boxtimes_Kbar_i_descends_to_product_quotient":
        issues.append("operation descent row must record external product descent")

    pullback = require_one_row(
        fixture,
        "pullback_ts_rows.csv",
        PULLBACK_TS_COLUMNS,
        "pullback_ts_id",
        "pullback_ts_R",
        "defect_rank",
        issues,
    )
    if pullback and pullback.get("extension_coefficient") != "bar_L_e_equals_bar_TS_bar_p_star_boxtimes_Kbar_i":
        issues.append("pullback/TS row must name the reduced extension coefficient")

    pushforward = require_one_row(
        fixture,
        "pushforward_descent_rows.csv",
        PUSHFORWARD_DESCENT_COLUMNS,
        "pushforward_descent_id",
        "pushforward_descent_R",
        "defect_rank",
        issues,
    )
    if pushforward and "delta_q_e" not in pushforward.get("quotient_pushforward_descent", ""):
        issues.append("pushforward descent row must name delta_q_e")

    bm = require_one_row(
        fixture,
        "bm_chain_comparison_rows.csv",
        BM_COMPARISON_COLUMNS,
        "comparison_id",
        "bm_theta_comparison_R",
        "comparison_defect_rank",
        issues,
    )
    if bm:
        if bm.get("Q_E_R_id") != "Q_E_R":
            issues.append("BM comparison row must name Q_E_R")
        if bm.get("chain_isomorphism") != "theta_Q_mu_R":
            issues.append("BM comparison row must name theta_Q_mu_R")
    assoc = require_one_row(
        fixture,
        "associativity_rows.csv",
        ASSOCIATIVITY_COLUMNS,
        "associativity_id",
        "theta_mu_associativity_all_words_R",
        "associativity_defect_rank",
        issues,
        ASSOC_PROOF_LABEL,
    )
    if assoc:
        if assoc.get("theta_id") != "quotient_theta_mu_R":
            issues.append("associativity row must name quotient_theta_mu_R")
        if assoc.get("flag_family") != "eight_two_step_flag_words":
            issues.append("associativity row must name the eight two-step flag words")
        if ASSOC_PROOF_LABEL not in assoc.get("proof_reference", ""):
            issues.append("associativity row does not point to the row-253 theorem")
    flag = require_one_row(
        fixture,
        "flag_coherence_rows.csv",
        FLAG_COLUMNS,
        "flag_id",
        "quotient_theta_associativity_flags_R",
        "flag_defect_rank",
        issues,
        ASSOC_PROOF_LABEL,
    )
    if flag:
        if flag.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("flag row must name the quotient-after-correspondence pseudofunctor")
        if ASSOC_PROOF_LABEL not in flag.get("proof_reference", ""):
            issues.append("flag row does not point to the row-253 theorem")
    coproduct = require_one_row(
        fixture,
        "coproduct_rows.csv",
        COPRODUCT_COLUMNS,
        "coproduct_id",
        "theta_mu_coproduct_R",
        "coproduct_defect_rank",
        issues,
        COPRODUCT_PROOF_LABEL,
    )
    if coproduct:
        if coproduct.get("theta_id") != "quotient_theta_mu_R":
            issues.append("coproduct row must name quotient_theta_mu_R")
        if coproduct.get("coproduct_family") != "finite_hall_collision_coproduct_rows":
            issues.append("coproduct row must name the finite Hall collision coproduct rows")
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
    if transition:
        if transition.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition row must name the quotient-after-correspondence pseudofunctor")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the theta_mu comparison packet")


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
        "compact_support_exceptional_pushforward_model": "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED",
        "quotient_after_correspondence_pseudofunctor_definition": "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED",
        "quotient_after_correspondence_base_change": "QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        "quotient_after_correspondence_thom_sebastiani": "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED",
        "quotient_after_correspondence_bm_chain_functor": "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED",
        "quotient_after_correspondence_quotient_first_exclusion": "QUOTIENT_AFTER_CORRESPONDENCE_QUOTIENT_FIRST_EXCLUSION_VERIFIED",
        "quotient_after_correspondence_theta_mu_associativity": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED",
        "quotient_after_correspondence_theta_mu_coproduct": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COPRODUCT_VERIFIED",
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
        print("QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
