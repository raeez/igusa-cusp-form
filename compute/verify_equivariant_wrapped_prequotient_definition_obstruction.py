#!/usr/bin/env python3
"""Verify the E-equivariant wrapped prequotient definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "equivariant_wrapped_prequotient_definition.v1"
EXPECTED_KIND = "equivariant_wrapped_prequotient_definition"
PREQUOTIENT_COLUMNS = (
    "prequotient_id",
    "R_id",
    "wrapped_colour_id",
    "ambient_stack_id",
    "scalar_rigidified_source",
    "universal_complex_source",
    "wrapped_condition",
    "prequotient_symbol",
    "forgetful_map_id",
    "quotient_symbol",
    "origin_id",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_PREQUOTIENT = {
    "prequotient_id": "M_eta_R_wr_rig",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "ambient_stack_id": "mathfrak_M_eta_R",
    "scalar_rigidified_source": "retained_scalar_rigidified_wrapped_locus",
    "universal_complex_source": "retained_universal_complexes",
    "wrapped_condition": "b_R_geom_eta_positive",
    "prequotient_symbol": "M_eta_R_wr_rig",
    "forgetful_map_id": "rho_eta_R_to_M_eta_R_wr",
    "quotient_symbol": "[M_eta_R_wr_rig_slash_E]",
    "origin_id": "0_E",
    "check_status": "verified",
}
ACTION_COLUMNS = (
    "action_id",
    "prequotient_id",
    "elliptic_curve_id",
    "origin_id",
    "action_formula",
    "identity_law",
    "composition_law",
    "colour_preservation",
    "e_equivariance_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ACTION = {
    "action_id": "E_action_M_eta_R_wr_rig",
    "prequotient_id": "M_eta_R_wr_rig",
    "elliptic_curve_id": "E",
    "origin_id": "0_E",
    "action_formula": "a_dot_A=(id_K3_times_tau_a)_star_A",
    "identity_law": "t_0_equals_id",
    "composition_law": "t_a_after_t_b_equals_t_a_plus_b",
    "colour_preservation": "b_R_geom_preserved_by_E_translation",
    "e_equivariance_defect_rank": "0",
    "check_status": "verified",
}
IMPORT_COLUMNS = (
    "import_id",
    "fixture_path",
    "import_status",
    "translation_row_count",
    "action_row_count",
    "quotient_row_count",
    "free_action_status",
    "translation_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_IMPORT = {
    "import_id": "retained_e_translation_import",
    "fixture_path": "certificates/moduli/retained_e_translation_rigidifications",
    "import_status": "RETAINED_E_TRANSLATION_RIGIDIFICATIONS_VERIFIED",
    "translation_row_count": "3",
    "action_row_count": "3",
    "quotient_row_count": "3",
    "free_action_status": "free_on_retained_rows",
    "translation_defect_rank": "0",
    "check_status": "verified",
}
EMPTY_TABLES = {
    "finite_type_rows.csv": (
        "finite_type_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "finite_type_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "properness_rows.csv": (
        "properness_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "properness_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_population_rows.csv": (
        "population_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "anchor_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_losslessness_rows.csv": (
        "losslessness_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "anchor_id",
        "anchor_loss_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "descent_id",
        "R_id",
        "prequotient_stack_id",
        "quotient_stack_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "prequotient_stack_id",
        "action_compatibility_defect_rank",
        "descent_compatibility_defect_rank",
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
    "prequotient_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "finite_type_rows",
        "properness_rows",
        "anchor_population_rows",
        "anchor_losslessness_rows",
        "quotient_descent_rows",
        "transition_rows",
        "aggregate_hybrid_population_rows",
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
        "wrapped_stratum_only",
        "retained_translation_quotient_only",
        "determinant_anchor_only",
        "finite_type_claim",
        "properness_claim",
        "quotient_first",
        "anchor_losslessness",
        "scalar_trace",
        "Borcherds_s_degree",
        "empty_hybrid_carrier",
    }
)
TRANSLATION_ACTION_COLUMNS = (
    "translation_action_id",
    "substack_id",
    "elliptic_curve_id",
    "origin_id",
    "action_defined",
    "action_free_on_retained_row",
    "action_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
TRANSLATION_RIGIDIFICATION_COLUMNS = (
    "translation_rigidification_id",
    "substack_id",
    "scalar_rigidification_id",
    "universal_id",
    "elliptic_curve_id",
    "translation_action_id",
    "quotient_stack_id",
    "translation_removed",
    "action_free_on_retained_row",
    "translation_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
QUOTIENT_COLUMNS = (
    "quotient_row_id",
    "translation_rigidification_id",
    "substack_id",
    "quotient_stack_id",
    "translation_removed",
    "quotient_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check E-equivariant wrapped prequotient definition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/equivariant_wrapped_prequotient_definition"),
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
        "fixture_name": "equivariant_wrapped_prequotient_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "prequotient_stacks_defined": True,
        "e_action_defined": True,
        "origin_fixed": True,
        "wrapped_colour_preserved": True,
        "retained_translation_imported": True,
        "finite_type_certification": False,
        "properness_certification": False,
        "anchor_population_certification": False,
        "anchor_losslessness_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "prequotient_rows.csv",
        "e_action_rows.csv",
        "translation_import_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected prequotient tables")
    expected_imports = {
        "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition",
        "certificates/hybrid/geometric_elliptic_degree_map",
        "certificates/moduli/retained_e_translation_rigidifications",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected prequotient imports")


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
        if row.get("prequotient_status") != "missing_open_obligation":
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
    wrapped = load_json(
        fixture.parent / "wrapped_stratum_bpositive_prestack_definition" / MANIFEST_NAME,
        issues,
    )
    if wrapped and wrapped.get("status") != "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED":
        issues.append("wrapped stratum manifest status is not verified")
    degree = load_json(fixture.parent / "geometric_elliptic_degree_map" / MANIFEST_NAME, issues)
    if degree and degree.get("status") != "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED":
        issues.append("geometric elliptic-degree manifest status is not verified")

    retained = fixture.parent.parent / "moduli" / "retained_e_translation_rigidifications"
    retained_manifest = load_json(retained / MANIFEST_NAME, issues)
    if retained_manifest:
        expected = {
            "certified": True,
            "e_translation_rigidifications": True,
            "translations_removed": True,
            "translation_defects_zero": True,
            "finite_inertia_stratifications": False,
            "extension_flag_stacks": False,
            "transitions": False,
            "compact_hall_stage": False,
            "pfaffian_orientation": False,
            "protected_trace": False,
        }
        for key, value in expected.items():
            if retained_manifest.get(key) != value:
                issues.append(
                    f"retained translation manifest {key}: "
                    f"expected {value!r}, got {retained_manifest.get(key)!r}"
                )
    rigidifications = load_csv(
        retained / "e_translation_rigidifications.csv",
        TRANSLATION_RIGIDIFICATION_COLUMNS,
        issues,
    )
    actions = load_csv(retained / "translation_actions.csv", TRANSLATION_ACTION_COLUMNS, issues)
    quotients = load_csv(retained / "quotient_rows.csv", QUOTIENT_COLUMNS, issues)
    if len(rigidifications.rows) != 3:
        issues.append("retained translation rigidification row count must be 3")
    if len(actions.rows) != 3:
        issues.append("retained translation action row count must be 3")
    if len(quotients.rows) != 3:
        issues.append("retained quotient row count must be 3")
    for index, row in enumerate(rigidifications.rows, start=2):
        if row.get("translation_removed") != "true":
            issues.append(f"e_translation_rigidifications.csv:{index} not removed")
        if row.get("action_free_on_retained_row") != "true":
            issues.append(f"e_translation_rigidifications.csv:{index} action not free")
        if row.get("translation_defect_rank") != "0":
            issues.append(f"e_translation_rigidifications.csv:{index} defect not zero")
        if row.get("check_status") != "verified":
            issues.append(f"e_translation_rigidifications.csv:{index} not verified")
    for index, row in enumerate(actions.rows, start=2):
        if row.get("action_defined") != "true":
            issues.append(f"translation_actions.csv:{index} action not defined")
        if row.get("action_free_on_retained_row") != "true":
            issues.append(f"translation_actions.csv:{index} action not free")
        if row.get("action_defect_rank") != "0":
            issues.append(f"translation_actions.csv:{index} defect not zero")
        if row.get("origin_id") != "0_E":
            issues.append(f"translation_actions.csv:{index} origin is not 0_E")
        if row.get("check_status") != "verified":
            issues.append(f"translation_actions.csv:{index} not verified")
    for index, row in enumerate(quotients.rows, start=2):
        if row.get("translation_removed") != "true":
            issues.append(f"quotient_rows.csv:{index} translation not removed")
        if row.get("quotient_defect_rank") != "0":
            issues.append(f"quotient_rows.csv:{index} quotient defect not zero")
        if row.get("check_status") != "verified":
            issues.append(f"quotient_rows.csv:{index} not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "prequotient_rows.csv", PREQUOTIENT_COLUMNS, EXPECTED_PREQUOTIENT, issues)
    check_single_row(fixture, "e_action_rows.csv", ACTION_COLUMNS, EXPECTED_ACTION, issues)
    check_single_row(fixture, "translation_import_rows.csv", IMPORT_COLUMNS, EXPECTED_IMPORT, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
