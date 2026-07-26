#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for compact-source packets.

This script is source-side only. It may read the path of a target
reference fixture, but it never computes, derives, or writes target truth.
A positive result is SCHEMA_COMPLETE_SCHEMA_ONLY: the manifest kind,
table schemas, row payloads, row statuses, target-reference separation,
target-label firewall, and source-degree firewall passed. It is not
compact-source certification, nor is it external mathematical
verification.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCHEMA_COMPLETE_SOURCE_KIND = "compact_source_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
TARGET_MANIFEST_NAME = "manifest.yaml"
TARGET_HASH_FILE = "hashes.sha256"
TARGET_HASHED_FILENAMES = (
    "manifest.yaml",
    "target_degrees.csv",
    "target_simple_generators.csv",
    "target_hall_lie_basis.csv",
    "target_relation_rows.csv",
    "target_pairing_blocks.csv",
    "target_radicals.csv",
    "target_dimensions.csv",
    "target_pbw.csv",
)
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "source_block_status",
        "window_status",
        "strict_pbw_status",
        "ml_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "signed_only",
        "status_only",
        "target_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_SOURCE_BLOCK_STATUSES = frozenset(
    {"source_verified", "source_admissible"}
)
ACCEPTABLE_SECONDARY_STATUSES = {
    "window_status": frozenset({"window_verified", "verified"}),
    "strict_pbw_status": frozenset({"strict_pbw_verified", "verified"}),
    "strict_status": frozenset({"strict_verified", "verified"}),
    "ml_status": frozenset({"ml_verified", "verified"}),
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    gate: str
    columns: tuple[str, ...]
    require_rows: bool = True


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "degrees.csv",
        "window degrees",
        (
            "degree_id",
            "c1",
            "c2",
            "c3",
            "sign",
            "in_window",
            "source_block_status",
            "target_reference_id",
            "geometric_source_id",
            "proof_reference",
            "notes",
        ),
    ),
    TableSpec(
        "parity_blocks.csv",
        "parity blocks",
        (
            "degree_id",
            "parity",
            "source_rank",
            "target_rank",
            "parity_source",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "basis_provenance.csv",
        "compact-source provenance",
        (
            "source_basis_id",
            "degree_id",
            "parity",
            "retained_charge_lift",
            "source_stack_or_stratum",
            "vanishing_cycle_or_ic_summand",
            "reduced_orientation",
            "quotient_orientation",
            "ts_transport",
            "finite_stabilizer_linearization",
            "protected_integration",
            "transition_compatibility",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "simple_representatives.csv",
        "simple primitive representatives",
        (
            "row_id",
            "representative_role",
            "degree_id",
            "parity",
            "source_basis_id",
            "cartan_basis_id",
            "target_reference_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "M_entries.csv",
        "Hall product M",
        (
            "row_id",
            "alpha_degree_id",
            "beta_degree_id",
            "target_degree_id",
            "row_source_basis_id",
            "column_left_basis_id",
            "column_right_basis_id",
            "value",
            "coefficient_ring",
            "source_correspondence_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "D_entries.csv",
        "source coproduct D",
        (
            "row_id",
            "source_degree_id",
            "mu_degree_id",
            "nu_degree_id",
            "row_left_basis_id",
            "row_right_basis_id",
            "column_source_basis_id",
            "value",
            "coefficient_ring",
            "source_correspondence_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "unit_counit.csv",
        "Hall unit and counit",
        (
            "row_id",
            "map_type",
            "degree_id",
            "domain_basis_id",
            "codomain_basis_id",
            "value",
            "coefficient_ring",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "B_entries.csv",
        "source bracket B",
        (
            "row_id",
            "alpha_degree_id",
            "beta_degree_id",
            "target_degree_id",
            "row_source_basis_id",
            "column_left_basis_id",
            "column_right_basis_id",
            "value",
            "coefficient_ring",
            "derived_from_M_row_ids",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "G_entries.csv",
        "Hopf pairing G",
        (
            "row_id",
            "degree_id",
            "parity",
            "positive_basis_id",
            "negative_basis_id",
            "value",
            "coefficient_ring",
            "pairing_correspondence_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hopf_pairing_identities.csv",
        "Hopf pairing adjointness and Frobenius identities",
        (
            "check_id",
            "identity_type",
            "degree_ids",
            "parity",
            "source_matrix_ids",
            "pairing_entry_ids",
            "left_matrix_id",
            "right_matrix_id",
            "defect_rank",
            "quotient_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "K_entries.csv",
        "radical kernel K",
        (
            "row_id",
            "degree_id",
            "parity",
            "kernel_basis_id",
            "source_basis_id",
            "value",
            "coefficient_ring",
            "radical_check_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "Q_entries.csv",
        "quotient splitting Q",
        (
            "row_id",
            "degree_id",
            "parity",
            "quotient_basis_id",
            "source_basis_id",
            "value",
            "coefficient_ring",
            "splitting_check_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "A_entries.csv",
        "source-to-target map A",
        (
            "row_id",
            "degree_id",
            "parity",
            "quotient_basis_id",
            "target_basis_id",
            "value",
            "coefficient_ring",
            "comparison_source_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hall_bialgebra_identities.csv",
        "Hall bialgebra identities",
        (
            "check_id",
            "identity_type",
            "degree_ids",
            "source_matrix_ids",
            "unit_counit_row_ids",
            "left_matrix_id",
            "right_matrix_id",
            "defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "radical_ideal_coideal.csv",
        "radical ideal/coideal identities",
        (
            "check_id",
            "degree_id",
            "parity",
            "identity",
            "source_matrix_ids",
            "left_rank",
            "right_rank",
            "combined_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "relation_rows.csv",
        "BK/GN relation rows",
        (
            "row_id",
            "relation_type",
            "terminal_degree_id",
            "source_matrix_ids",
            "window_status",
            "rank_or_value",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "no_extra.csv",
        "no-extra kernel equality",
        (
            "check_id",
            "window",
            "kernel_matrix_id",
            "relation_radical_matrix_id",
            "kernel_rank",
            "relation_radical_rank",
            "combined_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "generation.csv",
        "generation by simple primitives",
        (
            "check_id",
            "window",
            "degree_id",
            "parity",
            "source_basis_id",
            "bracket_word_ids",
            "intermediate_degree_ids",
            "span_matrix_id",
            "source_rank",
            "span_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pbw.csv",
        "PBW associated-graded comparison",
        (
            "check_id",
            "degree_or_weight",
            "parity",
            "source_graded_rank",
            "target_graded_rank",
            "comparison_matrix_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "strict transitions and ML",
        (
            "row_id",
            "from_stage",
            "to_stage",
            "degree_id",
            "parity",
            "source_transition_matrix_id",
            "target_transition_matrix_id",
            "strict_pbw_status",
            "ml_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "a_beta_comparison_maps.csv",
        "A_beta intertwining equations",
        (
            "check_id",
            "degree_id",
            "parity",
            "identity_type",
            "source_matrix_ids",
            "target_matrix_ids",
            "a_entry_ids",
            "q_entry_ids",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "koszul_cones.csv",
        "Koszul comparison quasi-isomorphism cones",
        (
            "check_id",
            "cone_type",
            "degree_id",
            "bar_length",
            "word_type",
            "parity",
            "source_complex_id",
            "target_complex_id",
            "cone_matrix_id",
            "cohomology_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "koszul_comparison_identities.csv",
        "Koszul comparison structure identities",
        (
            "check_id",
            "identity_type",
            "degree_id",
            "parity",
            "source_matrix_ids",
            "target_matrix_ids",
            "homotopy_id",
            "defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "koszul_transition_ml.csv",
        "Koszul comparison transition and ML identities",
        (
            "check_id",
            "from_stage",
            "to_stage",
            "defect_system",
            "source_transition_matrix_id",
            "target_transition_matrix_id",
            "homotopy_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


TARGET_LABEL_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"(?<![0-9A-Za-z_])e_(?:[0-9A-Za-z]+|\{[0-9A-Za-z]+\})(?![0-9A-Za-z_])"),
    re.compile(
        r"(?<![0-9A-Za-z_])E_(?:[0-9A-Za-z]+(?:_[0-9A-Za-z]+)*|"
        r"\{[0-9A-Za-z,]+\})(?![0-9A-Za-z_])"
    ),
    re.compile(
        r"(?<![0-9A-Za-z_])u_(?:[0-9A-Za-z]+(?:_[0-9A-Za-z]+)*|"
        r"\{[0-9A-Za-z,]+\})(?![0-9A-Za-z_])"
    ),
    re.compile(
        r"(?<![0-9A-Za-z_])T_(?:[0-9A-Za-z]+(?:_[0-9A-Za-z]+)*|"
        r"\{[0-9A-Za-z,]+\})(?![0-9A-Za-z_])"
    ),
    re.compile(
        r"(?<![0-9A-Za-z_])M_(?:[0-9A-Za-z]+(?:_[0-9A-Za-z]+)*|"
        r"\{[0-9A-Za-z,]+\})(?![0-9A-Za-z_])"
    ),
    re.compile(
        r"(?<![0-9A-Za-z_])w_(?:[0-9A-Za-z]+(?:_[0-9A-Za-z]+)*|"
        r"\{[0-9A-Za-z,]+\})(?![0-9A-Za-z_])"
    ),
    re.compile(r"(?:\\delta|delta)_?\{?[0-9A-Za-z,]+\}?"),
    re.compile(r"\b2delta123\b"),
    re.compile(
        r"(?<![0-9A-Za-z_])2a_(?:[0-9]{2}|\{[0-9]{2}\})"
        r"(?:\.(?:even|odd)\.[0-9]+)?(?![0-9A-Za-z_])"
    ),
    re.compile(r"\ba_\{?[0-9]{2}\}?\b"),
    re.compile(r"\bC_(?:\{?[0-9],[0-9]+\}?|[0-9]_[0-9]+)\b"),
)


ALLOWED_TARGET_LABEL_COLUMNS = {
    "target_basis_id",
    "target_complex_id",
    "target_matrix_ids",
    "target_reference_id",
    "target_transition_matrix_id",
}

SOURCE_DEGREE_LABEL_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "source block with BKM root subscript",
        re.compile(
            r"P\^(?:X|\{X\}|\\Pi|\{\\Pi\})_\{R,\s*\\?(?:alpha|beta|rho)\}"
        ),
    ),
    (
        "raw Pi descent block",
        re.compile(r"P\^\{(?:\\Pi|Pi),\s*(?:raw|\\mathrm\{raw\})\}"),
    ),
    (
        "source matrix with BKM root subscript",
        re.compile(r"\b[KGQ]_\{?\\?(?:alpha|beta|rho)\}?"),
    ),
)

REQUIRED_IDENTITY_TYPES: dict[str, frozenset[str]] = {
    "hall_bialgebra_identities.csv": frozenset(
        {
            "unit_left",
            "unit_right",
            "counit_left",
            "counit_right",
            "associativity",
            "coassociativity",
            "bialgebra_compatibility",
            "primitive_closure",
        }
    ),
    "hopf_pairing_identities.csv": frozenset(
        {"hopf_adjointness", "frobenius_cyclic", "quotient_nondegenerate"}
    ),
    "radical_ideal_coideal.csv": frozenset({"lie_ideal", "coproduct_coideal"}),
    "relation_rows.csv": frozenset(
        {"cartan", "chevalley", "real_serre", "borcherds_orthogonality", "super_sign"}
    ),
    "a_beta_comparison_maps.csv": frozenset(
        {"bracket", "coproduct", "pairing", "radical_quotient", "pbw"}
    ),
    "koszul_cones.csv": frozenset(
        {"source_bar_cobar_counit", "source_to_target_quasi_isomorphism"}
    ),
    "koszul_comparison_identities.csv": frozenset(
        {
            "weyl_action",
            "pfaffian_orientation",
            "hall_product",
            "hall_coproduct",
            "hopf_pairing",
            "radical_quotient",
            "pbw",
        }
    ),
    "koszul_transition_ml.csv": frozenset(
        {
            "source_cone",
            "target_cone",
            "weyl_action",
            "pfaffian_orientation",
            "hall_pairing",
            "radical_quotient",
            "pbw",
        }
    ),
}

IDENTITY_COLUMN_BY_TABLE: dict[str, str] = {
    "hall_bialgebra_identities.csv": "identity_type",
    "hopf_pairing_identities.csv": "identity_type",
    "radical_ideal_coideal.csv": "identity",
    "relation_rows.csv": "relation_type",
    "a_beta_comparison_maps.csv": "identity_type",
    "koszul_cones.csv": "cone_type",
    "koszul_comparison_identities.csv": "identity_type",
    "koszul_transition_ml.csv": "defect_system",
}


@dataclass
class CsvTable:
    spec: TableSpec
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check a compact-source fixture packet without deriving target "
            "truth. The verifier is check-only and never writes fixtures."
        )
    )
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="source fixture directory",
    )
    parser.add_argument(
        "--target",
        type=Path,
        help="optional target reference fixture directory; never generated",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help=(
            "explicitly request check-only mode; this is the default and "
            "does not change behavior"
        ),
    )
    parser.add_argument(
        "--schema-only-ok",
        action="store_true",
        help=(
            "return process success for schema-only completeness; without "
            "this flag schema-only completeness still exits fail-closed"
        ),
    )
    return parser.parse_args(argv)


def load_manifest(source: Path, issues: list[str]) -> dict[str, object]:
    manifest_path = source / MANIFEST_NAME
    if not manifest_path.is_file():
        issues.append(f"missing required manifest: {manifest_path}")
        return {}
    try:
        with manifest_path.open(encoding="utf-8") as handle:
            manifest = json.load(handle)
    except json.JSONDecodeError as exc:
        issues.append(f"manifest is not valid JSON: {manifest_path}: {exc}")
        return {}
    if not isinstance(manifest, dict):
        issues.append(f"manifest root is not an object: {manifest_path}")
        return {}
    return manifest


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


def mathematical_payload_columns(spec: TableSpec) -> tuple[str, ...]:
    return tuple(column for column in spec.columns if column not in NON_PAYLOAD_COLUMNS)


def row_has_mathematical_payload(spec: TableSpec, row: dict[str, str]) -> bool:
    return any(row.get(column, "") for column in mathematical_payload_columns(spec))


def load_csv_table(source: Path, spec: TableSpec, issues: list[str]) -> CsvTable | None:
    table_path = source / spec.path
    if not table_path.is_file():
        issues.append(f"{spec.gate}: missing table {spec.path}")
        return None

    with table_path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != spec.columns:
            issues.append(
                f"{spec.gate}: header mismatch in {spec.path}; "
                f"expected {','.join(spec.columns)}"
            )
            return CsvTable(spec, nonempty_rows(reader))
        rows = nonempty_rows(reader)

    if spec.require_rows and not any(
        row_has_mathematical_payload(spec, row) for row in rows
    ):
        issues.append(
            f"{spec.gate}: {spec.path} has no supplied rows with mathematical payload"
        )
    return CsvTable(spec, rows)


def check_manifest(manifest: dict[str, object], issues: list[str]) -> None:
    source_kind = manifest.get("source_kind")
    if source_kind != SCHEMA_COMPLETE_SOURCE_KIND:
        issues.append(
            "manifest source_kind is "
            f"{source_kind!r}, not {SCHEMA_COMPLETE_SOURCE_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("target_truth_generated") is True:
        issues.append("manifest claims generated target truth; source verifier forbids this")


def check_readme(source: Path, issues: list[str]) -> None:
    readme_path = source / README_NAME
    if not readme_path.is_file():
        issues.append(f"missing required README: {readme_path}")


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(path))


def parse_target_hashes(text: str, issues: list[str]) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line_number, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            issues.append(f"target hash line {line_number} is malformed: {raw_line!r}")
            continue
        digest, filename = parts
        entries[filename.strip()] = digest
    return entries


def check_target_manifest_identity(target: Path, issues: list[str]) -> None:
    manifest_path = target / TARGET_MANIFEST_NAME
    if not manifest_path.is_file():
        issues.append(f"target reference is missing {TARGET_MANIFEST_NAME}: {target}")
        return

    manifest = manifest_path.read_text(encoding="utf-8")
    manifest_lines = manifest.splitlines()
    required_lines = (
        "schema: a071_target_presentation_fixture",
        "target: delta5_gn_kac",
        "window: A071_added_target_rows_not_relation_closed",
        "target_only: true",
        "  imports_compact_source_packets: false",
        "  provides_compact_source_verification: false",
        "  feeds_compact_source_comparison: false",
    )
    for line in required_lines:
        if manifest_lines.count(line) != 1:
            issues.append(f"target manifest missing required identity line: {line}")
    forbidden_true_lines = (
        "  imports_compact_source_packets: true",
        "  provides_compact_source_verification: true",
        "  feeds_compact_source_comparison: true",
        "target_only: false",
    )
    for line in forbidden_true_lines:
        if line in manifest_lines:
            issues.append(f"target manifest contains contradictory identity line: {line}")


def check_target_hashes(target: Path, issues: list[str]) -> None:
    hash_path = target / TARGET_HASH_FILE
    if not hash_path.is_file():
        issues.append(f"target reference is missing {TARGET_HASH_FILE}: {target}")
        return

    entries = parse_target_hashes(hash_path.read_text(encoding="utf-8"), issues)
    expected_names = set(TARGET_HASHED_FILENAMES)
    actual_names = set(entries)
    if actual_names != expected_names:
        issues.append(
            "target hash entries mismatch: "
            f"expected {sorted(expected_names)}, got {sorted(actual_names)}"
        )

    for filename, expected_digest in entries.items():
        file_path = target / filename
        if not file_path.is_file():
            issues.append(f"target hash target missing: {filename}")
            continue
        actual_digest = hashlib.sha256(file_path.read_bytes()).hexdigest()
        if actual_digest != expected_digest:
            issues.append(
                f"target hash mismatch {filename}: {actual_digest} != {expected_digest}"
            )


def check_target_reference(source: Path, target: Path | None, issues: list[str]) -> None:
    if target is None:
        issues.append("target fixture path not supplied; target truth was not generated")
        return
    source_resolved = source.resolve()
    target_resolved = target.resolve(strict=False)
    source_lexical = lexical_absolute(source)
    target_lexical = lexical_absolute(target)
    if target_resolved == source_resolved or target_lexical == source_lexical:
        issues.append(
            f"target fixture path equals source fixture path: {target}; "
            "source verifier requires a separate target reference"
        )
        return
    if is_relative_to(target_resolved, source_resolved) or is_relative_to(
        target_lexical, source_lexical
    ):
        issues.append(
            f"target fixture path is inside the source packet: {target}; "
            "source verifier requires an external target reference"
        )
        return
    if not target.exists():
        issues.append(f"target fixture path does not exist: {target}; target truth was not generated")
        return
    if not target.is_dir():
        issues.append(f"target fixture path is not a directory: {target}")
        return
    check_target_manifest_identity(target, issues)
    check_target_hashes(target, issues)


def check_row_status(table: CsvTable, issues: list[str]) -> None:
    if "check_status" not in table.spec.columns:
        return
    for index, row in enumerate(table.rows, start=2):
        status = row.get("check_status", "")
        if status != "verified":
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"has check_status={status!r}, not 'verified'"
            )


def check_secondary_statuses(table: CsvTable, issues: list[str]) -> None:
    for column, acceptable in ACCEPTABLE_SECONDARY_STATUSES.items():
        if column not in table.spec.columns:
            continue
        expected = ",".join(sorted(acceptable))
        for index, row in enumerate(table.rows, start=2):
            status = row.get(column, "")
            if status not in acceptable:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has {column}={status!r}, expected one of {expected}"
                )


def check_mathematical_payload(table: CsvTable, issues: list[str]) -> None:
    payload_columns = mathematical_payload_columns(table.spec)
    for index, row in enumerate(table.rows, start=2):
        nonempty_payload = [
            column for column in payload_columns if row.get(column, "")
        ]
        if not nonempty_payload:
            nonempty_columns = ",".join(
                column for column, value in row.items() if value
            )
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                "has no mathematical payload; "
                f"nonempty columns {nonempty_columns or '<none>'} do not supply the row"
            )
            continue
        missing_payload = [
            column for column in payload_columns if not row.get(column, "")
        ]
        if missing_payload:
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                "missing mathematical payload columns: "
                f"{','.join(missing_payload)}"
            )


def check_geometric_provenance(table: CsvTable, issues: list[str]) -> None:
    if not all(column in table.spec.columns for column in PROVENANCE_COLUMNS):
        return
    for index, row in enumerate(table.rows, start=2):
        for column in PROVENANCE_COLUMNS:
            value = row.get(column, "")
            if not value:
                continue
            normalized_value = re.sub(r"[^0-9a-z]+", "_", value.lower()).strip("_")
            tokens = {
                token
                for token in re.split(r"[^0-9A-Za-z]+", value.lower())
                if token
            }
            forbidden = sorted(
                token
                for token in FORBIDDEN_PROVENANCE_TOKENS
                if token in tokens or token in normalized_value
            )
            if forbidden:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"column {column!r} contains non-proof provenance "
                    f"tokens: {','.join(forbidden)}"
                )


def check_degree_source_block_status(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "degrees.csv":
        return
    expected = ",".join(sorted(ACCEPTABLE_SOURCE_BLOCK_STATUSES))
    for index, row in enumerate(table.rows, start=2):
        status = row.get("source_block_status", "")
        if status not in ACCEPTABLE_SOURCE_BLOCK_STATUSES:
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"has source_block_status={status!r}, expected one of {expected}"
            )


def contains_target_label(value: str) -> bool:
    return any(pattern.search(value) for pattern in TARGET_LABEL_PATTERNS)


def check_target_label_firewall(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        for column, value in row.items():
            if column in ALLOWED_TARGET_LABEL_COLUMNS:
                continue
            if contains_target_label(value):
                issues.append(
                    f"target-label firewall: {table.spec.path}:{index} "
                    f"column {column!r} contains target label {value!r}"
                )


def find_source_degree_label(value: str) -> str | None:
    for label, pattern in SOURCE_DEGREE_LABEL_PATTERNS:
        if pattern.search(value):
            return label
    return None


def check_source_degree_label_firewall(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        for column, value in row.items():
            label = find_source_degree_label(value)
            if label is None:
                continue
            issues.append(
                f"source-degree firewall: {table.spec.path}:{index} "
                f"column {column!r} contains {label} {value!r}; "
                "use Gram labels gamma_alpha/gamma_beta/gamma_rho and "
                "the descended Pi block, not BKM root labels or raw Pi blocks"
            )


def parse_int_cell(
    table: CsvTable, row_index: int, row: dict[str, str], column: str, issues: list[str]
) -> int | None:
    value = row.get(column, "")
    if not re.fullmatch(r"[+-]?\d+", value):
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{row_index} "
            f"column {column!r} has non-integral rank/value {value!r}"
        )
        return None
    return int(value)


def check_equal_int_columns(
    table: CsvTable, row_index: int, row: dict[str, str], columns: tuple[str, ...], issues: list[str]
) -> None:
    values = [
        parse_int_cell(table, row_index, row, column, issues)
        for column in columns
    ]
    if any(value is None for value in values):
        return
    if len(set(values)) != 1:
        rendered = ", ".join(f"{column}={value}" for column, value in zip(columns, values))
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{row_index} "
            f"rank equality failed: {rendered}"
        )


def check_zero_int_column(
    table: CsvTable, row_index: int, row: dict[str, str], column: str, issues: list[str]
) -> None:
    value = parse_int_cell(table, row_index, row, column, issues)
    if value is None:
        return
    if value != 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{row_index} "
            f"requires {column}=0, got {value}"
        )


def check_rank_semantics(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        if table.spec.path == "parity_blocks.csv":
            check_equal_int_columns(table, index, row, ("source_rank", "target_rank"), issues)
        elif table.spec.path == "hall_bialgebra_identities.csv":
            check_zero_int_column(table, index, row, "defect_rank", issues)
        elif table.spec.path == "hopf_pairing_identities.csv":
            check_zero_int_column(table, index, row, "defect_rank", issues)
            quotient_rank = parse_int_cell(table, index, row, "quotient_rank", issues)
            if quotient_rank is not None and quotient_rank < 0:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires quotient_rank >= 0, got {quotient_rank}"
                )
        elif table.spec.path == "radical_ideal_coideal.csv":
            check_equal_int_columns(
                table, index, row, ("left_rank", "right_rank", "combined_rank"), issues
            )
        elif table.spec.path == "no_extra.csv":
            check_equal_int_columns(
                table,
                index,
                row,
                ("kernel_rank", "relation_radical_rank", "combined_rank"),
                issues,
            )
        elif table.spec.path == "generation.csv":
            check_equal_int_columns(table, index, row, ("source_rank", "span_rank"), issues)
        elif table.spec.path == "pbw.csv":
            check_equal_int_columns(
                table,
                index,
                row,
                ("source_graded_rank", "target_graded_rank", "comparison_matrix_rank"),
                issues,
            )
        elif table.spec.path == "koszul_cones.csv":
            check_zero_int_column(table, index, row, "cohomology_rank", issues)
        elif table.spec.path == "koszul_comparison_identities.csv":
            check_zero_int_column(table, index, row, "defect_rank", issues)
        elif table.spec.path == "koszul_transition_ml.csv":
            check_zero_int_column(table, index, row, "r1lim_rank", issues)


def check_required_identity_coverage(table: CsvTable, issues: list[str]) -> None:
    required = REQUIRED_IDENTITY_TYPES.get(table.spec.path)
    if required is None or not table.rows:
        return
    identity_column = IDENTITY_COLUMN_BY_TABLE[table.spec.path]
    present = {row.get(identity_column, "").strip() for row in table.rows}
    missing = sorted(required - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: {table.spec.path} missing required "
            f"{identity_column} rows: {','.join(missing)}"
        )


def run(source: Path, target: Path | None) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not source.exists():
        return False, [f"source fixture path does not exist: {source}"]
    if not source.is_dir():
        return False, [f"source fixture path is not a directory: {source}"]

    manifest = load_manifest(source, issues)
    check_manifest(manifest, issues)
    check_readme(source, issues)
    check_target_reference(source, target, issues)

    tables: list[CsvTable] = []
    for spec in TABLE_SPECS:
        table = load_csv_table(source, spec, issues)
        if table is not None:
            tables.append(table)

    for table in tables:
        check_mathematical_payload(table, issues)
        check_geometric_provenance(table, issues)
        check_row_status(table, issues)
        check_secondary_statuses(table, issues)
        check_degree_source_block_status(table, issues)
        check_target_label_firewall(table, issues)
        check_source_degree_label_firewall(table, issues)
        check_rank_semantics(table, issues)
        check_required_identity_coverage(table, issues)

    return not issues, issues


def print_report(
    source: Path, target: Path | None, schema_only_complete: bool, issues: list[str]
) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("compact-source fixture verifier")
    print("mode: check-only")
    print(f"source: {source}")
    print(f"target: {target if target is not None else '<none>'}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("compact_source_recognition: false")
    print("mathematical_certification: false")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    schema_only_complete, issues = run(args.source, args.target)
    print_report(args.source, args.target, schema_only_complete, issues)
    return 0 if schema_only_complete and args.schema_only_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
