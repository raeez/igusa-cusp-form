#!/usr/bin/env python3
"""Verify the row-362 finite Hall pairing-coproduct adjointness packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_pairing_coproduct_adjointness.v1"
EXPECTED_KIND = "finite_hall_pairing_coproduct_adjointness_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PAIRING_COPRODUCT_ADJOINTNESS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-pairing-coproduct-adjointness"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_pairing_coproduct_adjointness")

INVARIANCE_FIXTURE = Path("certificates/hall/finite_hall_pairing_invariance")
PRODUCT_OPERATOR_FIXTURE = Path("certificates/hall/finite_hall_product_operator")
COPRODUCT_OPERATOR_FIXTURE = Path("certificates/hall/finite_hall_coproduct_operator")
BIALGEBRA_FIXTURE = Path("certificates/hall/finite_hall_bialgebra_compatibility")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

INVARIANCE_STATUS = "FINITE_HALL_PAIRING_INVARIANCE_OBSTRUCTION_VERIFIED"
PRODUCT_OPERATOR_STATUS = "FINITE_HALL_PRODUCT_OPERATOR_DEFINITION_VERIFIED"
COPRODUCT_OPERATOR_STATUS = "FINITE_HALL_COPRODUCT_OPERATOR_DEFINITION_VERIFIED"
BIALGEBRA_STATUS = "FINITE_HALL_BIALGEBRA_COMPATIBILITY_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row361_pairing_invariance": INVARIANCE_STATUS,
    "row342_product_operator": PRODUCT_OPERATOR_STATUS,
    "row347_coproduct_operator": COPRODUCT_OPERATOR_STATUS,
    "row350_bialgebra_compatibility": BIALGEBRA_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
}

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "local_adjointness_rows": 0,
    "compact_source_M_entries": 0,
    "compact_source_D_entries": 0,
    "compact_source_G_entries": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "row342_product_operator_rows": 0,
    "row347_coproduct_operator_rows": 0,
    "row350_bialgebra_compatibility_rows": 0,
    "source_tensor_pairing_sign_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_M_entries",
    "source_D_entries",
    "source_G_entries",
    "tensor_pairing_sign_rows",
    "hopf_adjointness_rows",
    "product_correspondence_rows",
    "coproduct_correspondence_rows",
    "orientation_transport",
    "bialgebra_not_adjointness",
    "invariance_not_adjointness",
    "target_hopf_form_firewall",
    "source_vs_target_firewall",
}

REQUIRED_FIREWALL = {
    "bialgebra_compatibility",
    "pairing_invariance",
    "target_hopf_form",
    "formal_pairing_rows",
    "scalar_trace",
    "denominator_product",
    "signed_dimension",
    "empty_M_entries",
    "empty_D_entries",
    "empty_G_entries",
    "empty_hopf_pairing_identities",
    "quotient_nondegeneracy",
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
            "product_rows_required",
            "coproduct_rows_required",
            "pairing_rows_required",
            "tensor_pairing_sign_rows_required",
            "hopf_adjointness_rows_required",
            "product_correspondence_rows_required",
            "coproduct_correspondence_rows_required",
            "orientation_transport_required",
            "relative_theorem_recorded",
            "current_source_adjointness_proved",
            "quotient_nondegeneracy_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "adjointness_rows.csv",
        (
            "adjointness_row_id",
            "R_id",
            "left_degree_id",
            "right_degree_id",
            "output_degree_id",
            "left_parity",
            "right_parity",
            "output_parity",
            "product_entry_id",
            "coproduct_entry_id",
            "pairing_entry_ids",
            "tensor_sign_id",
            "computed_adjointness_defect",
            "expected_adjointness_defect",
            "adjointness_verified",
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
    require_equal(manifest.get("row_number"), 362, "row_number")

    for key in (
        "relative_theorem_recorded",
        "pairing_invariance_packet_imported",
        "product_operator_packet_imported",
        "coproduct_operator_packet_imported",
        "bialgebra_compatibility_packet_imported",
        "compact_hall_source_ledger_imported",
        "adjointness_formula_recorded",
        "tensor_pairing_sign_formula_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_M_entries_supplied",
        "source_D_entries_supplied",
        "source_G_entries_supplied",
        "source_tensor_pairing_sign_rows_supplied",
        "source_hopf_adjointness_rows_supplied",
        "source_product_correspondence_rows_supplied",
        "source_coproduct_correspondence_rows_supplied",
        "source_orientation_transport_rows_supplied",
        "coproduct_adjointness_proved_for_current_source",
        "quotient_nondegeneracy_proved",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(INVARIANCE_FIXTURE),
            str(PRODUCT_OPERATOR_FIXTURE),
            str(COPRODUCT_OPERATOR_FIXTURE),
            str(BIALGEBRA_FIXTURE),
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
        "product_rows_required",
        "coproduct_rows_required",
        "pairing_rows_required",
        "tensor_pairing_sign_rows_required",
        "hopf_adjointness_rows_required",
        "product_correspondence_rows_required",
        "coproduct_correspondence_rows_required",
        "orientation_transport_required",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_adjointness_proved",
        "quotient_nondegeneracy_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-362 proposition")

    require_equal(len(tables["adjointness_rows.csv"]), 0, "local adjointness row count")

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
    invariance = read_json(INVARIANCE_FIXTURE / "manifest.json")
    require_equal(invariance.get("status"), INVARIANCE_STATUS, "row361 packet status")
    require_false(
        invariance.get("pairing_invariance_proved_for_current_source"),
        "row361 current source invariance",
    )
    require_false(invariance.get("coproduct_compatibility_proved"), "row361 coproduct compatibility")

    product = read_json(PRODUCT_OPERATOR_FIXTURE / "manifest.json")
    require_equal(product.get("status"), PRODUCT_OPERATOR_STATUS, "row342 product status")
    require_false(product.get("product_matrix_rows_supplied"), "row342 product matrices")
    require_false(product.get("finite_hall_product_populated"), "row342 product populated")
    require_table_empty(PRODUCT_OPERATOR_FIXTURE / "product_operator_rows.csv")

    coproduct = read_json(COPRODUCT_OPERATOR_FIXTURE / "manifest.json")
    require_equal(coproduct.get("status"), COPRODUCT_OPERATOR_STATUS, "row347 coproduct status")
    require_false(coproduct.get("coproduct_matrix_rows_supplied"), "row347 coproduct matrices")
    require_false(coproduct.get("finite_hall_coproduct_populated"), "row347 coproduct populated")
    require_table_empty(COPRODUCT_OPERATOR_FIXTURE / "coproduct_operator_rows.csv")

    bialgebra = read_json(BIALGEBRA_FIXTURE / "manifest.json")
    require_equal(bialgebra.get("status"), BIALGEBRA_STATUS, "row350 bialgebra status")
    require_false(bialgebra.get("product_matrix_rows_supplied"), "row350 product matrices")
    require_false(bialgebra.get("coproduct_matrix_rows_supplied"), "row350 coproduct matrices")
    require_false(
        bialgebra.get("hall_bialgebra_compatibility_rows_supplied"),
        "row350 bialgebra rows",
    )
    require_false(
        bialgebra.get("actual_bialgebra_compatibility_proved"),
        "row350 actual bialgebra",
    )
    require_table_empty(BIALGEBRA_FIXTURE / "compatibility_rows.csv")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_source.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_source.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "M_entries.csv",
        "D_entries.csv",
        "G_entries.csv",
        "hopf_pairing_identities.csv",
        "hall_bialgebra_identities.csv",
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
