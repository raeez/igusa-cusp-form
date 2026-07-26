#!/usr/bin/env python3
"""Verify theta_mu primitive compatibility for quotient-after-correspondence."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_PRIMITIVES_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_theta_mu_primitives.v1"
EXPECTED_KIND = "quotient_after_correspondence_theta_mu_primitives"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-theta-mu-primitives"
TRANSITION_PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

PRIMITIVE_COLUMNS = (
    "primitive_id",
    "R_id",
    "theta_id",
    "primitive_projection",
    "primitive_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
PROJECTION_COLUMNS = (
    "projection_id",
    "R_id",
    "source_primitive_id",
    "reduced_primitive_id",
    "source_projection_id",
    "reduced_projection_id",
    "projection_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
KERNEL_INTERTWINING_COLUMNS = (
    "intertwining_id",
    "R_id",
    "source_reduced_coproduct_id",
    "reduced_reduced_coproduct_id",
    "source_counit_id",
    "reduced_counit_id",
    "kernel_intertwining_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
TRANSITION_COLUMNS = (
    "transition_id",
    "from_R",
    "to_R",
    "pseudofunctor_id",
    "transition_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EMPTY_TABLES = {
    "protected_integration_rows.csv": (
        "integration_id",
        "R_id",
        "Q_E_R_id",
        "I_prot_id",
        "integration_defect_rank",
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
    "quotient_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "protected_integration_rows",
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
        "theta_primitive_component_only",
        "theta_coproduct_component_only",
        "source_primitive_projection_matrix",
        "Q_E_R_transition_component_only",
        "protected_integration_claim",
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
        description="Check quotient theta_mu primitive compatibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(
            "certificates/hybrid/quotient_after_correspondence_theta_mu_primitives"
        ),
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
        "fixture_name": "quotient_after_correspondence_theta_mu_primitives",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "theta_mu_primitive_compatible": True,
        "primitive_certification": True,
        "primitive_defect_rank": 0,
        "primitive_projection_defect_rank": 0,
        "primitive_kernel_intertwining_defect_rank": 0,
        "quotient_after_correspondence_imported": True,
        "theta_mu_comparison_imported": True,
        "theta_mu_associativity_imported": True,
        "theta_mu_coproduct_imported": True,
        "coproduct_packet_imported": True,
        "transition_certification": True,
        "protected_integration_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "primitive_rows.csv",
        "primitive_projection_rows.csv",
        "kernel_intertwining_rows.csv",
        "transition_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected theta primitive tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct",
        "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected theta primitive imports")


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
    if row.get("check_status") != "verified":
        issues.append(f"{table_name} row is not verified")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append(f"{table_name} row does not point to {PROOF_LABEL}")
    return row


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    primitive = require_one_row(
        fixture,
        "primitive_rows.csv",
        PRIMITIVE_COLUMNS,
        "primitive_id",
        "theta_mu_primitives_R",
        "primitive_defect_rank",
        issues,
    )
    if primitive:
        if primitive.get("theta_id") != "quotient_theta_mu_R":
            issues.append("primitive row must name quotient_theta_mu_R")
        if primitive.get("primitive_projection") != "primitive_projection_P_R":
            issues.append("primitive row must name primitive_projection_P_R")

    projection = require_one_row(
        fixture,
        "primitive_projection_rows.csv",
        PROJECTION_COLUMNS,
        "projection_id",
        "theta_primitive_projection_R",
        "projection_defect_rank",
        issues,
    )
    if projection:
        if projection.get("source_primitive_id") != "P_R_E":
            issues.append("projection row must name P_R_E")
        if projection.get("reduced_primitive_id") != "bar_P_R":
            issues.append("projection row must name bar_P_R")
        if projection.get("source_projection_id") != "pi_R_Prim":
            issues.append("projection row must name pi_R_Prim")
        if projection.get("reduced_projection_id") != "bar_pi_R_Prim":
            issues.append("projection row must name bar_pi_R_Prim")

    kernel = require_one_row(
        fixture,
        "kernel_intertwining_rows.csv",
        KERNEL_INTERTWINING_COLUMNS,
        "intertwining_id",
        "theta_primitive_kernel_intertwining_R",
        "kernel_intertwining_defect_rank",
        issues,
    )
    if kernel:
        if kernel.get("source_reduced_coproduct_id") != "tilde_Delta_R":
            issues.append("kernel row must name tilde_Delta_R")
        if kernel.get("reduced_reduced_coproduct_id") != "tilde_bar_Delta_R":
            issues.append("kernel row must name tilde_bar_Delta_R")
        if kernel.get("source_counit_id") != "epsilon_R":
            issues.append("kernel row must name epsilon_R")
        if kernel.get("reduced_counit_id") != "bar_epsilon_R":
            issues.append("kernel row must name bar_epsilon_R")
    transition = load_csv(fixture / "transition_rows.csv", TRANSITION_COLUMNS, issues)
    if len(transition.rows) != 1:
        issues.append("transition_rows.csv must contain exactly one row")
    else:
        row = transition.rows[0]
        if row.get("transition_id") != "Q_E_R_hn_transition_Rprime_R":
            issues.append("transition row must be Q_E_R_hn_transition_Rprime_R")
        if row.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition row must name quotient_after_correspondence_pseudofunctor")
        if row.get("transition_defect_rank") != "0":
            issues.append("transition row defect rank must be zero")
        if row.get("check_status") != "verified":
            issues.append("transition row is not verified")
        if TRANSITION_PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append("transition row does not point to the row-256 theorem")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the theta primitive packet")


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
        if row.get("quotient_status") != "missing_open_obligation":
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
        "quotient_after_correspondence_theta_mu_comparison": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED",
        "quotient_after_correspondence_theta_mu_associativity": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED",
        "quotient_after_correspondence_theta_mu_coproduct": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COPRODUCT_VERIFIED",
        "quotient_after_correspondence_hn_transition_compatibility": "QUOTIENT_AFTER_CORRESPONDENCE_HN_TRANSITION_COMPATIBILITY_VERIFIED",
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
    check_positive_rows(fixture, issues)
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_PRIMITIVES_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
