#!/usr/bin/env python3
"""Retained dual-closure gate.

This verifier checks optimization row 180: when duals are used, the
retained finite HN window is closed under the supplied duality
involution.  It imports retained HN type bounds, retained class bounds,
retained closed substacks, and retained HN-factor closure, then checks
that factor duality is involutive and that each HN word maps to the
reverse of the factorwise dual word.

It does not construct extension/flag stacks, subquotient closure in
flag stacks, cosection atlases, transitions, Pfaffian orientations, or
protected traces.
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
SUCCESS_STATUS = "RETAINED_DUAL_CLOSURE_VERIFIED"
EXPECTED_KIND = "retained_dual_closure"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_dual_closure")
DEFAULT_HN_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
DEFAULT_CLASS_FIXTURE = Path("certificates/moduli/retained_class_bounds")
DEFAULT_CLOSED_FIXTURE = Path("certificates/moduli/retained_closed_substacks")
DEFAULT_HN_FACTOR_FIXTURE = Path("certificates/moduli/retained_hn_factor_closure")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})

OBJECT_HN_COLUMNS = (
    "object_id",
    "window_id",
    "hn_type_id",
    "type_sequence",
    "factor_count",
    "hn_height",
    "length_sum",
    "phase_sequence",
    "within_factor_bound",
    "within_height_bound",
    "source_reference",
    "check_status",
    "notes",
)
CLASS_COLUMNS = (
    "class_id",
    "window_id",
    "type_id",
    "charge_id",
    "substack_id",
    "hilbert_polynomial_id",
    "amplitude_bounds",
    "regularity_bound",
    "retained_class",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
CLOSED_SUBSTACK_COLUMNS = (
    "closed_substack_id",
    "substack_id",
    "translation_rigidification_id",
    "closed_embedding_id",
    "closed_in_ambient",
    "finite_type_status",
    "finite_residual_inertia",
    "closure_defect_rank",
    "inertia_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
HN_FACTOR_CLOSURE_COLUMNS = (
    "factor_closure_id",
    "window_id",
    "hn_type_id",
    "object_id",
    "factor_position",
    "factor_type_id",
    "factor_object_id",
    "factor_substack_id",
    "retained_class_id",
    "retained_closed_substack_id",
    "factor_retained",
    "hn_factor_closure_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
TYPE_DUAL_COLUMNS = (
    "type_dual_id",
    "type_id",
    "dual_type_id",
    "dual_class_id",
    "dual_substack_id",
    "dual_closed_substack_id",
    "retained_dual_type",
    "dual_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
DUAL_CLOSURE_COLUMNS = (
    "dual_closure_id",
    "window_id",
    "hn_type_id",
    "object_id",
    "type_sequence",
    "dual_hn_type_id",
    "dual_object_id",
    "dual_type_sequence",
    "reversed_factorwise_dual_sequence",
    "retained_dual",
    "dual_closure_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "class_rows_imported",
        "closed_substacks_imported",
        "hn_factor_closure_imported",
        "type_dual_rows_defined",
        "dual_hn_word_rows_defined",
        "type_duality_involutive",
        "hn_word_duality_involutive",
        "factorwise_reversal_verified",
        "dual_closure_defects_zero",
        "dual_closure_mirrored",
        "extension_flag_stacks_not_proved",
        "subquotient_closure_not_proved",
        "finite_hall_stage_not_proved",
    }
)
COUNT_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "class_rows_imported",
        "closed_substacks_imported",
        "hn_factor_closure_imported",
        "type_dual_rows_defined",
        "dual_hn_word_rows_defined",
        "type_duality_involutive",
        "hn_word_duality_involutive",
        "factorwise_reversal_verified",
        "dual_closure_defects_zero",
        "dual_closure_mirrored",
    }
)
ZERO_RELATIONS = REQUIRED_RELATIONS - COUNT_RELATIONS
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "extension_flag_stacks",
        "subquotient_closure",
        "cosection_atlas",
        "transitions",
        "scalar_firewall",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec("type_duals.csv", TYPE_DUAL_COLUMNS),
    TableSpec("dual_closure.csv", DUAL_CLOSURE_COLUMNS),
    TableSpec(
        "formal_relations.csv",
        (
            "relation_id",
            "relation_kind",
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
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--hn-fixture", type=Path, default=DEFAULT_HN_FIXTURE)
    parser.add_argument("--class-fixture", type=Path, default=DEFAULT_CLASS_FIXTURE)
    parser.add_argument("--closed-fixture", type=Path, default=DEFAULT_CLOSED_FIXTURE)
    parser.add_argument("--hn-factor-fixture", type=Path, default=DEFAULT_HN_FACTOR_FIXTURE)
    parser.add_argument("--finite-moduli-fixture", type=Path, default=DEFAULT_FINITE_MODULI_FIXTURE)
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


def split_semicolon(value: str) -> list[str]:
    if value == "empty":
        return []
    return [part for part in value.split(";") if part]


def join_sequence(parts: list[str]) -> str:
    return "empty" if not parts else ";".join(parts)


def check_row(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    if not row.get("source_reference", row.get("proof_reference", "")).strip():
        raise ValueError(f"{table_name}: missing source reference: {row}")
    haystack = " ".join(row.values()).lower()
    for token in FORBIDDEN_TOKENS:
        if token in haystack:
            raise ValueError(f"{table_name}: forbidden token {token!r} in {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_zero(value: int, label: str) -> None:
    if value != 0:
        raise ValueError(f"{label}: expected 0, got {value}")


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("moduli_kind"), EXPECTED_KIND, "manifest moduli_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("dual_closure"), True, "manifest dual_closure")
    require_equal(manifest.get("dual_closure_defects_zero"), True, "manifest dual_closure_defects_zero")
    for key in (
        "extension_flag_stacks",
        "subquotient_closure",
        "cosection_atlas",
        "transitions",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_equal(manifest.get(key), False, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def rows_by_key(fixture: Path, spec: TableSpec, key: str) -> dict[str, dict[str, str]]:
    rows = read_table(fixture, spec)
    by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, spec.path)
        value = row[key]
        if value in by_key:
            raise ValueError(f"{spec.path}: duplicate {key} {value}")
        by_key[value] = row
    return by_key


def load_inputs(args: argparse.Namespace) -> tuple[
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
]:
    objects = rows_by_key(args.hn_fixture, TableSpec("object_hn_type_bounds.csv", OBJECT_HN_COLUMNS), "hn_type_id")
    classes = rows_by_key(args.class_fixture, TableSpec("class_set.csv", CLASS_COLUMNS), "type_id")
    closed = rows_by_key(
        args.closed_fixture,
        TableSpec("retained_closed_substacks.csv", CLOSED_SUBSTACK_COLUMNS),
        "closed_substack_id",
    )
    factor_rows = rows_by_key(
        args.hn_factor_fixture,
        TableSpec("hn_factor_closure.csv", HN_FACTOR_CLOSURE_COLUMNS),
        "factor_closure_id",
    )
    for hn_type_id, row in objects.items():
        require_equal(bool_cell(row, "within_factor_bound"), True, f"{hn_type_id} factor bound")
        require_equal(bool_cell(row, "within_height_bound"), True, f"{hn_type_id} height bound")
    for type_id, row in classes.items():
        require_equal(bool_cell(row, "retained_class"), True, f"{type_id} retained class")
    for closed_id, row in closed.items():
        require_equal(bool_cell(row, "closed_in_ambient"), True, f"{closed_id} closed")
        require_equal(bool_cell(row, "finite_residual_inertia"), True, f"{closed_id} finite inertia")
        require_zero(int_cell(row, "closure_defect_rank"), f"{closed_id} closure defect")
        require_zero(int_cell(row, "inertia_defect_rank"), f"{closed_id} inertia defect")
    for factor_id, row in factor_rows.items():
        require_equal(bool_cell(row, "factor_retained"), True, f"{factor_id} retained")
        require_zero(int_cell(row, "hn_factor_closure_defect_rank"), f"{factor_id} factor defect")
    return objects, classes, closed, factor_rows


def verify_type_duals(
    rows: list[dict[str, str]],
    classes: dict[str, dict[str, str]],
    closed: dict[str, dict[str, str]],
) -> dict[str, str]:
    dual_by_type: dict[str, str] = {}
    for row in rows:
        check_row(row, "type_duals.csv")
        type_id = row["type_id"]
        dual_type_id = row["dual_type_id"]
        if type_id in dual_by_type:
            raise ValueError(f"type_duals.csv: duplicate type_id {type_id}")
        if type_id not in classes or dual_type_id not in classes:
            raise ValueError(f"type_duals.csv: unknown type dual {type_id}->{dual_type_id}")
        dual_class = classes[dual_type_id]
        require_equal(row["dual_class_id"], dual_class["class_id"], f"{type_id} dual class")
        require_equal(row["dual_substack_id"], dual_class["substack_id"], f"{type_id} dual substack")
        if row["dual_closed_substack_id"] not in closed:
            raise ValueError(f"type_duals.csv: unknown closed substack {row['dual_closed_substack_id']}")
        require_equal(
            closed[row["dual_closed_substack_id"]]["substack_id"],
            row["dual_substack_id"],
            f"{type_id} dual closed substack",
        )
        require_equal(bool_cell(row, "retained_dual_type"), True, f"{type_id} retained dual")
        require_zero(int_cell(row, "dual_defect_rank"), f"{type_id} dual defect")
        dual_by_type[type_id] = dual_type_id
    require_equal(set(dual_by_type), set(classes), "type dual coverage")
    for type_id, dual_type_id in dual_by_type.items():
        require_equal(dual_by_type[dual_type_id], type_id, f"{type_id} dual involution")
    return dual_by_type


def verify_dual_closure_rows(
    rows: list[dict[str, str]],
    objects: dict[str, dict[str, str]],
    dual_by_type: dict[str, str],
) -> dict[str, str]:
    dual_by_hn_type: dict[str, str] = {}
    for row in rows:
        check_row(row, "dual_closure.csv")
        hn_type_id = row["hn_type_id"]
        dual_hn_type_id = row["dual_hn_type_id"]
        if hn_type_id in dual_by_hn_type:
            raise ValueError(f"dual_closure.csv: duplicate hn_type_id {hn_type_id}")
        if hn_type_id not in objects or dual_hn_type_id not in objects:
            raise ValueError(f"dual_closure.csv: unknown HN dual {hn_type_id}->{dual_hn_type_id}")
        source = objects[hn_type_id]
        target = objects[dual_hn_type_id]
        require_equal(row["window_id"], source["window_id"], f"{hn_type_id} window")
        require_equal(row["object_id"], source["object_id"], f"{hn_type_id} object")
        require_equal(row["type_sequence"], source["type_sequence"], f"{hn_type_id} source sequence")
        require_equal(row["dual_object_id"], target["object_id"], f"{hn_type_id} dual object")
        require_equal(row["dual_type_sequence"], target["type_sequence"], f"{hn_type_id} dual sequence")
        source_sequence = split_semicolon(source["type_sequence"])
        reversed_dual = [dual_by_type[type_id] for type_id in reversed(source_sequence)]
        reversed_dual_text = join_sequence(reversed_dual)
        require_equal(
            row["reversed_factorwise_dual_sequence"],
            reversed_dual_text,
            f"{hn_type_id} displayed reversed dual",
        )
        require_equal(target["type_sequence"], reversed_dual_text, f"{hn_type_id} target sequence")
        require_equal(bool_cell(row, "retained_dual"), True, f"{hn_type_id} retained dual")
        require_zero(int_cell(row, "dual_closure_defect_rank"), f"{hn_type_id} dual closure defect")
        dual_by_hn_type[hn_type_id] = dual_hn_type_id
    require_equal(set(dual_by_hn_type), set(objects), "HN dual coverage")
    for hn_type_id, dual_hn_type_id in dual_by_hn_type.items():
        require_equal(dual_by_hn_type[dual_hn_type_id], hn_type_id, f"{hn_type_id} HN dual involution")
    return dual_by_hn_type


def verify_relations(
    rows: list[dict[str, str]],
    hn_word_count: int,
    class_count: int,
    closed_count: int,
    factor_count: int,
    type_dual_count: int,
    dual_word_count: int,
) -> None:
    relation_values = {
        "hn_type_words_imported": hn_word_count,
        "class_rows_imported": class_count,
        "closed_substacks_imported": closed_count,
        "hn_factor_closure_imported": factor_count,
        "type_dual_rows_defined": type_dual_count,
        "dual_hn_word_rows_defined": dual_word_count,
        "type_duality_involutive": type_dual_count,
        "hn_word_duality_involutive": dual_word_count,
        "factorwise_reversal_verified": dual_word_count,
        "dual_closure_defects_zero": dual_word_count,
        "dual_closure_mirrored": dual_word_count,
        "extension_flag_stacks_not_proved": 0,
        "subquotient_closure_not_proved": 0,
        "finite_hall_stage_not_proved": 0,
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        computed = int_cell(row, "computed_value")
        expected = int_cell(row, "expected_value")
        require_equal(computed, expected, f"{relation_id} computed/expected")
        require_equal(computed, relation_values[relation_id], f"{relation_id} actual value")
        if relation_id in ZERO_RELATIONS:
            require_zero(computed, f"{relation_id} computed")
        require_zero(int_cell(row, "defect_rank"), f"{relation_id} defect")
        seen.add(relation_id)
    require_equal(seen, REQUIRED_RELATIONS, "formal relation coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"scalar_firewall.csv: duplicate substitute {substitute}")
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_zero(int_cell(row, "defect_rank"), f"{substitute} defect")
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "firewall coverage")


def verify_finite_moduli_mirror(finite_moduli_fixture: Path, rows: list[dict[str, str]]) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("dual_closure.csv", DUAL_CLOSURE_COLUMNS))
    expected = sorted(rows, key=lambda row: row["dual_closure_id"])
    actual = sorted(mirrored, key=lambda row: row["dual_closure_id"])
    require_equal(actual, expected, "finite-moduli dual_closure mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        objects, classes, closed, factor_rows = load_inputs(args)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        dual_by_type = verify_type_duals(tables["type_duals.csv"], classes, closed)
        dual_by_hn_type = verify_dual_closure_rows(tables["dual_closure.csv"], objects, dual_by_type)
        verify_relations(
            tables["formal_relations.csv"],
            len(objects),
            len(classes),
            len(closed),
            len(factor_rows),
            len(dual_by_type),
            len(dual_by_hn_type),
        )
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["dual_closure.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_DUAL_CLOSURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
