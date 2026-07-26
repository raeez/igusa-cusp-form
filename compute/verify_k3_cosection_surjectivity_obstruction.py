#!/usr/bin/env python3
"""Verify the K3 cosection-surjectivity obstruction ledger.

A positive result means the row-274 obstruction ledger is complete and
the core surjectivity tables remain empty.  It does not prove
cosection surjectivity.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "K3_COSECTION_SURJECTIVITY_OBSTRUCTION_VERIFIED"
EXPECTED_SCHEMA = "k3_cosection_surjectivity_obstruction.v1"
EXPECTED_KIND = "k3_cosection_surjectivity_obstruction"
DEFAULT_FIXTURE = Path("certificates/orientation/k3_cosection_surjectivity")
COSECTION_FIXTURE = Path("certificates/orientation/k3_semiregularity_cosection")
RETAINED_CLASS_FIXTURE = Path("certificates/moduli/retained_class_bounds")
CHARGE_WINDOW_FIXTURE = Path("certificates/charge/k3e_charge_window")
D0_FIXTURE = Path("certificates/d0/k3e_d0_hn")
COSECTION_STATUS = "K3_SEMIREGULARITY_COSECTION_VERIFIED"
PROOF_LABEL = "prop:k3-cosection-surjectivity-criterion"
K3_WITNESS_COLUMNS = {
    "k3_class_id",
    "k3_curve_class_id",
    "k3_class_witness",
    "beta",
    "beta_id",
    "beta_nonzero",
    "nonzero_k3_class",
}
REQUIRED_OBLIGATIONS = {
    "nonzero_k3_class_witness",
    "branch_identification",
    "pointwise_surjectivity",
    "cokernel_rank_zero",
    "retained_strata_coverage",
    "no_scalar_substitution",
}
REQUIRED_FIREWALL = {
    "holomorphic_two_form_nonzero",
    "cosection_constructed",
    "dcritical_structure",
    "charge_id_only",
    "gram_degree_only",
    "OP_scalar_branch",
    "scalar_trace",
    "D0_empty_scaffold",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "criterion_rows.csv",
        (
            "criterion_id",
            "source_theorem",
            "required_witness",
            "required_branch",
            "required_cokernel_payload",
            "criterion_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "inspected_source_tables.csv",
        (
            "inspection_id",
            "source_table",
            "required_payload",
            "required_columns_present",
            "has_payload_rows",
            "inspection_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "k3_class_witness_rows.csv",
        (
            "witness_id",
            "substack_id",
            "class_id",
            "charge_id",
            "k3_curve_class_id",
            "beta_square",
            "beta_nonzero",
            "branch_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "surjectivity_rows.csv",
        (
            "surjectivity_id",
            "cosection_id",
            "substack_id",
            "witness_id",
            "source_theorem",
            "cokernel_row_id",
            "surjectivity_cokernel_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cokernel_rows.csv",
        (
            "cokernel_row_id",
            "cosection_id",
            "substack_id",
            "cokernel_sheaf_id",
            "cokernel_rank",
            "rank_defect",
            "proof_reference",
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
            "surjectivity_status",
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
            "source_reference",
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


def read_json(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"missing JSON file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root is not an object: {path}")
    return value


def read_table_path(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            raise ValueError(f"{path}: expected columns {columns}, got {actual}")
        return nonempty_rows(reader)


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns)


def read_header(path: Path) -> tuple[str, ...]:
    if not path.is_file():
        raise ValueError(f"missing inspected source table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        try:
            return tuple(next(reader))
        except StopIteration as exc:
            raise ValueError(f"empty inspected source table: {path}") from exc


def read_any_table(path: Path) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    if not path.is_file():
        raise ValueError(f"missing inspected source table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = tuple(reader.fieldnames or ())
        return header, nonempty_rows(reader)


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


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key}={value}")
        indexed[value] = row
    return indexed


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if proof_required and PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("mathematical_certification"), False, "mathematical_certification")
    require_equal(manifest.get("surjectivity_certification"), False, "surjectivity_certification")
    for key in (
        "k3_semiregularity_cosection_packet_imported",
        "retained_class_bounds_inspected",
        "d0_semiregularity_table_inspected",
        "surjectivity_rows_empty",
        "k3_class_witness_rows_empty",
        "cokernel_rows_empty",
    ):
        require_equal(manifest.get(key), True, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(COSECTION_FIXTURE), str(RETAINED_CLASS_FIXTURE), str(CHARGE_WINDOW_FIXTURE), str(D0_FIXTURE)},
        "imports",
    )


def verify_imports() -> None:
    cosection_manifest = read_json(COSECTION_FIXTURE / "manifest.json")
    require_equal(cosection_manifest.get("status"), COSECTION_STATUS, "cosection import status")
    for path in (
        RETAINED_CLASS_FIXTURE / "class_set.csv",
        CHARGE_WINDOW_FIXTURE / "gram_map.csv",
        D0_FIXTURE / "semiregularity_cosections.csv",
    ):
        read_header(path)


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"nonzero_k3_branch_surjectivity"}, "criterion ids")
    row = rows["nonzero_k3_branch_surjectivity"]
    check_verified(row, "criterion_rows.csv")
    require_equal(row["required_witness"], "beta_Rc_nonzero_in_H2_S", "required witness")
    require_equal(row["required_cokernel_payload"], "cokernel_rank_zero", "required cokernel payload")
    require_equal(int_cell(row, "criterion_defect_rank"), 0, "criterion defect")


def verify_empty_core_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    for table_name in ("k3_class_witness_rows.csv", "surjectivity_rows.csv", "cokernel_rows.csv"):
        if tables[table_name]:
            raise ValueError(f"{table_name} now has rows; retire or narrow obstruction packet")


def verify_inspections(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["inspected_source_tables.csv"], "inspection_id", "inspection rows")
    expected = {
        "retained_class_bounds_class_set": (RETAINED_CLASS_FIXTURE / "class_set.csv", False, False),
        "k3e_charge_window_gram_map": (CHARGE_WINDOW_FIXTURE / "gram_map.csv", False, False),
        "d0_semiregularity_cosections": (D0_FIXTURE / "semiregularity_cosections.csv", True, False),
    }
    require_equal(set(rows), set(expected), "inspection ids")
    for inspection_id, (source_path, expected_columns_present, expected_payload_rows) in expected.items():
        row = rows[inspection_id]
        check_verified(row, "inspected_source_tables.csv")
        require_equal(Path(row["source_table"]), source_path, f"{inspection_id} source table")
        header, source_rows = read_any_table(source_path)
        columns_present = bool(K3_WITNESS_COLUMNS.intersection(header))
        if "surjectivity_cokernel_rank" in header:
            columns_present = True
        require_equal(columns_present, expected_columns_present, f"{inspection_id} column presence")
        has_payload_rows = False
        if columns_present:
            witness_columns = K3_WITNESS_COLUMNS.intersection(header)
            for source_row in source_rows:
                if "surjectivity_cokernel_rank" in header and source_row.get("surjectivity_cokernel_rank"):
                    has_payload_rows = True
                if any(source_row.get(column, "") for column in witness_columns):
                    has_payload_rows = True
        require_equal(has_payload_rows, expected_payload_rows, f"{inspection_id} payload rows")
        require_equal(bool_cell(row, "required_columns_present"), expected_columns_present, f"{inspection_id} recorded columns")
        require_equal(bool_cell(row, "has_payload_rows"), expected_payload_rows, f"{inspection_id} recorded payload")
        require_equal(row["inspection_status"], "missing_open_obligation", f"{inspection_id} status")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        require_equal(row["surjectivity_status"], "missing_open_obligation", f"{row['obligation_id']} status")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        check_verified(row, "scalar_firewall.csv", proof_required=False)
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def verify_fixture(fixture: Path) -> None:
    if not fixture.is_dir():
        raise ValueError(f"fixture is not a directory: {fixture}")
    verify_manifest(fixture)
    verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_criterion(tables)
    verify_empty_core_tables(tables)
    verify_inspections(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"K3_COSECTION_SURJECTIVITY_OBSTRUCTION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
