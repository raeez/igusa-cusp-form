#!/usr/bin/env python3
"""Verify the local unit compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "LOCAL_UNIT_COMPATIBILITY_VERIFIED"
EXPECTED_SCHEMA = "local_unit_compatibility.v1"
EXPECTED_KIND = "local_unit_compatibility"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"

LOCAL_UNIT_COLUMNS = (
    "compatibility_id",
    "input_type",
    "unit_side",
    "unit_correspondence_id",
    "source_isomorphism_id",
    "target_isomorphism_id",
    "ts_unit_id",
    "identity_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_LOCAL_ROWS = {
    "local_LL_left_unit": ("left", "unit_LL_left", "ts_zero_left"),
    "local_LL_right_unit": ("right", "unit_LL_right", "ts_zero_right"),
}

SPLIT_COLUMNS = (
    "isomorphism_id",
    "unit_correspondence_id",
    "source_stack",
    "target_stack",
    "split_sequence",
    "target_map_model",
    "compact_support_model",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_SPLITS = {
    "split_left_source_insert_unit": "unit_LL_left",
    "split_right_source_insert_unit": "unit_LL_right",
}

ZERO_COLUMNS = (
    "zero_row_id",
    "zero_unit_object",
    "zero_coefficient",
    "orientation_unit",
    "ts_unit_id",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ZERO_ROWS = {
    "zero_left": "ts_zero_left",
    "zero_right": "ts_zero_right",
}

EMPTY_TABLES = {
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
    "quotient_descent_rows.csv": (
        "quotient_id",
        "unit_compatibility_id",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "unit_compatibility_id",
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
    "local_status",
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
        "unit_definition_only",
        "zero_charge_symbol_only",
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
    parser = argparse.ArgumentParser(description="Check local unit compatibility packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/local_unit_compatibility"),
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
        "fixture_name": "local_unit_compatibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "local_unit_compatibility_proved": True,
        "local_unit_row_count": 2,
        "left_unit_verified": True,
        "right_unit_verified": True,
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
        "local_unit_compatibility_rows.csv",
        "split_isomorphism_rows.csv",
        "zero_coefficient_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected local unit tables")
    expected_imports = {
        "certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences",
        "certificates/hybrid/local_local_correspondence_definition",
        "certificates/hybrid/local_local_extension_properness",
        "certificates/hybrid/compact_support_exceptional_pushforward_model",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected local unit imports")


def check_local_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "local_unit_compatibility_rows.csv", LOCAL_UNIT_COLUMNS, issues)
    by_id = {row.get("compatibility_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_LOCAL_ROWS):
        missing = sorted(set(EXPECTED_LOCAL_ROWS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_LOCAL_ROWS))
        if missing:
            issues.append("missing local unit rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected local unit rows: " + ", ".join(extra))
    for row_id, (side, unit_correspondence, ts_unit) in EXPECTED_LOCAL_ROWS.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        expected = {
            "input_type": "local",
            "unit_side": side,
            "unit_correspondence_id": unit_correspondence,
            "ts_unit_id": ts_unit,
            "identity_defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{row_id} {key}: expected {value!r}, got {row.get(key)!r}")
        if "identity" not in row.get("notes", ""):
            issues.append(f"{row_id} notes must record identity")


def check_split_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "split_isomorphism_rows.csv", SPLIT_COLUMNS, issues)
    by_id = {row.get("isomorphism_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_SPLITS):
        issues.append("split_isomorphism_rows.csv does not contain exactly the expected split rows")
    for row_id, unit_correspondence in EXPECTED_SPLITS.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        if row.get("unit_correspondence_id") != unit_correspondence:
            issues.append(f"{row_id} has wrong unit correspondence")
        if row.get("target_map_model") not in {"q_LL_left_equals_id", "q_LL_right_equals_id"}:
            issues.append(f"{row_id} target map is not marked as identity")
        if row.get("compact_support_model") != "identity_compactification":
            issues.append(f"{row_id} does not use identity compactification")
        if row.get("defect_rank") != "0" or row.get("check_status") != "verified":
            issues.append(f"{row_id} is not verified with zero defect")


def check_zero_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "zero_coefficient_rows.csv", ZERO_COLUMNS, issues)
    by_id = {row.get("zero_row_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_ZERO_ROWS):
        issues.append("zero_coefficient_rows.csv does not contain exactly the expected zero rows")
    for row_id, ts_unit in EXPECTED_ZERO_ROWS.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        expected = {
            "zero_unit_object": "mathbf_1_hyb_R",
            "zero_coefficient": "C_unit",
            "orientation_unit": "Joyce_Upmeier_orientation_unit",
            "ts_unit_id": ts_unit,
            "defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{row_id} {key}: expected {value!r}, got {row.get(key)!r}")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this local unit packet")


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
        if row.get("local_status") != "missing_open_obligation":
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
    expected_statuses = {
        "hybrid_unit_object_and_vacuum_correspondences": "HYBRID_UNIT_OBJECT_AND_VACUUM_CORRESPONDENCES_DEFINED",
        "local_local_correspondence_definition": "LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED",
        "local_local_extension_properness": "LOCAL_LOCAL_TARGET_PROPERNESS_VERIFIED",
        "compact_support_exceptional_pushforward_model": "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED",
    }
    for relative, expected_status in expected_statuses.items():
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
    check_local_rows(fixture, issues)
    check_split_rows(fixture, issues)
    check_zero_rows(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("LOCAL_UNIT_COMPATIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
