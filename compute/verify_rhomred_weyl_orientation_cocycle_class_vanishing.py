#!/usr/bin/env python3
"""Verify the row-310 orientation cocycle class-vanishing packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_cocycle_class_vanishing_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_cocycle_class_vanishing_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_CLASS_VANISHING_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-cocycle-class-vanishing-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_cocycle_class_vanishing")

ORIENTATION_COCYCLE_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_cocycle")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")

ORIENTATION_COCYCLE_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_OBSTRUCTION_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "row309_cocycle_value_rows": 0,
    "row309_normalization_rows": 0,
    "row309_cocycle_defect_rows": 0,
    "coxeter_cocycle_rows": 0,
    "cochain_complex_rows": 0,
    "class_vanishing_rows": 0,
    "cocycle_class_vanishing_claim": 0,
    "cochain_witness_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "populated_orientation_cocycle",
    "cocycle_closedness",
    "coefficient_system",
    "finite_components",
    "normalized_cochain_bases",
    "coboundary_matrix",
    "cocycle_vector",
    "rank_certificate",
    "cochain_witness_later",
    "no_target_coxeter_substitution",
    "no_maass_character_substitution",
    "no_abstract_group_cohomology_substitution",
}

REQUIRED_FIREWALL = {
    "row309_formula_only",
    "target_coxeter_graph",
    "maass_character_value",
    "tau_square_criterion",
    "constant_group_cohomology",
    "complete_orbit_without_rows",
    "unverified_cochain_witness",
}

REQUIRED_ORIENTATION_OBLIGATIONS = {
    "coxeter_projective_cocycle",
    "coxeter_cochain_trivialization",
    "coxeter_coherence",
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
            "cocycle_table_required",
            "coefficient_system_required",
            "normalized_complex_required",
            "d1_matrix_required",
            "cocycle_vector_required",
            "cocycle_closed_required",
            "rank_certificate_required",
            "witness_cochain_out_of_scope",
            "criterion_recorded",
            "cocycle_class_vanishing_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cochain_complex_rows.csv",
        (
            "complex_id",
            "R_id",
            "component_id",
            "coefficient_system_id",
            "C0_basis_id",
            "C1_basis_id",
            "C2_basis_id",
            "d0_matrix_id",
            "d1_matrix_id",
            "normalization_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "class_vanishing_rows.csv",
        (
            "vanishing_id",
            "R_id",
            "component_id",
            "cocycle_id",
            "d1_matrix_id",
            "cocycle_vector_id",
            "cocycle_defect_rank",
            "d1_rank",
            "augmented_rank",
            "class_rank",
            "vanishing_status",
            "witness_cochain_id",
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
            "vanishing_status",
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


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def count_data_rows(path: Path) -> int:
    return len(read_table_path(path, None, allow_empty=True))


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "orientation_cocycle_imported",
        "orientation_obstruction_imported",
        "rank_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "cocycle_value_rows_supplied",
        "cocycle_closedness_rows_supplied",
        "cochain_complex_rows_supplied",
        "coboundary_matrix_rows_supplied",
        "rank_certificate_rows_supplied",
        "cochain_witness_rows_supplied",
        "cocycle_class_vanishing_proved",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(ORIENTATION_COCYCLE_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    cocycle_manifest = read_json(ORIENTATION_COCYCLE_FIXTURE / "manifest.json")
    require_equal(cocycle_manifest.get("status"), ORIENTATION_COCYCLE_STATUS, "row-309 cocycle status")
    require_equal(cocycle_manifest.get("orientation_cocycle_defined"), False, "row-309 cocycle defined")
    require_equal(cocycle_manifest.get("cocycle_rows_supplied"), False, "row-309 cocycle rows")
    require_equal(cocycle_manifest.get("cocycle_defect_rows_supplied"), False, "row-309 defect rows")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_STATUS,
        "orientation obstruction status",
    )
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty")

    orientation_blocked = rows_by(
        read_table_path(ORIENTATION_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "orientation blocked obligations",
    )
    if not REQUIRED_ORIENTATION_OBLIGATIONS.issubset(orientation_blocked):
        missing = sorted(REQUIRED_ORIENTATION_OBLIGATIONS - set(orientation_blocked))
        raise ValueError(f"orientation ledger missing Coxeter obligations: {missing}")

    return {
        "row309_cocycle_value_rows": count_data_rows(
            ORIENTATION_COCYCLE_FIXTURE / "cocycle_value_rows.csv"
        ),
        "row309_normalization_rows": count_data_rows(
            ORIENTATION_COCYCLE_FIXTURE / "cocycle_normalization_rows.csv"
        ),
        "row309_cocycle_defect_rows": count_data_rows(
            ORIENTATION_COCYCLE_FIXTURE / "cocycle_defect_rows.csv"
        ),
        "coxeter_cocycle_rows": count_data_rows(ORIENTATION_FIXTURE / "coxeter_cocycles.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "orientation_cocycle": ORIENTATION_COCYCLE_STATUS,
        "orientation_obstruction": ORIENTATION_STATUS,
        "optimization_row": "row_310",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"orientation_cocycle_class_vanishing"}, "criterion ids")
    row = rows["orientation_cocycle_class_vanishing"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "cocycle_table_required",
        "coefficient_system_required",
        "normalized_complex_required",
        "d1_matrix_required",
        "cocycle_vector_required",
        "cocycle_closed_required",
        "rank_certificate_required",
        "witness_cochain_out_of_scope",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(
        bool_cell(row, "cocycle_class_vanishing_proved"),
        False,
        "cocycle class vanishing proved",
    )


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    for table_name in ("cochain_complex_rows.csv", "class_vanishing_rows.csv"):
        if tables[table_name]:
            raise ValueError(f"{table_name} must remain empty in obstruction packet")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["row309_cocycle_value_rows"] = counts["row309_cocycle_value_rows"]
    computed["row309_normalization_rows"] = counts["row309_normalization_rows"]
    computed["row309_cocycle_defect_rows"] = counts["row309_cocycle_defect_rows"]
    computed["coxeter_cocycle_rows"] = counts["coxeter_cocycle_rows"]
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(int_cell(row, "computed_value"), computed[coverage_id], f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(row["vanishing_status"], "missing_open_obligation", f"{row['obligation_id']} status")
        require_equal(row["check_status"], "verified", f"{row['obligation_id']} check")
        if not row["mathematical_payload"] or not row["why_required"]:
            raise ValueError(f"{row['obligation_id']}: missing payload or reason")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        check_verified(row, "scalar_firewall.csv")
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def verify_fixture(fixture: Path) -> None:
    if not fixture.is_dir():
        raise ValueError(f"fixture is not a directory: {fixture}")
    verify_manifest(fixture)
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_empty_tables(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(
            f"RHOMRED_WEYL_ORIENTATION_COCYCLE_CLASS_VANISHING_BLOCKED: {exc}",
            file=sys.stderr,
        )
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
