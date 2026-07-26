#!/usr/bin/env python3
"""Verify row-338 reduced CY3 pairing nondegeneracy packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_cy3_pairing_nondegeneracy_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_cy3_pairing_nondegeneracy_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_CY3_PAIRING_NONDEGENERACY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-cy3-pairing-nondegeneracy"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_pairing_nondegeneracy")

ROW333_FIXTURE = Path("certificates/orientation/rhomred_negative_root_orientation_compatibility")
ROW335_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_pairing")
ROW337_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_serre_signs")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
TRANSITION_RADICAL_FIXTURE = Path("certificates/hall/transition_radical_preservation")
PAIRING_KERNEL_LIM1_FIXTURE = Path("certificates/hall/pairing_kernel_lim1_vanishing")

ROW333_STATUS = "RHOMRED_NEGATIVE_ROOT_ORIENTATION_COMPATIBILITY_OBSTRUCTION_VERIFIED"
ROW335_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_PAIRING_OBSTRUCTION_VERIFIED"
ROW337_STATUS = "RHOMRED_ORIENTATION_CY3_SERRE_SIGNS_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
PAIRING_PUSHFORWARD_SCHEMA = "hall_pairing_pushforward_compatibility.v1"
TRANSITION_RADICAL_STATUS = "TRANSITION_RADICAL_PRESERVATION_OBSTRUCTION_VERIFIED"
PAIRING_KERNEL_LIM1_STATUS = "PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "source_pairing_rows": 0,
    "source_radical_rows": 0,
    "source_quotient_splitting_rows": 0,
    "source_hopf_pairing_identity_rows": 0,
    "radical_ideal_coideal_rows": 0,
    "formal_pairing_degree_zero_rows": 3,
    "negative_root_compatibility_rows": 0,
    "frobenius_pairing_rows": 0,
    "serre_sign_rows": 0,
    "transition_radical_pairing_rows": 0,
    "transition_radical_kernel_rows": 0,
    "transition_quotient_rows": 0,
    "pairing_kernel_maps": 0,
    "pairing_kernel_spaces": 0,
    "pairing_kernel_ml_rows": 0,
    "nondegeneracy_rows": 0,
    "row339_orientation_limit_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_pairing_matrix",
    "left_kernel_rows",
    "right_kernel_rows",
    "radical_identification",
    "quotient_splitting",
    "quotient_pairing_matrix",
    "quotient_full_rank_row",
    "quotient_nondegeneracy_identity",
    "radical_ideal_coideal",
    "serre_sign_line",
    "transition_radical_rows",
    "quotient_transition_rows",
    "pairing_kernel_ml_rows",
    "formal_pairing_not_nondegeneracy",
    "target_pairing_not_source",
    "row339_orientation_limit",
}

REQUIRED_FIREWALL = {
    "formal_pairing_degree_zero",
    "target_pairing_block",
    "row333_negative_root_criterion",
    "row335_Frobenius_criterion",
    "row337_Serre_sign_criterion",
    "transition_radical_obstruction_only",
    "pairing_kernel_lim1_obstruction_only",
    "empty_G_entries",
    "empty_K_entries",
    "empty_Q_entries",
    "empty_hopf_pairing_identities",
    "scalar_trace",
    "protected_trace",
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
            "source_pairing_matrix_required",
            "left_kernel_required",
            "right_kernel_required",
            "radical_identification_required",
            "quotient_splitting_required",
            "quotient_pairing_matrix_required",
            "quotient_full_rank_required",
            "quotient_nondegeneracy_identity_required",
            "radical_ideal_coideal_required",
            "transition_radical_required",
            "pairing_kernel_lim1_required",
            "formal_pairing_degree_zero_as_nondegenerate_allowed",
            "target_pairing_block_as_source_allowed",
            "serre_sign_line_as_full_rank_allowed",
            "criterion_recorded",
            "nondegeneracy_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "nondegeneracy_rows.csv",
        (
            "nondegeneracy_row_id",
            "R_id",
            "stratum_id",
            "degree_id",
            "positive_space_id",
            "negative_space_id",
            "pairing_matrix_id",
            "left_kernel_id",
            "right_kernel_id",
            "radical_id",
            "positive_quotient_splitting_id",
            "negative_quotient_splitting_id",
            "quotient_pairing_matrix_id",
            "full_left_rank",
            "full_right_rank",
            "determinant_or_smith_row_id",
            "rank_defect_left",
            "rank_defect_right",
            "radical_identification_defect_rank",
            "quotient_well_defined_defect_rank",
            "nondegeneracy_verified",
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


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")

    for key in (
        "negative_root_compatibility_imported",
        "frobenius_pairing_imported",
        "cy3_serre_signs_imported",
        "compact_hall_ledger_imported",
        "hall_pairing_pushforward_imported",
        "transition_radical_ledger_imported",
        "pairing_kernel_lim1_ledger_imported",
        "nondegeneracy_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_pairing_matrix_rows_supplied",
        "left_kernel_rows_supplied",
        "right_kernel_rows_supplied",
        "radical_identification_rows_supplied",
        "quotient_splitting_rows_supplied",
        "quotient_pairing_matrix_rows_supplied",
        "quotient_full_rank_rows_supplied",
        "quotient_nondegeneracy_identity_rows_supplied",
        "radical_ideal_coideal_rows_supplied",
        "transition_radical_rows_supplied",
        "pairing_kernel_lim1_rows_supplied",
        "inverse_limit_nondegeneracy_rows_supplied",
        "cy3_pairing_nondegeneracy_proved",
        "row339_orientation_limit_claimed",
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
            str(ROW335_FIXTURE),
            str(ROW337_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(TRANSITION_RADICAL_FIXTURE),
            str(PAIRING_KERNEL_LIM1_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion_rows count")
    row = criterion[0]
    for key in (
        "source_pairing_matrix_required",
        "left_kernel_required",
        "right_kernel_required",
        "radical_identification_required",
        "quotient_splitting_required",
        "quotient_pairing_matrix_required",
        "quotient_full_rank_required",
        "quotient_nondegeneracy_identity_required",
        "radical_ideal_coideal_required",
        "transition_radical_required",
        "pairing_kernel_lim1_required",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "formal_pairing_degree_zero_as_nondegenerate_allowed",
        "target_pairing_block_as_source_allowed",
        "serre_sign_line_as_full_rank_allowed",
        "nondegeneracy_proved",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-338 proposition")

    require_equal(len(tables["nondegeneracy_rows.csv"]), 0, "nondegeneracy_rows count")

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


def check_imports() -> None:
    row333 = read_json(ROW333_FIXTURE / "manifest.json")
    require_equal(row333.get("status"), ROW333_STATUS, "row333 status")
    require_false(row333.get("negative_root_orientation_compatibility_proved"), "row333 proof")
    require_table_empty(ROW333_FIXTURE / "negative_root_compatibility_rows.csv")

    row335 = read_json(ROW335_FIXTURE / "manifest.json")
    require_equal(row335.get("status"), ROW335_STATUS, "row335 status")
    require_false(row335.get("quotient_nondegeneracy_rows_supplied"), "row335 quotient rows")
    require_false(row335.get("frobenius_pairing_proved"), "row335 proof")
    require_table_empty(ROW335_FIXTURE / "frobenius_pairing_rows.csv")

    row337 = read_json(ROW337_FIXTURE / "manifest.json")
    require_equal(row337.get("status"), ROW337_STATUS, "row337 status")
    require_false(row337.get("cy3_serre_signs_proved"), "row337 proof")
    require_false(row337.get("row338_nondegeneracy_claimed"), "row337 row338 claim")
    require_table_empty(ROW337_FIXTURE / "serre_sign_rows.csv")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_false(compact.get("compact_source_recognition"), "compact source recognition")
    require_false(compact.get("mathematical_certification"), "compact mathematical certification")
    for rel_path in (
        "G_entries.csv",
        "K_entries.csv",
        "Q_entries.csv",
        "hopf_pairing_identities.csv",
        "radical_ideal_coideal.csv",
    ):
        require_table_empty(COMPACT_HALL_FIXTURE / rel_path)

    pairing = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pairing.get("schema_version"), PAIRING_PUSHFORWARD_SCHEMA, "pairing schema")
    require_true(pairing.get("certified"), "pairing certified")
    require_true(pairing.get("normal_ordered_pairing_degree"), "pairing degree")
    require_false(pairing.get("quotient_nondegeneracy"), "pairing quotient_nondegeneracy")
    rows = read_table_path(PAIRING_PUSHFORWARD_FIXTURE / "pairing_rows.csv")
    require_equal(len(rows), 3, "formal pairing rows")
    for row in rows:
        require_equal(row.get("homogeneous_degree_zero"), "true", f"{row.get('pairing_id')} degree")
        require_equal(int_cell(row, "degree_defect_rank"), 0, f"{row.get('pairing_id')} defect")

    transition = read_json(TRANSITION_RADICAL_FIXTURE / "manifest.json")
    require_equal(transition.get("status"), TRANSITION_RADICAL_STATUS, "transition radical status")
    require_false(transition.get("radical_transition_certification"), "transition radical certification")
    for rel_path in (
        "pairing_transition.csv",
        "radical_kernel_rows.csv",
        "radical_transition_matrices.csv",
        "quotient_transition_matrices.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANSITION_RADICAL_FIXTURE / rel_path)

    pairing_kernel = read_json(PAIRING_KERNEL_LIM1_FIXTURE / "manifest.json")
    require_equal(pairing_kernel.get("status"), PAIRING_KERNEL_LIM1_STATUS, "pairing kernel status")
    require_false(pairing_kernel.get("lim1_vanishing_certification"), "pairing kernel lim1 certification")
    for rel_path in (
        "pairing_maps.csv",
        "pairing_kernel_spaces.csv",
        "pairing_kernel_transition_maps.csv",
        "pairing_kernel_image_stabilization.csv",
        "pairing_kernel_ml_r1lim_defects.csv",
        "pairing_kernel_coverage.csv",
    ):
        require_table_empty(PAIRING_KERNEL_LIM1_FIXTURE / rel_path)


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
