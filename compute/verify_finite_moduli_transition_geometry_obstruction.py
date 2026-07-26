#!/usr/bin/env python3
"""Verify the finite-moduli transition-geometry obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite K3xE moduli transitions are closed embeddings or proper maps.  A
positive result means the obstruction ledger is complete and the core
transition tables remain empty; it does not prove transition
properness, closedness, or the finite-stage inverse system.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "FINITE_MODULI_TRANSITION_GEOMETRY_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "finite_moduli_transition_geometry_obstruction.v1"
EXPECTED_KIND = "finite_moduli_transition_geometry_obstruction"
EXPECTED_EMPTY_TABLES = (
    "stack_transitions.csv",
    "component_geometry.csv",
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
    "transition_status",
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
        "transition_morphism_rows",
        "object_stack_component",
        "extension_stack_component",
        "two_step_flag_stack_component",
        "proper_or_closed_choice",
        "image_or_graph_closed",
        "finite_type_source_target",
        "retained_locus_compatibility",
        "base_change_compatibility",
        "composition_zero",
        "domain_transport_compatibility",
        "no_window_to_moduli_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "formal_charge_window",
        "target_root_window",
        "source_window_index",
        "semistable_rows_without_morphisms",
        "liu_stability_only",
        "pfaffian_product",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "stack_transitions.csv",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "source_stack_id",
            "target_stack_id",
            "transition_morphism_id",
            "stack_kind",
            "source_retained_closed_substack_id",
            "target_retained_closed_substack_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "component_geometry.csv",
        (
            "geometry_id",
            "transition_id",
            "component_kind",
            "morphism_id",
            "proper_status",
            "closed_embedding_status",
            "finite_type_status",
            "image_closed",
            "graph_closed",
            "properness_defect_rank",
            "closed_embedding_defect_rank",
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
            "composition_defect_rank",
            "base_change_defect_rank",
            "retained_locus_defect_rank",
            "stabilizer_defect_rank",
            "orientation_domain_defect_rank",
            "vanishing_cycle_domain_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite-moduli transition-geometry obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/moduli/finite_moduli_transition_geometry"),
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
        "fixture_name": "finite_moduli_transition_geometry",
        "moduli_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "transition_geometry_certification": False,
        "mathematical_certification": False,
        "finite_moduli_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {"blocked_obligations.csv", "scalar_firewall.csv"}
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-geometry tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-geometry table: {spec.path}")
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
                "until transition geometry is proved"
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
        issues.append("missing transition obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected transition obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("transition_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: transition_status is not missing_open_obligation")
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
        print("FINITE_MODULI_TRANSITION_GEOMETRY_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
