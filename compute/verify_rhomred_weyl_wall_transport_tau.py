#!/usr/bin/env python3
"""Verify the row-306 Weyl wall transport tau packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_wall_transport_tau_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_wall_transport_tau_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:weyl-wall-transport-tau-construction"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")

ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
TYPE_II_FIXTURE = Path("certificates/lattice/type_ii_chamber_isotropic")
WALL_SURVIVAL_FIXTURE = Path("certificates/hybrid/type_ii_wall_e_quotient_survival")
O2_FIXTURE = Path("certificates/wall_atlas/k3e_o2_atlas")

ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
TYPE_II_STATUS = "TYPE_II_CHAMBER_ISOTROPIC_VERIFIED"
WALL_SURVIVAL_STATUS = "TYPE_II_WALL_E_QUOTIENT_SURVIVAL_VERIFIED"
O2_STATUS = "O2_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "type_ii_generator_rows_available": 3,
    "wall_profile_survival_rows_available": 3,
    "orientation_line_rows_supplied": 0,
    "weyl_lift_rows_supplied": 0,
    "wall_object_rows_supplied": 0,
    "tau_transport_claim": 0,
    "tau_square_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "orientation_line_rows",
    "determinant_square_compatibility",
    "retained_wall_object_rows",
    "wall_correspondence_transport",
    "quotient_cocycle_transport",
    "finite_stabilizer_transport",
    "linearization_transport",
    "weyl_lift_matrix",
    "torsor_defect_zero",
    "quotient_transport_defect_zero",
    "tau_square_row",
    "no_scalar_tau_substitution",
}

REQUIRED_FIREWALL = {
    "type_ii_generator_only",
    "wall_profile_survival_only",
    "o2_wall_atlas_only",
    "maass_character_value",
    "scalar_trace",
    "target_root_window",
    "tau_square_without_tau",
    "pfaffian_wall_sign",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


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
            "type_ii_generator_required",
            "retained_wall_correspondence_required",
            "source_orientation_line_required",
            "target_orientation_line_required",
            "determinant_square_required",
            "quotient_cocycle_transport_required",
            "finite_stabilizer_transport_required",
            "linearization_transport_required",
            "lift_matrix_required",
            "torsor_defect_zero_required",
            "quotient_transport_defect_zero_required",
            "tau_square_out_of_scope",
            "criterion_recorded",
            "tau_transport_constructed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "imported_status_rows.csv",
        (
            "import_id",
            "import_path",
            "import_status",
            "positive_input",
            "missing_input",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "tau_transport_obstruction_rows.csv",
        (
            "obstruction_id",
            "type_ii_generator_status",
            "wall_profile_status",
            "orientation_line_status",
            "retained_wall_object_status",
            "determinant_square_status",
            "quotient_cocycle_transport_status",
            "finite_stabilizer_transport_status",
            "linearization_transport_status",
            "lift_matrix_status",
            "torsor_defect_status",
            "quotient_transport_defect_status",
            "tau_square_status",
            "tau_transport_constructed",
            "mathematical_certification",
            "proof_reference",
            "check_status",
            "notes",
        ),
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
            "tau_transport_status",
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
    return read_table_path(fixture / spec.path, spec.columns)


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
        "orientation_obstruction_imported",
        "type_ii_chamber_imported",
        "wall_profile_survival_imported",
        "o2_wall_atlas_imported",
        "weyl_wall_transport_criterion_recorded",
        "type_ii_generators_available",
        "wall_profiles_survive_quotient",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_line_rows_supplied",
        "retained_wall_object_rows_supplied",
        "weyl_lift_rows_supplied",
        "tau_transport_constructed",
        "tau_square_proved",
        "transition_compatibility",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ORIENTATION_FIXTURE),
            str(TYPE_II_FIXTURE),
            str(WALL_SURVIVAL_FIXTURE),
            str(O2_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_STATUS,
        "orientation obstruction status",
    )
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty")
    require_equal(orientation_manifest.get("orientation_certification"), False, "orientation certification")
    require_equal(orientation_manifest.get("mathematical_certification"), False, "orientation math")

    type_ii_manifest = read_json(TYPE_II_FIXTURE / "manifest.json")
    require_equal(type_ii_manifest.get("certified"), True, "type-II certified")
    require_equal(type_ii_manifest.get("chamber_isotropic_certified"), True, "type-II chamber certified")
    require_equal(type_ii_manifest.get("compact_source"), False, "type-II compact source")
    require_equal(type_ii_manifest.get("pfaffian_orientation"), False, "type-II orientation")
    require_equal(type_ii_manifest.get("o2_wall_atlas"), False, "type-II O2")

    survival_manifest = read_json(WALL_SURVIVAL_FIXTURE / "manifest.json")
    require_equal(survival_manifest.get("status"), WALL_SURVIVAL_STATUS, "wall survival status")
    require_equal(survival_manifest.get("three_wall_survival_certified"), True, "three-wall survival")
    require_equal(survival_manifest.get("orientation_descent"), False, "wall survival orientation")
    require_equal(survival_manifest.get("o2_wall_atlas"), False, "wall survival O2")
    require_equal(survival_manifest.get("protected_integration"), False, "wall survival integration")

    o2_manifest = read_json(O2_FIXTURE / "manifest.json")
    require_equal(o2_manifest.get("obstruction_ledger_status"), O2_STATUS, "O2 obstruction status")
    require_equal(o2_manifest.get("empty_blocked"), True, "O2 empty")
    require_equal(o2_manifest.get("o2_certification"), False, "O2 certification")
    require_equal(o2_manifest.get("mathematical_certification"), False, "O2 math")

    orientation_blocked = rows_by(
        read_table_path(ORIENTATION_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "orientation obligations",
    )
    for obligation_id in (
        "orientation_square_root",
        "orientation_class_zero",
        "weyl_lift_torsor",
        "weyl_lift_quotient_transport",
    ):
        if obligation_id not in orientation_blocked:
            raise ValueError(f"orientation ledger missing {obligation_id}")
        require_equal(
            orientation_blocked[obligation_id]["orientation_status"],
            "missing_open_obligation",
            f"{obligation_id} status",
        )

    survival_blocked = rows_by(
        read_table_path(WALL_SURVIVAL_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "wall survival obligations",
    )
    for obligation_id in (
        "retained_wall_object_rows",
        "orientation_descent",
        "o2_wall_atlas_rows",
    ):
        if obligation_id not in survival_blocked:
            raise ValueError(f"wall survival ledger missing {obligation_id}")
        require_equal(
            survival_blocked[obligation_id]["survival_status"],
            "missing_open_obligation",
            f"{obligation_id} status",
        )

    return {
        "type_ii_generators": count_data_rows(TYPE_II_FIXTURE / "type_ii_generators.csv"),
        "wall_survival_rows": count_data_rows(WALL_SURVIVAL_FIXTURE / "wall_survival_rows.csv"),
        "orientation_lines": count_data_rows(ORIENTATION_FIXTURE / "orientation_lines.csv"),
        "weyl_lifts": count_data_rows(ORIENTATION_FIXTURE / "weyl_lifts.csv"),
        "wall_objects": count_data_rows(O2_FIXTURE / "wall_objects.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "orientation_obstruction": ORIENTATION_STATUS,
        "type_ii_chamber": TYPE_II_STATUS,
        "wall_profile_survival": WALL_SURVIVAL_STATUS,
        "o2_wall_atlas": O2_STATUS,
        "tau_transport_criterion": "proved_criterion",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"weyl_wall_tau_transport"}, "criterion ids")
    row = rows["weyl_wall_tau_transport"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "type_ii_generator_required",
        "retained_wall_correspondence_required",
        "source_orientation_line_required",
        "target_orientation_line_required",
        "determinant_square_required",
        "quotient_cocycle_transport_required",
        "finite_stabilizer_transport_required",
        "linearization_transport_required",
        "lift_matrix_required",
        "torsor_defect_zero_required",
        "quotient_transport_defect_zero_required",
        "tau_square_out_of_scope",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "tau_transport_constructed"), False, "tau transport constructed")


def verify_imported_status_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["imported_status_rows.csv"], "import_id", "imported rows")
    expected = {
        "orientation_obstruction": ORIENTATION_STATUS,
        "type_ii_chamber": TYPE_II_STATUS,
        "wall_profile_survival": WALL_SURVIVAL_STATUS,
        "o2_wall_atlas": O2_STATUS,
    }
    require_equal(set(rows), set(expected), "import ids")
    for import_id, status in expected.items():
        row = rows[import_id]
        require_equal(row["import_status"], status, f"{import_id} status")
        check_verified(row, "imported_status_rows.csv")
        if not row["positive_input"] or not row["missing_input"]:
            raise ValueError(f"{import_id}: missing positive or missing input description")


def verify_obstruction_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["tau_transport_obstruction_rows.csv"], "obstruction_id", "obstruction rows")
    require_equal(set(rows), {"weyl_wall_tau_transport"}, "obstruction ids")
    row = rows["weyl_wall_tau_transport"]
    check_verified(row, "tau_transport_obstruction_rows.csv")
    require_equal(row["type_ii_generator_status"], "available_target_input", "type-II generator status")
    require_equal(row["wall_profile_status"], "available_profile_input", "wall profile status")
    for key in (
        "orientation_line_status",
        "retained_wall_object_status",
        "determinant_square_status",
        "quotient_cocycle_transport_status",
        "finite_stabilizer_transport_status",
        "linearization_transport_status",
        "lift_matrix_status",
        "torsor_defect_status",
        "quotient_transport_defect_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(row["tau_square_status"], "separate_row_307", "tau square status")
    require_equal(bool_cell(row, "tau_transport_constructed"), False, "tau constructed")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["type_ii_generator_rows_available"] = counts["type_ii_generators"]
    computed["wall_profile_survival_rows_available"] = counts["wall_survival_rows"]
    computed["orientation_line_rows_supplied"] = counts["orientation_lines"]
    computed["weyl_lift_rows_supplied"] = counts["weyl_lifts"]
    computed["wall_object_rows_supplied"] = counts["wall_objects"]
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
        require_equal(row["tau_transport_status"], "missing_open_obligation", f"{row['obligation_id']} status")
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
    verify_imported_status_rows(tables)
    verify_obstruction_rows(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_WEYL_WALL_TRANSPORT_TAU_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
