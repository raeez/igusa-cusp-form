#!/usr/bin/env python3
"""Formal primitive lift gate for Mukai--Gram triples.

This verifier checks the formal primitive lift formula

    Q=e_1+n f_1,    P=l f_1+e_2+m f_2

inside two orthogonal hyperbolic planes U_1+U_2.  With pairings
(e_i,f_i)=1 and all other cross-plane pairings zero, it verifies

    Q^2=2n,  P^2=2m,  Q.P=l,  Pi_X(Q,P)=(n,l,m),

the unimodular primitive minor in rows e_1,e_2, the wedge torsion
invariant gcd(Q wedge P)=1, and the target root grading

    alpha(Pi_X(Q,P)) = 2n f_2 - l f_3 + 2m f_-2.

The packet is formal lattice arithmetic only.  It does not prove
algebraicity, effectivity, finite HN boundedness, compact Hall support,
source Hall brackets, Pfaffian orientations, O2 wall atlases, mirror
discriminants, or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "FORMAL_PRIMITIVE_LIFT_VERIFIED"
EXPECTED_KIND = "formal_primitive_lift_mukai_gram"
DEFAULT_FIXTURE = Path("certificates/charge/formal_primitive_lift")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_SAMPLE_ROWS = frozenset(
    {
        "zero",
        "delta1",
        "delta2",
        "delta3",
        "delta123",
        "mixed_test",
    }
)
REQUIRED_RELATIONS = frozenset(
    {
        "universal_formula",
        "pi_surjective_on_samples",
        "primitive_minor_one",
        "wedge_torsion_one",
        "alpha_pi_root_map",
        "formal_not_effective",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "algebraic_effectivity",
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
        "universal_formula.csv",
        (
            "formula_id",
            "Q_e1_const",
            "Q_f1_n_coeff",
            "Q_e2_const",
            "Q_f2_const",
            "P_e1_const",
            "P_f1_l_coeff",
            "P_e2_const",
            "P_f2_m_coeff",
            "primitive_minor_e1_e2",
            "wedge_e1_e2_coeff",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "sample_lifts.csv",
        (
            "lift_id",
            "n",
            "l",
            "m",
            "Q_e1",
            "Q_f1",
            "Q_e2",
            "Q_f2",
            "P_e1",
            "P_f1",
            "P_e2",
            "P_f2",
            "Q_square",
            "P_square",
            "QP_pairing",
            "pi_n",
            "pi_l",
            "pi_m",
            "alpha_f2",
            "alpha_f3",
            "alpha_fm2",
            "primitive_minor_e1_e2",
            "wedge_gcd",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "root_grading.csv",
        (
            "grading_id",
            "lift_id",
            "pi_n",
            "pi_l",
            "pi_m",
            "alpha_f2",
            "alpha_f3",
            "alpha_fm2",
            "root_map_residual_rank",
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


Vector = tuple[int, int, int, int]
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


def pair(left: Vector, right: Vector) -> int:
    e1, f1, e2, f2 = left
    e1p, f1p, e2p, f2p = right
    return e1 * f1p + f1 * e1p + e2 * f2p + f2 * e2p


def formal_lift(n: int, l: int, m: int) -> tuple[Vector, Vector]:
    return (1, n, 0, 0), (0, l, 1, m)


def pi(q: Vector, p: Vector) -> Triple:
    q_square = pair(q, q)
    p_square = pair(p, p)
    if q_square % 2 or p_square % 2:
        raise ValueError(f"non-even square for q={q}, p={p}")
    return q_square // 2, pair(q, p), p_square // 2


def alpha(triple: Triple) -> Triple:
    n, l, m = triple
    return 2 * n, -l, 2 * m


def wedge_coefficients(q: Vector, p: Vector) -> list[int]:
    coeffs: list[int] = []
    for i in range(4):
        for j in range(i + 1, 4):
            coeffs.append(q[i] * p[j] - q[j] * p[i])
    return coeffs


def wedge_gcd(q: Vector, p: Vector) -> int:
    coeffs = [abs(value) for value in wedge_coefficients(q, p)]
    return math.gcd(math.gcd(math.gcd(math.gcd(coeffs[0], coeffs[1]), coeffs[2]), coeffs[3]), math.gcd(coeffs[4], coeffs[5]))


def primitive_minor(q: Vector, p: Vector) -> int:
    # Rows e_1 and e_2 of the 4 x 2 coefficient matrix.
    return q[0] * p[2] - q[2] * p[0]


def vector_from_row(row: dict[str, str], prefix: str) -> Vector:
    return (
        int_cell(row, f"{prefix}_e1"),
        int_cell(row, f"{prefix}_f1"),
        int_cell(row, f"{prefix}_e2"),
        int_cell(row, f"{prefix}_f2"),
    )


def triple_from_row(row: dict[str, str], prefix: str) -> Triple:
    return (
        int_cell(row, f"{prefix}_n"),
        int_cell(row, f"{prefix}_l"),
        int_cell(row, f"{prefix}_m"),
    )


def alpha_from_row(row: dict[str, str]) -> Triple:
    return (
        int_cell(row, "alpha_f2"),
        int_cell(row, "alpha_f3"),
        int_cell(row, "alpha_fm2"),
    )


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("formal_primitive_lift_certified"), True, "manifest formal_primitive_lift_certified")
    require_equal(manifest.get("finite_hn_charge_window"), False, "manifest finite_hn_charge_window")
    require_equal(manifest.get("algebraic_effectivity"), False, "manifest algebraic_effectivity")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("source_hall_bracket"), False, "manifest source_hall_bracket")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("o2_wall_atlas"), False, "manifest o2_wall_atlas")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_universal_formula(rows: list[dict[str, str]]) -> None:
    if len(rows) != 1:
        raise ValueError("universal_formula.csv: expected one row")
    row = rows[0]
    check_row(row, "universal_formula.csv")
    require_equal(row["formula_id"], "Q_e1_plus_n_f1__P_l_f1_plus_e2_plus_m_f2", "formula_id")
    require_equal(int_cell(row, "Q_e1_const"), 1, "Q_e1_const")
    require_equal(int_cell(row, "Q_f1_n_coeff"), 1, "Q_f1_n_coeff")
    require_equal(int_cell(row, "Q_e2_const"), 0, "Q_e2_const")
    require_equal(int_cell(row, "Q_f2_const"), 0, "Q_f2_const")
    require_equal(int_cell(row, "P_e1_const"), 0, "P_e1_const")
    require_equal(int_cell(row, "P_f1_l_coeff"), 1, "P_f1_l_coeff")
    require_equal(int_cell(row, "P_e2_const"), 1, "P_e2_const")
    require_equal(int_cell(row, "P_f2_m_coeff"), 1, "P_f2_m_coeff")
    q, p = formal_lift(7, -5, 3)
    require_equal(primitive_minor(q, p), int_cell(row, "primitive_minor_e1_e2"), "symbolic primitive minor")
    require_equal(wedge_coefficients(q, p)[1], int_cell(row, "wedge_e1_e2_coeff"), "symbolic wedge e1e2")


def verify_sample_lifts(rows: list[dict[str, str]]) -> dict[str, dict[str, Triple]]:
    seen: set[str] = set()
    samples: dict[str, dict[str, Triple]] = {}
    for row in rows:
        check_row(row, "sample_lifts.csv")
        lift_id = row["lift_id"]
        if lift_id in seen:
            raise ValueError(f"sample_lifts.csv: duplicate lift_id {lift_id}")
        seen.add(lift_id)
        n, l, m = int_cell(row, "n"), int_cell(row, "l"), int_cell(row, "m")
        q, p = formal_lift(n, l, m)
        require_equal(vector_from_row(row, "Q"), q, f"{lift_id} Q")
        require_equal(vector_from_row(row, "P"), p, f"{lift_id} P")
        require_equal(pair(q, q), int_cell(row, "Q_square"), f"{lift_id} Q_square")
        require_equal(pair(p, p), int_cell(row, "P_square"), f"{lift_id} P_square")
        require_equal(pair(q, p), int_cell(row, "QP_pairing"), f"{lift_id} QP_pairing")
        pi_value = pi(q, p)
        require_equal(pi_value, triple_from_row(row, "pi"), f"{lift_id} Pi")
        alpha_value = alpha(pi_value)
        require_equal(alpha_value, alpha_from_row(row), f"{lift_id} alpha")
        require_equal(primitive_minor(q, p), int_cell(row, "primitive_minor_e1_e2"), f"{lift_id} primitive minor")
        require_equal(int_cell(row, "primitive_minor_e1_e2"), 1, f"{lift_id} primitive minor expected")
        require_equal(wedge_gcd(q, p), int_cell(row, "wedge_gcd"), f"{lift_id} wedge gcd")
        require_equal(int_cell(row, "wedge_gcd"), 1, f"{lift_id} wedge gcd expected")
        samples[lift_id] = {"pi": pi_value, "alpha": alpha_value}
    require_equal(seen, REQUIRED_SAMPLE_ROWS, "sample lift coverage")
    return samples


def verify_root_grading(rows: list[dict[str, str]], samples: dict[str, dict[str, Triple]]) -> int:
    residuals = 0
    seen: set[str] = set()
    for row in rows:
        check_row(row, "root_grading.csv")
        grading_id = row["grading_id"]
        if grading_id in seen:
            raise ValueError(f"root_grading.csv: duplicate grading_id {grading_id}")
        seen.add(grading_id)
        lift_id = row["lift_id"]
        if lift_id not in samples:
            raise ValueError(f"root_grading.csv: unknown lift_id {lift_id}")
        pi_value = triple_from_row(row, "pi")
        alpha_value = alpha_from_row(row)
        require_equal(pi_value, samples[lift_id]["pi"], f"{grading_id} pi")
        require_equal(alpha_value, samples[lift_id]["alpha"], f"{grading_id} alpha")
        residual = 0 if alpha_value == alpha(pi_value) else 1
        require_equal(int_cell(row, "root_map_residual_rank"), residual, f"{grading_id} residual")
        residuals += residual
    require_equal({row["lift_id"] for row in rows}, set(samples), "root grading lift coverage")
    return residuals


def verify_formal_relations(rows: list[dict[str, str]], samples: dict[str, dict[str, Triple]], root_residuals: int) -> None:
    relation_values = {
        "universal_formula": 1,
        "pi_surjective_on_samples": len(samples),
        "primitive_minor_one": 1,
        "wedge_torsion_one": 1,
        "alpha_pi_root_map": 1 if root_residuals == 0 else 0,
        "formal_not_effective": 1,
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
        verify_universal_formula(tables["universal_formula.csv"])
        samples = verify_sample_lifts(tables["sample_lifts.csv"])
        residuals = verify_root_grading(tables["root_grading.csv"], samples)
        verify_formal_relations(tables["formal_relations.csv"], samples, residuals)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"FORMAL_PRIMITIVE_LIFT_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
