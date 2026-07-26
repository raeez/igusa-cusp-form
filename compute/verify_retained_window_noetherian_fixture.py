#!/usr/bin/env python3
"""Finite retained-window noetherianity gate.

This verifier checks the finite ACC statement used for retained
windows in the Abramovich--Polishchuk/Liu heart.  It certifies that a
supplied finite exact window is subobject-closed and carries a length
rank strictly increasing along every strict subobject inclusion.  Hence
every ascending chain inside the retained window terminates.

It does not prove the global AP/Liu heart is noetherian, does not prove
Harder--Narasimhan filtrations, does not prove bounded HN types, and
does not construct finite-type moduli.
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
SUCCESS_STATUS = "RETAINED_WINDOW_NOETHERIAN_VERIFIED"
EXPECTED_KIND = "retained_window_noetherianity_finite_exact_category"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_window_noetherian")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "finite_object_set",
        "subobject_closure",
        "quotient_closure",
        "strict_length_increase",
        "subobject_graph_acyclic",
        "chain_bound_verified",
        "retained_window_noetherian",
        "global_noetherianity_not_proved",
        "hn_filtration_not_proved",
        "finite_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "global_ap_liu_noetherianity",
        "harder_narasimhan_filtrations",
        "bounded_hn_types",
        "finite_type_semistable_substacks",
        "quasi_smooth_moduli",
        "universal_complexes",
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
    TableSpec(
        "window_datum.csv",
        (
            "window_id",
            "heart_id",
            "hn_stage",
            "object_count",
            "subobject_closed",
            "quotient_closed",
            "finite_exact_status",
            "global_noetherian_claim",
            "hn_filtration_claim",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "object_lengths.csv",
        (
            "object_id",
            "window_id",
            "class_id",
            "length_rank",
            "is_zero_object",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "subobject_relations.csv",
        (
            "relation_id",
            "window_id",
            "subobject_id",
            "object_id",
            "quotient_id",
            "strict",
            "length_defect_rank",
            "closure_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "chain_bounds.csv",
        (
            "chain_id",
            "window_id",
            "start_object_id",
            "computed_max_strict_chain_length",
            "expected_max_strict_chain_length",
            "object_count_bound",
            "noetherian_defect_rank",
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


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("moduli_kind"), EXPECTED_KIND, "manifest moduli_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("retained_window_noetherianity"), True, "manifest retained_window_noetherianity")
    require_equal(manifest.get("global_ap_liu_noetherianity"), False, "manifest global_ap_liu_noetherianity")
    require_equal(manifest.get("hn_filtrations"), False, "manifest hn_filtrations")
    require_equal(manifest.get("bounded_hn_types"), False, "manifest bounded_hn_types")
    require_equal(manifest.get("finite_type_moduli"), False, "manifest finite_type_moduli")
    require_equal(manifest.get("derived_moduli"), False, "manifest derived_moduli")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_window(rows: list[dict[str, str]]) -> tuple[str, int]:
    require_equal(len(rows), 1, "window row count")
    row = rows[0]
    check_row(row, "window_datum.csv")
    window_id = row["window_id"]
    object_count = int_cell(row, "object_count")
    if object_count <= 0:
        raise ValueError("window object_count must be positive")
    require_equal(bool_cell(row, "subobject_closed"), True, "window subobject_closed")
    require_equal(bool_cell(row, "quotient_closed"), True, "window quotient_closed")
    require_equal(row["finite_exact_status"], "finite_exact_verified", "window finite_exact_status")
    require_equal(bool_cell(row, "global_noetherian_claim"), False, "window global_noetherian_claim")
    require_equal(bool_cell(row, "hn_filtration_claim"), False, "window hn_filtration_claim")
    return window_id, object_count


def verify_objects(rows: list[dict[str, str]], window_id: str, object_count: int) -> dict[str, int]:
    lengths: dict[str, int] = {}
    zero_count = 0
    for row in rows:
        check_row(row, "object_lengths.csv")
        require_equal(row["window_id"], window_id, f"{row['object_id']} window")
        object_id = row["object_id"]
        if object_id in lengths:
            raise ValueError(f"object_lengths.csv: duplicate object_id {object_id}")
        length = int_cell(row, "length_rank")
        if length < 0:
            raise ValueError(f"object_lengths.csv: negative length in {row}")
        if bool_cell(row, "is_zero_object"):
            zero_count += 1
            require_equal(length, 0, f"{object_id} zero length")
        elif length == 0:
            raise ValueError(f"object_lengths.csv: nonzero object has length 0 in {row}")
        lengths[object_id] = length
    require_equal(len(lengths), object_count, "object_count")
    require_equal(zero_count, 1, "zero object count")
    return lengths


def verify_subobjects(
    rows: list[dict[str, str]],
    window_id: str,
    lengths: dict[str, int],
) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {object_id: [] for object_id in lengths}
    for row in rows:
        check_row(row, "subobject_relations.csv")
        require_equal(row["window_id"], window_id, f"{row['relation_id']} window")
        subobject_id = row["subobject_id"]
        object_id = row["object_id"]
        quotient_id = row["quotient_id"]
        for label, value in (
            ("subobject_id", subobject_id),
            ("object_id", object_id),
            ("quotient_id", quotient_id),
        ):
            if value not in lengths:
                raise ValueError(f"subobject_relations.csv: unknown {label}={value}")
        strict = bool_cell(row, "strict")
        if not strict:
            raise ValueError(f"subobject_relations.csv: expected strict=true in {row}")
        if lengths[subobject_id] >= lengths[object_id]:
            raise ValueError(
                f"subobject_relations.csv: length does not increase for {subobject_id}->{object_id}"
            )
        require_zero(int_cell(row, "length_defect_rank"), f"{row['relation_id']} length_defect")
        require_zero(int_cell(row, "closure_defect_rank"), f"{row['relation_id']} closure_defect")
        graph[subobject_id].append(object_id)
    return graph


def longest_paths(graph: dict[str, list[str]]) -> dict[str, int]:
    visiting: set[str] = set()
    visited: dict[str, int] = {}

    def dfs(node: str) -> int:
        if node in visited:
            return visited[node]
        if node in visiting:
            raise ValueError(f"subobject graph has a cycle through {node}")
        visiting.add(node)
        best = 0
        for target in graph[node]:
            best = max(best, 1 + dfs(target))
        visiting.remove(node)
        visited[node] = best
        return best

    return {node: dfs(node) for node in graph}


def verify_chain_bounds(
    rows: list[dict[str, str]],
    window_id: str,
    object_count: int,
    path_lengths: dict[str, int],
) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "chain_bounds.csv")
        require_equal(row["window_id"], window_id, f"{row['chain_id']} window")
        object_id = row["start_object_id"]
        if object_id in seen:
            raise ValueError(f"chain_bounds.csv: duplicate start_object_id {object_id}")
        seen.add(object_id)
        if object_id not in path_lengths:
            raise ValueError(f"chain_bounds.csv: unknown start_object_id {object_id}")
        computed = path_lengths[object_id]
        require_equal(int_cell(row, "computed_max_strict_chain_length"), computed, f"{object_id} computed")
        require_equal(int_cell(row, "expected_max_strict_chain_length"), computed, f"{object_id} expected")
        require_equal(int_cell(row, "object_count_bound"), object_count - 1, f"{object_id} object_count_bound")
        if computed > object_count - 1:
            raise ValueError(f"{object_id}: chain longer than finite object bound")
        require_zero(int_cell(row, "noetherian_defect_rank"), f"{object_id} noetherian_defect")
    require_equal(seen, set(path_lengths), "chain bound coverage")


def verify_relations(
    rows: list[dict[str, str]],
    object_count: int,
    subobject_count: int,
    max_chain_length: int,
) -> None:
    relation_values = {
        "finite_object_set": object_count,
        "subobject_closure": subobject_count,
        "quotient_closure": subobject_count,
        "strict_length_increase": subobject_count,
        "subobject_graph_acyclic": 1,
        "chain_bound_verified": max_chain_length,
        "retained_window_noetherian": 1,
        "global_noetherianity_not_proved": 1,
        "hn_filtration_not_proved": 1,
        "finite_moduli_not_proved": 1,
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
        window_id, object_count = verify_window(tables["window_datum.csv"])
        lengths = verify_objects(tables["object_lengths.csv"], window_id, object_count)
        graph = verify_subobjects(tables["subobject_relations.csv"], window_id, lengths)
        path_lengths = longest_paths(graph)
        verify_chain_bounds(tables["chain_bounds.csv"], window_id, object_count, path_lengths)
        verify_relations(
            tables["formal_relations.csv"],
            object_count,
            len(tables["subobject_relations.csv"]),
            max(path_lengths.values()),
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_WINDOW_NOETHERIAN_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
