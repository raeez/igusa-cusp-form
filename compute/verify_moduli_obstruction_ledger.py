#!/usr/bin/env python3
"""Verify the finite K3xE moduli obstruction ledger.

This verifier certifies only the residual absence ledger for the
retained finite-moduli and d-critical/cosection atlas packet.  It checks
that the finite-moduli fixture is still blocked after the bounded HN
type, finite-type semistable-substack, quasi-smooth
derived-enhancement, scalar rigidification, finite residual inertia,
finite class-bound, universal-complex, and E-translation
rigidification rows, retained closed-substack rows, retained
extension-closure rows, retained HN-factor-closure rows, and retained
dual-closure rows have been supplied, that all remaining stack and
atlas tables have no rows, and that every missing moduli artifact is recorded in
blocked_obligations.csv.

It does not construct extension/flag stacks, the cosection atlas,
transitions, or the finite Hall stage.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "MODULI_OBSTRUCTION_LEDGER_VERIFIED"
MANIFEST_NAME = "manifest.json"
OBLIGATION_FILE = "blocked_obligations.csv"
EXPECTED_MODULI_KIND = "retained_dual_closure_partial_blocked"
POPULATED_TABLES = (
    "hn_type_bounds.csv",
    "semistable_substacks.csv",
    "derived_enhancements.csv",
    "universal_complexes.csv",
    "scalar_rigidifications.csv",
    "e_translation_rigidifications.csv",
    "stratifications.csv",
    "extension_closure.csv",
    "hn_factor_closure.csv",
    "dual_closure.csv",
)
EXPECTED_EMPTY_TABLES = (
    "extension_flag_stacks.csv",
    "cosection_atlas.csv",
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
    "moduli_status",
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
    RequiredObligation("extension_stack", "extension_flag", "extension_flag_stacks.csv", "extension_stack"),
    RequiredObligation("two_step_flag_stack", "extension_flag", "extension_flag_stacks.csv", "two_step_flag_stack"),
    RequiredObligation("flag_properness", "extension_flag", "extension_flag_stacks.csv", "proper_status"),
    RequiredObligation("flag_finite_type", "extension_flag", "extension_flag_stacks.csv", "finite_type_status"),
    RequiredObligation("flag_quasi_smooth", "extension_flag", "extension_flag_stacks.csv", "quasi_smooth_status"),
    RequiredObligation("flag_subquotient_closure", "extension_flag", "extension_flag_stacks.csv", "subquotient_closure"),
    RequiredObligation("flag_properness_defect", "extension_flag", "extension_flag_stacks.csv", "properness_defect"),
    RequiredObligation("dcritical_chart", "cosection_atlas", "cosection_atlas.csv", "dcritical_chart"),
    RequiredObligation("semiregularity_cosection", "cosection_atlas", "cosection_atlas.csv", "semiregularity_cosection"),
    RequiredObligation("vanishing_cycle", "cosection_atlas", "cosection_atlas.csv", "vanishing_cycle"),
    RequiredObligation("orientation_line", "cosection_atlas", "cosection_atlas.csv", "orientation_line"),
    RequiredObligation("cosection_surjectivity", "cosection_atlas", "cosection_atlas.csv", "cosection_surjectivity"),
    RequiredObligation("dcritical_compatibility", "cosection_atlas", "cosection_atlas.csv", "dcritical_compatibility"),
    RequiredObligation("orientation_defect", "cosection_atlas", "cosection_atlas.csv", "orientation_defect"),
    RequiredObligation("transition_morphism", "transition", "transitions.csv", "transition_morphism"),
    RequiredObligation("transition_proper_or_closed", "transition", "transitions.csv", "proper_or_closed"),
    RequiredObligation("transition_strict", "transition", "transitions.csv", "strict_transition"),
    RequiredObligation("transition_mittag_leffler", "transition", "transitions.csv", "mittag_leffler"),
    RequiredObligation("transition_composition", "transition", "transitions.csv", "composition_defect"),
    RequiredObligation("transition_r1lim", "transition", "transitions.csv", "r1lim_zero"),
    RequiredObligation("firewall_formal_charge_window", "scalar_firewall", "scalar_firewall.csv", "formal_charge_window"),
    RequiredObligation("firewall_hilbert_scheme_scalar", "scalar_firewall", "scalar_firewall.csv", "hilbert_scheme_scalar"),
    RequiredObligation("firewall_liu_stability_only", "scalar_firewall", "scalar_firewall.csv", "liu_stability_only"),
    RequiredObligation("firewall_pfaffian_product", "scalar_firewall", "scalar_firewall.csv", "pfaffian_product"),
    RequiredObligation("firewall_target_window", "scalar_firewall", "scalar_firewall.csv", "target_window"),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check the finite-moduli obstruction ledger.")
    parser.add_argument("--fixture", required=True, type=Path, help="finite-moduli fixture directory")
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
    if manifest.get("moduli_kind") != EXPECTED_MODULI_KIND:
        issues.append(
            "moduli manifest is not the retained dual-closure partial scaffold; "
            "retire or revise blocked_obligations.csv"
        )
    if manifest.get("empty_blocked") is not False:
        issues.append("moduli manifest does not mark empty_blocked=false")
    if manifest.get("bounded_hn_types") is not True:
        issues.append("moduli manifest does not mark bounded_hn_types=true")
    if manifest.get("finite_type_semistable_substacks") is not True:
        issues.append("moduli manifest does not mark finite_type_semistable_substacks=true")
    if manifest.get("quasi_smooth_derived_enhancements") is not True:
        issues.append("moduli manifest does not mark quasi_smooth_derived_enhancements=true")
    if manifest.get("scalar_rigidifications") is not True:
        issues.append("moduli manifest does not mark scalar_rigidifications=true")
    if manifest.get("finite_residual_inertia_after_rigidification") is not True:
        issues.append("moduli manifest does not mark finite_residual_inertia_after_rigidification=true")
    if manifest.get("finite_class_set") is not True:
        issues.append("moduli manifest does not mark finite_class_set=true")
    if manifest.get("hilbert_polynomial_bounds") is not True:
        issues.append("moduli manifest does not mark hilbert_polynomial_bounds=true")
    if manifest.get("cohomological_amplitude_bounds") is not True:
        issues.append("moduli manifest does not mark cohomological_amplitude_bounds=true")
    if manifest.get("finite_regularity_bounds") is not True:
        issues.append("moduli manifest does not mark finite_regularity_bounds=true")
    if manifest.get("universal_complexes") is not True:
        issues.append("moduli manifest does not mark universal_complexes=true")
    if manifest.get("e_translation_rigidifications") is not True:
        issues.append("moduli manifest does not mark e_translation_rigidifications=true")
    if manifest.get("retained_closed_substacks") is not True:
        issues.append("moduli manifest does not mark retained_closed_substacks=true")
    if manifest.get("finite_closed_cover") is not True:
        issues.append("moduli manifest does not mark finite_closed_cover=true")
    if manifest.get("finite_inertia_stratifications") is not True:
        issues.append("moduli manifest does not mark finite_inertia_stratifications=true")
    if manifest.get("extension_closure") is not True:
        issues.append("moduli manifest does not mark extension_closure=true")
    if manifest.get("hn_factor_closure") is not True:
        issues.append("moduli manifest does not mark hn_factor_closure=true")
    if manifest.get("dual_closure") is not True:
        issues.append("moduli manifest does not mark dual_closure=true")
    for key in ("scalar_only", "target_only", "liu_stability_only"):
        if manifest.get(key) is True:
            issues.append(f"moduli manifest marks {key}=true")


def check_tables_state(fixture: Path, issues: list[str]) -> None:
    for table_name in POPULATED_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing populated moduli table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if not rows:
            issues.append(f"populated moduli table {table_name} has no data rows")
    for table_name in EXPECTED_EMPTY_TABLES:
        path = fixture / table_name
        if not path.is_file():
            issues.append(f"missing moduli table: {table_name}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            rows = nonempty_rows(csv.DictReader(handle))
        if rows:
            issues.append(
                f"moduli table {table_name} now has data rows; "
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
        if row.get("moduli_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: moduli_status is not missing_open_obligation")
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.is_dir():
        return False, [f"finite-moduli fixture directory does not exist: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_tables_state(fixture, issues)
    rows = load_obligations(fixture, issues)
    check_obligations(rows, issues)
    return not issues, issues


def print_report(fixture: Path, ok: bool, issues: list[str]) -> None:
    status = SUCCESS_STATUS if ok else "MODULI_OBSTRUCTION_LEDGER_FAILED"
    print("finite K3xE moduli obstruction ledger verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print("moduli_certification: false")
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
