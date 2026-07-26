#!/usr/bin/env python3
"""Verify the mixed correspondence Thom--Sebastiani transport packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "MIXED_THOM_SEBASTIANI_TRANSPORT_CONDITIONAL_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "mixed_correspondence_thom_sebastiani.v1"
EXPECTED_KIND = "mixed_correspondence_thom_sebastiani"

TS_COLUMNS = (
    "ts_id",
    "R_id",
    "order",
    "source_product_id",
    "source_map_id",
    "extension_stack_id",
    "source_vanishing_cycle_id",
    "extension_vanishing_cycle_id",
    "orientation_transport_id",
    "dcritical_additivity",
    "quadratic_stabilization",
    "cosection_reduction_compatible",
    "bbdjs_ts_applied",
    "joyce_upmeier_orientation_applied",
    "binary_ts_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_TS_ROWS = {
    "mixed_LW_binary_ts_R": {
        "R_id": "R",
        "order": "LW",
        "source_product_id": "M_loc_alpha_R_I_times_M_wr_eta_R",
        "source_map_id": "p_LW",
        "extension_stack_id": "E_LW_alpha_eta_zeta_R_I",
        "source_vanishing_cycle_id": "Phi_loc_alpha_tensor_Phi_wr_eta",
        "extension_vanishing_cycle_id": "Phi_E_LW_red",
        "orientation_transport_id": "o_E_LW_equals_p_LW_star_o_source",
        "dcritical_additivity": "true",
        "quadratic_stabilization": "true",
        "cosection_reduction_compatible": "true",
        "bbdjs_ts_applied": "true",
        "joyce_upmeier_orientation_applied": "true",
        "binary_ts_defect_rank": "0",
        "check_status": "verified",
    },
    "mixed_WL_binary_ts_R": {
        "R_id": "R",
        "order": "WL",
        "source_product_id": "M_wr_eta_R_times_M_loc_alpha_R_I",
        "source_map_id": "p_WL",
        "extension_stack_id": "E_WL_eta_alpha_zeta_R_I",
        "source_vanishing_cycle_id": "Phi_wr_eta_tensor_Phi_loc_alpha",
        "extension_vanishing_cycle_id": "Phi_E_WL_red",
        "orientation_transport_id": "o_E_WL_equals_p_WL_star_o_source",
        "dcritical_additivity": "true",
        "quadratic_stabilization": "true",
        "cosection_reduction_compatible": "true",
        "bbdjs_ts_applied": "true",
        "joyce_upmeier_orientation_applied": "true",
        "binary_ts_defect_rank": "0",
        "check_status": "verified",
    },
}

ORIENTATION_COLUMNS = (
    "hypothesis_id",
    "R_id",
    "order",
    "orientation_source",
    "orientation_transport_required",
    "orientation_existence_constructed",
    "o1_discharged",
    "orientation_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_ORIENTATION_ROWS = {
    "mixed_LW_orientation_ts_hypothesis_R": {
        "R_id": "R",
        "order": "LW",
        "orientation_source": "Joyce_Upmeier_reduced_orientation",
        "orientation_transport_required": "true",
        "orientation_existence_constructed": "false",
        "o1_discharged": "false",
        "orientation_defect_rank": "0",
        "check_status": "verified",
    },
    "mixed_WL_orientation_ts_hypothesis_R": {
        "R_id": "R",
        "order": "WL",
        "orientation_source": "Joyce_Upmeier_reduced_orientation",
        "orientation_transport_required": "true",
        "orientation_existence_constructed": "false",
        "o1_discharged": "false",
        "orientation_defect_rank": "0",
        "check_status": "verified",
    },
}

EMPTY_TABLES = {
    "two_step_flag_pentagon_rows.csv": (
        "pentagon_id",
        "R_id",
        "word",
        "first_parenthesization",
        "second_parenthesization",
        "pentagon_defect_rank",
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
        "ts_quotient_descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "order",
        "source_map_id",
        "ts_transition_defect_rank",
        "orientation_transition_defect_rank",
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
    "ts_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "orientation_existence_rows",
        "two_step_flag_pentagon_rows",
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
        "base_change_only",
        "projection_formula_only",
        "orientation_line_only",
        "bbdjs_citation_only",
        "quotient_descent_from_mixed_ts",
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
        description="Check mixed correspondence Thom--Sebastiani transport packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/mixed_correspondence_thom_sebastiani"),
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
        "fixture_name": "mixed_correspondence_thom_sebastiani",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "mixed_thom_sebastiani_transport_proved": True,
        "conditional_on_reduced_ts_charts": True,
        "conditional_on_orientation_transport": True,
        "orientation_existence_certification": False,
        "o1_discharge": False,
        "dcritical_additivity_required": True,
        "quadratic_stabilization_allowed": True,
        "cosection_reduction_required": True,
        "uses_bbdjs_thom_sebastiani": True,
        "uses_joyce_upmeier_orientation_transport": True,
        "binary_ts_defects_zero": True,
        "base_change_packet_imported": True,
        "projection_formula_packet_imported": True,
        "two_step_flag_pentagon_certification": False,
        "quotient_descent_certification": True,
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
        "thom_sebastiani_rows.csv",
        "orientation_hypotheses.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected Thom--Sebastiani tables")
    expected_imports = {
        "certificates/hybrid/mixed_local_wrapped_correspondence_definition",
        "certificates/hybrid/mixed_local_wrapped_extension_admissibility",
        "certificates/hybrid/mixed_correspondence_base_change",
        "certificates/hybrid/mixed_correspondence_projection_formula",
        "certificates/orientation/k3e_reduced_orientation",
        "certificates/moduli/retained_universal_complexes",
        "certificates/hybrid/quotient_after_correspondence_thom_sebastiani",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected Thom--Sebastiani imports")


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
        status = row.get("ts_status")
        if row.get("obligation_id") == "orientation_existence_rows":
            if status != "assumed_open_obligation":
                issues.append(f"blocked_obligations.csv:{index} should keep O1 assumed")
        elif status != "missing_open_obligation":
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
    hybrid_root = repo_root / "certificates" / "hybrid"
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
            "mixed_correspondence_base_change",
            "MIXED_CORRESPONDENCE_BASE_CHANGE_VERIFIED",
        ),
        (
            "mixed_correspondence_projection_formula",
            "MIXED_CORRESPONDENCE_PROJECTION_FORMULA_VERIFIED",
        ),
        (
            "quotient_after_correspondence_thom_sebastiani",
            "QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED",
        ),
    ):
        manifest = load_json(hybrid_root / relative / MANIFEST_NAME, issues)
        if manifest and manifest.get("status") != expected_status:
            issues.append(
                f"{relative} manifest status: expected {expected_status!r}, got {manifest.get('status')!r}"
            )
    orientation_manifest = load_json(
        repo_root / "certificates" / "orientation" / "k3e_reduced_orientation" / MANIFEST_NAME,
        issues,
    )
    if orientation_manifest:
        if orientation_manifest.get("obstruction_ledger_status") != "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED":
            issues.append("orientation obstruction ledger status is not verified")
        if orientation_manifest.get("orientation_certification") is not False:
            issues.append("orientation certification must remain false for this conditional packet")
    universal_manifest = load_json(
        repo_root / "certificates" / "moduli" / "retained_universal_complexes" / MANIFEST_NAME,
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
        "thom_sebastiani_rows.csv",
        TS_COLUMNS,
        "ts_id",
        EXPECTED_TS_ROWS,
        issues,
    )
    check_expected_rows(
        fixture,
        "orientation_hypotheses.csv",
        ORIENTATION_COLUMNS,
        "hypothesis_id",
        EXPECTED_ORIENTATION_ROWS,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_import_statuses(fixture, issues)
    if issues:
        print("MIXED_THOM_SEBASTIANI_TRANSPORT_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
