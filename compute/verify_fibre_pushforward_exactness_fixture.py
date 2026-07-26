#!/usr/bin/env python3
"""Finite fibre-pushforward exactness and zero-fibre radical gate.

This verifier checks the finite linear algebra that is independent of
Hall geometry:

* the zero-fibre radical is the kernel of the finite pairing matrix on
  the displayed zero Gram fibre;
* each displayed finite Gram/parity block is an exact sequence
  0 -> A -> B -> C -> 0;
* finite fibre-summed pushforward is exact because it is a finite direct
  sum over Gram fibres.

The packet does not certify finite HN boundedness, compact Hall support,
source Hall brackets, Hopf ideal/coideal closure of the radical, exact
Hall pushforward, bar-construction commutation, Pfaffian orientations,
or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "FIBRE_PUSHFORWARD_EXACTNESS_VERIFIED"
EXPECTED_KIND = "fibre_pushforward_exactness_formal_linear_algebra"
DEFAULT_FIXTURE = Path("certificates/charge/fibre_pushforward_exactness")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "zero_fibre_radical_defined",
        "degreewise_exact",
        "pushforward_exact",
        "finite_direct_sum_exact",
        "hopf_radical_not_proved",
        "bar_commutation_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "finite_hn_charge_window",
        "compact_source",
        "source_hall_bracket",
        "hopf_radical_ideal_coideal",
        "exact_hall_pushforward",
        "bar_construction_commutation",
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
        "finite_degrees.csv",
        (
            "degree_id",
            "pi_n",
            "pi_l",
            "pi_m",
            "is_zero_fibre",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "exact_sequences.csv",
        (
            "sequence_id",
            "degree_id",
            "parity",
            "dim_A",
            "dim_B",
            "dim_C",
            "injection_matrix",
            "projection_matrix",
            "rank_injection",
            "rank_projection",
            "kernel_projection_dim",
            "composition_rank",
            "exact_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pushforward_sums.csv",
        (
            "pushforward_id",
            "degree_id",
            "parity",
            "sequence_ids",
            "total_dim_A",
            "total_dim_B",
            "total_dim_C",
            "total_rank_injection",
            "total_rank_projection",
            "total_kernel_projection_dim",
            "pushforward_exact_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "zero_fibre_radicals.csv",
        (
            "radical_id",
            "degree_id",
            "basis_ids",
            "even_count",
            "odd_count",
            "pairing_matrix",
            "radical_basis_ids",
            "matrix_rank",
            "radical_dim",
            "quotient_dim",
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


Matrix = list[list[Fraction]]


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


def parse_matrix(value: str, rows: int, cols: int, label: str) -> Matrix:
    row_texts = value.split(";") if value else []
    if len(row_texts) != rows:
        raise ValueError(f"{label}: expected {rows} rows, got {len(row_texts)}")
    matrix: Matrix = []
    for row_text in row_texts:
        entries = row_text.split()
        if len(entries) != cols:
            raise ValueError(f"{label}: expected {cols} columns, got {len(entries)}")
        matrix.append([Fraction(entry) for entry in entries])
    return matrix


def rank(matrix: Matrix) -> int:
    if not matrix:
        return 0
    work = [row[:] for row in matrix]
    row_count = len(work)
    col_count = len(work[0])
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if work[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][col]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][col]
            if factor:
                work[row] = [
                    entry - factor * pivot_entry
                    for entry, pivot_entry in zip(work[row], work[pivot_row])
                ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def matmul(left: Matrix, right: Matrix) -> Matrix:
    if not left or not right:
        return []
    if len(left[0]) != len(right):
        raise ValueError("matrix dimensions do not match")
    return [
        [
            sum(left[row][k] * right[k][col] for k in range(len(right)))
            for col in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("finite_vector_space_exactness"), True, "manifest finite_vector_space_exactness")
    require_equal(manifest.get("zero_fibre_radical_defined"), True, "manifest zero_fibre_radical_defined")
    require_equal(manifest.get("finite_hn_charge_window"), False, "manifest finite_hn_charge_window")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("source_hall_bracket"), False, "manifest source_hall_bracket")
    require_equal(manifest.get("hopf_radical_certification"), False, "manifest hopf_radical_certification")
    require_equal(manifest.get("hall_pushforward_exactness"), False, "manifest hall_pushforward_exactness")
    require_equal(manifest.get("bar_commutation"), False, "manifest bar_commutation")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_degrees(rows: list[dict[str, str]]) -> dict[str, tuple[int, int, int]]:
    degrees: dict[str, tuple[int, int, int]] = {}
    zero_seen = False
    for row in rows:
        check_row(row, "finite_degrees.csv")
        degree_id = row["degree_id"]
        if degree_id in degrees:
            raise ValueError(f"finite_degrees.csv: duplicate degree_id {degree_id}")
        triple = (int_cell(row, "pi_n"), int_cell(row, "pi_l"), int_cell(row, "pi_m"))
        degrees[degree_id] = triple
        is_zero = triple == (0, 0, 0)
        require_equal(bool_cell(row, "is_zero_fibre"), is_zero, f"{degree_id} zero flag")
        zero_seen = zero_seen or is_zero
    if not zero_seen:
        raise ValueError("finite_degrees.csv: expected a zero-fibre degree")
    return degrees


def verify_exact_sequences(rows: list[dict[str, str]], degrees: dict[str, tuple[int, int, int]]) -> dict[str, dict[str, int | str]]:
    sequences: dict[str, dict[str, int | str]] = {}
    for row in rows:
        check_row(row, "exact_sequences.csv")
        sequence_id = row["sequence_id"]
        if sequence_id in sequences:
            raise ValueError(f"exact_sequences.csv: duplicate sequence_id {sequence_id}")
        degree_id = row["degree_id"]
        if degree_id not in degrees:
            raise ValueError(f"exact_sequences.csv: unknown degree_id {degree_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"exact_sequences.csv: bad parity {parity!r}")
        dim_a = int_cell(row, "dim_A")
        dim_b = int_cell(row, "dim_B")
        dim_c = int_cell(row, "dim_C")
        injection = parse_matrix(row["injection_matrix"], dim_b, dim_a, f"{sequence_id} injection")
        projection = parse_matrix(row["projection_matrix"], dim_c, dim_b, f"{sequence_id} projection")
        rank_i = rank(injection)
        rank_p = rank(projection)
        composition_rank = rank(matmul(projection, injection))
        kernel_p_dim = dim_b - rank_p
        exact_defect = abs(kernel_p_dim - rank_i) + composition_rank
        require_equal(rank_i, int_cell(row, "rank_injection"), f"{sequence_id} rank injection")
        require_equal(rank_p, int_cell(row, "rank_projection"), f"{sequence_id} rank projection")
        require_equal(kernel_p_dim, int_cell(row, "kernel_projection_dim"), f"{sequence_id} kernel projection")
        require_equal(composition_rank, int_cell(row, "composition_rank"), f"{sequence_id} composition rank")
        require_equal(exact_defect, int_cell(row, "exact_defect_rank"), f"{sequence_id} exact defect")
        require_zero(exact_defect, f"{sequence_id} exact defect")
        require_equal(rank_i, dim_a, f"{sequence_id} injective")
        require_equal(rank_p, dim_c, f"{sequence_id} surjective")
        sequences[sequence_id] = {
            "degree_id": degree_id,
            "parity": parity,
            "dim_a": dim_a,
            "dim_b": dim_b,
            "dim_c": dim_c,
            "rank_i": rank_i,
            "rank_p": rank_p,
            "kernel_p_dim": kernel_p_dim,
        }
    return sequences


def verify_pushforwards(rows: list[dict[str, str]], sequences: dict[str, dict[str, int | str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "pushforward_sums.csv")
        pushforward_id = row["pushforward_id"]
        if pushforward_id in seen:
            raise ValueError(f"pushforward_sums.csv: duplicate pushforward_id {pushforward_id}")
        seen.add(pushforward_id)
        sequence_ids = [item for item in row["sequence_ids"].split(";") if item]
        if not sequence_ids:
            raise ValueError(f"pushforward_sums.csv: empty sequence_ids in {row}")
        for sequence_id in sequence_ids:
            if sequence_id not in sequences:
                raise ValueError(f"pushforward_sums.csv: unknown sequence_id {sequence_id}")
        degree_id = row["degree_id"]
        parity = row["parity"]
        if any(sequences[sequence_id]["degree_id"] != degree_id for sequence_id in sequence_ids):
            raise ValueError(f"pushforward_sums.csv: mixed degree ids in {row}")
        if any(sequences[sequence_id]["parity"] != parity for sequence_id in sequence_ids):
            raise ValueError(f"pushforward_sums.csv: mixed parity in {row}")
        total_a = sum(int(sequences[sequence_id]["dim_a"]) for sequence_id in sequence_ids)
        total_b = sum(int(sequences[sequence_id]["dim_b"]) for sequence_id in sequence_ids)
        total_c = sum(int(sequences[sequence_id]["dim_c"]) for sequence_id in sequence_ids)
        total_rank_i = sum(int(sequences[sequence_id]["rank_i"]) for sequence_id in sequence_ids)
        total_rank_p = sum(int(sequences[sequence_id]["rank_p"]) for sequence_id in sequence_ids)
        total_kernel_p = sum(int(sequences[sequence_id]["kernel_p_dim"]) for sequence_id in sequence_ids)
        defect = abs(total_kernel_p - total_rank_i)
        require_equal(total_a, int_cell(row, "total_dim_A"), f"{pushforward_id} total A")
        require_equal(total_b, int_cell(row, "total_dim_B"), f"{pushforward_id} total B")
        require_equal(total_c, int_cell(row, "total_dim_C"), f"{pushforward_id} total C")
        require_equal(total_rank_i, int_cell(row, "total_rank_injection"), f"{pushforward_id} total rank injection")
        require_equal(total_rank_p, int_cell(row, "total_rank_projection"), f"{pushforward_id} total rank projection")
        require_equal(total_kernel_p, int_cell(row, "total_kernel_projection_dim"), f"{pushforward_id} total kernel projection")
        require_equal(defect, int_cell(row, "pushforward_exact_defect_rank"), f"{pushforward_id} pushforward defect")
        require_zero(defect, f"{pushforward_id} pushforward defect")


def verify_zero_fibre_radicals(rows: list[dict[str, str]], degrees: dict[str, tuple[int, int, int]]) -> int:
    radical_count = 0
    for row in rows:
        check_row(row, "zero_fibre_radicals.csv")
        degree_id = row["degree_id"]
        if degrees.get(degree_id) != (0, 0, 0):
            raise ValueError(f"zero_fibre_radicals.csv: nonzero degree {degree_id}")
        basis = [item for item in row["basis_ids"].split(";") if item]
        radical_basis = [item for item in row["radical_basis_ids"].split(";") if item]
        dim = len(basis)
        require_equal(int_cell(row, "even_count") + int_cell(row, "odd_count"), dim, f"{degree_id} parity count")
        pairing = parse_matrix(row["pairing_matrix"], dim, dim, f"{degree_id} pairing")
        matrix_rank = rank(pairing)
        radical_dim = dim - matrix_rank
        quotient_dim = dim - radical_dim
        require_equal(matrix_rank, int_cell(row, "matrix_rank"), f"{degree_id} matrix rank")
        require_equal(radical_dim, int_cell(row, "radical_dim"), f"{degree_id} radical dim")
        require_equal(quotient_dim, int_cell(row, "quotient_dim"), f"{degree_id} quotient dim")
        require_equal(len(radical_basis), radical_dim, f"{degree_id} radical basis size")
        radical_count += 1
    return radical_count


def verify_relations(rows: list[dict[str, str]], sequence_count: int, radical_count: int) -> None:
    relation_values = {
        "zero_fibre_radical_defined": radical_count,
        "degreewise_exact": sequence_count,
        "pushforward_exact": 1,
        "finite_direct_sum_exact": 1,
        "hopf_radical_not_proved": 1,
        "bar_commutation_not_proved": 1,
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
        degrees = verify_degrees(tables["finite_degrees.csv"])
        sequences = verify_exact_sequences(tables["exact_sequences.csv"], degrees)
        verify_pushforwards(tables["pushforward_sums.csv"], sequences)
        radical_count = verify_zero_fibre_radicals(tables["zero_fibre_radicals.csv"], degrees)
        verify_relations(tables["formal_relations.csv"], len(sequences), radical_count)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"FIBRE_PUSHFORWARD_EXACTNESS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
