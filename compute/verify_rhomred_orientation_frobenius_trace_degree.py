#!/usr/bin/env python3
"""Verify row-336 orientation Frobenius trace-degree packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_frobenius_trace_degree_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_frobenius_trace_degree_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_TRACE_DEGREE_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-frobenius-trace-degree"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_trace_degree")

ROW335_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_pairing")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
PROTECTED_GRAM_FIXTURE = Path("certificates/hybrid/protected_integration_gram_degree")
PROTECTED_TRACE_FIXTURE = Path("certificates/trace/k3e_protected_trace")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

ROW335_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_PAIRING_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
PAIRING_PUSHFORWARD_SCHEMA = "hall_pairing_pushforward_compatibility.v1"
PROTECTED_GRAM_STATUS = "PROTECTED_INTEGRATION_GRAM_DEGREE_VERIFIED"
TRACE_STATUS = "TRACE_OBSTRUCTION_LEDGER_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"
EXPECTED_TRACE_DEGREE = -3

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "expected_trace_degree": -3,
    "frobenius_pairing_rows": 0,
    "source_product_rows": 0,
    "source_pairing_rows": 0,
    "source_hopf_pairing_identity_rows": 0,
    "source_radical_rows": 0,
    "source_quotient_splitting_rows": 0,
    "formal_pairing_degree_zero_rows": 3,
    "protected_integration_gram_degree_rows": 1,
    "protected_trace_functor_rows": 0,
    "protected_trace_identity_rows": 0,
    "orientation_transition_rows": 0,
    "trace_degree_rows": 0,
    "row337_serre_sign_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_trace_functional",
    "source_trace_degree_row",
    "trace_pairing_identity",
    "trace_cyclicity_identity",
    "source_degree_convention",
    "orientation_trace_line",
    "serre_shift_line",
    "source_product_for_trace",
    "source_pairing_for_trace",
    "radical_quotient_for_trace",
    "quotient_orientation_transport",
    "trace_transition_compatibility",
    "orientation_transition_compatibility",
    "protected_trace_not_source_trace",
    "row337_serre_signs",
}

REQUIRED_FIREWALL = {
    "row335_Frobenius_criterion",
    "formal_pairing_degree_zero",
    "protected_integration_gram_s_degree",
    "protected_trace_empty_ledger",
    "Borcherds_s_degree",
    "compact_Hall_empty_ledger",
    "empty_M_entries",
    "empty_G_entries",
    "empty_hopf_pairing_identities",
    "empty_trace_degree_rows",
    "determinant_line_only",
    "square_root_obstruction_ledger",
    "scalar_trace",
    "protected_trace",
    "pfaffian_product",
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
            "frobenius_pairing_required",
            "source_trace_functional_required",
            "trace_pairing_identity_required",
            "trace_cyclicity_required",
            "source_degree_convention_required",
            "orientation_trace_line_required",
            "serre_shift_required",
            "radical_quotient_required",
            "transition_compatibility_required",
            "protected_integration_gram_degree_as_trace_allowed",
            "protected_trace_as_source_trace_allowed",
            "formal_pairing_degree_zero_as_trace_allowed",
            "criterion_recorded",
            "trace_degree_proved",
            "expected_trace_degree",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "trace_degree_rows.csv",
        (
            "trace_degree_row_id",
            "R_id",
            "stratum_id",
            "trace_functional_id",
            "source_quotient_id",
            "trace_line_id",
            "source_degree_convention_id",
            "orientation_line_degree_id",
            "serre_shift_id",
            "product_matrix_id",
            "pairing_matrix_id",
            "trace_pairing_identity_id",
            "trace_cyclicity_identity_id",
            "computed_trace_degree",
            "expected_trace_degree",
            "degree_defect_rank",
            "trace_degree_verified",
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


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


def require_empty_csv(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    require_equal(rows, [], str(path))


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("expected_trace_degree"), EXPECTED_TRACE_DEGREE, "expected trace degree")
    for key in (
        "frobenius_pairing_imported",
        "compact_hall_ledger_imported",
        "hall_pairing_pushforward_imported",
        "protected_integration_gram_degree_imported",
        "protected_trace_ledger_imported",
        "transition_orientation_ledger_imported",
        "trace_degree_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_trace_functional_rows_supplied",
        "source_trace_degree_rows_supplied",
        "trace_pairing_identity_rows_supplied",
        "trace_cyclicity_rows_supplied",
        "source_degree_convention_rows_supplied",
        "orientation_trace_line_rows_supplied",
        "serre_shift_rows_supplied",
        "radical_quotient_rows_supplied",
        "quotient_orientation_rows_supplied",
        "transition_rows_supplied",
        "frobenius_trace_degree_proved",
        "row337_serre_sign_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW335_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(PROTECTED_GRAM_FIXTURE),
            str(PROTECTED_TRACE_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    row335 = read_json(ROW335_FIXTURE / "manifest.json")
    require_equal(row335.get("status"), ROW335_STATUS, "row335 status")
    require_equal(row335.get("frobenius_pairing_proved"), False, "row335 proved")
    require_equal(row335.get("row336_trace_degree_claimed"), False, "row335 trace degree flag")
    require_empty_csv(ROW335_FIXTURE / "frobenius_pairing_rows.csv")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty")
    for table in (
        "M_entries.csv",
        "G_entries.csv",
        "K_entries.csv",
        "Q_entries.csv",
        "hopf_pairing_identities.csv",
    ):
        require_empty_csv(COMPACT_HALL_FIXTURE / table)

    pairing_pushforward = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pairing_pushforward.get("schema_version"), PAIRING_PUSHFORWARD_SCHEMA, "pairing pushforward schema")
    require_equal(pairing_pushforward.get("certified"), True, "pairing pushforward certified")
    require_equal(pairing_pushforward.get("normal_ordered_pairing_degree"), True, "pairing degree")
    require_equal(pairing_pushforward.get("protected_trace"), False, "pairing protected trace")
    pairing_rows = read_table_path(PAIRING_PUSHFORWARD_FIXTURE / "pairing_rows.csv")
    require_equal(len(pairing_rows), 3, "formal pairing rows")
    for row in pairing_rows:
        require_equal(bool_cell(row, "homogeneous_degree_zero"), True, "formal pairing degree zero")
        require_equal(int_cell(row, "total_degree_m"), 0, "formal pairing m degree")

    gram = read_json(PROTECTED_GRAM_FIXTURE / "manifest.json")
    require_equal(gram.get("status"), PROTECTED_GRAM_STATUS, "protected gram status")
    require_equal(gram.get("gram_degree_certification"), True, "gram degree certification")
    require_equal(gram.get("protected_trace_certification"), False, "gram protected trace")
    gram_rows = read_table_path(PROTECTED_GRAM_FIXTURE / "integration_degree_rows.csv")
    require_equal(len(gram_rows), 1, "protected integration gram degree rows")
    require_equal(gram_rows[0]["s_degree_id"], "m_R", "protected integration s degree")

    trace = read_json(PROTECTED_TRACE_FIXTURE / "manifest.json")
    require_equal(trace.get("obstruction_ledger_status"), TRACE_STATUS, "trace obstruction status")
    require_equal(trace.get("empty_blocked"), True, "trace empty")
    require_equal(trace.get("protected_trace_certification"), False, "trace certification")
    for table in (
        "protected_trace_functors.csv",
        "trace_identities.csv",
        "trace_categories.csv",
        "trace_operators.csv",
    ):
        require_empty_csv(PROTECTED_TRACE_FIXTURE / table)

    transition_orientation = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(transition_orientation.get("status"), TRANSITION_ORIENTATION_STATUS, "transition orientation status")
    require_equal(transition_orientation.get("orientation_transition_certification"), False, "transition orientation certification")
    require_empty_csv(TRANSITION_ORIENTATION_FIXTURE / "orientation_transition_maps.csv")


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "frobenius_pairing",
            "compact_hall_source",
            "hall_pairing_pushforward",
            "protected_integration_gram_degree",
            "protected_trace",
            "transition_orientation",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "orientation_frobenius_trace_degree", "criterion id")
    for key in (
        "frobenius_pairing_required",
        "source_trace_functional_required",
        "trace_pairing_identity_required",
        "trace_cyclicity_required",
        "source_degree_convention_required",
        "orientation_trace_line_required",
        "serre_shift_required",
        "radical_quotient_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in (
        "protected_integration_gram_degree_as_trace_allowed",
        "protected_trace_as_source_trace_allowed",
        "formal_pairing_degree_zero_as_trace_allowed",
        "trace_degree_proved",
    ):
        require_equal(bool_cell(row, key), False, key)
    require_equal(int_cell(row, "expected_trace_degree"), EXPECTED_TRACE_DEGREE, "criterion expected degree")
    check_verified(row, "criterion_rows.csv")


def verify_coverage(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    for key, expected in EXPECTED_COVERAGE.items():
        row = indexed[key]
        require_equal(int_cell(row, "computed_value"), expected, f"{key} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{key} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{key} defect")
        require_equal(row.get("check_status"), "verified", f"{key} status")


def verify_obligations(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "obligation_id", "blocked_obligations.csv")
    require_equal(set(indexed), REQUIRED_OBLIGATIONS, "obligation ids")
    for row in indexed.values():
        require_equal(row["compatibility_status"], "missing_open_obligation", "obligation status")
        check_verified(row, "blocked_obligations.csv")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "forbidden_substitute", "scalar_firewall.csv")
    require_equal(set(indexed), REQUIRED_FIREWALL, "firewall substitutes")
    for row in indexed.values():
        require_equal(bool_cell(row, "excluded"), True, "firewall excluded")
        require_equal(int_cell(row, "defect_rank"), 0, "firewall defect")
        check_verified(row, "scalar_firewall.csv")


def verify_fixture(fixture: Path) -> None:
    verify_manifest(fixture)
    verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    verify_criterion(tables["criterion_rows.csv"])
    require_equal(tables["trace_degree_rows.csv"], [], "trace degree rows")
    verify_coverage(tables["coverage_rows.csv"])
    verify_obligations(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
