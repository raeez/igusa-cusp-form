#!/usr/bin/env python3
"""Verify theta_mu associativity compatibility for quotient-after-correspondence."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_theta_mu_associativity.v1"
EXPECTED_KIND = "quotient_after_correspondence_theta_mu_associativity"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-associativity"
COPRODUCT_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-coproduct"
PRIMITIVE_PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-primitives"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

WORDS = ("LLL", "LLW", "LWL", "WLL", "LWW", "WLW", "WWL", "WWW")
ASSOCIATIVITY_COLUMNS = (
    "associativity_id",
    "R_id",
    "word",
    "flag_stack_id",
    "left_composite_id",
    "right_composite_id",
    "left_theta_id",
    "right_theta_id",
    "associativity_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
NATURALITY_COLUMNS = (
    "square_id",
    "R_id",
    "word",
    "source_associator",
    "reduced_associator",
    "left_theta",
    "right_theta",
    "square_defect_rank",
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
        "theta_associativity_component_only",
        "theta_mu_component_only",
        "flag_stack_only",
        "word_associativity_only",
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
        description="Check quotient theta_mu associativity compatibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(
            "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity"
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
        "fixture_name": "quotient_after_correspondence_theta_mu_associativity",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "theta_mu_associativity_compatible": True,
        "quotient_after_correspondence_imported": True,
        "theta_mu_comparison_imported": True,
        "eight_word_flag_atlas_imported": True,
        "word_associativity_packets_imported": True,
        "word_count": 8,
        "flag_certification": True,
        "associativity_certification": True,
        "flag_defect_rank": 0,
        "associativity_defect_rank": 0,
        "coproduct_certification": True,
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
        "associativity_rows.csv",
        "naturality_square_rows.csv",
        "flag_coherence_rows.csv",
        "coproduct_rows.csv",
        "primitive_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected theta associativity tables")
    expected_imports = {
        "certificates/hybrid/eight_word_two_step_flag_stacks",
        "certificates/hybrid/lll_associativity",
        "certificates/hybrid/llw_associativity",
        "certificates/hybrid/lwl_associativity",
        "certificates/hybrid/wll_associativity",
        "certificates/hybrid/lww_associativity",
        "certificates/hybrid/wlw_associativity",
        "certificates/hybrid/wwl_associativity",
        "certificates/hybrid/www_associativity",
        "certificates/hybrid/quotient_after_correspondence_composition",
        "certificates/hybrid/quotient_after_correspondence_base_change",
        "certificates/hybrid/quotient_after_correspondence_thom_sebastiani",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_primitives",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected theta associativity imports")


def check_word_rows(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    word_key: str,
    defect_key: str,
    issues: list[str],
) -> list[dict[str, str]]:
    table = load_csv(fixture / table_name, columns, issues)
    by_word = {row.get(word_key, ""): row for row in table.rows}
    missing = sorted(set(WORDS) - set(by_word))
    extra = sorted(set(by_word) - set(WORDS))
    if missing:
        issues.append(f"{table_name} missing word rows: " + ", ".join(missing))
    if extra:
        issues.append(f"{table_name} unexpected word rows: " + ", ".join(extra))
    for word in WORDS:
        row = by_word.get(word)
        if row is None:
            continue
        if row.get("R_id") != "R":
            issues.append(f"{table_name} {word} must have R_id R")
        if row.get(defect_key) != "0":
            issues.append(f"{table_name} {word} {defect_key} must be zero")
        if row.get("check_status") != "verified":
            issues.append(f"{table_name} {word} row is not verified")
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append(f"{table_name} {word} does not point to {PROOF_LABEL}")
    return table.rows


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    assoc_rows = check_word_rows(
        fixture,
        "associativity_rows.csv",
        ASSOCIATIVITY_COLUMNS,
        "word",
        "associativity_defect_rank",
        issues,
    )
    for row in assoc_rows:
        word = row.get("word", "")
        if word in WORDS:
            expected_flag = f"F2_{word}_R"
            if row.get("flag_stack_id") != expected_flag:
                issues.append(f"{word} flag_stack_id: expected {expected_flag!r}")
            if row.get("left_theta_id") != f"Theta_L_{word}":
                issues.append(f"{word} left_theta_id must be Theta_L_{word}")
            if row.get("right_theta_id") != f"Theta_R_{word}":
                issues.append(f"{word} right_theta_id must be Theta_R_{word}")

    square_rows = check_word_rows(
        fixture,
        "naturality_square_rows.csv",
        NATURALITY_COLUMNS,
        "word",
        "square_defect_rank",
        issues,
    )
    for row in square_rows:
        word = row.get("word", "")
        if word in WORDS:
            if row.get("source_associator") != f"a_{word}":
                issues.append(f"{word} source_associator must be a_{word}")
            if row.get("reduced_associator") != f"bar_a_{word}":
                issues.append(f"{word} reduced_associator must be bar_a_{word}")

    flag_table = load_csv(fixture / "flag_coherence_rows.csv", FLAG_COLUMNS, issues)
    if len(flag_table.rows) != 1:
        issues.append("flag_coherence_rows.csv must contain exactly one row")
    else:
        row = flag_table.rows[0]
        if row.get("flag_id") != "quotient_theta_associativity_flags_R":
            issues.append("flag row must be quotient_theta_associativity_flags_R")
        if row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("flag row must name the quotient-after-correspondence pseudofunctor")
        if row.get("flag_defect_rank") != "0":
            issues.append("flag row defect rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("flag row is not verified")
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("flag row does not point to the row-253 theorem")
    coproduct_table = load_csv(fixture / "coproduct_rows.csv", COPRODUCT_COLUMNS, issues)
    if len(coproduct_table.rows) != 1:
        issues.append("coproduct_rows.csv must contain exactly one row")
    else:
        row = coproduct_table.rows[0]
        if row.get("coproduct_id") != "theta_mu_coproduct_R":
            issues.append("coproduct row must be theta_mu_coproduct_R")
        if row.get("theta_id") != "quotient_theta_mu_R":
            issues.append("coproduct row must name quotient_theta_mu_R")
        if row.get("coproduct_family") != "finite_hall_collision_coproduct_rows":
            issues.append("coproduct row must name finite_hall_collision_coproduct_rows")
        if row.get("coproduct_defect_rank") != "0":
            issues.append("coproduct row defect rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("coproduct row is not verified")
        if COPRODUCT_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("coproduct row does not point to the row-254 theorem")
    primitive_table = load_csv(fixture / "primitive_rows.csv", PRIMITIVE_COLUMNS, issues)
    if len(primitive_table.rows) != 1:
        issues.append("primitive_rows.csv must contain exactly one row")
    else:
        row = primitive_table.rows[0]
        if row.get("primitive_id") != "theta_mu_primitives_R":
            issues.append("primitive row must be theta_mu_primitives_R")
        if row.get("theta_id") != "quotient_theta_mu_R":
            issues.append("primitive row must name quotient_theta_mu_R")
        if row.get("primitive_projection") != "primitive_projection_P_R":
            issues.append("primitive row must name primitive_projection_P_R")
        if row.get("primitive_defect_rank") != "0":
            issues.append("primitive row defect rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("primitive row is not verified")
        if PRIMITIVE_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("primitive row does not point to the row-255 theorem")
    transition_table = load_csv(fixture / "transition_rows.csv", TRANSITION_COLUMNS, issues)
    if len(transition_table.rows) != 1:
        issues.append("transition_rows.csv must contain exactly one row")
    else:
        row = transition_table.rows[0]
        if row.get("transition_id") != "Q_E_R_hn_transition_Rprime_R":
            issues.append("transition row must be Q_E_R_hn_transition_Rprime_R")
        if row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition row must name quotient_after_correspondence_pseudofunctor")
        if row.get("transition_defect_rank") != "0":
            issues.append("transition row defect rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("transition row is not verified")
        if TRANSITION_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("transition row does not point to the row-256 theorem")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the theta associativity packet")


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
        "eight_word_two_step_flag_stacks": "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED",
        "lll_associativity": "LLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "llw_associativity": "LLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lwl_associativity": "LWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wll_associativity": "WLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "lww_associativity": "LWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wlw_associativity": "WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "wwl_associativity": "WWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "www_associativity": "WWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED",
        "quotient_after_correspondence_composition": "QUOTIENT_AFTER_CORRESPONDENCE_COMPOSITION_VERIFIED",
        "quotient_after_correspondence_base_change": "QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        "quotient_after_correspondence_thom_sebastiani": "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED",
        "quotient_after_correspondence_theta_mu_comparison": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED",
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
        print("QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
