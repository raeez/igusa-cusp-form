#!/usr/bin/env python3
"""Exact coefficient checks for the Delta_5 square-root computation.

The script uses Q=q^(1/8) and R=r^(1/2).  With the standard theta
normalization

    theta_2 = sum Q^((2n+1)^2) R^(2n+1),
    theta_3 = sum Q^(4n^2) R^(2n),
    theta_4 = sum (-1)^n Q^(4n^2) R^(2n),

the weak Jacobi form used in the manuscript is

    phi_{0,1} = 4 * sum_i theta_i(tau,z)^2 / theta_i(tau,0)^2.

All arithmetic is rational and finite-truncated.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb

Q_MAX = 24
N_TERMS = 8

Series = dict[tuple[int, int], Fraction]


def multiply(left: Series, right: Series, q_max: int = Q_MAX) -> Series:
    product: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (q_left, r_left), value_left in left.items():
        for (q_right, r_right), value_right in right.items():
            q_exp = q_left + q_right
            if q_exp <= q_max:
                product[(q_exp, r_left + r_right)] += value_left * value_right
    return dict(product)


def theta(kind: int) -> Series:
    terms: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for n in range(-N_TERMS, N_TERMS + 1):
        if kind == 2:
            q_exp = (2 * n + 1) ** 2
            r_exp = 2 * n + 1
            sign = 1
        elif kind == 3:
            q_exp = 4 * n * n
            r_exp = 2 * n
            sign = 1
        elif kind == 4:
            q_exp = 4 * n * n
            r_exp = 2 * n
            sign = 1 if n % 2 == 0 else -1
        else:
            raise ValueError(kind)
        if q_exp <= Q_MAX:
            terms[(q_exp, r_exp)] += Fraction(sign)
    return dict(terms)


def theta_denominator(theta_series: Series) -> Series:
    specialized: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (q_exp, _r_exp), value in theta_series.items():
        specialized[(q_exp, 0)] += value
    return multiply(dict(specialized), dict(specialized))


def divide_by_q_series(numerator: Series, denominator: Series) -> Series:
    min_q = min(q_exp for (q_exp, r_exp), value in denominator.items()
                if value and r_exp == 0)
    den = {
        q_exp - min_q: value
        for (q_exp, r_exp), value in denominator.items()
        if r_exp == 0 and q_exp - min_q <= Q_MAX
    }
    num: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (q_exp, r_exp), value in numerator.items():
        if min_q <= q_exp and q_exp - min_q <= Q_MAX:
            num[(q_exp - min_q, r_exp)] += value

    quotient: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    constant = den[0]
    for q_exp in range(Q_MAX + 1):
        r_exps = {r for (q, r) in num if q == q_exp}
        r_exps |= {r for (q, r) in quotient if q < q_exp}
        for r_exp in sorted(r_exps):
            value = num.get((q_exp, r_exp), Fraction(0))
            for den_exp, den_coeff in den.items():
                if den_exp == 0 or den_exp > q_exp:
                    continue
                value -= den_coeff * quotient.get((q_exp - den_exp, r_exp),
                                                   Fraction(0))
            if value:
                quotient[(q_exp, r_exp)] = value / constant
    return dict(quotient)


def phi_01_coefficients() -> dict[tuple[int, int], Fraction]:
    phi: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for kind in (2, 3, 4):
        th = theta(kind)
        ratio = divide_by_q_series(multiply(th, th), theta_denominator(th))
        for key, value in ratio.items():
            phi[key] += 4 * value

    coefficients: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (q_exp, r_exp), value in phi.items():
        if q_exp % 8 == 0 and r_exp % 2 == 0 and value:
            coefficients[(q_exp // 8, r_exp // 2)] += value
    return dict(coefficients)


def eta_power_coefficients(power: int, order: int) -> list[int]:
    coeffs = [0] * (order + 1)
    coeffs[0] = 1
    for k in range(1, order + 1):
        next_coeffs = [0] * (order + 1)
        for i, coeff in enumerate(coeffs):
            if coeff == 0:
                continue
            for j in range(power + 1):
                exponent = i + j * k
                if exponent <= order:
                    next_coeffs[exponent] += coeff * ((-1) ** j) * comb(power, j)
        coeffs = next_coeffs
    return coeffs


def main() -> None:
    phi = phi_01_coefficients()
    expected_phi = {
        (0, -1): 1, (0, 0): 10, (0, 1): 1,
        (1, -2): 10, (1, -1): -64, (1, 0): 108,
        (1, 1): -64, (1, 2): 10,
        (2, -3): 1, (2, -2): 108, (2, -1): -513,
        (2, 0): 808, (2, 1): -513, (2, 2): 108, (2, 3): 1,
    }
    for key, expected in expected_phi.items():
        assert phi[key] == expected, (key, phi[key], expected)

    eta9 = eta_power_coefficients(9, 9)
    assert eta9[:10] == [1, -9, 27, -12, -90, 135, 54, -99, -189, -85]

    print("phi_{0,1} coefficients through q^2:")
    for q_exp in range(3):
        row = sorted((l, phi[(q_exp, l)]) for (q, l) in phi if q == q_exp)
        print(f"q^{q_exp}: {row}")
    print("prod_{k>=1}(1-q^k)^9 through q^9:")
    print(eta9[:10])


if __name__ == "__main__":
    main()
