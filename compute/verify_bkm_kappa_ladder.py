#!/usr/bin/env python3
"""Consistency fixture for the corrected c_N(0) ladder (thm:bkm-kappa-universal).

Hard-coded inputs: the five CHL frame shapes,

    N = 1: 1^24,   N = 2: 1^8 2^8,   N = 3: 1^6 3^6,
    N = 4: 1^4 2^2 4^4,   N = 6: 1^2 2^2 3^2 6^2,

the corrected Jatkar--Sen / Govindarajan--Krishna constants

    c_N(0) = (10, 6, 4, 3, 2)  for N in {1, 2, 3, 4, 6},

and the manuscript's expected table as assertion targets.  The
Borcherds weights are kappa_BKM(Phi_N) = c_N(0)/2 = (5, 3, 2, 3/2, 1);
the N = 4 weight 3/2 is half-integral (Phi_4 lives on the genus-two
metaplectic cover).

Computed content:

* the characteristic polynomial of g_N on the 24-dimensional frame
  representation, prod_d (x^d - 1)^{a_d}, expanded exactly, giving the
  twined Euler characteristic chi^{g_N}(K3) = Tr(g_N | H^*(K3))
  = -[x^23] charpoly = a_1 (each d-cycle contributes the full sum of
  the d-th roots of unity, zero for d > 1);
* the equivariant q^0 row of the twined elliptic genus from Hodge
  character data: a finite symplectic automorphism acts trivially on
  H^{0,0}, H^{2,0}, H^{0,2}, H^{2,2}, so Tr(g_N | H^{1,1}) =
  chi^{g_N}(K3) - 4 and the q^0 row is 2y + (chi - 4) + 2y^{-1}, with
  row sum chi^{g_N}(K3);
* phi_{0,1} from its theta-quotient definition (verify_square_root),
  giving the N = 1 square-root constant c_1(0) = f(0,0) = 10.

Retraction guard.  The once-recorded identification
c_N(0) = chi^{g_N}(K3) = a_1 = (8, 6, 4, 2) for N in {2, 3, 4, 6},
giving the integral ladder (5, 4, 3, 2, 1), is retracted: the
frame-shape datum is the weight of the eta product
prod_d eta(d tau)^{a_d}, not the Jacobi constant term of the Borcherds
input.  The script computes the Lefschetz ladder exactly and asserts
that it differs from the corrected constants at N = 2, 3, 4 (at N = 6
the two numbers coincide accidentally at the value 2).

Scalar weight arithmetic only: no paramodular form is constructed, no
Borcherds lift is evaluated, no Pfaffian or orientation datum enters.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from verify_square_root import phi_01_coefficients  # noqa: E402

SUCCESS_STATUS = "BKM_KAPPA_LADDER_VERIFIED"
FAILURE_PREFIX = "BKM_KAPPA_LADDER_FAILED"

# Hard-coded input: the CHL frame shapes (Cheng--Harrison Sec. 2;
# Conway--Norton), as {cycle length d: multiplicity a_d}.
FRAME_SHAPES: dict[int, dict[int, int]] = {
    1: {1: 24},
    2: {1: 8, 2: 8},
    3: {1: 6, 3: 6},
    4: {1: 4, 2: 2, 4: 4},
    6: {1: 2, 2: 2, 3: 2, 6: 2},
}

# Assertion targets: the manuscript's corrected table in
# thm:bkm-kappa-universal (Jatkar--Sen; Govindarajan--Krishna for the
# composite rows).  The N = 4 weight is the half-integer 3/2.
MANUSCRIPT_C0 = {1: 10, 2: 6, 3: 4, 4: 3, 6: 2}
MANUSCRIPT_KAPPA = {1: Fraction(5), 2: Fraction(3), 3: Fraction(2),
                    4: Fraction(3, 2), 6: Fraction(1)}

# Retracted identification: the Lefschetz / frame-shape ladder that was
# once read as c_N(0).  Kept as a guard target only.
RETRACTED_LEFSCHETZ_C0 = {2: 8, 3: 6, 4: 4, 6: 2}


def poly_mul(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a == 0:
            continue
        for j, b in enumerate(right):
            if b:
                out[i + j] += a * b
    return out


def charpoly(frame: dict[int, int]) -> list[int]:
    """prod_d (x^d - 1)^{a_d}, exact integer coefficients, low degree first."""
    poly = [1]
    for d, mult in sorted(frame.items()):
        factor = [-1] + [0] * (d - 1) + [1]  # x^d - 1
        for _ in range(mult):
            poly = poly_mul(poly, factor)
    return poly


def frame_trace(frame: dict[int, int]) -> int:
    """Tr(g | frame representation) = -[x^{deg-1}] charpoly (monic)."""
    poly = charpoly(frame)
    degree = len(poly) - 1
    if poly[degree] != 1:
        raise AssertionError("characteristic polynomial is not monic")
    return -poly[degree - 1]


def euler_totient(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    try:
        phi = phi_01_coefficients()
        f00 = int(phi.get((0, 0), Fraction(0)))
        f01 = int(phi.get((0, 1), Fraction(0)))
        f0m1 = int(phi.get((0, -1), Fraction(0)))

        for N, frame in FRAME_SHAPES.items():
            # Frame validity: 24-dimensional representation, phi(N) | 2.
            require(
                sum(d * mult for d, mult in frame.items()) == 24,
                f"N={N}: frame shape is not 24-dimensional",
            )
            require(
                euler_totient(N) in (1, 2),
                f"N={N}: totient condition phi(N) | 2 fails",
            )

            # Twined Euler characteristic from the characteristic
            # polynomial; H^odd(K3) = 0, so the Lefschetz number is the
            # full trace.
            chi = frame_trace(frame)
            require(
                chi == frame.get(1, 0),
                f"N={N}: trace {chi} != 1-cycle count {frame.get(1, 0)}",
            )

            # Equivariant q^0 row of the twined elliptic genus from
            # Hodge characters: trivial action on H^{0,0}, H^{2,0},
            # H^{0,2}, H^{2,2}; Tr(g | H^{1,1}) = chi - 4.
            q0_row = (2, chi - 4, 2)  # coefficients of y, y^0, y^{-1}
            require(
                sum(q0_row) == chi,
                f"N={N}: q^0 row sum {sum(q0_row)} != chi {chi}",
            )

            if N == 1:
                # Untwined cross-check: Ell(K3) = 2 phi_{0,1} has q^0 row
                # 2(y + 10 + y^{-1}); its row sum is chi(K3) = 24 and its
                # y^0 constant 2 f(0,0) = 20 = chi - 4.
                require(chi == 24, f"chi(K3) = {chi} != 24")
                require(
                    2 * (f01 + f00 + f0m1) == chi,
                    "q^0 row sum of Ell(K3) = 2 phi_01 != chi(K3)",
                )
                require(
                    2 * f00 == chi - 4,
                    "y^0 constant of Ell(K3) != Tr(id | H^{1,1}) = 20",
                )
                # The ladder's N = 1 entry is the square-root constant
                # c_1(0) = f(0,0) = 10, NOT the Lefschetz number
                # chi^{g_1}(K3) = 24.
                c0 = f00
                require(c0 == 10, f"c_1(0) = {c0} != 10")
                require(c0 != chi, "square-root constant coincides with chi at N=1")
            else:
                # Corrected constants (Jatkar--Sen; Govindarajan--Krishna):
                # hard-coded input, NOT derived from the frame shape.
                c0 = MANUSCRIPT_C0[N]
                # Retraction guard: the frame-shape Lefschetz number is
                # the once-recorded (retracted) reading of c_N(0).
                require(
                    chi == RETRACTED_LEFSCHETZ_C0[N],
                    f"N={N}: Lefschetz number {chi} != recorded retracted "
                    f"value {RETRACTED_LEFSCHETZ_C0[N]}",
                )
                if N in (2, 3, 4):
                    require(
                        c0 != chi,
                        f"N={N}: corrected c_N(0) = {c0} must differ from "
                        f"the retracted Lefschetz reading {chi}",
                    )
                else:
                    # N = 6: accidental agreement at the value 2.
                    require(
                        c0 == chi == 2,
                        f"N={N}: expected accidental agreement at 2, got "
                        f"c_N(0) = {c0}, chi = {chi}",
                    )

            require(
                c0 == MANUSCRIPT_C0[N],
                f"N={N}: c_N(0) = {c0} != manuscript value {MANUSCRIPT_C0[N]}",
            )
            kappa = Fraction(c0, 2)
            require(
                kappa == MANUSCRIPT_KAPPA[N],
                f"N={N}: kappa = {kappa} != manuscript value {MANUSCRIPT_KAPPA[N]}",
            )
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"{FAILURE_PREFIX}: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
