#!/usr/bin/env python3
"""Verify row-323 S3 chamber Maass-character triviality packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "delta5_s3_chamber_maass_triviality.v1"
EXPECTED_KIND = "delta5_maass_character_s3_chamber_restriction"
SUCCESS_STATUS = "DELTA5_S3_CHAMBER_MAASS_TRIVIALITY_VERIFIED"
PROOF_LABEL = "prop:s3-chamber-maass-triviality"
DEFAULT_FIXTURE = Path("certificates/automorphic/delta5_s3_chamber_maass_triviality")

MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")
MAASS_SCHEMA = "delta5_maass_character.v1"
MAASS_VERIFIER_STATUS = "MAASS_CHARACTER_VERIFIED"

TYPE_I_GENERATORS = {
    "typeI_fminus2_f2": "delta1_delta2",
    "typeI_f2_f3": "delta1_delta3",
    "typeI_fminus2_f3": "delta2_delta3",
}

EXPECTED_COVERAGE = {
    "generator_count": 3,
    "relation_count": 3,
    "maass_typeI_plus_one_rows": 3,
    "maass_chamber_trivial_relation_rows": 1,
    "orientation_extension_claim": 0,
    "pfaffian_line_claim": 0,
}

REQUIRED_FIREWALL = {
    "orientation_character",
    "epsilon_o_extension_to_semidirect_product",
    "pfaffian_orientation",
    "type_II_W2_comparison",
    "determinant_character",
    "scalar_trace",
    "OP_scalar_branch",
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
        "generator_rows.csv",
        (
            "generator_id",
            "subgroup",
            "tex_label",
            "s3_transposition",
            "character_value",
            "restriction_rule",
            "square_value",
            "maass_source_row",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "relation_rows.csv",
        (
            "relation_id",
            "relation_kind",
            "subgroup",
            "generator_ids",
            "computed_value",
            "expected_value",
            "defect_rank",
            "maass_source_row",
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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("character_kind"), EXPECTED_KIND, "character_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "maass_character_imported",
        "s3_chamber_generators_recorded",
        "generator_values_trivial",
        "s3_generation_recorded",
        "triviality_on_s3_proved",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_character_constructed",
        "epsilon_o_extension_claimed",
        "pfaffian_line_constructed",
        "compact_source_claimed",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(MAASS_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    maass_manifest = read_json(MAASS_FIXTURE / "manifest.json")
    require_equal(maass_manifest.get("schema_version"), MAASS_SCHEMA, "Maass schema")
    require_equal(maass_manifest.get("certified"), True, "Maass certified")
    require_equal(
        maass_manifest.get("automorphic_character_certified"),
        True,
        "Maass automorphic certification",
    )
    require_equal(maass_manifest.get("orientation_character"), False, "Maass orientation firewall")
    require_equal(maass_manifest.get("pfaffian_line"), False, "Maass Pfaffian firewall")

    value_rows = read_table_path(MAASS_FIXTURE / "character_values.csv", None)
    type_i_plus_one = [
        row
        for row in value_rows
        if row.get("generator_id") in TYPE_I_GENERATORS
        and row.get("subgroup") == "type_I_chamber_automorphism"
        and row.get("character_value") == "1"
        and row.get("restriction_rule") == "trivial"
        and row.get("square_value") == "1"
        and row.get("check_status") == "verified"
    ]

    relation_rows = read_table_path(MAASS_FIXTURE / "character_relations.csv", None)
    chamber_relations = [
        row
        for row in relation_rows
        if row.get("relation_id") == "chamber_automorphism_trivial"
        and row.get("relation_kind") == "character_trivial"
        and row.get("subgroup") == "type_I_chamber_automorphism"
        and row.get("computed_value") == "1"
        and row.get("expected_value") == "1"
        and row.get("defect_rank") == "0"
        and row.get("check_status") == "verified"
    ]

    return {
        "maass_typeI_plus_one_rows": len(type_i_plus_one),
        "maass_chamber_trivial_relation_rows": len(chamber_relations),
    }


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(set(indexed), {"maass_character", "s3_chamber_action", "optimization_row"}, "source ids")
    require_equal(indexed["maass_character"]["source_status"], MAASS_VERIFIER_STATUS, "maass source")
    require_equal(indexed["s3_chamber_action"]["source_status"], "S3_chamber_action", "S3 source")
    require_equal(indexed["optimization_row"]["source_status"], "row_323", "optimization row")
    for row in rows:
        check_verified(row, "source_rows.csv")


def verify_generators(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "generator_id", "generator_rows.csv")
    require_equal(set(indexed), set(TYPE_I_GENERATORS), "generator ids")
    for generator_id, transposition in TYPE_I_GENERATORS.items():
        row = indexed[generator_id]
        require_equal(row["subgroup"], "type_I_chamber_automorphism", f"{generator_id} subgroup")
        require_equal(row["s3_transposition"], transposition, f"{generator_id} transposition")
        require_equal(int_cell(row, "character_value"), 1, f"{generator_id} character")
        require_equal(row["restriction_rule"], "trivial", f"{generator_id} rule")
        require_equal(int_cell(row, "square_value"), 1, f"{generator_id} square")
        check_verified(row, "generator_rows.csv")


def verify_relations(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "relation_id", "relation_rows.csv")
    require_equal(
        set(indexed),
        {
            "s3_generated_by_chamber_transpositions",
            "chamber_generator_values_trivial",
            "chamber_automorphism_trivial",
        },
        "relation ids",
    )
    expected_kinds = {
        "s3_generated_by_chamber_transpositions": "group_generation",
        "chamber_generator_values_trivial": "character_trivial_on_generators",
        "chamber_automorphism_trivial": "character_trivial",
    }
    for relation_id, kind in expected_kinds.items():
        row = indexed[relation_id]
        require_equal(row["relation_kind"], kind, f"{relation_id} kind")
        require_equal(row["subgroup"], "type_I_chamber_automorphism", f"{relation_id} subgroup")
        require_equal(int_cell(row, "computed_value"), 1, f"{relation_id} computed")
        require_equal(int_cell(row, "expected_value"), 1, f"{relation_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{relation_id} defect")
        check_verified(row, "relation_rows.csv")


def verify_coverage(
    rows: list[dict[str, str]],
    manifest: dict,
    import_counts: dict[str, int],
    generator_count: int,
    relation_count: int,
) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    dynamic = dict(EXPECTED_COVERAGE)
    dynamic.update(import_counts)
    dynamic["generator_count"] = generator_count
    dynamic["relation_count"] = relation_count
    dynamic["orientation_extension_claim"] = int(bool(manifest.get("epsilon_o_extension_claimed")))
    dynamic["pfaffian_line_claim"] = int(bool(manifest.get("pfaffian_line_constructed")))
    for key, expected in dynamic.items():
        row = indexed[key]
        require_equal(int_cell(row, "computed_value"), expected, f"{key} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{key} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{key} defect")
        check_verified(row, "coverage_rows.csv", proof_required=False)


def verify_firewall(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "forbidden_substitute", "scalar_firewall.csv")
    require_equal(set(indexed), REQUIRED_FIREWALL, "firewall substitutes")
    for row in indexed.values():
        require_equal(bool_cell(row, "excluded"), True, "firewall excluded")
        require_equal(int_cell(row, "defect_rank"), 0, "firewall defect")
        check_verified(row, "scalar_firewall.csv")


def verify_fixture(fixture: Path) -> None:
    manifest = verify_manifest(fixture)
    import_counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    verify_generators(tables["generator_rows.csv"])
    verify_relations(tables["relation_rows.csv"])
    verify_coverage(
        tables["coverage_rows.csv"],
        manifest,
        import_counts,
        len(tables["generator_rows.csv"]),
        len(tables["relation_rows.csv"]),
    )
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
