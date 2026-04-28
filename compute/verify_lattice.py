#!/usr/bin/env python3
"""Exact lattice checks for the Delta_5 denominator construction.

This is a target-side lattice and normal-form check only; its pairings
are Gram/Pfaffian lattice pairings, not compact Hall Hopf pairings.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations


def sign_to_standard(order: tuple[int, ...]) -> int:
    inversions = 0
    for i, left in enumerate(order):
        for right in order[i + 1:]:
            if left > right:
                inversions += 1
    return -1 if inversions % 2 else 1


def two_form(i: int, j: int, coeff: int = 1) -> dict[tuple[int, int], Fraction]:
    if i == j:
        return {}
    if i < j:
        return {(i, j): Fraction(coeff)}
    return {(j, i): Fraction(-coeff)}


def add(*forms: dict[tuple[int, int], Fraction]) -> dict[tuple[int, int], Fraction]:
    result: dict[tuple[int, int], Fraction] = {}
    for form in forms:
        for key, value in form.items():
            result[key] = result.get(key, Fraction(0)) + value
    return {key: value for key, value in result.items() if value}


def scale(form: dict[tuple[int, int], Fraction], scalar: Fraction) -> dict[tuple[int, int], Fraction]:
    return {key: scalar * value for key, value in form.items() if scalar * value}


def pairing(left: dict[tuple[int, int], Fraction], right: dict[tuple[int, int], Fraction]) -> Fraction:
    total = Fraction(0)
    for (i, j), a in left.items():
        for (k, l), b in right.items():
            if len({i, j, k, l}) < 4:
                continue
            total += a * b * sign_to_standard((i, j, k, l))
    return total


def mat_pair(x: tuple[Fraction, Fraction, Fraction], y: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    """Pairing on Z f_2 + Z f_3 + Z f_{-2}."""
    a, b, c = x
    d, e, f = y
    return 2 * b * e - a * f - c * d


def reflect(x: tuple[Fraction, Fraction, Fraction], delta: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    factor = mat_pair(x, delta)  # all simple real roots have square 2
    return tuple(x_i - factor * d_i for x_i, d_i in zip(x, delta))


def main() -> None:
    e12 = two_form(1, 2)
    e13 = two_form(1, 3)
    e23 = two_form(2, 3)
    e24 = two_form(2, 4)
    e41 = two_form(4, 1)
    e43 = two_form(4, 3)

    q0 = add(e13, e24)
    f1 = e12
    f2 = e23
    f3 = add(e13, scale(e24, Fraction(-1)))
    fm2 = e41
    fm1 = e43
    basis = [f1, f2, f3, fm2, fm1]

    gram = [[pairing(x, y) for y in basis] for x in basis]
    expected_gram = [
        [0, 0, 0, 0, -1],
        [0, 0, 0, -1, 0],
        [0, 0, 2, 0, 0],
        [0, -1, 0, 0, 0],
        [-1, 0, 0, 0, 0],
    ]
    assert gram == expected_gram, gram
    assert all(pairing(q0, vector) == 0 for vector in basis)

    delta1 = (Fraction(2), Fraction(-1), Fraction(0))
    delta2 = (Fraction(0), Fraction(-1), Fraction(2))
    delta3 = (Fraction(0), Fraction(1), Fraction(0))
    deltas = [delta1, delta2, delta3]
    delta_gram = [[mat_pair(x, y) for y in deltas] for x in deltas]
    assert delta_gram == [[2, -2, -2], [-2, 2, -2], [-2, -2, 2]], delta_gram

    rho = (Fraction(1), Fraction(-1, 2), Fraction(1))
    assert all(mat_pair(rho, delta) == -1 for delta in deltas)
    assert rho == tuple(sum(delta[i] for delta in deltas) / 2 for i in range(3))

    for delta in deltas:
        assert reflect(delta, delta) == tuple(-entry for entry in delta)
        for other in deltas:
            before = mat_pair(other, other)
            after = mat_pair(reflect(other, delta), reflect(other, delta))
            assert before == after

    for n, l, m in [(1, 1, 1), (3, -1, 1), (1, 3, 5), (5, -3, 7)]:
        alpha = (Fraction(2 * n), Fraction(-l), Fraction(2 * m))
        z_pairing = {
            "z1": -alpha[0],
            "z2": 2 * alpha[1],
            "z3": -alpha[2],
        }
        assert z_pairing == {"z1": -2 * n, "z2": -2 * l, "z3": -2 * m}

        half_alpha = (Fraction(n), Fraction(-l, 2), Fraction(m))
        a = (Fraction(n - 1), Fraction(-(l - 1), 2), Fraction(m - 1))
        assert tuple(rho[i] + a[i] for i in range(3)) == half_alpha
        if n % 2 == l % 2 == m % 2 == 1:
            assert a[0].denominator == 1 and a[0] % 2 == 0
            assert a[1].denominator == 1
            assert a[2].denominator == 1 and a[2] % 2 == 0

    print("Pfaffian Gram matrix in (f_1,f_2,f_3,f_-2,f_-1):")
    for row in gram:
        print(row)
    print("Type-II simple-root Gram matrix:")
    for row in delta_gram:
        print(row)
    print("rho:", rho)
    print("All lattice checks passed.")


if __name__ == "__main__":
    main()
