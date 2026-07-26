#!/usr/bin/env python3
"""Verify the row-347 finite Hall coproduct operator definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_coproduct_operator_definition.v1"
EXPECTED_KIND = "finite_hall_coproduct_operator_definition"
SUCCESS_STATUS = "FINITE_HALL_COPRODUCT_OPERATOR_DEFINITION_VERIFIED"
PROOF_LABEL = "def:compact-hall-coproduct"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_coproduct_operator")

FINITE_OBJECT_FIXTURE = Path("certificates/hall/finite_geometric_hall_object")
COMPACT_SUPPORT_FIXTURE = Path("certificates/hybrid/compact_support_exceptional_pushforward_model")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
TRANSITION_COPRODUCT_FIXTURE = Path("certificates/hall/transition_hall_coproduct_preservation")

FINITE_OBJECT_STATUS = "FINITE_GEOMETRIC_HALL_OBJECT_DEFINITION_VERIFIED"
COMPACT_SUPPORT_STATUS = "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
TRANSITION_COPRODUCT_STATUS = "TRANSITION_HALL_COPRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "definition_count": 1,
    "coproduct_operator_rows": 0,
    "finite_hall_object_components": 0,
    "compact_support_operation_rows": 2,
    "compact_support_map_population_rows": 0,
    "compactification_independence_rows": 0,
    "base_change_rows": 0,
    "projection_formula_rows": 0,
    "thom_sebastiani_rows": 0,
    "source_coproduct_matrix_rows": 0,
    "source_counit_rows": 0,
    "transition_coproduct_matrix_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "retained_splitting_correspondence",
    "pullback_functor_exists",
    "inverse_thom_sebastiani_transport",
    "exceptional_pushforward_p_exists",
    "compactification_independence",
    "coproduct_matrix_rows",
    "counit_rows",
    "coassociativity_rows",
    "bialgebra_compatibility_rows",
    "transition_coproduct_rows",
    "primitive_closure_rows",
}

REQUIRED_FIREWALL = {
    "finite_Hall_object_only",
    "compact_support_notation_only",
    "product_operator",
    "coproduct_matrix",
    "coassociativity",
    "transition_preservation",
    "counit",
    "primitive_subspace",
    "bar_coalgebra",
    "scalar_trace",
    "signed_multiplicity",
    "target_coproduct",
    "pfaffian_coproduct",
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
        "definition_rows.csv",
        (
            "definition_id",
            "finite_hall_object_required",
            "splitting_correspondence_required",
            "pullback_functor_required",
            "inverse_thom_sebastiani_required",
            "exceptional_pushforward_required",
            "compact_support_model_required",
            "formula_recorded",
            "pullback_existence_proved",
            "pushforward_existence_proved",
            "compactification_independence_proved",
            "coproduct_populated",
            "coassociativity_claimed",
            "transition_claimed",
            "primitive_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coproduct_operator_rows.csv",
        (
            "operator_id",
            "source_degree_id",
            "left_output_degree_id",
            "right_output_degree_id",
            "source_basis_id",
            "left_output_basis_id",
            "right_output_basis_id",
            "splitting_correspondence_id",
            "pullback_row_id",
            "inverse_ts_row_id",
            "pushforward_row_id",
            "coproduct_matrix_row_id",
            "operator_verified",
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
        "definition_recorded",
        "finite_hall_object_imported",
        "compact_support_model_imported",
        "compact_hall_source_ledger_imported",
        "transition_hall_coproduct_ledger_imported",
        "formal_coproduct_formula_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "pullback_exists_proved",
        "pushforward_exists_proved",
        "compactification_independence_proved",
        "retained_splitting_correspondence_rows_supplied",
        "inverse_thom_sebastiani_rows_supplied",
        "coproduct_matrix_rows_supplied",
        "counit_rows_supplied",
        "coassociativity_rows_supplied",
        "bialgebra_compatibility_rows_supplied",
        "transition_compatibility_rows_supplied",
        "finite_hall_coproduct_populated",
        "primitive_claimed",
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
            str(FINITE_OBJECT_FIXTURE),
            str(COMPACT_SUPPORT_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(TRANSITION_COPRODUCT_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    definition = tables["definition_rows.csv"]
    require_equal(len(definition), 1, "definition row count")
    row = definition[0]
    for key in (
        "finite_hall_object_required",
        "splitting_correspondence_required",
        "pullback_functor_required",
        "inverse_thom_sebastiani_required",
        "exceptional_pushforward_required",
        "compact_support_model_required",
        "formula_recorded",
    ):
        require_equal(row.get(key), "true", f"definition {key}")
    for key in (
        "pullback_existence_proved",
        "pushforward_existence_proved",
        "compactification_independence_proved",
        "coproduct_populated",
        "coassociativity_claimed",
        "transition_claimed",
        "primitive_claimed",
    ):
        require_equal(row.get(key), "false", f"definition {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("definition proof reference does not point to compact Hall coproduct")

    require_equal(len(tables["coproduct_operator_rows.csv"]), 0, "coproduct rows count")

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
            raise ValueError(f"{obligation_id}: proof reference does not point to definition")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, frow in firewall.items():
        require_equal(frow.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(frow, "defect_rank"), 0, f"{substitute} defect")
        require_equal(frow.get("check_status"), "verified", f"{substitute} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{substitute}: proof reference does not point to definition")


def check_imports() -> None:
    finite_object = read_json(FINITE_OBJECT_FIXTURE / "manifest.json")
    require_equal(finite_object.get("status"), FINITE_OBJECT_STATUS, "finite object status")
    require_false(finite_object.get("finite_hall_object_populated"), "finite object populated")
    require_false(finite_object.get("coproduct_claimed"), "finite object coproduct claimed")
    require_table_empty(FINITE_OBJECT_FIXTURE / "object_components.csv")

    compact_support = read_json(COMPACT_SUPPORT_FIXTURE / "manifest.json")
    require_equal(compact_support.get("status"), COMPACT_SUPPORT_STATUS, "compact support status")
    require_true(
        compact_support.get("compact_support_model_defined"),
        "compact support model defined",
    )
    require_true(
        compact_support.get("proper_pushforward_formula_defined"),
        "proper pushforward formula defined",
    )
    require_false(compact_support.get("choice_independence_certification"), "choice independence")
    require_false(compact_support.get("map_population_certification"), "map population")
    require_false(compact_support.get("base_change_certification"), "base change")
    require_false(compact_support.get("projection_formula_certification"), "projection formula")
    require_false(compact_support.get("thom_sebastiani_certification"), "Thom-Sebastiani")
    require_false(compact_support.get("hall_product_certification"), "Hall product certification")
    operation_rows = read_table_path(COMPACT_SUPPORT_FIXTURE / "operation_rows.csv")
    require_equal(len(operation_rows), 2, "compact-support operation rows")
    for rel_path in (
        "map_population_rows.csv",
        "choice_independence_rows.csv",
        "base_change_rows.csv",
        "projection_formula_rows.csv",
        "thom_sebastiani_rows.csv",
        "transition_rows.csv",
        "aggregate_population_rows.csv",
    ):
        require_table_empty(COMPACT_SUPPORT_FIXTURE / rel_path)

    compact_hall = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(
        compact_hall.get("obstruction_ledger_status"),
        COMPACT_HALL_STATUS,
        "compact Hall status",
    )
    require_equal(compact_hall.get("source_kind"), "mock_empty_blocked", "compact source kind")
    require_true(compact_hall.get("empty_blocked"), "compact source empty blocked")
    require_false(compact_hall.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_hall.get("mathematical_certification"), "compact math certification")
    for rel_path in ("D_entries.csv", "unit_counit.csv", "hall_bialgebra_identities.csv"):
        require_table_empty(COMPACT_HALL_FIXTURE / rel_path)

    transition = read_json(TRANSITION_COPRODUCT_FIXTURE / "manifest.json")
    require_equal(
        transition.get("status"),
        TRANSITION_COPRODUCT_STATUS,
        "transition coproduct status",
    )
    require_false(
        transition.get("hall_coproduct_transition_certification"),
        "Hall coproduct transition certification",
    )
    require_false(transition.get("mathematical_certification"), "transition math certification")
    for rel_path in (
        "splitting_correspondence_transitions.csv",
        "coefficient_transport.csv",
        "coproduct_matrix_transport.csv",
        "base_change_projection.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANSITION_COPRODUCT_FIXTURE / rel_path)


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
