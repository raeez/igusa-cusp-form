#!/usr/bin/env python3
"""Verify the Dirac-Igusa pro-object morphism obstruction ledger.

This verifier certifies only the absence ledger for the finite-stage
Dirac-Igusa morphism packet.  It checks that the packet remains the
empty blocked scaffold, that the core pro-object tables contain no
rows, that the scalar-firewall rows exclude scalar substitutes, and
that every missing cofinality, finite-stage, transition, Mittag-Leffler,
and pro-isomorphism artifact is recorded in blocked_obligations.csv.

It does not construct the Dirac-Igusa pro-object.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "MORPHISM_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_MORPHISM_KIND = "mock_empty_blocked"
EXPECTED_EMPTY_TABLES = (
    "cofinal_subsystems.csv",
    "stage_objects.csv",
    "stage_morphisms.csv",
    "component_maps.csv",
    "composition_laws.csv",
    "ml_exactness.csv",
    "pro_isomorphisms.csv",
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "denominator_product",
        "protected_trace",
        "scalar_pfaffian_product",
        "signed_exponent_table",
        "squared_determinant",
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
    "pro_object_status",
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
    RequiredObligation("cofinal_poset", "cofinality", "cofinal_subsystems.csv", "poset_id"),
    RequiredObligation("cofinal_directed", "cofinality", "cofinal_subsystems.csv", "directed_status"),
    RequiredObligation("cofinal_verified", "cofinality", "cofinal_subsystems.csv", "cofinal_status"),
    RequiredObligation("cofinal_identity", "cofinality", "cofinal_subsystems.csv", "identity_defect_zero"),
    RequiredObligation("cofinal_composition", "cofinality", "cofinal_subsystems.csv", "composition_defect_zero"),
    RequiredObligation("pro_topology", "cofinality", "cofinal_subsystems.csv", "inverse_limit_topology"),
    RequiredObligation("component_A_E3", "stage_objects", "stage_objects.csv", "A_E3"),
    RequiredObligation("component_F_hyb", "stage_objects", "stage_objects.csv", "F_hyb"),
    RequiredObligation("component_Gamma", "stage_objects", "stage_objects.csv", "Gamma"),
    RequiredObligation("component_Pi", "stage_objects", "stage_objects.csv", "Pi"),
    RequiredObligation("component_Phi", "stage_objects", "stage_objects.csv", "Phi"),
    RequiredObligation("component_o", "stage_objects", "stage_objects.csv", "o"),
    RequiredObligation("component_H", "stage_objects", "stage_objects.csv", "H"),
    RequiredObligation("component_P_Pi", "stage_objects", "stage_objects.csv", "P_Pi"),
    RequiredObligation("component_C", "stage_objects", "stage_objects.csv", "C"),
    RequiredObligation("component_Theta_Kos", "stage_objects", "stage_objects.csv", "Theta_Kos"),
    RequiredObligation("component_L_Pf", "stage_objects", "stage_objects.csv", "L_Pf"),
    RequiredObligation("component_pf", "stage_objects", "stage_objects.csv", "pf"),
    RequiredObligation("component_epsilon_o", "stage_objects", "stage_objects.csv", "epsilon_o"),
    RequiredObligation("component_Rec", "stage_objects", "stage_objects.csv", "Rec"),
    RequiredObligation("stage_typed_category", "stage_objects", "stage_objects.csv", "typed_category"),
    RequiredObligation("stage_finite_type", "stage_objects", "stage_objects.csv", "finite_type_status"),
    RequiredObligation("stage_payload_packet", "stage_objects", "stage_objects.csv", "payload_packet_id"),
    RequiredObligation("transition_morphism", "stage_morphisms", "stage_morphisms.csv", "morphism_id"),
    RequiredObligation("transition_strict", "stage_morphisms", "stage_morphisms.csv", "strict_status"),
    RequiredObligation("transition_component_coverage", "stage_morphisms", "stage_morphisms.csv", "component_coverage_status"),
    RequiredObligation("transition_identity", "stage_morphisms", "stage_morphisms.csv", "identity_defect_zero"),
    RequiredObligation("component_map_M1", "component_maps", "component_maps.csv", "M1"),
    RequiredObligation("component_map_M2", "component_maps", "component_maps.csv", "M2"),
    RequiredObligation("component_map_M3", "component_maps", "component_maps.csv", "M3"),
    RequiredObligation("component_map_M4", "component_maps", "component_maps.csv", "M4"),
    RequiredObligation("component_map_M5", "component_maps", "component_maps.csv", "M5"),
    RequiredObligation("component_map_M6", "component_maps", "component_maps.csv", "M6"),
    RequiredObligation("component_map_M7", "component_maps", "component_maps.csv", "M7"),
    RequiredObligation("component_map_M8", "component_maps", "component_maps.csv", "M8"),
    RequiredObligation("component_map_payload", "component_maps", "component_maps.csv", "map_payload_id"),
    RequiredObligation("component_map_compatibility", "component_maps", "component_maps.csv", "compatibility_defect_zero"),
    RequiredObligation("component_map_kernel", "component_maps", "component_maps.csv", "kernel_rank_zero"),
    RequiredObligation("component_map_cokernel", "component_maps", "component_maps.csv", "cokernel_rank_zero"),
    RequiredObligation("composition_law", "composition", "composition_laws.csv", "rho_composition"),
    RequiredObligation("composition_left_right", "composition", "composition_laws.csv", "left_right_composites"),
    RequiredObligation("composition_defect", "composition", "composition_laws.csv", "composition_defect_zero"),
    RequiredObligation("ml_component_tower", "ml_exactness", "ml_exactness.csv", "component_tower"),
    RequiredObligation("ml_strict", "ml_exactness", "ml_exactness.csv", "strict_status"),
    RequiredObligation("ml_verified", "ml_exactness", "ml_exactness.csv", "ml_status"),
    RequiredObligation("ml_r1lim", "ml_exactness", "ml_exactness.csv", "r1lim_zero"),
    RequiredObligation("ml_transition_defect", "ml_exactness", "ml_exactness.csv", "transition_defect_zero"),
    RequiredObligation("pro_iso_common_cofinal", "pro_isomorphisms", "pro_isomorphisms.csv", "common_cofinal_subsystem"),
    RequiredObligation("pro_iso_finite_family", "pro_isomorphisms", "pro_isomorphisms.csv", "finite_stage_iso_family"),
    RequiredObligation("pro_iso_inverse_family", "pro_isomorphisms", "pro_isomorphisms.csv", "inverse_family"),
    RequiredObligation("pro_iso_status", "pro_isomorphisms", "pro_isomorphisms.csv", "iso_status"),
    RequiredObligation("pro_iso_commuting", "pro_isomorphisms", "pro_isomorphisms.csv", "commute_defect_zero"),
    RequiredObligation("pro_iso_left_inverse", "pro_isomorphisms", "pro_isomorphisms.csv", "left_inverse_defect_zero"),
    RequiredObligation("pro_iso_right_inverse", "pro_isomorphisms", "pro_isomorphisms.csv", "right_inverse_defect_zero"),
    RequiredObligation("pro_iso_presentation_independence", "pro_isomorphisms", "pro_isomorphisms.csv", "finite_presentation_independence"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check the Dirac-Igusa pro-object morphism obstruction ledger."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="morphism fixture directory")
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
    if manifest.get("morphism_kind") != EXPECTED_MORPHISM_KIND:
        issues.append(
            "morphism manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("morphism manifest does not mark empty_blocked=true")
    if manifest.get("certified") is not False:
        issues.append("morphism manifest must keep certified=false")
    for key in ("scalar_only", "product_only"):
        if manifest.get(key) is True:
            issues.append(f"morphism manifest marks {key}=true")


def check_core_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_EMPTY_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing morphism table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"morphism table {table_name} now has data rows; "
                "the obstruction ledger must be retired or narrowed"
            )


def check_scalar_firewall(fixture: Path, issues: list[str]) -> None:
    path = fixture / "scalar_firewall.csv"
    if not path.is_file():
        issues.append("missing morphism scalar_firewall.csv")
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
    extra = sorted(set(by_type) - REQUIRED_FIREWALL_TYPES)
    if missing:
        issues.append("scalar_firewall.csv missing firewall_type rows: " + ",".join(missing))
    if extra:
        issues.append("scalar_firewall.csv has unexpected firewall_type rows: " + ",".join(extra))
    for firewall_type, row in by_type.items():
        if row.get("excluded_from_morphism", "").lower() != "true":
            issues.append(f"{firewall_type}: excluded_from_morphism is not true")
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
        if row.get("pro_object_status") != "missing_open_obligation":
            issues.append(
                f"{obligation_id}: pro_object_status is not missing_open_obligation"
            )
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"morphism fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_core_tables_are_empty(fixture, issues)
    check_scalar_firewall(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "MORPHISM_OBSTRUCTION_LEDGER_FAILED"
    print("Dirac-Igusa pro-object morphism obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("pro_object_certification: false")
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
