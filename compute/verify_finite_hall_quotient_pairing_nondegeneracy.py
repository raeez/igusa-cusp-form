#!/usr/bin/env python3
"""Verify the row-363 finite Hall quotient-pairing nondegeneracy packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_quotient_pairing_nondegeneracy.v1"
EXPECTED_KIND = "finite_hall_quotient_pairing_nondegeneracy_obstruction"
SUCCESS_STATUS = "FINITE_HALL_QUOTIENT_PAIRING_NONDEGENERACY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-quotient-pairing-nondegeneracy"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_quotient_pairing_nondegeneracy")

ADJOINTNESS_FIXTURE = Path("certificates/hall/finite_hall_pairing_coproduct_adjointness")
SUPERSYMMETRY_FIXTURE = Path("certificates/hall/finite_hall_pairing_supersymmetry")
PAIRING_DEFINITION_FIXTURE = Path("certificates/hall/finite_hall_positive_negative_pairing")
PAIRING_KERNEL_LIM1_FIXTURE = Path("certificates/hall/pairing_kernel_lim1_vanishing")
TRANSITION_RADICAL_FIXTURE = Path("certificates/hall/transition_radical_preservation")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

ADJOINTNESS_STATUS = "FINITE_HALL_PAIRING_COPRODUCT_ADJOINTNESS_OBSTRUCTION_VERIFIED"
SUPERSYMMETRY_STATUS = "FINITE_HALL_PAIRING_SUPERSYMMETRY_OBSTRUCTION_VERIFIED"
PAIRING_DEFINITION_STATUS = "FINITE_HALL_POSITIVE_NEGATIVE_PAIRING_OBSTRUCTION_VERIFIED"
PAIRING_KERNEL_LIM1_STATUS = "PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED"
TRANSITION_RADICAL_STATUS = "TRANSITION_RADICAL_PRESERVATION_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row362_coproduct_adjointness": ADJOINTNESS_STATUS,
    "row360_pairing_supersymmetry": SUPERSYMMETRY_STATUS,
    "row358_positive_negative_pairing": PAIRING_DEFINITION_STATUS,
    "pairing_kernel_lim1": PAIRING_KERNEL_LIM1_STATUS,
    "transition_radical": TRANSITION_RADICAL_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
}

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "local_qnd_rows": 0,
    "compact_source_G_entries": 0,
    "compact_source_K_entries": 0,
    "compact_source_Q_entries": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "pairing_kernel_lim1_rows": 0,
    "transition_radical_rows": 0,
    "source_quotient_rank_rows": 0,
    "source_determinant_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_G_entries",
    "left_radical_K_entries",
    "right_radical_K_entries",
    "quotient_Q_entries",
    "quotient_pairing_matrix",
    "quotient_rank_rows",
    "determinant_rows",
    "radical_identification_rows",
    "transition_radical_firewall",
    "lim1_firewall",
    "target_radical_firewall",
    "rank_equality_firewall",
}

REQUIRED_FIREWALL = {
    "hopf_adjointness",
    "pairing_invariance",
    "supersymmetry",
    "target_radical_table",
    "rank_equality_only",
    "signed_dimension",
    "scalar_trace",
    "denominator_product",
    "empty_G_entries",
    "empty_K_entries",
    "empty_Q_entries",
    "transition_radical_preservation",
    "pairing_kernel_lim1",
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
            "pairing_rows_required",
            "left_radical_rows_required",
            "right_radical_rows_required",
            "quotient_splittings_required",
            "quotient_pairing_matrix_required",
            "quotient_rank_rows_required",
            "determinant_rows_allowed",
            "radical_identification_rows_required",
            "relative_theorem_recorded",
            "current_source_qnd_proved",
            "transition_radical_claimed",
            "lim1_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "quotient_nondegeneracy_rows.csv",
        (
            "qnd_row_id",
            "R_id",
            "degree_id",
            "parity",
            "G_matrix_id",
            "left_radical_K_id",
            "right_radical_K_id",
            "left_quotient_Q_id",
            "right_quotient_Q_id",
            "quotient_pairing_matrix_id",
            "computed_rank",
            "left_quotient_dim",
            "right_quotient_dim",
            "determinant_id",
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
    TableSpec(
        "text_requirements.csv",
        (
            "requirement_id",
            "file_path",
            "required_fragment",
            "fragment_present",
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
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
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
        raise ValueError(f"{path}: expected no rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("row_number"), 363, "row_number")

    for key in (
        "relative_theorem_recorded",
        "coproduct_adjointness_packet_imported",
        "pairing_supersymmetry_packet_imported",
        "positive_negative_pairing_packet_imported",
        "pairing_kernel_lim1_packet_imported",
        "transition_radical_packet_imported",
        "compact_hall_source_ledger_imported",
        "quotient_rank_formula_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_G_entries_supplied",
        "source_K_entries_supplied",
        "source_Q_entries_supplied",
        "source_quotient_pairing_rows_supplied",
        "source_quotient_rank_rows_supplied",
        "source_determinant_rows_supplied",
        "source_radical_identification_rows_supplied",
        "quotient_nondegeneracy_proved_for_current_source",
        "transition_radical_preservation_proved",
        "pairing_kernel_lim1_vanishing_proved",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ADJOINTNESS_FIXTURE),
            str(SUPERSYMMETRY_FIXTURE),
            str(PAIRING_DEFINITION_FIXTURE),
            str(PAIRING_KERNEL_LIM1_FIXTURE),
            str(TRANSITION_RADICAL_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    sources = {row["source_id"]: row for row in tables["source_rows.csv"]}
    require_equal(set(sources), set(EXPECTED_SOURCE_ROWS), "source row ids")
    for source_id, status in EXPECTED_SOURCE_ROWS.items():
        row = sources[source_id]
        require_equal(row.get("source_status"), status, f"{source_id} status")
        require_equal(row.get("check_status"), "verified", f"{source_id} check")

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "pairing_rows_required",
        "left_radical_rows_required",
        "right_radical_rows_required",
        "quotient_splittings_required",
        "quotient_pairing_matrix_required",
        "quotient_rank_rows_required",
        "determinant_rows_allowed",
        "radical_identification_rows_required",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_qnd_proved",
        "transition_radical_claimed",
        "lim1_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-363 proposition")

    require_equal(len(tables["quotient_nondegeneracy_rows.csv"]), 0, "local qnd row count")

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

    for req in tables["text_requirements.csv"]:
        require_equal(req.get("fragment_present"), "true", f"{req['requirement_id']} fragment flag")
        require_equal(req.get("check_status"), "verified", f"{req['requirement_id']} status")


def check_pairing_kernel_lim1() -> None:
    manifest = read_json(PAIRING_KERNEL_LIM1_FIXTURE / "manifest.json")
    require_equal(manifest.get("status"), PAIRING_KERNEL_LIM1_STATUS, "pairing-kernel lim1 status")
    require_false(manifest.get("lim1_vanishing_certification"), "pairing-kernel lim1 certification")
    require_false(manifest.get("mathematical_certification"), "pairing-kernel mathematical certification")
    for key in (
        "compact_hall_packet_imported",
        "primitive_space_packet_imported",
        "transition_radical_packet_imported",
    ):
        require_true(manifest.get(key), f"pairing-kernel {key}")
    for table_name in (
        "pairing_maps.csv",
        "pairing_kernel_spaces.csv",
        "pairing_kernel_transition_maps.csv",
        "pairing_kernel_image_stabilization.csv",
        "pairing_kernel_ml_r1lim_defects.csv",
        "pairing_kernel_coverage.csv",
    ):
        require_table_empty(PAIRING_KERNEL_LIM1_FIXTURE / table_name)


def check_transition_radical() -> None:
    manifest = read_json(TRANSITION_RADICAL_FIXTURE / "manifest.json")
    require_equal(manifest.get("status"), TRANSITION_RADICAL_STATUS, "transition radical status")
    require_false(manifest.get("radical_transition_certification"), "transition radical certification")
    require_false(manifest.get("mathematical_certification"), "transition radical mathematical certification")
    for key in (
        "compact_hall_packet_imported",
        "primitive_transition_packet_imported",
    ):
        require_true(manifest.get(key), f"transition radical {key}")
    for table_name in (
        "pairing_transition.csv",
        "radical_kernel_rows.csv",
        "radical_transition_matrices.csv",
        "quotient_transition_matrices.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANSITION_RADICAL_FIXTURE / table_name)


def check_imports() -> None:
    adjointness = read_json(ADJOINTNESS_FIXTURE / "manifest.json")
    require_equal(adjointness.get("status"), ADJOINTNESS_STATUS, "row362 packet status")
    require_false(
        adjointness.get("coproduct_adjointness_proved_for_current_source"),
        "row362 current source adjointness",
    )
    require_false(adjointness.get("quotient_nondegeneracy_proved"), "row362 quotient nondegeneracy")

    supersymmetry = read_json(SUPERSYMMETRY_FIXTURE / "manifest.json")
    require_equal(supersymmetry.get("status"), SUPERSYMMETRY_STATUS, "row360 packet status")
    require_false(supersymmetry.get("source_G_entries_supplied"), "row360 source G entries")
    require_false(
        supersymmetry.get("pairing_supersymmetry_proved_for_current_source"),
        "row360 current source supersymmetry",
    )

    pairing_definition = read_json(PAIRING_DEFINITION_FIXTURE / "manifest.json")
    require_equal(pairing_definition.get("status"), PAIRING_DEFINITION_STATUS, "row358 packet status")
    require_false(pairing_definition.get("source_G_entries_supplied"), "row358 source G entries")
    require_false(pairing_definition.get("quotient_nondegeneracy_proved"), "row358 qnd")

    check_pairing_kernel_lim1()
    check_transition_radical()

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_source.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_source.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "G_entries.csv",
        "K_entries.csv",
        "Q_entries.csv",
        "hopf_pairing_identities.csv",
    ):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)


def check_text_requirements(fixture: Path) -> None:
    rows = read_table_path(
        fixture / "text_requirements.csv",
        next(spec.columns for spec in TABLE_SPECS if spec.path == "text_requirements.csv"),
    )
    for row in rows:
        path = Path(row["file_path"])
        if not path.exists():
            raise ValueError(f"{row['requirement_id']}: missing text file {path}")
        text = path.read_text(encoding="utf-8")
        if row["required_fragment"] not in text:
            raise ValueError(f"{row['requirement_id']}: required fragment not found")


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
    check_text_requirements(fixture)
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
