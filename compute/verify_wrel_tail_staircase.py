#!/usr/bin/env python3
"""Symbolic six-row tail certificate for the W_rel target-degree audit.

The finite W_rel degree-closure verifier reaches the six-row layer
called ``third_six_row_saturation_real_string_saturation_extension``.
From that point the same two symbolic transitions repeat.

For an even integer N >= 14 define

    A_N = {(0,N,N-1), (0,N,N), (0,N+1,N),
           (N,0,N-1), (N,0,N), (N+1,0,N)}

and

    B_N = {(0,N,N+1), (0,N+1,N+1), (0,N+1,N+2),
           (N,0,N+1), (N+1,0,N+1), (N+1,0,N+2)}.

This verifier checks, by affine arithmetic in N, that real-root terminal
relations through A_N force zero terminal codomains whose downward
saturation contains B_N, and that real-root terminal relations through
B_N force zero terminal codomains whose downward saturation contains
A_{N+2}.  The nonzero multiplicities of the six next rows are the
q^0 coefficients y^{-1}, 10, y of phi_{0,1}.  This is a target-degree
tail certificate only; it is not a compact source construction.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from verify_square_root import phi_01_coefficients


SUCCESS_STATUS = "WREL_TAIL_STAIRCASE_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/targets/delta5_gn_kac/wrel_tail_staircase")
DEFAULT_WREL_FIXTURE = Path("certificates/targets/delta5_gn_kac/wrel_degree_closure")
N_MIN = 14

TABLE_COLUMNS = (
    "check_id",
    "transition_id",
    "parameter_condition",
    "input_pattern",
    "next_pattern",
    "next_degree_formula",
    "next_signed_dimension",
    "witness_input_formula",
    "witness_real_root",
    "pairing_formula",
    "serre_exponent_formula",
    "terminal_formula",
    "terminal_signed_dimension",
    "subdegree_check",
    "proof_reference",
    "check_status",
    "notes",
)

ANCHOR_COLUMNS = (
    "degree_id",
    "beta_c1",
    "beta_c2",
    "beta_c3",
    "signed_dimension",
    "source_table",
    "proof_reference",
    "check_status",
    "notes",
)

UNBOUNDED_COLUMNS = (
    "sequence_id",
    "parameter_condition",
    "degree_family",
    "representative_degree_formula",
    "unbounded_coordinate",
    "coordinate_formula",
    "induction_source",
    "proof_reference",
    "check_status",
    "notes",
)

ANCHOR_SOURCE_TABLE = "six_row_saturation_real_string_saturation_extension.csv"


@dataclass(frozen=True)
class Lin:
    coefficient: int
    constant: int = 0

    def __add__(self, other: Lin | int) -> Lin:
        other = to_lin(other)
        return Lin(self.coefficient + other.coefficient, self.constant + other.constant)

    def __radd__(self, other: Lin | int) -> Lin:
        return self + other

    def __sub__(self, other: Lin | int) -> Lin:
        other = to_lin(other)
        return Lin(self.coefficient - other.coefficient, self.constant - other.constant)

    def __rsub__(self, other: Lin | int) -> Lin:
        return to_lin(other) - self

    def __mul__(self, scale: int) -> Lin:
        return Lin(scale * self.coefficient, scale * self.constant)

    def __rmul__(self, scale: int) -> Lin:
        return self * scale

    def value(self, n_value: int) -> int:
        return self.coefficient * n_value + self.constant

    def is_zero(self) -> bool:
        return self.coefficient == 0 and self.constant == 0

    def is_nonnegative_for_tail(self) -> bool:
        return self.coefficient >= 0 and self.value(N_MIN) >= 0

    def is_negative_for_tail(self) -> bool:
        return self.coefficient <= 0 and self.value(N_MIN) < 0

    def __str__(self) -> str:
        if self.coefficient == 0:
            return str(self.constant)
        head = "N" if self.coefficient == 1 else f"{self.coefficient}N"
        if self.constant == 0:
            return head
        sign = "+" if self.constant > 0 else "-"
        return f"{head}{sign}{abs(self.constant)}"


def to_lin(value: Lin | int) -> Lin:
    if isinstance(value, Lin):
        return value
    return Lin(0, value)


ZERO = Lin(0, 0)
ONE = Lin(0, 1)
N = Lin(1, 0)

LinBeta = tuple[Lin, Lin, Lin]


def beta_text(beta: LinBeta) -> str:
    return f"({beta[0]},{beta[1]},{beta[2]})"


def beta_degree_id(beta: tuple[int, int, int]) -> str:
    return f"beta_{beta[0]}_{beta[1]}_{beta[2]}"


def linbeta_to_int(beta: LinBeta, n_value: int) -> tuple[int, int, int]:
    return tuple(component.value(n_value) for component in beta)  # type: ignore[return-value]


def lin_pair(left: LinBeta, right: LinBeta) -> Lin:
    c1, c2, c3 = left
    d1, d2, d3 = right
    c1_scalar, c2_scalar, c3_scalar = c1.value(0), c2.value(0), c3.value(0)
    return (
        2 * c1_scalar * d1
        + 2 * c2_scalar * d2
        + 2 * c3_scalar * d3
        - 2 * (c1_scalar * d2 + c2_scalar * d1)
        - 2 * (c1_scalar * d3 + c3_scalar * d1)
        - 2 * (c2_scalar * d3 + c3_scalar * d2)
    )


def real_roots() -> dict[str, LinBeta]:
    return {
        "delta_1": (ONE, ZERO, ZERO),
        "delta_2": (ZERO, ONE, ZERO),
        "delta_3": (ZERO, ZERO, ONE),
    }


def exponent_from_pairing(pairing: Lin) -> Lin:
    return ONE - pairing


def terminal_beta(beta: LinBeta, real_root: LinBeta, exponent: Lin) -> LinBeta:
    return tuple(beta[index] + real_root[index].value(0) * exponent for index in range(3))  # type: ignore[return-value]


def gamma(beta: LinBeta) -> LinBeta:
    c1, c2, c3 = beta
    return c1, c1 + c2 - c3, c2


def q_zero_signed_dimension(beta: LinBeta) -> int | None:
    n_exp, r_exp, s_exp = gamma(beta)
    if not n_exp.is_zero() and not s_exp.is_zero():
        return None
    if r_exp.coefficient != 0:
        return None
    if abs(r_exp.constant) == 1:
        return 1
    if r_exp.constant == 0:
        return 10
    return 0


def proper_subdegree_for_tail(subdegree: LinBeta, parent: LinBeta) -> bool:
    differences = [parent[index] - subdegree[index] for index in range(3)]
    if not all(difference.is_nonnegative_for_tail() for difference in differences):
        return False
    if all(difference.is_zero() for difference in differences):
        return False
    if all(component.is_zero() for component in subdegree):
        return False
    return True


def pattern_a(n_symbol: Lin = N) -> list[LinBeta]:
    return [
        (ZERO, n_symbol, n_symbol - 1),
        (ZERO, n_symbol, n_symbol),
        (ZERO, n_symbol + 1, n_symbol),
        (n_symbol, ZERO, n_symbol - 1),
        (n_symbol, ZERO, n_symbol),
        (n_symbol + 1, ZERO, n_symbol),
    ]


def pattern_b(n_symbol: Lin = N) -> list[LinBeta]:
    return [
        (ZERO, n_symbol, n_symbol + 1),
        (ZERO, n_symbol + 1, n_symbol + 1),
        (ZERO, n_symbol + 1, n_symbol + 2),
        (n_symbol, ZERO, n_symbol + 1),
        (n_symbol + 1, ZERO, n_symbol + 1),
        (n_symbol + 1, ZERO, n_symbol + 2),
    ]


def terminal_candidates(input_rows: list[LinBeta]) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for input_beta in input_rows:
        for real_id, real_beta in real_roots().items():
            pairing = lin_pair(real_beta, input_beta)
            if not pairing.is_negative_for_tail():
                continue
            exponent = exponent_from_pairing(pairing)
            terminal = terminal_beta(input_beta, real_beta, exponent)
            if q_zero_signed_dimension(terminal) != 0:
                continue
            candidates.append({
                "input_beta": input_beta,
                "real_id": real_id,
                "pairing": pairing,
                "exponent": exponent,
                "terminal": terminal,
            })
    return candidates


def expected_rows() -> list[dict[str, str]]:
    transitions = [
        ("A_to_B", "A_N", "B_N", pattern_a(N), pattern_b(N)),
        ("B_to_A_shift", "B_N", "A_{N+2}", pattern_b(N), pattern_a(N + 2)),
    ]
    rows: list[dict[str, str]] = []
    for transition_id, input_pattern, next_pattern, input_rows, next_rows in transitions:
        candidates = terminal_candidates(input_rows)
        for index, next_beta in enumerate(next_rows, start=1):
            signed = q_zero_signed_dimension(next_beta)
            if signed not in {1, 10}:
                raise AssertionError(f"{transition_id} {beta_text(next_beta)} is not a nonzero q^0 row")
            witnesses = [
                candidate for candidate in candidates
                if proper_subdegree_for_tail(next_beta, candidate["terminal"])  # type: ignore[arg-type]
            ]
            if not witnesses:
                raise AssertionError(f"{transition_id} {beta_text(next_beta)} has no zero-terminal witness")
            witness = sorted(
                witnesses,
                key=lambda item: (str(item["real_id"]), beta_text(item["input_beta"])),  # type: ignore[arg-type]
            )[0]
            rows.append({
                "check_id": f"{transition_id}_{index}",
                "transition_id": transition_id,
                "parameter_condition": "N even, N >= 14",
                "input_pattern": input_pattern,
                "next_pattern": next_pattern,
                "next_degree_formula": beta_text(next_beta),
                "next_signed_dimension": str(signed),
                "witness_input_formula": beta_text(witness["input_beta"]),  # type: ignore[arg-type]
                "witness_real_root": str(witness["real_id"]),
                "pairing_formula": str(witness["pairing"]),
                "serre_exponent_formula": str(witness["exponent"]),
                "terminal_formula": beta_text(witness["terminal"]),  # type: ignore[arg-type]
                "terminal_signed_dimension": "0",
                "subdegree_check": "proper_nonzero_subdegree_for_all_N_ge_14",
                "proof_reference": (
                    "compute/verify_wrel_tail_staircase.py symbolic affine pairing "
                    "and phi_0_1 q^0 support"
                ),
                "check_status": "verified",
                "notes": "target-degree tail implication; not a compact source representative",
            })
    return rows


def expected_anchor_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for beta in pattern_a(Lin(0, N_MIN)):
        beta_value = linbeta_to_int(beta, N_MIN)
        signed = q_zero_signed_dimension(beta)
        if signed not in {1, 10}:
            raise AssertionError(f"A_14 anchor {beta_text(beta)} has unexpected signed dimension {signed}")
        rows.append({
            "degree_id": beta_degree_id(beta_value),
            "beta_c1": str(beta_value[0]),
            "beta_c2": str(beta_value[1]),
            "beta_c3": str(beta_value[2]),
            "signed_dimension": str(signed),
            "source_table": ANCHOR_SOURCE_TABLE,
            "proof_reference": "wrel_degree_closure six_row_saturation_real_string_saturation_extension.csv",
            "check_status": "verified",
            "notes": "finite Wrel anchor for the symbolic A_N tail at N=14",
        })
    return rows


def expected_unbounded_rows() -> list[dict[str, str]]:
    return [
        {
            "sequence_id": "A_tail",
            "parameter_condition": "k >= 0",
            "degree_family": "A_{14+2k}",
            "representative_degree_formula": "(0,14+2k,13+2k)",
            "unbounded_coordinate": "beta_c2",
            "coordinate_formula": "14+2k",
            "induction_source": "finite_anchor_A14_and_A_N_to_B_N_to_A_N_plus_2",
            "proof_reference": "compute/verify_wrel_tail_staircase.py expected_unbounded_rows",
            "check_status": "verified",
            "notes": "one representative in each A_{14+2k}; coordinate tends to infinity with k",
        },
        {
            "sequence_id": "B_tail",
            "parameter_condition": "k >= 0",
            "degree_family": "B_{14+2k}",
            "representative_degree_formula": "(0,14+2k,15+2k)",
            "unbounded_coordinate": "beta_c3",
            "coordinate_formula": "15+2k",
            "induction_source": "finite_anchor_A14_and_A_N_to_B_N",
            "proof_reference": "compute/verify_wrel_tail_staircase.py expected_unbounded_rows",
            "check_status": "verified",
            "notes": "one representative in each B_{14+2k}; coordinate tends to infinity with k",
        },
    ]


def verify_affine_k_formula(formula: str) -> None:
    if "+2k" not in formula:
        raise ValueError(f"unbounded coordinate formula has no positive 2k term: {formula}")
    constant = int(formula.split("+", 1)[0])
    values = [constant + 2 * k for k in range(4)]
    if values != sorted(set(values)):
        raise ValueError(f"unbounded coordinate formula is not strictly increasing: {formula}")


def expected_manifest() -> dict[str, object]:
    return {
        "schema_version": "wrel_tail_staircase.v1",
        "fixture_name": "wrel_tail_staircase",
        "target_kind": "wrel_infinite_six_row_tail",
        "parameter_start": 14,
        "parameter_step": 2,
        "parameter_condition": "N even, N >= 14",
        "transition_count": 2,
        "symbolic_check_count": 12,
        "finite_anchor": "A_14",
        "finite_anchor_degree_count": 6,
        "finite_anchor_source_table": ANCHOR_SOURCE_TABLE,
        "unbounded_tail_check_count": 2,
        "infinite_tail": True,
        "finite_target_degree_enumeration_closed": False,
        "certified": True,
        "target_only": True,
        "compact_source": False,
        "primitive_recognition": False,
        "source_formula_id": "lorentzian_pairing_real_string_and_phi_0_1_q0_support",
        "tables": ["finite_anchor.csv", "staircase_symbolic_checks.csv", "unbounded_tail.csv"],
        "limitations": [
            "This packet proves the symbolic target-degree tail A_N -> B_N -> A_{N+2} for even N >= 14.",
            "It verifies A_14 inside the finite W_rel degree-closure packet and proves that the target-degree audit has an infinite six-row staircase from that anchor.",
            "It records an unbounded coordinate subsequence, so finite target-degree enumeration cannot close this target-only audit.",
            "It does not construct compact source representatives, source relation matrices, PBW comparison data, or primitive recognition.",
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--wrel-fixture", type=Path, default=DEFAULT_WREL_FIXTURE)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def write_fixture(fixture: Path) -> None:
    fixture.mkdir(parents=True, exist_ok=True)
    (fixture / "manifest.json").write_text(
        json.dumps(expected_manifest(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    with (fixture / "finite_anchor.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ANCHOR_COLUMNS)
        writer.writeheader()
        writer.writerows(expected_anchor_rows())
    with (fixture / "staircase_symbolic_checks.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TABLE_COLUMNS)
        writer.writeheader()
        writer.writerows(expected_rows())
    with (fixture / "unbounded_tail.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=UNBOUNDED_COLUMNS)
        writer.writeheader()
        writer.writerows(expected_unbounded_rows())
    (fixture / "README.md").write_text(
        "# W_rel six-row tail staircase\n\n"
        "This target-side certificate proves the symbolic two-step tail\n"
        "`A_N -> B_N -> A_{N+2}` for every even `N >= 14`.  The proof uses\n"
        "only the Lorentzian pairing, real-string exponents, and the\n"
        "`q^0` support `y^{-1}+10+y` of `phi_{0,1}`.  The `finite_anchor.csv`\n"
        "table verifies the six rows of `A_14` inside the finite\n"
        "`wrel_degree_closure` packet.  The `unbounded_tail.csv` table records\n"
        "a strictly increasing coordinate subsequence, so finite target-degree\n"
        "enumeration cannot close this target-only audit.  It is not a compact\n"
        "source theorem and does not prove primitive recognition.\n\n"
        "Run:\n\n"
        "```sh\n"
        "python3 compute/verify_wrel_tail_staircase.py \\\n"
        "  --fixture certificates/targets/delta5_gn_kac/wrel_tail_staircase \\\n"
        "  --wrel-fixture certificates/targets/delta5_gn_kac/wrel_degree_closure \\\n"
        "  --check\n"
        "```\n\n"
        f"A positive result is `{SUCCESS_STATUS}`.\n",
        encoding="utf-8",
    )


def read_csv(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != columns:
            raise ValueError(f"{path}: unexpected columns {reader.fieldnames}")
        return list(reader)


def read_source_rows(path: Path) -> dict[str, dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        degree_id = row["degree_id"]
        if degree_id in out:
            raise ValueError(f"{path}: duplicate degree_id {degree_id}")
        out[degree_id] = row
    return out


def verify_finite_anchor(fixture: Path, wrel_fixture: Path) -> None:
    anchor_path = fixture / "finite_anchor.csv"
    source_path = wrel_fixture / ANCHOR_SOURCE_TABLE
    if not source_path.exists():
        raise ValueError(f"missing Wrel anchor source table: {source_path}")
    actual_anchor = read_csv(anchor_path, ANCHOR_COLUMNS)
    expected_anchor = expected_anchor_rows()
    if actual_anchor != expected_anchor:
        raise ValueError("finite_anchor.csv does not match expected A_14 anchor rows")
    source_rows = read_source_rows(source_path)
    for row in expected_anchor:
        degree_id = row["degree_id"]
        if degree_id not in source_rows:
            raise ValueError(f"A_14 anchor {degree_id} absent from {source_path}")
        source_row = source_rows[degree_id]
        for key in ("beta_c1", "beta_c2", "beta_c3", "signed_dimension"):
            if source_row[key] != row[key]:
                raise ValueError(
                    f"A_14 anchor {degree_id} {key}: expected {row[key]}, got {source_row[key]}"
                )
        if source_row.get("check_status") != "verified":
            raise ValueError(f"A_14 anchor {degree_id} is not verified in {source_path}")


def verify_unbounded_tail(fixture: Path) -> None:
    unbounded_path = fixture / "unbounded_tail.csv"
    actual_rows = read_csv(unbounded_path, UNBOUNDED_COLUMNS)
    expected_rows_ = expected_unbounded_rows()
    if actual_rows != expected_rows_:
        raise ValueError("unbounded_tail.csv does not match expected unbounded-tail rows")
    for row in actual_rows:
        verify_affine_k_formula(row["coordinate_formula"])
        if row["check_status"] != "verified":
            raise ValueError(f"unbounded tail row is not verified: {row}")


def verify_fixture(fixture: Path, wrel_fixture: Path) -> None:
    manifest_path = fixture / "manifest.json"
    table_path = fixture / "staircase_symbolic_checks.csv"
    readme_path = fixture / "README.md"
    if not manifest_path.exists():
        raise ValueError(f"missing manifest: {manifest_path}")
    if not readme_path.exists() or not readme_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest != expected_manifest():
        raise ValueError("manifest does not match symbolic tail specification")
    phi = phi_01_coefficients()
    q_zero = {key: int(value) for key, value in phi.items() if key[0] == 0}
    expected_q_zero = {(0, -1): 1, (0, 0): 10, (0, 1): 1}
    for key, value in expected_q_zero.items():
        if q_zero.get(key) != value:
            raise ValueError(f"phi_0_1 q^0 coefficient {key}: expected {value}, got {q_zero.get(key)}")
    forbidden = [key for key, value in q_zero.items() if key[1] not in {-1, 0, 1} and value]
    if forbidden:
        raise ValueError(f"unexpected nonzero q^0 phi_0_1 coefficients: {forbidden}")
    verify_finite_anchor(fixture, wrel_fixture)
    verify_unbounded_tail(fixture)
    actual_rows = read_csv(table_path, TABLE_COLUMNS)
    expected = expected_rows()
    if actual_rows != expected:
        raise ValueError("staircase_symbolic_checks.csv does not match expected symbolic rows")


def main() -> int:
    args = parse_args()
    try:
        if args.write:
            write_fixture(args.fixture)
        if args.check or not args.write:
            verify_fixture(args.fixture, args.wrel_fixture)
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"WREL_TAIL_STAIRCASE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
