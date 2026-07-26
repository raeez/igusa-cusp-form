#!/usr/bin/env python3
"""Verify the O2 wall-atlas obstruction ledger.

This verifier certifies only the absence ledger for the retained
type-II wall-atlas packet.  It checks that the O2 fixture is still the
empty blocked scaffold, that its required tables have no rows, and that
every missing wall-atlas artifact is recorded in blocked_obligations.csv.

It does not prove the O2 wall-normal-form theorem.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "O2_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_O2_KIND = "mock_empty_blocked"
EXPECTED_TABLES = (
    "wall_objects.csv",
    "wall_charts.csv",
    "overlaps.csv",
    "orbit_transport.csv",
    "half_hilbert_orbit.csv",
    "compatibilities.csv",
    "scalar_separation.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "rank_or_scalar_payload",
    "why_required",
    "o2_status",
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
    RequiredObligation("simple_wall_coverage", "wall_object", "wall_objects.csv", "simple_type_ii_wall_coverage"),
    RequiredObligation("charge_match", "wall_object", "wall_objects.csv", "charge_match"),
    RequiredObligation("wall_semistability", "wall_object", "wall_objects.csv", "semistability"),
    RequiredObligation("self_ext_splitting", "wall_object", "wall_objects.csv", "self_ext_splitting"),
    RequiredObligation("rank_one_block", "wall_object", "wall_objects.csv", "rank_one_block"),
    RequiredObligation("invariant_unit", "wall_object", "wall_objects.csv", "invariant_unit"),
    RequiredObligation("quotient_orientation", "wall_object", "wall_objects.csv", "quotient_orientation"),
    RequiredObligation("middle_wall_wrapped_object", "wall_object", "wall_objects.csv", "wrapped_wall_object"),
    RequiredObligation("chart_coordinate", "wall_chart", "wall_charts.csv", "normal_coordinate"),
    RequiredObligation("chart_tangent_pfaffian_line", "wall_chart", "wall_charts.csv", "tangent_pfaffian_line"),
    RequiredObligation("chart_normal_rank", "wall_chart", "wall_charts.csv", "normal_rank"),
    RequiredObligation("chart_divisor_order", "wall_chart", "wall_charts.csv", "divisor_order"),
    RequiredObligation("chart_unit_invariant", "wall_chart", "wall_charts.csv", "unit_invariant"),
    RequiredObligation("chart_reflection_flip", "wall_chart", "wall_charts.csv", "reflection_flip"),
    RequiredObligation("chart_local_sign", "wall_chart", "wall_charts.csv", "local_sign"),
    RequiredObligation("overlap_transition", "overlap", "overlaps.csv", "transition_isomorphism"),
    RequiredObligation("overlap_cech_cocycle", "overlap", "overlaps.csv", "cech_2cocycle"),
    RequiredObligation("overlap_cochain", "overlap", "overlaps.csv", "cochain"),
    RequiredObligation("overlap_coboundary", "overlap", "overlaps.csv", "coboundary_defect"),
    RequiredObligation("overlap_unit", "overlap", "overlaps.csv", "unit_overlap_defect"),
    RequiredObligation("overlap_orientation", "overlap", "overlaps.csv", "orientation_overlap_defect"),
    RequiredObligation("transport_weyl_lift", "orbit_transport", "orbit_transport.csv", "weyl_lift"),
    RequiredObligation("transport_orientation", "orbit_transport", "orbit_transport.csv", "orientation_transport"),
    RequiredObligation("transport_pfaffian", "orbit_transport", "orbit_transport.csv", "pfaffian_transport"),
    RequiredObligation("transport_rank", "orbit_transport", "orbit_transport.csv", "rank_preservation"),
    RequiredObligation("transport_sign", "orbit_transport", "orbit_transport.csv", "sign_preservation"),
    RequiredObligation("half_hilbert_coordinates", "half_hilbert_orbit", "half_hilbert_orbit.csv", "binary_coordinates"),
    RequiredObligation("half_hilbert_cardinality", "half_hilbert_orbit", "half_hilbert_orbit.csv", "orbit_cardinality"),
    RequiredObligation("half_hilbert_components", "half_hilbert_orbit", "half_hilbert_orbit.csv", "component_coverage"),
    RequiredObligation("half_hilbert_boundaries", "half_hilbert_orbit", "half_hilbert_orbit.csv", "boundary_coverage"),
    RequiredObligation("half_hilbert_sign_matrix", "half_hilbert_orbit", "half_hilbert_orbit.csv", "sign_assignment_matrix"),
    RequiredObligation("half_hilbert_coverage_defect", "half_hilbert_orbit", "half_hilbert_orbit.csv", "coverage_defect"),
    RequiredObligation("compat_boundary", "compatibility", "compatibilities.csv", "boundary"),
    RequiredObligation("compat_component", "compatibility", "compatibilities.csv", "component"),
    RequiredObligation("compat_hn_transition", "compatibility", "compatibilities.csv", "hn_transition"),
    RequiredObligation("compat_protected_integration", "compatibility", "compatibilities.csv", "protected_integration"),
    RequiredObligation("compat_quotient_orientation", "compatibility", "compatibilities.csv", "quotient_orientation"),
    RequiredObligation("compat_thom_sebastiani", "compatibility", "compatibilities.csv", "thom_sebastiani"),
    RequiredObligation("compat_weyl_lift", "compatibility", "compatibilities.csv", "weyl_lift"),
    RequiredObligation("compat_type_i_exclusion", "compatibility", "compatibilities.csv", "type_i_exclusion"),
    RequiredObligation("compat_d0_limit", "compatibility", "compatibilities.csv", "d0_limit_extension"),
    RequiredObligation("scalar_maass_firewall", "scalar_separation", "scalar_separation.csv", "maass_character_not_atlas"),
    RequiredObligation("scalar_op_firewall", "scalar_separation", "scalar_separation.csv", "op_scalar_not_orientation"),
    RequiredObligation("scalar_theta_firewall", "scalar_separation", "scalar_separation.csv", "wall_count_vs_squared_theta_leading"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the O2 wall-atlas obstruction ledger.")
    parser.add_argument("--fixture", required=True, type=Path, help="O2 wall-atlas fixture directory")
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
    if manifest.get("o2_atlas_kind") != EXPECTED_O2_KIND:
        issues.append(
            "O2 manifest is no longer the blocked scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not True:
        issues.append("O2 manifest does not mark empty_blocked=true")
    if manifest.get("local_only") is True:
        issues.append("O2 manifest marks local-only data")
    if manifest.get("scalar_only") is True:
        issues.append("O2 manifest marks scalar-only data")
    if manifest.get("op_scalar_only") is True:
        issues.append("O2 manifest marks OP-scalar-only data")


def check_tables_are_empty(fixture: Path, issues: list[str]) -> None:
    for table_name in EXPECTED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing O2 table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"O2 table {table_name} now has data rows; "
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
        if row.get("o2_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: o2_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"O2 fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_are_empty(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "O2_OBSTRUCTION_LEDGER_FAILED"
    print("O2 wall-atlas obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("o2_certification: false")
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
