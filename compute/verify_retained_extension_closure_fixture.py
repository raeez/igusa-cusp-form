#!/usr/bin/env python3
"""Retained extension-closure gate.

This verifier checks optimization row 178: the retained finite HN
window is closed under the supplied extension words.  It imports the
retained HN type-bound packet and the retained closed-substack packet,
then checks nonempty binary extension rows whose middle HN type remains
inside the retained finite HN word set with zero extension-closure
defect.

It does not construct extension stacks, two-step flag stacks, closure
under HN factors, closure under duals, cosection atlases, transitions,
Pfaffian orientations, or protected traces.
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
SUCCESS_STATUS = "RETAINED_EXTENSION_CLOSURE_VERIFIED"
EXPECTED_KIND = "retained_extension_closure"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_extension_closure")
DEFAULT_HN_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
DEFAULT_CLOSED_FIXTURE = Path("certificates/moduli/retained_closed_substacks")
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
CLOSURE_BOUND_COLUMNS = (
    "closure_id",
    "window_id",
    "closure_kind",
    "source_type_ids",
    "target_hn_type_id",
    "closure_defect_rank",
    "source_reference",
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
REQUIRED_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "closed_substacks_imported",
        "closure_bounds_imported",
        "binary_extension_rows_defined",
        "retained_middle_terms_defined",
        "middle_terms_inside_retained_window",
        "extension_closure_defects_zero",
        "extension_closure_mirrored",
        "extension_flag_stacks_not_proved",
        "hn_factor_closure_not_proved",
        "dual_closure_not_proved",
        "finite_hall_stage_not_proved",
    }
)
COUNT_RELATIONS = frozenset(
    {
        "hn_type_words_imported",
        "closed_substacks_imported",
        "closure_bounds_imported",
        "binary_extension_rows_defined",
        "retained_middle_terms_defined",
        "middle_terms_inside_retained_window",
        "extension_closure_defects_zero",
        "extension_closure_mirrored",
    }
)
ZERO_RELATIONS = REQUIRED_RELATIONS - COUNT_RELATIONS
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "extension_flag_stacks",
        "two_step_flag_stacks",
        "hn_factor_closure",
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
    TableSpec("extension_closure.csv", EXTENSION_CLOSURE_COLUMNS),
    TableSpec(
        "extension_middle_terms.csv",
        (
            "middle_term_id",
            "middle_hn_type_id",
            "middle_object_id",
            "source_extension_closure_ids",
            "retained_middle_term",
            "middle_defect_rank",
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
    parser.add_argument("--closed-fixture", type=Path, default=DEFAULT_CLOSED_FIXTURE)
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
    require_equal(manifest.get("extension_closure"), True, "manifest extension_closure")
    require_equal(manifest.get("extension_closure_defects_zero"), True, "manifest extension_closure_defects_zero")
    for key in (
        "extension_flag_stacks",
        "two_step_flag_stacks",
        "hn_factor_closure",
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


def load_inputs(
    hn_fixture: Path,
    closed_fixture: Path,
) -> tuple[
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
]:
    factors = rows_by_key(hn_fixture, TableSpec("hn_factor_types.csv", HN_FACTOR_COLUMNS), "type_id")
    objects = rows_by_key(hn_fixture, TableSpec("object_hn_type_bounds.csv", OBJECT_HN_COLUMNS), "hn_type_id")
    closure_bounds = rows_by_key(hn_fixture, TableSpec("closure_bounds.csv", CLOSURE_BOUND_COLUMNS), "closure_id")
    closed_substacks = rows_by_key(
        closed_fixture,
        TableSpec("retained_closed_substacks.csv", CLOSED_SUBSTACK_COLUMNS),
        "closed_substack_id",
    )
    if len(closed_substacks) == 0:
        raise ValueError("retained closed-substack input is empty")
    for type_id, row in factors.items():
        if int_cell(row, "length_rank") <= 0:
            raise ValueError(f"hn_factor_types.csv: nonpositive length rank in {type_id}")
    for hn_type_id, row in objects.items():
        require_equal(bool_cell(row, "within_factor_bound"), True, f"{hn_type_id} factor bound")
        require_equal(bool_cell(row, "within_height_bound"), True, f"{hn_type_id} height bound")
    for closure_id, row in closure_bounds.items():
        require_zero(int_cell(row, "closure_defect_rank"), f"{closure_id} closure defect")
        target = row["target_hn_type_id"]
        if target not in objects:
            raise ValueError(f"closure_bounds.csv: target {target} is not retained")
        for source in split_semicolon(row["source_type_ids"]):
            if source not in factors:
                raise ValueError(f"closure_bounds.csv: source factor {source} is not retained")
    return factors, objects, closure_bounds, closed_substacks


def verify_extension_closure_rows(
    rows: list[dict[str, str]],
    objects: dict[str, dict[str, str]],
    closure_bounds: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_id: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "extension_closure.csv")
        closure_id = row["extension_closure_id"]
        if closure_id in by_id:
            raise ValueError(f"extension_closure.csv: duplicate extension_closure_id {closure_id}")
        left = row["left_hn_type_id"]
        right = row["right_hn_type_id"]
        middle = row["middle_hn_type_id"]
        for hn_type_id in (left, right, middle):
            if hn_type_id not in objects:
                raise ValueError(f"extension_closure.csv: unknown HN type {hn_type_id}")
        middle_object = objects[middle]["object_id"]
        require_equal(row["middle_object_id"], middle_object, f"{closure_id} middle object")
        left_sequence = split_semicolon(objects[left]["type_sequence"])
        right_sequence = split_semicolon(objects[right]["type_sequence"])
        middle_sequence = split_semicolon(objects[middle]["type_sequence"])
        require_equal(left_sequence + right_sequence, middle_sequence, f"{closure_id} HN word concatenation")
        extension_word = closure_bounds.get(row["extension_word_id"])
        if extension_word is None:
            raise ValueError(f"extension_closure.csv: unknown extension_word_id {row['extension_word_id']}")
        if extension_word["closure_kind"] != "extension_word":
            raise ValueError(f"{closure_id}: extension_word_id does not point to extension_word")
        require_equal(extension_word["target_hn_type_id"], middle, f"{closure_id} extension target")
        require_equal(
            split_semicolon(extension_word["source_type_ids"]),
            middle_sequence,
            f"{closure_id} extension-bound word",
        )
        require_equal(bool_cell(row, "retained_middle_term"), True, f"{closure_id} retained_middle_term")
        require_zero(int_cell(row, "extension_closure_defect_rank"), f"{closure_id} extension defect")
        by_id[closure_id] = row
    if len(by_id) < 4:
        raise ValueError("extension_closure.csv: expected at least four nonvacuous binary extension rows")
    return by_id


def verify_middle_terms(
    rows: list[dict[str, str]],
    extension_rows: dict[str, dict[str, str]],
    objects: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_middle: dict[str, dict[str, str]] = {}
    covered_extension_ids: set[str] = set()
    for row in rows:
        check_row(row, "extension_middle_terms.csv")
        middle = row["middle_hn_type_id"]
        if middle in by_middle:
            raise ValueError(f"extension_middle_terms.csv: duplicate middle_hn_type_id {middle}")
        if middle not in objects:
            raise ValueError(f"extension_middle_terms.csv: unknown middle_hn_type_id {middle}")
        require_equal(row["middle_object_id"], objects[middle]["object_id"], f"{middle} middle object")
        require_equal(bool_cell(row, "retained_middle_term"), True, f"{middle} retained")
        require_zero(int_cell(row, "middle_defect_rank"), f"{middle} middle defect")
        source_ids = set(split_semicolon(row["source_extension_closure_ids"]))
        if not source_ids:
            raise ValueError(f"extension_middle_terms.csv: no source extensions for {middle}")
        for extension_id in source_ids:
            extension = extension_rows.get(extension_id)
            if extension is None:
                raise ValueError(f"extension_middle_terms.csv: unknown source extension {extension_id}")
            require_equal(extension["middle_hn_type_id"], middle, f"{extension_id} middle")
        covered_extension_ids |= source_ids
        by_middle[middle] = row
    require_equal(covered_extension_ids, set(extension_rows), "middle-term extension coverage")
    return by_middle


def verify_relations(
    rows: list[dict[str, str]],
    hn_type_count: int,
    closed_substack_count: int,
    closure_bound_count: int,
    extension_count: int,
    middle_count: int,
) -> None:
    relation_values = {
        "hn_type_words_imported": hn_type_count,
        "closed_substacks_imported": closed_substack_count,
        "closure_bounds_imported": closure_bound_count,
        "binary_extension_rows_defined": extension_count,
        "retained_middle_terms_defined": middle_count,
        "middle_terms_inside_retained_window": middle_count,
        "extension_closure_defects_zero": extension_count,
        "extension_closure_mirrored": extension_count,
        "extension_flag_stacks_not_proved": 0,
        "hn_factor_closure_not_proved": 0,
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
        expected_value = relation_values[relation_id]
        computed = int_cell(row, "computed_value")
        expected = int_cell(row, "expected_value")
        require_equal(computed, expected, f"{relation_id} computed/expected")
        require_equal(computed, expected_value, f"{relation_id} actual value")
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
    mirrored = read_table(finite_moduli_fixture, TableSpec("extension_closure.csv", EXTENSION_CLOSURE_COLUMNS))
    expected = sorted(rows, key=lambda row: row["extension_closure_id"])
    actual = sorted(mirrored, key=lambda row: row["extension_closure_id"])
    require_equal(actual, expected, "finite-moduli extension_closure mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        _factors, objects, closure_bounds, closed_substacks = load_inputs(
            args.hn_fixture,
            args.closed_fixture,
        )
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        extension_rows = verify_extension_closure_rows(
            tables["extension_closure.csv"],
            objects,
            closure_bounds,
        )
        middle_terms = verify_middle_terms(tables["extension_middle_terms.csv"], extension_rows, objects)
        extension_bound_count = sum(
            1 for row in closure_bounds.values() if row["closure_kind"] == "extension_word"
        )
        verify_relations(
            tables["formal_relations.csv"],
            len(objects),
            len(closed_substacks),
            extension_bound_count,
            len(extension_rows),
            len(middle_terms),
        )
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["extension_closure.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_EXTENSION_CLOSURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
