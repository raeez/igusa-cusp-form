#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for finite moduli packets.

This script checks only the retained finite-moduli and d-critical atlas
packet.  It does not prove boundedness, construct derived substacks, or
construct the cosection atlas.  A positive result is schema-only
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


SCHEMA_COMPLETE_MODULI_KIND = "finite_k3e_moduli_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "finite_type_status",
        "ml_status",
        "proper_or_closed_status",
        "proper_status",
        "quasi_smooth_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "charge_window_only",
        "hilbert_scheme_only",
        "liu_stability_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "scalar_only",
        "status_only",
        "target_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_FINITE_TYPE_STATUSES = frozenset({"finite_type_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
ACCEPTABLE_PROPER_STATUSES = frozenset(
    {"proper_verified", "closed_verified", "proper_or_closed_verified", "verified"}
)
ACCEPTABLE_QUASI_SMOOTH_STATUSES = frozenset({"quasi_smooth_verified", "verified"})
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
        "hn_type_bounds.csv",
        "retained HN type bounds",
        (
            "type_id",
            "hn_height",
            "charge_id",
            "amplitude_bounds",
            "hilbert_polynomial_id",
            "regularity_bound",
            "closure_family_id",
            "extension_closure_defect_rank",
            "finite_type_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "semistable_substacks.csv",
        "finite-type semistable substacks",
        (
            "substack_id",
            "type_id",
            "stability_id",
            "ambient_stack_id",
            "quot_postnikov_chart_id",
            "finite_type_status",
            "specialization_closed",
            "semistability_defect_rank",
            "boundedness_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "derived_enhancements.csv",
        "quasi-smooth derived enhancements",
        (
            "enhancement_id",
            "substack_id",
            "derived_stack_id",
            "shifted_symplectic_form_id",
            "quasi_smooth_status",
            "cotangent_amplitude",
            "tor_amplitude_defect_rank",
            "symplectic_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "universal_complexes.csv",
        "universal perfect complexes",
        (
            "universal_id",
            "substack_id",
            "perfect_complex_id",
            "base_change_id",
            "tor_amplitude",
            "descent_defect_rank",
            "perfection_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_rigidifications.csv",
        "scalar rigidifications",
        (
            "rigidification_id",
            "substack_id",
            "automorphism_group_id",
            "scalar_gm_removed",
            "residual_inertia_finite",
            "rigidification_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "stratifications.csv",
        "finite inertia stratifications",
        (
            "stratification_id",
            "substack_id",
            "strata_count",
            "closed_cover_id",
            "finite_residual_inertia",
            "coverage_defect_rank",
            "inertia_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "extension_flag_stacks.csv",
        "extension and flag stacks",
        (
            "flag_id",
            "source_type_ids",
            "extension_stack_id",
            "two_step_flag_stack_id",
            "proper_status",
            "finite_type_status",
            "quasi_smooth_status",
            "subquotient_closure_defect_rank",
            "properness_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cosection_atlas.csv",
        "d-critical cosection atlas",
        (
            "atlas_id",
            "stack_id",
            "dcritical_chart_id",
            "cosection_id",
            "vanishing_cycle_id",
            "orientation_line_id",
            "cosection_surjectivity_defect_rank",
            "dcritical_compatibility_defect_rank",
            "orientation_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "finite-moduli transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "stack_id",
            "transition_morphism_id",
            "proper_or_closed_status",
            "strict_status",
            "ml_status",
            "composition_defect_rank",
            "r1lim_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "finite-moduli scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_moduli",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "formal_charge_window",
        "hilbert_scheme_scalar",
        "liu_stability_only",
        "pfaffian_product",
        "target_window",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite K3xE moduli fixture shape without proving boundedness."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="finite-moduli fixture directory")
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
    moduli_kind = manifest.get("moduli_kind")
    if moduli_kind != SCHEMA_COMPLETE_MODULI_KIND:
        issues.append(
            "manifest moduli_kind is "
            f"{moduli_kind!r}, not {SCHEMA_COMPLETE_MODULI_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; finite moduli require stacks")
    if manifest.get("target_only") is True:
        issues.append("manifest marks this packet as target-only; finite moduli are source data")
    if manifest.get("liu_stability_only") is True:
        issues.append("manifest marks this packet as Liu-stability-only; bounded substacks are required")


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
            ("finite_type_status", ACCEPTABLE_FINITE_TYPE_STATUSES),
            ("ml_status", ACCEPTABLE_ML_STATUSES),
            ("proper_or_closed_status", ACCEPTABLE_PROPER_STATUSES),
            ("proper_status", ACCEPTABLE_PROPER_STATUSES),
            ("quasi_smooth_status", ACCEPTABLE_QUASI_SMOOTH_STATUSES),
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


def require_nonnegative(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value < 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} requires {column}>=0, got {value}"
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


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    zero_columns_by_table = {
        "hn_type_bounds.csv": ("extension_closure_defect_rank",),
        "semistable_substacks.csv": ("semistability_defect_rank", "boundedness_defect_rank"),
        "derived_enhancements.csv": ("tor_amplitude_defect_rank", "symplectic_defect_rank"),
        "universal_complexes.csv": ("descent_defect_rank", "perfection_defect_rank"),
        "scalar_rigidifications.csv": ("rigidification_defect_rank",),
        "stratifications.csv": ("coverage_defect_rank", "inertia_defect_rank"),
        "extension_flag_stacks.csv": ("subquotient_closure_defect_rank", "properness_defect_rank"),
        "cosection_atlas.csv": (
            "cosection_surjectivity_defect_rank",
            "dcritical_compatibility_defect_rank",
            "orientation_defect_rank",
        ),
        "transitions.csv": ("composition_defect_rank", "r1lim_rank"),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "hn_type_bounds.csv":
            require_nonnegative(table, index, row, "regularity_bound", issues)
        elif table.spec.path == "semistable_substacks.csv":
            require_bool_text(table, index, row, "specialization_closed", "true", issues)
        elif table.spec.path == "scalar_rigidifications.csv":
            require_bool_text(table, index, row, "scalar_gm_removed", "true", issues)
            require_bool_text(table, index, row, "residual_inertia_finite", "true", issues)
        elif table.spec.path == "stratifications.csv":
            require_positive(table, index, row, "strata_count", issues)
            require_bool_text(table, index, row, "finite_residual_inertia", "true", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_moduli", "true", issues)


def check_scalar_firewall_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "scalar_firewall.csv" or not table.rows:
        return
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
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite K3xE moduli fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("moduli_certification: false")
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
