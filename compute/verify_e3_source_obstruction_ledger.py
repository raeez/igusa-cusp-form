#!/usr/bin/env python3
"""Verify the finite E3 source obstruction ledger.

This verifier certifies only the absence ledger for the finite
holomorphic E3-prefactorization and K3-to-E specialization packet.  It
checks that the E3 source fixture is still the empty blocked scaffold,
that its required tables have no rows, and that every missing compact
source artifact is recorded in blocked_obligations.csv.

It does not construct the compact K3xE source.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "E3_SOURCE_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_E3_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "formal_target_charts.csv",
    "field_complexes.csv",
    "e3_operations.csv",
    "bv_qme.csv",
    "anomaly_framing.csv",
    "compact_support.csv",
    "factorization_descent.csv",
    "k3_to_e_specialization.csv",
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
    "e3_status",
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
    RequiredObligation("formal_chart", "formal_target", "formal_target_charts.csv", "derived_formal_neighborhood"),
    RequiredObligation("local_model", "formal_target", "formal_target_charts.csv", "local_model"),
    RequiredObligation("holomorphic_volume_form", "formal_target", "formal_target_charts.csv", "holomorphic_volume_form"),
    RequiredObligation("finite_type_chart", "formal_target", "formal_target_charts.csv", "finite_type_status"),
    RequiredObligation("field_complex", "field_complex", "field_complexes.csv", "field_complex"),
    RequiredObligation("field_differential", "field_complex", "field_complexes.csv", "differential"),
    RequiredObligation("field_symplectic_pairing", "field_complex", "field_complexes.csv", "symplectic_pairing"),
    RequiredObligation("field_pairing_degree", "field_complex", "field_complexes.csv", "pairing_degree"),
    RequiredObligation("field_elliptic_window", "field_complex", "field_complexes.csv", "elliptic_degree_window"),
    RequiredObligation("field_cohomology_defect", "field_complex", "field_complexes.csv", "cohomology_defect"),
    RequiredObligation("field_pairing_defect", "field_complex", "field_complexes.csv", "pairing_defect"),
    RequiredObligation("operation_unit", "e3_operation", "e3_operations.csv", "unit"),
    RequiredObligation("operation_binary_product", "e3_operation", "e3_operations.csv", "binary_product"),
    RequiredObligation("operation_little_3_disks", "e3_operation", "e3_operations.csv", "little_3_disks_action"),
    RequiredObligation("operation_higher_coherence", "e3_operation", "e3_operations.csv", "higher_coherence"),
    RequiredObligation("operation_locality", "e3_operation", "e3_operations.csv", "locality_support"),
    RequiredObligation("operation_associativity", "e3_operation", "e3_operations.csv", "associativity_defect"),
    RequiredObligation("operation_equivariance", "e3_operation", "e3_operations.csv", "equivariance_defect"),
    RequiredObligation("operation_unitality", "e3_operation", "e3_operations.csv", "unit_defect"),
    RequiredObligation("qme_action_functional", "bv_qme", "bv_qme.csv", "action_functional"),
    RequiredObligation("qme_bv_laplacian", "bv_qme", "bv_qme.csv", "bv_laplacian"),
    RequiredObligation("qme_bv_bracket", "bv_qme", "bv_qme.csv", "bv_bracket"),
    RequiredObligation("qme_classical_master", "bv_qme", "bv_qme.csv", "classical_master"),
    RequiredObligation("qme_quantum_master", "bv_qme", "bv_qme.csv", "quantum_master"),
    RequiredObligation("qme_anomaly_class", "bv_qme", "bv_qme.csv", "anomaly_class"),
    RequiredObligation("anomaly_bv_qme", "anomaly", "anomaly_framing.csv", "bv_qme"),
    RequiredObligation("anomaly_holomorphic_de_rham", "anomaly", "anomaly_framing.csv", "holomorphic_de_rham"),
    RequiredObligation("anomaly_framing", "anomaly", "anomaly_framing.csv", "framing"),
    RequiredObligation("anomaly_formality", "anomaly", "anomaly_framing.csv", "formality"),
    RequiredObligation("anomaly_trivialization", "anomaly", "anomaly_framing.csv", "trivialization"),
    RequiredObligation("support_compact_condition", "compact_support", "compact_support.csv", "compact_support_condition"),
    RequiredObligation("support_proper_status", "compact_support", "compact_support.csv", "proper_status"),
    RequiredObligation("support_boundary_exclusion", "compact_support", "compact_support.csv", "boundary_exclusion"),
    RequiredObligation("support_defect", "compact_support", "compact_support.csv", "support_defect"),
    RequiredObligation("descent_cover", "descent", "factorization_descent.csv", "cover"),
    RequiredObligation("descent_prefactorization_map", "descent", "factorization_descent.csv", "prefactorization_map"),
    RequiredObligation("descent_cech", "descent", "factorization_descent.csv", "cech_defect"),
    RequiredObligation("descent_locality", "descent", "factorization_descent.csv", "locality_defect"),
    RequiredObligation("descent_defect", "descent", "factorization_descent.csv", "descent_defect"),
    RequiredObligation("specialization_chain_map", "specialization", "k3_to_e_specialization.csv", "chain_map"),
    RequiredObligation("specialization_cosection", "specialization", "k3_to_e_specialization.csv", "cosection_compatibility"),
    RequiredObligation("specialization_wrapped_leg", "specialization", "k3_to_e_specialization.csv", "wrapped_leg_compatibility"),
    RequiredObligation("specialization_vanishing_cycle", "specialization", "k3_to_e_specialization.csv", "vanishing_cycle_defect"),
    RequiredObligation("specialization_orientation", "specialization", "k3_to_e_specialization.csv", "orientation_defect"),
    RequiredObligation("specialization_pfaffian", "specialization", "k3_to_e_specialization.csv", "pfaffian_defect"),
    RequiredObligation("specialization_chain_homotopy", "specialization", "k3_to_e_specialization.csv", "chain_homotopy_defect"),
    RequiredObligation("transition_strict", "transition", "transitions.csv", "strict_transition"),
    RequiredObligation("transition_mittag_leffler", "transition", "transitions.csv", "mittag_leffler"),
    RequiredObligation("transition_r1lim", "transition", "transitions.csv", "r1lim_zero"),
    RequiredObligation("transition_operation_defect", "transition", "transitions.csv", "operation_defect"),
    RequiredObligation("transition_specialization_defect", "transition", "transitions.csv", "specialization_defect"),
    RequiredObligation("firewall_automorphic_section", "scalar_firewall", "scalar_firewall.csv", "automorphic_section"),
    RequiredObligation("firewall_borcherds_denominator", "scalar_firewall", "scalar_firewall.csv", "borcherds_denominator"),
    RequiredObligation("firewall_hybrid_carrier_only", "scalar_firewall", "scalar_firewall.csv", "hybrid_carrier_only"),
    RequiredObligation("firewall_protected_trace", "scalar_firewall", "scalar_firewall.csv", "protected_trace"),
    RequiredObligation("firewall_target_current_envelope", "scalar_firewall", "scalar_firewall.csv", "target_current_envelope"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the finite E3 source obstruction ledger.")
    parser.add_argument("--fixture", required=True, type=Path, help="E3 source fixture directory")
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
    if manifest.get("e3_source_kind") != EXPECTED_E3_KIND:
        issues.append(
            "E3 source manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("E3 source manifest does not mark empty_blocked=true")
    for key in ("scalar_only", "target_only", "hybrid_only"):
        if manifest.get(key) is True:
            issues.append(f"E3 source manifest marks {key}=true")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing E3 source table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"E3 source table {table_name} now has data rows; "
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
        if row.get("e3_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: e3_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"E3 source fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "E3_SOURCE_OBSTRUCTION_LEDGER_FAILED"
    print("finite E3 source obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("e3_source_certification: false")
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
