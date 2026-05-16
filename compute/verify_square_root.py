#!/usr/bin/env python3
"""Exact coefficient checks for the Delta_5 square-root computation.

The script uses Q=q^(1/8) and R=r^(1/2).  With the standard theta
normalization

    theta_2 = sum Q^((2n+1)^2) R^(2n+1),
    theta_3 = sum Q^(4n^2) R^(2n),
    theta_4 = sum (-1)^n Q^(4n^2) R^(2n),

the weak Jacobi form used in the manuscript is

    phi_{0,1} = 4 * sum_i theta_i(tau,z)^2 / theta_i(tau,0)^2.

All arithmetic is rational and finite-truncated.  This is a target-side
Borcherds/Gritsenko-Nikulin check only; it does not construct compact
Hall stacks, protected source representatives, Hopf pairings, coproducts,
or radical kernels.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial, gcd

Q_MAX = 64
N_TERMS = 8

Series = dict[tuple[int, int], Fraction]
MonicDegree = tuple[int, int, int]
DeltaDegree = tuple[int, int, int]


def multiply(left: Series, right: Series, q_max: int | None = None) -> Series:
    if q_max is None:
        q_max = Q_MAX
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


def _factor_terms(
    n_exp: int,
    r_exp: int,
    s_exp: int,
    exponent: int,
    target: MonicDegree,
) -> list[tuple[int, int, int, int]]:
    max_power: int | None = None
    if n_exp > 0:
        max_power = target[0] // n_exp
    if s_exp > 0:
        s_bound = target[2] // s_exp
        max_power = s_bound if max_power is None else min(max_power, s_bound)
    if max_power is None:
        if exponent < 0:
            raise ValueError("unbounded negative exponent in q^0 s^0 factor")
        max_power = exponent

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
    return terms


def monic_delta_coefficient(
    phi: dict[tuple[int, int], Fraction],
    target: MonicDegree,
) -> int:
    """Coefficient of q^a*r^b*s^c after the leading monomial in 64^{-1} Delta_5."""

    factors: list[tuple[int, int, int, int]] = []
    for n_exp in range(target[0] + 1):
        for s_exp in range(target[2] + 1):
            for phi_q, r_exp in sorted(phi):
                if phi_q != n_exp * s_exp:
                    continue
                effective = (
                    s_exp > 0
                    or (s_exp == 0 and n_exp > 0)
                    or (s_exp == 0 and n_exp == 0 and r_exp < 0)
                )
                exponent = int(phi[(phi_q, r_exp)])
                if effective and exponent:
                    factors.append((n_exp, r_exp, s_exp, exponent))

    series: dict[MonicDegree, int] = {(0, 0, 0): 1}
    for n_exp, r_exp, s_exp, exponent in factors:
        product: defaultdict[MonicDegree, int] = defaultdict(int)
        for current, current_coeff in series.items():
            for dn, dr, ds, term_coeff in _factor_terms(
                n_exp, r_exp, s_exp, exponent, target
            ):
                next_exp = (current[0] + dn, current[1] + dr, current[2] + ds)
                if next_exp[0] <= target[0] and next_exp[2] <= target[2]:
                    product[next_exp] += current_coeff * term_coeff
        series = {key: value for key, value in product.items() if value}

    return series.get(target, 0)


def monic_delta_qrs_coefficient(phi: dict[tuple[int, int], Fraction]) -> int:
    """Coefficient of q*r*s after the leading monomial in 64^{-1} Delta_5."""

    return monic_delta_coefficient(phi, (1, 1, 1))


def delta_basis_to_gamma(delta_degree: DeltaDegree) -> MonicDegree:
    """Convert c1*delta_1+c2*delta_2+c3*delta_3 to the monic q,r,s degree."""

    c1, c2, c3 = delta_degree
    return c1, c1 + c2 - c3, c2


def additive_m_coefficient(
    phi: dict[tuple[int, int], Fraction],
    delta_degree: DeltaDegree,
) -> int:
    """Gritsenko-Nikulin additive coefficient m(a) for a timelike delta-degree."""

    return -monic_delta_coefficient(phi, delta_basis_to_gamma(delta_degree))


def signed_root_supermultiplicity(
    phi: dict[tuple[int, int], Fraction],
    delta_degree: DeltaDegree,
) -> int:
    """Signed root supermultiplicity f(n*m,l) in the delta basis."""

    n_exp, r_exp, s_exp = delta_basis_to_gamma(delta_degree)
    return int(phi.get((n_exp * s_exp, r_exp), Fraction(0)))


def delta_pair(left: DeltaDegree, right: DeltaDegree) -> int:
    """Lorentzian pairing in the delta_1, delta_2, delta_3 basis."""

    c1, c2, c3 = left
    d1, d2, d3 = right
    return (
        2 * c1 * d1
        + 2 * c2 * d2
        + 2 * c3 * d3
        - 2 * (c1 * d2 + c2 * d1)
        - 2 * (c1 * d3 + c3 * d1)
        - 2 * (c2 * d3 + c3 * d2)
    )


def real_string_exponent(real_root: DeltaDegree, other: DeltaDegree) -> int:
    """Borcherds-Kac real-string exponent 1-2(real,other)/(real,real)."""

    return 1 - 2 * delta_pair(real_root, other) // delta_pair(real_root, real_root)


def next_timelike_additive_checks(
    phi: dict[tuple[int, int], Fraction],
) -> dict[DeltaDegree, int]:
    """First height-four checks and the next point on the delta_123 ray."""

    return {
        (2, 1, 1): additive_m_coefficient(phi, (2, 1, 1)),
        (1, 2, 1): additive_m_coefficient(phi, (1, 2, 1)),
        (1, 1, 2): additive_m_coefficient(phi, (1, 1, 2)),
        (2, 2, 2): additive_m_coefficient(phi, (2, 2, 2)),
    }


def height_four_timelike_gap_checks(
    phi: dict[tuple[int, int], Fraction],
) -> dict[DeltaDegree, tuple[int, int, int]]:
    """Signed root multiplicity, additive simple coefficient, and their gap."""

    degrees = ((2, 1, 1), (1, 2, 1), (1, 1, 2))
    return {
        degree: (
            signed_root_supermultiplicity(phi, degree),
            additive_m_coefficient(phi, degree),
            signed_root_supermultiplicity(phi, degree)
            - additive_m_coefficient(phi, degree),
        )
        for degree in degrees
    }


def doubled_isotropic_gap_checks(
    phi: dict[tuple[int, int], Fraction],
) -> dict[DeltaDegree, tuple[int, int, int]]:
    """Signed multiplicity versus the GN isotropic simple multiplicity tau=9."""

    isotropic_simple_multiplicity = 9
    degrees = ((2, 2, 0), (2, 0, 2), (0, 2, 2))
    return {
        degree: (
            signed_root_supermultiplicity(phi, degree),
            isotropic_simple_multiplicity,
            signed_root_supermultiplicity(phi, degree)
            - isotropic_simple_multiplicity,
        )
        for degree in degrees
    }


def real_string_relation_checks() -> dict[str, int]:
    """Finite real-string constants used in the recognition obstruction."""

    delta_1 = (1, 0, 0)
    delta_2 = (0, 1, 0)
    delta_3 = (0, 0, 1)
    a_12 = (1, 1, 0)
    delta_123 = (1, 1, 1)
    return {
        "real_real_pairing": delta_pair(delta_1, delta_2),
        "real_real_exponent": real_string_exponent(delta_1, delta_2),
        "adjacent_isotropic_pairing": delta_pair(delta_1, a_12),
        "complement_isotropic_pairing": delta_pair(delta_3, a_12),
        "complement_isotropic_exponent": real_string_exponent(delta_3, a_12),
        "timelike_delta123_pairing": delta_pair(delta_1, delta_123),
        "timelike_delta123_exponent": real_string_exponent(delta_1, delta_123),
    }


Laurent = dict[int, int]


def laurent_add(left: Laurent, right: Laurent) -> Laurent:
    result: defaultdict[int, int] = defaultdict(int)
    for exponent, coefficient in left.items():
        result[exponent] += coefficient
    for exponent, coefficient in right.items():
        result[exponent] += coefficient
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient
    }


def laurent_multiply(left: Laurent, right: Laurent) -> Laurent:
    result: defaultdict[int, int] = defaultdict(int)
    for left_exp, left_coeff in left.items():
        for right_exp, right_coeff in right.items():
            result[left_exp + right_exp] += left_coeff * right_coeff
    return {
        exponent: coefficient
        for exponent, coefficient in result.items()
        if coefficient
    }


def first_timelike_laurent_check(phi: dict[tuple[int, int], Fraction]) -> Laurent:
    """Laurent polynomial whose r^1 coefficient is the first timelike coefficient."""

    chamber_wall = {-1: -1, 0: 1}  # 1 - r^{-1}
    q_or_s_linear = {ell: -int(phi[(0, ell)]) for ell in (-1, 0, 1)}
    q_and_s_linear = {ell: -int(phi[(1, ell)]) for ell in (-2, -1, 0, 1, 2)}
    return laurent_multiply(
        chamber_wall,
        laurent_add(laurent_multiply(q_or_s_linear, q_or_s_linear), q_and_s_linear),
    )


def mobius(value: int) -> int:
    n = value
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            prime_factors += 1
            if n % divisor == 0:
                return 0
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def free_lie_multidegree_dimension(multidegree: tuple[int, ...]) -> int:
    """Witt dimension for the free Lie algebra in a fixed multidegree."""

    total = sum(multidegree)
    common = 0
    for entry in multidegree:
        common = gcd(common, entry)

    numerator = 0
    for divisor in range(1, common + 1):
        if common % divisor != 0:
            continue
        term = factorial(total // divisor)
        for entry in multidegree:
            term //= factorial(entry // divisor)
        numerator += mobius(divisor) * term
    return numerator // total


def first_timelike_presentation_split(
    phi: dict[tuple[int, int], Fraction],
) -> tuple[int, int]:
    """Target-side Borcherds-Kac presentation split in degree delta_1+delta_2+delta_3."""

    real_real_real = free_lie_multidegree_dimension((1, 1, 1))
    isotropic_simple_multiplicity = 9
    mixed_real_isotropic = 3 * isotropic_simple_multiplicity
    odd_imaginary_simple = monic_delta_qrs_coefficient(phi)
    even = real_real_real + mixed_real_isotropic
    return even, odd_imaginary_simple


def eichler_zagier_invariant_check(
    phi: dict[tuple[int, int], Fraction],
    n_max: int,
) -> dict[tuple[int, int], int]:
    """For a weak Jacobi form of weight 0 and index 1, the Fourier coefficient
    f(n,r) depends only on the discriminant Delta=4n-r^2 and the parity of r.
    Returns a Delta->value map for Delta in [-1, 4*n_max], collected from the
    most-stable (largest n) (n,r) realising that discriminant; raises on any
    inconsistency.
    """

    by_discriminant: dict[int, set[int]] = {}
    for (n, r), value in phi.items():
        if value == 0:
            continue
        if n < 0 or n > n_max:
            continue
        discriminant = 4 * n - r * r
        by_discriminant.setdefault(discriminant, set()).add(int(value))
    representative: dict[tuple[int, int], int] = {}
    for discriminant, values in sorted(by_discriminant.items()):
        if len(values) != 1:
            raise AssertionError(
                f"Eichler-Zagier invariant fails at Delta={discriminant}: "
                f"values {sorted(values)}"
            )
        (value,) = values
        representative[(discriminant, 0)] = value
    return representative


CHL_TWIST_KAPPA_BKM_TABLE: dict[int, tuple[int, int]] = {
    1: (10, 5),
    2: (8, 4),
    3: (6, 3),
    4: (4, 2),
    6: (2, 1),
}


def kappa_bkm_universal_check(table: dict[int, tuple[int, int]]) -> None:
    """Verify kappa_BKM(Phi_N) = c_N(0)/2 across the CHL frame N in {1,2,3,4,6}.

    For each N, table[N] = (c_N(0), kappa_BKM). The identity is integer-level
    arithmetic; the test catches typos or transcription drift between this
    fixture, Ch.4 Theorem thm:bkm-kappa-universal, and KICKSTART Section 6.
    """

    for level, (c_zero, kappa_value) in sorted(table.items()):
        expected_kappa = c_zero // 2
        if expected_kappa * 2 != c_zero:
            raise AssertionError(
                f"c_{level}(0) = {c_zero} is not even; kappa_BKM must be a "
                f"half-integer count"
            )
        if expected_kappa != kappa_value:
            raise AssertionError(
                f"kappa_BKM(Phi_{level}) = {kappa_value} disagrees with "
                f"c_{level}(0)/2 = {expected_kappa}"
            )


def main() -> None:
    phi = phi_01_coefficients()
    expected_phi = {
        # Depths 0--4 (the established verification table).
        (0, -1): 1, (0, 0): 10, (0, 1): 1,
        (1, -2): 10, (1, -1): -64, (1, 0): 108,
        (1, 1): -64, (1, 2): 10,
        (2, -3): 1, (2, -2): 108, (2, -1): -513,
        (2, 0): 808, (2, 1): -513, (2, 2): 108, (2, 3): 1,
        (3, -3): -64, (3, -2): 808, (3, -1): -2752,
        (3, 0): 4016, (3, 1): -2752, (3, 2): 808, (3, 3): -64,
        (4, -4): 10, (4, -3): -513, (4, -2): 4016,
        (4, -1): -11775, (4, 0): 16524, (4, 1): -11775,
        (4, 2): 4016, (4, 3): -513, (4, 4): 10,
        # Depth 5 (verified by Eichler-Zagier Delta-orbit consistency:
        # f(5,4)=f(2,2)=f(1,0)=108; f(5,2)=f(4,0)=16524; f(5,3)=f(3,1)=-2752).
        (5, -4): 108, (5, -3): -2752, (5, -2): 16524,
        (5, -1): -43200, (5, 0): 58640, (5, 1): -43200,
        (5, 2): 16524, (5, 3): -2752, (5, 4): 108,
        # Depth 6 (Delta-orbit cross-checks: f(6,5)=f(2,3)=f(0,1)=1;
        # f(6,4)=f(3,2)=f(2,0)=808; f(6,3)=f(4,1)=-11775;
        # f(6,2)=f(5,0)=58640).
        (6, -5): 1, (6, -4): 808, (6, -3): -11775,
        (6, -2): 58640, (6, -1): -141826, (6, 0): 188304,
        (6, 1): -141826, (6, 2): 58640, (6, 3): -11775,
        (6, 4): 808, (6, 5): 1,
    }
    for key, expected in expected_phi.items():
        assert phi[key] == expected, (key, phi[key], expected)
    discriminant_map = eichler_zagier_invariant_check(phi, n_max=6)
    expected_discriminants = {
        (-1, 0): 1,
        (0, 0): 10,
        (3, 0): -64,
        (4, 0): 108,
        (7, 0): -513,
        (8, 0): 808,
        (11, 0): -2752,
        (12, 0): 4016,
        (15, 0): -11775,
        (16, 0): 16524,
        (19, 0): -43200,
        (20, 0): 58640,
        (23, 0): -141826,
        (24, 0): 188304,
    }
    for key, expected in expected_discriminants.items():
        assert discriminant_map[key] == expected, (
            key, discriminant_map[key], expected
        )
    kappa_bkm_universal_check(CHL_TWIST_KAPPA_BKM_TABLE)
    # Anchor the table to the theta computation at N=1: c_1(0) is the
    # leading [q^0 r^0] of phi_{0,1}, which we compute directly.
    c_one_zero_from_phi = int(phi[(0, 0)])
    assert c_one_zero_from_phi == CHL_TWIST_KAPPA_BKM_TABLE[1][0], (
        c_one_zero_from_phi, CHL_TWIST_KAPPA_BKM_TABLE[1][0]
    )

    eta9 = eta_power_coefficients(9, 9)
    assert eta9[:10] == [1, -9, 27, -12, -90, 135, 54, -99, -189, -85]
    laurent_check = first_timelike_laurent_check(phi)
    assert laurent_check == {-3: 9, -2: -93, -1: 90, 0: -90, 1: 93, 2: -9}
    assert monic_delta_qrs_coefficient(phi) == laurent_check[1] == 93
    even, odd = first_timelike_presentation_split(phi)
    assert (even, odd) == (29, 93)
    assert even - odd == phi[(1, 1)] == -64
    next_checks = next_timelike_additive_checks(phi)
    assert next_checks == {
        (2, 1, 1): 90,
        (1, 2, 1): 90,
        (1, 1, 2): 90,
        (2, 2, 2): -540,
    }
    assert monic_delta_coefficient(phi, (2, 2, 2)) == 540
    height_four_gaps = height_four_timelike_gap_checks(phi)
    assert height_four_gaps == {
        (2, 1, 1): (108, 90, 18),
        (1, 2, 1): (108, 90, 18),
        (1, 1, 2): (108, 90, 18),
    }
    doubled_isotropic_gaps = doubled_isotropic_gap_checks(phi)
    assert doubled_isotropic_gaps == {
        (2, 2, 0): (10, 9, 1),
        (2, 0, 2): (10, 9, 1),
        (0, 2, 2): (10, 9, 1),
    }
    string_checks = real_string_relation_checks()
    assert string_checks == {
        "real_real_pairing": -2,
        "real_real_exponent": 3,
        "adjacent_isotropic_pairing": 0,
        "complement_isotropic_pairing": -4,
        "complement_isotropic_exponent": 5,
        "timelike_delta123_pairing": -2,
        "timelike_delta123_exponent": 3,
    }

    print("phi_{0,1} coefficients through q^6:")
    for q_exp in range(7):
        row = sorted((l, phi[(q_exp, l)]) for (q, l) in phi if q == q_exp)
        print(f"q^{q_exp}: {row}")
    print("Eichler-Zagier Delta-invariants through Delta=24:")
    for (discriminant, _), value in sorted(discriminant_map.items()):
        if discriminant <= 24:
            print(f"Delta={discriminant}: {value}")
    print("kappa_BKM universality across CHL frame N in {1,2,3,4,6}:")
    for level, (c_zero, kappa_value) in sorted(CHL_TWIST_KAPPA_BKM_TABLE.items()):
        print(f"N={level}: c_N(0)={c_zero}, kappa_BKM=c_N(0)/2={kappa_value}")
    print("prod_{k>=1}(1-q^k)^9 through q^9:")
    print(eta9[:10])
    print("[q*r*s] 64^{-1} Delta_5 / (q*r*s)^{1/2}:")
    print(monic_delta_qrs_coefficient(phi))
    print("first timelike Laurent check A*(B^2+C):")
    print(sorted(laurent_check.items()))
    print("first timelike target presentation split even|odd:")
    print(f"{even}|{odd}")
    print("m(delta_1+delta_2+delta_3):")
    print(-monic_delta_qrs_coefficient(phi))
    print("next timelike additive m checks:")
    for delta_degree, value in sorted(next_checks.items()):
        print(f"{delta_degree}: {value}")
    print("height-four timelike signed|m|gap checks:")
    for delta_degree, value in sorted(height_four_gaps.items()):
        print(f"{delta_degree}: {value[0]}|{value[1]}|{value[2]}")
    print("doubled isotropic signed|tau|gap checks:")
    for delta_degree, value in sorted(doubled_isotropic_gaps.items()):
        print(f"{delta_degree}: {value[0]}|{value[1]}|{value[2]}")
    print("real-string pairing/exponent checks:")
    for key, value in sorted(string_checks.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
