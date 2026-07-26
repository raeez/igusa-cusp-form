#!/usr/bin/env python3
"""Verify the finite anchor-residual definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "ANCHOR_RESIDUAL_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "anchor_residual_definition.v1"
EXPECTED_KIND = "anchor_residual_definition"
TARGET_COLUMNS = (
    "target_id",
    "R_id",
    "wrapped_colour_id",
    "repaired_anchor_target",
    "determinant_projection",
    "extra_anchor_restriction",
    "monoid_operation",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_TARGET = {
    "target_id": "repaired_anchor_target_sym_jh_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "repaired_anchor_target": "Sym^r_eta_Pic0_E",
    "determinant_projection": "Abel_sum_to_Pic0_E",
    "extra_anchor_restriction": "degree_zero_jordan_holder_divisor",
    "monoid_operation": "divisor_union_on_exact_sequences",
    "check_status": "verified",
}
COMPONENT_COLUMNS = (
    "component_id",
    "symbol",
    "component_type",
    "domain",
    "target_or_defect",
    "zero_condition",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_COMPONENTS = {
    "anchor_residual_existence": {
        "symbol": "o_lambda_ex",
        "component_type": "existence",
        "domain": "wrapped_prequotient_rows",
        "target_or_defect": "repaired_anchor_maps_to_Sym^r_Pic0_E",
        "zero_condition": "every_wrapped_colour_has_functorial_repaired_anchor",
    },
    "anchor_residual_unit": {
        "symbol": "o_lambda_unit",
        "component_type": "unit_weight",
        "domain": "repaired_anchor_E_action",
        "target_or_defect": "finite_cover_unit_weight_normalization",
        "zero_condition": "translation_weight_one_after_finite_cover",
    },
    "anchor_residual_loss": {
        "symbol": "o_lambda_loss",
        "component_type": "losslessness",
        "domain": "kernel_pair",
        "target_or_defect": "kernel_pair_minus_retained_equivalence_relation",
        "zero_condition": "kernel_pair_equals_retained_equivalence_relation",
    },
    "anchor_residual_multi": {
        "symbol": "o_lambda_multi",
        "component_type": "multiplicativity",
        "domain": "unreduced_LW_WL_WW_LWL_correspondences",
        "target_or_defect": "equalizer_complement_of_target_vs_divisor_union_sources",
        "zero_condition": "target_anchor_equals_divisor_union_of_sources",
    },
    "anchor_residual_transition": {
        "symbol": "o_lambda_tr",
        "component_type": "transition",
        "domain": "HN_transition_pairs",
        "target_or_defect": "equalizer_complement_of_Rprime_to_R_anchor_square",
        "zero_condition": "anchor_square_commutes_under_HN_restriction",
    },
}
EMPTY_TABLES = {
    "residual_vanishing_rows.csv": (
        "vanishing_id",
        "R_id",
        "residual_component",
        "vanishing_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "first_window_vanishing_rows.csv": (
        "first_window_id",
        "R_id",
        "residual_component",
        "window_id",
        "vanishing_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "descent_id",
        "R_id",
        "repaired_anchor_target",
        "quotient_pseudofunctor_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "stabilizer_linearization_rows.csv": (
        "linearization_id",
        "R_id",
        "wrapped_colour_id",
        "stabilizer_id",
        "character_formula",
        "linearization_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "finite_stage_population_rows.csv": (
        "population_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "repaired_anchor_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_compatibility_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "repaired_anchor_morphism_id",
        "transition_defect_rank",
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
    "residual_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "residual_vanishing_rows",
        "first_window_vanishing_rows",
        "quotient_descent_rows",
        "stabilizer_linearization_rows",
        "finite_stage_population_rows",
        "transition_compatibility_rows",
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
        "determinant_anchor_only",
        "extra_anchor_data_only",
        "source_target_memory_only",
        "chi_zero_degeneracy_only",
        "first_window_vanishing",
        "quotient_descent",
        "stabilizer_linearization",
        "scalar_Fock_factor",
        "Borcherds_s_degree",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite anchor-residual definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/anchor_residual_definition"),
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
        "fixture_name": "anchor_residual_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "anchor_residual_defined": True,
        "repaired_anchor_target": "Sym^r_Pic0_E",
        "determinant_projection": "Abel_sum_to_Pic0_E",
        "extra_anchor_restriction": "degree_zero_jordan_holder_divisor",
        "vanishing_certification": False,
        "first_window_vanishing_certification": False,
        "quotient_descent_certification": False,
        "stabilizer_linearization_certification": False,
        "finite_stage_population_certification": False,
        "transition_compatibility_certification": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_components = {
        "existence",
        "unit_weight",
        "losslessness",
        "multiplicativity",
        "transition",
    }
    if set(manifest.get("components", [])) != expected_components:
        issues.append("manifest components do not match the five anchor residual components")
    expected_tables = set(EMPTY_TABLES) | {
        "target_model_rows.csv",
        "residual_component_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected anchor-residual tables")
    expected_imports = {
        "certificates/hybrid/determinant_anchor_extra_anchor_data",
        "certificates/hybrid/source_target_anchor_memory_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected anchor-residual imports")


def check_target(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "target_model_rows.csv", TARGET_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("target_model_rows.csv must contain exactly one target row")
        return
    row = table.rows[0]
    for key, value in EXPECTED_TARGET.items():
        if row.get(key) != value:
            issues.append(f"target_model_rows.csv {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("proof_reference"):
        issues.append("target_model_rows.csv row lacks proof_reference")


def check_components(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "residual_component_rows.csv", COMPONENT_COLUMNS, issues)
    ids = {row.get("component_id", "") for row in table.rows}
    expected_ids = set(EXPECTED_COMPONENTS)
    missing = sorted(expected_ids - ids)
    extra = sorted(ids - expected_ids)
    if missing:
        issues.append("missing residual components: " + ", ".join(missing))
    if extra:
        issues.append("unexpected residual components: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        component_id = row.get("component_id", "")
        expected = EXPECTED_COMPONENTS.get(component_id)
        if not expected:
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"residual_component_rows.csv:{index} {key}: "
                    f"expected {value!r}, got {row.get(key)!r}"
                )
        if row.get("check_status") != "verified":
            issues.append(f"residual_component_rows.csv:{index} is not verified")
        if not row.get("proof_reference"):
            issues.append(f"residual_component_rows.csv:{index} lacks proof_reference")


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
        if row.get("residual_status") != "missing_open_obligation":
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


def check_imports(fixture: Path, issues: list[str]) -> None:
    extra_anchor_manifest = load_json(
        fixture.parent / "determinant_anchor_extra_anchor_data" / MANIFEST_NAME,
        issues,
    )
    if extra_anchor_manifest and extra_anchor_manifest.get("status") != (
        "DETERMINANT_ANCHOR_EXTRA_ANCHOR_DATA_VERIFIED"
    ):
        issues.append("determinant_anchor_extra_anchor_data import is not verified")
    memory_manifest = load_json(
        fixture.parent / "source_target_anchor_memory_definition" / MANIFEST_NAME,
        issues,
    )
    if memory_manifest and memory_manifest.get("status") != (
        "SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED"
    ):
        issues.append("source_target_anchor_memory_definition import is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_target(fixture, issues)
    check_components(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("ANCHOR_RESIDUAL_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
