#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for protected trace packets.

This script checks only the finite level-Z protected trace packet.  It
does not construct a categorical trace, a gravity-line operator algebra,
or a Pfaffian theorem.  A positive result is schema-only completeness
for the trace table packet.
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


SCHEMA_COMPLETE_TRACE_KIND = "finite_protected_trace_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "conjectural_status",
        "constructed_status",
        "ml_status",
        "orientation_forgetting_status",
        "strict_status",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "source_formula_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "automorphic_only",
        "determinant_only",
        "gravity_only",
        "mock",
        "op_only",
        "path_integral_only",
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
ACCEPTABLE_ORIENTATION_FORGETTING_STATUSES = frozenset(
    {"orientation_forgetting_verified", "verified"}
)
ACCEPTABLE_CONJECTURAL_STATUSES = frozenset({"conjectural", "open"})
ACCEPTABLE_CONSTRUCTED_STATUSES = frozenset({"not_constructed", "open"})
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
        "trace_categories.csv",
        "level-Z trace category",
        (
            "trace_id",
            "beilinson_level",
            "source_object_id",
            "trace_category_id",
            "closed_cobordism_id",
            "operator_domain_id",
            "category_defect_rank",
            "closedness_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "protected_trace_functors.csv",
        "protected trace functor",
        (
            "functor_id",
            "trace_id",
            "domain_category_id",
            "codomain_id",
            "closed_cobordism_id",
            "degree_variable_id",
            "functoriality_defect_rank",
            "cyclicity_defect_rank",
            "excision_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "trace_operators.csv",
        "operator being traced",
        (
            "operator_id",
            "trace_id",
            "pfaffian_section_id",
            "determinant_section_id",
            "inverse_square_id",
            "delta5_square_id",
            "orientation_forgetting_status",
            "operator_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_normalizations.csv",
        "OP and unscaled scalar normalizations",
        (
            "normalization_id",
            "trace_id",
            "op_branch_id",
            "leading_coefficient",
            "square_coefficient",
            "op_sign",
            "unscaled_trace_id",
            "normalization_residual",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "trace_identities.csv",
        "protected trace identities",
        (
            "identity_id",
            "trace_id",
            "left_expression",
            "right_expression",
            "equality_context",
            "delta5_power",
            "phi10_power",
            "identity_residual_rank",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "forgetful_maps.csv",
        "trace-forgetful maps",
        (
            "map_id",
            "trace_id",
            "input_datum",
            "output_scalar_id",
            "kernel_witness_id",
            "orientation_killed",
            "bracket_killed",
            "pairing_killed",
            "pbw_killed",
            "parity_killed",
            "forgetfulness_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "gravity_residuals.csv",
        "Hall-Borcherds gravity residual",
        (
            "residual_id",
            "trace_id",
            "residual_name",
            "beilinson_level",
            "operator_algebra_id",
            "morphism_id",
            "trace_character_id",
            "conjectural_status",
            "constructed_status",
            "used_in_trace_proof",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "trace transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "trace_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "normalization_defect_rank",
            "forgetful_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "protected-trace scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_reconstruction",
            "excluded_from_trace",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "gravity_path_integral",
        "hopf_pairing",
        "orientation_character",
        "parity_split",
        "pbw_basis",
        "pfaffian_line",
        "primitive_bracket",
        "source_koszul_map",
    }
)
ACCEPTABLE_TRACE_LEVELS = frozenset({"Z", "level_Z", "mathsf_Z"})
ACCEPTABLE_GRAVITY_LEVELS = frozenset({"A", "level_A", "mathsf_A"})
ACCEPTABLE_EQUALITY_CONTEXTS = frozenset(
    {"unscaled_trace", "op_chamber", "protected_trace"}
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite protected trace fixture shape without proving the trace."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="trace fixture directory")
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
    trace_kind = manifest.get("trace_kind")
    if trace_kind != SCHEMA_COMPLETE_TRACE_KIND:
        issues.append(
            "manifest trace_kind is "
            f"{trace_kind!r}, not {SCHEMA_COMPLETE_TRACE_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    for key in (
        "automorphic_only",
        "gravity_path_integral",
        "op_only",
        "pfaffian_only",
        "scalar_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"manifest marks this packet as {key}; protected trace rows are required")


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
            ("orientation_forgetting_status", ACCEPTABLE_ORIENTATION_FORGETTING_STATUSES),
            ("conjectural_status", ACCEPTABLE_CONJECTURAL_STATUSES),
            ("constructed_status", ACCEPTABLE_CONSTRUCTED_STATUSES),
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


def require_int(
    table: CsvTable, index: int, row: dict[str, str], column: str, expected: int, issues: list[str]
) -> None:
    value = parse_int(table, index, row, column, issues)
    if value is not None and value != expected:
        issues.append(
            f"{table.spec.gate}: {table.spec.path}:{index} "
            f"requires {column}={expected}, got {value}"
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
        "trace_categories.csv": ("category_defect_rank", "closedness_defect_rank"),
        "protected_trace_functors.csv": (
            "functoriality_defect_rank",
            "cyclicity_defect_rank",
            "excision_defect_rank",
        ),
        "trace_operators.csv": ("operator_defect_rank",),
        "scalar_normalizations.csv": ("normalization_residual",),
        "trace_identities.csv": ("identity_residual_rank",),
        "forgetful_maps.csv": ("forgetfulness_defect_rank",),
        "transitions.csv": (
            "r1lim_rank",
            "normalization_defect_rank",
            "forgetful_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "trace_categories.csv":
            level = row.get("beilinson_level", "")
            if level not in ACCEPTABLE_TRACE_LEVELS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires level Z, got {level!r}"
                )
        elif table.spec.path == "scalar_normalizations.csv":
            require_int(table, index, row, "leading_coefficient", 64, issues)
            require_int(table, index, row, "square_coefficient", 4096, issues)
            require_int(table, index, row, "op_sign", -1, issues)
        elif table.spec.path == "trace_identities.csv":
            require_int(table, index, row, "delta5_power", -2, issues)
            require_int(table, index, row, "phi10_power", -1, issues)
            context = row.get("equality_context", "")
            if context not in ACCEPTABLE_EQUALITY_CONTEXTS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown equality_context={context!r}"
                )
        elif table.spec.path == "forgetful_maps.csv":
            for column in (
                "orientation_killed",
                "bracket_killed",
                "pairing_killed",
                "pbw_killed",
                "parity_killed",
            ):
                require_bool_text(table, index, row, column, "true", issues)
        elif table.spec.path == "gravity_residuals.csv":
            level = row.get("beilinson_level", "")
            if level not in ACCEPTABLE_GRAVITY_LEVELS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires level A for gravity residual, got {level!r}"
                )
            require_bool_text(table, index, row, "used_in_trace_proof", "false", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_trace", "true", issues)


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
    print("finite protected trace fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("protected_trace_certification: false")
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
