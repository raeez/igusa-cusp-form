#!/usr/bin/env python3
"""Verify the first relation-closed window obstruction ledger.

This verifier certifies only the absence ledger for the first
relation-closed compact-source recognition window.  It checks that the
first-window packet is still the scalar-firewall blocked scaffold, that
the core recognition tables remain empty, that the scalar-firewall table
excludes the known shortcuts, and that every missing finite theorem row
is recorded in blocked_obligations.csv.

It does not prove first-window primitive recognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "FIRST_WINDOW_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_FIRST_WINDOW_KIND = "first_window_scalar_firewall_blocked"
EXPECTED_STAGE = "scalar_firewall_only"
EXPECTED_EMPTY_TABLES = (
    "window_closure.csv",
    "target_source_representatives.csv",
    "chevalley_serre_matrices.csv",
    "hall_boundary_complex.csv",
    "spectral_sequence.csv",
    "kernel_matrices.csv",
    "pbw_graded.csv",
    "first_window_theorems.csv",
    "transitions.csv",
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "arbitrary_matrices",
        "denominator_product",
        "pfaffian_product",
        "scalar_trace",
        "signed_dimensions_only",
        "status_only_rows",
        "target_labels_only",
        "target_pbw_only",
    }
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "first_window_status",
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
    RequiredObligation("window_downward_saturated", "window", "window_closure.csv", "downward_saturated"),
    RequiredObligation("window_relation_closed", "window", "window_closure.csv", "relation_closed"),
    RequiredObligation("window_active_exhaustive", "window", "window_closure.csv", "active_exhaustive"),
    RequiredObligation("window_target_admissible", "window", "window_closure.csv", "target_admissible"),
    RequiredObligation("window_source_admissible", "window", "window_closure.csv", "source_admissible"),
    RequiredObligation("window_closure_defect", "window", "window_closure.csv", "closure_defect_zero"),
    RequiredObligation("window_signed_only_defect", "window", "window_closure.csv", "signed_only_defect_zero"),
    RequiredObligation("representative_source_basis", "representatives", "target_source_representatives.csv", "source_cycle"),
    RequiredObligation("representative_compact_provenance", "representatives", "target_source_representatives.csv", "compact_provenance"),
    RequiredObligation("representative_full_parity", "representatives", "target_source_representatives.csv", "even_odd_parity"),
    RequiredObligation("representative_rank_equality", "representatives", "target_source_representatives.csv", "source_target_rank_equality"),
    RequiredObligation("representative_parity_defect", "representatives", "target_source_representatives.csv", "parity_defect_zero"),
    RequiredObligation("relation_cartan", "relations", "chevalley_serre_matrices.csv", "cartan"),
    RequiredObligation("relation_chevalley", "relations", "chevalley_serre_matrices.csv", "chevalley"),
    RequiredObligation("relation_real_serre", "relations", "chevalley_serre_matrices.csv", "real_serre"),
    RequiredObligation("relation_borcherds_orthogonality", "relations", "chevalley_serre_matrices.csv", "borcherds_orthogonality"),
    RequiredObligation("relation_super_sign", "relations", "chevalley_serre_matrices.csv", "super_sign"),
    RequiredObligation("relation_rank_equality", "relations", "chevalley_serre_matrices.csv", "source_target_rank_equality"),
    RequiredObligation("relation_defect", "relations", "chevalley_serre_matrices.csv", "relation_defect_zero"),
    RequiredObligation("boundary_complex_terms", "hall_boundary", "hall_boundary_complex.csv", "c0_c1_c2_terms"),
    RequiredObligation("boundary_d1_matrix", "hall_boundary", "hall_boundary_complex.csv", "d1_matrix"),
    RequiredObligation("boundary_d1_square", "hall_boundary", "hall_boundary_complex.csv", "d1_square_zero"),
    RequiredObligation("boundary_serre_defect", "hall_boundary", "hall_boundary_complex.csv", "serre_boundary_defect_zero"),
    RequiredObligation("spectral_ranks", "spectral_sequence", "spectral_sequence.csv", "e1_e2_einf_ranks"),
    RequiredObligation("spectral_d1_defect", "spectral_sequence", "spectral_sequence.csv", "d1_defect_zero"),
    RequiredObligation("spectral_higher_differentials", "spectral_sequence", "spectral_sequence.csv", "higher_differentials_zero"),
    RequiredObligation("spectral_strong_convergence", "spectral_sequence", "spectral_sequence.csv", "strong_convergence"),
    RequiredObligation("kernel_presentation_matrix", "kernel", "kernel_matrices.csv", "presentation_matrix"),
    RequiredObligation("kernel_basis", "kernel", "kernel_matrices.csv", "kernel_basis"),
    RequiredObligation("kernel_gn_rank", "kernel", "kernel_matrices.csv", "gn_kernel_rank"),
    RequiredObligation("kernel_radical_rank", "kernel", "kernel_matrices.csv", "radical_rank"),
    RequiredObligation("kernel_equality", "kernel", "kernel_matrices.csv", "kernel_equality_defect_zero"),
    RequiredObligation("kernel_no_extra", "kernel", "kernel_matrices.csv", "no_extra_defect_zero"),
    RequiredObligation("pbw_source_rank", "pbw", "pbw_graded.csv", "source_pbw_rank"),
    RequiredObligation("pbw_target_rank", "pbw", "pbw_graded.csv", "target_pbw_rank"),
    RequiredObligation("pbw_associated_graded", "pbw", "pbw_graded.csv", "associated_graded_rank"),
    RequiredObligation("pbw_defect", "pbw", "pbw_graded.csv", "pbw_defect_zero"),
    RequiredObligation("pbw_filtration_strict", "pbw", "pbw_graded.csv", "filtration_strictness_zero"),
    RequiredObligation("theorem_o1", "theorem_rows", "first_window_theorems.csv", "o1"),
    RequiredObligation("theorem_o1_plus", "theorem_rows", "first_window_theorems.csv", "o1_plus"),
    RequiredObligation("theorem_o2", "theorem_rows", "first_window_theorems.csv", "o2"),
    RequiredObligation("theorem_pfin", "theorem_rows", "first_window_theorems.csv", "pfin"),
    RequiredObligation("theorem_hall_product", "theorem_rows", "first_window_theorems.csv", "hall_product"),
    RequiredObligation("theorem_hall_coproduct", "theorem_rows", "first_window_theorems.csv", "hall_coproduct"),
    RequiredObligation("theorem_hopf_pairing", "theorem_rows", "first_window_theorems.csv", "hopf_pairing"),
    RequiredObligation("theorem_koszul_comparison", "theorem_rows", "first_window_theorems.csv", "koszul_comparison"),
    RequiredObligation("theorem_pbw_comparison", "theorem_rows", "first_window_theorems.csv", "pbw_comparison"),
    RequiredObligation("theorem_primitive_recognition", "theorem_rows", "first_window_theorems.csv", "primitive_recognition"),
    RequiredObligation("theorem_pfaffian_equality", "theorem_rows", "first_window_theorems.csv", "pfaffian_equality"),
    RequiredObligation("transition_strict", "transitions", "transitions.csv", "strict_transition"),
    RequiredObligation("transition_mittag_leffler", "transitions", "transitions.csv", "mittag_leffler"),
    RequiredObligation("transition_r1lim", "transitions", "transitions.csv", "r1lim_zero"),
    RequiredObligation("transition_kernel_compatible", "transitions", "transitions.csv", "kernel_transition_defect_zero"),
    RequiredObligation("transition_pbw_compatible", "transitions", "transitions.csv", "pbw_transition_defect_zero"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the first-window obstruction ledger."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="first-window fixture directory")
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
    if manifest.get("first_window_kind") != EXPECTED_FIRST_WINDOW_KIND:
        issues.append(
            "first-window manifest is no longer the scalar-firewall scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("stage") != EXPECTED_STAGE:
        issues.append("first-window manifest stage is not scalar_firewall_only")
    if manifest.get("certified") is not False:
        issues.append("first-window manifest must keep certified=false")
    if manifest.get("scalar_firewall_verified") is not True:
        issues.append("first-window manifest must keep scalar_firewall_verified=true")
    for key in (
        "arbitrary_matrices",
        "denominator_only",
        "pfaffian_only",
        "scalar_only",
        "signed_only",
        "target_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"first-window manifest marks {key}=true")


def check_core_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_EMPTY_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing first-window table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"first-window table {table_name} now has data rows; "
                "the obstruction ledger must be retired or narrowed"
            )


def check_scalar_firewall(fixture: Path, issues: list[str]) -> None:
    path = fixture / "scalar_firewall.csv"
    if not path.is_file():
        issues.append("missing first-window scalar_firewall.csv")
        return
    with path.open(newline="", encoding="utf-8") as handle:
        rows = nonempty_rows(csv.DictReader(handle))
    by_type: dict[str, dict[str, str]] = {}
    seen_check_ids: set[str] = set()
    for row_number, row in enumerate(rows, start=2):
        check_id = row.get("check_id", "")
        if check_id in seen_check_ids:
            issues.append(f"scalar_firewall.csv:{row_number} duplicate check_id {check_id!r}")
        seen_check_ids.add(check_id)
        firewall_type = row.get("firewall_type", "")
        if firewall_type in by_type:
            issues.append(
                f"scalar_firewall.csv:{row_number} duplicate firewall_type {firewall_type!r}"
            )
        by_type[firewall_type] = row
    missing = sorted(REQUIRED_FIREWALL_TYPES - set(by_type))
    if missing:
        issues.append("scalar_firewall.csv missing firewall_type rows: " + ",".join(missing))
    for firewall_type, row in by_type.items():
        if firewall_type not in REQUIRED_FIREWALL_TYPES:
            issues.append(f"unexpected scalar firewall row: {firewall_type}")
            continue
        if row.get("excluded_from_first_window", "").lower() != "true":
            issues.append(f"{firewall_type}: excluded_from_first_window is not true")
        if row.get("check_status") != "verified":
            issues.append(f"{firewall_type}: check_status is not verified")
        for column in ("geometric_source_id", "proof_reference", "notes"):
            if not row.get(column, ""):
                issues.append(f"{firewall_type}: missing scalar firewall {column}")


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
        if row.get("first_window_status") != "missing_open_obligation":
            issues.append(
                f"{obligation_id}: first_window_status is not missing_open_obligation"
            )
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"first-window fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_core_tables_are_empty(fixture, issues)
    check_scalar_firewall(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "FIRST_WINDOW_OBSTRUCTION_LEDGER_FAILED"
    print("first relation-closed window obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("first_window_certification: false")
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
