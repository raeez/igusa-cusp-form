#!/usr/bin/env python3
"""Verify the quotient-after-correspondence base-change packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_base_change.v1"
EXPECTED_KIND = "quotient_after_correspondence_base_change"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-preserves-base-change"
QFIRST_PROOF_LABEL = "prop:quotient-after-correspondence-excludes-quotient-first"
BM_PROOF_LABEL = "prop:quotient-after-correspondence-borel-moore-chain-functor"
THETA_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-comparison"
ASSOC_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-associativity"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

BASE_CHANGE_COLUMNS = (
    "base_change_id",
    "R_id",
    "square_family",
    "unreduced_square",
    "reduced_square",
    "comparison_2_isomorphism",
    "base_change_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
CARTESIAN_COLUMNS = (
    "equivalence_id",
    "R_id",
    "unreduced_cartesian_square",
    "quotient_fibre_product",
    "stack_equivalence",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
COMPACT_SUPPORT_COLUMNS = (
    "square_id",
    "R_id",
    "square_type",
    "unreduced_square",
    "quotient_square",
    "cartesian_after_quotient",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_COMPACT_SUPPORT_SQUARES = {
    "source_square_R": "source",
    "target_square_R": "target",
    "open_square_R": "open",
    "compactified_square_R": "compactified",
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
        "base_change_component_only",
        "compact_support_pushforward_base_change_claim",
        "coefficient_pullback_claim",
        "projection_formula_claim",
        "quotient_first",
        "thom_sebastiani_from_base_change",
        "flag_coherence_component_only",
        "bm_chain_functor_component_only",
        "theta_mu_component_only",
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
        description="Check quotient-after-correspondence base-change packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/quotient_after_correspondence_base_change"),
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
        "fixture_name": "quotient_after_correspondence_base_change",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "base_change_preservation_proved": True,
        "quotient_after_correspondence_imported": True,
        "stack_quotient_cartesian_square_equivalence": True,
        "retained_compact_support_squares_preserved": True,
        "base_change_defect_rank": 0,
        "compact_support_pushforward_base_change": False,
        "coefficient_pullback_certification": False,
        "projection_formula_certification": False,
        "thom_sebastiani_certification": False,
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
        "base_change_rows.csv",
        "cartesian_square_equivalence_rows.csv",
        "compact_support_square_rows.csv",
        "quotient_first_exclusion_rows.csv",
        "bm_chain_functor_rows.csv",
        "theta_mu_rows.csv",
        "flag_coherence_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected base-change packet tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition",
        "certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion",
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected base-change packet imports")


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
        issues.append(f"{table_name} {expected_id_key}: expected {expected_id!r}, got {row.get(expected_id_key)!r}")
    if row.get(defect_key) != "0":
        issues.append(f"{table_name} {defect_key} must be zero")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {PROOF_LABEL}")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    base_change = require_one_row(
        fixture,
        "base_change_rows.csv",
        BASE_CHANGE_COLUMNS,
        "base_change_id",
        "quotient_base_change_cartesian_squares_R",
        "base_change_defect_rank",
        issues,
    )
    if base_change and base_change.get("comparison_2_isomorphism") != "Beta_square_R":
        issues.append("base-change row must name Beta_square_R as the comparison")
    cartesian = require_one_row(
        fixture,
        "cartesian_square_equivalence_rows.csv",
        CARTESIAN_COLUMNS,
        "equivalence_id",
        "quotient_cartesian_square_equivalence_R",
        "defect_rank",
        issues,
    )
    if cartesian and "equals" not in cartesian.get("stack_equivalence", ""):
        issues.append("cartesian square row must record the quotient-stack equivalence")
    compact_support = load_csv(
        fixture / "compact_support_square_rows.csv",
        COMPACT_SUPPORT_COLUMNS,
        issues,
    )
    by_id = {row.get("square_id", ""): row for row in compact_support.rows}
    missing = sorted(set(EXPECTED_COMPACT_SUPPORT_SQUARES) - set(by_id))
    extra = sorted(set(by_id) - set(EXPECTED_COMPACT_SUPPORT_SQUARES))
    if missing:
        issues.append("missing compact-support square rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected compact-support square rows: " + ", ".join(extra))
    for square_id, square_type in EXPECTED_COMPACT_SUPPORT_SQUARES.items():
        row = by_id.get(square_id)
        if row is None:
            continue
        if row.get("square_type") != square_type:
            issues.append(f"{square_id} square_type: expected {square_type!r}, got {row.get('square_type')!r}")
        if row.get("cartesian_after_quotient") != "true":
            issues.append(f"{square_id} must be cartesian after quotient")
        if row.get("defect_rank") != "0":
            issues.append(f"{square_id} defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append(f"{square_id} is not verified")
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append(f"{square_id} does not point to {PROOF_LABEL}")
    exclusion = load_csv(fixture / "quotient_first_exclusion_rows.csv", EXCLUSION_COLUMNS, issues)
    if len(exclusion.rows) != 1:
        issues.append("quotient_first_exclusion_rows.csv must contain exactly one row")
    else:
        row = exclusion.rows[0]
        if row.get("exclusion_id") != "quotient_first_exclusion_R":
            issues.append("quotient_first_exclusion_rows.csv exclusion_id must be quotient_first_exclusion_R")
        if row.get("exclusion_defect_rank") != "0":
            issues.append("quotient_first_exclusion_rows.csv exclusion_defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("quotient_first_exclusion_rows.csv row is not verified")
        if QFIRST_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("quotient_first_exclusion_rows.csv row does not point to the row-250 theorem")
    bm = load_csv(fixture / "bm_chain_functor_rows.csv", BM_COLUMNS, issues)
    if len(bm.rows) != 1:
        issues.append("bm_chain_functor_rows.csv must contain exactly one row")
    else:
        row = bm.rows[0]
        if row.get("bm_id") != "quotient_bm_chain_functor_R":
            issues.append("bm_chain_functor_rows.csv bm_id must be quotient_bm_chain_functor_R")
        if row.get("bm_chain_defect_rank") != "0":
            issues.append("bm_chain_functor_rows.csv bm_chain_defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("bm_chain_functor_rows.csv row is not verified")
        if BM_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("bm_chain_functor_rows.csv row does not point to the row-251 theorem")
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
            issues.append(f"{table_name} must remain empty in the base-change packet")


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


def check_import_status(fixture: Path, issues: list[str]) -> None:
    repo_root = fixture.parents[2]
    expected_hybrid_statuses = {
        "quotient_after_correspondence_pseudofunctor_definition": "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED",
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
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_status(fixture, issues)
    if issues:
        print("QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
