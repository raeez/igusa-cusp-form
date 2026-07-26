#!/usr/bin/env python3
"""Verify the higher-coloured tree category definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "HIGHER_COLOURED_TREE_CATEGORY_DEFINED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "higher_coloured_tree_category_definition.v1"
EXPECTED_KIND = "higher_coloured_tree_category_definition"

OBJECT_COLUMNS = (
    "profile_id",
    "profile_kind",
    "input_data",
    "output_type_rule",
    "anchor_memory_required",
    "configuration_refinement_required",
    "defined",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_OBJECTS = {
    "local_leaf": ("L", "false", "true"),
    "wrapped_leaf": ("W", "true", "false"),
    "internal_edge": ("hybrid_intermediate", "true", "true"),
    "root_output": ("hybrid_output", "true", "true"),
}

GENERATOR_COLUMNS = (
    "generator_id",
    "generator_kind",
    "arity_range",
    "mathematical_payload",
    "composition_rule",
    "defined",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_GENERATORS = {
    "planar_tree",
    "internal_vertex",
    "tree_contraction",
    "local_refinement",
    "local_symmetric_relabelling",
    "wrapped_order",
    "overlap_chart",
    "unit_placeholder",
}

RESIDUAL_COLUMNS = (
    "component_id",
    "residual_symbol",
    "measures",
    "vanishing_claimed",
    "definition_status",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_RESIDUALS = {
    "tree_contraction": "o_tree_R",
    "unit": "o_unit_R",
    "symmetry": "o_sym_R",
    "refinement": "o_ref_R",
    "descent": "o_des_R",
    "overlap": "o_ov_R",
}

EMPTY_TABLES = {
    "residual_vanishing_rows.csv": (
        "vanishing_id",
        "residual_component",
        "vanishing_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "unit_rows.csv": (
        "unit_id",
        "unit_kind",
        "unit_object",
        "unit_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "tree_generator_id",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "tree_generator_id",
        "tree_transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "tree_category_id",
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
    "tree_category_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "residual_vanishing",
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
        "pentagon_only",
        "definition_as_vanishing",
        "unit_claim",
        "symmetric_descent_claim",
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
    parser = argparse.ArgumentParser(description="Check higher-coloured tree category packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/higher_coloured_tree_category_definition"),
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
        "fixture_name": "higher_coloured_tree_category_definition",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "definition_only": True,
        "category_defined": True,
        "nonunital_category": True,
        "object_profiles_defined": True,
        "tree_generators_defined": True,
        "residual_components_defined": True,
        "residual_vanishing": False,
        "unit_certification": False,
        "symmetric_descent_certification": False,
        "wrapped_order_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "object_profile_rows.csv",
        "generator_rows.csv",
        "residual_component_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected higher-coloured definition tables")
    expected_imports = {
        "certificates/hybrid/eight_word_binary_vocabulary",
        "certificates/hybrid/eight_word_two_step_flag_stacks",
        "certificates/hybrid/four_input_pentagon_coherence",
        "certificates/hybrid/source_target_anchor_memory_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected higher-coloured imports")


def check_objects(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "object_profile_rows.csv", OBJECT_COLUMNS, issues)
    by_id = {row.get("profile_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_OBJECTS):
        missing = sorted(set(EXPECTED_OBJECTS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_OBJECTS))
        if missing:
            issues.append("missing object profile rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected object profile rows: " + ", ".join(extra))
    for profile_id, (kind, anchor, refinement) in EXPECTED_OBJECTS.items():
        row = by_id.get(profile_id)
        if row is None:
            continue
        expected = {
            "profile_kind": kind,
            "anchor_memory_required": anchor,
            "configuration_refinement_required": refinement,
            "defined": "true",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"object {profile_id} {key}: expected {value!r}, got {row.get(key)!r}")
        if not row.get("proof_reference"):
            issues.append(f"object {profile_id} lacks proof_reference")


def check_generators(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "generator_rows.csv", GENERATOR_COLUMNS, issues)
    by_id = {row.get("generator_id", ""): row for row in table.rows}
    if set(by_id) != EXPECTED_GENERATORS:
        missing = sorted(EXPECTED_GENERATORS - set(by_id))
        extra = sorted(set(by_id) - EXPECTED_GENERATORS)
        if missing:
            issues.append("missing generator rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected generator rows: " + ", ".join(extra))
    for generator_id, row in by_id.items():
        if row.get("defined") != "true":
            issues.append(f"generator {generator_id} is not defined")
        if row.get("check_status") != "verified":
            issues.append(f"generator {generator_id} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"generator {generator_id} lacks mathematical payload")


def check_residuals(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "residual_component_rows.csv", RESIDUAL_COLUMNS, issues)
    by_id = {row.get("component_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_RESIDUALS):
        missing = sorted(set(EXPECTED_RESIDUALS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_RESIDUALS))
        if missing:
            issues.append("missing residual rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected residual rows: " + ", ".join(extra))
    for component_id, symbol in EXPECTED_RESIDUALS.items():
        row = by_id.get(component_id)
        if row is None:
            continue
        expected = {
            "residual_symbol": symbol,
            "vanishing_claimed": "false",
            "definition_status": "defined",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"residual {component_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if "vanishing" not in row.get("notes", "") and component_id != "unit":
            issues.append(f"residual {component_id} notes must mark vanishing as unsupplied")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this definition-only packet")


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
        if row.get("tree_category_status") != "missing_open_obligation":
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
    repo_root = fixture.parents[2]
    expected_hybrid_statuses = {
        "eight_word_binary_vocabulary": "EIGHT_WORD_BINARY_VOCABULARY_DEFINED",
        "eight_word_two_step_flag_stacks": "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED",
        "four_input_pentagon_coherence": "FOUR_INPUT_PENTAGON_CONDITIONAL_VERIFIED",
        "source_target_anchor_memory_definition": "SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED",
    }
    for relative, expected_status in expected_hybrid_statuses.items():
        manifest = load_json(
            repo_root / "certificates" / "hybrid" / relative / MANIFEST_NAME,
            issues,
        )
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_objects(fixture, issues)
    check_generators(fixture, issues)
    check_residuals(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("HIGHER_COLOURED_TREE_CATEGORY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
