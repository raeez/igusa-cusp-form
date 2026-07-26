#!/usr/bin/env python3
"""Finite Maass-character gate for the Delta_5 automorphic line.

This verifier checks only automorphic character arithmetic:

* nu_Delta5 is a character with values in {+1,-1};
* on type-II Weyl generators it equals the determinant character;
* on the type-I chamber automorphism factor it is trivial;
* nu_Delta5^2 is trivial, so Delta_5^2 is scalar of weight 10;
* Delta_5 lives on L^5 tensor nu_Delta5, not on an orientation line.

It does not construct the Pfaffian orientation, Weyl-equivariant
transport of determinant lines, an O2 wall atlas, compact source data,
or an OP scalar trace.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "MAASS_CHARACTER_VERIFIED"
EXPECTED_KIND = "delta5_maass_character_automorphic_line"
FORBIDDEN_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "todo",
        "unsupplied",
    }
)
REQUIRED_GENERATORS = {
    "typeII_delta1": ("type_II_weyl", -1, -1, "determinant"),
    "typeII_delta2": ("type_II_weyl", -1, -1, "determinant"),
    "typeII_delta3": ("type_II_weyl", -1, -1, "determinant"),
    "typeI_fminus2_f2": ("type_I_chamber_automorphism", 1, -1, "trivial"),
    "typeI_f2_f3": ("type_I_chamber_automorphism", 1, -1, "trivial"),
    "typeI_fminus2_f3": ("type_I_chamber_automorphism", 1, -1, "trivial"),
}
REQUIRED_RELATIONS = frozenset(
    {
        "weyl_restriction_determinant",
        "chamber_automorphism_trivial",
        "character_order_two",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "orientation_character",
        "pfaffian_orientation",
        "op_scalar_branch",
        "squared_determinant",
        "compact_source_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "character_values.csv",
        (
            "generator_id",
            "subgroup",
            "tex_label",
            "character_value",
            "determinant_value",
            "restriction_rule",
            "square_value",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "character_relations.csv",
        (
            "relation_id",
            "relation_kind",
            "subgroup",
            "generator_ids",
            "computed_value",
            "expected_value",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "automorphic_line.csv",
        (
            "line_id",
            "section_id",
            "base_line",
            "weight",
            "character_id",
            "character_order",
            "squared_line",
            "squared_weight",
            "squared_character_trivial",
            "is_orientation_line",
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
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/automorphic/delta5_maass_character"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def read_manifest(fixture: Path) -> dict:
    manifest_path = fixture / MANIFEST_NAME
    readme_path = fixture / README_NAME
    if not manifest_path.exists():
        raise ValueError(f"missing manifest: {manifest_path}")
    if not readme_path.exists() or not readme_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    path = fixture / spec.path
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != spec.columns:
            raise ValueError(
                f"{spec.path}: expected columns {spec.columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{spec.path}: unparsed CSV fields in row {row}")
    return rows


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def check_row(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    if not row.get("source_reference", "").strip():
        raise ValueError(f"{table_name}: missing source_reference: {row}")
    haystack = " ".join(row.values()).lower()
    for token in FORBIDDEN_TOKENS:
        if token in haystack:
            raise ValueError(f"{table_name}: forbidden token {token!r} in {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("character_kind"), EXPECTED_KIND, "manifest character_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("automorphic_character_certified"), True, "manifest automorphic_character_certified")
    require_equal(manifest.get("orientation_character"), False, "manifest orientation_character")
    require_equal(manifest.get("pfaffian_line"), False, "manifest pfaffian_line")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("op_scalar_branch"), False, "manifest op_scalar_branch")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_character_values(rows: list[dict[str, str]]) -> dict[str, dict[str, int | str]]:
    values: dict[str, dict[str, int | str]] = {}
    for row in rows:
        check_row(row, "character_values.csv")
        generator_id = row["generator_id"]
        if generator_id in values:
            raise ValueError(f"character_values.csv: duplicate generator_id {generator_id}")
        if generator_id not in REQUIRED_GENERATORS:
            raise ValueError(f"character_values.csv: unexpected generator_id {generator_id}")
        subgroup, character_value, determinant_value, restriction_rule = REQUIRED_GENERATORS[generator_id]
        require_equal(row["subgroup"], subgroup, f"{generator_id} subgroup")
        require_equal(int_cell(row, "character_value"), character_value, f"{generator_id} character_value")
        require_equal(int_cell(row, "determinant_value"), determinant_value, f"{generator_id} determinant_value")
        require_equal(row["restriction_rule"], restriction_rule, f"{generator_id} restriction_rule")
        require_equal(character_value * character_value, int_cell(row, "square_value"), f"{generator_id} square_value")
        require_equal(int_cell(row, "square_value"), 1, f"{generator_id} square is one")
        if restriction_rule == "determinant":
            require_equal(character_value, determinant_value, f"{generator_id} determinant restriction")
        elif restriction_rule == "trivial":
            require_equal(character_value, 1, f"{generator_id} trivial restriction")
        else:
            raise ValueError(f"{generator_id}: unknown restriction_rule {restriction_rule}")
        values[generator_id] = {
            "subgroup": subgroup,
            "character_value": character_value,
            "determinant_value": determinant_value,
            "restriction_rule": restriction_rule,
        }
    require_equal(set(values), set(REQUIRED_GENERATORS), "character generator coverage")
    return values


def verify_character_relations(
    rows: list[dict[str, str]],
    values: dict[str, dict[str, int | str]],
) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "character_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"character_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"character_relations.csv: unexpected relation_id {relation_id}")
        generator_ids = split_ids(row["generator_ids"])
        if not generator_ids:
            raise ValueError(f"{relation_id}: empty generator_ids")
        for generator_id in generator_ids:
            if generator_id not in values:
                raise ValueError(f"{relation_id}: unknown generator {generator_id}")
            if row["subgroup"] != "all_generators":
                require_equal(values[generator_id]["subgroup"], row["subgroup"], f"{relation_id} subgroup")

        if row["relation_kind"] == "character_equals_determinant":
            defects = sum(
                int(values[generator_id]["character_value"])
                != int(values[generator_id]["determinant_value"])
                for generator_id in generator_ids
            )
            computed = 1 if defects == 0 else 0
        elif row["relation_kind"] == "character_trivial":
            defects = sum(
                int(values[generator_id]["character_value"]) != 1
                for generator_id in generator_ids
            )
            computed = 1 if defects == 0 else 0
        elif row["relation_kind"] == "character_order_two":
            defects = sum(
                int(values[generator_id]["character_value"]) ** 2 != 1
                for generator_id in generator_ids
            )
            computed = 1 if defects == 0 else 0
        else:
            raise ValueError(f"{relation_id}: unknown relation_kind {row['relation_kind']!r}")
        require_equal(int_cell(row, "computed_value"), computed, f"{relation_id} computed_value")
        require_equal(int_cell(row, "expected_value"), 1, f"{relation_id} expected_value")
        require_equal(int_cell(row, "defect_rank"), defects, f"{relation_id} defect_rank")
    require_equal(seen, REQUIRED_RELATIONS, "character relation coverage")


def verify_automorphic_line(rows: list[dict[str, str]]) -> None:
    if len(rows) != 1:
        raise ValueError("automorphic_line.csv: expected exactly one row")
    row = rows[0]
    check_row(row, "automorphic_line.csv")
    require_equal(row["line_id"], "delta5_automorphic_line", "line_id")
    require_equal(row["section_id"], "Delta5", "section_id")
    require_equal(row["base_line"], "Hodge_L", "base_line")
    require_equal(int_cell(row, "weight"), 5, "weight")
    require_equal(row["character_id"], "nu_Delta5", "character_id")
    require_equal(int_cell(row, "character_order"), 2, "character_order")
    require_equal(row["squared_line"], "Hodge_L^10", "squared_line")
    require_equal(int_cell(row, "squared_weight"), 10, "squared_weight")
    require_equal(bool_cell(row, "squared_character_trivial"), True, "squared_character_trivial")
    require_equal(bool_cell(row, "is_orientation_line"), False, "is_orientation_line")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"scalar_firewall.csv: duplicate substitute {substitute}")
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"scalar_firewall.csv missing rows: {sorted(missing)}")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        values = verify_character_values(tables["character_values.csv"])
        verify_character_relations(tables["character_relations.csv"], values)
        verify_automorphic_line(tables["automorphic_line.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"MAASS_CHARACTER_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
