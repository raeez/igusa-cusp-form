#!/usr/bin/env python3
"""Verify the finite Pfaffian obstruction ledger.

This verifier certifies only the absence ledger for the finite
geometric Pfaffian packet.  It checks that the Pfaffian fixture is still
the empty blocked scaffold, that its required tables have no rows, and
that every missing P_fin artifact is recorded in blocked_obligations.csv.

It does not prove the Pfaffian--Dirac theorem.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PFAFFIAN_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_PFIN_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "strata.csv",
    "skew_complexes.csv",
    "pfaffian_lines.csv",
    "pfaffian_sections.csv",
    "wall_charts.csv",
    "automorphic_comparisons.csv",
    "transitions.csv",
    "scalar_firewall.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "rank_or_scalar_payload",
    "why_required",
    "pfaffian_status",
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
    RequiredObligation("retained_strata", "strata", "strata.csv", "retained_stratum"),
    RequiredObligation("skew_perfect_complex", "skew_complex", "skew_complexes.csv", "skew_self_dual_complex"),
    RequiredObligation("skew_obstruction_theory", "skew_complex", "skew_complexes.csv", "obstruction_theory"),
    RequiredObligation("skew_quotient_compatibility", "skew_complex", "skew_complexes.csv", "quotient_compatibility"),
    RequiredObligation("pfaffian_line", "pfaffian_line", "pfaffian_lines.csv", "determinant_line"),
    RequiredObligation("pfaffian_square", "pfaffian_line", "pfaffian_lines.csv", "square_isomorphism"),
    RequiredObligation("pfaffian_orientation", "pfaffian_line", "pfaffian_lines.csv", "orientation_id"),
    RequiredObligation("section_active_support", "pfaffian_section", "pfaffian_sections.csv", "active_support"),
    RequiredObligation("section_parity_ranks", "pfaffian_section", "pfaffian_sections.csv", "even_odd_ranks"),
    RequiredObligation("section_borcherds_exponent", "pfaffian_section", "pfaffian_sections.csv", "borcherds_exponent"),
    RequiredObligation("section_skew_block", "pfaffian_section", "pfaffian_sections.csv", "skew_block"),
    RequiredObligation("wall_normal_rank", "wall_chart", "wall_charts.csv", "normal_rank"),
    RequiredObligation("wall_divisor_order", "wall_chart", "wall_charts.csv", "divisor_order"),
    RequiredObligation("wall_type_i_exclusion", "wall_chart", "wall_charts.csv", "type_i_excluded"),
    RequiredObligation("wall_reflection_unit", "wall_chart", "wall_charts.csv", "reflection_unit_invariant"),
    RequiredObligation("wall_sign_value", "wall_chart", "wall_charts.csv", "sign_value"),
    RequiredObligation("automorphic_line", "automorphic_comparison", "automorphic_comparisons.csv", "automorphic_line"),
    RequiredObligation("automorphic_leading_coefficient", "automorphic_comparison", "automorphic_comparisons.csv", "leading_coefficient"),
    RequiredObligation("automorphic_weight", "automorphic_comparison", "automorphic_comparisons.csv", "weight"),
    RequiredObligation("automorphic_character", "automorphic_comparison", "automorphic_comparisons.csv", "character"),
    RequiredObligation("automorphic_square_compatibility", "automorphic_comparison", "automorphic_comparisons.csv", "square_compatibility"),
    RequiredObligation("transition_line", "transition", "transitions.csv", "line_transition"),
    RequiredObligation("transition_section", "transition", "transitions.csv", "section_transition"),
    RequiredObligation("transition_closed_image", "transition", "transitions.csv", "closed_image"),
    RequiredObligation("transition_ml", "transition", "transitions.csv", "mittag_leffler"),
    RequiredObligation("firewall_scalar_product", "scalar_firewall", "scalar_firewall.csv", "scalar_borcherds_product"),
    RequiredObligation("firewall_squared_determinant", "scalar_firewall", "scalar_firewall.csv", "squared_determinant"),
    RequiredObligation("firewall_op_scalar_trace", "scalar_firewall", "scalar_firewall.csv", "op_scalar_trace"),
    RequiredObligation("firewall_exponent_table", "scalar_firewall", "scalar_firewall.csv", "exponent_table"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the finite Pfaffian obstruction ledger."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="Pfaffian fixture directory")
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
    if manifest.get("pfaffian_kind") != EXPECTED_PFIN_KIND:
        issues.append(
            "Pfaffian manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("Pfaffian manifest does not mark empty_blocked=true")
    if manifest.get("scalar_only") is True:
        issues.append("Pfaffian manifest marks scalar-only data")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing Pfaffian table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"Pfaffian table {table_name} now has data rows; "
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
        if row.get("pfaffian_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: pfaffian_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"Pfaffian fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "PFAFFIAN_OBSTRUCTION_LEDGER_FAILED"
    print("finite Pfaffian obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("pfaffian_certification: false")
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
