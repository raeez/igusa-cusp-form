#!/usr/bin/env python3
"""Verify the row-349 finite Hall coproduct coassociativity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_coproduct_coassociativity_two_step_flags_obstruction.v1"
EXPECTED_KIND = "finite_hall_coproduct_coassociativity_two_step_flags_obstruction"
SUCCESS_STATUS = "FINITE_HALL_COPRODUCT_COASSOCIATIVITY_TWO_STEP_FLAGS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-coproduct-coassociativity-two-step-flags"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_coproduct_coassociativity_two_step_flags")

COPRODUCT_OPERATOR_FIXTURE = Path("certificates/hall/finite_hall_coproduct_operator")
PUSHFORWARD_FIXTURE = Path("certificates/hall/finite_hall_coproduct_pushforward_functor")
FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
COMPACT_SUPPORT_FIXTURE = Path("certificates/hybrid/compact_support_exceptional_pushforward_model")
HYBRID_FLAG_FIXTURE = Path("certificates/hybrid/eight_word_two_step_flag_stacks")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")
TRANSITION_COPRODUCT_FIXTURE = Path("certificates/hall/transition_hall_coproduct_preservation")

COPRODUCT_OPERATOR_STATUS = "FINITE_HALL_COPRODUCT_OPERATOR_DEFINITION_VERIFIED"
PUSHFORWARD_STATUS = "FINITE_HALL_COPRODUCT_PUSHFORWARD_FUNCTOR_OBSTRUCTION_VERIFIED"
FINITE_MODULI_STATUS = "MODULI_OBSTRUCTION_LEDGER_VERIFIED"
COMPACT_SUPPORT_STATUS = "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED"
HYBRID_FLAG_STATUS = "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
TRANSITION_COPRODUCT_STATUS = "TRANSITION_HALL_COPRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "coassociativity_rows": 0,
    "row347_coproduct_operator_rows": 0,
    "row348_pushforward_rows": 0,
    "finite_moduli_extension_flag_rows": 0,
    "compact_support_base_change_rows": 0,
    "compact_support_projection_formula_rows": 0,
    "compact_support_thom_sebastiani_rows": 0,
    "compact_support_choice_independence_rows": 0,
    "hybrid_two_step_flag_rows": 8,
    "hybrid_comparison_map_rows": 16,
    "hybrid_flag_associativity_rows": 0,
    "compact_source_coproduct_matrix_rows": 0,
    "compact_source_bialgebra_rows": 0,
    "transition_coproduct_matrix_rows": 0,
    "transition_defect_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "populated_coproduct_rows",
    "compact_hall_two_step_splitting_flag_stack",
    "base_change_rows",
    "projection_formula_rows",
    "inverse_thom_sebastiani_rows",
    "compactification_independent_final_pushforward",
    "quotient_descent_rows",
    "transition_rows",
    "coproduct_matrix_rows",
    "hall_bialgebra_coassociativity_rows",
    "hybrid_to_compact_population",
}

REQUIRED_FIREWALL = {
    "coproduct_operator_notation",
    "p_bang_existence",
    "compactification_independence",
    "hybrid_wordwise_associativity",
    "two_step_flag_stacks_only",
    "four_input_pentagon",
    "coproduct_matrix",
    "product_associativity",
    "bar_coalgebra",
    "scalar_trace",
    "signed_multiplicity",
    "target_coproduct",
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
            "coproduct_legs_required",
            "two_step_splitting_flag_stack_required",
            "left_right_comparison_maps_required",
            "base_change_required",
            "projection_formula_required",
            "inverse_thom_sebastiani_required",
            "compactification_independence_required",
            "criterion_recorded",
            "actual_coassociativity_proved",
            "coproduct_matrix_claimed",
            "transition_claimed",
            "primitive_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coassociativity_rows.csv",
        (
            "coassociativity_row_id",
            "R_id",
            "left_degree_id",
            "middle_degree_id",
            "right_degree_id",
            "two_step_flag_stack_id",
            "left_composite_id",
            "right_composite_id",
            "comparison_isomorphism_id",
            "coassociativity_defect_rank",
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
        "coproduct_operator_packet_imported",
        "pushforward_packet_imported",
        "finite_moduli_packet_imported",
        "compact_support_model_imported",
        "hybrid_two_step_flag_packet_imported",
        "compact_hall_source_ledger_imported",
        "transition_hall_coproduct_ledger_imported",
        "two_step_flag_coassociativity_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "populated_coproduct_rows_supplied",
        "compact_hall_two_step_flag_rows_supplied",
        "base_change_projection_ts_rows_supplied",
        "p_bang_compactification_independence_rows_supplied",
        "quotient_descent_rows_supplied",
        "transition_rows_supplied",
        "coproduct_matrix_rows_supplied",
        "hall_bialgebra_coassociativity_rows_supplied",
        "actual_Delta_R_coassociativity_proved",
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
            str(COPRODUCT_OPERATOR_FIXTURE),
            str(PUSHFORWARD_FIXTURE),
            str(FINITE_MODULI_FIXTURE),
            str(COMPACT_SUPPORT_FIXTURE),
            str(HYBRID_FLAG_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
            str(TRANSITION_COPRODUCT_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "coproduct_legs_required",
        "two_step_splitting_flag_stack_required",
        "left_right_comparison_maps_required",
        "base_change_required",
        "projection_formula_required",
        "inverse_thom_sebastiani_required",
        "compactification_independence_required",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "actual_coassociativity_proved",
        "coproduct_matrix_claimed",
        "transition_claimed",
        "primitive_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-349 proposition")

    require_equal(len(tables["coassociativity_rows.csv"]), 0, "coassociativity row count")

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
    coproduct = read_json(COPRODUCT_OPERATOR_FIXTURE / "manifest.json")
    require_equal(coproduct.get("status"), COPRODUCT_OPERATOR_STATUS, "coproduct operator status")
    require_false(coproduct.get("coassociativity_rows_supplied"), "row347 coassociativity rows")
    require_false(coproduct.get("finite_hall_coproduct_populated"), "row347 populated coproduct")
    require_table_empty(COPRODUCT_OPERATOR_FIXTURE / "coproduct_operator_rows.csv")

    pushforward = read_json(PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pushforward.get("status"), PUSHFORWARD_STATUS, "pushforward status")
    require_false(pushforward.get("finite_hall_coproduct_populated"), "row348 populated coproduct")
    require_false(pushforward.get("coassociativity_claimed"), "row348 coassociativity")
    require_table_empty(PUSHFORWARD_FIXTURE / "pushforward_rows.csv")

    moduli = read_json(FINITE_MODULI_FIXTURE / "manifest.json")
    require_equal(moduli.get("obstruction_ledger_status"), FINITE_MODULI_STATUS, "moduli status")
    require_false(moduli.get("moduli_certification"), "moduli certification")
    require_false(moduli.get("mathematical_certification"), "moduli mathematical certification")
    require_table_empty(FINITE_MODULI_FIXTURE / "extension_flag_stacks.csv")

    compact_support = read_json(COMPACT_SUPPORT_FIXTURE / "manifest.json")
    require_equal(compact_support.get("status"), COMPACT_SUPPORT_STATUS, "compact support status")
    require_false(compact_support.get("base_change_certification"), "base change")
    require_false(compact_support.get("projection_formula_certification"), "projection formula")
    require_false(compact_support.get("thom_sebastiani_certification"), "Thom-Sebastiani")
    require_false(compact_support.get("choice_independence_certification"), "choice independence")
    for table_name in (
        "base_change_rows.csv",
        "projection_formula_rows.csv",
        "thom_sebastiani_rows.csv",
        "choice_independence_rows.csv",
        "transition_rows.csv",
        "aggregate_population_rows.csv",
    ):
        require_table_empty(COMPACT_SUPPORT_FIXTURE / table_name)

    flag = read_json(HYBRID_FLAG_FIXTURE / "manifest.json")
    require_equal(flag.get("status"), HYBRID_FLAG_STATUS, "hybrid flag status")
    require_equal(flag.get("word_count"), 8, "hybrid flag word count")
    require_equal(flag.get("comparison_map_count"), 16, "hybrid comparison map count")
    require_false(flag.get("associativity_certification"), "hybrid flag associativity")
    require_false(flag.get("quotient_descent_certification"), "hybrid flag quotient descent")
    require_false(flag.get("transition_certification"), "hybrid flag transition")
    require_false(flag.get("aggregate_hybrid_population"), "hybrid flag aggregate population")
    require_equal(len(read_table_path(HYBRID_FLAG_FIXTURE / "flag_stack_rows.csv")), 8, "flag rows")
    require_equal(
        len(read_table_path(HYBRID_FLAG_FIXTURE / "comparison_map_rows.csv")),
        16,
        "comparison rows",
    )
    for table_name in (
        "associativity_rows.csv",
        "quotient_descent_rows.csv",
        "transition_rows.csv",
        "aggregate_population_rows.csv",
    ):
        require_table_empty(HYBRID_FLAG_FIXTURE / table_name)

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
    require_table_empty(COMPACT_SOURCE_FIXTURE / "D_entries.csv")
    require_table_empty(COMPACT_SOURCE_FIXTURE / "hall_bialgebra_identities.csv")

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
    require_false(
        transition.get("mathematical_certification"),
        "transition coproduct mathematical certification",
    )
    require_table_empty(TRANSITION_COPRODUCT_FIXTURE / "coproduct_matrix_transport.csv")
    require_table_empty(TRANSITION_COPRODUCT_FIXTURE / "transition_defects.csv")


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
