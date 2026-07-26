#!/usr/bin/env python3
"""Verify row-330 isotropic a_ij chart-orientation packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_isotropic_aij_chart_orientation_obstruction.v1"
EXPECTED_KIND = "rhomred_isotropic_aij_chart_orientation_obstruction"
SUCCESS_STATUS = "RHOMRED_ISOTROPIC_AIJ_CHART_ORIENTATION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:isotropic-aij-chart-orientation"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_isotropic_aij_chart_orientation")

CHAMBER_FIXTURE = Path("certificates/lattice/type_ii_chamber_isotropic")
WLE3_FIXTURE = Path("certificates/targets/delta5_gn_kac/wle3_target_parity")
SIMPLE_WALL_FIXTURE = Path("certificates/orientation/rhomred_three_simple_wall_chart_orientation")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")

CHAMBER_STATUS = "type_ii_chamber_isotropic.v1"
WLE3_STATUS = "wle3_target_parity.v1"
SIMPLE_WALL_STATUS = "RHOMRED_THREE_SIMPLE_WALL_CHART_ORIENTATION_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "target_isotropic_ray_count": 3,
    "target_aij_even_rank": 10,
    "target_aij_odd_rank": 0,
    "expected_chart_sign": 1,
    "source_isotropic_chart_rows": 0,
    "source_parity_rows": 0,
    "unconditional_orientation_vector_claim": 0,
    "row331_delta123_claim": 0,
    "row332_parity_compatibility_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_isotropic_charts",
    "source_parity_rows",
    "affine_null_direction",
    "gn_isotropic_directions",
    "quotient_orientation",
    "determinant_square",
    "transition_compatibility",
    "row331_delta123_chart",
    "row332_parity_split_compatibility",
}

REQUIRED_FIREWALL = {
    "target_parity_10_0",
    "type_ii_chamber_isotropic_target_data",
    "Borcherds_multiplicity_10",
    "GN_tau_9",
    "simple_wall_orientation_vector",
    "maass_character_value",
    "OP_scalar_branch",
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
            "isotropic_rays_required",
            "target_parity_required",
            "source_chart_required",
            "source_parity_required",
            "quotient_orientation_required",
            "determinant_square_required",
            "transition_compatibility_required",
            "target_parity_as_source_allowed",
            "criterion_recorded",
            "isotropic_orientation_computed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "isotropic_chart_rows.csv",
        (
            "orientation_row_id",
            "R_id",
            "stratum_id",
            "ray_id",
            "source_chart_id",
            "source_parity_row_id",
            "even_rank",
            "odd_rank",
            "affine_null_direction_id",
            "gn_isotropic_direction_ids",
            "quotient_orientation_id",
            "determinant_square_id",
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
        "type_ii_chamber_isotropic_imported",
        "wle3_target_parity_imported",
        "simple_wall_chart_orientation_imported",
        "compact_hall_ledger_imported",
        "isotropic_chart_orientation_criterion_recorded",
        "target_aij_parity_certified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_isotropic_chart_rows_supplied",
        "source_parity_rows_supplied",
        "quotient_orientation_rows_supplied",
        "determinant_square_rows_supplied",
        "transition_rows_supplied",
        "isotropic_aij_orientation_computed",
        "orientation_vector_claimed_unconditionally",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(CHAMBER_FIXTURE), str(WLE3_FIXTURE), str(SIMPLE_WALL_FIXTURE), str(COMPACT_HALL_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> None:
    chamber = read_json(CHAMBER_FIXTURE / "manifest.json")
    require_equal(chamber.get("schema_version"), CHAMBER_STATUS, "chamber schema")
    require_equal(chamber.get("chamber_isotropic_certified"), True, "chamber certified")
    require_equal(chamber.get("pfaffian_orientation"), False, "chamber orientation flag")

    wle3 = read_json(WLE3_FIXTURE / "manifest.json")
    require_equal(wle3.get("schema_version"), WLE3_STATUS, "WLE3 schema")
    require_equal(wle3.get("certified"), True, "WLE3 certified")
    require_equal(wle3.get("target_only"), True, "WLE3 target only")

    simple_wall = read_json(SIMPLE_WALL_FIXTURE / "manifest.json")
    require_equal(simple_wall.get("status"), SIMPLE_WALL_STATUS, "simple wall status")
    require_equal(
        simple_wall.get("three_simple_wall_orientation_computed"),
        False,
        "simple wall computed flag",
    )

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty blocked")


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "type_ii_chamber_isotropic",
            "wle3_target_parity",
            "simple_wall_chart_orientation",
            "compact_hall_source",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "isotropic_aij_chart_orientation", "criterion id")
    for key in (
        "isotropic_rays_required",
        "target_parity_required",
        "source_chart_required",
        "source_parity_required",
        "quotient_orientation_required",
        "determinant_square_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in ("target_parity_as_source_allowed", "isotropic_orientation_computed"):
        require_equal(bool_cell(row, key), False, key)
    check_verified(row, "criterion_rows.csv")


def verify_empty_chart_rows(rows: list[dict[str, str]]) -> None:
    require_equal(rows, [], "isotropic chart rows")


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
    verify_empty_chart_rows(tables["isotropic_chart_rows.csv"])
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
