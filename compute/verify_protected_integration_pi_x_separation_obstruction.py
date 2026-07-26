#!/usr/bin/env python3
"""Verify the finite protected integration Pi_X-separation packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PROTECTED_INTEGRATION_PI_X_SEPARATION_VERIFIED"
EXPECTED_SCHEMA = "protected_integration_pi_x_separation.v1"
EXPECTED_KIND = "protected_integration_pi_x_separation"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:protected-integration-pi-x-separation"

PI_LABEL_COLUMNS = (
    "pi_label_id",
    "height",
    "source_charge_family_id",
    "lifted_charge_family_id",
    "label_family_id",
    "label_lift_map_id",
    "target_gram_map_id",
    "normal_ordered_map_id",
    "comparison_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
PI_COORDINATE_COLUMNS = (
    "coordinate_id",
    "height",
    "label_family_id",
    "lifted_charge_family_id",
    "q_coordinate_id",
    "r_coordinate_id",
    "s_coordinate_id",
    "borcherds_s_coordinate_id",
    "coordinate_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
SEPARATION_COLUMNS = (
    "separation_id",
    "height",
    "integration_id",
    "normal_ordered_degree_id",
    "geometric_degree_map_id",
    "geometric_degree_role",
    "substitution_excluded",
    "comparison_condition",
    "separation_defect_rank",
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
REQUIRED_OBLIGATIONS = frozenset({"transition_compatibility"})
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "b_R_geom_as_protected_integration_exponent",
        "pr3_overlinePi_X_as_support_degree",
        "branch_relation_as_definition",
        "protected_integration_transition_claim",
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
        description="Check finite protected integration Pi_X-separation packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/protected_integration_pi_x_separation"),
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
        "fixture_name": "protected_integration_pi_x_separation",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "protected_integration_defined": True,
        "gram_degree_imported": True,
        "geometric_separation_imported": True,
        "pi_x_degree_certification": True,
        "label_comparison_defect_rank": 0,
        "coordinate_comparison_defect_rank": 0,
        "separation_defect_rank": 0,
        "geom_b_substitute_excluded": True,
        "transition_compatibility_certification": False,
        "protected_trace_certification": False,
        "pfaffian_line_certification": False,
        "aggregate_hybrid_population": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = {
        "pi_label_rows.csv",
        "pi_coordinate_rows.csv",
        "separation_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected Pi_X-separation tables")
    expected_imports = {
        "certificates/hybrid/protected_integration_gram_degree",
        "certificates/hybrid/geometric_borcherds_degree_separation",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected Pi_X-separation imports")


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
    label = require_one_row(
        fixture,
        "pi_label_rows.csv",
        PI_LABEL_COLUMNS,
        "pi_label_id",
        "I_prot_pi_label_R",
        "comparison_defect_rank",
        issues,
    )
    if label:
        expected = {
            "source_charge_family_id": "Gamma_R",
            "lifted_charge_family_id": "widehat_Gamma_R",
            "label_family_id": "omega_R_labels",
            "label_lift_map_id": "widehatomega_R",
            "target_gram_map_id": "g_R",
            "normal_ordered_map_id": "overlinePi_X",
        }
        for key, value in expected.items():
            if label.get(key) != value:
                issues.append(f"pi label row {key}: expected {value!r}, got {label.get(key)!r}")

    coordinate = require_one_row(
        fixture,
        "pi_coordinate_rows.csv",
        PI_COORDINATE_COLUMNS,
        "coordinate_id",
        "I_prot_pi_coordinates_R",
        "coordinate_defect_rank",
        issues,
    )
    if coordinate:
        expected = {
            "label_family_id": "omega_R_labels",
            "lifted_charge_family_id": "widehat_Gamma_R",
            "q_coordinate_id": "n_R",
            "r_coordinate_id": "l_R",
            "s_coordinate_id": "m_R",
            "borcherds_s_coordinate_id": "pr3_overlinePi_X",
        }
        for key, value in expected.items():
            if coordinate.get(key) != value:
                issues.append(
                    f"coordinate row {key}: expected {value!r}, got {coordinate.get(key)!r}"
                )

    separation = require_one_row(
        fixture,
        "separation_rows.csv",
        SEPARATION_COLUMNS,
        "separation_id",
        "I_prot_uses_pi_not_b_geom",
        "separation_defect_rank",
        issues,
    )
    if separation:
        expected = {
            "integration_id": "I_R_prot",
            "normal_ordered_degree_id": "m_R_Bch",
            "geometric_degree_map_id": "b_R_geom",
            "geometric_degree_role": "local_wrapped_support_split",
            "substitution_excluded": "true",
            "comparison_condition": "branch_comparison_required_for_any_relation",
        }
        for key, value in expected.items():
            if separation.get(key) != value:
                issues.append(
                    f"separation row {key}: expected {value!r}, got {separation.get(key)!r}"
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
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append(f"blocked_obligations.csv:{index} does not point to proof")


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
    for relative in (
        "../protected_integration_gram_degree/manifest.json",
        "../geometric_borcherds_degree_separation/manifest.json",
    ):
        if not (fixture / relative).resolve().is_file():
            issues.append(f"missing imported manifest: {relative}")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    check_manifest(fixture, issues)
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_imports(fixture, issues)
    check_positive_rows(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    return not issues, issues


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    ok, issues = run(args.fixture)
    if ok:
        print(SUCCESS_STATUS)
        return 0
    print("PROTECTED_INTEGRATION_PI_X_SEPARATION_BLOCKED")
    for issue in issues:
        print(f"- {issue}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
