#!/usr/bin/env python3
"""Verify the mixed correspondence compact-support projection-formula packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "MIXED_CORRESPONDENCE_PROJECTION_FORMULA_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "mixed_correspondence_projection_formula.v1"
EXPECTED_KIND = "mixed_correspondence_projection_formula"

PROJECTION_COLUMNS = (
    "projection_formula_id",
    "R_id",
    "order",
    "target_map_id",
    "compactification_model_id",
    "coefficient_object_id",
    "coefficient_on_target",
    "coefficient_finite_tor",
    "coefficient_dualizable",
    "uses_open_projection_formula",
    "uses_proper_projection_formula",
    "proper_target_specialization",
    "compact_support_formula",
    "source_functor",
    "target_functor",
    "projection_formula_isomorphism_id",
    "projection_formula_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_PROJECTION_ROWS = {
    "mixed_LW_q_projection_formula_R": {
        "R_id": "R",
        "order": "LW",
        "target_map_id": "q_LW",
        "compactification_model_id": "Q_cs_q_LW_K_LW",
        "coefficient_object_id": "L_LW_target",
        "coefficient_on_target": "true",
        "coefficient_finite_tor": "true",
        "coefficient_dualizable": "true",
        "uses_open_projection_formula": "true",
        "uses_proper_projection_formula": "true",
        "proper_target_specialization": "true",
        "compact_support_formula": "q_cs_bang_K=bar_q_star_j_bang_K",
        "source_functor": "q_LW_cs_bang_K_LW_tensor_q_LW_star_L_LW",
        "target_functor": "q_LW_cs_bang_K_LW_tensor_L_LW",
        "projection_formula_isomorphism_id": "q_LW_cs_projection_formula",
        "projection_formula_defect_rank": "0",
        "check_status": "verified",
    },
    "mixed_WL_q_projection_formula_R": {
        "R_id": "R",
        "order": "WL",
        "target_map_id": "q_WL",
        "compactification_model_id": "Q_cs_q_WL_K_WL",
        "coefficient_object_id": "L_WL_target",
        "coefficient_on_target": "true",
        "coefficient_finite_tor": "true",
        "coefficient_dualizable": "true",
        "uses_open_projection_formula": "true",
        "uses_proper_projection_formula": "true",
        "proper_target_specialization": "true",
        "compact_support_formula": "q_cs_bang_K=bar_q_star_j_bang_K",
        "source_functor": "q_WL_cs_bang_K_WL_tensor_q_WL_star_L_WL",
        "target_functor": "q_WL_cs_bang_K_WL_tensor_L_WL",
        "projection_formula_isomorphism_id": "q_WL_cs_projection_formula",
        "projection_formula_defect_rank": "0",
        "check_status": "verified",
    },
}

EMPTY_TABLES = {
    "choice_independence_rows.csv": (
        "independence_id",
        "R_id",
        "order",
        "compactification_pair_id",
        "comparison_isomorphism_id",
        "independence_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "thom_sebastiani_rows.csv": (
        "ts_id",
        "R_id",
        "order",
        "target_map_id",
        "vanishing_cycle_source_id",
        "vanishing_cycle_target_id",
        "ts_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "quotient_descent_id",
        "R_id",
        "order",
        "target_map_id",
        "reduced_target_map_id",
        "quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "order",
        "target_map_id",
        "projection_formula_compatibility_defect_rank",
        "compactification_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "correspondence_id",
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
    "projection_formula_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "choice_independence_rows",
        "thom_sebastiani_rows",
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
        "mixed_definition_only",
        "mixed_admissibility_only",
        "compact_support_model_only",
        "base_change_only",
        "no_target_coefficient",
        "non_finite_tor_coefficient",
        "thom_sebastiani",
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
        description="Check mixed correspondence compact-support projection formula packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/mixed_correspondence_projection_formula"),
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
        "fixture_name": "mixed_correspondence_projection_formula",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "mixed_projection_formula_proved": True,
        "target_coefficient_required": True,
        "target_coefficient_finite_tor_required": True,
        "compact_support_model_imported": True,
        "base_change_packet_imported": True,
        "uses_open_projection_formula": True,
        "uses_proper_projection_formula": True,
        "proper_target_specialization_used": True,
        "projection_formula_defects_zero": True,
        "choice_independence_certification": False,
        "thom_sebastiani_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    if set(manifest.get("orders", [])) != {"LW", "WL"}:
        issues.append("manifest orders must be exactly LW and WL")
    expected_tables = set(EMPTY_TABLES) | {
        "projection_formula_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected projection-formula tables")
    expected_imports = {
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/mixed_local_wrapped_extension_admissibility",
        "certificates/hybrid/compact_support_exceptional_pushforward_model",
        "certificates/hybrid/mixed_correspondence_base_change",
        "certificates/moduli/retained_universal_complexes",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected projection-formula imports")


def check_expected_rows(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    key_name: str,
    expected_rows: dict[str, dict[str, str]],
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != len(expected_rows):
        issues.append(f"{table_name} must contain exactly {len(expected_rows)} rows")
        return
    by_id = {row.get(key_name, ""): row for row in table.rows}
    missing = sorted(set(expected_rows) - set(by_id))
    extra = sorted(set(by_id) - set(expected_rows))
    if missing:
        issues.append(f"missing rows in {table_name}: " + ", ".join(missing))
    if extra:
        issues.append(f"unexpected rows in {table_name}: " + ", ".join(extra))
    for row_id, expected in expected_rows.items():
        row = by_id.get(row_id)
        if row is None:
            continue
        for key, value in expected.items():
            if row.get(key) != value:
                issues.append(
                    f"{table_name} row {row_id} {key}: expected {value!r}, got {row.get(key)!r}"
                )
        if not row.get("proof_reference"):
            issues.append(f"{table_name} row {row_id} lacks proof_reference")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until later rows are supplied")


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
        if row.get("projection_formula_status") != "missing_open_obligation":
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
    hybrid_root = fixture.parent
    certificate_root = fixture.parent.parent
    for relative, expected_status in (
        (
            "mixed_local_wrapped_correspondence_definition",
            "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
        ),
        (
            "mixed_local_wrapped_extension_admissibility",
            "MIXED_LOCAL_WRAPPED_ADMISSIBILITY_VERIFIED",
        ),
        (
            "compact_support_exceptional_pushforward_model",
            "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED",
        ),
        (
            "mixed_correspondence_base_change",
            "MIXED_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        ),
    ):
        manifest = load_json(hybrid_root / relative / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )
    universal_manifest = load_json(
        certificate_root / "moduli" / "retained_universal_complexes" / MANIFEST_NAME,
        issues,
    )
    if universal_manifest:
        if universal_manifest.get("certified") is not True:
            issues.append("retained universal complexes manifest is not certified")
        if universal_manifest.get("universal_complexes") is not True:
            issues.append("retained universal complexes manifest lacks universal complexes")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_expected_rows(
        fixture,
        "projection_formula_rows.csv",
        PROJECTION_COLUMNS,
        "projection_formula_id",
        EXPECTED_PROJECTION_ROWS,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("MIXED_CORRESPONDENCE_PROJECTION_FORMULA_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
