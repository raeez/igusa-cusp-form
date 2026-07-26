#!/usr/bin/env python3
"""Formal Gram-fibre and kernel gate for the Mukai--Gram map.

This verifier checks the finite formal arithmetic needed before a
finite Hall charge window can use the Gram projection:

* charges with the same Gram label are grouped and their parity blocks
  are summed separately;
* the kernel of Pi_X is the zero Gram fibre
  { (Q,P) | Q^2=P^2=Q.P=0 };
* this kernel is not an additive subgroup of the formal charge lattice;
* alpha(Pi_X) vanishes on kernel rows;
* signed superdimension is not used as a substitute for parity blocks.

The packet is formal lattice and bookkeeping arithmetic only.  It does
not prove algebraic effectivity, finite HN boundedness, compact Hall
support, source Hall brackets, Hopf radical ideal/coideal properties,
exactness of a finite-window pushforward, Pfaffian orientations, or
protected traces.
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
SUCCESS_STATUS = "GRAM_FIBRE_KERNEL_VERIFIED"
EXPECTED_KIND = "gram_fibre_kernel_formal_mukai"
DEFAULT_FIXTURE = Path("certificates/charge/gram_fibre_kernel")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "same_gram_summed",
        "kernel_defined",
        "kernel_not_subgroup",
        "alpha_zero_on_kernel",
        "parity_profile_not_signed_only",
        "radical_not_proved",
        "exactness_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "finite_hn_charge_window",
        "compact_source",
        "source_hall_bracket",
        "source_parity_proof",
        "radical_ideal_coideal",
        "exact_pushforward",
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
        "formal_charges.csv",
        (
            "charge_id",
            "Q_e1",
            "Q_f1",
            "Q_e2",
            "Q_f2",
            "P_e1",
            "P_f1",
            "P_e2",
            "P_f2",
            "pi_n",
            "pi_l",
            "pi_m",
            "alpha_f2",
            "alpha_f3",
            "alpha_fm2",
            "gram_label",
            "parity",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "same_gram_sums.csv",
        (
            "sum_id",
            "gram_label",
            "pi_n",
            "pi_l",
            "pi_m",
            "source_charge_ids",
            "total_count",
            "even_count",
            "odd_count",
            "signed_superdimension",
            "parity_profile_recorded",
            "hidden_zero_superdimension_excluded",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "kernel_rows.csv",
        (
            "kernel_id",
            "charge_id",
            "Q_e1",
            "Q_f1",
            "Q_e2",
            "Q_f2",
            "P_e1",
            "P_f1",
            "P_e2",
            "P_f2",
            "pi_n",
            "pi_l",
            "pi_m",
            "nonzero_charge",
            "wedge_gcd",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "kernel_nonadditivity.csv",
        (
            "test_id",
            "left_kernel_id",
            "right_kernel_id",
            "sum_Q_e1",
            "sum_Q_f1",
            "sum_Q_e2",
            "sum_Q_f2",
            "sum_P_e1",
            "sum_P_f1",
            "sum_P_e2",
            "sum_P_f2",
            "sum_pi_n",
            "sum_pi_l",
            "sum_pi_m",
            "kernel_closed_under_addition",
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


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_zero(value: int, label: str) -> None:
    if value != 0:
        raise ValueError(f"{label}: expected 0, got {value}")


def check_row(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    if not row.get("source_reference", "").strip():
        raise ValueError(f"{table_name}: missing source_reference: {row}")
    haystack = " ".join(row.values()).lower()
    for token in FORBIDDEN_TOKENS:
        if token in haystack:
            raise ValueError(f"{table_name}: forbidden token {token!r} in {row}")


def pair(left: Vector, right: Vector) -> int:
    e1, f1, e2, f2 = left
    e1p, f1p, e2p, f2p = right
    return e1 * f1p + f1 * e1p + e2 * f2p + f2 * e2p


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
    gcd = 0
    for coeff in coeffs:
        gcd = math.gcd(gcd, coeff)
    return gcd


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
    require_equal(manifest.get("formal_gram_fibre_kernel_certified"), True, "manifest formal_gram_fibre_kernel_certified")
    require_equal(manifest.get("finite_hn_charge_window"), False, "manifest finite_hn_charge_window")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("source_hall_bracket"), False, "manifest source_hall_bracket")
    require_equal(manifest.get("source_parity_certification"), False, "manifest source_parity_certification")
    require_equal(manifest.get("radical_certification"), False, "manifest radical_certification")
    require_equal(manifest.get("pushforward_exactness"), False, "manifest pushforward_exactness")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_formal_charges(rows: list[dict[str, str]]) -> dict[str, dict[str, object]]:
    charges: dict[str, dict[str, object]] = {}
    for row in rows:
        check_row(row, "formal_charges.csv")
        charge_id = row["charge_id"]
        if charge_id in charges:
            raise ValueError(f"formal_charges.csv: duplicate charge_id {charge_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"formal_charges.csv: bad parity {parity!r}")
        q = vector_from_row(row, "Q")
        p = vector_from_row(row, "P")
        pi_value = pi(q, p)
        require_equal(pi_value, triple_from_row(row, "pi"), f"{charge_id} Pi")
        require_equal(alpha(pi_value), alpha_from_row(row), f"{charge_id} alpha")
        charges[charge_id] = {
            "q": q,
            "p": p,
            "pi": pi_value,
            "alpha": alpha(pi_value),
            "gram_label": row["gram_label"],
            "parity": parity,
        }
    return charges


def verify_same_gram_sums(rows: list[dict[str, str]], charges: dict[str, dict[str, object]]) -> int:
    seen: set[str] = set()
    hidden_zero_rows = 0
    for row in rows:
        check_row(row, "same_gram_sums.csv")
        sum_id = row["sum_id"]
        if sum_id in seen:
            raise ValueError(f"same_gram_sums.csv: duplicate sum_id {sum_id}")
        seen.add(sum_id)
        ids = [item for item in row["source_charge_ids"].split(";") if item]
        if not ids:
            raise ValueError(f"same_gram_sums.csv: empty source_charge_ids in {row}")
        for charge_id in ids:
            if charge_id not in charges:
                raise ValueError(f"same_gram_sums.csv: unknown charge_id {charge_id}")
        gram_label = row["gram_label"]
        if any(charges[charge_id]["gram_label"] != gram_label for charge_id in ids):
            raise ValueError(f"same_gram_sums.csv: mixed Gram labels in {row}")
        pi_values = {charges[charge_id]["pi"] for charge_id in ids}
        if len(pi_values) != 1:
            raise ValueError(f"same_gram_sums.csv: mixed Pi values in {row}")
        pi_value = next(iter(pi_values))
        require_equal(pi_value, triple_from_row(row, "pi"), f"{sum_id} Pi")
        even_count = sum(1 for charge_id in ids if charges[charge_id]["parity"] == "even")
        odd_count = sum(1 for charge_id in ids if charges[charge_id]["parity"] == "odd")
        total_count = len(ids)
        signed = even_count - odd_count
        require_equal(int_cell(row, "total_count"), total_count, f"{sum_id} total_count")
        require_equal(int_cell(row, "even_count"), even_count, f"{sum_id} even_count")
        require_equal(int_cell(row, "odd_count"), odd_count, f"{sum_id} odd_count")
        require_equal(int_cell(row, "signed_superdimension"), signed, f"{sum_id} signed")
        require_equal(bool_cell(row, "parity_profile_recorded"), True, f"{sum_id} parity_profile_recorded")
        hidden_excluded = total_count > 0 and bool_cell(row, "parity_profile_recorded")
        require_equal(bool_cell(row, "hidden_zero_superdimension_excluded"), hidden_excluded, f"{sum_id} hidden exclusion")
        if total_count > abs(signed):
            hidden_zero_rows += 1
    return hidden_zero_rows


def verify_kernel_rows(rows: list[dict[str, str]], charges: dict[str, dict[str, object]]) -> dict[str, str]:
    kernels: dict[str, str] = {}
    for row in rows:
        check_row(row, "kernel_rows.csv")
        kernel_id = row["kernel_id"]
        if kernel_id in kernels:
            raise ValueError(f"kernel_rows.csv: duplicate kernel_id {kernel_id}")
        charge_id = row["charge_id"]
        if charge_id not in charges:
            raise ValueError(f"kernel_rows.csv: unknown charge_id {charge_id}")
        q = vector_from_row(row, "Q")
        p = vector_from_row(row, "P")
        require_equal(q, charges[charge_id]["q"], f"{kernel_id} Q")
        require_equal(p, charges[charge_id]["p"], f"{kernel_id} P")
        require_equal(pi(q, p), (0, 0, 0), f"{kernel_id} kernel Pi")
        require_equal(triple_from_row(row, "pi"), (0, 0, 0), f"{kernel_id} row Pi")
        require_equal(alpha(pi(q, p)), (0, 0, 0), f"{kernel_id} alpha")
        require_equal(bool_cell(row, "nonzero_charge"), q != (0, 0, 0, 0) or p != (0, 0, 0, 0), f"{kernel_id} nonzero")
        require_equal(int_cell(row, "wedge_gcd"), wedge_gcd(q, p), f"{kernel_id} wedge_gcd")
        kernels[kernel_id] = charge_id
    return kernels


def verify_kernel_nonadditivity(rows: list[dict[str, str]], kernels: dict[str, str], charges: dict[str, dict[str, object]]) -> int:
    failures = 0
    seen: set[str] = set()
    for row in rows:
        check_row(row, "kernel_nonadditivity.csv")
        test_id = row["test_id"]
        if test_id in seen:
            raise ValueError(f"kernel_nonadditivity.csv: duplicate test_id {test_id}")
        seen.add(test_id)
        left_id = row["left_kernel_id"]
        right_id = row["right_kernel_id"]
        if left_id not in kernels or right_id not in kernels:
            raise ValueError(f"kernel_nonadditivity.csv: unknown kernel id in {row}")
        left = charges[kernels[left_id]]
        right = charges[kernels[right_id]]
        sum_q = tuple(a + b for a, b in zip(left["q"], right["q"]))  # type: ignore[arg-type]
        sum_p = tuple(a + b for a, b in zip(left["p"], right["p"]))  # type: ignore[arg-type]
        require_equal(sum_q, vector_from_row(row, "sum_Q"), f"{test_id} sum Q")
        require_equal(sum_p, vector_from_row(row, "sum_P"), f"{test_id} sum P")
        sum_pi = pi(sum_q, sum_p)
        require_equal(sum_pi, triple_from_row(row, "sum_pi"), f"{test_id} sum Pi")
        closed = sum_pi == (0, 0, 0)
        require_equal(bool_cell(row, "kernel_closed_under_addition"), closed, f"{test_id} closed flag")
        if not closed:
            failures += 1
    if failures == 0:
        raise ValueError("kernel_nonadditivity.csv: expected at least one non-closure witness")
    return failures


def verify_relations(rows: list[dict[str, str]], hidden_zero_rows: int, kernel_count: int, nonadditivity_count: int) -> None:
    relation_values = {
        "same_gram_summed": 3,
        "kernel_defined": kernel_count,
        "kernel_not_subgroup": 1 if nonadditivity_count else 0,
        "alpha_zero_on_kernel": 1,
        "parity_profile_not_signed_only": 1 if hidden_zero_rows else 0,
        "radical_not_proved": 1,
        "exactness_not_proved": 1,
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
        require_zero(int_cell(row, "defect_rank"), f"{relation_id} defect_rank")
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
        charges = verify_formal_charges(tables["formal_charges.csv"])
        hidden_zero_rows = verify_same_gram_sums(tables["same_gram_sums.csv"], charges)
        kernels = verify_kernel_rows(tables["kernel_rows.csv"], charges)
        nonadditivity_count = verify_kernel_nonadditivity(tables["kernel_nonadditivity.csv"], kernels, charges)
        verify_relations(tables["formal_relations.csv"], hidden_zero_rows, len(kernels), nonadditivity_count)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"GRAM_FIBRE_KERNEL_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
