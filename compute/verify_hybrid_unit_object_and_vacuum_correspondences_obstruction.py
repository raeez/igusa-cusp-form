#!/usr/bin/env python3
"""Verify the hybrid unit object and vacuum-correspondence packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "HYBRID_UNIT_OBJECT_AND_VACUUM_CORRESPONDENCES_DEFINED"
EXPECTED_SCHEMA = "hybrid_unit_object_and_vacuum_correspondences.v1"
EXPECTED_KIND = "hybrid_unit_definition"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"

UNIT_OBJECT_COLUMNS = (
    "unit_id",
    "unit_symbol",
    "charge_symbol",
    "object_stack",
    "local_chart",
    "geometric_degree",
    "retained_zero_source",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_UNIT_OBJECT = {
    "unit_id": "hybrid_vacuum",
    "unit_symbol": "mathbf_1_hyb_R",
    "charge_symbol": "0_R",
    "object_stack": "M_loc_cl_0_R_R_empty",
    "local_chart": "empty",
    "geometric_degree": "b_R_geom_0_R_equals_0",
    "check_status": "verified",
}

UNIT_CORRESPONDENCE_COLUMNS = (
    "correspondence_id",
    "input_type",
    "unit_side",
    "binary_type",
    "source_profile",
    "target_profile",
    "extension_sequence",
    "substack_symbol",
    "split_model_defined",
    "identity_law_proved",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_CORRESPONDENCES = {
    "unit_LL_left": ("local", "left", "LL"),
    "unit_LL_right": ("local", "right", "LL"),
    "unit_LW_left": ("wrapped", "left", "LW"),
    "unit_WL_right": ("wrapped", "right", "WL"),
}

EMPTY_TABLES = {
    "local_unit_compatibility_rows.csv": (
        "compatibility_id",
        "input_type",
        "unit_side",
        "unit_correspondence_id",
        "identity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "wrapped_unit_compatibility_rows.csv": (
        "compatibility_id",
        "input_type",
        "unit_side",
        "unit_correspondence_id",
        "identity_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "unit_correspondence_id",
        "transition_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "row_type",
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
    "definition_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
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
        "zero_charge_symbol_only",
        "nonunital_tree_category",
        "unit_definition_as_identity_law",
        "local_unit_compatibility",
        "wrapped_unit_compatibility",
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
    parser = argparse.ArgumentParser(description="Check hybrid unit definition packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences"),
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
        "fixture_name": "hybrid_unit_object_and_vacuum_correspondences",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "definition_only": True,
        "unit_object_defined": True,
        "unit_correspondences_defined": True,
        "unit_correspondence_count": 4,
        "local_unit_compatibility_proved": False,
        "wrapped_unit_compatibility_proved": False,
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
        "unit_object_rows.csv",
        "unit_correspondence_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected unit packet tables")
    expected_imports = {
        "certificates/moduli/retained_window_hn_filtration",
        "certificates/hybrid/local_local_correspondence_definition",
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/higher_coloured_residual_vanishing_criterion",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected unit packet imports")


def check_unit_object(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "unit_object_rows.csv", UNIT_OBJECT_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("unit_object_rows.csv must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in EXPECTED_UNIT_OBJECT.items():
        if row.get(key) != value:
            issues.append(f"unit object {key}: expected {value!r}, got {row.get(key)!r}")
    if not row.get("retained_zero_source") or not row.get("proof_reference"):
        issues.append("unit object row lacks source references")


def check_correspondences(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "unit_correspondence_rows.csv", UNIT_CORRESPONDENCE_COLUMNS, issues)
    by_id = {row.get("correspondence_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_CORRESPONDENCES):
        missing = sorted(set(EXPECTED_CORRESPONDENCES) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_CORRESPONDENCES))
        if missing:
            issues.append("missing unit correspondence rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected unit correspondence rows: " + ", ".join(extra))
    for row_id, (input_type, side, binary_type) in EXPECTED_CORRESPONDENCES.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        expected = {
            "input_type": input_type,
            "unit_side": side,
            "binary_type": binary_type,
            "split_model_defined": "true",
            "identity_law_proved": "false",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{row_id} {key}: expected {value!r}, got {row.get(key)!r}")
        if "defined_not_proved" not in row.get("notes", ""):
            issues.append(f"{row_id} notes must mark identity law as not proved")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this definition packet")


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
        if row.get("definition_status") != "missing_open_obligation":
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
    moduli_manifest = load_json(
        repo_root / "certificates" / "moduli" / "retained_window_hn_filtration" / MANIFEST_NAME,
        issues,
    )
    if moduli_manifest and moduli_manifest.get("certified") is not True:
        issues.append("retained_window_hn_filtration manifest is not certified")
    expected_hybrid_statuses = {
        "local_local_correspondence_definition": "LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED",
        "mixed_local_wrapped_correspondence_definition": "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        "higher_coloured_residual_vanishing_criterion": "HIGHER_COLOURED_RESIDUAL_CONDITIONAL_CRITERION_VERIFIED",
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
    check_unit_object(fixture, issues)
    check_correspondences(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("HYBRID_UNIT_OBJECT_AND_VACUUM_CORRESPONDENCES_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
