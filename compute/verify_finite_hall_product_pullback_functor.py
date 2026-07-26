#!/usr/bin/env python3
"""Verify the row-343 finite Hall product pullback-functor packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_product_pullback_functor_obstruction.v1"
EXPECTED_KIND = "finite_hall_product_pullback_functor_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PRODUCT_PULLBACK_FUNCTOR_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-product-pullback-existence"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_product_pullback_functor")

PRODUCT_OPERATOR_FIXTURE = Path("certificates/hall/finite_hall_product_operator")
FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FINITE_OBJECT_FIXTURE = Path("certificates/hall/finite_geometric_hall_object")
COMPACT_SUPPORT_FIXTURE = Path("certificates/hybrid/compact_support_exceptional_pushforward_model")

PRODUCT_OPERATOR_STATUS = "FINITE_HALL_PRODUCT_OPERATOR_DEFINITION_VERIFIED"
FINITE_MODULI_STATUS = "MODULI_OBSTRUCTION_LEDGER_VERIFIED"
FINITE_OBJECT_STATUS = "FINITE_GEOMETRIC_HALL_OBJECT_DEFINITION_VERIFIED"
COMPACT_SUPPORT_STATUS = "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "pullback_rows": 0,
    "row342_product_operator_rows": 0,
    "finite_moduli_extension_flag_rows": 0,
    "finite_moduli_cosection_atlas_rows": 0,
    "finite_hall_object_components": 0,
    "compact_support_map_population_rows": 0,
    "compact_support_operation_rows": 2,
}

REQUIRED_OBLIGATIONS = {
    "retained_extension_stack",
    "p_map_row",
    "p_map_finite_type",
    "input_coefficient_constructible",
    "pullback_row",
    "external_product_basis",
    "row342_notation_not_pstar",
    "q_bang_separate",
}

REQUIRED_FIREWALL = {
    "product_operator_notation",
    "finite_Hall_object_only",
    "extension_closure_only",
    "compact_support_pushforward_model",
    "q_bang",
    "thom_sebastiani",
    "product_matrix",
    "scalar_trace",
    "signed_multiplicity",
    "target_root_window",
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
            "retained_extension_correspondence_required",
            "p_map_finite_type_required",
            "chosen_six_functor_formalism_required",
            "input_coefficient_constructible_required",
            "pullback_functor_required",
            "criterion_recorded",
            "actual_p_star_leg_proved",
            "q_bang_claimed",
            "thom_sebastiani_claimed",
            "product_matrix_claimed",
            "associativity_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pullback_rows.csv",
        (
            "pullback_row_id",
            "R_id",
            "source_degree_id",
            "left_input_degree_id",
            "right_input_degree_id",
            "p_map_id",
            "input_coefficient_id",
            "pullback_coefficient_id",
            "p_finite_type",
            "pullback_exists",
            "constructibility_preserved",
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
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")

    for key in (
        "criterion_recorded",
        "product_operator_packet_imported",
        "finite_moduli_packet_imported",
        "finite_hall_object_packet_imported",
        "compact_support_model_imported",
        "six_functor_pullback_formalism_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "retained_extension_correspondence_rows_supplied",
        "p_map_finite_type_rows_supplied",
        "input_coefficient_constructibility_rows_supplied",
        "pullback_functor_rows_supplied",
        "actual_p_star_leg_proved",
        "finite_hall_product_populated",
        "q_bang_claimed",
        "thom_sebastiani_claimed",
        "product_matrix_claimed",
        "associativity_claimed",
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
            str(PRODUCT_OPERATOR_FIXTURE),
            str(FINITE_MODULI_FIXTURE),
            str(FINITE_OBJECT_FIXTURE),
            str(COMPACT_SUPPORT_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "retained_extension_correspondence_required",
        "p_map_finite_type_required",
        "chosen_six_functor_formalism_required",
        "input_coefficient_constructible_required",
        "pullback_functor_required",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "actual_p_star_leg_proved",
        "q_bang_claimed",
        "thom_sebastiani_claimed",
        "product_matrix_claimed",
        "associativity_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-343 proposition")

    require_equal(len(tables["pullback_rows.csv"]), 0, "pullback row count")

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
    product = read_json(PRODUCT_OPERATOR_FIXTURE / "manifest.json")
    require_equal(product.get("status"), PRODUCT_OPERATOR_STATUS, "product operator status")
    require_false(product.get("pullback_exists_proved"), "row342 pullback proof")
    require_false(product.get("finite_hall_product_populated"), "row342 populated product")
    require_table_empty(PRODUCT_OPERATOR_FIXTURE / "product_operator_rows.csv")

    moduli = read_json(FINITE_MODULI_FIXTURE / "manifest.json")
    require_equal(moduli.get("obstruction_ledger_status"), FINITE_MODULI_STATUS, "moduli status")
    require_true(moduli.get("extension_closure"), "extension closure")
    require_false(moduli.get("moduli_certification"), "moduli certification")
    require_false(moduli.get("mathematical_certification"), "moduli mathematical certification")
    require_table_empty(FINITE_MODULI_FIXTURE / "extension_flag_stacks.csv")
    require_table_empty(FINITE_MODULI_FIXTURE / "cosection_atlas.csv")

    finite_object = read_json(FINITE_OBJECT_FIXTURE / "manifest.json")
    require_equal(finite_object.get("status"), FINITE_OBJECT_STATUS, "finite object status")
    require_false(finite_object.get("finite_hall_object_populated"), "finite object populated")
    require_false(finite_object.get("product_claimed"), "finite object product claimed")
    require_table_empty(FINITE_OBJECT_FIXTURE / "object_components.csv")

    compact_support = read_json(COMPACT_SUPPORT_FIXTURE / "manifest.json")
    require_equal(compact_support.get("status"), COMPACT_SUPPORT_STATUS, "compact support status")
    require_true(compact_support.get("compact_support_model_defined"), "compact support model")
    require_true(
        compact_support.get("coefficient_constructibility_required"),
        "coefficient constructibility required",
    )
    require_false(compact_support.get("map_population_certification"), "map population")
    require_false(compact_support.get("hall_product_certification"), "Hall product certification")
    require_equal(
        len(read_table_path(COMPACT_SUPPORT_FIXTURE / "operation_rows.csv")),
        2,
        "compact support operation rows",
    )
    require_table_empty(COMPACT_SUPPORT_FIXTURE / "map_population_rows.csv")


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
