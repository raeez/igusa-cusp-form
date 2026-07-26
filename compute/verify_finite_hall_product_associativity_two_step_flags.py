#!/usr/bin/env python3
"""Verify the row-346 finite Hall product associativity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_product_associativity_two_step_flags_obstruction.v1"
EXPECTED_KIND = "finite_hall_product_associativity_two_step_flags_obstruction"
SUCCESS_STATUS = "FINITE_HALL_PRODUCT_ASSOCIATIVITY_TWO_STEP_FLAGS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-product-associativity-two-step-flags"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_product_associativity_two_step_flags")

PRODUCT_OPERATOR_FIXTURE = Path("certificates/hall/finite_hall_product_operator")
PUSHFORWARD_FIXTURE = Path("certificates/hall/finite_hall_product_pushforward_functor")
INDEPENDENCE_FIXTURE = Path("certificates/hall/finite_hall_product_compactification_independence")
FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
COMPACT_SUPPORT_FIXTURE = Path("certificates/hybrid/compact_support_exceptional_pushforward_model")
HYBRID_FLAG_FIXTURE = Path("certificates/hybrid/eight_word_two_step_flag_stacks")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

WORD_FIXTURES = {
    "LLL": (Path("certificates/hybrid/lll_associativity"), "LLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "LLW": (Path("certificates/hybrid/llw_associativity"), "LLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "LWL": (Path("certificates/hybrid/lwl_associativity"), "LWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "WLL": (Path("certificates/hybrid/wll_associativity"), "WLL_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "LWW": (Path("certificates/hybrid/lww_associativity"), "LWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "WLW": (Path("certificates/hybrid/wlw_associativity"), "WLW_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "WWL": (Path("certificates/hybrid/wwl_associativity"), "WWL_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
    "WWW": (Path("certificates/hybrid/www_associativity"), "WWW_ASSOCIATIVITY_CONDITIONAL_VERIFIED"),
}

PRODUCT_OPERATOR_STATUS = "FINITE_HALL_PRODUCT_OPERATOR_DEFINITION_VERIFIED"
PUSHFORWARD_STATUS = "FINITE_HALL_PRODUCT_PUSHFORWARD_FUNCTOR_OBSTRUCTION_VERIFIED"
INDEPENDENCE_STATUS = "FINITE_HALL_PRODUCT_COMPACTIFICATION_INDEPENDENCE_OBSTRUCTION_VERIFIED"
FINITE_MODULI_STATUS = "MODULI_OBSTRUCTION_LEDGER_VERIFIED"
COMPACT_SUPPORT_STATUS = "COMPACT_SUPPORT_EXCEPTIONAL_PUSHFORWARD_MODEL_DEFINED"
HYBRID_FLAG_STATUS = "EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "associativity_rows": 0,
    "row342_product_operator_rows": 0,
    "row344_pushforward_rows": 0,
    "row345_independence_rows": 0,
    "finite_moduli_extension_flag_rows": 0,
    "compact_support_base_change_rows": 0,
    "compact_support_projection_formula_rows": 0,
    "compact_support_thom_sebastiani_rows": 0,
    "hybrid_two_step_flag_rows": 8,
    "hybrid_comparison_map_rows": 16,
    "hybrid_flag_associativity_rows": 0,
    "wordwise_associativity_packets": 8,
    "compact_source_product_matrix_rows": 0,
    "compact_source_bialgebra_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "populated_product_rows",
    "compact_hall_two_step_flag_stack",
    "base_change_rows",
    "projection_formula_rows",
    "reduced_thom_sebastiani_rows",
    "compactification_independent_final_pushforward",
    "quotient_descent_rows",
    "transition_rows",
    "product_matrix_rows",
    "hall_bialgebra_associativity_rows",
    "hybrid_to_compact_population",
}

REQUIRED_FIREWALL = {
    "product_operator_notation",
    "q_bang_existence",
    "compactification_independence",
    "hybrid_wordwise_associativity",
    "two_step_flag_stacks_only",
    "four_input_pentagon",
    "product_matrix",
    "scalar_trace",
    "signed_multiplicity",
    "target_product",
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
            "product_legs_required",
            "two_step_flag_stack_required",
            "left_right_comparison_maps_required",
            "base_change_required",
            "projection_formula_required",
            "thom_sebastiani_required",
            "compactification_independence_required",
            "criterion_recorded",
            "actual_associativity_proved",
            "product_matrix_claimed",
            "transition_claimed",
            "primitive_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "associativity_rows.csv",
        (
            "associativity_row_id",
            "R_id",
            "left_degree_id",
            "middle_degree_id",
            "right_degree_id",
            "two_step_flag_stack_id",
            "left_composite_id",
            "right_composite_id",
            "comparison_isomorphism_id",
            "associativity_defect_rank",
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
        "pushforward_packet_imported",
        "compactification_independence_packet_imported",
        "finite_moduli_packet_imported",
        "compact_support_model_imported",
        "hybrid_two_step_flag_packet_imported",
        "wordwise_associativity_packets_imported",
        "compact_hall_source_ledger_imported",
        "two_step_flag_associativity_criterion_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "populated_product_rows_supplied",
        "compact_hall_two_step_flag_rows_supplied",
        "base_change_projection_ts_rows_supplied",
        "quotient_descent_rows_supplied",
        "transition_rows_supplied",
        "product_matrix_rows_supplied",
        "hall_bialgebra_associativity_rows_supplied",
        "actual_m_R_associativity_proved",
        "finite_hall_product_populated",
        "primitive_claimed",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(
        set(manifest.get("tables", [])),
        {spec.path for spec in TABLE_SPECS},
        "manifest tables",
    )
    expected_imports = {
        str(PRODUCT_OPERATOR_FIXTURE),
        str(PUSHFORWARD_FIXTURE),
        str(INDEPENDENCE_FIXTURE),
        str(FINITE_MODULI_FIXTURE),
        str(COMPACT_SUPPORT_FIXTURE),
        str(HYBRID_FLAG_FIXTURE),
        str(COMPACT_SOURCE_FIXTURE),
    } | {str(path) for path, _status in WORD_FIXTURES.values()}
    require_equal(set(manifest.get("imports", [])), expected_imports, "manifest imports")


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "product_legs_required",
        "two_step_flag_stack_required",
        "left_right_comparison_maps_required",
        "base_change_required",
        "projection_formula_required",
        "thom_sebastiani_required",
        "compactification_independence_required",
        "criterion_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "actual_associativity_proved",
        "product_matrix_claimed",
        "transition_claimed",
        "primitive_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-346 proposition")

    require_equal(len(tables["associativity_rows.csv"]), 0, "associativity row count")

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
    require_false(product.get("associativity_rows_supplied"), "row342 associativity rows")
    require_false(product.get("finite_hall_product_populated"), "row342 populated product")
    require_table_empty(PRODUCT_OPERATOR_FIXTURE / "product_operator_rows.csv")

    pushforward = read_json(PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pushforward.get("status"), PUSHFORWARD_STATUS, "pushforward status")
    require_false(pushforward.get("finite_hall_product_populated"), "row344 populated product")
    require_table_empty(PUSHFORWARD_FIXTURE / "pushforward_rows.csv")

    independence = read_json(INDEPENDENCE_FIXTURE / "manifest.json")
    require_equal(independence.get("status"), INDEPENDENCE_STATUS, "independence status")
    require_false(
        independence.get("actual_q_bang_independence_proved"),
        "row345 actual q bang independence",
    )
    require_table_empty(INDEPENDENCE_FIXTURE / "independence_rows.csv")

    moduli = read_json(FINITE_MODULI_FIXTURE / "manifest.json")
    require_equal(moduli.get("obstruction_ledger_status"), FINITE_MODULI_STATUS, "moduli status")
    require_false(moduli.get("moduli_certification"), "moduli certification")
    require_table_empty(FINITE_MODULI_FIXTURE / "extension_flag_stacks.csv")

    compact_support = read_json(COMPACT_SUPPORT_FIXTURE / "manifest.json")
    require_equal(compact_support.get("status"), COMPACT_SUPPORT_STATUS, "compact support status")
    require_false(compact_support.get("base_change_certification"), "base change")
    require_false(compact_support.get("projection_formula_certification"), "projection formula")
    require_false(compact_support.get("thom_sebastiani_certification"), "Thom-Sebastiani")
    for table_name in (
        "base_change_rows.csv",
        "projection_formula_rows.csv",
        "thom_sebastiani_rows.csv",
        "transition_rows.csv",
        "aggregate_population_rows.csv",
    ):
        require_table_empty(COMPACT_SUPPORT_FIXTURE / table_name)

    flag = read_json(HYBRID_FLAG_FIXTURE / "manifest.json")
    require_equal(flag.get("status"), HYBRID_FLAG_STATUS, "hybrid flag status")
    require_equal(flag.get("word_count"), 8, "hybrid flag word count")
    require_equal(flag.get("comparison_map_count"), 16, "hybrid comparison map count")
    require_false(flag.get("associativity_certification"), "hybrid flag associativity")
    require_false(flag.get("aggregate_hybrid_population"), "hybrid flag aggregate population")
    require_equal(len(read_table_path(HYBRID_FLAG_FIXTURE / "flag_stack_rows.csv")), 8, "flag rows")
    require_equal(
        len(read_table_path(HYBRID_FLAG_FIXTURE / "comparison_map_rows.csv")),
        16,
        "comparison rows",
    )
    require_table_empty(HYBRID_FLAG_FIXTURE / "associativity_rows.csv")

    for word, (path, status) in WORD_FIXTURES.items():
        manifest = read_json(path / "manifest.json")
        require_equal(manifest.get("status"), status, f"{word} status")
        require_true(manifest.get("associativity_proved"), f"{word} associativity")
        conditional = manifest.get("conditional_on_functorial_rows")
        if word == "LLL":
            conditional = manifest.get("conditional_on_local_functorial_rows")
        require_true(conditional, f"{word} functorial conditional")
        require_equal(manifest.get("associativity_defect_rank"), 0, f"{word} defect")
        require_false(manifest.get("quotient_descent_certification"), f"{word} quotient")
        require_false(manifest.get("transition_certification"), f"{word} transition")
        require_false(manifest.get("aggregate_hybrid_population"), f"{word} aggregate")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(
        compact_source.get("obstruction_ledger_status"),
        COMPACT_SOURCE_STATUS,
        "compact source status",
    )
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_table_empty(COMPACT_SOURCE_FIXTURE / "M_entries.csv")
    require_table_empty(COMPACT_SOURCE_FIXTURE / "hall_bialgebra_identities.csv")


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
