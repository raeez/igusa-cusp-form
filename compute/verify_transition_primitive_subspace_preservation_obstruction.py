#!/usr/bin/env python3
"""Verify the transition-primitive-subspace preservation obstruction ledger.

This fail-closed verifier records the data missing from the proof that
finite-stage transition maps preserve the primitive Hall subspaces.  A
positive result means the obstruction ledger is complete and the core
transition tables remain empty; it does not prove preservation of
primitive subspaces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "transition_primitive_subspace_preservation_obstruction.v1"
EXPECTED_KIND = "transition_primitive_subspace_preservation_obstruction"
EXPECTED_EMPTY_TABLES = (
    "primitive_kernel_rows.csv",
    "primitive_transition_matrices.csv",
    "kernel_intertwining.csv",
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
    "primitive_transition_status",
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
        "source_hall_coproduct_matrix",
        "target_hall_coproduct_matrix",
        "source_counit_map",
        "target_counit_map",
        "source_reduced_coproduct_matrix",
        "target_reduced_coproduct_matrix",
        "source_primitive_kernel",
        "target_primitive_kernel",
        "ambient_transition_matrix",
        "hall_coproduct_transition_input",
        "counit_transition_compatibility",
        "kernel_intertwining_identity",
        "primitive_projection_matrix",
        "primitive_restricted_transition_matrix",
        "primitive_transition_composition",
        "no_scalar_primitive_subspace_substitution",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "scalar_trace",
        "denominator_product",
        "signed_multiplicities",
        "target_bkm_root_space",
        "bar_coalgebra_primitives",
        "hall_product_preservation",
        "hall_coproduct_preservation_without_kernels",
        "normal_ordered_degree_map",
        "abstract_kernel_matrix",
        "primitive_rank_only",
    }
)


@dataclass(frozen=True)
class EmptyTableSpec:
    path: str
    columns: tuple[str, ...]


EMPTY_TABLE_SPECS: tuple[EmptyTableSpec, ...] = (
    EmptyTableSpec(
        "primitive_kernel_rows.csv",
        (
            "kernel_id",
            "stage",
            "hall_space_id",
            "reduced_coproduct_matrix_id",
            "counit_matrix_id",
            "primitive_basis_id",
            "primitive_projection_id",
            "kernel_rank",
            "ambient_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "primitive_transition_matrices.csv",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "ambient_transition_matrix_id",
            "source_primitive_basis_id",
            "target_primitive_basis_id",
            "restricted_transition_matrix_id",
            "source_inclusion_id",
            "target_inclusion_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    EmptyTableSpec(
        "kernel_intertwining.csv",
        (
            "intertwining_id",
            "transition_id",
            "source_reduced_coproduct_id",
            "target_reduced_coproduct_id",
            "source_counit_id",
            "target_counit_id",
            "tensor_transition_id",
            "reduced_coproduct_intertwining_defect_rank",
            "counit_intertwining_defect_rank",
            "primitive_image_defect_rank",
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
            "kernel_rank_defect",
            "primitive_image_defect_rank",
            "projection_commutator_defect_rank",
            "composition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check transition-primitive-subspace preservation obstruction ledger."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hall/transition_primitive_subspace_preservation"),
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
        "fixture_name": "transition_primitive_subspace_preservation",
        "hall_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "primitive_transition_certification": False,
        "mathematical_certification": False,
        "compact_hall_packet_imported": True,
        "hall_coproduct_transition_packet_imported": True,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EXPECTED_EMPTY_TABLES) | {"blocked_obligations.csv", "scalar_firewall.csv"}
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected transition-primitive-subspace tables")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for spec in EMPTY_TABLE_SPECS:
        path = fixture / spec.path
        if not path.is_file():
            issues.append(f"missing transition-primitive-subspace table: {spec.path}")
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
                "until primitive-subspace preservation is proved"
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
        issues.append("missing primitive-transition obligations: " + ", ".join(sorted(missing)))
    if extra:
        issues.append("unexpected primitive-transition obligations: " + ", ".join(sorted(extra)))
    for obligation_id, row in by_id.items():
        if row.get("primitive_transition_status") != "missing_open_obligation":
            issues.append(f"{obligation_id}: primitive_transition_status is not missing_open_obligation")
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
        print("TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_FAILED", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
