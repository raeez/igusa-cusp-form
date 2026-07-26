#!/usr/bin/env python3
"""Exact type-II Weyl-vector gate for the Delta_5 BKM lattice.

This verifier checks only target-side lattice arithmetic:

* the type-II simple roots in the fixed (f_2,f_3,f_-2) convention;
* the Cartan matrix 4 I_3 - 2 J_3 and discriminant -32;
* the isometry Lambda_II^{2,1} ~= U(4) + <2>;
* rho = 1/2(delta_1+delta_2+delta_3);
* (rho,delta_i)=-1, (rho,rho)=-3/2, and rho lies in the dual root lattice.

It does not construct a compact source, a Pfaffian orientation, an O2
wall atlas, a mirror discriminant, or a protected scalar trace.
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
SUCCESS_STATUS = "TYPE_II_WEYL_VECTOR_VERIFIED"
EXPECTED_KIND = "type_ii_weyl_vector_lattice"
AMBIENT_GRAM = (
    (Fraction(0), Fraction(0), Fraction(-1)),
    (Fraction(0), Fraction(2), Fraction(0)),
    (Fraction(-1), Fraction(0), Fraction(0)),
)
ROOTS = {
    "delta_1": (Fraction(2), Fraction(-1), Fraction(0)),
    "delta_2": (Fraction(0), Fraction(-1), Fraction(2)),
    "delta_3": (Fraction(0), Fraction(1), Fraction(0)),
}
ROOT_ORDER = ("delta_1", "delta_2", "delta_3")
RHO = (Fraction(1), Fraction(-1, 2), Fraction(1))
ISOMETRY_BASIS = {
    "u": (Fraction(1), Fraction(0), Fraction(1)),
    "v": (Fraction(0), Fraction(1), Fraction(1)),
    "h": (Fraction(0), Fraction(0), Fraction(1)),
}
EXPECTED_ISOMETRY_GRAM = {
    ("u", "u"): 0,
    ("u", "v"): -4,
    ("u", "h"): 0,
    ("v", "u"): -4,
    ("v", "v"): 0,
    ("v", "h"): 0,
    ("h", "u"): 0,
    ("h", "v"): 0,
    ("h", "h"): 2,
}
REQUIRED_RELATIONS = frozenset(
    {
        "cartan_matrix",
        "root_lattice_discriminant",
        "rho_half_sum",
        "rho_simple_pairings",
        "rho_norm",
        "rho_dual_membership",
        "u4_plus_2_isometry",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source",
        "pfaffian_orientation",
        "o2_wall_atlas",
        "mirror_discriminant",
        "protected_trace",
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
        "simple_roots.csv",
        (
            "root_id",
            "f2",
            "f3_num",
            "f3_den",
            "fm2",
            "square",
            "divisibility",
            "primitive",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cartan_matrix.csv",
        (
            "entry_id",
            "row_root",
            "col_root",
            "computed_pairing",
            "expected_pairing",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "isometry_basis.csv",
        (
            "basis_id",
            "delta1_coeff",
            "delta2_coeff",
            "delta3_coeff",
            "u_pair",
            "v_pair",
            "h_pair",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "weyl_vector.csv",
        (
            "vector_id",
            "f2_num",
            "f2_den",
            "f3_num",
            "f3_den",
            "fm2_num",
            "fm2_den",
            "delta1_coeff_num",
            "delta1_coeff_den",
            "delta2_coeff_num",
            "delta2_coeff_den",
            "delta3_coeff_num",
            "delta3_coeff_den",
            "pair_delta1",
            "pair_delta2",
            "pair_delta3",
            "norm_num",
            "norm_den",
            "dual_membership",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "lattice_relations.csv",
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
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/lattice/type_ii_weyl_vector"),
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


def fraction_cell(row: dict[str, str], num_key: str, den_key: str) -> Fraction:
    denominator = int_cell(row, den_key)
    if denominator == 0:
        raise ValueError(f"{den_key} is zero in row {row}")
    return Fraction(int_cell(row, num_key), denominator)


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


def pair(left: tuple[Fraction, Fraction, Fraction], right: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum(
        left[i] * AMBIENT_GRAM[i][j] * right[j]
        for i in range(3)
        for j in range(3)
    )


def root_combination(coeffs: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        sum(coeffs[i] * ROOTS[ROOT_ORDER[i]][j] for i in range(3))
        for j in range(3)
    )


def determinant_3(matrix: list[list[Fraction]]) -> Fraction:
    return (
        matrix[0][0] * matrix[1][1] * matrix[2][2]
        + matrix[0][1] * matrix[1][2] * matrix[2][0]
        + matrix[0][2] * matrix[1][0] * matrix[2][1]
        - matrix[0][2] * matrix[1][1] * matrix[2][0]
        - matrix[0][1] * matrix[1][0] * matrix[2][2]
        - matrix[0][0] * matrix[1][2] * matrix[2][1]
    )


def root_gram() -> list[list[Fraction]]:
    return [[pair(ROOTS[left], ROOTS[right]) for right in ROOT_ORDER] for left in ROOT_ORDER]


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("lattice_kind"), EXPECTED_KIND, "manifest lattice_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("lattice_arithmetic_certified"), True, "manifest lattice_arithmetic_certified")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("o2_wall_atlas"), False, "manifest o2_wall_atlas")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_simple_roots(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "simple_roots.csv")
        root_id = row["root_id"]
        if root_id in seen:
            raise ValueError(f"simple_roots.csv: duplicate root_id {root_id}")
        seen.add(root_id)
        if root_id not in ROOTS:
            raise ValueError(f"simple_roots.csv: unexpected root_id {root_id}")
        displayed = (
            Fraction(int_cell(row, "f2")),
            fraction_cell(row, "f3_num", "f3_den"),
            Fraction(int_cell(row, "fm2")),
        )
        root = ROOTS[root_id]
        require_equal(displayed, root, f"{root_id} coordinates")
        require_equal(pair(root, root), int_cell(row, "square"), f"{root_id} square")
        require_equal(int_cell(row, "divisibility"), 2, f"{root_id} divisibility")
        require_equal(bool_cell(row, "primitive"), True, f"{root_id} primitive")
    require_equal(seen, set(ROOTS), "simple root coverage")


def verify_cartan_matrix(rows: list[dict[str, str]]) -> None:
    seen: set[tuple[str, str]] = set()
    for row in rows:
        check_row(row, "cartan_matrix.csv")
        key = (row["row_root"], row["col_root"])
        if key in seen:
            raise ValueError(f"cartan_matrix.csv: duplicate entry {key}")
        seen.add(key)
        if key[0] not in ROOTS or key[1] not in ROOTS:
            raise ValueError(f"cartan_matrix.csv: unknown root in {key}")
        computed = pair(ROOTS[key[0]], ROOTS[key[1]])
        require_equal(int_cell(row, "computed_pairing"), int(computed), f"{row['entry_id']} computed")
        require_equal(int_cell(row, "expected_pairing"), int(computed), f"{row['entry_id']} expected")
    require_equal(seen, {(left, right) for left in ROOT_ORDER for right in ROOT_ORDER}, "cartan entry coverage")


def verify_isometry_basis(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    basis_vectors: dict[str, tuple[Fraction, Fraction, Fraction]] = {}
    for row in rows:
        check_row(row, "isometry_basis.csv")
        basis_id = row["basis_id"]
        if basis_id in seen:
            raise ValueError(f"isometry_basis.csv: duplicate basis_id {basis_id}")
        seen.add(basis_id)
        if basis_id not in ISOMETRY_BASIS:
            raise ValueError(f"isometry_basis.csv: unexpected basis_id {basis_id}")
        coeffs = (
            Fraction(int_cell(row, "delta1_coeff")),
            Fraction(int_cell(row, "delta2_coeff")),
            Fraction(int_cell(row, "delta3_coeff")),
        )
        require_equal(coeffs, ISOMETRY_BASIS[basis_id], f"{basis_id} coefficients")
        vector = root_combination(coeffs)
        basis_vectors[basis_id] = vector
    require_equal(seen, set(ISOMETRY_BASIS), "isometry basis coverage")
    for row in rows:
        basis_id = row["basis_id"]
        vector = basis_vectors[basis_id]
        for other_id, column in (("u", "u_pair"), ("v", "v_pair"), ("h", "h_pair")):
            computed = pair(vector, basis_vectors[other_id])
            require_equal(int_cell(row, column), int(computed), f"{basis_id} {column}")
            require_equal(int(computed), EXPECTED_ISOMETRY_GRAM[(basis_id, other_id)], f"{basis_id} target {column}")


def verify_weyl_vector(rows: list[dict[str, str]]) -> None:
    if len(rows) != 1:
        raise ValueError("weyl_vector.csv: expected exactly one row")
    row = rows[0]
    check_row(row, "weyl_vector.csv")
    require_equal(row["vector_id"], "rho", "vector_id")
    displayed = (
        fraction_cell(row, "f2_num", "f2_den"),
        fraction_cell(row, "f3_num", "f3_den"),
        fraction_cell(row, "fm2_num", "fm2_den"),
    )
    require_equal(displayed, RHO, "rho coordinates")
    coeffs = (
        fraction_cell(row, "delta1_coeff_num", "delta1_coeff_den"),
        fraction_cell(row, "delta2_coeff_num", "delta2_coeff_den"),
        fraction_cell(row, "delta3_coeff_num", "delta3_coeff_den"),
    )
    require_equal(coeffs, (Fraction(1, 2), Fraction(1, 2), Fraction(1, 2)), "rho delta coefficients")
    require_equal(root_combination(coeffs), RHO, "rho half-sum")
    for root_id, key in (("delta_1", "pair_delta1"), ("delta_2", "pair_delta2"), ("delta_3", "pair_delta3")):
        require_equal(int_cell(row, key), int(pair(RHO, ROOTS[root_id])), f"rho {root_id}")
        require_equal(int_cell(row, key), -1, f"rho {root_id} expected")
    norm = pair(RHO, RHO)
    require_equal(fraction_cell(row, "norm_num", "norm_den"), norm, "rho norm")
    require_equal(norm, Fraction(-3, 2), "rho norm expected")
    require_equal(bool_cell(row, "dual_membership"), True, "rho dual membership")
    if not all(pair(RHO, ROOTS[root_id]).denominator == 1 for root_id in ROOT_ORDER):
        raise ValueError("rho is not in the dual root lattice")


def verify_lattice_relations(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    gram = root_gram()
    relation_values = {
        "cartan_matrix": 1 if gram == [[Fraction(2), Fraction(-2), Fraction(-2)], [Fraction(-2), Fraction(2), Fraction(-2)], [Fraction(-2), Fraction(-2), Fraction(2)]] else 0,
        "root_lattice_discriminant": int(determinant_3(gram)),
        "rho_half_sum": 1 if root_combination((Fraction(1, 2), Fraction(1, 2), Fraction(1, 2))) == RHO else 0,
        "rho_simple_pairings": 1 if all(pair(RHO, ROOTS[root_id]) == -1 for root_id in ROOT_ORDER) else 0,
        "rho_norm": -3,
        "rho_dual_membership": 1 if all(pair(RHO, ROOTS[root_id]).denominator == 1 for root_id in ROOT_ORDER) else 0,
        "u4_plus_2_isometry": 1,
    }
    for row in rows:
        check_row(row, "lattice_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"lattice_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"lattice_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed_value")
        require_equal(int_cell(row, "computed_value"), int_cell(row, "expected_value"), f"{relation_id} expected_value")
        require_equal(int_cell(row, "defect_rank"), 0, f"{relation_id} defect_rank")
    require_equal(seen, REQUIRED_RELATIONS, "lattice relation coverage")


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
        verify_simple_roots(tables["simple_roots.csv"])
        verify_cartan_matrix(tables["cartan_matrix.csv"])
        verify_isometry_basis(tables["isometry_basis.csv"])
        verify_weyl_vector(tables["weyl_vector.csv"])
        verify_lattice_relations(tables["lattice_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TYPE_II_WEYL_VECTOR_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
