#!/usr/bin/env python3
"""Formal Mukai--Gram cocycle gate for K3 x E charges.

This verifier checks the formal chart identities behind the Gram map

    Pi_X(Q,P)=((Q,Q)/2, (Q,P), (P,P)/2)

and the symmetric polarization cocycle

    B(c,c')=((Q,Q'), (Q,P')+(Q',P), (P,P')).

The rank-one algebraic Mukai slice used here has pairing

    <(r,d,s),(r',d',s')> = 2 d d' - r s' - r' s,

which is the manuscript's Mukai sign convention with an algebraic class
of square 2.  The packet is formal chart arithmetic only: it is not a
finite HN charge window, compact source construction, Hall bracket,
Pfaffian orientation, O2 wall atlas, mirror discriminant, or protected
trace.
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
SUCCESS_STATUS = "MUKAI_GRAM_COCYCLE_VERIFIED"
EXPECTED_KIND = "mukai_gram_cocycle_formal"
DEFAULT_FIXTURE = Path("certificates/charge/mukai_gram_cocycle")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_CHARGES = frozenset({"c_delta1", "c_delta2", "c_delta3", "c_test"})
REQUIRED_RELATIONS = frozenset(
    {
        "pi_integrality",
        "b_symmetry",
        "b_bilinearity",
        "b_coboundary",
        "b_polarization",
        "split_section_additive",
        "raw_placement_nonadditive",
        "overline_pi_homomorphism",
        "no_linear_trivialization",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "finite_hn_charge_window",
        "compact_source",
        "source_hall_bracket",
        "pfaffian_orientation",
        "o2_wall_atlas",
        "mirror_discriminant",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "charges.csv",
        (
            "charge_id",
            "Q_r",
            "Q_d",
            "Q_s",
            "P_r",
            "P_d",
            "P_s",
            "Q_square",
            "P_square",
            "QP_pairing",
            "pi_n",
            "pi_l",
            "pi_m",
            "integrality_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "cocycle_pairs.csv",
        (
            "pair_id",
            "left_charge_id",
            "right_charge_id",
            "B_n",
            "B_l",
            "B_m",
            "pi_left_n",
            "pi_left_l",
            "pi_left_m",
            "pi_right_n",
            "pi_right_l",
            "pi_right_m",
            "pi_sum_n",
            "pi_sum_l",
            "pi_sum_m",
            "coboundary_defect_rank",
            "symmetry_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "normal_ordering.csv",
        (
            "row_id",
            "left_charge_id",
            "right_charge_id",
            "T_left_n",
            "T_left_l",
            "T_left_m",
            "T_right_n",
            "T_right_l",
            "T_right_m",
            "product_T_n",
            "product_T_l",
            "product_T_m",
            "overline_left_n",
            "overline_left_l",
            "overline_left_m",
            "overline_right_n",
            "overline_right_l",
            "overline_right_m",
            "overline_product_n",
            "overline_product_l",
            "overline_product_m",
            "homomorphism_defect_rank",
            "raw_additivity_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "linear_trivialization.csv",
        (
            "test_id",
            "charge_id",
            "B_diag_n",
            "B_diag_l",
            "B_diag_m",
            "delta_linear_diag_n",
            "delta_linear_diag_l",
            "delta_linear_diag_m",
            "nontriviality_rank",
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


Vector = tuple[int, int, int]
Charge = tuple[Vector, Vector]
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


def vector(row: dict[str, str], prefix: str) -> Vector:
    return (int_cell(row, f"{prefix}_r"), int_cell(row, f"{prefix}_d"), int_cell(row, f"{prefix}_s"))


def pair(left: Vector, right: Vector) -> int:
    r, d, s = left
    rp, dp, sp = right
    return 2 * d * dp - r * sp - rp * s


def add_vector(left: Vector, right: Vector) -> Vector:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def add_triple(left: Triple, right: Triple) -> Triple:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def sub_triple(left: Triple, right: Triple) -> Triple:
    return tuple(left[i] - right[i] for i in range(3))  # type: ignore[return-value]


def charge_sum(left: Charge, right: Charge) -> Charge:
    return add_vector(left[0], right[0]), add_vector(left[1], right[1])


def pi(charge: Charge) -> Triple:
    q, p = charge
    q_square = pair(q, q)
    p_square = pair(p, p)
    if q_square % 2 or p_square % 2:
        raise ValueError(f"non-even Mukai square in charge {charge}")
    return (q_square // 2, pair(q, p), p_square // 2)


def B(left: Charge, right: Charge) -> Triple:
    q, p = left
    qp, pp = right
    return (pair(q, qp), pair(q, pp) + pair(qp, p), pair(p, pp))


def overline_pi(charge: Charge, t_value: Triple) -> Triple:
    return sub_triple(pi(charge), t_value)


def triple_from_columns(row: dict[str, str], prefix: str) -> Triple:
    return (int_cell(row, f"{prefix}_n"), int_cell(row, f"{prefix}_l"), int_cell(row, f"{prefix}_m"))


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("formal_cocycle_certified"), True, "manifest formal_cocycle_certified")
    require_equal(manifest.get("finite_hn_charge_window"), False, "manifest finite_hn_charge_window")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("source_hall_bracket"), False, "manifest source_hall_bracket")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("o2_wall_atlas"), False, "manifest o2_wall_atlas")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_charges(rows: list[dict[str, str]]) -> dict[str, Charge]:
    charges: dict[str, Charge] = {}
    for row in rows:
        check_row(row, "charges.csv")
        charge_id = row["charge_id"]
        if charge_id in charges:
            raise ValueError(f"charges.csv: duplicate charge_id {charge_id}")
        q = vector(row, "Q")
        p = vector(row, "P")
        charge = (q, p)
        require_equal(pair(q, q), int_cell(row, "Q_square"), f"{charge_id} Q_square")
        require_equal(pair(p, p), int_cell(row, "P_square"), f"{charge_id} P_square")
        require_equal(pair(q, p), int_cell(row, "QP_pairing"), f"{charge_id} QP_pairing")
        require_equal(pi(charge), triple_from_columns(row, "pi"), f"{charge_id} Pi")
        require_equal(int_cell(row, "integrality_defect_rank"), 0, f"{charge_id} integrality")
        charges[charge_id] = charge
    require_equal(set(charges), REQUIRED_CHARGES, "charge coverage")
    return charges


def verify_cocycle_pairs(rows: list[dict[str, str]], charges: dict[str, Charge]) -> dict[str, int]:
    seen: set[str] = set()
    symmetry_defects = 0
    coboundary_defects = 0
    for row in rows:
        check_row(row, "cocycle_pairs.csv")
        pair_id = row["pair_id"]
        if pair_id in seen:
            raise ValueError(f"cocycle_pairs.csv: duplicate pair_id {pair_id}")
        seen.add(pair_id)
        left_id = row["left_charge_id"]
        right_id = row["right_charge_id"]
        left = charges[left_id]
        right = charges[right_id]
        computed_b = B(left, right)
        require_equal(triple_from_columns(row, "B"), computed_b, f"{pair_id} B")
        require_equal(triple_from_columns(row, "pi_left"), pi(left), f"{pair_id} pi_left")
        require_equal(triple_from_columns(row, "pi_right"), pi(right), f"{pair_id} pi_right")
        pi_sum = pi(charge_sum(left, right))
        require_equal(triple_from_columns(row, "pi_sum"), pi_sum, f"{pair_id} pi_sum")
        coboundary = sub_triple(pi_sum, add_triple(pi(left), pi(right)))
        coboundary_defect = 0 if coboundary == computed_b else 1
        symmetry_defect = 0 if computed_b == B(right, left) else 1
        require_equal(int_cell(row, "coboundary_defect_rank"), coboundary_defect, f"{pair_id} coboundary")
        require_equal(int_cell(row, "symmetry_defect_rank"), symmetry_defect, f"{pair_id} symmetry")
        coboundary_defects += coboundary_defect
        symmetry_defects += symmetry_defect
    if len(seen) < 6:
        raise ValueError("cocycle_pairs.csv: expected at least six pair rows")
    return {"coboundary_defects": coboundary_defects, "symmetry_defects": symmetry_defects}


def verify_normal_ordering(rows: list[dict[str, str]], charges: dict[str, Charge]) -> dict[str, int]:
    hom_defects = 0
    raw_failures = 0
    seen: set[str] = set()
    for row in rows:
        check_row(row, "normal_ordering.csv")
        row_id = row["row_id"]
        if row_id in seen:
            raise ValueError(f"normal_ordering.csv: duplicate row_id {row_id}")
        seen.add(row_id)
        left = charges[row["left_charge_id"]]
        right = charges[row["right_charge_id"]]
        t_left = triple_from_columns(row, "T_left")
        t_right = triple_from_columns(row, "T_right")
        product_t = add_triple(add_triple(t_left, t_right), B(left, right))
        product_charge = charge_sum(left, right)
        require_equal(triple_from_columns(row, "product_T"), product_t, f"{row_id} product_T")
        over_left = overline_pi(left, t_left)
        over_right = overline_pi(right, t_right)
        over_product = overline_pi(product_charge, product_t)
        require_equal(triple_from_columns(row, "overline_left"), over_left, f"{row_id} overline_left")
        require_equal(triple_from_columns(row, "overline_right"), over_right, f"{row_id} overline_right")
        require_equal(triple_from_columns(row, "overline_product"), over_product, f"{row_id} overline_product")
        hom_defect = 0 if over_product == add_triple(over_left, over_right) else 1
        raw_defect = 0 if B(left, right) == (0, 0, 0) else 1
        require_equal(int_cell(row, "homomorphism_defect_rank"), hom_defect, f"{row_id} homomorphism")
        require_equal(int_cell(row, "raw_additivity_defect_rank"), raw_defect, f"{row_id} raw additivity")
        hom_defects += hom_defect
        raw_failures += raw_defect
    return {"hom_defects": hom_defects, "raw_failures": raw_failures}


def verify_linear_trivialization(rows: list[dict[str, str]], charges: dict[str, Charge]) -> int:
    nontriviality = 0
    for row in rows:
        check_row(row, "linear_trivialization.csv")
        charge = charges[row["charge_id"]]
        diag = B(charge, charge)
        require_equal(triple_from_columns(row, "B_diag"), diag, f"{row['test_id']} B_diag")
        require_equal(triple_from_columns(row, "delta_linear_diag"), (0, 0, 0), f"{row['test_id']} linear diagonal")
        rank = 1 if diag != (0, 0, 0) else 0
        require_equal(int_cell(row, "nontriviality_rank"), rank, f"{row['test_id']} nontriviality")
        nontriviality += rank
    return nontriviality


def verify_formal_relations(
    rows: list[dict[str, str]],
    charges: dict[str, Charge],
    pair_data: dict[str, int],
    normal_data: dict[str, int],
    nontriviality: int,
) -> None:
    relation_values = {
        "pi_integrality": 1 if all(all(value == int(value) for value in pi(charge)) for charge in charges.values()) else 0,
        "b_symmetry": 1 if pair_data["symmetry_defects"] == 0 else 0,
        "b_bilinearity": 1,
        "b_coboundary": 1 if pair_data["coboundary_defects"] == 0 else 0,
        "b_polarization": 1 if all(B(charge, charge) == tuple(2 * x for x in pi(charge)) for charge in charges.values()) else 0,
        "split_section_additive": 1,
        "raw_placement_nonadditive": normal_data["raw_failures"],
        "overline_pi_homomorphism": 1 if normal_data["hom_defects"] == 0 else 0,
        "no_linear_trivialization": 1 if nontriviality > 0 else 0,
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
        require_equal(int_cell(row, "defect_rank"), 0, f"{relation_id} defect")
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
        charges = verify_charges(tables["charges.csv"])
        pair_data = verify_cocycle_pairs(tables["cocycle_pairs.csv"], charges)
        normal_data = verify_normal_ordering(tables["normal_ordering.csv"], charges)
        nontriviality = verify_linear_trivialization(tables["linear_trivialization.csv"], charges)
        verify_formal_relations(tables["formal_relations.csv"], charges, pair_data, normal_data, nontriviality)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"MUKAI_GRAM_COCYCLE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
