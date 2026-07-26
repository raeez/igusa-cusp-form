#!/usr/bin/env python3
"""Finite Humbert-divisor gate for the Delta_5 automorphic divisor.

This verifier checks only automorphic divisor arithmetic:

* the three type-II wall representatives lie on the Humbert support;
* Delta_5 has simple zero order one on those representatives;
* Delta_5^{-2} has pole order two on the same support;
* support equality and multiplicity are recorded as separate rows.

It does not construct a Pfaffian wall chart, a mirror-period
discriminant, an O2 atlas, compact source data, or a protected trace.
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
SUCCESS_STATUS = "HUMBERT_DIVISOR_VERIFIED"
EXPECTED_KIND = "delta5_humbert_divisor_automorphic"
REQUIRED_COMPONENTS = {
    "H_delta1": ("delta_1", "type_II_wall", 1),
    "H_delta2": ("delta_2", "type_II_wall", 1),
    "H_delta3": ("delta_3", "type_II_wall", 1),
}
REQUIRED_RELATIONS = frozenset(
    {
        "delta5_humbert_zero",
        "delta5_inverse_square_pole",
        "support_multiplicity_separation",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "pfaffian_wall_chart",
        "o2_wall_atlas",
        "mirror_discriminant",
        "compact_source_trace",
        "orientation_character",
    }
)
FORBIDDEN_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "todo",
        "unsupplied",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "support_components.csv",
        (
            "component_id",
            "wall_label",
            "support_kind",
            "orbit_id",
            "support_label",
            "delta5_order",
            "support_member",
            "multiplicity_status",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "divisor_relations.csv",
        (
            "relation_id",
            "relation_kind",
            "form_id",
            "support_label",
            "expected_support_label",
            "base_zero_order",
            "form_exponent",
            "computed_order",
            "expected_order",
            "support_defect_rank",
            "multiplicity_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "support_multiplicity_separation.csv",
        (
            "separation_id",
            "support_statement",
            "multiplicity_statement",
            "support_defect_rank",
            "multiplicity_defect_rank",
            "collapsed",
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
        default=Path("certificates/automorphic/delta5_humbert_divisor"),
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


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("divisor_kind"), EXPECTED_KIND, "manifest divisor_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("automorphic_divisor_certified"), True, "manifest automorphic_divisor_certified")
    require_equal(manifest.get("pfaffian_wall_chart"), False, "manifest pfaffian_wall_chart")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_support_components(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "support_components.csv")
        component_id = row["component_id"]
        if component_id in seen:
            raise ValueError(f"support_components.csv: duplicate component_id {component_id}")
        seen.add(component_id)
        if component_id not in REQUIRED_COMPONENTS:
            raise ValueError(f"support_components.csv: unexpected component_id {component_id}")
        wall_label, support_kind, order = REQUIRED_COMPONENTS[component_id]
        require_equal(row["wall_label"], wall_label, f"{component_id} wall_label")
        require_equal(row["support_kind"], support_kind, f"{component_id} support_kind")
        require_equal(row["orbit_id"], "Humbert_one_orbit", f"{component_id} orbit_id")
        require_equal(row["support_label"], "H_Hum", f"{component_id} support_label")
        require_equal(int_cell(row, "delta5_order"), order, f"{component_id} delta5_order")
        require_equal(bool_cell(row, "support_member"), True, f"{component_id} support_member")
        require_equal(row["multiplicity_status"], "simple_zero", f"{component_id} multiplicity_status")
    require_equal(seen, set(REQUIRED_COMPONENTS), "support component coverage")


def verify_divisor_relations(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "divisor_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"divisor_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"divisor_relations.csv: unexpected relation_id {relation_id}")
        require_equal(row["support_label"], "H_Hum", f"{relation_id} support_label")
        require_equal(row["expected_support_label"], "H_Hum", f"{relation_id} expected_support_label")
        require_equal(int_cell(row, "support_defect_rank"), 0, f"{relation_id} support_defect_rank")

        base_order = int_cell(row, "base_zero_order")
        exponent = int_cell(row, "form_exponent")
        relation_kind = row["relation_kind"]
        if relation_kind == "zero_divisor":
            computed = base_order * exponent
        elif relation_kind == "inverse_power_polar_divisor":
            if exponent >= 0:
                raise ValueError(f"{relation_id}: expected negative exponent for polar divisor")
            computed = base_order * (-exponent)
        elif relation_kind == "support_only":
            computed = 0
        else:
            raise ValueError(f"{relation_id}: unknown relation_kind {relation_kind!r}")
        require_equal(int_cell(row, "computed_order"), computed, f"{relation_id} computed_order")
        require_equal(int_cell(row, "computed_order"), int_cell(row, "expected_order"), f"{relation_id} expected_order")
        require_equal(int_cell(row, "multiplicity_defect_rank"), 0, f"{relation_id} multiplicity_defect_rank")
    require_equal(seen, REQUIRED_RELATIONS, "divisor relation coverage")


def verify_support_multiplicity_separation(rows: list[dict[str, str]]) -> None:
    if len(rows) != 1:
        raise ValueError("support_multiplicity_separation.csv: expected exactly one row")
    row = rows[0]
    check_row(row, "support_multiplicity_separation.csv")
    require_equal(row["separation_id"], "support_not_multiplicity", "separation_id")
    require_equal(row["support_statement"], "same_H_Hum_support", "support_statement")
    require_equal(row["multiplicity_statement"], "orders_1_and_2_distinct", "multiplicity_statement")
    require_equal(int_cell(row, "support_defect_rank"), 0, "support_defect_rank")
    require_equal(int_cell(row, "multiplicity_defect_rank"), 0, "multiplicity_defect_rank")
    require_equal(bool_cell(row, "collapsed"), False, "collapsed")


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
        verify_support_components(tables["support_components.csv"])
        verify_divisor_relations(tables["divisor_relations.csv"])
        verify_support_multiplicity_separation(tables["support_multiplicity_separation.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"HUMBERT_DIVISOR_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
