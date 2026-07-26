#!/usr/bin/env python3
"""Finite normal-ordered pushforward compatibility gate.

This verifier checks the finite algebraic statement that an additive
normal-ordered Gram grading preserves the degree of a supplied bracket
and a supplied homogeneous pairing.  It does not construct the Hall
correspondence, prove primitive closure, prove Hopf adjointness, prove
the Frobenius cyclic identity, or prove quotient non-degeneracy.
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
SUCCESS_STATUS = "HALL_PAIRING_PUSHFORWARD_COMPATIBILITY_VERIFIED"
EXPECTED_KIND = "hall_pairing_pushforward_compatibility_formal_linear_algebra"
DEFAULT_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "bracket_degree_compatible",
        "pairing_degree_compatible",
        "pushforward_bracket_graded",
        "pushforward_pairing_graded",
        "hall_geometry_not_proved",
        "hopf_adjointness_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_hall_correspondence",
        "primitive_closure",
        "hopf_adjointness",
        "frobenius_cyclic_identity",
        "quotient_nondegeneracy",
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
        "basis_degrees.csv",
        (
            "basis_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "parity",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "bracket_rows.csv",
        (
            "bracket_id",
            "left_basis_id",
            "right_basis_id",
            "target_basis_id",
            "structure_coeff",
            "left_degree_n",
            "left_degree_l",
            "left_degree_m",
            "right_degree_n",
            "right_degree_l",
            "right_degree_m",
            "target_degree_n",
            "target_degree_l",
            "target_degree_m",
            "sum_degree_n",
            "sum_degree_l",
            "sum_degree_m",
            "target_parity",
            "sum_parity",
            "degree_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pairing_rows.csv",
        (
            "pairing_id",
            "left_basis_id",
            "right_basis_id",
            "pairing_value",
            "left_degree_n",
            "left_degree_l",
            "left_degree_m",
            "right_degree_n",
            "right_degree_l",
            "right_degree_m",
            "total_degree_n",
            "total_degree_l",
            "total_degree_m",
            "homogeneous_degree_zero",
            "degree_defect_rank",
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


def triple_from_row(row: dict[str, str], prefix: str) -> Triple:
    return (
        int_cell(row, f"{prefix}_n"),
        int_cell(row, f"{prefix}_l"),
        int_cell(row, f"{prefix}_m"),
    )


def add_triples(left: Triple, right: Triple) -> Triple:
    return left[0] + right[0], left[1] + right[1], left[2] + right[2]


def parity_sum(left: str, right: str) -> str:
    if left not in {"even", "odd"} or right not in {"even", "odd"}:
        raise ValueError(f"bad parities {left!r}, {right!r}")
    return "odd" if (left == "odd") ^ (right == "odd") else "even"


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("normal_ordered_bracket_degree"), True, "manifest normal_ordered_bracket_degree")
    require_equal(manifest.get("normal_ordered_pairing_degree"), True, "manifest normal_ordered_pairing_degree")
    require_equal(manifest.get("compact_hall_correspondence"), False, "manifest compact_hall_correspondence")
    require_equal(manifest.get("primitive_closure"), False, "manifest primitive_closure")
    require_equal(manifest.get("hopf_adjointness"), False, "manifest hopf_adjointness")
    require_equal(manifest.get("frobenius_cyclic_identity"), False, "manifest frobenius_cyclic_identity")
    require_equal(manifest.get("quotient_nondegeneracy"), False, "manifest quotient_nondegeneracy")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_basis(rows: list[dict[str, str]]) -> tuple[dict[str, Triple], dict[str, str]]:
    degrees: dict[str, Triple] = {}
    parities: dict[str, str] = {}
    for row in rows:
        check_row(row, "basis_degrees.csv")
        basis_id = row["basis_id"]
        if basis_id in degrees:
            raise ValueError(f"basis_degrees.csv: duplicate basis_id {basis_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"basis_degrees.csv: bad parity {parity!r}")
        degrees[basis_id] = triple_from_row(row, "degree")
        parities[basis_id] = parity
    return degrees, parities


def verify_brackets(rows: list[dict[str, str]], degrees: dict[str, Triple], parities: dict[str, str]) -> int:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "bracket_rows.csv")
        bracket_id = row["bracket_id"]
        if bracket_id in seen:
            raise ValueError(f"bracket_rows.csv: duplicate bracket_id {bracket_id}")
        seen.add(bracket_id)
        left = row["left_basis_id"]
        right = row["right_basis_id"]
        target = row["target_basis_id"]
        for basis_id in (left, right, target):
            if basis_id not in degrees:
                raise ValueError(f"bracket_rows.csv: unknown basis_id {basis_id}")
        require_equal(degrees[left], triple_from_row(row, "left_degree"), f"{bracket_id} left degree")
        require_equal(degrees[right], triple_from_row(row, "right_degree"), f"{bracket_id} right degree")
        require_equal(degrees[target], triple_from_row(row, "target_degree"), f"{bracket_id} target degree")
        degree_sum = add_triples(degrees[left], degrees[right])
        require_equal(degree_sum, triple_from_row(row, "sum_degree"), f"{bracket_id} sum degree")
        require_equal(degrees[target], degree_sum, f"{bracket_id} target=sum")
        require_equal(parities[target], row["target_parity"], f"{bracket_id} target parity")
        require_equal(parity_sum(parities[left], parities[right]), row["sum_parity"], f"{bracket_id} sum parity")
        require_equal(parities[target], row["sum_parity"], f"{bracket_id} parity")
        require_zero(int_cell(row, "degree_defect_rank"), f"{bracket_id} defect")
    return len(rows)


def verify_pairings(rows: list[dict[str, str]], degrees: dict[str, Triple]) -> int:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "pairing_rows.csv")
        pairing_id = row["pairing_id"]
        if pairing_id in seen:
            raise ValueError(f"pairing_rows.csv: duplicate pairing_id {pairing_id}")
        seen.add(pairing_id)
        left = row["left_basis_id"]
        right = row["right_basis_id"]
        for basis_id in (left, right):
            if basis_id not in degrees:
                raise ValueError(f"pairing_rows.csv: unknown basis_id {basis_id}")
        require_equal(degrees[left], triple_from_row(row, "left_degree"), f"{pairing_id} left degree")
        require_equal(degrees[right], triple_from_row(row, "right_degree"), f"{pairing_id} right degree")
        total = add_triples(degrees[left], degrees[right])
        require_equal(total, triple_from_row(row, "total_degree"), f"{pairing_id} total degree")
        homogeneous = total == (0, 0, 0)
        require_equal(bool_cell(row, "homogeneous_degree_zero"), homogeneous, f"{pairing_id} homogeneous flag")
        require_equal(int_cell(row, "pairing_value") != 0, True, f"{pairing_id} nonzero value")
        require_zero(int_cell(row, "degree_defect_rank"), f"{pairing_id} defect")
    return len(rows)


def verify_relations(rows: list[dict[str, str]], bracket_count: int, pairing_count: int) -> None:
    relation_values = {
        "bracket_degree_compatible": bracket_count,
        "pairing_degree_compatible": pairing_count,
        "pushforward_bracket_graded": 1,
        "pushforward_pairing_graded": 1,
        "hall_geometry_not_proved": 1,
        "hopf_adjointness_not_proved": 1,
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
        degrees, parities = verify_basis(tables["basis_degrees.csv"])
        bracket_count = verify_brackets(tables["bracket_rows.csv"], degrees, parities)
        pairing_count = verify_pairings(tables["pairing_rows.csv"], degrees)
        verify_relations(tables["formal_relations.csv"], bracket_count, pairing_count)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"HALL_PAIRING_PUSHFORWARD_COMPATIBILITY_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
