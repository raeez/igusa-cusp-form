# finite_hall_hopf_pairing_defect_rows

This packet records correction row 365.

It verifies the relative theorem that supplied compact geometric Hall
bialgebra data together with supplied compact geometric Hopf-pairing
data give the finite Hopf-pairing defect rows
`O_Hpair,R = 0`.

The packet imports row 364, row 350, row 362, row 361, row 363, and the
compact Hall source obstruction ledger.  It records no current compact
source Hopf-adjointness, Frobenius cyclic, quotient non-degeneracy,
radical ideal/coideal, or `M/D/G/K/Q` rows.

Run:

```sh
python3 compute/verify_finite_hall_hopf_pairing_defect_rows.py \
  --fixture certificates/hall/finite_hall_hopf_pairing_defect_rows --check
```

Expected status:

```text
FINITE_HALL_HOPF_PAIRING_DEFECT_ROWS_OBSTRUCTION_VERIFIED
```
