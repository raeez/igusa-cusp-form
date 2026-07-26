#!/usr/bin/env python3
"""Verify the transition-PBW filtration preservation obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite-stage transition maps preserve PBW filtrations.  A positive
result means the obstruction ledger is complete and the core transition
tables remain empty; it does not prove PBW filtration preservation.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "TRANSITION_PBW_FILTRATION_PRESERVATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "transition_pbw_filtration_preservation_obstruction.v1"
EXPECTED_KIND = "transition_pbw_filtration_preservation_obstruction"
EXPECTED_EMPTY_TABLES = (
    "pbw_filtration_rows.csv",
    "ordered_word_bases.csv",
    "pbw_relation_rewrites.csv",
    "pbw_transition_matrices.csv",
    "associated_graded_transition.csv",
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
    "pbw_transition_status",
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
        "radical_quotient_transition_input",
        "source_pbw_filtration_rows",
        "target_pbw_filtration_rows",
        "associated_graded_rank_rows",
        "source_ordered_word_basis",
        "target_ordered_word_basis",
        "source_relation_rewrite_system",
        "target_relation_rewrite_system",
        "quotient_transition_matrix",
        "multiplicative_word_transition",
        "relation_rewrite_compatibility",
        "filtered_image_identity",
        "restricted_filtered_transition_matrix",
        "associated_graded_transition_matrix",
        "pbw_symbol_intertwining_identity",
        "a_beta_pbw_transition_square",
        "pbw_transition_composition",
        "no_scalar_pbw_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "scalar_trace",
        "denominator_product",
        "signed_multiplicities",
        "target_pbw_table",
        "pbw_rank_equality_only",
        "pbw_pushforward_only",
        "primitive_transition_only",
        "radical_transition_only",
        "hilbert_series_only",
        "abstract_associated_graded_matrix",
        "bar_length_filtration",
        "normal_ordered_degree_map",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "pbw_filtration_rows.csv",
        (
            "filtration_id",
            "stage",
            "side",
            "degree_id",
            "parity",
            "pbw_level",
            "ordered_word_basis_id",
            "filtered_piece_rank",
            "associated_graded_rank",
            "quotient_basis_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "ordered_word_bases.csv",
        (
            "word_basis_id",
            "stage",
            "side",
            "pbw_level",
            "ordered_generator_basis_id",
            "word_count",
            "relation_rewrite_system_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "pbw_relation_rewrites.csv",
        (
            "rewrite_id",
            "stage",
            "side",
            "relation_ideal_id",
            "ordered_word_basis_id",
            "normal_form_algorithm_id",
            "confluence_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "pbw_transition_matrices.csv",
        (
            "pbw_transition_id",
            "from_stage",
            "to_stage",
            "side",
            "quotient_transition_matrix_id",
            "multiplicative_word_transition_id",
            "filtered_level",
            "source_filtered_basis_id",
            "target_filtered_basis_id",
            "restricted_transition_matrix_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "associated_graded_transition.csv",
        (
            "graded_transition_id",
            "pbw_transition_id",
            "source_graded_basis_id",
            "target_graded_basis_id",
            "associated_graded_matrix_id",
            "symbol_intertwining_defect_rank",
            "a_beta_square_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "transition_defects.csv",
        (
            "defect_id",
            "pbw_transition_id",
            "relation_rewrite_defect_rank",
            "filtered_image_defect_rank",
            "rank_defect",
            "symbol_intertwining_defect_rank",
            "a_beta_square_defect_rank",
            "composition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check transition-PBW filtration preservation obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hall/transition_pbw_filtration_preservation"),
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
        "fixture_name": "transition_pbw_filtration_preservation",
        "hall_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "pbw_transition_certification": False,
        "mathematical_certification": False,
        "compact_hall_packet_imported": True,
        "radical_transition_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-PBW tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-PBW table: {spec.path}")
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
                "until PBW transition preservation is proved"
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
        issues.append("missing transition-PBW obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected transition-PBW obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("pbw_transition_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: pbw_transition_status is not missing_open_obligation")
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
        print("TRANSITION_PBW_FILTRATION_PRESERVATION_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
