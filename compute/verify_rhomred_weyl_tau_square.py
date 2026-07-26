#!/usr/bin/env python3
"""Verify the row-307 Weyl tau-square packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_tau_square_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_tau_square_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_TAU_SQUARE_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:weyl-wall-transport-tau-square"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_tau_square")

TAU_TRANSPORT_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
TYPE_II_FIXTURE = Path("certificates/lattice/type_ii_chamber_isotropic")
MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")

TAU_TRANSPORT_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
TYPE_II_STATUS = "TYPE_II_CHAMBER_ISOTROPIC_VERIFIED"
MAASS_STATUS = "MAASS_CHARACTER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "type_ii_generator_rows_available": 3,
    "maass_square_rows_available": 3,
    "weyl_lift_rows_supplied": 0,
    "tau_square_rows_supplied": 0,
    "tau_transport_claim": 0,
    "tau_square_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "tau_transport_rows",
    "double_reflection_source_loop",
    "determinant_square_compatibility",
    "quotient_loop_transport",
    "finite_stabilizer_loop",
    "linearization_loop",
    "line_automorphism_identity",
    "tau_square_defect_zero",
    "coxeter_coherence_later",
    "no_scalar_tau_square_substitution",
}

REQUIRED_FIREWALL = {
    "target_reflection_square",
    "maass_square_value",
    "tau_transport_criterion_only",
    "determinant_square_only",
    "scalar_trace",
    "pfaffian_wall_sign",
    "target_root_window",
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
            "tau_transport_required",
            "double_reflection_loop_required",
            "target_square_required",
            "determinant_square_required",
            "quotient_loop_transport_required",
            "finite_stabilizer_loop_required",
            "linearization_loop_required",
            "line_automorphism_identity_required",
            "tau_square_defect_required",
            "criterion_recorded",
            "tau_square_proved",
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
        "tau_square_obstruction_rows.csv",
        (
            "obstruction_id",
            "tau_transport_status",
            "target_square_status",
            "maass_square_status",
            "double_reflection_loop_status",
            "determinant_square_status",
            "quotient_loop_transport_status",
            "finite_stabilizer_loop_status",
            "linearization_loop_status",
            "line_automorphism_status",
            "tau_square_defect_status",
            "tau_square_proved",
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
            "tau_square_status",
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


def count_maass_type_ii_squares() -> int:
    rows = read_table_path(MAASS_FIXTURE / "character_values.csv", None)
    count = 0
    for row in rows:
        if row.get("subgroup") == "type_II_weyl" and row.get("square_value") == "1":
            if row.get("check_status") != "verified":
                raise ValueError("type-II Maass square row is not verified")
            count += 1
    return count


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "tau_transport_imported",
        "orientation_obstruction_imported",
        "type_ii_chamber_imported",
        "maass_character_imported",
        "tau_square_criterion_recorded",
        "target_reflection_square_available",
        "maass_square_available",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "tau_transport_rows_supplied",
        "tau_square_rows_supplied",
        "tau_square_proved",
        "coxeter_coherence",
        "transition_compatibility",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(TAU_TRANSPORT_FIXTURE),
            str(ORIENTATION_FIXTURE),
            str(TYPE_II_FIXTURE),
            str(MAASS_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    tau_manifest = read_json(TAU_TRANSPORT_FIXTURE / "manifest.json")
    require_equal(tau_manifest.get("status"), TAU_TRANSPORT_STATUS, "tau transport status")
    require_equal(tau_manifest.get("tau_transport_constructed"), False, "tau transport constructed")
    require_equal(tau_manifest.get("tau_square_proved"), False, "tau square in row 306")

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
    require_equal(type_ii_manifest.get("pfaffian_orientation"), False, "type-II orientation")

    maass_manifest = read_json(MAASS_FIXTURE / "manifest.json")
    require_equal(maass_manifest.get("certified"), True, "Maass certified")
    require_equal(
        maass_manifest.get("automorphic_character_certified"),
        True,
        "Maass automorphic character",
    )
    require_equal(maass_manifest.get("orientation_character"), False, "Maass orientation")
    require_equal(maass_manifest.get("pfaffian_line"), False, "Maass Pfaffian")
    require_equal(maass_manifest.get("compact_source"), False, "Maass compact source")

    orientation_blocked = rows_by(
        read_table_path(ORIENTATION_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "orientation obligations",
    )
    for obligation_id in (
        "weyl_lift_tau_square",
        "weyl_lift_torsor",
        "weyl_lift_quotient_transport",
        "coxeter_coherence",
    ):
        if obligation_id not in orientation_blocked:
            raise ValueError(f"orientation ledger missing {obligation_id}")
        require_equal(
            orientation_blocked[obligation_id]["orientation_status"],
            "missing_open_obligation",
            f"{obligation_id} status",
        )

    return {
        "type_ii_generators": count_data_rows(TYPE_II_FIXTURE / "type_ii_generators.csv"),
        "maass_square_rows": count_maass_type_ii_squares(),
        "weyl_lifts": count_data_rows(ORIENTATION_FIXTURE / "weyl_lifts.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "tau_transport": TAU_TRANSPORT_STATUS,
        "orientation_obstruction": ORIENTATION_STATUS,
        "type_ii_chamber": TYPE_II_STATUS,
        "maass_character": MAASS_STATUS,
        "tau_square_criterion": "proved_criterion",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"weyl_tau_square"}, "criterion ids")
    row = rows["weyl_tau_square"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "tau_transport_required",
        "double_reflection_loop_required",
        "target_square_required",
        "determinant_square_required",
        "quotient_loop_transport_required",
        "finite_stabilizer_loop_required",
        "linearization_loop_required",
        "line_automorphism_identity_required",
        "tau_square_defect_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "tau_square_proved"), False, "tau square proved")


def verify_imported_status_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["imported_status_rows.csv"], "import_id", "imported rows")
    expected = {
        "row306_tau_transport": TAU_TRANSPORT_STATUS,
        "orientation_obstruction": ORIENTATION_STATUS,
        "type_ii_chamber": TYPE_II_STATUS,
        "maass_character": MAASS_STATUS,
    }
    require_equal(set(rows), set(expected), "import ids")
    for import_id, status in expected.items():
        row = rows[import_id]
        require_equal(row["import_status"], status, f"{import_id} status")
        check_verified(row, "imported_status_rows.csv")
        if not row["positive_input"] or not row["missing_input"]:
            raise ValueError(f"{import_id}: missing positive or missing input description")


def verify_obstruction_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["tau_square_obstruction_rows.csv"], "obstruction_id", "obstruction rows")
    require_equal(set(rows), {"weyl_tau_square"}, "obstruction ids")
    row = rows["weyl_tau_square"]
    check_verified(row, "tau_square_obstruction_rows.csv")
    require_equal(row["target_square_status"], "available_target_input", "target square")
    require_equal(row["maass_square_status"], "available_scalar_input", "Maass square")
    for key in (
        "tau_transport_status",
        "double_reflection_loop_status",
        "determinant_square_status",
        "quotient_loop_transport_status",
        "finite_stabilizer_loop_status",
        "linearization_loop_status",
        "line_automorphism_status",
        "tau_square_defect_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    require_equal(bool_cell(row, "tau_square_proved"), False, "tau square proved")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["type_ii_generator_rows_available"] = counts["type_ii_generators"]
    computed["maass_square_rows_available"] = counts["maass_square_rows"]
    computed["weyl_lift_rows_supplied"] = counts["weyl_lifts"]
    computed["tau_square_rows_supplied"] = counts["weyl_lifts"]
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
        require_equal(row["tau_square_status"], "missing_open_obligation", f"{row['obligation_id']} status")
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
        print(f"RHOMRED_WEYL_TAU_SQUARE_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
