#!/usr/bin/env python3
"""Finite bar-pushforward commutation gate.

This verifier checks the finite algebraic statement that pushforward
along the additive normal-ordered Gram grading commutes with the reduced
tensor coalgebra underlying the bar construction:

    phi_* T^c(\bar A) = T^c(phi_* \bar A)

on the displayed finite words.  It also checks compatibility with
deconcatenation and with finite bar-differential degree bookkeeping.

The packet does not certify the raw quadratic Pi_X pushforward, chiral
Koszul quasi-isomorphism, Hall bracket compatibility, Hopf pairing
compatibility, Pfaffian orientations, or protected traces.
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
SUCCESS_STATUS = "BAR_PUSHFORWARD_COMMUTATION_VERIFIED"
EXPECTED_KIND = "bar_pushforward_commutation_formal_tensor_coalgebra"
DEFAULT_FIXTURE = Path("certificates/charge/bar_pushforward_commutation")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "bar_word_commutation",
        "deconcatenation_commutation",
        "bar_differential_degree",
        "finite_length_bound",
        "raw_quadratic_not_proved",
        "chiral_koszul_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "raw_quadratic_pushforward",
        "chiral_koszul_quasiisomorphism",
        "hall_bracket_compatibility",
        "hopf_pairing_compatibility",
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
        "generators.csv",
        (
            "generator_id",
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
        "bar_words.csv",
        (
            "word_id",
            "generator_ids",
            "word_length",
            "left_pushforward_degree_n",
            "left_pushforward_degree_l",
            "left_pushforward_degree_m",
            "right_bar_degree_n",
            "right_bar_degree_l",
            "right_bar_degree_m",
            "degree_defect_rank",
            "parity",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "deconcatenation.csv",
        (
            "split_id",
            "word_id",
            "left_generator_ids",
            "right_generator_ids",
            "left_degree_n",
            "left_degree_l",
            "left_degree_m",
            "right_degree_n",
            "right_degree_l",
            "right_degree_m",
            "total_degree_n",
            "total_degree_l",
            "total_degree_m",
            "deconcatenation_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "bar_differential.csv",
        (
            "differential_id",
            "left_generator_id",
            "right_generator_id",
            "product_degree_n",
            "product_degree_l",
            "product_degree_m",
            "sum_degree_n",
            "sum_degree_l",
            "sum_degree_m",
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


def add_triples(values: list[Triple]) -> Triple:
    return (
        sum(value[0] for value in values),
        sum(value[1] for value in values),
        sum(value[2] for value in values),
    )


def parse_ids(value: str) -> list[str]:
    return [item for item in value.split(";") if item]


def parity_sum(ids: list[str], parities: dict[str, str]) -> str:
    odd_count = sum(1 for item in ids if parities[item] == "odd")
    return "odd" if odd_count % 2 else "even"


def degree_sum(ids: list[str], degrees: dict[str, Triple]) -> Triple:
    return add_triples([degrees[item] for item in ids])


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("bar_pushforward_commutation_certified"), True, "manifest bar_pushforward_commutation_certified")
    require_equal(manifest.get("normal_ordered_additive_grading"), True, "manifest normal_ordered_additive_grading")
    require_equal(manifest.get("raw_quadratic_pushforward"), False, "manifest raw_quadratic_pushforward")
    require_equal(manifest.get("chiral_koszul_quasiisomorphism"), False, "manifest chiral_koszul_quasiisomorphism")
    require_equal(manifest.get("hall_bracket_compatibility"), False, "manifest hall_bracket_compatibility")
    require_equal(manifest.get("hopf_pairing_compatibility"), False, "manifest hopf_pairing_compatibility")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_generators(rows: list[dict[str, str]]) -> tuple[dict[str, Triple], dict[str, str]]:
    degrees: dict[str, Triple] = {}
    parities: dict[str, str] = {}
    for row in rows:
        check_row(row, "generators.csv")
        generator_id = row["generator_id"]
        if generator_id in degrees:
            raise ValueError(f"generators.csv: duplicate generator_id {generator_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"generators.csv: bad parity {parity!r}")
        degrees[generator_id] = triple_from_row(row, "degree")
        parities[generator_id] = parity
    return degrees, parities


def verify_bar_words(rows: list[dict[str, str]], degrees: dict[str, Triple], parities: dict[str, str]) -> tuple[dict[str, list[str]], int]:
    words: dict[str, list[str]] = {}
    max_length = 0
    for row in rows:
        check_row(row, "bar_words.csv")
        word_id = row["word_id"]
        if word_id in words:
            raise ValueError(f"bar_words.csv: duplicate word_id {word_id}")
        ids = parse_ids(row["generator_ids"])
        if not ids:
            raise ValueError(f"bar_words.csv: empty word {row}")
        for generator_id in ids:
            if generator_id not in degrees:
                raise ValueError(f"bar_words.csv: unknown generator_id {generator_id}")
        degree = degree_sum(ids, degrees)
        require_equal(len(ids), int_cell(row, "word_length"), f"{word_id} length")
        require_equal(degree, triple_from_row(row, "left_pushforward_degree"), f"{word_id} left degree")
        require_equal(degree, triple_from_row(row, "right_bar_degree"), f"{word_id} right degree")
        require_zero(int_cell(row, "degree_defect_rank"), f"{word_id} defect")
        require_equal(parity_sum(ids, parities), row["parity"], f"{word_id} parity")
        words[word_id] = ids
        max_length = max(max_length, len(ids))
    return words, max_length


def verify_deconcatenation(rows: list[dict[str, str]], words: dict[str, list[str]], degrees: dict[str, Triple]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "deconcatenation.csv")
        split_id = row["split_id"]
        if split_id in seen:
            raise ValueError(f"deconcatenation.csv: duplicate split_id {split_id}")
        seen.add(split_id)
        word_id = row["word_id"]
        if word_id not in words:
            raise ValueError(f"deconcatenation.csv: unknown word_id {word_id}")
        left = parse_ids(row["left_generator_ids"])
        right = parse_ids(row["right_generator_ids"])
        require_equal(left + right, words[word_id], f"{split_id} concatenation")
        left_degree = degree_sum(left, degrees)
        right_degree = degree_sum(right, degrees)
        total_degree = add_triples([left_degree, right_degree])
        require_equal(left_degree, triple_from_row(row, "left_degree"), f"{split_id} left degree")
        require_equal(right_degree, triple_from_row(row, "right_degree"), f"{split_id} right degree")
        require_equal(total_degree, triple_from_row(row, "total_degree"), f"{split_id} total degree")
        require_zero(int_cell(row, "deconcatenation_defect_rank"), f"{split_id} defect")


def verify_bar_differential(rows: list[dict[str, str]], degrees: dict[str, Triple]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "bar_differential.csv")
        differential_id = row["differential_id"]
        if differential_id in seen:
            raise ValueError(f"bar_differential.csv: duplicate differential_id {differential_id}")
        seen.add(differential_id)
        left = row["left_generator_id"]
        right = row["right_generator_id"]
        if left not in degrees or right not in degrees:
            raise ValueError(f"bar_differential.csv: unknown generator in {row}")
        expected = add_triples([degrees[left], degrees[right]])
        require_equal(expected, triple_from_row(row, "product_degree"), f"{differential_id} product degree")
        require_equal(expected, triple_from_row(row, "sum_degree"), f"{differential_id} sum degree")
        require_zero(int_cell(row, "degree_defect_rank"), f"{differential_id} defect")


def verify_relations(rows: list[dict[str, str]], word_count: int, split_count: int, differential_count: int, max_length: int) -> None:
    relation_values = {
        "bar_word_commutation": word_count,
        "deconcatenation_commutation": split_count,
        "bar_differential_degree": differential_count,
        "finite_length_bound": max_length,
        "raw_quadratic_not_proved": 1,
        "chiral_koszul_not_proved": 1,
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
        degrees, parities = verify_generators(tables["generators.csv"])
        words, max_length = verify_bar_words(tables["bar_words.csv"], degrees, parities)
        verify_deconcatenation(tables["deconcatenation.csv"], words, degrees)
        verify_bar_differential(tables["bar_differential.csv"], degrees)
        verify_relations(
            tables["formal_relations.csv"],
            len(words),
            len(tables["deconcatenation.csv"]),
            len(tables["bar_differential.csv"]),
            max_length,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"BAR_PUSHFORWARD_COMMUTATION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
