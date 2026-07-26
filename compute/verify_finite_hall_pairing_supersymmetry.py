#!/usr/bin/env python3
"""Verify the row-360 finite Hall pairing-supersymmetry packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_pairing_supersymmetry.v1"
EXPECTED_KIND = "finite_hall_pairing_supersymmetry_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PAIRING_SUPERSYMMETRY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-pairing-supersymmetry"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_pairing_supersymmetry")

HOMOGENEITY_FIXTURE = Path("certificates/hall/finite_hall_pairing_homogeneity")
PAIRING_DEFINITION_FIXTURE = Path("certificates/hall/finite_hall_positive_negative_pairing")
SERRE_SIGN_FIXTURE = Path("certificates/orientation/rhomred_orientation_cy3_serre_signs")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

HOMOGENEITY_STATUS = "FINITE_HALL_PAIRING_HOMOGENEITY_OBSTRUCTION_VERIFIED"
PAIRING_DEFINITION_STATUS = "FINITE_HALL_POSITIVE_NEGATIVE_PAIRING_OBSTRUCTION_VERIFIED"
SERRE_SIGN_STATUS = "RHOMRED_ORIENTATION_CY3_SERRE_SIGNS_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row359_pairing_homogeneity": HOMOGENEITY_STATUS,
    "row358_positive_negative_pairing": PAIRING_DEFINITION_STATUS,
    "row337_serre_signs": SERRE_SIGN_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
}

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "local_supersymmetry_rows": 0,
    "compact_source_G_entries": 0,
    "compact_source_parity_rows": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "serre_sign_rows": 0,
    "source_orientation_transport_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_G_entries",
    "opposite_G_entries",
    "source_parity_blocks",
    "signed_transpose_rows",
    "serre_sign_rows",
    "orientation_transport",
    "formal_pairing_firewall",
    "row361_362_firewall",
    "source_vs_target_firewall",
}

REQUIRED_FIREWALL = {
    "formal_pairing_rows",
    "target_pairing_blocks",
    "row359_homogeneity_only",
    "row337_serre_sign_criterion_only",
    "scalar_trace",
    "denominator_product",
    "signed_dimension",
    "empty_G_entries",
    "empty_supersymmetry_rows",
    "invariance_shortcut",
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
            "positive_negative_pairing_required",
            "homogeneity_required",
            "signed_transpose_rows_required",
            "source_parity_blocks_required",
            "cy3_serre_sign_rows_required",
            "orientation_transport_required",
            "relative_theorem_recorded",
            "current_source_supersymmetry_proved",
            "invariance_claimed",
            "coproduct_claimed",
            "quotient_nondegeneracy_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "supersymmetry_rows.csv",
        (
            "supersymmetry_row_id",
            "R_id",
            "degree_id",
            "parity",
            "positive_basis_id",
            "negative_basis_id",
            "G_positive_negative_entry_id",
            "G_negative_positive_entry_id",
            "computed_signed_difference",
            "expected_signed_difference",
            "supersymmetry_verified",
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
    require_equal(manifest.get("row_number"), 360, "row_number")

    for key in (
        "relative_theorem_recorded",
        "pairing_homogeneity_packet_imported",
        "positive_negative_pairing_packet_imported",
        "cy3_serre_sign_packet_imported",
        "compact_hall_source_ledger_imported",
        "signed_transpose_formula_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_G_entries_supplied",
        "source_parity_blocks_supplied",
        "source_signed_transpose_rows_supplied",
        "source_serre_sign_rows_supplied",
        "source_orientation_transport_rows_supplied",
        "pairing_supersymmetry_proved_for_current_source",
        "invariance_proved",
        "coproduct_compatibility_proved",
        "quotient_nondegeneracy_proved",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(HOMOGENEITY_FIXTURE),
            str(PAIRING_DEFINITION_FIXTURE),
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
        "positive_negative_pairing_required",
        "homogeneity_required",
        "signed_transpose_rows_required",
        "source_parity_blocks_required",
        "cy3_serre_sign_rows_required",
        "orientation_transport_required",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_supersymmetry_proved",
        "invariance_claimed",
        "coproduct_claimed",
        "quotient_nondegeneracy_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-360 proposition")

    require_equal(len(tables["supersymmetry_rows.csv"]), 0, "local supersymmetry row count")

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
    homogeneity = read_json(HOMOGENEITY_FIXTURE / "manifest.json")
    require_equal(homogeneity.get("status"), HOMOGENEITY_STATUS, "row359 packet status")
    require_false(
        homogeneity.get("pairing_homogeneity_proved_for_current_source"),
        "row359 current source homogeneity",
    )
    require_false(homogeneity.get("supersymmetry_proved"), "row359 supersymmetry")

    pairing_definition = read_json(PAIRING_DEFINITION_FIXTURE / "manifest.json")
    require_equal(pairing_definition.get("status"), PAIRING_DEFINITION_STATUS, "row358 packet status")
    require_false(pairing_definition.get("source_G_entries_supplied"), "row358 source G entries")
    require_false(pairing_definition.get("supersymmetry_proved"), "row358 supersymmetry")

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
