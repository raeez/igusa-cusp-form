#!/usr/bin/env python3
"""Verify row-320 simple orientation-character sign packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_simple_sign_computation_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_simple_sign_computation_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_SIMPLE_SIGN_COMPUTATION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-character-simple-wall-sign-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_simple_sign_computation")

CHARACTER_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_character_definition")
O2_FIXTURE = Path("certificates/wall_atlas/k3e_o2_atlas")
PFIN_FIXTURE = Path("certificates/pfaffian/k3e_finite_pfaffian")
MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")

CHARACTER_STATUS = "RHOMRED_WEYL_ORIENTATION_CHARACTER_DEFINITION_OBSTRUCTION_VERIFIED"
O2_STATUS = "O2_OBSTRUCTION_LEDGER_VERIFIED"
PFIN_STATUS = "PFAFFIAN_OBSTRUCTION_LEDGER_VERIFIED"
MAASS_SCHEMA = "delta5_maass_character.v1"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "row319_character_constructed_claim": 0,
    "row319_generator_sign_rows": 0,
    "o2_wall_object_rows": 0,
    "o2_wall_chart_rows": 0,
    "o2_certification_claim": 0,
    "pfin_wall_chart_rows": 0,
    "pfin_certification_claim": 0,
    "maass_typeII_minus_one_rows": 3,
    "maass_orientation_character_claim": 0,
    "simple_sign_rows": 0,
    "simple_sign_computation_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "orientation_character_constructed",
    "simple_wall_coverage",
    "rank_one_wall_chart",
    "normal_coordinate",
    "reflection_flip",
    "invariant_unit",
    "divisor_order",
    "local_sign_row",
    "finite_pfaffian_wall_chart",
    "generator_sign_row",
    "stratum_independence",
    "transition_compatibility",
    "row321_separation",
    "maass_firewall",
}

REQUIRED_FIREWALL = {
    "maass_character_value",
    "automorphic_character_certified",
    "determinant_character",
    "row319_definition_only",
    "local_formula_only",
    "O2_obstruction_ledger_only",
    "finite_pfaffian_ledger_only",
    "target_coxeter_graph",
    "OP_scalar_branch",
    "scalar_trace",
    "squared_determinant",
    "empty_sign_table",
    "row321_det_comparison",
    "row322_maass_comparison",
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
            "orientation_character_required",
            "o2_wall_atlas_required",
            "finite_pfaffian_wall_chart_required",
            "simple_wall_coverage_required",
            "normal_rank_required",
            "divisor_order_required",
            "unit_invariance_required",
            "reflection_coordinate_flip_required",
            "local_sign_required",
            "stratum_independence_required",
            "transition_compatibility_required",
            "maass_as_source_allowed",
            "criterion_recorded",
            "simple_sign_computation_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "simple_sign_rows.csv",
        (
            "sign_id",
            "R_id",
            "stratum_id",
            "delta_id",
            "wall_chart_id",
            "orientation_character_row_id",
            "normal_rank",
            "divisor_order",
            "unit_invariant",
            "reflection_flips_coordinate",
            "N_pf",
            "local_pfaffian_sign",
            "generator_sign",
            "sign_computation_verified",
            "stratum_independence_row_id",
            "transition_compatibility_row_id",
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
            "sign_status",
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


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "orientation_character_definition_imported",
        "o2_wall_atlas_imported",
        "finite_pfaffian_imported",
        "maass_character_firewall_imported",
        "local_sign_formula_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_character_constructed",
        "simple_wall_coverage_rows_supplied",
        "rank_one_wall_chart_rows_supplied",
        "pfaffian_unit_rows_supplied",
        "reflection_coordinate_rows_supplied",
        "local_sign_rows_supplied",
        "generator_sign_rows_supplied",
        "stratum_independence_rows_supplied",
        "transition_compatibility_rows_supplied",
        "simple_sign_computation_proved",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(CHARACTER_FIXTURE), str(O2_FIXTURE), str(PFIN_FIXTURE), str(MAASS_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    character_manifest = read_json(CHARACTER_FIXTURE / "manifest.json")
    require_equal(character_manifest.get("status"), CHARACTER_STATUS, "character status")
    require_equal(
        character_manifest.get("orientation_character_constructed"),
        False,
        "orientation character constructed",
    )
    character_sign_rows = count_data_rows(CHARACTER_FIXTURE / "generator_sign_rows.csv")

    o2_manifest = read_json(O2_FIXTURE / "manifest.json")
    require_equal(o2_manifest.get("obstruction_ledger_status"), O2_STATUS, "O2 status")
    require_equal(o2_manifest.get("o2_certification"), False, "O2 certification")
    require_equal(o2_manifest.get("mathematical_certification"), False, "O2 math certification")
    o2_wall_objects = count_data_rows(O2_FIXTURE / "wall_objects.csv")
    o2_wall_charts = count_data_rows(O2_FIXTURE / "wall_charts.csv")

    pfin_manifest = read_json(PFIN_FIXTURE / "manifest.json")
    require_equal(pfin_manifest.get("obstruction_ledger_status"), PFIN_STATUS, "Pfin status")
    require_equal(pfin_manifest.get("pfaffian_certification"), False, "Pfin certification")
    require_equal(pfin_manifest.get("mathematical_certification"), False, "Pfin math certification")
    pfin_wall_charts = count_data_rows(PFIN_FIXTURE / "wall_charts.csv")

    maass_manifest = read_json(MAASS_FIXTURE / "manifest.json")
    require_equal(maass_manifest.get("schema_version"), MAASS_SCHEMA, "Maass schema")
    require_equal(maass_manifest.get("automorphic_character_certified"), True, "Maass certified")
    require_equal(maass_manifest.get("orientation_character"), False, "Maass orientation firewall")
    require_equal(maass_manifest.get("pfaffian_line"), False, "Maass Pfaffian firewall")

    maass_rows = read_table_path(MAASS_FIXTURE / "character_values.csv", None)
    type_ii_minus_one = [
        row
        for row in maass_rows
        if row.get("subgroup") == "type_II_weyl" and row.get("character_value") == "-1"
    ]

    return {
        "row319_character_constructed_claim": int(
            bool(character_manifest.get("orientation_character_constructed"))
        ),
        "row319_generator_sign_rows": character_sign_rows,
        "o2_wall_object_rows": o2_wall_objects,
        "o2_wall_chart_rows": o2_wall_charts,
        "o2_certification_claim": int(bool(o2_manifest.get("o2_certification"))),
        "pfin_wall_chart_rows": pfin_wall_charts,
        "pfin_certification_claim": int(bool(pfin_manifest.get("pfaffian_certification"))),
        "maass_typeII_minus_one_rows": len(type_ii_minus_one),
        "maass_orientation_character_claim": int(bool(maass_manifest.get("orientation_character"))),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "orientation_character_definition": CHARACTER_STATUS,
        "o2_wall_atlas": O2_STATUS,
        "finite_pfaffian": PFIN_STATUS,
        "maass_character_firewall": MAASS_SCHEMA,
        "optimization_row": "row_320",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    expected_id = "simple_wall_orientation_sign"
    require_equal(set(rows), {expected_id}, "criterion ids")
    row = rows[expected_id]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "orientation_character_required",
        "o2_wall_atlas_required",
        "finite_pfaffian_wall_chart_required",
        "simple_wall_coverage_required",
        "normal_rank_required",
        "divisor_order_required",
        "unit_invariance_required",
        "reflection_coordinate_flip_required",
        "local_sign_required",
        "stratum_independence_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "maass_as_source_allowed"), False, "Maass as source")
    require_equal(
        bool_cell(row, "simple_sign_computation_proved"),
        False,
        "simple sign computation proved",
    )


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    if tables["simple_sign_rows.csv"]:
        raise ValueError("simple_sign_rows.csv must remain empty in obstruction packet")


def verify_coverage(
    manifest: dict,
    tables: dict[str, list[dict[str, str]]],
    counts: dict[str, int],
) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed.update(counts)
    computed["simple_sign_rows"] = len(tables["simple_sign_rows.csv"])
    computed["simple_sign_computation_claim"] = int(
        bool(manifest.get("simple_sign_computation_proved"))
    )
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(
            int_cell(row, "computed_value"),
            computed[coverage_id],
            f"{coverage_id} computed",
        )
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(
            row["sign_status"],
            "missing_open_obligation",
            f"{row['obligation_id']} status",
        )
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
    manifest = verify_manifest(fixture)
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_empty_tables(tables)
    verify_coverage(manifest, tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_WEYL_ORIENTATION_SIMPLE_SIGN_COMPUTATION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
