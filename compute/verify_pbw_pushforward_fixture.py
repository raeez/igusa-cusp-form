#!/usr/bin/env python3
"""Finite PBW-filtration pushforward gate.

This verifier checks the finite filtered-vector-space statement that
pushforward along the additive normal-ordered Gram grading preserves a
supplied PBW filtration:

    F_{<=d}(phi_* U)_gamma =
        direct sum_{phi(hat_gamma)=gamma} F_{<=d}U_{hat_gamma}.

It also checks that the finite associated-graded dimensions are
computed as successive filtration quotients.  The packet does not prove
the compact-source PBW comparison, the target PBW comparison, no-extra
relations, primitive recognition, Pfaffian orientations, or protected
traces.
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
SUCCESS_STATUS = "PBW_PUSHFORWARD_VERIFIED"
EXPECTED_KIND = "pbw_pushforward_formal_filtered_vector_space"
DEFAULT_FIXTURE = Path("certificates/charge/pbw_pushforward")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "source_block_count",
        "pushforward_filtered_rows",
        "associated_graded_rows",
        "cumulative_monotone_degrees",
        "pbw_filtration_preserved",
        "associated_graded_from_quotients",
        "source_pbw_comparison_not_proved",
        "target_pbw_comparison_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "source_pbw_comparison",
        "target_pbw_comparison",
        "compact_source",
        "primitive_recognition",
        "no_extra_relations",
        "universal_enveloping_isomorphism",
        "pfaffian_orientation",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "source_filtered_blocks.csv",
        (
            "block_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "pbw_level",
            "dimension",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pushforward_filtered_sums.csv",
        (
            "pushforward_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "pbw_level",
            "source_block_ids",
            "level_dimension",
            "cumulative_dimension",
            "filtration_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "associated_graded_rows.csv",
        (
            "graded_id",
            "degree_id",
            "pbw_level",
            "computed_graded_dimension",
            "expected_graded_dimension",
            "graded_defect_rank",
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


Triple = tuple[int, int, int]
Block = tuple[str, Triple, int, int]
PushRow = tuple[int, int, int]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
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


def require_zero(value: int, label: str) -> None:
    if value != 0:
        raise ValueError(f"{label}: expected 0, got {value}")


def triple_from_row(row: dict[str, str]) -> Triple:
    return int_cell(row, "degree_n"), int_cell(row, "degree_l"), int_cell(row, "degree_m")


def split_ids(cell: str) -> list[str]:
    ids = [part.strip() for part in cell.split(";") if part.strip()]
    if not ids:
        raise ValueError(f"empty source_block_ids cell {cell!r}")
    return ids


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("normal_ordered_pbw_pushforward"), True, "manifest normal_ordered_pbw_pushforward")
    require_equal(manifest.get("pbw_filtration_preserved"), True, "manifest pbw_filtration_preserved")
    require_equal(manifest.get("source_pbw_comparison"), False, "manifest source_pbw_comparison")
    require_equal(manifest.get("target_pbw_comparison"), False, "manifest target_pbw_comparison")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("no_extra_relations"), False, "manifest no_extra_relations")
    require_equal(
        manifest.get("universal_enveloping_isomorphism"),
        False,
        "manifest universal_enveloping_isomorphism",
    )
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_source_blocks(rows: list[dict[str, str]]) -> dict[str, Block]:
    blocks: dict[str, Block] = {}
    for row in rows:
        check_row(row, "source_filtered_blocks.csv")
        block_id = row["block_id"]
        if block_id in blocks:
            raise ValueError(f"source_filtered_blocks.csv: duplicate block_id {block_id}")
        level = int_cell(row, "pbw_level")
        dimension = int_cell(row, "dimension")
        if level < 0:
            raise ValueError(f"source_filtered_blocks.csv: negative PBW level in {row}")
        if dimension <= 0:
            raise ValueError(f"source_filtered_blocks.csv: nonpositive dimension in {row}")
        blocks[block_id] = (row["degree_id"], triple_from_row(row), level, dimension)
    return blocks


def verify_pushforward_rows(
    rows: list[dict[str, str]],
    blocks: dict[str, Block],
) -> tuple[dict[tuple[str, int], PushRow], int]:
    by_degree_level: dict[tuple[str, int], list[tuple[str, int]]] = {}
    degree_triples: dict[str, Triple] = {}
    for block_id, (degree_id, triple, level, dimension) in blocks.items():
        by_degree_level.setdefault((degree_id, level), []).append((block_id, dimension))
        if degree_id in degree_triples:
            require_equal(triple, degree_triples[degree_id], f"{degree_id} triple")
        degree_triples[degree_id] = triple

    seen_keys: set[tuple[str, int]] = set()
    pushed: dict[tuple[str, int], PushRow] = {}
    monotone: dict[str, list[tuple[int, int]]] = {}
    used_blocks: set[str] = set()
    for row in rows:
        check_row(row, "pushforward_filtered_sums.csv")
        degree_id = row["degree_id"]
        level = int_cell(row, "pbw_level")
        key = (degree_id, level)
        if key in seen_keys:
            raise ValueError(f"pushforward_filtered_sums.csv: duplicate degree/level {key}")
        seen_keys.add(key)
        require_equal(triple_from_row(row), degree_triples[degree_id], f"{degree_id} pushforward triple")
        expected_ids_dims = sorted(by_degree_level.get(key, []))
        actual_ids = sorted(split_ids(row["source_block_ids"]))
        require_equal(actual_ids, [block_id for block_id, _ in expected_ids_dims], f"{key} source ids")
        used_blocks.update(actual_ids)
        level_dimension = sum(dimension for _, dimension in expected_ids_dims)
        cumulative_dimension = sum(
            dimension
            for (source_degree_id, source_level), block_dims in by_degree_level.items()
            if source_degree_id == degree_id and source_level <= level
            for _, dimension in block_dims
        )
        require_equal(int_cell(row, "level_dimension"), level_dimension, f"{key} level dimension")
        require_equal(int_cell(row, "cumulative_dimension"), cumulative_dimension, f"{key} cumulative dimension")
        require_zero(int_cell(row, "filtration_defect_rank"), f"{key} filtration defect")
        pushed[key] = (level_dimension, cumulative_dimension, 0)
        monotone.setdefault(degree_id, []).append((level, cumulative_dimension))

    require_equal(used_blocks, set(blocks), "source block coverage")
    for degree_id, entries in monotone.items():
        previous_level = -1
        previous_dimension = -1
        for level, cumulative_dimension in sorted(entries):
            if level <= previous_level:
                raise ValueError(f"{degree_id}: PBW levels are not increasing")
            if cumulative_dimension < previous_dimension:
                raise ValueError(f"{degree_id}: cumulative dimension decreases")
            previous_level = level
            previous_dimension = cumulative_dimension
    return pushed, len(monotone)


def verify_associated_graded(
    rows: list[dict[str, str]],
    pushed: dict[tuple[str, int], PushRow],
) -> None:
    seen: set[tuple[str, int]] = set()
    previous_by_degree: dict[str, int] = {}
    for row in sorted(rows, key=lambda item: (item["degree_id"], int_cell(item, "pbw_level"))):
        check_row(row, "associated_graded_rows.csv")
        degree_id = row["degree_id"]
        level = int_cell(row, "pbw_level")
        key = (degree_id, level)
        if key in seen:
            raise ValueError(f"associated_graded_rows.csv: duplicate degree/level {key}")
        seen.add(key)
        if key not in pushed:
            raise ValueError(f"associated_graded_rows.csv: no pushforward row for {key}")
        level_dimension, cumulative_dimension, _ = pushed[key]
        previous_cumulative = previous_by_degree.get(degree_id, 0)
        quotient_dimension = cumulative_dimension - previous_cumulative
        require_equal(quotient_dimension, level_dimension, f"{key} quotient equals level dimension")
        require_equal(int_cell(row, "computed_graded_dimension"), quotient_dimension, f"{key} graded dimension")
        require_equal(
            int_cell(row, "expected_graded_dimension"),
            quotient_dimension,
            f"{key} expected graded dimension",
        )
        require_zero(int_cell(row, "graded_defect_rank"), f"{key} graded defect")
        previous_by_degree[degree_id] = cumulative_dimension
    require_equal(seen, set(pushed), "associated graded coverage")


def verify_relations(
    rows: list[dict[str, str]],
    source_count: int,
    pushforward_count: int,
    graded_count: int,
    monotone_degree_count: int,
) -> None:
    relation_values = {
        "source_block_count": source_count,
        "pushforward_filtered_rows": pushforward_count,
        "associated_graded_rows": graded_count,
        "cumulative_monotone_degrees": monotone_degree_count,
        "pbw_filtration_preserved": 1,
        "associated_graded_from_quotients": 1,
        "source_pbw_comparison_not_proved": 1,
        "target_pbw_comparison_not_proved": 1,
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed")
        require_equal(int_cell(row, "computed_value"), int_cell(row, "expected_value"), f"{relation_id} expected")
        require_zero(int_cell(row, "defect_rank"), f"{relation_id} defect")
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
        require_zero(int_cell(row, "defect_rank"), f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"scalar_firewall.csv missing rows: {sorted(missing)}")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        blocks = verify_source_blocks(tables["source_filtered_blocks.csv"])
        pushed, monotone_degree_count = verify_pushforward_rows(
            tables["pushforward_filtered_sums.csv"],
            blocks,
        )
        verify_associated_graded(tables["associated_graded_rows.csv"], pushed)
        verify_relations(
            tables["formal_relations.csv"],
            len(blocks),
            len(pushed),
            len(tables["associated_graded_rows.csv"]),
            monotone_degree_count,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"PBW_PUSHFORWARD_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
