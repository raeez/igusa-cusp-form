#!/usr/bin/env python3
"""Verify the D0-HN obstruction ledger.

This verifier certifies only the absence ledger for the finite D0-HN
packet.  It checks that the D0 fixture is still the empty blocked
scaffold, that its required tables have no rows, and that every missing
D0-HN artifact is recorded in blocked_obligations.csv.

It does not prove the D0-degeneration criterion.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "D0_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_D0_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "degeneration_families.csv",
    "retained_substacks.csv",
    "hn_transitions.csv",
    "derived_enhancements.csv",
    "semiregularity_cosections.csv",
    "vanishing_cycles.csv",
    "orientation_specializations.csv",
    "pfaffian_integration.csv",
    "ml_exactness.csv",
    "scalar_firewall.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "rank_or_status_payload",
    "why_required",
    "d0_status",
    "proof_reference",
    "check_status",
    "notes",
)


@dataclass(frozen=True)
class RequiredObligation:
    obligation_id: str
    lane: str
    required_table: str
    required_row_type: str


REQUIRED_OBLIGATIONS: tuple[RequiredObligation, ...] = (
    RequiredObligation("flat_degen_family", "degeneration", "degeneration_families.csv", "flat_family"),
    RequiredObligation("contains_d0_sector", "degeneration", "degeneration_families.csv", "d0_special_fiber"),
    RequiredObligation("substack_object", "retained_substacks", "retained_substacks.csv", "object"),
    RequiredObligation("substack_extension", "retained_substacks", "retained_substacks.csv", "extension"),
    RequiredObligation("substack_mixed", "retained_substacks", "retained_substacks.csv", "mixed"),
    RequiredObligation("substack_wrapped", "retained_substacks", "retained_substacks.csv", "wrapped"),
    RequiredObligation("substack_two_step_flag", "retained_substacks", "retained_substacks.csv", "two_step_flag"),
    RequiredObligation("hn_transition_proper_closed", "hn_transition", "hn_transitions.csv", "proper_or_closed"),
    RequiredObligation("hn_transition_d0_fiber", "hn_transition", "hn_transitions.csv", "preserves_d0_fiber"),
    RequiredObligation("hn_transition_composition", "hn_transition", "hn_transitions.csv", "composition_law"),
    RequiredObligation("derived_quasi_smooth", "derived_enhancement", "derived_enhancements.csv", "quasi_smooth"),
    RequiredObligation("derived_shifted_symplectic", "derived_enhancement", "derived_enhancements.csv", "shifted_symplectic"),
    RequiredObligation("derived_dcritical", "derived_enhancement", "derived_enhancements.csv", "dcritical_truncation"),
    RequiredObligation("derived_perfect_obstruction", "derived_enhancement", "derived_enhancements.csv", "perfect_obstruction_theory"),
    RequiredObligation("cosection_surjective", "semiregularity", "semiregularity_cosections.csv", "surjectivity"),
    RequiredObligation("cosection_d0_compatible", "semiregularity", "semiregularity_cosections.csv", "d0_compatibility"),
    RequiredObligation("cosection_extension_additive", "semiregularity", "semiregularity_cosections.csv", "extension_additivity"),
    RequiredObligation("vc_specialization", "vanishing_cycles", "vanishing_cycles.csv", "specialization_cone"),
    RequiredObligation("vc_transition", "vanishing_cycles", "vanishing_cycles.csv", "transition_defect"),
    RequiredObligation("orientation_square_root_specialization", "orientation", "orientation_specializations.csv", "square_root"),
    RequiredObligation("orientation_ts_specialization", "orientation", "orientation_specializations.csv", "ts_multiplicativity"),
    RequiredObligation("orientation_specialization_cone", "orientation", "orientation_specializations.csv", "specialization_cone"),
    RequiredObligation("orientation_transition", "orientation", "orientation_specializations.csv", "transition_defect"),
    RequiredObligation("pfaffian_line_specialization", "pfaffian_integration", "pfaffian_integration.csv", "pfaffian_line"),
    RequiredObligation("pfaffian_section_specialization", "pfaffian_integration", "pfaffian_integration.csv", "pfaffian_section"),
    RequiredObligation("protected_integration_specialization", "pfaffian_integration", "pfaffian_integration.csv", "protected_integration"),
    RequiredObligation("compact_support_specialization", "pfaffian_integration", "pfaffian_integration.csv", "compact_support_operation"),
    RequiredObligation("hall_operation_specialization", "pfaffian_integration", "pfaffian_integration.csv", "hall_operation"),
    RequiredObligation("ml_vanishing_cycles", "ml_exactness", "ml_exactness.csv", "vanishing_cycles"),
    RequiredObligation("ml_orientation_gerbes", "ml_exactness", "ml_exactness.csv", "orientation_gerbes"),
    RequiredObligation("ml_pfaffian_lines", "ml_exactness", "ml_exactness.csv", "pfaffian_lines"),
    RequiredObligation("ml_compact_support", "ml_exactness", "ml_exactness.csv", "compact_support_operations"),
    RequiredObligation("ml_hall_product", "ml_exactness", "ml_exactness.csv", "hall_product"),
    RequiredObligation("ml_hall_coproduct", "ml_exactness", "ml_exactness.csv", "hall_coproduct"),
    RequiredObligation("ml_finite_stage_morphisms", "ml_exactness", "ml_exactness.csv", "finite_stage_morphisms"),
    RequiredObligation("firewall_hilbert_scheme_scalar", "scalar_firewall", "scalar_firewall.csv", "hilbert_scheme_scalar_specialization"),
    RequiredObligation("firewall_k3_scalar_test", "scalar_firewall", "scalar_firewall.csv", "k3_scalar_test"),
    RequiredObligation("firewall_scalar_trace", "scalar_firewall", "scalar_firewall.csv", "scalar_trace"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the D0-HN obstruction ledger.")
    parser.add_argument("--fixture", required=True, type=Path, help="D0 fixture directory")
    parser.add_argument("--check", action="store_true", help="explicit check-only mode")
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


def load_manifest(fixture: Path, issues: list[str]) -> dict[str, object]:
    path = fixture / MANIFEST_NAME
    if not path.is_file():
        issues.append(f"missing manifest: {path}")
        return {}
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"manifest is not valid JSON: {exc}")
        return {}
    if not isinstance(manifest, dict):
        issues.append("manifest root is not an object")
        return {}
    return manifest


def check_manifest(manifest: dict[str, object], issues: list[str]) -> None:
    if manifest.get("d0_kind") != EXPECTED_D0_KIND:
        issues.append(
            "D0 manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("D0 manifest does not mark empty_blocked=true")
    if manifest.get("hilbert_scheme_scalar_only") is True:
        issues.append("D0 manifest marks Hilbert-scheme-scalar-only data")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing D0 table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"D0 table {table_name} now has data rows; "
                "the obstruction ledger must be retired or narrowed"
            )


def load_obligations(fixture: Path, issues: list[str]) -> list[dict[str, str]]:
    path = fixture / OBLIGATION_FILE
    if not path.is_file():
        issues.append(f"missing obstruction ledger: {path}")
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != OBLIGATION_COLUMNS:
            issues.append(
                "blocked_obligations.csv header mismatch; expected "
                + ",".join(OBLIGATION_COLUMNS)
            )
        return nonempty_rows(reader)


def check_obligations(rows: list[dict[str, str]], issues: list[str]) -> None:
    required_by_id = {entry.obligation_id: entry for entry in REQUIRED_OBLIGATIONS}
    actual_by_id = {row.get("obligation_id", ""): row for row in rows}
    missing = sorted(set(required_by_id) - set(actual_by_id))
    extra = sorted(set(actual_by_id) - set(required_by_id))
    if missing:
        issues.append("missing obligation rows: " + ",".join(missing))
    if extra:
        issues.append("unexpected obligation rows: " + ",".join(extra))

    for row_number, row in enumerate(rows, start=2):
        obligation_id = row.get("obligation_id", "")
        required = required_by_id.get(obligation_id)
        if required is None:
            continue
        for column in OBLIGATION_COLUMNS:
            if not row.get(column, ""):
                issues.append(f"blocked_obligations.csv:{row_number} missing {column}")
        if row.get("lane") != required.lane:
            issues.append(
                f"{obligation_id}: lane {row.get('lane')!r} != {required.lane!r}"
            )
        if row.get("required_table") != required.required_table:
            issues.append(
                f"{obligation_id}: table {row.get('required_table')!r} "
                f"!= {required.required_table!r}"
            )
        if row.get("required_row_type") != required.required_row_type:
            issues.append(
                f"{obligation_id}: row type {row.get('required_row_type')!r} "
                f"!= {required.required_row_type!r}"
            )
        if row.get("d0_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: d0_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"D0 fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "D0_OBSTRUCTION_LEDGER_FAILED"
    print("D0 obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("d0_certification: false")
    print("mathematical_certification: false")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    ok, issues = run(args.fixture)
    print_report(args.fixture, ok, issues)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
