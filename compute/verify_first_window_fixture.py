#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for the first recognition window.

This script checks only the finite first relation-closed window packet.
It does not construct the compact Hall source, compute the matrices, or
prove primitive recognition.  A positive result is schema-only
completeness for the table packet.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SCHEMA_COMPLETE_FIRST_WINDOW_KIND = "first_relation_closed_window_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "convergence_status",
        "ml_status",
        "proof_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "arbitrary_matrices",
        "denominator_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "scalar_only",
        "signed_only",
        "status_only",
        "target_labels_only",
        "target_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_CONVERGENCE_STATUSES = frozenset(
    {"strong_convergence_verified", "verified"}
)
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
ACCEPTABLE_PROOF_STATUSES = frozenset({"proved_in_window", "verified"})
ACCEPTABLE_STRICT_STATUSES = frozenset({"strict_verified", "verified"})


@dataclass(frozen=True)
class TableSpec:
    path: str
    gate: str
    columns: tuple[str, ...]
    require_rows: bool = True


@dataclass
class CsvTable:
    spec: TableSpec
    rows: list[dict[str, str]]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "window_closure.csv",
        "first relation-closed window",
        (
            "window_id",
            "target_window_id",
            "source_window_id",
            "height_bound",
            "downward_saturated",
            "relation_closed",
            "active_exhaustive",
            "target_admissible",
            "source_admissible",
            "closure_defect_rank",
            "signed_only_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "target_source_representatives.csv",
        "target-source representatives",
        (
            "representative_id",
            "window_id",
            "target_degree_id",
            "source_degree_id",
            "source_cycle_id",
            "compact_provenance_id",
            "parity",
            "target_even_rank",
            "target_odd_rank",
            "source_even_rank",
            "source_odd_rank",
            "parity_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "chevalley_serre_matrices.csv",
        "Chevalley and Serre matrices",
        (
            "relation_id",
            "window_id",
            "relation_type",
            "left_word_id",
            "right_word_id",
            "matrix_id",
            "serre_exponent",
            "source_rank",
            "target_rank",
            "relation_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hall_boundary_complex.csv",
        "Hall-Chevalley boundary complex",
        (
            "complex_id",
            "window_id",
            "filtration_id",
            "degree_id",
            "c0_rank",
            "c1_rank",
            "c2_rank",
            "d1_matrix_id",
            "d1_square_rank",
            "serre_boundary_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "spectral_sequence.csv",
        "first-window spectral sequence",
        (
            "spectral_id",
            "complex_id",
            "e1_rank",
            "e2_rank",
            "einf_rank",
            "d1_defect_rank",
            "higher_differential_rank",
            "strong_convergence_defect_rank",
            "convergence_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "kernel_matrices.csv",
        "kernel and no-extra matrices",
        (
            "kernel_id",
            "window_id",
            "presentation_matrix_id",
            "computed_kernel_rank",
            "gn_kernel_rank",
            "radical_rank",
            "kernel_basis_id",
            "kernel_equality_defect_rank",
            "no_extra_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pbw_graded.csv",
        "PBW associated graded",
        (
            "pbw_id",
            "window_id",
            "degree_id",
            "source_pbw_rank",
            "target_pbw_rank",
            "associated_graded_rank",
            "pbw_defect_rank",
            "filtration_strictness_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "first_window_theorems.csv",
        "first-window theorem packet",
        (
            "theorem_id",
            "window_id",
            "theorem_type",
            "statement_id",
            "proof_artifact_id",
            "proof_status",
            "residual_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "first-window transitions",
        (
            "transition_id",
            "from_window",
            "to_window",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "kernel_transition_defect_rank",
            "pbw_transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "first-window scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_shortcut",
            "excluded_from_first_window",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_RELATION_TYPES = frozenset(
    {"borcherds_orthogonality", "cartan", "chevalley", "real_serre", "super_sign"}
)
REQUIRED_THEOREM_TYPES = frozenset(
    {
        "hall_coproduct",
        "hall_product",
        "hopf_pairing",
        "koszul_comparison",
        "o1",
        "o1_plus",
        "o2",
        "pbw_comparison",
        "pfin",
        "pfaffian_equality",
        "primitive_recognition",
    }
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "arbitrary_matrices",
        "denominator_product",
        "pfaffian_product",
        "scalar_trace",
        "signed_dimensions_only",
        "status_only_rows",
        "target_labels_only",
        "target_pbw_only",
    }
)
ACCEPTABLE_PARITIES = frozenset({"even", "mixed", "odd"})


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check first relation-closed recognition-window fixture shape."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="first-window fixture directory")
    parser.add_argument("--check", action="store_true", help="explicit check-only mode")
    parser.add_argument(
        "--schema-only-ok",
        action="store_true",
        help="return process success for schema-only completeness",
    )
    return parser.parse_args(argv)


def load_manifest(fixture: Path, issues: list[str]) -> dict[str, object]:
    manifest_path = fixture / MANIFEST_NAME
    if not manifest_path.is_file():
        issues.append(f"missing required manifest: {manifest_path}")
        return {}
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"manifest is not valid JSON: {manifest_path}: {exc}")
        return {}
    if not isinstance(manifest, dict):
        issues.append(f"manifest root is not an object: {manifest_path}")
        return {}
    return manifest


def check_manifest(manifest: dict[str, object], issues: list[str]) -> None:
    first_window_kind = manifest.get("first_window_kind")
    if first_window_kind != SCHEMA_COMPLETE_FIRST_WINDOW_KIND:
        issues.append(
            "manifest first_window_kind is "
            f"{first_window_kind!r}, not {SCHEMA_COMPLETE_FIRST_WINDOW_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    for key in (
        "arbitrary_matrices",
        "denominator_only",
        "pfaffian_only",
        "scalar_only",
        "signed_only",
        "target_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"manifest marks this packet as {key}; first-window rows are required")


def check_readme(fixture: Path, issues: list[str]) -> None:
    readme_path = fixture / README_NAME
    if not readme_path.is_file():
        issues.append(f"missing required README: {readme_path}")


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


def payload_columns(spec: TableSpec) -> tuple[str, ...]:
    return tuple(column for column in spec.columns if column not in NON_PAYLOAD_COLUMNS)


def row_has_payload(spec: TableSpec, row: dict[str, str]) -> bool:
    return any(row.get(column, "") for column in payload_columns(spec))


def load_csv_table(fixture: Path, spec: TableSpec, issues: list[str]) -> CsvTable | None:
    table_path = fixture / spec.path
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
    if spec.require_rows and not any(row_has_payload(spec, row) for row in rows):
        issues.append(f"{spec.gate}: {spec.path} has no supplied rows with mathematical payload")
    return CsvTable(spec, rows)


def check_statuses(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        status = row.get("check_status", "")
        if status != "verified":
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"has check_status={status!r}, not 'verified'"
            )
        status_checks = (
            ("convergence_status", ACCEPTABLE_CONVERGENCE_STATUSES),
            ("ml_status", ACCEPTABLE_ML_STATUSES),
            ("proof_status", ACCEPTABLE_PROOF_STATUSES),
            ("strict_status", ACCEPTABLE_STRICT_STATUSES),
        )
        for column, acceptable in status_checks:
            if column in table.spec.columns:
                value = row.get(column, "")
                if value not in acceptable:
                    issues.append(
                        f"{table.spec.gate}: {table.spec.path}:{index} "
                        f"has {column}={value!r}"
                    )


def check_payload(table: CsvTable, issues: list[str]) -> None:
    columns = payload_columns(table.spec)
    for index, row in enumerate(table.rows, start=2):
        missing = [column for column in columns if not row.get(column, "")]
        if missing:
            issues.append(
                f"{table.spec.gate}: {table.spec.path}:{index} "
                f"missing mathematical payload columns: {','.join(missing)}"
            )


def check_provenance(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        for column in PROVENANCE_COLUMNS:
            value = row.get(column, "")
            if not value:
                continue
            normalized = re.sub(r"[^0-9a-z]+", "_", value.lower()).strip("_")
            tokens = {
                token for token in re.split(r"[^0-9A-Za-z]+", value.lower()) if token
            }
            forbidden = sorted(
                token
                for token in FORBIDDEN_PROVENANCE_TOKENS
                if token in tokens or token in normalized
            )
            if forbidden:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"column {column!r} contains non-proof provenance tokens: "
                    f"{','.join(forbidden)}"
                )


def parse_int(
    table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]
) -> int | None:
    value = row.get(column, "")
    if not re.fullmatch(r"[+-]?\d+", value):
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"column {column!r} has non-integral value {value!r}"
        )
        return None
    return int(value)


def require_zero(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value != 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column}=0, got {value}"
        )


def require_positive(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value <= 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column}>0, got {value}"
        )


def require_bool_text(
    table: CsvTable, index: int, row: dict[str, str], column: str, expected: str, issues: list[str]
) -> None:
    value = row.get(column, "").lower()
    if value != expected:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}={expected!r}, got {row.get(column, '')!r}"
        )


def require_equal_ints(
    table: CsvTable,
    index: int,
    row: dict[str, str],
    left: str,
    right: str,
    issues: list[str],
) -> None:
    left_value = parse_int(table, index, row, left, issues)
    right_value = parse_int(table, index, row, right, issues)
    if left_value is not None and right_value is not None and left_value != right_value:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {left}={right}, got {left_value}!={right_value}"
        )


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    zero_columns_by_table = {
        "window_closure.csv": ("closure_defect_rank", "signed_only_defect_rank"),
        "target_source_representatives.csv": ("parity_defect_rank",),
        "chevalley_serre_matrices.csv": ("relation_defect_rank",),
        "hall_boundary_complex.csv": ("d1_square_rank", "serre_boundary_defect_rank"),
        "spectral_sequence.csv": (
            "d1_defect_rank",
            "higher_differential_rank",
            "strong_convergence_defect_rank",
        ),
        "kernel_matrices.csv": ("kernel_equality_defect_rank", "no_extra_defect_rank"),
        "pbw_graded.csv": ("pbw_defect_rank", "filtration_strictness_defect_rank"),
        "first_window_theorems.csv": ("residual_defect_rank",),
        "transitions.csv": (
            "r1lim_rank",
            "kernel_transition_defect_rank",
            "pbw_transition_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "window_closure.csv":
            require_positive(table, index, row, "height_bound", issues)
            for column in (
                "downward_saturated",
                "relation_closed",
                "active_exhaustive",
                "target_admissible",
                "source_admissible",
            ):
                require_bool_text(table, index, row, column, "true", issues)
        elif table.spec.path == "target_source_representatives.csv":
            parity = row.get("parity", "")
            if parity not in ACCEPTABLE_PARITIES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has parity={parity!r}"
                )
            require_equal_ints(table, index, row, "target_even_rank", "source_even_rank", issues)
            require_equal_ints(table, index, row, "target_odd_rank", "source_odd_rank", issues)
        elif table.spec.path == "chevalley_serre_matrices.csv":
            relation_type = row.get("relation_type", "")
            if relation_type not in REQUIRED_RELATION_TYPES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown relation_type={relation_type!r}"
                )
            require_equal_ints(table, index, row, "source_rank", "target_rank", issues)
            if relation_type == "real_serre":
                value = parse_int(table, index, row, "serre_exponent", issues)
                if value is not None and value != 3:
                    issues.append(
                        f"{table.spec.gate}: {table.spec.path}:{index} "
                        f"requires real_serre exponent 3, got {value}"
                    )
            else:
                parse_int(table, index, row, "serre_exponent", issues)
        elif table.spec.path == "hall_boundary_complex.csv":
            for column in ("c0_rank", "c1_rank", "c2_rank"):
                parse_int(table, index, row, column, issues)
        elif table.spec.path == "spectral_sequence.csv":
            for column in ("e1_rank", "e2_rank", "einf_rank"):
                parse_int(table, index, row, column, issues)
            require_equal_ints(table, index, row, "e2_rank", "einf_rank", issues)
        elif table.spec.path == "kernel_matrices.csv":
            require_equal_ints(table, index, row, "computed_kernel_rank", "gn_kernel_rank", issues)
            parse_int(table, index, row, "radical_rank", issues)
        elif table.spec.path == "pbw_graded.csv":
            require_equal_ints(table, index, row, "source_pbw_rank", "target_pbw_rank", issues)
            require_equal_ints(table, index, row, "source_pbw_rank", "associated_graded_rank", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_first_window", "true", issues)


def check_coverage(table: CsvTable, issues: list[str]) -> None:
    if not table.rows:
        return
    if table.spec.path == "chevalley_serre_matrices.csv":
        present = {row.get("relation_type", "") for row in table.rows}
        missing = sorted(REQUIRED_RELATION_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: chevalley_serre_matrices.csv missing relation_type rows: "
                f"{','.join(missing)}"
            )
    elif table.spec.path == "first_window_theorems.csv":
        present = {row.get("theorem_type", "") for row in table.rows}
        missing = sorted(REQUIRED_THEOREM_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: first_window_theorems.csv missing theorem_type rows: "
                f"{','.join(missing)}"
            )
    elif table.spec.path == "scalar_firewall.csv":
        present = {row.get("firewall_type", "") for row in table.rows}
        missing = sorted(REQUIRED_FIREWALL_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: scalar_firewall.csv missing firewall_type rows: "
                f"{','.join(missing)}"
            )


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    if not fixture.exists():
        return False, [f"fixture path does not exist: {fixture}"]
    if not fixture.is_dir():
        return False, [f"fixture path is not a directory: {fixture}"]
    manifest = load_manifest(fixture, issues)
    check_manifest(manifest, issues)
    check_readme(fixture, issues)

    tables: list[CsvTable] = []
    for spec in TABLE_SPECS:
        table = load_csv_table(fixture, spec, issues)
        if table is not None:
            tables.append(table)

    for table in tables:
        check_statuses(table, issues)
        check_payload(table, issues)
        check_provenance(table, issues)
        check_semantics(table, issues)
        check_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("first relation-closed window fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("first_window_certification: false")
    print("mathematical_certification: false")
    if issues:
        print("fail_closed_limitations:")
        for issue in issues:
            print(f"- {issue}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    schema_only_complete, issues = run(args.fixture)
    print_report(args.fixture, schema_only_complete, issues)
    return 0 if schema_only_complete and args.schema_only_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
