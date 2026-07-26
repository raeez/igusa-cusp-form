#!/usr/bin/env python3
"""Verify HN transition compatibility for Q_E_R."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_HN_TRANSITION_COMPATIBILITY_VERIFIED"
EXPECTED_SCHEMA = "quotient_after_correspondence_hn_transition_compatibility.v1"
EXPECTED_KIND = "quotient_after_correspondence_hn_transition_compatibility"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:quotient-after-correspondence-hn-transition-compatibility"

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
OBJECT_TRANSITION_COLUMNS = (
    "object_transition_id",
    "from_R",
    "to_R",
    "source_object_transition",
    "quotient_object_transition",
    "quotient_square_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
COEFFICIENT_TRANSITION_COLUMNS = (
    "coefficient_transition_id",
    "from_R",
    "to_R",
    "source_coefficient_transport",
    "quotient_coefficient_transport",
    "descent_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
BM_TRANSITION_COLUMNS = (
    "square_id",
    "from_R",
    "to_R",
    "source_transition_id",
    "reduced_transition_id",
    "Q_source_id",
    "Q_target_id",
    "square_defect_rank",
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
        "Q_E_R_transition_component_only",
        "hall_product_transition_claim",
        "hall_coproduct_transition_claim",
        "primitive_transition_claim",
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
        description="Check quotient-after-correspondence HN transition packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path(
            "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility"
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
        "fixture_name": "quotient_after_correspondence_hn_transition_compatibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "hn_transition_compatible": True,
        "q_e_transition_compatible": True,
        "transition_certification": True,
        "transition_defect_rank": 0,
        "object_transition_defect_rank": 0,
        "coefficient_transition_defect_rank": 0,
        "bm_transition_square_defect_rank": 0,
        "quotient_after_correspondence_imported": True,
        "bm_chain_functor_imported": True,
        "hall_product_transition_certification": False,
        "hall_coproduct_transition_certification": False,
        "primitive_transition_certification": False,
        "protected_integration_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "transition_rows.csv",
        "object_transition_rows.csv",
        "coefficient_transition_rows.csv",
        "bm_transition_square_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected HN transition tables")
    expected_imports = {
        "certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition",
        "certificates/hybrid/quotient_after_correspondence_bm_chain_functor",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected HN transition imports")


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
    transition = require_one_row(
        fixture,
        "transition_rows.csv",
        TRANSITION_COLUMNS,
        "transition_id",
        "Q_E_R_hn_transition_Rprime_R",
        "transition_defect_rank",
        issues,
    )
    if transition:
        if transition.get("from_R") != "Rprime" or transition.get("to_R") != "R":
            issues.append("transition row must record Rprime -> R")
        if transition.get("pseudofunctor_id") != "quotient_after_correspondence_pseudofunctor":
            issues.append("transition row must name the quotient-after-correspondence pseudofunctor")

    obj = require_one_row(
        fixture,
        "object_transition_rows.csv",
        OBJECT_TRANSITION_COLUMNS,
        "object_transition_id",
        "quotient_object_transition_Rprime_R",
        "quotient_square_defect_rank",
        issues,
    )
    if obj:
        if obj.get("source_object_transition") != "Y_Rprime_to_Y_R":
            issues.append("object transition row must name Y_Rprime_to_Y_R")
        if obj.get("quotient_object_transition") != "bar_Y_Rprime_to_bar_Y_R":
            issues.append("object transition row must name bar_Y_Rprime_to_bar_Y_R")

    coeff = require_one_row(
        fixture,
        "coefficient_transition_rows.csv",
        COEFFICIENT_TRANSITION_COLUMNS,
        "coefficient_transition_id",
        "quotient_coefficient_transition_Rprime_R",
        "descent_defect_rank",
        issues,
    )
    if coeff:
        if coeff.get("source_coefficient_transport") != "K_Rprime_to_K_R":
            issues.append("coefficient transition row must name K_Rprime_to_K_R")
        if coeff.get("quotient_coefficient_transport") != "bar_K_Rprime_to_bar_K_R":
            issues.append("coefficient transition row must name bar_K_Rprime_to_bar_K_R")

    square = require_one_row(
        fixture,
        "bm_transition_square_rows.csv",
        BM_TRANSITION_COLUMNS,
        "square_id",
        "Q_E_R_transition_square_Rprime_R",
        "square_defect_rank",
        issues,
    )
    if square:
        if square.get("source_transition_id") != "T_E_Rprime_R":
            issues.append("BM transition square must name T_E_Rprime_R")
        if square.get("reduced_transition_id") != "bar_T_Rprime_R":
            issues.append("BM transition square must name bar_T_Rprime_R")
        if square.get("Q_source_id") != "Q_E_Rprime":
            issues.append("BM transition square must name Q_E_Rprime")
        if square.get("Q_target_id") != "Q_E_R":
            issues.append("BM transition square must name Q_E_R")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty in the HN transition packet")


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
        "quotient_after_correspondence_pseudofunctor_definition": "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED",
        "quotient_after_correspondence_bm_chain_functor": "QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED",
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
        print("QUOTIENT_AFTER_CORRESPONDENCE_HN_TRANSITION_COMPATIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
