#!/usr/bin/env python3
"""Verify the transition-orientation preservation obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite-stage transition maps preserve Joyce--Upmeier orientations.  A
positive result means the obstruction ledger is complete and the core
transport tables remain empty; it does not prove orientation
preservation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "transition_orientation_preservation_obstruction.v1"
EXPECTED_KIND = "transition_orientation_preservation_obstruction"
EXPECTED_EMPTY_TABLES = (
    "orientation_transition_maps.csv",
    "null_trivialization_transport.csv",
    "multiplicative_weyl_transport.csv",
    "transition_defects.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "orientation_transition_status",
    "proof_reference",
    "check_status",
    "notes",
)
SCALAR_FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "transition_geometry_input",
        "orientation_line_pullback",
        "determinant_square_commutes",
        "reduced_gerbe_trivialization_transport",
        "free_e_trivialization_transport",
        "finite_stabilizer_trivialization_transport",
        "linearization_transport",
        "ts_transition_compatibility",
        "weyl_lift_transition_compatibility",
        "coxeter_cochain_transition",
        "strict_picard_groupoid_transition",
        "orientation_mittag_leffler",
        "no_scalar_orientation_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "scalar_trace",
        "squared_determinant",
        "op_scalar_branch",
        "maass_character_value",
        "pfaffian_product",
        "moduli_transition_geometry_only",
        "target_root_window",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "orientation_transition_maps.csv",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "stack_transition_id",
            "source_orientation_line_id",
            "target_orientation_line_id",
            "pullback_isomorphism_id",
            "determinant_square_id",
            "square_commutes",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "null_trivialization_transport.csv",
        (
            "transport_id",
            "transition_id",
            "reduced_gerbe_trivialization_id",
            "free_e_trivialization_id",
            "finite_stabilizer_trivialization_id",
            "linearization_transport_id",
            "quotient_borel_defect_rank",
            "linearization_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "multiplicative_weyl_transport.csv",
        (
            "transport_id",
            "transition_id",
            "ts_transport_id",
            "weyl_lift_transport_id",
            "coxeter_cochain_transport_id",
            "ts_transition_defect_rank",
            "weyl_transition_defect_rank",
            "coxeter_transition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "transition_defects.csv",
        (
            "defect_id",
            "transition_id",
            "picard_groupoid_defect_rank",
            "square_root_defect_rank",
            "null_trivialization_defect_rank",
            "ts_defect_rank",
            "weyl_defect_rank",
            "composition_defect_rank",
            "r1lim_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check transition-orientation preservation obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/orientation/transition_orientation_preservation"),
    )
    parser.add_argument("--check", action="store_true")
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


def read_json(path: Path, issues: list[str]) -> dict[str, object]:
    if not path.is_file():
        issues.append(f"missing JSON file: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {path}")
        return {}
    return value


def check_manifest(fixture: Path, issues: list[str]) -> None:
    readme = fixture / README_NAME
    if not readme.is_file() or not readme.read_text(encoding="utf-8").strip():
        issues.append(f"missing nonempty README: {readme}")
    manifest = read_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "transition_orientation_preservation",
        "orientation_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "orientation_transition_certification": False,
        "mathematical_certification": False,
        "orientation_packet_imported": True,
        "transition_geometry_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {"blocked_obligations.csv", "scalar_firewall.csv"}
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-orientation tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-orientation table: {spec.path}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if tuple(reader.fieldnames or ()) != spec.columns:
                issues.append(f"{spec.path}: header mismatch")
                continue
            rows = nonempty_rows(reader)
        if rows:
            issues.append(
                f"{spec.path}: obstruction packet must keep core table empty "
                "until orientation preservation is proved"
            )


def check_obligations(fixture: Path, issues: list[str]) -> None:
    path = fixture / "blocked_obligations.csv"
    if not path.is_file():
        issues.append("missing blocked_obligations.csv")
        return
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != OBLIGATION_COLUMNS:
            issues.append("blocked_obligations.csv header mismatch")
            return
        rows = nonempty_rows(reader)
    by_id = {row["obligation_id"]: row for row in rows}
    missing = REQUIRED_OBLIGATIONS - set(by_id)
    extra = set(by_id) - REQUIRED_OBLIGATIONS
    if missing:
        issues.append("missing orientation-transition obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected orientation-transition obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("orientation_transition_status") != "missing_open_obligation":
            issues.append(
                f"{obligation_id}: orientation_transition_status is not missing_open_obligation"
            )
        if row.get("check_status") != "verified":
            issues.append(f"{obligation_id}: check_status is not verified")
        if not row.get("mathematical_payload") or not row.get("why_required"):
            issues.append(f"{obligation_id}: missing payload or reason")


def check_scalar_firewall(fixture: Path, issues: list[str]) -> None:
    path = fixture / "scalar_firewall.csv"
    if not path.is_file():
        issues.append("missing scalar_firewall.csv")
        return
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != SCALAR_FIREWALL_COLUMNS:
            issues.append("scalar_firewall.csv header mismatch")
            return
        rows = nonempty_rows(reader)
    by_substitute = {row["forbidden_substitute"]: row for row in rows}
    missing = REQUIRED_FIREWALL_ROWS - set(by_substitute)
    extra = set(by_substitute) - REQUIRED_FIREWALL_ROWS
    if missing:
        issues.append("missing firewall rows: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected firewall rows: " + ", ".join(sorted(extra)))
    for substitute, row in by_substitute.items():
        if row.get("excluded") != "true":
            issues.append(f"{substitute}: excluded is not true")
        if row.get("defect_rank") != "0":
            issues.append(f"{substitute}: defect_rank is not zero")
        if row.get("check_status") != "verified":
            issues.append(f"{substitute}: check_status is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    issues: list[str] = []
    check_manifest(args.fixture, issues)
    check_empty_tables(args.fixture, issues)
    check_obligations(args.fixture, issues)
    check_scalar_firewall(args.fixture, issues)
    if issues:
        print("TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
