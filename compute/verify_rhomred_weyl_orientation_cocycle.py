#!/usr/bin/env python3
"""Verify the row-309 orientation projective-cocycle packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_cocycle_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_cocycle_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "def:orientation-projective-cocycle-coR"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_cocycle")

PARTIAL_GROUPOID_FIXTURE = Path("certificates/orientation/rhomred_weyl_partial_action_groupoid")
TAU_TRANSPORT_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")
TAU_SQUARE_FIXTURE = Path("certificates/orientation/rhomred_weyl_tau_square")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")

PARTIAL_GROUPOID_STATUS = "RHOMRED_WEYL_PARTIAL_ACTION_GROUPOID_OBSTRUCTION_VERIFIED"
TAU_TRANSPORT_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
TAU_SQUARE_STATUS = "RHOMRED_WEYL_TAU_SQUARE_OBSTRUCTION_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "definition_count": 1,
    "groupoid_object_rows_supplied": 0,
    "groupoid_arrow_rows_supplied": 0,
    "groupoid_composition_rows_supplied": 0,
    "weyl_lift_rows_supplied": 0,
    "coxeter_cocycle_rows_supplied": 0,
    "composable_pair_rows_supplied": 0,
    "cocycle_value_rows_supplied": 0,
    "normalization_rows_supplied": 0,
    "cocycle_defect_rows_supplied": 0,
    "orientation_cocycle_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "partial_action_groupoid_rows",
    "weyl_lift_rows",
    "coefficient_fibre_rows",
    "composable_pair_rows",
    "cocycle_value_rows",
    "normalization_rows",
    "cocycle_defect_rows",
    "cohomology_vanishing_later",
    "cochain_later",
    "no_target_coxeter_substitution",
}

REQUIRED_FIREWALL = {
    "partial_groupoid_schema_only",
    "tau_transport_criterion_only",
    "tau_square_criterion_only",
    "target_coxeter_graph",
    "maass_character_value",
    "constant_group_cohomology",
    "cocycle_vanishing",
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
        "definition_rows.csv",
        (
            "definition_id",
            "groupoid_required",
            "lift_required",
            "composable_pair_required",
            "coefficient_fibre_required",
            "cocycle_value_required",
            "normalization_required",
            "cocycle_defect_required",
            "cohomology_vanishing_out_of_scope",
            "definition_recorded",
            "orientation_cocycle_defined",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "composable_pair_rows.csv",
        (
            "pair_id",
            "R_id",
            "source_object_id",
            "middle_object_id",
            "target_object_id",
            "g_arrow_id",
            "h_arrow_id",
            "composite_arrow_id",
            "composition_defined",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "cocycle_value_rows.csv",
        (
            "cocycle_id",
            "R_id",
            "pair_id",
            "coefficient_fibre_id",
            "tau_g_id",
            "tau_h_id",
            "tau_composite_id",
            "cocycle_value",
            "normalization_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "cocycle_normalization_rows.csv",
        (
            "normalization_id",
            "R_id",
            "object_id",
            "arrow_id",
            "left_identity_value",
            "right_identity_value",
            "normalization_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "cocycle_defect_rows.csv",
        (
            "defect_id",
            "R_id",
            "triple_id",
            "left_pair_id",
            "right_pair_id",
            "cocycle_coboundary_value",
            "cocycle_defect_rank",
            "cohomology_class_status",
            "cochain_id",
            "cochain_defect_rank",
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
            "cocycle_status",
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
        "partial_action_groupoid_imported",
        "tau_transport_imported",
        "tau_square_imported",
        "orientation_obstruction_imported",
        "cocycle_formula_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "groupoid_rows_supplied",
        "lift_rows_supplied",
        "composable_pair_rows_supplied",
        "cocycle_rows_supplied",
        "normalization_rows_supplied",
        "cocycle_defect_rows_supplied",
        "orientation_cocycle_defined",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(PARTIAL_GROUPOID_FIXTURE),
            str(TAU_TRANSPORT_FIXTURE),
            str(TAU_SQUARE_FIXTURE),
            str(ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    groupoid_manifest = read_json(PARTIAL_GROUPOID_FIXTURE / "manifest.json")
    require_equal(groupoid_manifest.get("status"), PARTIAL_GROUPOID_STATUS, "partial groupoid status")
    require_equal(groupoid_manifest.get("partial_action_groupoid_defined"), False, "partial groupoid defined")

    tau_manifest = read_json(TAU_TRANSPORT_FIXTURE / "manifest.json")
    require_equal(tau_manifest.get("status"), TAU_TRANSPORT_STATUS, "tau transport status")
    require_equal(tau_manifest.get("tau_transport_constructed"), False, "tau transport constructed")

    tau_square_manifest = read_json(TAU_SQUARE_FIXTURE / "manifest.json")
    require_equal(tau_square_manifest.get("status"), TAU_SQUARE_STATUS, "tau square status")
    require_equal(tau_square_manifest.get("tau_square_proved"), False, "tau square proved")

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
        "groupoid_object_rows": count_data_rows(PARTIAL_GROUPOID_FIXTURE / "groupoid_object_rows.csv"),
        "groupoid_arrow_rows": count_data_rows(PARTIAL_GROUPOID_FIXTURE / "groupoid_arrow_rows.csv"),
        "groupoid_composition_rows": count_data_rows(
            PARTIAL_GROUPOID_FIXTURE / "groupoid_composition_rows.csv"
        ),
        "weyl_lift_rows": count_data_rows(ORIENTATION_FIXTURE / "weyl_lifts.csv"),
        "coxeter_cocycle_rows": count_data_rows(ORIENTATION_FIXTURE / "coxeter_cocycles.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "partial_action_groupoid": PARTIAL_GROUPOID_STATUS,
        "tau_transport": TAU_TRANSPORT_STATUS,
        "tau_square": TAU_SQUARE_STATUS,
        "orientation_obstruction": ORIENTATION_STATUS,
        "orientation_cocycle_formula": "proved_formula",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_definition(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["definition_rows.csv"], "definition_id", "definition rows")
    require_equal(set(rows), {"orientation_projective_cocycle"}, "definition ids")
    row = rows["orientation_projective_cocycle"]
    check_verified(row, "definition_rows.csv")
    for key in (
        "groupoid_required",
        "lift_required",
        "composable_pair_required",
        "coefficient_fibre_required",
        "cocycle_value_required",
        "normalization_required",
        "cocycle_defect_required",
        "cohomology_vanishing_out_of_scope",
        "definition_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "orientation_cocycle_defined"), False, "orientation cocycle defined")


def verify_empty_cocycle_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    for table_name in (
        "composable_pair_rows.csv",
        "cocycle_value_rows.csv",
        "cocycle_normalization_rows.csv",
        "cocycle_defect_rows.csv",
    ):
        if tables[table_name]:
            raise ValueError(f"{table_name} must remain empty in obstruction packet")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["groupoid_object_rows_supplied"] = counts["groupoid_object_rows"]
    computed["groupoid_arrow_rows_supplied"] = counts["groupoid_arrow_rows"]
    computed["groupoid_composition_rows_supplied"] = counts["groupoid_composition_rows"]
    computed["weyl_lift_rows_supplied"] = counts["weyl_lift_rows"]
    computed["coxeter_cocycle_rows_supplied"] = counts["coxeter_cocycle_rows"]
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
        require_equal(row["cocycle_status"], "missing_open_obligation", f"{row['obligation_id']} status")
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
    verify_definition(tables)
    verify_empty_cocycle_tables(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_WEYL_ORIENTATION_COCYCLE_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
