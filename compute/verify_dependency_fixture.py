#!/usr/bin/env python3
"""Fail-closed schema/status/payload gate for theorem dependency ledgers.

This script checks only a finite theorem-dependency ledger:
Beilinson-level sites, typed objects, typed morphisms, theorem
dependencies, forbidden edges, status separation, equality scopes,
equality sites, definition-separation rows, and
obstruction-independence rows.  It does not prove any theorem.  A
positive result is schema-only completeness for the dependency packet.
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


SCHEMA_COMPLETE_DEPENDENCY_KIND = "finite_theorem_dependency_candidate"
SCHEMA_ONLY_STATUS = "SCHEMA_COMPLETE_SCHEMA_ONLY"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
NON_PAYLOAD_COLUMNS = frozenset(
    {
        "check_status",
        "claim_status",
        "constructed_status",
        "ml_status",
        "strict_status",
        "used_in_proof",
        "notes",
    }
)
PROVENANCE_COLUMNS = ("geometric_source_id", "proof_reference")
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "automorphic_only",
        "conjecture_only",
        "gravity_only",
        "mirror_only",
        "mock",
        "op_only",
        "placeholder",
        "scalar_only",
        "status_only",
        "target_only",
        "todo",
        "trace_only",
        "unsupplied",
    }
)
ACCEPTABLE_CLAIM_STATUSES = frozenset(
    {"conditional", "conjectured", "definition", "open", "proved", "proved_elsewhere", "relative"}
)
ACCEPTABLE_CONSTRUCTED_STATUSES = frozenset(
    {"constructed", "conjectural", "not_constructed", "open", "retained", "verified"}
)
ACCEPTABLE_ML_STATUSES = frozenset({"ml_verified", "verified"})
ACCEPTABLE_STRICT_STATUSES = frozenset({"strict_verified", "verified"})
ACCEPTABLE_LEVELS = frozenset({"A", "C", "P", "S", "Z", "level_A", "level_C", "level_P", "level_S", "level_Z", "mathsf_A", "mathsf_C", "mathsf_P", "mathsf_S", "mathsf_Z"})


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
        "beilinson_levels.csv",
        "Beilinson-level sites",
        (
            "level_id",
            "standard_symbol",
            "mathematical_site",
            "category_id",
            "primitive_object_id",
            "allowed_equality_kinds",
            "scalar_shadow_status",
            "forbidden_promotion",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "objects.csv",
        "typed theorem objects",
        (
            "object_id",
            "object_kind",
            "beilinson_level",
            "category_id",
            "construction_packet_id",
            "constructed_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "morphisms.csv",
        "typed morphisms",
        (
            "morphism_id",
            "source_object_id",
            "target_object_id",
            "morphism_kind",
            "category_id",
            "construction_packet_id",
            "functoriality_defect_rank",
            "level_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "theorem_dependencies.csv",
        "theorem dependency rows",
        (
            "theorem_id",
            "theorem_label",
            "theorem_type",
            "claim_status",
            "conclusion_level",
            "hypothesis_packet_ids",
            "allowed_dependency_ids",
            "dependency_closure_id",
            "closure_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "dependency_edges.csv",
        "allowed dependency edges",
        (
            "edge_id",
            "theorem_id",
            "dependency_id",
            "dependency_kind",
            "source_level",
            "target_level",
            "used_in_proof",
            "edge_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "forbidden_edges.csv",
        "forbidden proof edges",
        (
            "check_id",
            "theorem_id",
            "forbidden_dependency_type",
            "forbidden_dependency_id",
            "forbidden_use",
            "excluded_from_proof",
            "separation_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "status_separation.csv",
        "claim-status separation",
        (
            "separation_id",
            "theorem_id",
            "proved_status_id",
            "conditional_status_id",
            "conjectural_status_id",
            "open_status_id",
            "no_status_collapse",
            "status_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "level_equalities.csv",
        "Beilinson-level equality scopes",
        (
            "equality_id",
            "left_object_id",
            "right_object_id",
            "equality_kind",
            "ambient_category_id",
            "beilinson_level",
            "claim_status",
            "scalar_shadow_allowed",
            "equality_defect_rank",
            "forbidden_lift",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "equality_sites.csv",
        "mathematical equality sites",
        (
            "site_id",
            "site_kind",
            "mathematical_site",
            "allowed_equality_forms",
            "excluded_equality_forms",
            "beilinson_levels",
            "ambient_category_ids",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "definition_separation.csv",
        "non-circular definition separation",
        (
            "separation_id",
            "defined_object_id",
            "definition_site",
            "construction_inputs",
            "comparison_outputs",
            "forbidden_definition_inputs",
            "noncircular_order",
            "beilinson_level",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "obstruction_independence.csv",
        "obstruction implication and independence witnesses",
        (
            "datum_id",
            "datum_kind",
            "type_dependencies",
            "logical_implications",
            "independence_witness",
            "deleted_residue_id",
            "geometric_counterexample_status",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        "dependency-ledger transitions",
        (
            "transition_id",
            "from_stage",
            "to_stage",
            "dependency_ledger_id",
            "strict_status",
            "ml_status",
            "r1lim_rank",
            "edge_transition_defect_rank",
            "status_transition_defect_rank",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        "dependency scalar firewall",
        (
            "check_id",
            "firewall_type",
            "forbidden_dependency",
            "excluded_from_dependency_ledger",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


REQUIRED_THEOREM_TYPES = frozenset(
    {
        "construction",
        "gravity_line",
        "mirror_discriminant",
        "orientation_character",
        "pfaffian_dirac",
        "primitive_recognition",
        "scalar_trace",
    }
)
REQUIRED_FORBIDDEN_TYPES = frozenset(
    {
        "automorphic_section_defines_pfaffian",
        "denominator_product_recognition",
        "gravity_residual_in_pfaffian",
        "gravity_residual_in_recognition",
        "mirror_conjecture_in_pfaffian",
        "mirror_conjecture_in_recognition",
        "op_scalar_orientation",
        "scalar_trace_orientation",
        "scalar_trace_primitive_bracket",
        "target_counit_source_koszul",
        "target_label_source_representative",
    }
)
REQUIRED_FIREWALL_TYPES = frozenset(
    {
        "automorphic_only",
        "conjectural_status_collapse",
        "gravity_line",
        "mirror_conjecture",
        "op_scalar_branch",
        "scalar_trace",
        "target_only",
    }
)
REQUIRED_BEILINSON_LEVELS = frozenset({"P", "C", "S", "Z", "A"})
ACCEPTABLE_SCALAR_SHADOW_STATUSES = frozenset(
    {"not_scalar", "scalar_shadow", "conjectural_scalar", "open_operator_lift"}
)
REQUIRED_EQUALITY_SITE_KINDS = frozenset(
    {
        "automorphic_line_bundle",
        "completed_lie_superalgebra",
        "derived_category",
        "k0_group",
        "picard_groupoid",
        "pro_category",
        "scalar_trace",
    }
)
REQUIRED_DEFINITION_SEPARATIONS = frozenset(
    {
        "koszul_not_target_counit",
        "orientation_not_scalar",
        "pfaffian_not_automorphic_value",
        "pfaffian_not_desired_value",
        "primitive_not_target_multiplicity",
        "pro_object_not_scalar_shadow",
    }
)
ACCEPTABLE_NONCIRCULAR_ORDERS = frozenset(
    {
        "definition_before_comparison",
        "operator_before_scalar_trace",
        "orientation_before_character_comparison",
        "pro_object_before_section_comparison",
        "source_before_target_comparison",
    }
)
REQUIRED_OBSTRUCTION_INDEPENDENCE_ROWS = frozenset(
    {
        "D0_HN",
        "O1_quot",
        "O1_plus_torsor",
        "O2_atlas",
        "P_fin",
        "koszul_source",
        "primitive_recognition",
    }
)
ACCEPTABLE_COUNTEREXAMPLE_STATUSES = frozenset(
    {"finite_row_witness_only", "geometric_counterexample_not_claimed"}
)
REQUIRED_EQUALITY_KINDS = frozenset(
    {
        "automorphic_section",
        "bkm_denominator",
        "gravity_residual_open",
        "koszul_chiral_comparison",
        "mirror_discriminant_conjecture",
        "orientation_character",
        "pfaffian_section",
        "primitive_recognition",
        "pro_object_identity",
        "scalar_trace",
    }
)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite theorem-dependency ledger shape without proving theorems."
    )
    parser.add_argument("--fixture", required=True, type=Path, help="dependency fixture directory")
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
    dependency_kind = manifest.get("dependency_kind")
    if dependency_kind != SCHEMA_COMPLETE_DEPENDENCY_KIND:
        issues.append(
            "manifest dependency_kind is "
            f"{dependency_kind!r}, not {SCHEMA_COMPLETE_DEPENDENCY_KIND!r}"
        )
    if manifest.get("empty_blocked") is True:
        issues.append("manifest marks this packet as empty-blocked")
    for key in (
        "automorphic_only",
        "gravity_only",
        "mirror_only",
        "scalar_only",
        "target_only",
    ):
        if manifest.get(key) is True:
            issues.append(f"manifest marks this packet as {key}; dependency rows are required")


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
            ("claim_status", ACCEPTABLE_CLAIM_STATUSES),
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
        "morphisms.csv": ("functoriality_defect_rank", "level_defect_rank"),
        "theorem_dependencies.csv": ("closure_defect_rank",),
        "dependency_edges.csv": ("edge_defect_rank",),
        "forbidden_edges.csv": ("separation_defect_rank",),
        "status_separation.csv": ("status_defect_rank",),
        "level_equalities.csv": ("equality_defect_rank",),
        "transitions.csv": (
            "r1lim_rank",
            "edge_transition_defect_rank",
            "status_transition_defect_rank",
        ),
    }
    for index, row in enumerate(table.rows, start=2):
        for column in zero_columns_by_table.get(table.spec.path, ()):
            require_zero(table, index, row, column, issues)
        if table.spec.path == "beilinson_levels.csv":
            level_id = row.get("level_id", "")
            if level_id not in REQUIRED_BEILINSON_LEVELS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid level_id={level_id!r}"
                )
            if row.get("standard_symbol", "") != f"mathsf_{level_id}":
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has standard_symbol={row.get('standard_symbol', '')!r}"
                )
            scalar_status = row.get("scalar_shadow_status", "")
            if scalar_status not in ACCEPTABLE_SCALAR_SHADOW_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has scalar_shadow_status={scalar_status!r}"
                )
        elif table.spec.path == "equality_sites.csv":
            site_kind = row.get("site_kind", "")
            if site_kind not in REQUIRED_EQUALITY_SITE_KINDS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid site_kind={site_kind!r}"
                )
            levels = {
                level.strip()
                for level in row.get("beilinson_levels", "").split(";")
                if level.strip()
            }
            invalid_levels = sorted(levels - REQUIRED_BEILINSON_LEVELS)
            if invalid_levels:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid beilinson_levels={';'.join(invalid_levels)}"
                )
            allowed_forms = {
                form.strip()
                for form in row.get("allowed_equality_forms", "").split(";")
                if form.strip()
            }
            excluded_forms = {
                form.strip()
                for form in row.get("excluded_equality_forms", "").split(";")
                if form.strip()
            }
            overlap = sorted(allowed_forms & excluded_forms)
            if overlap:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"allows and excludes equality forms: {';'.join(overlap)}"
                )
        elif table.spec.path == "definition_separation.csv":
            separation_id = row.get("separation_id", "")
            if separation_id not in REQUIRED_DEFINITION_SEPARATIONS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid separation_id={separation_id!r}"
                )
            level = row.get("beilinson_level", "")
            if level not in REQUIRED_BEILINSON_LEVELS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid beilinson_level={level!r}"
                )
            order = row.get("noncircular_order", "")
            if order not in ACCEPTABLE_NONCIRCULAR_ORDERS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid noncircular_order={order!r}"
                )
            construction_inputs = {
                value.strip()
                for value in row.get("construction_inputs", "").split(";")
                if value.strip()
            }
            comparison_outputs = {
                value.strip()
                for value in row.get("comparison_outputs", "").split(";")
                if value.strip()
            }
            forbidden_inputs = {
                value.strip()
                for value in row.get("forbidden_definition_inputs", "").split(";")
                if value.strip()
            }
            overlap = sorted(forbidden_inputs & (construction_inputs | comparison_outputs))
            if overlap:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"forbidden definition inputs are also used: {';'.join(overlap)}"
                )
        elif table.spec.path == "obstruction_independence.csv":
            datum_id = row.get("datum_id", "")
            if datum_id not in REQUIRED_OBSTRUCTION_INDEPENDENCE_ROWS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid datum_id={datum_id!r}"
                )
            status = row.get("geometric_counterexample_status", "")
            if status not in ACCEPTABLE_COUNTEREXAMPLE_STATUSES:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"has invalid geometric_counterexample_status={status!r}"
                )
            implications = {
                value.strip()
                for value in row.get("logical_implications", "").split(";")
                if value.strip()
            }
            if implications != {"none"}:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    "logical_implications must be 'none'"
                )
        if table.spec.path in {"objects.csv", "theorem_dependencies.csv", "dependency_edges.csv", "level_equalities.csv"}:
            for column in ("beilinson_level", "conclusion_level", "source_level", "target_level"):
                if column in table.spec.columns:
                    value = row.get(column, "")
                    if value not in ACCEPTABLE_LEVELS:
                        issues.append(
                            f"{table.spec.gate}: {table.spec.path}:{index} "
                            f"has invalid {column}={value!r}"
                        )
        if table.spec.path == "dependency_edges.csv":
            require_bool_text(table, index, row, "used_in_proof", "true", issues)
        elif table.spec.path == "forbidden_edges.csv":
            require_bool_text(table, index, row, "excluded_from_proof", "true", issues)
        elif table.spec.path == "status_separation.csv":
            require_bool_text(table, index, row, "no_status_collapse", "true", issues)
        elif table.spec.path == "level_equalities.csv":
            scalar_shadow = row.get("scalar_shadow_allowed", "").lower()
            if scalar_shadow not in {"true", "false"}:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"requires scalar_shadow_allowed boolean, got {row.get('scalar_shadow_allowed', '')!r}"
                )
            equality_kind = row.get("equality_kind", "")
            if equality_kind not in REQUIRED_EQUALITY_KINDS:
                issues.append(
                    f"{table.spec.gate}: {table.spec.path}:{index} "
                    f"unknown equality_kind={equality_kind!r}"
                )
        elif table.spec.path == "scalar_firewall.csv":
            require_bool_text(table, index, row, "excluded_from_dependency_ledger", "true", issues)


def check_coverage(table: CsvTable, issues: list[str]) -> None:
    if not table.rows:
        return
    if table.spec.path == "beilinson_levels.csv":
        present = {row.get("level_id", "") for row in table.rows}
        missing = sorted(REQUIRED_BEILINSON_LEVELS - present)
        extra = sorted(present - REQUIRED_BEILINSON_LEVELS)
        if missing:
            issues.append(
                f"{table.spec.gate}: beilinson_levels.csv missing level_id rows: "
                f"{','.join(missing)}"
            )
        if extra:
            issues.append(
                f"{table.spec.gate}: beilinson_levels.csv has unexpected level_id rows: "
                f"{','.join(extra)}"
            )
    elif table.spec.path == "equality_sites.csv":
        present = {row.get("site_kind", "") for row in table.rows}
        missing = sorted(REQUIRED_EQUALITY_SITE_KINDS - present)
        extra = sorted(present - REQUIRED_EQUALITY_SITE_KINDS)
        if missing:
            issues.append(
                f"{table.spec.gate}: equality_sites.csv missing site_kind rows: "
                f"{','.join(missing)}"
            )
        if extra:
            issues.append(
                f"{table.spec.gate}: equality_sites.csv has unexpected site_kind rows: "
                f"{','.join(extra)}"
            )
    elif table.spec.path == "definition_separation.csv":
        present = {row.get("separation_id", "") for row in table.rows}
        missing = sorted(REQUIRED_DEFINITION_SEPARATIONS - present)
        extra = sorted(present - REQUIRED_DEFINITION_SEPARATIONS)
        if missing:
            issues.append(
                f"{table.spec.gate}: definition_separation.csv missing separation_id rows: "
                f"{','.join(missing)}"
            )
        if extra:
            issues.append(
                f"{table.spec.gate}: definition_separation.csv has unexpected separation_id rows: "
                f"{','.join(extra)}"
            )
    elif table.spec.path == "obstruction_independence.csv":
        present = {row.get("datum_id", "") for row in table.rows}
        missing = sorted(REQUIRED_OBSTRUCTION_INDEPENDENCE_ROWS - present)
        extra = sorted(present - REQUIRED_OBSTRUCTION_INDEPENDENCE_ROWS)
        if missing:
            issues.append(
                f"{table.spec.gate}: obstruction_independence.csv missing datum_id rows: "
                f"{','.join(missing)}"
            )
        if extra:
            issues.append(
                f"{table.spec.gate}: obstruction_independence.csv has unexpected datum_id rows: "
                f"{','.join(extra)}"
            )
    elif table.spec.path == "theorem_dependencies.csv":
        present = {row.get("theorem_type", "") for row in table.rows}
        missing = sorted(REQUIRED_THEOREM_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: theorem_dependencies.csv missing theorem_type rows: "
                f"{','.join(missing)}"
            )
    elif table.spec.path == "forbidden_edges.csv":
        present = {row.get("forbidden_dependency_type", "") for row in table.rows}
        missing = sorted(REQUIRED_FORBIDDEN_TYPES - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: forbidden_edges.csv missing forbidden_dependency_type rows: "
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
    elif table.spec.path == "level_equalities.csv":
        present = {row.get("equality_kind", "") for row in table.rows}
        missing = sorted(REQUIRED_EQUALITY_KINDS - present)
        if missing:
            issues.append(
                f"{table.spec.gate}: level_equalities.csv missing equality_kind rows: "
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
    print("theorem dependency fixture verifier")
    print("mode: check-only")
    print(f"fixture: {fixture}")
    print(f"status: {status}")
    print(f"schema_only_complete: {str(schema_only_complete).lower()}")
    print("dependency_certification: false")
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
