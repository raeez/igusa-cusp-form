#!/usr/bin/env python3
"""Verify the compact-support exceptional pushforward model packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "compact_support_exceptional_pushforward_model.v1"
EXPECTED_KIND = "compact_support_exceptional_pushforward_model"

MODEL_COLUMNS = (
    "model_id",
    "R_id",
    "map_symbol",
    "source_stack_symbol",
    "compactification_stack_symbol",
    "target_stack_symbol",
    "open_immersion_symbol",
    "proper_map_symbol",
    "coefficient_complex_symbol",
    "exceptional_pushforward_formula",
    "finite_residual_inertia_required",
    "constructibility_required",
    "model_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_MODEL = {
    "model_id": "compact_support_exceptional_pushforward_model_R",
    "R_id": "R",
    "map_symbol": "f",
    "source_stack_symbol": "E",
    "compactification_stack_symbol": "Ebar_f",
    "target_stack_symbol": "Z",
    "open_immersion_symbol": "j_f",
    "proper_map_symbol": "bar_f",
    "coefficient_complex_symbol": "K_E",
    "exceptional_pushforward_formula": "f_cs_bang_K=bar_f_star_j_f_bang_K",
    "finite_residual_inertia_required": "true",
    "constructibility_required": "true",
    "model_defect_rank": "0",
    "check_status": "verified",
}

OPERATION_COLUMNS = (
    "operation_id",
    "R_id",
    "map_role",
    "input_functor",
    "compact_support_functor",
    "formula",
    "operation_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_OPERATIONS = {
    "target_pushforward_q": {
        "R_id": "R",
        "map_role": "target_leg",
        "input_functor": "pullback_then_target_pushforward",
        "compact_support_functor": "q_cs_bang",
        "formula": "q_cs_bang(K_E)=bar_q_star_j_q_bang(K_E)",
        "operation_defect_rank": "0",
        "check_status": "verified",
    },
    "source_pushforward_p": {
        "R_id": "R",
        "map_role": "source_leg",
        "input_functor": "pullback_then_source_pushforward",
        "compact_support_functor": "p_cs_bang",
        "formula": "p_cs_bang(K_E)=bar_p_star_j_p_bang(K_E)",
        "operation_defect_rank": "0",
        "check_status": "verified",
    },
}

PROPER_COLUMNS = (
    "specialization_id",
    "R_id",
    "map_symbol",
    "proper_map_condition",
    "compactification_choice",
    "formula",
    "specialization_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_PROPER = {
    "specialization_id": "proper_map_identity_compactification",
    "R_id": "R",
    "map_symbol": "f",
    "proper_map_condition": "f_proper",
    "compactification_choice": "j_f_equals_id_E_and_Ebar_f_equals_E_and_bar_f_equals_f",
    "formula": "f_cs_bang_equals_f_star",
    "specialization_defect_rank": "0",
    "check_status": "verified",
}

EMPTY_TABLES = {
    "map_population_rows.csv": (
        "population_id",
        "R_id",
        "correspondence_type",
        "map_symbol",
        "compactification_model_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "choice_independence_rows.csv": (
        "independence_id",
        "R_id",
        "map_symbol",
        "compactification_pair_id",
        "comparison_isomorphism_id",
        "independence_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "base_change_rows.csv": (
        "base_change_id",
        "R_id",
        "map_symbol",
        "square_id",
        "base_change_isomorphism_id",
        "base_change_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "projection_formula_rows.csv": (
        "projection_formula_id",
        "R_id",
        "map_symbol",
        "coefficient_object_id",
        "projection_formula_isomorphism_id",
        "projection_formula_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "thom_sebastiani_rows.csv": (
        "ts_id",
        "R_id",
        "map_symbol",
        "vanishing_cycle_source_id",
        "vanishing_cycle_target_id",
        "ts_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "symmetric_descent_rows.csv": (
        "symmetric_descent_id",
        "R_id",
        "correspondence_type",
        "symmetry_morphism_id",
        "symmetric_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "R_id",
        "map_symbol",
        "reduced_map_symbol",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "map_symbol",
        "compactification_compatibility_defect_rank",
        "pushforward_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "correspondence_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
}

OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "model_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "map_population_rows",
        "choice_independence_rows",
        "base_change_rows",
        "projection_formula_rows",
        "thom_sebastiani_rows",
        "symmetric_descent_rows",
        "quotient_descent_rows",
        "transition_rows",
        "aggregate_population_rows",
    }
)

SCALAR_FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "target_properness_only",
        "mixed_admissibility_only",
        "wrapped_wrapped_admissibility_only",
        "raw_nonproper_pushforward",
        "choice_independence",
        "base_change",
        "projection_formula",
        "thom_sebastiani",
        "quotient_first",
        "scalar_trace",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check compact-support exceptional pushforward model packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/compact_support_exceptional_pushforward_model"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


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


def load_csv(path: Path, columns: tuple[str, ...], issues: list[str]) -> CsvTable:
    if not path.is_file():
        issues.append(f"missing table: {path}")
        return CsvTable(path, [])
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            issues.append(f"header mismatch in {path}; expected {','.join(columns)}")
        rows = nonempty_rows(reader)
    return CsvTable(path, rows)


def load_json(path: Path, issues: list[str]) -> dict[str, object]:
    if not path.is_file():
        issues.append(f"missing JSON file: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {path}")
        return {}
    return value


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "compact_support_exceptional_pushforward_model",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "compact_support_model_defined": True,
        "compactification_data_defined": True,
        "extension_by_zero_formula_defined": True,
        "proper_pushforward_formula_defined": True,
        "proper_map_specialization_defined": True,
        "finite_residual_inertia_required": True,
        "coefficient_constructibility_required": True,
        "choice_independence_certification": False,
        "map_population_certification": False,
        "base_change_certification": False,
        "projection_formula_certification": False,
        "thom_sebastiani_certification": False,
        "symmetric_descent_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "hall_product_certification": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "model_rows.csv",
        "operation_rows.csv",
        "proper_specialization_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected compact-support tables")
    expected_imports = {
        "certificates/hybrid/local_local_extension_properness",
        "certificates/hybrid/mixed_local_wrapped_extension_admissibility",
        "certificates/hybrid/wrapped_wrapped_extension_admissibility",
        "certificates/moduli/retained_universal_complexes",
        "certificates/moduli/retained_closed_substacks",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected compact-support imports")


def check_single_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected: dict[str, str],
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"{table_name} {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append(f"{table_name} row lacks proof_reference")


def check_operations(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "operation_rows.csv", OPERATION_COLUMNS, issues)
    if len(table.rows) != len(EXPECTED_OPERATIONS):
        issues.append("operation_rows.csv must contain the q and p compact-support rows")
        return
    by_id = {row.get("operation_id", ""): row for row in table.rows}
    missing = sorted(set(EXPECTED_OPERATIONS) - set(by_id))
    extra = sorted(set(by_id) - set(EXPECTED_OPERATIONS))
    if missing:
        issues.append("missing operation rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected operation rows: " + ", ".join(extra))
    for operation_id, expected in EXPECTED_OPERATIONS.items():
        row = by_id.get(operation_id)
        if row is None:
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"operation {operation_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"operation row {operation_id} lacks proof_reference")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until later rows are supplied")


def check_obligations(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "blocked_obligations.csv", OBLIGATION_COLUMNS, issues)
    ids = {row.get("obligation_id", "") for row in table.rows}
    missing = sorted(REQUIRED_OBLIGATIONS - ids)
    extra = sorted(ids - REQUIRED_OBLIGATIONS)
    if missing:
        issues.append("missing obligation rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected obligation rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("model_status") != "missing_open_obligation":
            issues.append(f"blocked_obligations.csv:{index} has non-missing status")
        if row.get("check_status") != "verified":
            issues.append(f"blocked_obligations.csv:{index} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"blocked_obligations.csv:{index} lacks mathematical payload")


def check_firewall(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "scalar_firewall.csv", SCALAR_FIREWALL_COLUMNS, issues)
    substitutes = {row.get("forbidden_substitute", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_ROWS - substitutes)
    extra = sorted(substitutes - REQUIRED_FIREWALL_ROWS)
    if missing:
        issues.append("missing firewall rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected firewall rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("excluded") != "true":
            issues.append(f"scalar_firewall.csv:{index} excluded is not true")
        if row.get("defect_rank") != "0":
            issues.append(f"scalar_firewall.csv:{index} defect_rank is not zero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_firewall.csv:{index} is not verified")


def check_import_statuses(fixture: Path, issues: list[str]) -> None:
    hybrid_root = fixture.parent
    certificate_root = fixture.parent.parent
    for relative, expected_status in (
        ("local_local_extension_properness", "LOCAL_LOCAL_TARGET_PROPERNESS_VERIFIED"),
        (
            "mixed_local_wrapped_extension_admissibility",
            "MIXED_LOCAL_WRAPPED_ADMISSIBILITY_VERIFIED",
        ),
        (
            "wrapped_wrapped_extension_admissibility",
            "WRAPPED_WRAPPED_ADMISSIBILITY_VERIFIED",
        ),
    ):
        manifest = load_json(hybrid_root / relative / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )

    universal_manifest = load_json(
        certificate_root / "moduli" / "retained_universal_complexes" / MANIFEST_NAME,
        issues,
    )
    if universal_manifest:
        if universal_manifest.get("certified") is not True:
            issues.append("retained universal complexes manifest is not certified")
        if universal_manifest.get("universal_complexes") is not True:
            issues.append("retained universal complexes manifest lacks universal complexes")
    closed_manifest = load_json(
        certificate_root / "moduli" / "retained_closed_substacks" / MANIFEST_NAME,
        issues,
    )
    if closed_manifest:
        if closed_manifest.get("certified") is not True:
            issues.append("retained closed substacks manifest is not certified")
        if closed_manifest.get("retained_closed_substacks") is not True:
            issues.append("retained closed substacks manifest lacks retained closed substacks")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "model_rows.csv", MODEL_COLUMNS, EXPECTED_MODEL, issues)
    check_operations(fixture, issues)
    check_single_row(
        fixture,
        "proper_specialization_rows.csv",
        PROPER_COLUMNS,
        EXPECTED_PROPER,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
