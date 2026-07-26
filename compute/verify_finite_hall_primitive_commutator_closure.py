#!/usr/bin/env python3
"""Verify the row-354 finite Hall primitive-commutator closure packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_primitive_commutator_closure.v1"
EXPECTED_KIND = "finite_hall_primitive_commutator_closure_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PRIMITIVE_COMMUTATOR_CLOSURE_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:hall-bialgebra-defects-primitive-closure"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_primitive_commutator_closure")

PRIMITIVE_FIXTURE = Path("certificates/hall/finite_hall_primitive_subspace_definition")
BIALGEBRA_FIXTURE = Path("certificates/hall/finite_hall_bialgebra_compatibility")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

PRIMITIVE_STATUS = "FINITE_HALL_PRIMITIVE_SUBSPACE_DEFINITION_OBSTRUCTION_VERIFIED"
BIALGEBRA_STATUS = "FINITE_HALL_BIALGEBRA_COMPATIBILITY_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "primitive_closure_rows": 0,
    "row353_primitive_kernel_rows": 0,
    "row350_compatibility_rows": 0,
    "source_product_matrix_rows": 0,
    "source_coproduct_matrix_rows": 0,
    "source_unit_counit_rows": 0,
    "source_bialgebra_identity_rows": 0,
    "source_supercommutator_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "primitive_subspace_rows",
    "product_matrix_rows",
    "coproduct_matrix_rows",
    "unit_counit_rows",
    "associativity_rows",
    "bialgebra_compatibility_rows",
    "counit_multiplicativity_rows",
    "primitive_closure_defect_rows",
    "supercommutator_matrix_rows",
    "graded_jacobi_rows",
}

REQUIRED_FIREWALL = {
    "primitive_space_definition",
    "product_only",
    "coproduct_only",
    "bialgebra_criterion_without_rows",
    "hopf_pairing",
    "target_root_space",
    "scalar_trace",
    "signed_multiplicity",
    "bar_coalgebra_primitives",
    "jacobi_shortcut",
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
            "primitive_subspace_required",
            "associative_product_required",
            "counital_coproduct_required",
            "bialgebra_compatibility_required",
            "reduced_coproduct_kernel_required",
            "epsilon_algebra_homomorphism_required",
            "supercommutator_formula_required",
            "closure_defect_zero_required",
            "relative_theorem_recorded",
            "current_source_closure_proved",
            "primitive_bracket_populated",
            "graded_jacobi_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "primitive_closure_rows.csv",
        (
            "closure_row_id",
            "R_id",
            "left_primitive_basis_id",
            "right_primitive_basis_id",
            "product_matrix_id",
            "coproduct_matrix_id",
            "counit_matrix_id",
            "bialgebra_identity_row_id",
            "supercommutator_matrix_id",
            "reduced_coproduct_defect_rank",
            "counit_defect_rank",
            "closure_verified",
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
        raise ValueError(f"{path}: expected no rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("row_number"), 354, "row_number")

    for key in (
        "relative_theorem_recorded",
        "primitive_subspace_packet_imported",
        "bialgebra_compatibility_packet_imported",
        "compact_hall_source_ledger_imported",
        "closure_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "product_matrix_rows_supplied",
        "coproduct_matrix_rows_supplied",
        "unit_counit_rows_supplied",
        "primitive_kernel_rows_supplied",
        "bialgebra_identity_rows_supplied",
        "primitive_closure_rows_supplied",
        "supercommutator_matrix_rows_supplied",
        "primitive_commutator_closure_proved_for_current_source",
        "primitive_bracket_populated",
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
        {str(PRIMITIVE_FIXTURE), str(BIALGEBRA_FIXTURE), str(COMPACT_SOURCE_FIXTURE)},
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "primitive_subspace_required",
        "associative_product_required",
        "counital_coproduct_required",
        "bialgebra_compatibility_required",
        "reduced_coproduct_kernel_required",
        "epsilon_algebra_homomorphism_required",
        "supercommutator_formula_required",
        "closure_defect_zero_required",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_closure_proved",
        "primitive_bracket_populated",
        "graded_jacobi_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-354 proposition")

    require_equal(len(tables["primitive_closure_rows.csv"]), 0, "primitive closure row count")

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
    primitive = read_json(PRIMITIVE_FIXTURE / "manifest.json")
    require_equal(primitive.get("status"), PRIMITIVE_STATUS, "primitive packet status")
    require_false(primitive.get("primitive_subspace_populated"), "row353 populated primitive")
    require_false(primitive.get("primitive_bracket_claimed"), "row353 primitive bracket")
    require_table_empty(PRIMITIVE_FIXTURE / "primitive_kernel_rows.csv")

    bialgebra = read_json(BIALGEBRA_FIXTURE / "manifest.json")
    require_equal(bialgebra.get("status"), BIALGEBRA_STATUS, "bialgebra packet status")
    require_false(bialgebra.get("actual_bialgebra_compatibility_proved"), "row350 actual bialgebra")
    require_false(bialgebra.get("finite_hall_bialgebra_populated"), "row350 populated bialgebra")
    require_table_empty(BIALGEBRA_FIXTURE / "compatibility_rows.csv")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(
        compact_source.get("obstruction_ledger_status"),
        COMPACT_SOURCE_STATUS,
        "compact source status",
    )
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(
        compact_source.get("mathematical_certification"),
        "compact source mathematical certification",
    )
    for table_name in (
        "M_entries.csv",
        "D_entries.csv",
        "unit_counit.csv",
        "hall_bialgebra_identities.csv",
        "B_entries.csv",
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
