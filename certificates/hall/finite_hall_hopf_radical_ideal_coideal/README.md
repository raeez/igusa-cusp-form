# finite_hall_hopf_radical_ideal_coideal

This packet records correction row 367.

It verifies the conditional finite algebraic criterion for the Hopf
radical: Hopf adjointness plus quotient tensor non-degeneracy proves
the coideal half, and the Frobenius cyclic identity proves the Lie-ideal
half.

The packet imports row 366, row 365, row 362, row 361, row 363, and the
compact Hall source obstruction ledger. The current compact source
supplies no Hopf-adjointness, Frobenius cyclic, quotient tensor
non-degeneracy, radical coideal, radical Lie-ideal, or `G/K/Q` rows.

Run:

```sh
python3 compute/verify_finite_hall_hopf_radical_ideal_coideal.py \
  --fixture certificates/hall/finite_hall_hopf_radical_ideal_coideal --check
```

Expected status:

```text
FINITE_HALL_HOPF_RADICAL_IDEAL_COIDEAL_OBSTRUCTION_VERIFIED
```
