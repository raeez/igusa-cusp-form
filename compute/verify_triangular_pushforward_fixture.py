#!/usr/bin/env python3
"""Finite triangular-decomposition pushforward gate.

This verifier checks the finite statement that pushforward along the
additive normal-ordered Gram grading preserves a supplied triangular
decomposition

    V = V^- direct-sum V^0 direct-sum V^+

when the positive, Cartan, and negative parts are defined by a supplied
integer height on the pushed Gram degrees.  It also checks supplied
bracket sign rows.  The packet does not prove exact triangular
completion, compact-source primitive recognition, target triangular
completion, no-extra relations, Pfaffian orientations, or protected
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
SUCCESS_STATUS = "TRIANGULAR_PUSHFORWARD_VERIFIED"
EXPECTED_KIND = "triangular_pushforward_formal_direct_sum"
DEFAULT_FIXTURE = Path("certificates/charge/triangular_pushforward")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "source_triangular_row_count",
        "pushforward_triangular_row_count",
        "bracket_sign_row_count",
        "height_sign_consistency",
        "triangular_direct_sum_preserved",
        "bracket_sign_compatible",
        "exact_triangular_completion_not_proved",
        "primitive_recognition_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "exact_triangular_completion",
        "target_triangular_completion",
        "compact_source",
        "primitive_recognition",
        "no_extra_relations",
        "pbw_comparison",
        "universal_enveloping_isomorphism",
        "pfaffian_orientation",
        "protected_trace",
    }
)
TRIANGULAR_PARTS = frozenset({"positive", "cartan", "negative"})


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "source_triangular_rows.csv",
        (
            "source_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "height",
            "triangular_part",
            "dimension",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pushforward_triangular_sums.csv",
        (
            "pushforward_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "height",
            "triangular_part",
            "source_ids",
            "total_dimension",
            "triangular_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "bracket_sign_rows.csv",
        (
            "bracket_id",
            "left_source_id",
            "right_source_id",
            "target_source_id",
            "left_part",
            "right_part",
            "target_part",
            "sum_degree_n",
            "sum_degree_l",
            "sum_degree_m",
            "sum_height",
            "triangular_defect_rank",
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
SourceRow = tuple[str, Triple, int, str, int]


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


def triple_from_row(row: dict[str, str], prefix: str = "degree") -> Triple:
    return int_cell(row, f"{prefix}_n"), int_cell(row, f"{prefix}_l"), int_cell(row, f"{prefix}_m")


def add_triples(left: Triple, right: Triple) -> Triple:
    return left[0] + right[0], left[1] + right[1], left[2] + right[2]


def split_ids(cell: str) -> list[str]:
    ids = [part.strip() for part in cell.split(";") if part.strip()]
    if not ids:
        raise ValueError(f"empty source_ids cell {cell!r}")
    return ids


def sign_from_height(height: int) -> str:
    if height > 0:
        return "positive"
    if height < 0:
        return "negative"
    return "cartan"


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(
        manifest.get("normal_ordered_triangular_pushforward"),
        True,
        "manifest normal_ordered_triangular_pushforward",
    )
    require_equal(manifest.get("triangular_direct_sum_preserved"), True, "manifest triangular_direct_sum_preserved")
    require_equal(manifest.get("bracket_sign_rows_verified"), True, "manifest bracket_sign_rows_verified")
    require_equal(manifest.get("exact_triangular_completion"), False, "manifest exact_triangular_completion")
    require_equal(manifest.get("target_triangular_completion"), False, "manifest target_triangular_completion")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("no_extra_relations"), False, "manifest no_extra_relations")
    require_equal(manifest.get("pbw_comparison"), False, "manifest pbw_comparison")
    require_equal(
        manifest.get("universal_enveloping_isomorphism"),
        False,
        "manifest universal_enveloping_isomorphism",
    )
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_source_rows(rows: list[dict[str, str]]) -> dict[str, SourceRow]:
    sources: dict[str, SourceRow] = {}
    for row in rows:
        check_row(row, "source_triangular_rows.csv")
        source_id = row["source_id"]
        if source_id in sources:
            raise ValueError(f"source_triangular_rows.csv: duplicate source_id {source_id}")
        triangular_part = row["triangular_part"]
        if triangular_part not in TRIANGULAR_PARTS:
            raise ValueError(f"source_triangular_rows.csv: bad triangular_part {triangular_part!r}")
        height = int_cell(row, "height")
        require_equal(sign_from_height(height), triangular_part, f"{source_id} height sign")
        dimension = int_cell(row, "dimension")
        if dimension <= 0:
            raise ValueError(f"source_triangular_rows.csv: nonpositive dimension in {row}")
        sources[source_id] = (row["degree_id"], triple_from_row(row), height, triangular_part, dimension)
    return sources


def verify_pushforward_rows(
    rows: list[dict[str, str]],
    sources: dict[str, SourceRow],
) -> int:
    seen: set[tuple[str, str]] = set()
    used_sources: set[str] = set()
    for row in rows:
        check_row(row, "pushforward_triangular_sums.csv")
        degree_id = row["degree_id"]
        triangular_part = row["triangular_part"]
        if triangular_part not in TRIANGULAR_PARTS:
            raise ValueError(f"pushforward_triangular_sums.csv: bad triangular_part {triangular_part!r}")
        key = (degree_id, triangular_part)
        if key in seen:
            raise ValueError(f"pushforward_triangular_sums.csv: duplicate degree/part {key}")
        seen.add(key)
        height = int_cell(row, "height")
        require_equal(sign_from_height(height), triangular_part, f"{key} height sign")
        row_degree = triple_from_row(row)
        total = 0
        for source_id in split_ids(row["source_ids"]):
            if source_id not in sources:
                raise ValueError(f"pushforward_triangular_sums.csv: unknown source_id {source_id}")
            source_degree_id, source_degree, source_height, source_part, dimension = sources[source_id]
            require_equal(source_degree_id, degree_id, f"{source_id} degree_id")
            require_equal(source_degree, row_degree, f"{source_id} degree")
            require_equal(source_height, height, f"{source_id} height")
            require_equal(source_part, triangular_part, f"{source_id} triangular_part")
            total += dimension
            used_sources.add(source_id)
        require_equal(int_cell(row, "total_dimension"), total, f"{key} total dimension")
        require_zero(int_cell(row, "triangular_defect_rank"), f"{key} triangular defect")
    require_equal(used_sources, set(sources), "source triangular row coverage")
    return len(seen)


def verify_bracket_rows(rows: list[dict[str, str]], sources: dict[str, SourceRow]) -> int:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "bracket_sign_rows.csv")
        bracket_id = row["bracket_id"]
        if bracket_id in seen:
            raise ValueError(f"bracket_sign_rows.csv: duplicate bracket_id {bracket_id}")
        seen.add(bracket_id)
        left_id = row["left_source_id"]
        right_id = row["right_source_id"]
        target_id = row["target_source_id"]
        for source_id in (left_id, right_id, target_id):
            if source_id not in sources:
                raise ValueError(f"bracket_sign_rows.csv: unknown source_id {source_id}")
        _, left_degree, left_height, left_part, _ = sources[left_id]
        _, right_degree, right_height, right_part, _ = sources[right_id]
        _, target_degree, target_height, target_part, _ = sources[target_id]
        require_equal(row["left_part"], left_part, f"{bracket_id} left part")
        require_equal(row["right_part"], right_part, f"{bracket_id} right part")
        require_equal(row["target_part"], target_part, f"{bracket_id} target part")
        degree_sum = add_triples(left_degree, right_degree)
        height_sum = left_height + right_height
        require_equal(triple_from_row(row, "sum_degree"), degree_sum, f"{bracket_id} displayed sum degree")
        require_equal(target_degree, degree_sum, f"{bracket_id} target degree")
        require_equal(int_cell(row, "sum_height"), height_sum, f"{bracket_id} displayed sum height")
        require_equal(target_height, height_sum, f"{bracket_id} target height")
        require_equal(sign_from_height(height_sum), target_part, f"{bracket_id} target sign")
        require_zero(int_cell(row, "triangular_defect_rank"), f"{bracket_id} triangular defect")
    return len(rows)


def verify_relations(
    rows: list[dict[str, str]],
    source_count: int,
    pushforward_count: int,
    bracket_count: int,
) -> None:
    relation_values = {
        "source_triangular_row_count": source_count,
        "pushforward_triangular_row_count": pushforward_count,
        "bracket_sign_row_count": bracket_count,
        "height_sign_consistency": 1,
        "triangular_direct_sum_preserved": 1,
        "bracket_sign_compatible": 1,
        "exact_triangular_completion_not_proved": 1,
        "primitive_recognition_not_proved": 1,
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
        sources = verify_source_rows(tables["source_triangular_rows.csv"])
        pushforward_count = verify_pushforward_rows(tables["pushforward_triangular_sums.csv"], sources)
        bracket_count = verify_bracket_rows(tables["bracket_sign_rows.csv"], sources)
        verify_relations(
            tables["formal_relations.csv"],
            len(sources),
            pushforward_count,
            bracket_count,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TRIANGULAR_PUSHFORWARD_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
