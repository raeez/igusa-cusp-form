#!/usr/bin/env python3
"""Verify row-337 Calabi-Yau threefold Serre-sign packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_cy3_serre_signs_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_cy3_serre_signs_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_CY3_SERRE_SIGNS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-cy3-serre-signs"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_serre_signs")

ROW333_FIXTURE = Path("certificates/orientation/rhomred_negative_root_orientation_compatibility")
ROW334_FIXTURE = Path("certificates/orientation/rhomred_orientation_chevalley_antiinvolution")
ROW335_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_pairing")
ROW336_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_trace_degree")
PTVV_FIXTURE = Path("certificates/orientation/ptvv_finite_substack_symplectic")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

ROW333_STATUS = "RHOMRED_NEGATIVE_ROOT_ORIENTATION_COMPATIBILITY_OBSTRUCTION_VERIFIED"
ROW334_STATUS = "RHOMRED_ORIENTATION_CHEVALLEY_ANTIINVOLUTION_OBSTRUCTION_VERIFIED"
ROW335_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_PAIRING_OBSTRUCTION_VERIFIED"
ROW336_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_TRACE_DEGREE_OBSTRUCTION_VERIFIED"
PTVV_STATUS = "PTVV_FINITE_SUBSTACK_SYMPLECTIC_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "ptvv_rows": 3,
    "ptvv_orientation_input_rows": 3,
    "negative_root_compatibility_rows": 0,
    "chevalley_antiinvolution_rows": 0,
    "frobenius_pairing_rows": 0,
    "trace_degree_rows": 0,
    "source_pairing_rows": 0,
    "source_hopf_pairing_identity_rows": 0,
    "source_parity_rows": 0,
    "source_radical_rows": 0,
    "orientation_transition_rows": 0,
    "serre_sign_rows": 0,
    "row338_nondegeneracy_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "reduced_serre_duality_isomorphism",
    "source_sign_exponent_table",
    "source_degree_convention",
    "source_parity_blocks",
    "orientation_sign_line",
    "determinant_duality_square",
    "thom_sebastiani_sign_comparison",
    "chevalley_sign_comparison",
    "frobenius_cyclic_sign_comparison",
    "trace_cyclicity_sign_comparison",
    "source_pairing_rows",
    "source_hopf_pairing_identities",
    "radical_quotient",
    "quotient_orientation_transport",
    "transition_compatibility",
    "ptvv_not_serre_sign",
    "row338_nondegeneracy",
}

REQUIRED_FIREWALL = {
    "PTVV_shifted_symplectic_input",
    "target_negative_dual_block",
    "formal_pairing_degree_zero",
    "row333_negative_root_criterion",
    "row334_Chevalley_criterion",
    "row335_Frobenius_criterion",
    "row336_trace_degree_criterion",
    "protected_trace",
    "protected_integration",
    "scalar_trace",
    "empty_serre_sign_rows",
    "empty_orientation_transitions",
    "empty_compact_pairing_rows",
    "determinant_line_only",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]
    allow_empty: bool = False


TABLE_SPECS = (
    TableSpec(
        "source_rows.csv",
        (
            "source_id",
            "source_kind",
            "source_path_or_key",
            "source_status",
            "input_payload",
            "output_payload",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "criterion_rows.csv",
        (
            "criterion_id",
            "reduced_serre_duality_required",
            "source_sign_exponent_table_required",
            "orientation_sign_line_required",
            "determinant_duality_square_required",
            "thom_sebastiani_sign_required",
            "chevalley_sign_required",
            "frobenius_cyclic_sign_required",
            "trace_cyclicity_sign_required",
            "radical_quotient_required",
            "transition_compatibility_required",
            "ptvv_shifted_symplectic_as_sign_allowed",
            "target_negative_dual_block_as_sign_allowed",
            "formal_pairing_degree_zero_as_sign_allowed",
            "criterion_recorded",
            "serre_signs_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "serre_sign_rows.csv",
        (
            "serre_sign_row_id",
            "R_id",
            "stratum_id",
            "degree_id",
            "positive_complex_id",
            "negative_complex_id",
            "serre_duality_row_id",
            "source_degree_convention_id",
            "parity_block_id",
            "determinant_duality_square_id",
            "orientation_sign_line_id",
            "thom_sebastiani_sign_id",
            "chevalley_sign_id",
            "frobenius_cyclic_sign_id",
            "trace_cyclicity_sign_id",
            "transition_row_id",
            "computed_sign_exponent",
            "expected_cy3_sign_exponent",
            "sign_defect_rank",
            "serre_sign_verified",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "coverage_rows.csv",
        (
            "coverage_id",
            "claim_kind",
            "computed_value",
            "expected_value",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "blocked_obligations.csv",
        (
            "obligation_id",
            "lane",
            "required_artifact",
            "required_table",
            "required_row_type",
            "mathematical_payload",
            "why_required",
            "compatibility_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        (
            "firewall_id",
            "forbidden_substitute",
            "excluded",
            "defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"json root is not an object: {path}")
    return value


def read_table_path(
    path: Path,
    columns: tuple[str, ...] | None = None,
    *,
    allow_empty: bool = False,
) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if columns is not None and tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = []
        for row in reader:
            normalized = {
                key: (value or "").strip()
                for key, value in row.items()
                if key is not None
            }
            if any(normalized.values()):
                rows.append(normalized)
    if not rows and not allow_empty:
        raise ValueError(f"{path}: expected at least one row")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns, allow_empty=spec.allow_empty)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_true(value: object, label: str) -> None:
    require_equal(value, True, label)


def require_false(value: object, label: str) -> None:
    require_equal(value, False, label)


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"{key}: expected integer cell, got {row.get(key)!r}") from exc


def require_table_empty(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    if rows:
        raise ValueError(f"{path}: expected no source rows, got {len(rows)}")


def check_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")

    for key in (
        "negative_root_compatibility_imported",
        "chevalley_antiinvolution_imported",
        "frobenius_pairing_imported",
        "frobenius_trace_degree_imported",
        "ptvv_finite_substack_symplectic_imported",
        "compact_hall_ledger_imported",
        "transition_orientation_ledger_imported",
        "serre_sign_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "reduced_serre_duality_rows_supplied",
        "source_sign_exponent_rows_supplied",
        "orientation_sign_line_rows_supplied",
        "determinant_duality_square_rows_supplied",
        "thom_sebastiani_sign_rows_supplied",
        "chevalley_sign_rows_supplied",
        "frobenius_cyclic_sign_rows_supplied",
        "trace_cyclicity_sign_rows_supplied",
        "source_degree_convention_rows_supplied",
        "source_parity_rows_supplied",
        "radical_quotient_rows_supplied",
        "quotient_orientation_rows_supplied",
        "transition_rows_supplied",
        "cy3_serre_signs_proved",
        "row338_nondegeneracy_claimed",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(
        set(manifest.get("tables", [])),
        {spec.path for spec in TABLE_SPECS},
        "manifest tables",
    )
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW333_FIXTURE),
            str(ROW334_FIXTURE),
            str(ROW335_FIXTURE),
            str(ROW336_FIXTURE),
            str(PTVV_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "manifest imports",
    )
    return manifest


def check_local_tables(fixture: Path) -> dict[str, list[dict[str, str]]]:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion_rows count")
    row = criterion[0]
    for key in (
        "reduced_serre_duality_required",
        "source_sign_exponent_table_required",
        "orientation_sign_line_required",
        "determinant_duality_square_required",
        "thom_sebastiani_sign_required",
        "chevalley_sign_required",
        "frobenius_cyclic_sign_required",
        "trace_cyclicity_sign_required",
        "radical_quotient_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "ptvv_shifted_symplectic_as_sign_allowed",
        "target_negative_dual_block_as_sign_allowed",
        "formal_pairing_degree_zero_as_sign_allowed",
        "serre_signs_proved",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-337 proposition")

    require_equal(len(tables["serre_sign_rows.csv"]), 0, "serre_sign_rows count")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        crow = coverage[coverage_id]
        require_equal(int_cell(crow, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(crow, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(crow, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(crow.get("check_status"), "verified", f"{coverage_id} status")

    obligations = {row["obligation_id"]: row for row in tables["blocked_obligations.csv"]}
    require_equal(set(obligations), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, orow in obligations.items():
        require_equal(orow.get("compatibility_status"), "missing_open_obligation", obligation_id)
        require_equal(orow.get("check_status"), "verified", f"{obligation_id} status")
        if PROOF_LABEL not in orow.get("proof_reference", ""):
            raise ValueError(f"{obligation_id}: proof reference does not point to proposition")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, frow in firewall.items():
        require_equal(frow.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(frow, "defect_rank"), 0, f"{substitute} defect")
        require_equal(frow.get("check_status"), "verified", f"{substitute} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{substitute}: proof reference does not point to proposition")

    return tables


def check_imports() -> None:
    row333 = read_json(ROW333_FIXTURE / "manifest.json")
    require_equal(row333.get("status"), ROW333_STATUS, "row333 status")
    require_false(row333.get("serre_sign_line_rows_supplied"), "row333 Serre sign rows")
    require_false(row333.get("row337_serre_sign_claimed"), "row333 row337 claim")
    require_table_empty(ROW333_FIXTURE / "negative_root_compatibility_rows.csv")

    row334 = read_json(ROW334_FIXTURE / "manifest.json")
    require_equal(row334.get("status"), ROW334_STATUS, "row334 status")
    require_false(row334.get("serre_sign_line_rows_supplied"), "row334 Serre sign rows")
    require_false(row334.get("row337_serre_sign_claimed"), "row334 row337 claim")
    require_table_empty(ROW334_FIXTURE / "chevalley_antiinvolution_rows.csv")

    row335 = read_json(ROW335_FIXTURE / "manifest.json")
    require_equal(row335.get("status"), ROW335_STATUS, "row335 status")
    require_false(row335.get("serre_sign_line_rows_supplied"), "row335 Serre sign rows")
    require_false(row335.get("row337_serre_sign_claimed"), "row335 row337 claim")
    require_table_empty(ROW335_FIXTURE / "frobenius_pairing_rows.csv")

    row336 = read_json(ROW336_FIXTURE / "manifest.json")
    require_equal(row336.get("status"), ROW336_STATUS, "row336 status")
    require_false(row336.get("serre_shift_rows_supplied"), "row336 Serre shift rows")
    require_false(row336.get("row337_serre_sign_claimed"), "row336 row337 claim")
    require_table_empty(ROW336_FIXTURE / "trace_degree_rows.csv")

    ptvv = read_json(PTVV_FIXTURE / "manifest.json")
    require_equal(ptvv.get("status"), PTVV_STATUS, "PTVV status")
    require_true(ptvv.get("finite_substack_symplectic_forms"), "PTVV forms")
    for key in (
        "joyce_dcritical_truncation",
        "rhom_red",
        "det_rhom_red",
        "orientation_square_root",
        "quotient_orientation",
        "protected_integration",
    ):
        require_false(ptvv.get(key), f"PTVV {key}")
    require_equal(len(read_table_path(PTVV_FIXTURE / "ptvv_rows.csv")), 3, "PTVV rows")
    require_equal(
        len(read_table_path(PTVV_FIXTURE / "orientation_input_rows.csv")),
        3,
        "PTVV orientation input rows",
    )

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_false(compact.get("compact_source_recognition"), "compact source recognition")
    require_false(compact.get("mathematical_certification"), "compact mathematical certification")
    for rel_path in (
        "G_entries.csv",
        "hopf_pairing_identities.csv",
        "parity_blocks.csv",
        "K_entries.csv",
        "Q_entries.csv",
    ):
        require_table_empty(COMPACT_HALL_FIXTURE / rel_path)

    transition = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(transition.get("status"), TRANSITION_ORIENTATION_STATUS, "transition status")
    require_false(transition.get("orientation_transition_certification"), "transition certification")
    require_table_empty(TRANSITION_ORIENTATION_FIXTURE / "orientation_transition_maps.csv")


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
    return SUCCESS_STATUS


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        status = verify(args.fixture)
    except Exception as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
