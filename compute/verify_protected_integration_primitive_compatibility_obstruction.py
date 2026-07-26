#!/usr/bin/env python3
"""Verify the finite protected integration primitive-compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PROTECTED_INTEGRATION_PRIMITIVE_COMPATIBILITY_VERIFIED"
EXPECTED_SCHEMA = "protected_integration_primitive_compatibility.v1"
EXPECTED_KIND = "protected_integration_primitive_compatibility"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:protected-integration-primitive-compatibility"

PRIMITIVE_COLUMNS = (
    "primitive_projection_id",
    "height",
    "reduced_hall_object_id",
    "reduced_primitive_id",
    "reduced_projection_id",
    "primitive_projection_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
TARGET_COLUMNS = (
    "target_primitive_row_id",
    "height",
    "target_object_id",
    "target_primitive_id",
    "target_projection_id",
    "target_primitive_defect_rank",
    "gram_identification_status",
    "proof_reference",
    "check_status",
    "notes",
)
SQUARE_COLUMNS = (
    "square_id",
    "height",
    "reduced_projection_id",
    "target_projection_id",
    "integration_id",
    "restricted_integration_id",
    "square_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "integration_status",
    "proof_reference",
    "check_status",
    "notes",
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
REQUIRED_OBLIGATIONS = frozenset(
    {
        "transition_compatibility",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "primitive_projection_compatibility_only",
        "protected_integration_transition_claim",
        "gram_degree_claim",
        "Pi_X_vs_b_geom_claim",
        "level_Z_protected_trace",
        "pfaffian_line_or_section",
        "empty_hybrid_carrier",
    }
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check finite protected integration primitive-compatibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/protected_integration_primitive_compatibility"),
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
        "fixture_name": "protected_integration_primitive_compatibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "protected_integration_defined": True,
        "product_compatibility_imported": True,
        "coproduct_compatibility_imported": True,
        "primitive_compatibility_certification": True,
        "primitive_projection_defect_rank": 0,
        "target_primitive_defect_rank": 0,
        "integration_square_defect_rank": 0,
        "transition_compatibility_certification": False,
        "gram_degree_certification": False,
        "pi_x_degree_certification": False,
        "protected_trace_certification": False,
        "pfaffian_line_certification": False,
        "aggregate_hybrid_population": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "primitive_projection_rows.csv",
        "target_primitive_rows.csv",
        "integration_square_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected primitive compatibility tables")
    expected_imports = {
        "certificates/hybrid/protected_integration_definition",
        "certificates/hybrid/protected_integration_product_compatibility",
        "certificates/hybrid/protected_integration_coproduct_compatibility",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_primitives",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected primitive compatibility imports")


def require_one_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected_id_key: str,
    expected_id: str,
    defect_key: str,
    issues: list[str],
) -> dict[str, str] | None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return None
    row = table.rows[0]
    if row.get(expected_id_key) != expected_id:
        issues.append(
            f"{table_name} {expected_id_key}: expected {expected_id!r}, "
            f"got {row.get(expected_id_key)!r}"
        )
    if row.get(defect_key) != "0":
        issues.append(f"{table_name} {defect_key} must be zero")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {PROOF_LABEL}")
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    primitive = require_one_row(
        fixture,
        "primitive_projection_rows.csv",
        PRIMITIVE_COLUMNS,
        "primitive_projection_id",
        "I_prot_primitive_projection_R",
        "primitive_projection_defect_rank",
        issues,
    )
    if primitive:
        expected = {
            "reduced_hall_object_id": "H_red_hyb_R",
            "reduced_primitive_id": "bar_P_R",
            "reduced_projection_id": "bar_pi_R_Prim",
        }
        for key, value in expected.items():
            if primitive.get(key) != value:
                issues.append(
                    f"primitive row {key}: expected {value!r}, got {primitive.get(key)!r}"
                )

    target = require_one_row(
        fixture,
        "target_primitive_rows.csv",
        TARGET_COLUMNS,
        "target_primitive_row_id",
        "T_R_primitive_projection",
        "target_primitive_defect_rank",
        issues,
    )
    if target:
        expected = {
            "target_object_id": "C_T_R_le_R",
            "target_projection_id": "pi_T_R_Prim",
            "gram_identification_status": "not_certified",
        }
        for key, value in expected.items():
            if target.get(key) != value:
                issues.append(
                    f"target row {key}: expected {value!r}, got {target.get(key)!r}"
                )

    square = require_one_row(
        fixture,
        "integration_square_rows.csv",
        SQUARE_COLUMNS,
        "square_id",
        "I_prot_primitive_square_R",
        "square_defect_rank",
        issues,
    )
    if square:
        expected = {
            "reduced_projection_id": "bar_pi_R_Prim",
            "target_projection_id": "pi_T_R_Prim",
            "integration_id": "I_R_prot",
            "restricted_integration_id": "I_R_prot_restricted_to_bar_P_R",
        }
        for key, value in expected.items():
            if square.get(key) != value:
                issues.append(
                    f"square row {key}: expected {value!r}, got {square.get(key)!r}"
                )


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
        if row.get("integration_status") != "missing_open_obligation":
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
    expected_statuses = {
        "protected_integration_definition": "PROTECTED_INTEGRATION_DEFINITION_VERIFIED",
        "protected_integration_product_compatibility": "PROTECTED_INTEGRATION_PRODUCT_COMPATIBILITY_VERIFIED",
        "protected_integration_coproduct_compatibility": "PROTECTED_INTEGRATION_COPRODUCT_COMPATIBILITY_VERIFIED",
        "quotient_after_correspondence_theta_mu_primitives": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_PRIMITIVES_VERIFIED",
    }
    for directory, status in expected_statuses.items():
        manifest = load_json(fixture.parent / directory / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != status:
            issues.append(f"import {directory} status is not {status}")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_positive_rows(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("PROTECTED_INTEGRATION_PRIMITIVE_COMPATIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
