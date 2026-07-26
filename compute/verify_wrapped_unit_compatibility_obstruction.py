#!/usr/bin/env python3
"""Verify the wrapped unit compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_UNIT_COMPATIBILITY_VERIFIED"
EXPECTED_SCHEMA = "wrapped_unit_compatibility.v1"
EXPECTED_KIND = "wrapped_unit_compatibility"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"

WRAPPED_UNIT_COLUMNS = (
    "compatibility_id",
    "input_type",
    "unit_side",
    "unit_correspondence_id",
    "source_isomorphism_id",
    "target_isomorphism_id",
    "anchor_memory_id",
    "ts_unit_id",
    "identity_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_WRAPPED_ROWS = {
    "wrapped_LW_left_unit": ("left", "unit_LW_left", "anchor_memory_LW_left", "ts_zero_wr_left"),
    "wrapped_WL_right_unit": ("right", "unit_WL_right", "anchor_memory_WL_right", "ts_zero_wr_right"),
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
    "split_left_wrapped_source_insert_unit": "unit_LW_left",
    "split_right_wrapped_source_insert_unit": "unit_WL_right",
}

ANCHOR_COLUMNS = (
    "anchor_memory_id",
    "unit_correspondence_id",
    "zero_local_anchor",
    "wrapped_source_anchor",
    "target_anchor",
    "anchor_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ANCHORS = {
    "anchor_memory_LW_left": "unit_LW_left",
    "anchor_memory_WL_right": "unit_WL_right",
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
    "zero_wr_left": "ts_zero_wr_left",
    "zero_wr_right": "ts_zero_wr_right",
}

EMPTY_TABLES = {
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
    "wrapped_status",
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
        "local_unit_compatibility_only",
        "anchor_forgetting",
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
    parser = argparse.ArgumentParser(description="Check wrapped unit compatibility packet.")
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_unit_compatibility"),
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
        "fixture_name": "wrapped_unit_compatibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "wrapped_unit_compatibility_proved": True,
        "wrapped_unit_row_count": 2,
        "left_wrapped_unit_verified": True,
        "right_wrapped_unit_verified": True,
        "anchor_memory_preserved": True,
        "local_unit_compatibility_imported": True,
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
        "wrapped_unit_compatibility_rows.csv",
        "split_isomorphism_rows.csv",
        "anchor_memory_rows.csv",
        "zero_coefficient_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected wrapped unit tables")
    expected_imports = {
        "certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences",
        "certificates/hybrid/local_unit_compatibility",
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/mixed_local_wrapped_extension_admissibility",
        "certificates/hybrid/compact_support_exceptional_pushforward_model",
        "certificates/hybrid/mixed_correspondence_thom_sebastiani",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected wrapped unit imports")


def check_wrapped_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "wrapped_unit_compatibility_rows.csv", WRAPPED_UNIT_COLUMNS, issues)
    by_id = {row.get("compatibility_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_WRAPPED_ROWS):
        missing = sorted(set(EXPECTED_WRAPPED_ROWS) - set(by_id))
        extra = sorted(set(by_id) - set(EXPECTED_WRAPPED_ROWS))
        if missing:
            issues.append("missing wrapped unit rows: " + ", ".join(missing))
        if extra:
            issues.append("unexpected wrapped unit rows: " + ", ".join(extra))
    for row_id, (side, unit_correspondence, anchor_id, ts_unit) in EXPECTED_WRAPPED_ROWS.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        expected = {
            "input_type": "wrapped",
            "unit_side": side,
            "unit_correspondence_id": unit_correspondence,
            "anchor_memory_id": anchor_id,
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
        if row.get("target_map_model") not in {"q_LW_left_equals_id", "q_WL_right_equals_id"}:
            issues.append(f"{row_id} target map is not marked as identity")
        if row.get("compact_support_model") != "identity_compactification":
            issues.append(f"{row_id} does not use identity compactification")
        if row.get("defect_rank") != "0" or row.get("check_status") != "verified":
            issues.append(f"{row_id} is not verified with zero defect")


def check_anchor_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "anchor_memory_rows.csv", ANCHOR_COLUMNS, issues)
    by_id = {row.get("anchor_memory_id", ""): row for row in table.rows}
    if set(by_id) != set(EXPECTED_ANCHORS):
        issues.append("anchor_memory_rows.csv does not contain exactly the expected rows")
    for row_id, unit_correspondence in EXPECTED_ANCHORS.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        expected = {
            "unit_correspondence_id": unit_correspondence,
            "zero_local_anchor": "none",
            "wrapped_source_anchor": "lambda_eta_R_W_eta",
            "target_anchor": "lambda_eta_R_W_eta",
            "anchor_defect_rank": "0",
            "check_status": "verified",
        }
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(f"{row_id} {key}: expected {value!r}, got {row.get(key)!r}")


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
            issues.append(f"{table_name} must remain empty in this wrapped unit packet")


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
        if row.get("wrapped_status") != "missing_open_obligation":
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
        "local_unit_compatibility": "LOCAL_UNIT_COMPATIBILITY_VERIFIED",
        "mixed_local_wrapped_correspondence_definition": "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        "mixed_local_wrapped_extension_admissibility": "MIXED_LOCAL_WRAPPED_ADMISSIBILITY_VERIFIED",
        "compact_support_exceptional_pushforward_model": "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED",
        "mixed_correspondence_thom_sebastiani": "MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED",
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
    check_wrapped_rows(fixture, issues)
    check_split_rows(fixture, issues)
    check_anchor_rows(fixture, issues)
    check_zero_rows(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("WRAPPED_UNIT_COMPATIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
