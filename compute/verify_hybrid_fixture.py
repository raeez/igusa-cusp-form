#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for hybrid carrier packets.

This script checks only the finite hybrid local/wrapped carrier packet.
It does not construct the wrapped prequotient, anchors,
correspondences, quotient pseudofunctor, or protected integration.  A
positive result is schema-only completeness for the table packet.
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


SCHEMA_COMPLETE_HYBRID_KIND = "finite_hybrid_carrier_candidate"
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
        "determinant_only",
        "fock_only",
        "mock",
        "ordinary_ran_only",
        "placeholder",
        "quotient_first",
        "scalar_only",
        "status_only",
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
        "hybrid_base.csv",
        "hybrid base and elliptic-degree split",
        (
            "base_id",
            "hn_height",
            "local_window_id",
            "wrapped_window_id",
            "elliptic_degree_map_id",
            "additivity_defect_rank",
            "finite_type_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "local_configurations.csv",
        "projection-finite local configurations",
        (
            "configuration_id",
            "base_id",
            "charge_id",
            "index_set_id",
            "incidence_stack_id",
            "diagonal_compatibility_id",
            "symmetric_descent_id",
            "support_locality_defect_rank",
            "descent_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "wrapped_prequotients.csv",
        "wrapped prequotients and anchors",
        (
            "wrapped_id",
            "base_id",
            "charge_id",
            "prequotient_stack_id",
            "rigidification_id",
            "origin_id",
            "anchor_id",
            "e_equivariance_defect_rank",
            "anchor_loss_defect_rank",
            "finite_type_status",
            "proper_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "correspondences.csv",
        "local, mixed, and wrapped correspondences",
        (
            "correspondence_id",
            "correspondence_type",
            "source_charge_ids",
            "target_charge_id",
            "correspondence_stack_id",
            "source_anchor_memory_id",
            "target_anchor_memory_id",
            "proper_status",
            "finite_type_status",
            "thom_sebastiani_defect_rank",
            "admissibility_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "flag_atlas.csv",
        "eight-word two-step flag atlas",
        (
            "flag_id",
            "word",
            "flag_stack_id",
            "left_parenthesization_id",
            "right_parenthesization_id",
            "associativity_defect_rank",
            "pentagon_defect_rank",
            "anchor_retention_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "higher_coloured.csv",
        "higher-coloured hybrid coherences",
        (
            "coherence_id",
            "arity",
            "tree_id",
            "unit_defect_rank",
            "symmetry_defect_rank",
            "refinement_defect_rank",
            "overlap_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "quotient_pseudofunctor.csv",
        "quotient-after-correspondence pseudofunctor",
        (
            "quotient_id",
            "source_correspondence_id",
            "reduced_correspondence_id",
            "q_functor_id",
            "theta_q_id",
            "composition_defect_rank",
            "base_change_defect_rank",
            "thom_sebastiani_defect_rank",
            "flag_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "protected_integration.csv",
        "protected integration with Gram trace",
        (
            "integration_id",
            "source_component_id",
            "gram_label_id",
            "target_monomial_id",
            "chain_defect_rank",
            "product_defect_rank",
            "coproduct_defect_rank",
            "primitive_defect_rank",
            "transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "hybrid carrier transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "hybrid_component_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "anchor_defect_rank",
            "correspondence_defect_rank",
            "quotient_defect_rank",
            "integration_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "hybrid scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_scalar",
            "excluded_from_hybrid",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_CORRESPONDENCE_TYPES = frozenset(
    {"LL", "mixed", "WW", "two_sided_mixed"}
)
REQUIRED_FLAG_WORDS = frozenset(
    {"LLL", "LLW", "LWL", "WLL", "LWW", "WLW", "WWL", "WWW"}
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "borcherds_s_degree_only",
        "determinant_anchor_only",
        "fock_trace",
        "ordinary_ran_only",
        "quotient_first_hall_product",
        "scalar_pfaffian_product",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite hybrid carrier fixture shape without proving the carrier."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="hybrid fixture directory")
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
    hybrid_kind = manifest.get("hybrid_kind")
    if hybrid_kind != SCHEMA_COMPLETE_HYBRID_KIND:
        issues.append(
            "manifest hybrid_kind is "
            f"{hybrid_kind!r}, not {SCHEMA_COMPLETE_HYBRID_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    if manifest.get("ordinary_ran_only") is True:
        issues.append("manifest marks this packet as ordinary-Ran-only; wrapped data are required")
    if manifest.get("quotient_first") is True:
        issues.append("manifest marks this packet as quotient-first; hybrid data require unreduced correspondences")
    if manifest.get("scalar_only") is True:
        issues.append("manifest marks this packet as scalar-only; hybrid data require correspondence stacks")


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


def check_semantics(table: CsvTable, issues: list[str]) -> None:
    zero_columns_by_table = {
        "hybrid_base.csv": ("additivity_defect_rank",),
        "local_configurations.csv": ("support_locality_defect_rank", "descent_defect_rank"),
        "wrapped_prequotients.csv": ("e_equivariance_defect_rank", "anchor_loss_defect_rank"),
        "correspondences.csv": ("thom_sebastiani_defect_rank", "admissibility_defect_rank"),
        "flag_atlas.csv": (
            "associativity_defect_rank",
            "pentagon_defect_rank",
            "anchor_retention_defect_rank",
        ),
        "higher_coloured.csv": (
            "unit_defect_rank",
            "symmetry_defect_rank",
            "refinement_defect_rank",
            "overlap_defect_rank",
        ),
        "quotient_pseudofunctor.csv": (
            "composition_defect_rank",
            "base_change_defect_rank",
            "thom_sebastiani_defect_rank",
            "flag_defect_rank",
        ),
        "protected_integration.csv": (
            "chain_defect_rank",
            "product_defect_rank",
            "coproduct_defect_rank",
            "primitive_defect_rank",
            "transition_defect_rank",
        ),
        "transitions.csv": (
            "r1lim_rank",
            "anchor_defect_rank",
            "correspondence_defect_rank",
            "quotient_defect_rank",
            "integration_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "correspondences.csv":
            correspondence_type = row.get("correspondence_type", "")
            if correspondence_type not in REQUIRED_CORRESPONDENCE_TYPES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown correspondence_type={correspondence_type!r}"
                )
        elif table.spec.path == "flag_atlas.csv":
            word = row.get("word", "")
            if word not in REQUIRED_FLAG_WORDS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown word={word!r}"
                )
        elif table.spec.path == "higher_coloured.csv":
            require_positive(table, index, row, "arity", issues)
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_hybrid", "true", issues)


def check_correspondence_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "correspondences.csv" or not table.rows:
        return
    present = {row.get("correspondence_type", "") for row in table.rows}
    missing = sorted(REQUIRED_CORRESPONDENCE_TYPES - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: correspondences.csv missing correspondence_type rows: "
            f"{','.join(missing)}"
        )


def check_flag_word_coverage(table: CsvTable, issues: list[str]) -> None:
    if table.spec.path != "flag_atlas.csv" or not table.rows:
        return
    present = {row.get("word", "") for row in table.rows}
    missing = sorted(REQUIRED_FLAG_WORDS - present)
    if missing:
        issues.append(
            f"{table.spec.gate}: flag_atlas.csv missing word rows: {','.join(missing)}"
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
        check_correspondence_coverage(table, issues)
        check_flag_word_coverage(table, issues)
        check_scalar_firewall_coverage(table, issues)

    return not issues, issues


def print_report(fixture: Path, schema_only_complete: bool, issues: list[str]) -> None:
    status = SCHEMA_ONLY_STATUS if schema_only_complete else "BLOCKED"
    print("finite hybrid carrier fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("hybrid_certification: false")
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
