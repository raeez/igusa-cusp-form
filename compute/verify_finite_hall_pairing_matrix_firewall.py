#!/usr/bin/env python3
"""Verify the row-366 finite Hall pairing-matrix firewall packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_pairing_matrix_firewall.v1"
EXPECTED_KIND = "finite_hall_pairing_matrix_firewall_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PAIRING_MATRIX_FIREWALL_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:pairing-matrix-not-hopf-pairing-proof"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_pairing_matrix_firewall")

HPAIR_DEFECT_FIXTURE = Path("certificates/hall/finite_hall_hopf_pairing_defect_rows")
ADJOINTNESS_FIXTURE = Path("certificates/hall/finite_hall_pairing_coproduct_adjointness")
INVARIANCE_FIXTURE = Path("certificates/hall/finite_hall_pairing_invariance")
QND_FIXTURE = Path("certificates/hall/finite_hall_quotient_pairing_nondegeneracy")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

HPAIR_DEFECT_STATUS = "FINITE_HALL_HOPF_PAIRING_DEFECT_ROWS_OBSTRUCTION_VERIFIED"
ADJOINTNESS_STATUS = "FINITE_HALL_PAIRING_COPRODUCT_ADJOINTNESS_OBSTRUCTION_VERIFIED"
INVARIANCE_STATUS = "FINITE_HALL_PAIRING_INVARIANCE_OBSTRUCTION_VERIFIED"
QND_STATUS = "FINITE_HALL_QUOTIENT_PAIRING_NONDEGENERACY_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row365_hpair_defects": HPAIR_DEFECT_STATUS,
    "row362_coproduct_adjointness": ADJOINTNESS_STATUS,
    "row361_pairing_invariance": INVARIANCE_STATUS,
    "row363_quotient_nondegeneracy": QND_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
}

EXPECTED_COVERAGE = {
    "theorem_count": 1,
    "matrix_firewall_count": 8,
    "row365_hpair_defect_rows": 0,
    "row362_adjointness_rows": 0,
    "row361_invariance_rows": 0,
    "row363_quotient_nondegeneracy_rows": 0,
    "compact_source_G_entries": 0,
    "compact_source_K_entries": 0,
    "compact_source_Q_entries": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "compact_source_radical_ideal_coideal_rows": 0,
    "quotient_hopf_pairing_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_G_entries",
    "source_K_entries",
    "source_Q_entries",
    "hopf_adjointness_defects",
    "frobenius_cyclic_defects",
    "quotient_nondegeneracy_witnesses",
    "radical_coideal_rows",
    "radical_lie_ideal_rows",
    "quotient_hopf_pairing_rows",
    "source_vs_target_firewall",
    "scalar_trace_firewall",
}

REQUIRED_FIREWALL = {
    "pairing_matrix_only",
    "kernel_matrix_only",
    "quotient_splitting_only",
    "rank_equality_only",
    "row365_packet_only",
    "row363_qnd_only",
    "target_hopf_form",
    "target_radical_table",
    "denominator_product",
    "level_Z_protected_trace",
    "empty_compact_source",
}

REQUIRED_MATRIX_FIREWALL = {
    "G_only",
    "K_only",
    "Q_only",
    "rank_only",
    "target_radical",
    "denominator_product",
    "level_Z_trace",
    "empty_source",
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
        "theorem_rows.csv",
        (
            "theorem_id",
            "G_matrix_records_bilinear_form",
            "K_matrix_records_linear_radical",
            "Q_records_splitting",
            "hopf_adjointness_required",
            "frobenius_cyclic_required",
            "quotient_nondegeneracy_required",
            "radical_coideal_conclusion_conditional",
            "radical_lie_ideal_conclusion_conditional",
            "quotient_hopf_pairing_conclusion_conditional",
            "relative_theorem_recorded",
            "current_source_descent_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "matrix_firewall_rows.csv",
        (
            "firewall_row_id",
            "linear_payload",
            "forbidden_conclusion",
            "missing_required_input",
            "excluded",
            "proof_reference",
            "check_status",
            "notes",
        ),
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
    require_equal(manifest.get("row_number"), 366, "row_number")

    for key in (
        "relative_theorem_recorded",
        "hpair_defect_packet_imported",
        "coproduct_adjointness_packet_imported",
        "pairing_invariance_packet_imported",
        "quotient_nondegeneracy_packet_imported",
        "compact_hall_source_ledger_imported",
        "matrix_firewall_recorded",
        "radical_coideal_conditional_recorded",
        "radical_lie_ideal_conditional_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "current_source_G_entries_supplied",
        "current_source_K_entries_supplied",
        "current_source_Q_entries_supplied",
        "source_hopf_adjointness_rows_supplied",
        "source_frobenius_cyclic_rows_supplied",
        "source_quotient_nondegeneracy_rows_supplied",
        "source_radical_coideal_rows_supplied",
        "source_radical_lie_ideal_rows_supplied",
        "source_quotient_hopf_pairing_rows_supplied",
        "pairing_matrix_proves_hopf_radical",
        "hopf_radical_descent_proved_for_current_source",
        "radical_coideal_proved_for_current_source",
        "radical_lie_ideal_proved_for_current_source",
        "quotient_hopf_pairing_constructed_for_current_source",
        "target_radical_substitutes_for_source_radical",
        "level_Z_trace_substitutes_for_source_trace",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(HPAIR_DEFECT_FIXTURE),
            str(ADJOINTNESS_FIXTURE),
            str(INVARIANCE_FIXTURE),
            str(QND_FIXTURE),
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

    theorem = tables["theorem_rows.csv"]
    require_equal(len(theorem), 1, "theorem row count")
    row = theorem[0]
    for key in (
        "G_matrix_records_bilinear_form",
        "K_matrix_records_linear_radical",
        "Q_records_splitting",
        "hopf_adjointness_required",
        "frobenius_cyclic_required",
        "quotient_nondegeneracy_required",
        "radical_coideal_conclusion_conditional",
        "radical_lie_ideal_conclusion_conditional",
        "quotient_hopf_pairing_conclusion_conditional",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"theorem {key}")
    require_equal(row.get("current_source_descent_proved"), "false", "theorem current source")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("theorem proof reference does not point to row-366 proposition")

    matrix_firewall = {row["firewall_row_id"]: row for row in tables["matrix_firewall_rows.csv"]}
    require_equal(set(matrix_firewall), REQUIRED_MATRIX_FIREWALL, "matrix firewall ids")
    for firewall_id, frow in matrix_firewall.items():
        require_equal(frow.get("excluded"), "true", f"{firewall_id} excluded")
        require_equal(frow.get("check_status"), "verified", f"{firewall_id} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{firewall_id}: proof reference does not point to proposition")

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
    hpair = read_json(HPAIR_DEFECT_FIXTURE / "manifest.json")
    require_equal(hpair.get("status"), HPAIR_DEFECT_STATUS, "row365 packet status")
    require_false(hpair.get("current_source_defect_vanishing_proved"), "row365 current source")
    require_false(hpair.get("radical_coideal_proved_for_current_source"), "row365 coideal")
    require_false(hpair.get("radical_lie_ideal_proved_for_current_source"), "row365 Lie ideal")
    require_table_empty(HPAIR_DEFECT_FIXTURE / "hpair_defect_rows.csv")

    adjointness = read_json(ADJOINTNESS_FIXTURE / "manifest.json")
    require_equal(adjointness.get("status"), ADJOINTNESS_STATUS, "row362 packet status")
    require_false(adjointness.get("coproduct_adjointness_proved_for_current_source"), "row362 current source")
    require_table_empty(ADJOINTNESS_FIXTURE / "adjointness_rows.csv")

    invariance = read_json(INVARIANCE_FIXTURE / "manifest.json")
    require_equal(invariance.get("status"), INVARIANCE_STATUS, "row361 packet status")
    require_false(invariance.get("pairing_invariance_proved_for_current_source"), "row361 current source")
    require_table_empty(INVARIANCE_FIXTURE / "invariance_rows.csv")

    qnd = read_json(QND_FIXTURE / "manifest.json")
    require_equal(qnd.get("status"), QND_STATUS, "row363 packet status")
    require_false(qnd.get("quotient_nondegeneracy_proved_for_current_source"), "row363 current source")
    require_table_empty(QND_FIXTURE / "quotient_nondegeneracy_rows.csv")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_source.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_source.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "G_entries.csv",
        "K_entries.csv",
        "Q_entries.csv",
        "hopf_pairing_identities.csv",
        "radical_ideal_coideal.csv",
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
