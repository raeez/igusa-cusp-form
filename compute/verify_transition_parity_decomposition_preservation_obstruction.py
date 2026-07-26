#!/usr/bin/env python3
"""Verify the transition-parity preservation obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite-stage transition maps preserve even and odd parity summands.  A
positive result means the obstruction ledger is complete and the core
transition tables remain empty; it does not prove parity preservation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "TRANSITION_PARITY_DECOMPOSITION_PRESERVATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "transition_parity_decomposition_preservation_obstruction.v1"
EXPECTED_KIND = "transition_parity_decomposition_preservation_obstruction"
EXPECTED_EMPTY_TABLES = (
    "parity_decomposition_rows.csv",
    "parity_involutions.csv",
    "parity_transition_matrices.csv",
    "parity_comparison_squares.csv",
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
    "parity_transition_status",
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
        "primitive_transition_input",
        "source_parity_blocks",
        "target_stage_parity_blocks",
        "source_parity_homogeneous_basis",
        "target_parity_homogeneous_basis",
        "source_fermion_parity_involution",
        "target_fermion_parity_involution",
        "ambient_transition_matrix",
        "parity_commutator_identity",
        "off_diagonal_zero_identity",
        "even_restricted_transition_matrix",
        "odd_restricted_transition_matrix",
        "negative_root_parity_transport",
        "comparison_parity_square",
        "parity_transition_composition",
        "no_scalar_parity_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "scalar_trace",
        "denominator_product",
        "signed_superdimension",
        "target_parity_table",
        "parity_rank_equality_only",
        "parity_pushforward_only",
        "primitive_transition_only",
        "radical_transition_only",
        "pbw_transition_only",
        "chevalley_antiinvolution_only",
        "hilbert_series_only",
        "abstract_super_vector_space",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "parity_decomposition_rows.csv",
        (
            "decomposition_id",
            "stage",
            "side",
            "degree_id",
            "space_id",
            "even_basis_id",
            "odd_basis_id",
            "even_rank",
            "odd_rank",
            "parity_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "parity_involutions.csv",
        (
            "involution_id",
            "stage",
            "space_id",
            "even_projection_id",
            "odd_projection_id",
            "fermion_parity_matrix_id",
            "idempotent_defect_rank",
            "split_sum_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "parity_transition_matrices.csv",
        (
            "parity_transition_id",
            "from_stage",
            "to_stage",
            "degree_id",
            "ambient_transition_matrix_id",
            "source_parity_involution_id",
            "target_parity_involution_id",
            "even_restricted_transition_id",
            "odd_restricted_transition_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "parity_comparison_squares.csv",
        (
            "comparison_square_id",
            "parity_transition_id",
            "comparison_map_id",
            "source_target_parity_map_id",
            "even_square_defect_rank",
            "odd_square_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "transition_defects.csv",
        (
            "defect_id",
            "parity_transition_id",
            "parity_commutator_defect_rank",
            "even_to_odd_defect_rank",
            "odd_to_even_defect_rank",
            "restricted_rank_defect",
            "comparison_square_defect_rank",
            "composition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check transition-parity preservation obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hall/transition_parity_decomposition_preservation"),
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
        "fixture_name": "transition_parity_decomposition_preservation",
        "hall_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "parity_transition_certification": False,
        "mathematical_certification": False,
        "compact_hall_packet_imported": True,
        "primitive_transition_packet_imported": True,
        "parity_pushforward_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-parity tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-parity table: {spec.path}")
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
                "until parity transition preservation is proved"
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
        issues.append("missing transition-parity obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected transition-parity obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("parity_transition_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: parity_transition_status is not missing_open_obligation")
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
        print("TRANSITION_PARITY_DECOMPOSITION_PRESERVATION_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
