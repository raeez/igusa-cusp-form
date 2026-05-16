#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for compact-source packets.

This script is source-side only. It may read the path of a target
reference fixture, but it never computes, derives, or writes target truth.
A positive result is SCHEMA_COMPLETE: the manifest kind, table schemas,
row payloads, row statuses, target-reference separation, target-label
firewall, and source-degree firewall passed. It is not compact-source
certification, nor is it external mathematical verification.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCHEMA_COMPLETE_SOURCE_KIND = "compact_source_candidate"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
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
ACCEPTABLE_SOURCE_BLOCK_STATUSES = frozenset(
    {"source_verified", "source_admissible"}
)
ACCEPTABLE_SECONDARY_STATUSES = {
    "window_status": frozenset({"window_verified", "verified"}),
    "strict_pbw_status": frozenset({"strict_pbw_verified", "verified"}),
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
            "check_status",
            "notes",
        ),
    ),
)


TARGET_LABEL_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\be_[0-9A-Za-z]+\b"),
    re.compile(r"\bE_[0-9A-Za-z,]+\b"),
    re.compile(r"\bu_[0-9A-Za-z,]+\b"),
    re.compile(r"\bT_[0-9A-Za-z,]+\b"),
    re.compile(r"\bM_[0-9A-Za-z,]+\b"),
    re.compile(r"\bw_[0-9A-Za-z,]+\b"),
)


ALLOWED_TARGET_LABEL_COLUMNS = {
    "target_basis_id",
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
        check_row_status(table, issues)
        check_secondary_statuses(table, issues)
        check_degree_source_block_status(table, issues)
        check_target_label_firewall(table, issues)
        check_source_degree_label_firewall(table, issues)

    return not issues, issues


def print_report(
    source: Path, target: Path | None, schema_complete: bool, issues: list[str]
) -> None:
    status = "SCHEMA_COMPLETE" if schema_complete else "BLOCKED"
    print("compact-source fixture verifier")
    print("mode: check-only")
    print(f"source: {source}")
    print(f"target: {target if target is not None else '<none>'}")
    print(f"status: {status}")
    print(f"schema_complete: {str(schema_complete).lower()}")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    schema_complete, issues = run(args.source, args.target)
    print_report(args.source, args.target, schema_complete, issues)
    return 0 if schema_complete else 1


if __name__ == "__main__":
    raise SystemExit(main())
