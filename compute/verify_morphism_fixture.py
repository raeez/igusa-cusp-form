#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for finite-stage morphisms.

This script checks only the finite-stage Dirac-Igusa morphism packet.
It does not construct the morphisms, prove strict Mittag-Leffler
exactness, or prove a pro-isomorphism.  A positive result is
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


SCHEMA_COMPLETE_MORPHISM_KIND = "finite_stage_dirac_igusa_morphism_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "cofinal_status",
        "component_coverage_status",
        "directed_status",
        "finite_type_status",
        "iso_status",
        "ml_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "denominator_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "product_only",
        "scalar_only",
        "signed_only",
        "status_only",
        "target_only",
        "todo",
        "trace_only",
        "unsupplied",
    }
)
ACCEPTABLE_COFINAL_STATUSES = frozenset({"cofinal_verified", "verified"})
ACCEPTABLE_COMPONENT_COVERAGE_STATUSES = frozenset(
    {"component_coverage_verified", "verified"}
)
ACCEPTABLE_DIRECTED_STATUSES = frozenset({"directed_verified", "verified"})
ACCEPTABLE_FINITE_TYPE_STATUSES = frozenset({"finite_type_verified", "verified"})
ACCEPTABLE_ISO_STATUSES = frozenset({"isomorphism_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
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
        "cofinal_subsystems.csv",
        "cofinal HN subsystem",
        (
            "subsystem_id",
            "poset_id",
            "directed_status",
            "cofinal_status",
            "identity_defect_rank",
            "composition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "stage_objects.csv",
        "finite-stage DI objects",
        (
            "stage_id",
            "hn_height",
            "component_name",
            "component_id",
            "payload_packet_id",
            "typed_category",
            "finite_type_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "stage_morphisms.csv",
        "finite-stage transition morphisms",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "morphism_id",
            "subsystem_id",
            "strict_status",
            "component_coverage_status",
            "identity_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "component_maps.csv",
        "component maps for clauses M1-M8",
        (
            "map_id",
            "transition_id",
            "clause",
            "source_component_id",
            "target_component_id",
            "map_payload_id",
            "compatibility_defect_rank",
            "kernel_rank",
            "cokernel_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "composition_laws.csv",
        "composition laws for finite-stage transitions",
        (
            "composition_id",
            "high_stage",
            "mid_stage",
            "low_stage",
            "left_composite_id",
            "right_composite_id",
            "composition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "ml_exactness.csv",
        "Mittag-Leffler exactness for component towers",
        (
            "system_id",
            "component_name",
            "clause",
            "tower_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pro_isomorphisms.csv",
        "Dirac-Igusa pro-isomorphisms",
        (
            "pro_iso_id",
            "source_pro_object_id",
            "target_pro_object_id",
            "cofinal_subsystem_id",
            "finite_stage_iso_family_id",
            "inverse_family_id",
            "iso_status",
            "commute_defect_rank",
            "left_inverse_defect_rank",
            "right_inverse_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "morphism scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_morphism",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_COMPONENT_NAMES = frozenset(
    {
        "A_E3",
        "C",
        "F_hyb",
        "Gamma",
        "H",
        "L_Pf",
        "P_Pi",
        "Phi",
        "Pi",
        "Rec",
        "Theta_Kos",
        "epsilon_o",
        "o",
        "pf",
    }
)
REQUIRED_CLAUSES = frozenset({f"M{index}" for index in range(1, 9)})
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "denominator_product",
        "protected_trace",
        "scalar_pfaffian_product",
        "signed_exponent_table",
        "squared_determinant",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite-stage DI morphism fixture shape without proving the pro-object."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="morphism fixture directory")
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
    morphism_kind = manifest.get("morphism_kind")
    if morphism_kind != SCHEMA_COMPLETE_MORPHISM_KIND:
        issues.append(
            "manifest morphism_kind is "
            f"{morphism_kind!r}, not {SCHEMA_COMPLETE_MORPHISM_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; morphisms require typed data")
    if manifest.get("product_only") is True:
        issues.append("manifest marks this packet as product-only; scalar products do not define transitions")


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
            ("cofinal_status", ACCEPTABLE_COFINAL_STATUSES),
            ("component_coverage_status", ACCEPTABLE_COMPONENT_COVERAGE_STATUSES),
            ("directed_status", ACCEPTABLE_DIRECTED_STATUSES),
            ("finite_type_status", ACCEPTABLE_FINITE_TYPE_STATUSES),
            ("iso_status", ACCEPTABLE_ISO_STATUSES),
            ("ml_status", ACCEPTABLE_ML_STATUSES),
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
        "cofinal_subsystems.csv": ("identity_defect_rank", "composition_defect_rank"),
        "stage_morphisms.csv": ("identity_defect_rank",),
        "component_maps.csv": ("compatibility_defect_rank", "kernel_rank", "cokernel_rank"),
        "composition_laws.csv": ("composition_defect_rank",),
        "ml_exactness.csv": ("r1lim_rank", "transition_defect_rank"),
        "pro_isomorphisms.csv": (
            "commute_defect_rank",
            "left_inverse_defect_rank",
            "right_inverse_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "stage_objects.csv":
            component_name = row.get("component_name", "")
            if component_name not in REQUIRED_COMPONENT_NAMES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown component_name={component_name!r}"
                )
        elif table.spec.path in {"component_maps.csv", "ml_exactness.csv"}:
            clause = row.get("clause", "")
            if clause not in REQUIRED_CLAUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown clause={clause!r}"
                )
            if table.spec.path == "ml_exactness.csv":
                component_name = row.get("component_name", "")
                if component_name not in REQUIRED_COMPONENT_NAMES:
                    issues.append(
                        f"{table.spec.gate}: {table.spec.path}:{index} "
                        f"unknown component_name={component_name!r}"
                    )
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_morphism", "true", issues)


def check_stage_component_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "stage_objects.csv" or not table.rows:
        return
    present = {row.get("component_name", "") for row in table.rows}
    missing = sorted(REQUIRED_COMPONENT_NAMES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: stage_objects.csv missing component_name rows: "
            f"{','.join(missing)}"
        )


def check_clause_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path not in {"component_maps.csv", "ml_exactness.csv"} or not table.rows:
        return
    present = {row.get("clause", "") for row in table.rows}
    missing = sorted(REQUIRED_CLAUSES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: {table.spec.path} missing clause rows: "
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
        check_stage_component_coverage(table, issues)
        check_clause_coverage(table, issues)
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite-stage DI morphism fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("pro_object_certification: false")
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
