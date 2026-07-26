#!/usr/bin/env python3
"""Verify row-329 three-simple-wall chart-orientation packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_three_simple_wall_chart_orientation_obstruction.v1"
EXPECTED_KIND = "rhomred_three_simple_wall_chart_orientation_obstruction"
SUCCESS_STATUS = "RHOMRED_THREE_SIMPLE_WALL_CHART_ORIENTATION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:three-simple-wall-chart-orientation"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_three_simple_wall_chart_orientation")

SIMPLE_SIGN_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_simple_sign_computation")
O2_FIXTURE = Path("certificates/wall_atlas/k3e_o2_atlas")
PFIN_FIXTURE = Path("certificates/pfaffian/k3e_finite_pfaffian")
MAASS_IRRELEVANCE_FIXTURE = Path(
    "certificates/orientation/rhomred_local_divisor_monodromy_maass_irrelevance"
)

SIMPLE_SIGN_STATUS = "RHOMRED_WEYL_ORIENTATION_SIMPLE_SIGN_COMPUTATION_OBSTRUCTION_VERIFIED"
O2_STATUS = "O2_OBSTRUCTION_LEDGER_VERIFIED"
PFIN_STATUS = "PFAFFIAN_OBSTRUCTION_LEDGER_VERIFIED"
MAASS_IRRELEVANCE_STATUS = "RHOMRED_LOCAL_DIVISOR_MONODROMY_MAASS_IRRELEVANCE_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "required_simple_walls": 3,
    "chart_orientation_rows": 0,
    "o2_wall_object_rows": 0,
    "o2_wall_chart_rows": 0,
    "pfin_wall_chart_rows": 0,
    "local_sign_rows": 0,
    "unconditional_orientation_vector_claim": 0,
    "global_orientation_character_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "three_wall_objects",
    "rank_one_wall_charts",
    "normal_coordinate_flip",
    "invariant_tangent_unit",
    "quotient_orientation",
    "divisor_order",
    "local_sign_rows",
    "transition_compatibility",
    "global_orientation_character",
}

REQUIRED_FIREWALL = {
    "maass_character_value",
    "local_divisor_monodromy",
    "O2_obstruction_ledger_only",
    "finite_pfaffian_ledger_only",
    "row320_formula_only",
    "OP_scalar_branch",
    "squared_determinant",
    "scalar_trace",
    "empty_chart_table",
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
            "three_simple_walls_required",
            "wall_object_required",
            "rank_one_chart_required",
            "normal_coordinate_required",
            "reflection_flip_required",
            "invariant_unit_required",
            "quotient_orientation_required",
            "divisor_order_required",
            "local_sign_required",
            "transition_compatibility_required",
            "maass_as_chart_data_allowed",
            "criterion_recorded",
            "three_chart_orientation_computed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "chart_orientation_rows.csv",
        (
            "orientation_row_id",
            "R_id",
            "stratum_id",
            "delta_id",
            "wall_object_id",
            "wall_chart_id",
            "normal_coordinate_id",
            "tangent_pfaffian_unit_id",
            "quotient_orientation_id",
            "normal_rank",
            "divisor_order",
            "reflection_flips_coordinate",
            "unit_invariant",
            "local_pfaffian_sign",
            "chart_orientation_sign",
            "transition_row_id",
            "orientation_computation_verified",
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
            "chart_orientation_status",
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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "simple_sign_criterion_imported",
        "o2_wall_atlas_imported",
        "finite_pfaffian_imported",
        "maass_irrelevance_imported",
        "chart_orientation_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "three_chart_rows_supplied",
        "wall_object_rows_supplied",
        "rank_one_chart_rows_supplied",
        "invariant_unit_rows_supplied",
        "quotient_orientation_rows_supplied",
        "local_sign_rows_supplied",
        "transition_rows_supplied",
        "three_simple_wall_orientation_computed",
        "orientation_vector_claimed_unconditionally",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(SIMPLE_SIGN_FIXTURE),
            str(O2_FIXTURE),
            str(PFIN_FIXTURE),
            str(MAASS_IRRELEVANCE_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> None:
    simple_sign = read_json(SIMPLE_SIGN_FIXTURE / "manifest.json")
    require_equal(simple_sign.get("status"), SIMPLE_SIGN_STATUS, "simple-sign status")
    require_equal(simple_sign.get("simple_sign_computation_proved"), False, "simple sign proved")

    o2 = read_json(O2_FIXTURE / "manifest.json")
    require_equal(o2.get("obstruction_ledger_status"), O2_STATUS, "O2 status")
    require_equal(o2.get("empty_blocked"), True, "O2 empty blocked")
    require_equal(o2.get("o2_certification"), False, "O2 certification")

    pfin = read_json(PFIN_FIXTURE / "manifest.json")
    require_equal(pfin.get("obstruction_ledger_status"), PFIN_STATUS, "Pfaffian status")
    require_equal(pfin.get("pfaffian_certification"), False, "Pfaffian certification")

    maass_irrelevance = read_json(MAASS_IRRELEVANCE_FIXTURE / "manifest.json")
    require_equal(
        maass_irrelevance.get("status"),
        MAASS_IRRELEVANCE_STATUS,
        "Maass irrelevance status",
    )
    require_equal(
        maass_irrelevance.get("row329_simple_wall_orientation_computed"),
        False,
        "row329 computed flag",
    )


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "simple_sign_criterion",
            "o2_wall_atlas",
            "finite_pfaffian",
            "maass_irrelevance",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "three_simple_wall_chart_orientation", "criterion id")
    for key in (
        "three_simple_walls_required",
        "wall_object_required",
        "rank_one_chart_required",
        "normal_coordinate_required",
        "reflection_flip_required",
        "invariant_unit_required",
        "quotient_orientation_required",
        "divisor_order_required",
        "local_sign_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in ("maass_as_chart_data_allowed", "three_chart_orientation_computed"):
        require_equal(bool_cell(row, key), False, key)
    check_verified(row, "criterion_rows.csv")


def verify_empty_chart_rows(rows: list[dict[str, str]]) -> None:
    require_equal(rows, [], "chart orientation rows")


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
        require_equal(row["chart_orientation_status"], "missing_open_obligation", "obligation status")
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
    verify_empty_chart_rows(tables["chart_orientation_rows.csv"])
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
