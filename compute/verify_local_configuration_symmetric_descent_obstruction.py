#!/usr/bin/env python3
"""Verify the local configuration symmetric descent packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "LOCAL_CONFIGURATION_SYMMETRIC_DESCENT_VERIFIED"
EXPECTED_SCHEMA = "local_configuration_symmetric_descent.v1"
EXPECTED_KIND = "local_configuration_symmetric_descent"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"

RELABELING_COLUMNS = (
    "relabeling_id",
    "R_id",
    "source_profile",
    "target_profile",
    "coordinate_map",
    "incidence_stack_isomorphism",
    "support_locus_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_RELABELING = {
    "relabeling_id": "local_relabel_sigma",
    "support_locus_defect_rank": "0",
    "check_status": "verified",
}

EQUIVARIANCE_COLUMNS = (
    "equivariance_id",
    "relabeling_id",
    "coefficient_source",
    "coefficient_target",
    "vanishing_cycle_defect_rank",
    "orientation_defect_rank",
    "total_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_EQUIVARIANCE = {
    "equivariance_id": "local_coefficient_relabeling",
    "relabeling_id": "local_relabel_sigma",
    "vanishing_cycle_defect_rank": "0",
    "orientation_defect_rank": "0",
    "total_defect_rank": "0",
    "check_status": "verified",
}

QUOTIENT_COLUMNS = (
    "quotient_id",
    "group_id",
    "action_stack",
    "quotient_stack",
    "coefficient_descent_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_QUOTIENT = {
    "quotient_id": "local_stabilizer_quotient",
    "group_id": "Aut_I_alpha",
    "coefficient_descent_defect_rank": "0",
    "check_status": "verified",
}

EMPTY_TABLES = {
    "ordered_colimit_descent_rows.csv": (
        "descent_id",
        "R_id",
        "ordered_chart_family",
        "symmetric_colimit_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "collision_descent_rows.csv": (
        "collision_id",
        "R_id",
        "diagonal_map",
        "collision_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "refinement_rows.csv": (
        "refinement_id",
        "R_id",
        "source_chart",
        "target_chart",
        "refinement_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "symmetric_descent_id",
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
    "symmetric_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "ordered_colimit_descent",
        "collision_descent_rows",
        "refinement_rows",
        "overlap_rows",
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
        "ordinary_ran_only",
        "coefficient_invariance_only",
        "ordered_colimit_descent",
        "collision_descent",
        "refinement_claim",
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
        description="Check local configuration symmetric descent packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/local_configuration_symmetric_descent"),
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
        "fixture_name": "local_configuration_symmetric_descent",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "symmetric_descent_proved": True,
        "fixed_chart_descent": True,
        "local_configuration_relabelling": True,
        "support_locus_preserved": True,
        "coefficient_equivariance": True,
        "quotient_stack_descent": True,
        "ordered_colimit_descent": False,
        "collision_descent": False,
        "refinement_certification": False,
        "overlap_certification": False,
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
        "relabeling_rows.csv",
        "coefficient_equivariance_rows.csv",
        "quotient_stack_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected symmetric descent tables")
    expected_imports = {
        "certificates/hybrid/hybrid_ran_prestack_definition",
        "certificates/hybrid/local_stratum_b0_prestack_definition",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected symmetric descent imports")


def require_one_row(
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
    if "prop:local-configuration-symmetric-descent" not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to the row-244 proposition")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in this fixed-chart packet")


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
        if row.get("symmetric_status") != "missing_open_obligation":
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
        "hybrid_ran_prestack_definition": "HYBRID_RAN_PRESTACK_DEFINITION_VERIFIED",
        "local_stratum_b0_prestack_definition": "LOCAL_STRATUM_B0_PRESTACK_DEFINITION_VERIFIED",
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
    require_one_row(fixture, "relabeling_rows.csv", RELABELING_COLUMNS, EXPECTED_RELABELING, issues)
    require_one_row(
        fixture,
        "coefficient_equivariance_rows.csv",
        EQUIVARIANCE_COLUMNS,
        EXPECTED_EQUIVARIANCE,
        issues,
    )
    require_one_row(fixture, "quotient_stack_rows.csv", QUOTIENT_COLUMNS, EXPECTED_QUOTIENT, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("LOCAL_CONFIGURATION_SYMMETRIC_DESCENT_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
