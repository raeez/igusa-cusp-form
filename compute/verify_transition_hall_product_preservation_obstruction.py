#!/usr/bin/env python3
"""Verify the transition-Hall-product preservation obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite-stage transition maps preserve the compact Hall product.  A
positive result means the obstruction ledger is complete and the core
transition tables remain empty; it does not prove Hall-product
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


SUCCESS_STATUS = "TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "transition_hall_product_preservation_obstruction.v1"
EXPECTED_KIND = "transition_hall_product_preservation_obstruction"
EXPECTED_EMPTY_TABLES = (
    "extension_correspondence_transitions.csv",
    "coefficient_transport.csv",
    "product_matrix_transport.csv",
    "base_change_projection.csv",
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
    "hall_product_status",
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
        "orientation_transition_input",
        "vanishing_cycle_transition_input",
        "source_product_matrix",
        "extension_correspondence_square",
        "input_product_stack_square",
        "output_product_stack_square",
        "coefficient_system_transport",
        "ts_product_transport",
        "proper_base_change",
        "projection_formula",
        "compact_support_pushforward",
        "product_matrix_intertwining",
        "associativity_transition_compatibility",
        "hall_product_mittag_leffler",
        "no_scalar_hall_product_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "scalar_trace",
        "denominator_product",
        "signed_multiplicities",
        "target_bkm_product",
        "pfaffian_product",
        "vanishing_cycle_transport_only",
        "orientation_transport_only",
        "abstract_bialgebra_matrix",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "extension_correspondence_transitions.csv",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "source_extension_stack_id",
            "target_extension_stack_id",
            "input_square_id",
            "output_square_id",
            "transition_graph_id",
            "extension_square_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "coefficient_transport.csv",
        (
            "transport_id",
            "transition_id",
            "orientation_transport_id",
            "vanishing_cycle_transport_id",
            "ts_product_transport_id",
            "coefficient_system_defect_rank",
            "ts_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "product_matrix_transport.csv",
        (
            "matrix_transport_id",
            "transition_id",
            "source_product_matrix_id",
            "target_product_matrix_id",
            "left_transition_matrix_id",
            "right_transition_matrix_id",
            "output_transition_matrix_id",
            "intertwining_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "base_change_projection.csv",
        (
            "compatibility_id",
            "transition_id",
            "proper_base_change_id",
            "projection_formula_id",
            "compact_support_pushforward_id",
            "base_change_defect_rank",
            "projection_formula_defect_rank",
            "compact_support_defect_rank",
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
            "correspondence_defect_rank",
            "coefficient_defect_rank",
            "base_change_defect_rank",
            "projection_formula_defect_rank",
            "product_intertwining_defect_rank",
            "associativity_transition_defect_rank",
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
        description="Check transition-Hall-product preservation obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hall/transition_hall_product_preservation"),
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
        "fixture_name": "transition_hall_product_preservation",
        "hall_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "hall_product_transition_certification": False,
        "mathematical_certification": False,
        "compact_hall_packet_imported": True,
        "transition_geometry_packet_imported": True,
        "orientation_transition_packet_imported": True,
        "vanishing_cycle_transition_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {"blocked_obligations.csv", "scalar_firewall.csv"}
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-Hall-product tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-Hall-product table: {spec.path}")
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
                "until Hall-product preservation is proved"
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
        issues.append("missing Hall-product obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected Hall-product obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("hall_product_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: hall_product_status is not missing_open_obligation")
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
        print("TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
