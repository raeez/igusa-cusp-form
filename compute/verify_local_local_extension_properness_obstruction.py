#!/usr/bin/env python3
"""Verify the local/local extension target-properness packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "LOCAL_LOCAL_TARGET_PROPERNESS_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "local_local_extension_properness.v1"
EXPECTED_KIND = "local_local_extension_properness"
EXTENSION_COLUMNS = (
    "stack_row_id",
    "R_id",
    "local_left_colour_id",
    "local_right_colour_id",
    "target_colour_id",
    "left_index_set_id",
    "right_index_set_id",
    "target_index_set_id",
    "extension_stack_id",
    "relative_quot_model_id",
    "exact_sequence_convention",
    "extension_closure_source",
    "finite_type_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_EXTENSION = {
    "stack_row_id": "LL_ext_alpha_beta_gamma_R_I_J_K",
    "R_id": "R",
    "local_left_colour_id": "alpha_I_to_Gamma_R_loc",
    "local_right_colour_id": "beta_J_to_Gamma_R_loc",
    "target_colour_id": "gamma_equals_sum_alpha_plus_sum_beta",
    "left_index_set_id": "I",
    "right_index_set_id": "J",
    "target_index_set_id": "K_equals_I_disjoint_union_J_mod_collisions",
    "extension_stack_id": "E_LL_alpha_beta_gamma_R_I_J_K",
    "relative_quot_model_id": "RelQuot_gamma_to_alpha_kernel_beta",
    "exact_sequence_convention": "zero_to_A_beta_J_to_B_gamma_K_to_A_alpha_I_to_zero",
    "extension_closure_source": "retained_extension_closure_rows",
    "finite_type_defect_rank": "0",
    "check_status": "verified",
}
TARGET_MAP_COLUMNS = (
    "map_row_id",
    "R_id",
    "extension_stack_id",
    "source_map_formula",
    "target_map_formula",
    "quotient_projection",
    "kernel_projection",
    "target_map_defect_rank",
    "source_map_defined",
    "source_properness_asserted",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_TARGET_MAP = {
    "map_row_id": "LL_maps_alpha_beta_gamma_R",
    "R_id": "R",
    "extension_stack_id": "E_LL_alpha_beta_gamma_R_I_J_K",
    "source_map_formula": "p_LL=(quotient_A_alpha_I,kernel_A_beta_J)",
    "target_map_formula": "q_LL=B_gamma_K",
    "quotient_projection": "B_gamma_K_to_A_alpha_I",
    "kernel_projection": "kernel_A_beta_J_to_B_gamma_K",
    "target_map_defect_rank": "0",
    "source_map_defined": "true",
    "source_properness_asserted": "false",
    "check_status": "verified",
}
PROPERNESS_COLUMNS = (
    "properness_id",
    "R_id",
    "extension_stack_id",
    "target_map_id",
    "relative_quot_projective",
    "closed_support_restriction",
    "retained_colour_restriction",
    "target_properness_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_PROPERNESS = {
    "properness_id": "LL_q_proper_alpha_beta_gamma_R",
    "R_id": "R",
    "extension_stack_id": "E_LL_alpha_beta_gamma_R_I_J_K",
    "target_map_id": "q_LL",
    "relative_quot_projective": "true",
    "closed_support_restriction": "true",
    "retained_colour_restriction": "true",
    "target_properness_defect_rank": "0",
    "check_status": "verified",
}
SOURCE_NONPROPER_COLUMNS = (
    "source_row_id",
    "R_id",
    "extension_stack_id",
    "source_map_id",
    "generic_fibre_model",
    "source_properness_asserted",
    "source_properness_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_SOURCE_NONPROPER = {
    "source_row_id": "LL_p_not_proper_general",
    "R_id": "R",
    "extension_stack_id": "E_LL_alpha_beta_gamma_R_I_J_K",
    "source_map_id": "p_LL",
    "generic_fibre_model": "Ext1(A_alpha_I,A_beta_J)_mod_Hom",
    "source_properness_asserted": "false",
    "source_properness_defect_rank": "1",
    "check_status": "verified",
}
EMPTY_TABLES = {
    "descent_rows.csv": (
        "descent_id",
        "R_id",
        "extension_stack_id",
        "symmetric_descent_defect_rank",
        "collision_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "collision_rows.csv": (
        "collision_id",
        "R_id",
        "extension_stack_id",
        "collision_map_id",
        "collision_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "thom_sebastiani_rows.csv": (
        "ts_id",
        "R_id",
        "extension_stack_id",
        "vanishing_cycle_source_id",
        "vanishing_cycle_target_id",
        "ts_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "extension_stack_id",
        "target_properness_compatibility_defect_rank",
        "descent_compatibility_defect_rank",
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
    "properness_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "descent_rows",
        "collision_rows",
        "thom_sebastiani_rows",
        "transition_rows",
        "aggregate_population_rows",
        "compact_support_model_rows",
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
        "local_local_definition_only",
        "extension_closure_only",
        "source_map_properness",
        "quotient_first",
        "mixed_as_local_local",
        "wrapped_wrapped_as_local_local",
        "scalar_trace",
        "Borcherds_s_degree",
        "ordinary_Ran_uncoloured",
        "empty_hybrid_carrier",
    }
)
EXTENSION_CLOSURE_COLUMNS = (
    "extension_closure_id",
    "window_id",
    "left_hn_type_id",
    "right_hn_type_id",
    "middle_hn_type_id",
    "middle_object_id",
    "extension_word_id",
    "retained_middle_term",
    "extension_closure_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
UNIVERSAL_COLUMNS = (
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
)
CLOSED_SUBSTACK_COLUMNS = (
    "closed_substack_id",
    "substack_id",
    "translation_rigidification_id",
    "closed_embedding_id",
    "closed_in_ambient",
    "finite_type_status",
    "finite_residual_inertia",
    "closure_defect_rank",
    "inertia_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check local/local extension target-properness packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/local_local_extension_properness"),
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
        "fixture_name": "local_local_extension_properness",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "local_local_extension_stack_model": True,
        "relative_quot_model": True,
        "target_map_proper": True,
        "source_map_proper": False,
        "extension_closure_imported": True,
        "universal_complexes_imported": True,
        "descent_certification": False,
        "collision_certification": False,
        "thom_sebastiani_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "extension_stack_rows.csv",
        "target_map_rows.csv",
        "target_properness_rows.csv",
        "source_nonproper_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected LL properness tables")
    expected_imports = {
        "certificates/hybrid/local_local_correspondence_definition",
        "certificates/hybrid/local_stratum_b0_prestack_definition",
        "certificates/moduli/retained_extension_closure",
        "certificates/moduli/retained_universal_complexes",
        "certificates/moduli/retained_closed_substacks",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected LL properness imports")


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
        if row.get("properness_status") != "missing_open_obligation":
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
    root = fixture.parent.parent
    local_local = load_json(
        fixture.parent / "local_local_correspondence_definition" / MANIFEST_NAME,
        issues,
    )
    if local_local and local_local.get("status") != "LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED":
        issues.append("local/local correspondence manifest status is not verified")
    local = load_json(fixture.parent / "local_stratum_b0_prestack_definition" / MANIFEST_NAME, issues)
    if local and local.get("status") != "LOCAL_STRATUM_B0_PRESTACK_DEFINITION_VERIFIED":
        issues.append("local stratum manifest status is not verified")

    extension_fixture = root / "moduli" / "retained_extension_closure"
    universal_fixture = root / "moduli" / "retained_universal_complexes"
    closed_fixture = root / "moduli" / "retained_closed_substacks"
    extension_manifest = load_json(extension_fixture / MANIFEST_NAME, issues)
    if extension_manifest:
        if extension_manifest.get("certified") is not True:
            issues.append("retained extension closure manifest is not certified")
        if extension_manifest.get("extension_closure") is not True:
            issues.append("retained extension closure manifest lacks extension_closure")
        if extension_manifest.get("extension_flag_stacks") is not False:
            issues.append("retained extension closure must not claim extension flag stacks")
    universal_manifest = load_json(universal_fixture / MANIFEST_NAME, issues)
    if universal_manifest:
        if universal_manifest.get("certified") is not True:
            issues.append("retained universal complexes manifest is not certified")
        if universal_manifest.get("universal_complexes") is not True:
            issues.append("retained universal complexes manifest lacks universal complexes")
    closed_manifest = load_json(closed_fixture / MANIFEST_NAME, issues)
    if closed_manifest:
        if closed_manifest.get("certified") is not True:
            issues.append("retained closed substacks manifest is not certified")
        if closed_manifest.get("retained_closed_substacks") is not True:
            issues.append("retained closed substacks manifest lacks retained closed substacks")

    extension_rows = load_csv(
        extension_fixture / "extension_closure.csv",
        EXTENSION_CLOSURE_COLUMNS,
        issues,
    ).rows
    universal_rows = load_csv(
        universal_fixture / "universal_complexes.csv",
        UNIVERSAL_COLUMNS,
        issues,
    ).rows
    closed_rows = load_csv(
        closed_fixture / "retained_closed_substacks.csv",
        CLOSED_SUBSTACK_COLUMNS,
        issues,
    ).rows
    if len(extension_rows) != 4:
        issues.append("retained extension closure row count must be 4")
    if len(universal_rows) != 3:
        issues.append("retained universal complex row count must be 3")
    if len(closed_rows) != 3:
        issues.append("retained closed substack row count must be 3")
    for index, row in enumerate(extension_rows, start=2):
        if row.get("retained_middle_term") != "true":
            issues.append(f"extension_closure.csv:{index} middle term not retained")
        if row.get("extension_closure_defect_rank") != "0":
            issues.append(f"extension_closure.csv:{index} closure defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"extension_closure.csv:{index} is not verified")
    for index, row in enumerate(universal_rows, start=2):
        if row.get("descent_defect_rank") != "0":
            issues.append(f"universal_complexes.csv:{index} descent defect nonzero")
        if row.get("perfection_defect_rank") != "0":
            issues.append(f"universal_complexes.csv:{index} perfection defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"universal_complexes.csv:{index} is not verified")
    for index, row in enumerate(closed_rows, start=2):
        if row.get("closed_in_ambient") != "true":
            issues.append(f"retained_closed_substacks.csv:{index} is not closed")
        if row.get("closure_defect_rank") != "0":
            issues.append(f"retained_closed_substacks.csv:{index} closure defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"retained_closed_substacks.csv:{index} is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "extension_stack_rows.csv", EXTENSION_COLUMNS, EXPECTED_EXTENSION, issues)
    check_single_row(fixture, "target_map_rows.csv", TARGET_MAP_COLUMNS, EXPECTED_TARGET_MAP, issues)
    check_single_row(fixture, "target_properness_rows.csv", PROPERNESS_COLUMNS, EXPECTED_PROPERNESS, issues)
    check_single_row(
        fixture,
        "source_nonproper_rows.csv",
        SOURCE_NONPROPER_COLUMNS,
        EXPECTED_SOURCE_NONPROPER,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("LOCAL_LOCAL_TARGET_PROPERNESS_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
