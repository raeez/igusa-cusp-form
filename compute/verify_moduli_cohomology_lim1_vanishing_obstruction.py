#!/usr/bin/env python3
"""Verify the moduli-cohomology lim1 obstruction ledger.

This fail-closed verifier records the data missing from the proof that
R^1 lim vanishes on retained moduli cohomology towers.  A positive
result means the obstruction ledger is complete and the core cohomology
and Mittag-Leffler tables remain empty; it does not prove lim1
vanishing.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "MODULI_COHOMOLOGY_LIM1_VANISHING_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "moduli_cohomology_lim1_vanishing_obstruction.v1"
EXPECTED_KIND = "moduli_cohomology_lim1_vanishing_obstruction"
EXPECTED_EMPTY_TABLES = (
    "coefficient_systems.csv",
    "cohomology_towers.csv",
    "cohomology_transition_maps.csv",
    "image_stabilization.csv",
    "ml_r1lim_defects.csv",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "lim1_status",
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
        "cofinal_hn_sequence",
        "moduli_stack_inputs",
        "transition_geometry_input",
        "coefficient_system_rows",
        "cohomology_group_rows",
        "finite_rank_rows",
        "cohomology_transition_maps",
        "transition_functoriality",
        "image_subspace_rows",
        "image_stabilization_witness",
        "strict_ml_status",
        "r1lim_zero_row",
        "degreewise_exhaustion",
        "no_scalar_lim1_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "finite_type_only",
        "proper_or_closed_only",
        "bounded_hn_types",
        "transition_geometry_only",
        "euler_characteristic",
        "scalar_trace",
        "protected_trace",
        "hilbert_scheme_scalar",
        "target_window",
        "formal_charge_window",
        "vanishing_cycle_transition_only",
        "orientation_transition_only",
        "empty_ml_status",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "coefficient_systems.csv",
        (
            "coefficient_system_id",
            "stage",
            "stack_kind",
            "coefficient_kind",
            "constructible_status",
            "transport_id",
            "finite_rank_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "cohomology_towers.csv",
        (
            "tower_id",
            "stage",
            "stack_kind",
            "coefficient_system_id",
            "cohomological_degree",
            "support_block_id",
            "cohomology_group_id",
            "finite_rank",
            "topology_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "cohomology_transition_maps.csv",
        (
            "transition_map_id",
            "tower_id",
            "from_stage",
            "to_stage",
            "moduli_transition_id",
            "cohomology_functor",
            "linear_map_id",
            "map_direction",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "image_stabilization.csv",
        (
            "stabilization_id",
            "tower_id",
            "base_stage",
            "witness_stage",
            "later_stage",
            "image_basis_id",
            "image_rank",
            "stabilization_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "ml_r1lim_defects.csv",
        (
            "defect_id",
            "tower_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "functoriality_defect_rank",
            "composition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check moduli-cohomology lim1 vanishing obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/moduli/moduli_cohomology_lim1_vanishing"),
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
        "fixture_name": "moduli_cohomology_lim1_vanishing",
        "moduli_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "lim1_vanishing_certification": False,
        "mathematical_certification": False,
        "finite_moduli_packet_imported": True,
        "transition_geometry_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected moduli-cohomology tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing moduli-cohomology table: {spec.path}")
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
                "until cohomology lim1 vanishing is proved"
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
        issues.append("missing moduli-cohomology obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected moduli-cohomology obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("lim1_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: lim1_status is not missing_open_obligation")
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
        print("MODULI_COHOMOLOGY_LIM1_VANISHING_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
