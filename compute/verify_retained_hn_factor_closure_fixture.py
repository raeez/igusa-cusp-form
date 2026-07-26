#!/usr/bin/env python3
"""Retained HN-factor-closure gate.

This verifier checks optimization row 179: every Harder--Narasimhan
factor of a retained finite HN word is again represented by a retained
finite substack.  It imports retained HN type bounds, retained class
bounds, retained semistable substacks, retained closed substacks, and
retained extension closure, then checks one row for every nonzero HN
factor occurrence.

It does not prove extension/flag stacks, subquotient closure in
compactified flag stacks, cosection atlases, transitions, Pfaffian
orientations, or protected traces.  Dual closure is checked by
verify_retained_dual_closure_fixture.py.
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
SUCCESS_STATUS = "RETAINED_HN_FACTOR_CLOSURE_VERIFIED"
EXPECTED_KIND = "retained_hn_factor_closure"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_hn_factor_closure")
DEFAULT_HN_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
DEFAULT_CLASS_FIXTURE = Path("certificates/moduli/retained_class_bounds")
DEFAULT_SEMISTABLE_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
DEFAULT_CLOSED_FIXTURE = Path("certificates/moduli/retained_closed_substacks")
DEFAULT_EXTENSION_FIXTURE = Path("certificates/moduli/retained_extension_closure")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})

HN_FACTOR_COLUMNS = (
    "type_id",
    "factor_object_id",
    "phase_num",
    "phase_den",
    "length_rank",
    "source_reference",
    "check_status",
    "notes",
)
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
SEMISTABLE_COLUMNS = (
    "substack_id",
    "type_id",
    "stability_id",
    "ambient_stack_id",
    "quot_postnikov_chart_id",
    "finite_type_status",
    "specialization_closed",
    "semistability_defect_rank",
    "boundedness_defect_rank",
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
EXTENSION_CLOSURE_COLUMNS = (
    "extension_closure_id",
    "window_id",
    "left_hn_type_id",
    "right_hn_type_id",
    "middle_hn_type_id",
    "middle_object_id",
    "extension_word_id",
    "retained_middle_term",
    "extension_closure_defect_rank",
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
REQUIRED_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "nonzero_hn_words_checked",
        "factor_types_imported",
        "class_rows_imported",
        "closed_substacks_imported",
        "extension_closure_imported",
        "hn_factor_rows_defined",
        "factor_occurrences_retained",
        "hn_factor_closure_defects_zero",
        "hn_factor_closure_mirrored",
        "extension_flag_stacks_not_proved",
        "subquotient_closure_not_proved",
        "dual_closure_not_proved",
        "finite_hall_stage_not_proved",
    }
)
COUNT_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "nonzero_hn_words_checked",
        "factor_types_imported",
        "class_rows_imported",
        "closed_substacks_imported",
        "extension_closure_imported",
        "hn_factor_rows_defined",
        "factor_occurrences_retained",
        "hn_factor_closure_defects_zero",
        "hn_factor_closure_mirrored",
    }
)
ZERO_RELATIONS = REQUIRED_RELATIONS - COUNT_RELATIONS
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "extension_flag_stacks",
        "subquotient_closure",
        "dual_closure",
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
    TableSpec("hn_factor_closure.csv", HN_FACTOR_CLOSURE_COLUMNS),
    TableSpec(
        "hn_factor_words.csv",
        (
            "hn_word_closure_id",
            "window_id",
            "hn_type_id",
            "object_id",
            "factor_count",
            "retained_factor_count",
            "all_factors_retained",
            "hn_factor_closure_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
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
    parser.add_argument("--semistable-fixture", type=Path, default=DEFAULT_SEMISTABLE_FIXTURE)
    parser.add_argument("--closed-fixture", type=Path, default=DEFAULT_CLOSED_FIXTURE)
    parser.add_argument("--extension-fixture", type=Path, default=DEFAULT_EXTENSION_FIXTURE)
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
    require_equal(manifest.get("hn_factor_closure"), True, "manifest hn_factor_closure")
    require_equal(manifest.get("hn_factor_closure_defects_zero"), True, "manifest hn_factor_closure_defects_zero")
    for key in (
        "extension_flag_stacks",
        "subquotient_closure",
        "dual_closure",
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
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
]:
    factors = rows_by_key(args.hn_fixture, TableSpec("hn_factor_types.csv", HN_FACTOR_COLUMNS), "type_id")
    objects = rows_by_key(args.hn_fixture, TableSpec("object_hn_type_bounds.csv", OBJECT_HN_COLUMNS), "hn_type_id")
    classes = rows_by_key(args.class_fixture, TableSpec("class_set.csv", CLASS_COLUMNS), "type_id")
    semistable = rows_by_key(
        args.semistable_fixture,
        TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS),
        "type_id",
    )
    closed_by_substack = rows_by_key(
        args.closed_fixture,
        TableSpec("retained_closed_substacks.csv", CLOSED_SUBSTACK_COLUMNS),
        "substack_id",
    )
    extensions = rows_by_key(
        args.extension_fixture,
        TableSpec("extension_closure.csv", EXTENSION_CLOSURE_COLUMNS),
        "extension_closure_id",
    )
    require_equal(set(factors), set(classes), "factor/class type coverage")
    require_equal(set(factors), set(semistable), "factor/semistable type coverage")
    require_equal({row["substack_id"] for row in semistable.values()}, set(closed_by_substack), "semistable/closed substack coverage")
    for type_id, row in factors.items():
        if int_cell(row, "length_rank") <= 0:
            raise ValueError(f"hn_factor_types.csv: nonpositive length rank for {type_id}")
    for hn_type_id, row in objects.items():
        require_equal(bool_cell(row, "within_factor_bound"), True, f"{hn_type_id} factor bound")
        require_equal(bool_cell(row, "within_height_bound"), True, f"{hn_type_id} height bound")
        require_equal(int_cell(row, "factor_count"), len(split_semicolon(row["type_sequence"])), f"{hn_type_id} factor count")
    for type_id, row in classes.items():
        require_equal(bool_cell(row, "retained_class"), True, f"{type_id} retained class")
    for type_id, row in semistable.items():
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite type")
        require_equal(bool_cell(row, "specialization_closed"), True, f"{type_id} specialization_closed")
        require_zero(int_cell(row, "semistability_defect_rank"), f"{type_id} semistability defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{type_id} boundedness defect")
    for substack_id, row in closed_by_substack.items():
        require_equal(bool_cell(row, "closed_in_ambient"), True, f"{substack_id} closed")
        require_equal(bool_cell(row, "finite_residual_inertia"), True, f"{substack_id} finite inertia")
        require_zero(int_cell(row, "closure_defect_rank"), f"{substack_id} closure defect")
        require_zero(int_cell(row, "inertia_defect_rank"), f"{substack_id} inertia defect")
    for extension_id, row in extensions.items():
        require_equal(bool_cell(row, "retained_middle_term"), True, f"{extension_id} retained middle")
        require_zero(int_cell(row, "extension_closure_defect_rank"), f"{extension_id} extension defect")
    return factors, objects, classes, semistable, closed_by_substack, extensions


def verify_factor_rows(
    rows: list[dict[str, str]],
    factors: dict[str, dict[str, str]],
    objects: dict[str, dict[str, str]],
    classes: dict[str, dict[str, str]],
    semistable: dict[str, dict[str, str]],
    closed_by_substack: dict[str, dict[str, str]],
) -> tuple[dict[str, list[dict[str, str]]], int]:
    by_word: dict[str, list[dict[str, str]]] = {hn_type_id: [] for hn_type_id in objects}
    seen: set[str] = set()
    for row in rows:
        check_row(row, "hn_factor_closure.csv")
        factor_closure_id = row["factor_closure_id"]
        if factor_closure_id in seen:
            raise ValueError(f"hn_factor_closure.csv: duplicate factor_closure_id {factor_closure_id}")
        seen.add(factor_closure_id)
        hn_type_id = row["hn_type_id"]
        if hn_type_id not in objects:
            raise ValueError(f"hn_factor_closure.csv: unknown hn_type_id {hn_type_id}")
        object_row = objects[hn_type_id]
        require_equal(row["object_id"], object_row["object_id"], f"{factor_closure_id} object")
        sequence = split_semicolon(object_row["type_sequence"])
        position = int_cell(row, "factor_position")
        if position < 1 or position > len(sequence):
            raise ValueError(f"{factor_closure_id}: factor_position outside HN word")
        factor_type_id = row["factor_type_id"]
        require_equal(sequence[position - 1], factor_type_id, f"{factor_closure_id} factor sequence")
        factor = factors.get(factor_type_id)
        if factor is None:
            raise ValueError(f"{factor_closure_id}: unknown factor_type_id {factor_type_id}")
        require_equal(row["factor_object_id"], factor["factor_object_id"], f"{factor_closure_id} factor object")
        class_row = classes[factor_type_id]
        semistable_row = semistable[factor_type_id]
        closed = closed_by_substack[semistable_row["substack_id"]]
        require_equal(row["factor_substack_id"], semistable_row["substack_id"], f"{factor_closure_id} substack")
        require_equal(row["retained_class_id"], class_row["class_id"], f"{factor_closure_id} class")
        require_equal(row["retained_closed_substack_id"], closed["closed_substack_id"], f"{factor_closure_id} closed substack")
        require_equal(bool_cell(row, "factor_retained"), True, f"{factor_closure_id} retained factor")
        require_zero(int_cell(row, "hn_factor_closure_defect_rank"), f"{factor_closure_id} factor closure defect")
        by_word[hn_type_id].append(row)
    expected_occurrences = sum(int_cell(row, "factor_count") for row in objects.values())
    require_equal(len(rows), expected_occurrences, "HN factor occurrence count")
    return by_word, expected_occurrences


def verify_word_rows(
    rows: list[dict[str, str]],
    objects: dict[str, dict[str, str]],
    factor_rows_by_word: dict[str, list[dict[str, str]]],
) -> int:
    seen: set[str] = set()
    nonzero_count = 0
    for row in rows:
        check_row(row, "hn_factor_words.csv")
        hn_type_id = row["hn_type_id"]
        if hn_type_id in seen:
            raise ValueError(f"hn_factor_words.csv: duplicate hn_type_id {hn_type_id}")
        seen.add(hn_type_id)
        object_row = objects.get(hn_type_id)
        if object_row is None:
            raise ValueError(f"hn_factor_words.csv: unknown hn_type_id {hn_type_id}")
        require_equal(row["window_id"], object_row["window_id"], f"{hn_type_id} window")
        require_equal(row["object_id"], object_row["object_id"], f"{hn_type_id} object")
        factor_count = int_cell(object_row, "factor_count")
        retained_count = len(factor_rows_by_word[hn_type_id])
        require_equal(int_cell(row, "factor_count"), factor_count, f"{hn_type_id} factor_count")
        require_equal(int_cell(row, "retained_factor_count"), retained_count, f"{hn_type_id} retained_factor_count")
        require_equal(retained_count, factor_count, f"{hn_type_id} retained coverage")
        require_equal(bool_cell(row, "all_factors_retained"), True, f"{hn_type_id} all_factors_retained")
        require_zero(int_cell(row, "hn_factor_closure_defect_rank"), f"{hn_type_id} word defect")
        if factor_count > 0:
            nonzero_count += 1
    require_equal(seen, set(objects), "HN factor word coverage")
    return nonzero_count


def verify_relations(
    rows: list[dict[str, str]],
    hn_word_count: int,
    nonzero_word_count: int,
    factor_type_count: int,
    class_count: int,
    closed_substack_count: int,
    extension_count: int,
    factor_occurrence_count: int,
) -> None:
    relation_values = {
        "hn_type_words_imported": hn_word_count,
        "nonzero_hn_words_checked": nonzero_word_count,
        "factor_types_imported": factor_type_count,
        "class_rows_imported": class_count,
        "closed_substacks_imported": closed_substack_count,
        "extension_closure_imported": extension_count,
        "hn_factor_rows_defined": factor_occurrence_count,
        "factor_occurrences_retained": factor_occurrence_count,
        "hn_factor_closure_defects_zero": factor_occurrence_count,
        "hn_factor_closure_mirrored": factor_occurrence_count,
        "extension_flag_stacks_not_proved": 0,
        "subquotient_closure_not_proved": 0,
        "dual_closure_not_proved": 0,
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
    mirrored = read_table(finite_moduli_fixture, TableSpec("hn_factor_closure.csv", HN_FACTOR_CLOSURE_COLUMNS))
    expected = sorted(rows, key=lambda row: row["factor_closure_id"])
    actual = sorted(mirrored, key=lambda row: row["factor_closure_id"])
    require_equal(actual, expected, "finite-moduli hn_factor_closure mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        factors, objects, classes, semistable, closed_by_substack, extensions = load_inputs(args)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        factor_rows_by_word, factor_occurrences = verify_factor_rows(
            tables["hn_factor_closure.csv"],
            factors,
            objects,
            classes,
            semistable,
            closed_by_substack,
        )
        nonzero_words = verify_word_rows(tables["hn_factor_words.csv"], objects, factor_rows_by_word)
        verify_relations(
            tables["formal_relations.csv"],
            len(objects),
            nonzero_words,
            len(factors),
            len(classes),
            len(closed_by_substack),
            len(extensions),
            factor_occurrences,
        )
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["hn_factor_closure.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_HN_FACTOR_CLOSURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
