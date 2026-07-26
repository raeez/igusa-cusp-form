#!/usr/bin/env python3
"""Verify the compact Hall source obstruction ledger.

This verifier certifies only the absence ledger for the compact
K3xE Hall source packet.  It checks that the source fixture is still the
empty blocked scaffold, that the required source tables have no rows,
and that every missing Hall, Hopf, radical, PBW, transition, A_beta, and
Koszul artifact is recorded in blocked_obligations.csv.

It does not prove compact-source recognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_SOURCE_KIND = "mock_empty_blocked"
EXPECTED_SOURCE_TABLES = (
    "degrees.csv",
    "parity_blocks.csv",
    "basis_provenance.csv",
    "simple_representatives.csv",
    "M_entries.csv",
    "D_entries.csv",
    "unit_counit.csv",
    "B_entries.csv",
    "G_entries.csv",
    "hopf_pairing_identities.csv",
    "K_entries.csv",
    "Q_entries.csv",
    "A_entries.csv",
    "hall_bialgebra_identities.csv",
    "radical_ideal_coideal.csv",
    "relation_rows.csv",
    "no_extra.csv",
    "generation.csv",
    "pbw.csv",
    "transitions.csv",
    "a_beta_comparison_maps.csv",
    "koszul_cones.csv",
    "koszul_comparison_identities.csv",
    "koszul_transition_ml.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "source_status",
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
    RequiredObligation("source_degrees", "source_basis", "degrees.csv", "compact_source_degree"),
    RequiredObligation("parity_blocks", "source_basis", "parity_blocks.csv", "even_odd_ranks"),
    RequiredObligation("basis_provenance", "source_basis", "basis_provenance.csv", "geometric_basis_rows"),
    RequiredObligation("simple_representatives", "source_basis", "simple_representatives.csv", "simple_primitive_rows"),
    RequiredObligation("hall_product_M", "hall_bialgebra", "M_entries.csv", "product_matrix"),
    RequiredObligation("hall_coproduct_D", "hall_bialgebra", "D_entries.csv", "coproduct_matrix"),
    RequiredObligation("hall_unit", "hall_bialgebra", "unit_counit.csv", "unit"),
    RequiredObligation("hall_counit", "hall_bialgebra", "unit_counit.csv", "counit"),
    RequiredObligation("identity_unit_left", "hall_bialgebra", "hall_bialgebra_identities.csv", "unit_left"),
    RequiredObligation("identity_unit_right", "hall_bialgebra", "hall_bialgebra_identities.csv", "unit_right"),
    RequiredObligation("identity_counit_left", "hall_bialgebra", "hall_bialgebra_identities.csv", "counit_left"),
    RequiredObligation("identity_counit_right", "hall_bialgebra", "hall_bialgebra_identities.csv", "counit_right"),
    RequiredObligation("identity_associativity", "hall_bialgebra", "hall_bialgebra_identities.csv", "associativity"),
    RequiredObligation("identity_coassociativity", "hall_bialgebra", "hall_bialgebra_identities.csv", "coassociativity"),
    RequiredObligation("identity_bialgebra_compatibility", "hall_bialgebra", "hall_bialgebra_identities.csv", "bialgebra_compatibility"),
    RequiredObligation("identity_primitive_closure", "hall_bialgebra", "hall_bialgebra_identities.csv", "primitive_closure"),
    RequiredObligation("bracket_B", "primitive_bracket", "B_entries.csv", "supercommutator_matrix"),
    RequiredObligation("pairing_G", "hopf_pairing", "G_entries.csv", "pairing_matrix"),
    RequiredObligation("identity_hopf_adjointness", "hopf_pairing", "hopf_pairing_identities.csv", "hopf_adjointness"),
    RequiredObligation("identity_frobenius_cyclic", "hopf_pairing", "hopf_pairing_identities.csv", "frobenius_cyclic"),
    RequiredObligation("identity_quotient_nondegenerate", "hopf_pairing", "hopf_pairing_identities.csv", "quotient_nondegenerate"),
    RequiredObligation("radical_kernel_K", "radical_quotient", "K_entries.csv", "kernel_matrix"),
    RequiredObligation("quotient_splitting_Q", "radical_quotient", "Q_entries.csv", "quotient_splitting"),
    RequiredObligation("identity_lie_ideal", "radical_quotient", "radical_ideal_coideal.csv", "lie_ideal"),
    RequiredObligation("identity_coproduct_coideal", "radical_quotient", "radical_ideal_coideal.csv", "coproduct_coideal"),
    RequiredObligation("relation_cartan", "relations", "relation_rows.csv", "cartan"),
    RequiredObligation("relation_chevalley", "relations", "relation_rows.csv", "chevalley"),
    RequiredObligation("relation_real_serre", "relations", "relation_rows.csv", "real_serre"),
    RequiredObligation("relation_borcherds_orthogonality", "relations", "relation_rows.csv", "borcherds_orthogonality"),
    RequiredObligation("relation_super_sign", "relations", "relation_rows.csv", "super_sign"),
    RequiredObligation("no_extra_kernel", "recognition", "no_extra.csv", "kernel_equality"),
    RequiredObligation("generation_span", "recognition", "generation.csv", "simple_generation"),
    RequiredObligation("pbw_associated_graded", "recognition", "pbw.csv", "associated_graded_rank"),
    RequiredObligation("strict_ml_transitions", "recognition", "transitions.csv", "strict_pbw_and_ml"),
    RequiredObligation("a_beta_bracket", "comparison", "a_beta_comparison_maps.csv", "bracket"),
    RequiredObligation("a_beta_coproduct", "comparison", "a_beta_comparison_maps.csv", "coproduct"),
    RequiredObligation("a_beta_pairing", "comparison", "a_beta_comparison_maps.csv", "pairing"),
    RequiredObligation("a_beta_radical_quotient", "comparison", "a_beta_comparison_maps.csv", "radical_quotient"),
    RequiredObligation("a_beta_pbw", "comparison", "a_beta_comparison_maps.csv", "pbw"),
    RequiredObligation("koszul_source_counit_cone", "koszul", "koszul_cones.csv", "source_bar_cobar_counit"),
    RequiredObligation("koszul_quasi_isomorphism_cone", "koszul", "koszul_cones.csv", "source_to_target_quasi_isomorphism"),
    RequiredObligation("koszul_identity_weyl_action", "koszul", "koszul_comparison_identities.csv", "weyl_action"),
    RequiredObligation("koszul_identity_pfaffian_orientation", "koszul", "koszul_comparison_identities.csv", "pfaffian_orientation"),
    RequiredObligation("koszul_identity_hall_product", "koszul", "koszul_comparison_identities.csv", "hall_product"),
    RequiredObligation("koszul_identity_hall_coproduct", "koszul", "koszul_comparison_identities.csv", "hall_coproduct"),
    RequiredObligation("koszul_identity_hopf_pairing", "koszul", "koszul_comparison_identities.csv", "hopf_pairing"),
    RequiredObligation("koszul_identity_radical_quotient", "koszul", "koszul_comparison_identities.csv", "radical_quotient"),
    RequiredObligation("koszul_identity_pbw", "koszul", "koszul_comparison_identities.csv", "pbw"),
    RequiredObligation("koszul_ml_source_cone", "koszul", "koszul_transition_ml.csv", "source_cone"),
    RequiredObligation("koszul_ml_target_cone", "koszul", "koszul_transition_ml.csv", "target_cone"),
    RequiredObligation("koszul_ml_weyl_action", "koszul", "koszul_transition_ml.csv", "weyl_action"),
    RequiredObligation("koszul_ml_pfaffian_orientation", "koszul", "koszul_transition_ml.csv", "pfaffian_orientation"),
    RequiredObligation("koszul_ml_hall_pairing", "koszul", "koszul_transition_ml.csv", "hall_pairing"),
    RequiredObligation("koszul_ml_radical_quotient", "koszul", "koszul_transition_ml.csv", "radical_quotient"),
    RequiredObligation("koszul_ml_pbw", "koszul", "koszul_transition_ml.csv", "pbw"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the compact Hall source obstruction ledger."
    )
    parser.add_argument("--source", required=True, type=Path, help="source fixture directory")
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


def load_manifest(source: Path, issues: list[str]) -> dict[str, object]:
    path = source / MANIFEST_NAME
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
    if manifest.get("source_kind") != EXPECTED_SOURCE_KIND:
        issues.append(
            "source manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("source manifest does not mark empty_blocked=true")
    if manifest.get("target_truth_generated") is True:
        issues.append("source manifest claims generated target truth")


def check_source_tables_are_empty(source: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_SOURCE_TABLES:
        path = source / table_name
        if not path.is_file():
            issues.append(f"missing source table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"source table {table_name} now has data rows; "
                "the obstruction ledger must be retired or narrowed"
            )


def load_obligations(source: Path, issues: list[str]) -> list[dict[str, str]]:
    path = source / OBLIGATION_FILE
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
    by_id = {row.get("obligation_id", ""): row for row in rows}
    required_ids = {entry.obligation_id for entry in REQUIRED_OBLIGATIONS}
    actual_ids = set(by_id)
    missing = sorted(required_ids - actual_ids)
    extra = sorted(actual_ids - required_ids)
    if missing:
        issues.append("missing obligation rows: " + ",".join(missing))
    if extra:
        issues.append("unexpected obligation rows: " + ",".join(extra))

    required_by_id = {entry.obligation_id: entry for entry in REQUIRED_OBLIGATIONS}
    for row_number, row in enumerate(rows, start=2):
        obligation_id = row.get("obligation_id", "")
        required = required_by_id.get(obligation_id)
        if required is None:
            continue
        for column in OBLIGATION_COLUMNS:
            if not row.get(column, ""):
                issues.append(
                    f"blocked_obligations.csv:{row_number} missing {column}"
                )
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
        if row.get("source_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: source_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(source: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not source.is_dir():
        return False, [f"source fixture directory does not exist: {source}"]
    manifest = load_manifest(source, issues)
    check_manifest(manifest, issues)
    check_source_tables_are_empty(source, issues)
    rows = load_obligations(source, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(source: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "COMPACT_HALL_OBSTRUCTION_LEDGER_FAILED"
    print("compact Hall source obstruction ledger verifier")
    print("mode: check-only")
    print(f"source: {source}")
    print(f"status: {status}")
    print("compact_source_recognition: false")
    print("mathematical_certification: false")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    ok, issues = run(args.source)
    print_report(args.source, ok, issues)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
