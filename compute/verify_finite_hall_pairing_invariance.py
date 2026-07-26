#!/usr/bin/env python3
"""Verify the row-361 finite Hall pairing-invariance packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_pairing_invariance.v1"
EXPECTED_KIND = "finite_hall_pairing_invariance_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PAIRING_INVARIANCE_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-pairing-invariance"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_pairing_invariance")

SUPERSYMMETRY_FIXTURE = Path("certificates/hall/finite_hall_pairing_supersymmetry")
BRACKET_PARITY_FIXTURE = Path("certificates/hall/finite_hall_bracket_parity")
GRADED_JACOBI_FIXTURE = Path("certificates/hall/finite_hall_graded_jacobi")
SERRE_SIGN_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_serre_signs")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

SUPERSYMMETRY_STATUS = "FINITE_HALL_PAIRING_SUPERSYMMETRY_OBSTRUCTION_VERIFIED"
BRACKET_PARITY_STATUS = "FINITE_HALL_BRACKET_PARITY_OBSTRUCTION_VERIFIED"
GRADED_JACOBI_STATUS = "FINITE_HALL_GRADED_JACOBI_OBSTRUCTION_VERIFIED"
SERRE_SIGN_STATUS = "RHOMRED_ORIENTATION_CY3_SERRE_SIGNS_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row360_pairing_supersymmetry": SUPERSYMMETRY_STATUS,
    "row357_bracket_parity": BRACKET_PARITY_STATUS,
    "row355_graded_jacobi": GRADED_JACOBI_STATUS,
    "row337_serre_signs": SERRE_SIGN_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
}

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "local_invariance_rows": 0,
    "compact_source_G_entries": 0,
    "compact_source_B_entries": 0,
    "compact_source_parity_rows": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "serre_sign_rows": 0,
    "source_cyclic_correspondence_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_G_entries",
    "source_primitive_bracket_rows",
    "source_parity_blocks",
    "frobenius_defect_rows",
    "cyclic_correspondence_rows",
    "serre_sign_rows",
    "orientation_transport",
    "super_skew_rows",
    "formal_pairing_firewall",
    "target_invariant_pairing_firewall",
    "row362_firewall",
    "source_vs_target_firewall",
}

REQUIRED_FIREWALL = {
    "formal_pairing_rows",
    "target_pairing_blocks",
    "target_invariant_pairing",
    "row360_supersymmetry_only",
    "row357_parity_only",
    "row355_jacobi_only",
    "row337_serre_sign_criterion_only",
    "scalar_trace",
    "denominator_product",
    "signed_dimension",
    "empty_G_entries",
    "empty_B_entries",
    "empty_hopf_pairing_identities",
    "coproduct_shortcut",
}

SERRE_FALSE_FLAGS = (
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
    "mathematical_certification",
)


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
            "pairing_supersymmetry_required",
            "bracket_parity_required",
            "super_skew_bracket_required",
            "frobenius_defect_rows_required",
            "source_G_entries_required",
            "source_bracket_rows_required",
            "cy3_serre_sign_rows_required",
            "orientation_transport_required",
            "relative_theorem_recorded",
            "current_source_invariance_proved",
            "coproduct_claimed",
            "quotient_nondegeneracy_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "invariance_rows.csv",
        (
            "invariance_row_id",
            "R_id",
            "left_degree_id",
            "middle_degree_id",
            "right_degree_id",
            "left_parity",
            "middle_parity",
            "right_parity",
            "bracket_entry_id",
            "pairing_entry_id",
            "computed_frobenius_defect",
            "expected_frobenius_defect",
            "invariance_verified",
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
    require_equal(manifest.get("row_number"), 361, "row_number")

    for key in (
        "relative_theorem_recorded",
        "pairing_supersymmetry_packet_imported",
        "bracket_parity_packet_imported",
        "graded_jacobi_packet_imported",
        "cy3_serre_sign_packet_imported",
        "compact_hall_source_ledger_imported",
        "frobenius_formula_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_G_entries_supplied",
        "source_primitive_bracket_rows_supplied",
        "source_parity_blocks_supplied",
        "source_frobenius_defect_rows_supplied",
        "source_cyclic_correspondence_rows_supplied",
        "source_serre_sign_rows_supplied",
        "source_orientation_transport_rows_supplied",
        "pairing_invariance_proved_for_current_source",
        "coproduct_compatibility_proved",
        "quotient_nondegeneracy_proved",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(SUPERSYMMETRY_FIXTURE),
            str(BRACKET_PARITY_FIXTURE),
            str(GRADED_JACOBI_FIXTURE),
            str(SERRE_SIGN_FIXTURE),
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
        "pairing_supersymmetry_required",
        "bracket_parity_required",
        "super_skew_bracket_required",
        "frobenius_defect_rows_required",
        "source_G_entries_required",
        "source_bracket_rows_required",
        "cy3_serre_sign_rows_required",
        "orientation_transport_required",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_invariance_proved",
        "coproduct_claimed",
        "quotient_nondegeneracy_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-361 proposition")

    require_equal(len(tables["invariance_rows.csv"]), 0, "local invariance row count")

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


def check_imports() -> None:
    supersymmetry = read_json(SUPERSYMMETRY_FIXTURE / "manifest.json")
    require_equal(supersymmetry.get("status"), SUPERSYMMETRY_STATUS, "row360 packet status")
    require_false(
        supersymmetry.get("pairing_supersymmetry_proved_for_current_source"),
        "row360 current source supersymmetry",
    )
    require_false(supersymmetry.get("invariance_proved"), "row360 invariance")

    bracket_parity = read_json(BRACKET_PARITY_FIXTURE / "manifest.json")
    require_equal(bracket_parity.get("status"), BRACKET_PARITY_STATUS, "row357 packet status")
    require_false(
        bracket_parity.get("bracket_parity_proved_for_current_source"),
        "row357 current source parity",
    )
    require_false(bracket_parity.get("primitive_lie_algebra_populated"), "row357 primitive Lie algebra")

    graded_jacobi = read_json(GRADED_JACOBI_FIXTURE / "manifest.json")
    require_equal(graded_jacobi.get("status"), GRADED_JACOBI_STATUS, "row355 packet status")
    require_false(
        graded_jacobi.get("graded_jacobi_proved_for_current_source"),
        "row355 current source Jacobi",
    )
    require_false(graded_jacobi.get("primitive_lie_algebra_populated"), "row355 primitive Lie algebra")

    serre = read_json(SERRE_SIGN_FIXTURE / "manifest.json")
    require_equal(serre.get("status"), SERRE_SIGN_STATUS, "row337 Serre-sign status")
    require_true(serre.get("serre_sign_criterion_recorded"), "Serre-sign criterion")
    for key in SERRE_FALSE_FLAGS:
        require_false(serre.get(key), f"Serre-sign {key}")
    require_table_empty(SERRE_SIGN_FIXTURE / "serre_sign_rows.csv")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_source.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_source.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "B_entries.csv",
        "G_entries.csv",
        "parity_blocks.csv",
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
