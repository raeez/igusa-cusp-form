#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for finite E3 source packets.

This script checks only the retained holomorphic E3-prefactorization
and K3-to-E specialization packet.  It does not construct the compact
source, solve the BV quantum master equation, prove anomaly
cancellation, or prove the specialization.  A positive result is
schema-only completeness for the table packet.
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


SCHEMA_COMPLETE_E3_KIND = "finite_e3_holfa_source_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "finite_type_status",
        "ml_status",
        "proper_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "denominator_only",
        "hybrid_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "scalar_only",
        "status_only",
        "target_only",
        "todo",
        "trace_only",
        "unsupplied",
    }
)
ACCEPTABLE_FINITE_TYPE_STATUSES = frozenset({"finite_type_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
ACCEPTABLE_PROPER_STATUSES = frozenset(
    {"proper_verified", "closed_verified", "proper_or_closed_verified", "verified"}
)
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
        "formal_target_charts.csv",
        "formal K3xE target charts",
        (
            "chart_id",
            "hn_height",
            "derived_formal_neighborhood_id",
            "local_model_id",
            "holomorphic_volume_form_id",
            "finite_type_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "field_complexes.csv",
        "finite field complexes",
        (
            "complex_id",
            "chart_id",
            "field_name",
            "cohomological_amplitude",
            "differential_id",
            "symplectic_pairing_id",
            "pairing_degree",
            "elliptic_degree_window_id",
            "cohomology_defect_rank",
            "pairing_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "e3_operations.csv",
        "holomorphic E3 operations",
        (
            "operation_id",
            "operation_type",
            "arity",
            "input_complex_ids",
            "output_complex_id",
            "little_disks_chain_id",
            "locality_support_id",
            "associativity_defect_rank",
            "equivariance_defect_rank",
            "unit_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "bv_qme.csv",
        "BV quantum master equation",
        (
            "qme_id",
            "chart_id",
            "action_functional_id",
            "bv_laplacian_id",
            "bracket_id",
            "classical_master_defect_rank",
            "quantum_master_defect_rank",
            "anomaly_class_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "anomaly_framing.csv",
        "anomaly, framing, and formality rows",
        (
            "check_id",
            "chart_id",
            "anomaly_type",
            "obstruction_class_id",
            "obstruction_rank",
            "trivialization_id",
            "framing_id",
            "formality_map_id",
            "formality_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "compact_support.csv",
        "compact retained support",
        (
            "support_id",
            "chart_id",
            "compact_support_condition",
            "proper_status",
            "boundary_exclusion_id",
            "support_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "factorization_descent.csv",
        "prefactorization descent",
        (
            "descent_id",
            "chart_id",
            "cover_id",
            "prefactorization_map_id",
            "support_condition",
            "cech_defect_rank",
            "locality_defect_rank",
            "descent_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "k3_to_e_specialization.csv",
        "K3-to-E chain specialization",
        (
            "specialization_id",
            "source_chart_id",
            "target_hybrid_chart_id",
            "chain_map_id",
            "cosection_compatibility_id",
            "wrapped_leg_compatibility_id",
            "vanishing_cycle_defect_rank",
            "orientation_defect_rank",
            "pfaffian_defect_rank",
            "chain_homotopy_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "E3 source and specialization transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "source_component_id",
            "target_component_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "operation_defect_rank",
            "specialization_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "E3 source scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_e3_source",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_OPERATION_TYPES = frozenset(
    {"unit", "binary_product", "little_3_disks_action", "higher_coherence"}
)
REQUIRED_ANOMALY_TYPES = frozenset(
    {"bv_qme", "holomorphic_de_rham", "framing", "formality"}
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "automorphic_section",
        "borcherds_denominator",
        "hybrid_carrier_only",
        "protected_trace",
        "target_current_envelope",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite E3 source fixture shape without proving the compact source."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="E3 source fixture directory")
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
    source_kind = manifest.get("e3_source_kind")
    if source_kind != SCHEMA_COMPLETE_E3_KIND:
        issues.append(
            "manifest e3_source_kind is "
            f"{source_kind!r}, not {SCHEMA_COMPLETE_E3_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; E3 source requires chain data")
    if manifest.get("target_only") is True:
        issues.append("manifest marks this packet as target-only; E3 source is compact-source data")
    if manifest.get("hybrid_only") is True:
        issues.append("manifest marks this packet as hybrid-only; K3xE source data are required")


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
            ("proper_status", ACCEPTABLE_PROPER_STATUSES),
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


def require_nonnegative(
    table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]
) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value < 0:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}>=0, got {value}"
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
        "field_complexes.csv": ("cohomology_defect_rank", "pairing_defect_rank"),
        "e3_operations.csv": (
            "associativity_defect_rank",
            "equivariance_defect_rank",
            "unit_defect_rank",
        ),
        "bv_qme.csv": (
            "classical_master_defect_rank",
            "quantum_master_defect_rank",
            "anomaly_class_rank",
        ),
        "anomaly_framing.csv": ("obstruction_rank", "formality_defect_rank"),
        "compact_support.csv": ("support_defect_rank",),
        "factorization_descent.csv": (
            "cech_defect_rank",
            "locality_defect_rank",
            "descent_defect_rank",
        ),
        "k3_to_e_specialization.csv": (
            "vanishing_cycle_defect_rank",
            "orientation_defect_rank",
            "pfaffian_defect_rank",
            "chain_homotopy_defect_rank",
        ),
        "transitions.csv": (
            "r1lim_rank",
            "operation_defect_rank",
            "specialization_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "e3_operations.csv":
            operation_type = row.get("operation_type", "")
            if operation_type not in REQUIRED_OPERATION_TYPES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown operation_type={operation_type!r}"
                )
            require_nonnegative(table, index, row, "arity", issues)
        elif table.spec.path == "field_complexes.csv":
            parse_int(table, index, row, "pairing_degree", issues)
        elif table.spec.path == "anomaly_framing.csv":
            anomaly_type = row.get("anomaly_type", "")
            if anomaly_type not in REQUIRED_ANOMALY_TYPES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown anomaly_type={anomaly_type!r}"
                )
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_e3_source", "true", issues)


def check_operation_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "e3_operations.csv" or not table.rows:
        return
    present = {row.get("operation_type", "") for row in table.rows}
    missing = sorted(REQUIRED_OPERATION_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: e3_operations.csv missing operation_type rows: "
            f"{','.join(missing)}"
        )


def check_anomaly_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "anomaly_framing.csv" or not table.rows:
        return
    present = {row.get("anomaly_type", "") for row in table.rows}
    missing = sorted(REQUIRED_ANOMALY_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: anomaly_framing.csv missing anomaly_type rows: "
            f"{','.join(missing)}"
        )


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
        check_operation_coverage(table, issues)
        check_anomaly_coverage(table, issues)
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite E3 source fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("e3_source_certification: false")
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
