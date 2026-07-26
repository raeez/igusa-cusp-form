#!/usr/bin/env python3
"""Exact theta-product / Borcherds-product identity for Delta_5.

Both sides of the foundational identity

    Delta_5(Z) = prod_{ten even (a,b)} nu_{a,b}(Z)
               = 64 q^{1/2} r^{1/2} s^{1/2}
                 prod_{(n,l,m) in Gamma_eff} (1 - q^n r^l s^m)^{f(nm,l)}

are computed from first principles and compared monomial by monomial
on the box (q-exponent <= 5/2, s-exponent <= 5/2, all r-powers kept):

* Theta side: the ten even genus-two theta constants in the phase
  convention of the manuscript (03_view1_automorphic.tex),

      nu_{a,b}(Z) = sum_{l in Z^2} exp(pi i (z[l + a/2] + t(b) l)),

  with z[v] = t(v) z v, multiplied exactly in the units
  Q = q^{1/8}, R = r^{1/4}, S = s^{1/8}.
* Borcherds side: the exponents f(n,l) are the Fourier coefficients of
  phi_{0,1}, computed from the theta-quotient definition
  (phi_01_coefficients of verify_square_root); the product is expanded
  exactly over the active semigroup Gamma_eff of the chamber
  0 < |s| << |q| << |r|^{-1} << 1.

Sign trap (recorded in certificates/normalizations/delta5_theta_leading):
the script also computes the ten-even-theta product in the Mumford
convention

    theta[a;b](Z) = sum_l exp(pi i (z[l + a/2] + t(l + a/2) b)),

whose phase differs by exp(pi i t(a) b / 2), and asserts that the
Mumford-convention product equals MINUS the manuscript-convention
product on the whole box: the theta-leading coefficient is +64 in the
manuscript convention and -64 in the Mumford convention.  The sign of
the leading constant is convention-dependent; the identity with the
Borcherds product holds with +64 in the manuscript's pinned convention.

Scalar q-expansion identity only: no Pfaffian line, no O2 wall atlas,
no orientation character, no compact-source trace.
"""

from __future__ import annotations

import sys
from collections import defaultdict
from fractions import Fraction
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import verify_square_root  # noqa: E402
from verify_square_root import phi_01_coefficients  # noqa: E402

SUCCESS_STATUS = "THETA_PRODUCT_IDENTITY_VERIFIED"
FAILURE_PREFIX = "THETA_PRODUCT_IDENTITY_FAILED"

# Box: Delta_5 exponents q^{uq/8} r^{ur/4} s^{us/8} with uq, us <= 28,
# i.e. q- and s-exponents <= 7/2.  All r-powers inside the box are kept.
# The box q,s <= 5/2 (50 monomials) already suffices; 7/2 gives 120.
Q_UNITS_MAX = 28
S_UNITS_MAX = 28

Units = tuple[int, int, int]
Series = dict[Units, int]


def even_characteristics() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    chars = [
        ((a1, a2), (b1, b2))
        for a1 in (0, 1)
        for a2 in (0, 1)
        for b1 in (0, 1)
        for b2 in (0, 1)
        if (a1 * b1 + a2 * b2) % 2 == 0
    ]
    if len(chars) != 10:
        raise AssertionError(f"expected 10 even characteristics, got {len(chars)}")
    return chars


def theta_constant(
    a: tuple[int, int], b: tuple[int, int], convention: str
) -> Series:
    """One even theta constant, truncated to the box, exact integers.

    Units: (uq, ur, us) = (w1^2, w1*w2, w2^2) with w = 2l + a, so that
    the monomial is q^{uq/8} r^{ur/4} s^{us/8}.
    """
    terms: defaultdict[Units, int] = defaultdict(int)
    for l1 in range(-3, 4):
        for l2 in range(-3, 4):
            w1 = 2 * l1 + a[0]
            w2 = 2 * l2 + a[1]
            uq = w1 * w1
            us = w2 * w2
            if uq > Q_UNITS_MAX or us > S_UNITS_MAX:
                continue
            ur = w1 * w2
            if convention == "manuscript":
                # exp(pi i t(b) l) = (-1)^{b.l}
                sign = -1 if (b[0] * l1 + b[1] * l2) % 2 else 1
            elif convention == "mumford":
                # exp(pi i t(l + a/2) b) = exp(pi i (w.b)/2); w.b is even
                # for an even characteristic, so the phase is a sign.
                dot = w1 * b[0] + w2 * b[1]
                if dot % 2 != 0:
                    raise AssertionError("odd w.b on an even characteristic")
                sign = -1 if (dot // 2) % 2 else 1
            else:
                raise ValueError(convention)
            terms[(uq, ur, us)] += sign
    return {key: value for key, value in terms.items() if value}


def multiply(left: Series, right: Series) -> Series:
    product: defaultdict[Units, int] = defaultdict(int)
    for (q1, r1, s1), c1 in left.items():
        for (q2, r2, s2), c2 in right.items():
            uq = q1 + q2
            us = s1 + s2
            if uq <= Q_UNITS_MAX and us <= S_UNITS_MAX:
                product[(uq, r1 + r2, us)] += c1 * c2
    return {key: value for key, value in product.items() if value}


def theta_product(convention: str) -> Series:
    series: Series = {(0, 0, 0): 1}
    for a, b in even_characteristics():
        series = multiply(series, theta_constant(a, b, convention))
    return series


def borcherds_factors(
    phi: dict[tuple[int, int], Fraction], q_max: int, s_max: int
) -> list[tuple[int, int, int, int]]:
    """Active factors (n, l, m, f(nm, l)) of Gamma_eff inside the box."""
    factors: list[tuple[int, int, int, int]] = []
    for n_exp in range(q_max + 1):
        for s_exp in range(s_max + 1):
            for (phi_q, r_exp), value in sorted(phi.items()):
                if phi_q != n_exp * s_exp or not value:
                    continue
                effective = (
                    s_exp > 0
                    or (s_exp == 0 and n_exp > 0)
                    or (s_exp == 0 and n_exp == 0 and r_exp < 0)
                )
                if effective:
                    factors.append((n_exp, r_exp, s_exp, int(value)))
    return factors


def monic_product_series(
    phi: dict[tuple[int, int], Fraction], q_max: int, s_max: int
) -> dict[tuple[int, int, int], int]:
    """prod (1 - q^n r^l s^m)^{f(nm,l)} truncated to q <= q_max, s <= s_max."""
    series: dict[tuple[int, int, int], int] = {(0, 0, 0): 1}
    for n_exp, r_exp, s_exp, exponent in borcherds_factors(phi, q_max, s_max):
        if n_exp > 0:
            max_power = q_max // n_exp
            if s_exp > 0:
                max_power = min(max_power, s_max // s_exp)
        elif s_exp > 0:
            max_power = s_max // s_exp
        elif exponent >= 0:
            max_power = exponent
        else:
            raise AssertionError("unbounded negative exponent at q^0 s^0")

        terms: list[tuple[int, int, int, int]] = []
        if exponent >= 0:
            for power in range(min(exponent, max_power) + 1):
                coeff = (-1) ** power * comb(exponent, power)
                terms.append((power * n_exp, power * r_exp, power * s_exp, coeff))
        else:
            order = -exponent
            for power in range(max_power + 1):
                coeff = comb(order + power - 1, power)
                terms.append((power * n_exp, power * r_exp, power * s_exp, coeff))

        product: defaultdict[tuple[int, int, int], int] = defaultdict(int)
        for (aq, ar, asx), current in series.items():
            for dq, dr, ds, coeff in terms:
                nq, ns = aq + dq, asx + ds
                if nq <= q_max and ns <= s_max:
                    product[(nq, ar + dr, ns)] += current * coeff
        series = {key: value for key, value in product.items() if value}
    return series


def borcherds_side(phi: dict[tuple[int, int], Fraction]) -> Series:
    """64 q^{1/2} r^{1/2} s^{1/2} prod(...) in the (1/8, 1/4, 1/8) units."""
    monic = monic_product_series(phi, Q_UNITS_MAX // 8, S_UNITS_MAX // 8)
    side: Series = {}
    for (a, b, c), coeff in monic.items():
        units = (8 * a + 4, 4 * b + 2, 8 * c + 4)
        if units[0] <= Q_UNITS_MAX and units[2] <= S_UNITS_MAX:
            side[units] = 64 * coeff
    return side


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    try:
        # The Borcherds factors inside the box need f(nm, l) through
        # nm = (Q_UNITS_MAX // 8) * (S_UNITS_MAX // 8); widen the exact
        # phi_{0,1} truncation of verify_square_root accordingly.
        needed_nm = (Q_UNITS_MAX // 8) * (S_UNITS_MAX // 8) + 1
        verify_square_root.Q_MAX = max(verify_square_root.Q_MAX, 8 * needed_nm)
        phi = phi_01_coefficients()

        # phi_{0,1} anchor coefficients (discriminant decomposition rows).
        for key, expected in (
            ((0, 0), 10),
            ((0, 1), 1),
            ((0, -1), 1),
            ((1, 0), 108),
            ((1, 1), -64),
            ((1, -1), -64),
            ((1, 2), 10),
            ((1, -2), 10),
        ):
            require(
                int(phi.get(key, Fraction(0))) == expected,
                f"phi_01 coefficient f{key} != {expected}",
            )

        theta_man = theta_product("manuscript")
        theta_mum = theta_product("mumford")
        borcherds = borcherds_side(phi)

        # Structural support: every theta-product monomial sits on the
        # shifted lattice q^{1/2+Z} r^{1/2+Z/?} s^{1/2+Z} of the cusp form.
        for uq, ur, us in theta_man:
            require(uq % 8 == 4, f"q-units {uq} not congruent to 4 mod 8")
            require(us % 8 == 4, f"s-units {us} not congruent to 4 mod 8")
            require(ur % 4 == 2, f"r-units {ur} not congruent to 2 mod 4")

        # The identity, monomial by monomial, on the whole box.
        require(
            theta_man == borcherds,
            "theta product != 64 * Borcherds product on the box: "
            f"{sorted(set(theta_man) ^ set(borcherds))[:5]} ...",
        )
        require(
            len(theta_man) >= 100,
            f"box too small to be probative: {len(theta_man)} monomials",
        )

        # Leading coefficient +64 in the manuscript convention.
        require(theta_man.get((4, 2, 4)) == 64, "leading coefficient != +64")

        # Sign trap: the Mumford convention flips the global sign.
        require(
            theta_mum == {key: -value for key, value in theta_man.items()},
            "Mumford-convention product != -(manuscript-convention product)",
        )
        require(theta_mum.get((4, 2, 4)) == -64, "Mumford leading != -64")

        # Spot checks against the manuscript's verified drivers.
        # [q^{3/2} r^{1/2} s^{1/2}] Delta_5 = -576, i.e. -9 in D_5: the
        # exponent rho + 2 f_2 that witnesses the imaginary-simple
        # correction terms of the denominator identity (Chapter 1).
        require(
            theta_man.get((12, 2, 4)) == -576,
            "[q^{3/2} r^{1/2} s^{1/2}] Delta_5 != -576",
        )
        require(
            theta_man.get((4, 2, 12)) == -576,
            "[q^{1/2} r^{1/2} s^{3/2}] Delta_5 != -576 (q <-> s symmetry)",
        )
        # [q^{3/2} r^{3/2} s^{3/2}] Delta_5 = 64 * 93 = 5952: the monic
        # driver of m(delta_123) = -93 in the BKM chapter.
        require(
            theta_man.get((12, 6, 12)) == 5952,
            "[q^{3/2} r^{3/2} s^{3/2}] Delta_5 != 5952 = 64 * 93",
        )
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"{FAILURE_PREFIX}: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
