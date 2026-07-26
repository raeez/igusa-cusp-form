#!/usr/bin/env python3
"""Verify the protected trace obstruction ledger.

This verifier certifies only the absence ledger for the finite
level-Z protected trace packet.  It checks that the trace fixture is
still the empty blocked scaffold, that its required tables have no
rows, and that every missing trace artifact is recorded in
blocked_obligations.csv.

It does not construct the protected trace or the gravity-line operator
algebra.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "TRACE_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_TRACE_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "trace_categories.csv",
    "protected_trace_functors.csv",
    "trace_operators.csv",
    "scalar_normalizations.csv",
    "trace_identities.csv",
    "forgetful_maps.csv",
    "gravity_residuals.csv",
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
    "trace_status",
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
    RequiredObligation("trace_category_level", "trace_category", "trace_categories.csv", "level_z_category"),
    RequiredObligation("trace_source_object", "trace_category", "trace_categories.csv", "source_object"),
    RequiredObligation("trace_closed_cobordism", "trace_category", "trace_categories.csv", "closed_cobordism"),
    RequiredObligation("trace_operator_domain", "trace_category", "trace_categories.csv", "operator_domain"),
    RequiredObligation("trace_category_defects", "trace_category", "trace_categories.csv", "category_defects"),
    RequiredObligation("trace_functor_domain", "trace_functor", "protected_trace_functors.csv", "domain_category"),
    RequiredObligation("trace_functor_codomain", "trace_functor", "protected_trace_functors.csv", "codomain"),
    RequiredObligation("trace_functor_degree", "trace_functor", "protected_trace_functors.csv", "degree_variable"),
    RequiredObligation("trace_functor_functoriality", "trace_functor", "protected_trace_functors.csv", "functoriality"),
    RequiredObligation("trace_functor_cyclicity", "trace_functor", "protected_trace_functors.csv", "cyclicity"),
    RequiredObligation("trace_functor_excision", "trace_functor", "protected_trace_functors.csv", "excision"),
    RequiredObligation("operator_pfaffian_section", "trace_operator", "trace_operators.csv", "pfaffian_section"),
    RequiredObligation("operator_determinant_section", "trace_operator", "trace_operators.csv", "determinant_section"),
    RequiredObligation("operator_inverse_square", "trace_operator", "trace_operators.csv", "inverse_square"),
    RequiredObligation("operator_delta5_square", "trace_operator", "trace_operators.csv", "delta5_square"),
    RequiredObligation("operator_orientation_forgetting", "trace_operator", "trace_operators.csv", "orientation_forgetting"),
    RequiredObligation("normalization_op_branch", "scalar_normalization", "scalar_normalizations.csv", "op_branch"),
    RequiredObligation("normalization_leading_64", "scalar_normalization", "scalar_normalizations.csv", "leading_coefficient"),
    RequiredObligation("normalization_square_4096", "scalar_normalization", "scalar_normalizations.csv", "square_coefficient"),
    RequiredObligation("normalization_op_sign", "scalar_normalization", "scalar_normalizations.csv", "op_sign"),
    RequiredObligation("normalization_unscaled_trace", "scalar_normalization", "scalar_normalizations.csv", "unscaled_trace"),
    RequiredObligation("identity_delta5_inverse_square", "trace_identity", "trace_identities.csv", "delta5_inverse_square"),
    RequiredObligation("identity_phi10_inverse", "trace_identity", "trace_identities.csv", "phi10_inverse"),
    RequiredObligation("identity_context", "trace_identity", "trace_identities.csv", "equality_context"),
    RequiredObligation("identity_residual", "trace_identity", "trace_identities.csv", "identity_residual"),
    RequiredObligation("forget_orientation", "forgetful_map", "forgetful_maps.csv", "orientation_killed"),
    RequiredObligation("forget_bracket", "forgetful_map", "forgetful_maps.csv", "bracket_killed"),
    RequiredObligation("forget_hopf_pairing", "forgetful_map", "forgetful_maps.csv", "pairing_killed"),
    RequiredObligation("forget_pbw", "forgetful_map", "forgetful_maps.csv", "pbw_killed"),
    RequiredObligation("forget_parity", "forgetful_map", "forgetful_maps.csv", "parity_killed"),
    RequiredObligation("forget_kernel_witness", "forgetful_map", "forgetful_maps.csv", "kernel_witness"),
    RequiredObligation("gravity_level_a_residual", "gravity_residual", "gravity_residuals.csv", "level_a_residual"),
    RequiredObligation("gravity_operator_algebra", "gravity_residual", "gravity_residuals.csv", "operator_algebra"),
    RequiredObligation("gravity_morphism", "gravity_residual", "gravity_residuals.csv", "morphism"),
    RequiredObligation("gravity_trace_character", "gravity_residual", "gravity_residuals.csv", "trace_character"),
    RequiredObligation("gravity_open_status", "gravity_residual", "gravity_residuals.csv", "open_not_constructed"),
    RequiredObligation("gravity_unused_in_trace", "gravity_residual", "gravity_residuals.csv", "unused_in_trace_proof"),
    RequiredObligation("transition_strict", "transition", "transitions.csv", "strict_transition"),
    RequiredObligation("transition_mittag_leffler", "transition", "transitions.csv", "mittag_leffler"),
    RequiredObligation("transition_r1lim", "transition", "transitions.csv", "r1lim_zero"),
    RequiredObligation("transition_normalization", "transition", "transitions.csv", "normalization_defect"),
    RequiredObligation("transition_forgetful", "transition", "transitions.csv", "forgetful_defect"),
    RequiredObligation("firewall_gravity_path_integral", "scalar_firewall", "scalar_firewall.csv", "gravity_path_integral"),
    RequiredObligation("firewall_hopf_pairing", "scalar_firewall", "scalar_firewall.csv", "hopf_pairing"),
    RequiredObligation("firewall_orientation_character", "scalar_firewall", "scalar_firewall.csv", "orientation_character"),
    RequiredObligation("firewall_parity_split", "scalar_firewall", "scalar_firewall.csv", "parity_split"),
    RequiredObligation("firewall_pbw_basis", "scalar_firewall", "scalar_firewall.csv", "pbw_basis"),
    RequiredObligation("firewall_pfaffian_line", "scalar_firewall", "scalar_firewall.csv", "pfaffian_line"),
    RequiredObligation("firewall_primitive_bracket", "scalar_firewall", "scalar_firewall.csv", "primitive_bracket"),
    RequiredObligation("firewall_source_koszul_map", "scalar_firewall", "scalar_firewall.csv", "source_koszul_map"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the protected trace obstruction ledger.")
    parser.add_argument("--fixture", required=True, type=Path, help="trace fixture directory")
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
    if manifest.get("trace_kind") != EXPECTED_TRACE_KIND:
        issues.append(
            "trace manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("trace manifest does not mark empty_blocked=true")
    for key in (
        "automorphic_only",
        "gravity_path_integral",
        "op_only",
        "pfaffian_only",
        "scalar_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"trace manifest marks {key}=true")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing trace table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"trace table {table_name} now has data rows; "
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
        if row.get("trace_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: trace_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"trace fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "TRACE_OBSTRUCTION_LEDGER_FAILED"
    print("protected trace obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("protected_trace_certification: false")
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
