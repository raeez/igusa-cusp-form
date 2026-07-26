#!/usr/bin/env python3
"""Verify the wrapped/wrapped extension target-admissibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_WRAPPED_ADMISSIBILITY_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "wrapped_wrapped_extension_admissibility.v1"
EXPECTED_KIND = "wrapped_wrapped_extension_admissibility"

EXTENSION_COLUMNS = (
    "stack_row_id",
    "R_id",
    "wrapped_left_colour_id",
    "wrapped_right_colour_id",
    "target_colour_id",
    "extension_stack_id",
    "relative_quot_model_id",
    "exact_sequence_convention",
    "closed_endpoint_conditions",
    "extension_closure_source",
    "finite_type_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_EXTENSION = {
    "stack_row_id": "WW_ext_eta1_eta2_zeta_R",
    "R_id": "R",
    "wrapped_left_colour_id": "eta_1_in_Gamma_R_wr",
    "wrapped_right_colour_id": "eta_2_in_Gamma_R_wr",
    "target_colour_id": "zeta_equals_eta_1_plus_eta_2_in_Gamma_R_wr",
    "extension_stack_id": "E_WW_eta1_eta2_zeta_R",
    "relative_quot_model_id": "RelQuot_zeta_to_eta1_kernel_eta2",
    "exact_sequence_convention": "zero_to_W_eta_2_to_B_zeta_to_W_eta_1_to_zero",
    "closed_endpoint_conditions": "retained_closed_substacks",
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
    "map_row_id": "WW_maps_eta1_eta2_zeta_R",
    "R_id": "R",
    "extension_stack_id": "E_WW_eta1_eta2_zeta_R",
    "source_map_formula": "p_WW=(quotient_W_eta_1,kernel_W_eta_2)",
    "target_map_formula": "q_WW=B_zeta",
    "quotient_projection": "B_zeta_to_W_eta_1",
    "kernel_projection": "kernel_W_eta_2_to_B_zeta",
    "target_map_defect_rank": "0",
    "source_map_defined": "true",
    "source_properness_asserted": "false",
    "check_status": "verified",
}

ADMISSIBILITY_COLUMNS = (
    "admissibility_id",
    "R_id",
    "extension_stack_id",
    "target_map_id",
    "relative_quot_projective",
    "closed_endpoint_restriction",
    "wrapped_target_finite_type",
    "proper_target_pushforward_admissible",
    "admissibility_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ADMISSIBILITY = {
    "admissibility_id": "WW_q_admissible_eta1_eta2_zeta_R",
    "R_id": "R",
    "extension_stack_id": "E_WW_eta1_eta2_zeta_R",
    "target_map_id": "q_WW",
    "relative_quot_projective": "true",
    "closed_endpoint_restriction": "true",
    "wrapped_target_finite_type": "true",
    "proper_target_pushforward_admissible": "true",
    "admissibility_defect_rank": "0",
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
    "source_row_id": "WW_p_not_proper_general",
    "R_id": "R",
    "extension_stack_id": "E_WW_eta1_eta2_zeta_R",
    "source_map_id": "p_WW",
    "generic_fibre_model": "Ext1(W_eta_1,W_eta_2)_mod_Hom",
    "source_properness_asserted": "false",
    "source_properness_defect_rank": "1",
    "check_status": "verified",
}

EMPTY_TABLES = {
    "compact_support_model_rows.csv": (
        "compact_support_id",
        "R_id",
        "extension_stack_id",
        "model_status",
        "compact_support_model_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_memory_rows.csv": (
        "anchor_memory_id",
        "R_id",
        "extension_stack_id",
        "left_source_anchor_id",
        "right_source_anchor_id",
        "target_anchor_id",
        "relative_anchor_id",
        "anchor_memory_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "symmetric_descent_rows.csv": (
        "symmetric_descent_id",
        "R_id",
        "extension_stack_id",
        "swap_morphism_id",
        "symmetric_descent_defect_rank",
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
        "wrapped_wrapped_correspondence_morphism_id",
        "target_admissibility_compatibility_defect_rank",
        "anchor_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "R_id",
        "extension_stack_id",
        "reduced_correspondence_id",
        "quotient_descent_defect_rank",
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
    "admissibility_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "compact_support_model_rows",
        "anchor_memory_rows",
        "symmetric_descent_rows",
        "thom_sebastiani_rows",
        "transition_rows",
        "quotient_descent_rows",
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
        "wrapped_wrapped_definition_only",
        "mixed_admissibility_only",
        "local_local_properness_only",
        "wrapped_prequotient_finite_type_only",
        "extension_closure_only",
        "retained_closed_substacks_only",
        "source_map_properness",
        "compact_support_model",
        "symmetric_descent",
        "thom_sebastiani",
        "quotient_first",
        "scalar_trace",
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
WRAPPED_FINITE_TYPE_COLUMNS = (
    "finite_type_id",
    "R_id",
    "wrapped_colour_id",
    "prequotient_stack_id",
    "class_index_set",
    "semistable_source",
    "rigidification_source",
    "wrapped_locus_kind",
    "finite_type_status",
    "finite_type_defect_rank",
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
        description="Check wrapped/wrapped extension target-admissibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_wrapped_extension_admissibility"),
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
        "fixture_name": "wrapped_wrapped_extension_admissibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "wrapped_wrapped_extension_stack_model": True,
        "relative_quot_model": True,
        "target_map_proper": True,
        "proper_target_pushforward_admissible": True,
        "source_map_proper": False,
        "before_e_quotient": True,
        "closed_endpoint_conditions_imported": True,
        "extension_closure_imported": True,
        "universal_complexes_imported": True,
        "wrapped_prequotient_finite_type_imported": True,
        "compact_support_model_certification": False,
        "anchor_memory_certification": False,
        "symmetric_descent_certification": False,
        "thom_sebastiani_certification": False,
        "transition_certification": False,
        "quotient_descent_certification": False,
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
        "target_admissibility_rows.csv",
        "source_nonproper_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected WW admissibility tables")
    expected_imports = {
        "certificates/hybrid/wrapped_wrapped_correspondence_definition",
        "certificates/hybrid/equivariant_wrapped_prequotient_definition",
        "certificates/hybrid/wrapped_prequotient_finite_type",
        "certificates/moduli/retained_extension_closure",
        "certificates/moduli/retained_universal_complexes",
        "certificates/moduli/retained_closed_substacks",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected WW admissibility imports")


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
        if row.get("admissibility_status") != "missing_open_obligation":
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
    expected_hybrid_statuses = (
        (
            "wrapped_wrapped_correspondence_definition",
            "WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
        (
            "equivariant_wrapped_prequotient_definition",
            "E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_VERIFIED",
        ),
        (
            "wrapped_prequotient_finite_type",
            "WRAPPED_PREQUOTIENT_FINITE_TYPE_VERIFIED",
        ),
    )
    for relative, expected_status in expected_hybrid_statuses:
        manifest = load_json(hybrid_root / relative / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )

    extension_fixture = certificate_root / "moduli" / "retained_extension_closure"
    universal_fixture = certificate_root / "moduli" / "retained_universal_complexes"
    closed_fixture = certificate_root / "moduli" / "retained_closed_substacks"

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
    wrapped_ft_rows = load_csv(
        hybrid_root / "wrapped_prequotient_finite_type" / "finite_type_rows.csv",
        WRAPPED_FINITE_TYPE_COLUMNS,
        issues,
    ).rows

    if len(extension_rows) != 4:
        issues.append("retained extension closure row count must be 4")
    if len(universal_rows) != 3:
        issues.append("retained universal complex row count must be 3")
    if len(closed_rows) != 3:
        issues.append("retained closed substack row count must be 3")
    if len(wrapped_ft_rows) != 1:
        issues.append("wrapped prequotient finite-type row count must be 1")

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
    for index, row in enumerate(wrapped_ft_rows, start=2):
        if row.get("finite_type_status") != "finite_type_verified":
            issues.append(f"finite_type_rows.csv:{index} finite-type status is not verified")
        if row.get("finite_type_defect_rank") != "0":
            issues.append(f"finite_type_rows.csv:{index} finite-type defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"finite_type_rows.csv:{index} is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "extension_stack_rows.csv", EXTENSION_COLUMNS, EXPECTED_EXTENSION, issues)
    check_single_row(fixture, "target_map_rows.csv", TARGET_MAP_COLUMNS, EXPECTED_TARGET_MAP, issues)
    check_single_row(
        fixture,
        "target_admissibility_rows.csv",
        ADMISSIBILITY_COLUMNS,
        EXPECTED_ADMISSIBILITY,
        issues,
    )
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
    check_import_statuses(fixture, issues)
    if issues:
        print("WRAPPED_WRAPPED_ADMISSIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
