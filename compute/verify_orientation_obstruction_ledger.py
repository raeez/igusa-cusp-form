#!/usr/bin/env python3
"""Verify the reduced-orientation obstruction ledger.

This verifier certifies only the absence ledger for the finite
orientation packet.  It checks that the orientation fixture is still the
empty blocked scaffold, that its required tables have no rows, and that
every missing O1/O1+ artifact is recorded in blocked_obligations.csv.

It does not prove reduced orientation, Weyl equivariance, or the
orientation character.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_ORIENTATION_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "orientation_lines.csv",
    "ts_multiplicativity.csv",
    "quotient_borel.csv",
    "finite_stabilizers.csv",
    "weyl_lifts.csv",
    "coxeter_cocycles.csv",
    "transitions.csv",
    "scalar_firewall.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "cohomology_or_rank_payload",
    "why_required",
    "orientation_status",
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
    RequiredObligation("orientation_square_root", "orientation_line", "orientation_lines.csv", "square_root"),
    RequiredObligation("orientation_class_zero", "orientation_line", "orientation_lines.csv", "orientation_class_rank"),
    RequiredObligation("ts_multiplicativity", "multiplicativity", "ts_multiplicativity.csv", "ts_isomorphism"),
    RequiredObligation("ts_pentagon", "multiplicativity", "ts_multiplicativity.csv", "pentagon_defect"),
    RequiredObligation("borel_reduced_gerbe", "quotient_borel", "quotient_borel.csv", "reduced_gerbe"),
    RequiredObligation("borel_free_E", "quotient_borel", "quotient_borel.csv", "free_E"),
    RequiredObligation("borel_finite_stabilizer", "quotient_borel", "quotient_borel.csv", "finite_stabilizer_borel"),
    RequiredObligation("borel_linearization", "quotient_borel", "quotient_borel.csv", "linearization"),
    RequiredObligation("finite_edge_reduction", "finite_stabilizer", "finite_stabilizers.csv", "edge_reduction"),
    RequiredObligation("finite_odd_transfer", "finite_stabilizer", "finite_stabilizers.csv", "odd_transfer"),
    RequiredObligation("finite_klein_four_quadratic", "finite_stabilizer", "finite_stabilizers.csv", "klein_four_b20_b11_b02"),
    RequiredObligation("finite_klein_four_linear", "finite_stabilizer", "finite_stabilizers.csv", "klein_four_lambda"),
    RequiredObligation("finite_two_primary_quadratic", "finite_stabilizer", "finite_stabilizers.csv", "two_primary_A1_A12_A2"),
    RequiredObligation("finite_two_primary_linear", "finite_stabilizer", "finite_stabilizers.csv", "two_primary_lambda"),
    RequiredObligation("weyl_lift_tau_square", "weyl_transport", "weyl_lifts.csv", "tau_square"),
    RequiredObligation("weyl_lift_torsor", "weyl_transport", "weyl_lifts.csv", "torsor_defect"),
    RequiredObligation("weyl_lift_quotient_transport", "weyl_transport", "weyl_lifts.csv", "quotient_cocycle_transport"),
    RequiredObligation("coxeter_projective_cocycle", "weyl_transport", "coxeter_cocycles.csv", "projective_cocycle"),
    RequiredObligation("coxeter_cochain_trivialization", "weyl_transport", "coxeter_cocycles.csv", "cochain_trivialization"),
    RequiredObligation("coxeter_coherence", "weyl_transport", "coxeter_cocycles.csv", "coxeter_coherence"),
    RequiredObligation("transition_strict", "transition", "transitions.csv", "strict_orientation_transition"),
    RequiredObligation("transition_ml", "transition", "transitions.csv", "orientation_ML"),
    RequiredObligation("firewall_scalar_trace", "scalar_firewall", "scalar_firewall.csv", "scalar_trace"),
    RequiredObligation("firewall_squared_determinant", "scalar_firewall", "scalar_firewall.csv", "squared_determinant"),
    RequiredObligation("firewall_op_scalar_branch", "scalar_firewall", "scalar_firewall.csv", "op_scalar_branch"),
    RequiredObligation("firewall_maass_character", "scalar_firewall", "scalar_firewall.csv", "maass_character_value"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the reduced-orientation obstruction ledger."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="orientation fixture directory")
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
    if manifest.get("orientation_kind") != EXPECTED_ORIENTATION_KIND:
        issues.append(
            "orientation manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("orientation manifest does not mark empty_blocked=true")
    if manifest.get("picard_line_only") is True:
        issues.append("orientation manifest marks Picard-line-only data")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing orientation table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"orientation table {table_name} now has data rows; "
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
        if row.get("orientation_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: orientation_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"orientation fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "ORIENTATION_OBSTRUCTION_LEDGER_FAILED"
    print("orientation obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("orientation_certification: false")
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
