#!/usr/bin/env python3
"""Verify the finite protected integration product-compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "PROTECTED_INTEGRATION_PRODUCT_COMPATIBILITY_VERIFIED"
EXPECTED_SCHEMA = "protected_integration_product_compatibility.v1"
EXPECTED_KIND = "protected_integration_product_compatibility"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:protected-integration-product-compatibility"
WORDS = ("LL", "LW", "WL", "WW")

PRODUCT_COLUMNS = (
    "product_id",
    "height",
    "word",
    "source_charge_1",
    "source_charge_2",
    "target_charge",
    "reduced_product_id",
    "theta_mu_id",
    "product_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
LABEL_COLUMNS = (
    "label_product_id",
    "height",
    "word",
    "left_label",
    "right_label",
    "target_label",
    "monoid_product_id",
    "label_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
SQUARE_COLUMNS = (
    "square_id",
    "height",
    "word",
    "source_product_id",
    "left_integral_id",
    "right_integral_id",
    "target_integral_id",
    "target_product_id",
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
        "product_compatibility_only",
        "coproduct_compatibility_claim",
        "primitive_projection_compatibility_claim",
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
        description="Check finite protected integration product-compatibility packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/protected_integration_product_compatibility"),
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
        "fixture_name": "protected_integration_product_compatibility",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "protected_integration_defined": True,
        "product_compatibility_certification": True,
        "product_word_count": 4,
        "product_defect_rank": 0,
        "label_multiplication_defect_rank": 0,
        "integration_square_defect_rank": 0,
        "coproduct_compatibility_certification": False,
        "primitive_compatibility_certification": False,
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
        "product_rows.csv",
        "label_multiplication_rows.csv",
        "integration_square_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected product compatibility tables")
    expected_imports = {
        "certificates/hybrid/protected_integration_definition",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_comparison",
        "certificates/hybrid/quotient_after_correspondence_theta_mu_associativity",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected product compatibility imports")


def check_word_rows(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    id_key: str,
    defect_key: str,
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != len(WORDS):
        issues.append(f"{table_name} must contain exactly {len(WORDS)} rows")
    words = {row.get("word", "") for row in table.rows}
    missing = sorted(set(WORDS) - words)
    extra = sorted(words - set(WORDS))
    if missing:
        issues.append(f"{table_name} missing words: {', '.join(missing)}")
    if extra:
        issues.append(f"{table_name} has unexpected words: {', '.join(extra)}")
    for index, row in enumerate(table.rows, start=2):
        word = row.get("word", "")
        if not row.get(id_key):
            issues.append(f"{table_name}:{index} missing {id_key}")
        if row.get(defect_key) != "0":
            issues.append(f"{table_name}:{index} {defect_key} must be zero")
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append(f"{table_name}:{index} does not point to {PROOF_LABEL}")
        if row.get("check_status") != "verified":
            issues.append(f"{table_name}:{index} is not verified")
        if word and word not in WORDS:
            issues.append(f"{table_name}:{index} invalid word {word!r}")


def check_positive_rows(fixture: Path, issues: list[str]) -> None:
    check_word_rows(
        fixture,
        "product_rows.csv",
        PRODUCT_COLUMNS,
        "product_id",
        "product_defect_rank",
        issues,
    )
    check_word_rows(
        fixture,
        "label_multiplication_rows.csv",
        LABEL_COLUMNS,
        "label_product_id",
        "label_defect_rank",
        issues,
    )
    check_word_rows(
        fixture,
        "integration_square_rows.csv",
        SQUARE_COLUMNS,
        "square_id",
        "square_defect_rank",
        issues,
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
        "quotient_after_correspondence_theta_mu_comparison": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED",
        "quotient_after_correspondence_theta_mu_associativity": "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED",
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
        print("PROTECTED_INTEGRATION_PRODUCT_COMPATIBILITY_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
