#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for D0-HN packets.

This script checks only the retained D0-HN degeneration packet shape. It
does not construct degeneration families and does not prove (D0).  A
positive result is schema-only completeness.
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


SCHEMA_COMPLETE_D0_KIND = "d0_hn_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "finite_type_status",
        "proper_or_closed_status",
        "quasi_smooth_status",
        "strict_status",
        "ml_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "hilbert_scheme_only",
        "mock",
        "placeholder",
        "scalar_only",
        "status_only",
        "todo",
        "unsupplied",
    }
)
ACCEPTABLE_FINITE_TYPE_STATUSES = frozenset({"finite_type_verified", "verified"})
ACCEPTABLE_PROPER_CLOSED_STATUSES = frozenset(
    {"proper_verified", "closed_verified", "proper_or_closed_verified", "verified"}
)
ACCEPTABLE_QUASI_SMOOTH_STATUSES = frozenset({"quasi_smooth_verified", "verified"})
ACCEPTABLE_STRICT_STATUSES = frozenset({"strict_verified", "verified"})
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})


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
        "degeneration_families.csv",
        "flat D0-degeneration families",
        (
            "family_id",
            "hn_height",
            "base_id",
            "generic_fiber_id",
            "special_fiber_id",
            "d0_sector_id",
            "flatness_defect_rank",
            "contains_d0_sector",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "retained_substacks.csv",
        "retained degeneration substacks",
        (
            "substack_id",
            "family_id",
            "substack_type",
            "finite_type_status",
            "compatibility_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hn_transitions.csv",
        "HN transition morphisms",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "source_stack_id",
            "target_stack_id",
            "proper_or_closed_status",
            "preserves_d0_fiber",
            "composition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "derived_enhancements.csv",
        "derived and d-critical enhancements",
        (
            "enhancement_id",
            "stack_id",
            "quasi_smooth_status",
            "shifted_symplectic_id",
            "dcritical_truncation_id",
            "perfect_obstruction_theory_id",
            "obstruction_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "semiregularity_cosections.csv",
        "K3 semiregularity cosections",
        (
            "cosection_id",
            "stack_id",
            "source_obstruction_id",
            "target_structure_sheaf_id",
            "surjectivity_cokernel_rank",
            "d0_compatibility_defect_rank",
            "extension_additivity_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "vanishing_cycles.csv",
        "reduced vanishing-cycle specializations",
        (
            "vc_id",
            "stack_id",
            "localized_complex_id",
            "specialization_map_id",
            "transition_map_id",
            "specialization_cone_rank",
            "transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "orientation_specializations.csv",
        "orientation specializations",
        (
            "orientation_id",
            "stack_id",
            "square_root_id",
            "ts_multiplicativity_id",
            "specialization_map_id",
            "transition_map_id",
            "square_defect_rank",
            "ts_defect_rank",
            "specialization_cone_rank",
            "transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pfaffian_integration.csv",
        "Pfaffian and protected-integration specializations",
        (
            "check_id",
            "stack_id",
            "pfaffian_line_id",
            "pfaffian_section_id",
            "protected_integration_id",
            "compact_support_operation_id",
            "hall_operation_id",
            "specialization_defect_rank",
            "transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "ml_exactness.csv",
        "D0-HN strict Mittag-Leffler exactness",
        (
            "check_id",
            "system_type",
            "from_stage",
            "to_stage",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "D0 scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_d0_hn",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_SUBSTACK_TYPES = frozenset(
    {"object", "extension", "mixed", "wrapped", "two_step_flag"}
)
REQUIRED_ML_SYSTEM_TYPES = frozenset(
    {
        "vanishing_cycles",
        "orientation_gerbes",
        "pfaffian_lines",
        "compact_support_operations",
        "hall_product",
        "hall_coproduct",
        "finite_stage_morphisms",
    }
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {"hilbert_scheme_scalar_specialization", "k3_scalar_test", "scalar_trace"}
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check a D0-HN fixture packet without proving (D0)."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="D0 fixture directory")
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
    d0_kind = manifest.get("d0_kind")
    if d0_kind != SCHEMA_COMPLETE_D0_KIND:
        issues.append(f"manifest d0_kind is {d0_kind!r}, not {SCHEMA_COMPLETE_D0_KIND!r}")
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("hilbert_scheme_scalar_only") is True:
        issues.append("manifest marks this packet as Hilbert-scheme-scalar-only")


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
        if "finite_type_status" in table.spec.columns:
            finite_type = row.get("finite_type_status", "")
            if finite_type not in ACCEPTABLE_FINITE_TYPE_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has finite_type_status={finite_type!r}"
                )
        if "proper_or_closed_status" in table.spec.columns:
            proper = row.get("proper_or_closed_status", "")
            if proper not in ACCEPTABLE_PROPER_CLOSED_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has proper_or_closed_status={proper!r}"
                )
        if "quasi_smooth_status" in table.spec.columns:
            quasi = row.get("quasi_smooth_status", "")
            if quasi not in ACCEPTABLE_QUASI_SMOOTH_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has quasi_smooth_status={quasi!r}"
                )
        if "strict_status" in table.spec.columns:
            strict = row.get("strict_status", "")
            if strict not in ACCEPTABLE_STRICT_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has strict_status={strict!r}"
                )
        if "ml_status" in table.spec.columns:
            ml_status = row.get("ml_status", "")
            if ml_status not in ACCEPTABLE_ML_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has ml_status={ml_status!r}"
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
            tokens = {token for token in re.split(r"[^0-9A-Za-z]+", value.lower()) if token}
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


def parse_int(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> int | None:
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


def require_true(table: CsvTable, index: int, row: dict[str, str], column: str, issues: list[str]) -> None:
    value = row.get(column, "").lower()
    if value != "true":
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}='true', got {row.get(column, '')!r}"
        )


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    for index, row in enumerate(table.rows, start=2):
        if table.spec.path == "degeneration_families.csv":
            require_zero(table, index, row, "flatness_defect_rank", issues)
            require_true(table, index, row, "contains_d0_sector", issues)
            parse_int(table, index, row, "hn_height", issues)
        elif table.spec.path == "retained_substacks.csv":
            require_zero(table, index, row, "compatibility_defect_rank", issues)
        elif table.spec.path == "hn_transitions.csv":
            require_true(table, index, row, "preserves_d0_fiber", issues)
            require_zero(table, index, row, "composition_defect_rank", issues)
        elif table.spec.path == "derived_enhancements.csv":
            require_zero(table, index, row, "obstruction_defect_rank", issues)
        elif table.spec.path == "semiregularity_cosections.csv":
            require_zero(table, index, row, "surjectivity_cokernel_rank", issues)
            require_zero(table, index, row, "d0_compatibility_defect_rank", issues)
            require_zero(table, index, row, "extension_additivity_defect_rank", issues)
        elif table.spec.path == "vanishing_cycles.csv":
            require_zero(table, index, row, "specialization_cone_rank", issues)
            require_zero(table, index, row, "transition_defect_rank", issues)
        elif table.spec.path == "orientation_specializations.csv":
            require_zero(table, index, row, "square_defect_rank", issues)
            require_zero(table, index, row, "ts_defect_rank", issues)
            require_zero(table, index, row, "specialization_cone_rank", issues)
            require_zero(table, index, row, "transition_defect_rank", issues)
        elif table.spec.path == "pfaffian_integration.csv":
            require_zero(table, index, row, "specialization_defect_rank", issues)
            require_zero(table, index, row, "transition_defect_rank", issues)
        elif table.spec.path == "ml_exactness.csv":
            require_zero(table, index, row, "r1lim_rank", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_true(table, index, row, "excluded_from_d0_hn", issues)


def check_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path == "retained_substacks.csv" and table.rows:
        present = {row.get("substack_type", "") for row in table.rows}
        missing = sorted(REQUIRED_SUBSTACK_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: retained_substacks.csv missing substack_type rows: "
                f"{','.join(missing)}"
            )
    if table.spec.path == "ml_exactness.csv" and table.rows:
        present = {row.get("system_type", "") for row in table.rows}
        missing = sorted(REQUIRED_ML_SYSTEM_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: ml_exactness.csv missing system_type rows: "
                f"{','.join(missing)}"
            )
    if table.spec.path == "scalar_firewall.csv" and table.rows:
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
    print("D0-HN fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("d0_certification: false")
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
