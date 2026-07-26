# finite_hall_pairing_matrix_firewall

This packet records correction row 366.

It verifies the finite-stage firewall that a pairing matrix `G`, a
kernel matrix `K`, and a quotient splitting `Q` do not by themselves
prove the Hopf radical used in primitive recognition. Hopf-radical
descent requires the Hopf-pairing defect rows: Hopf adjointness,
Frobenius cyclicity, and quotient non-degeneracy.

The packet imports row 365, row 362, row 361, row 363, and the compact
Hall source obstruction ledger. The current compact source supplies no
`G/K/Q` rows and no Hopf-adjointness, Frobenius cyclic, quotient
non-degeneracy, radical coideal, radical Lie-ideal, or quotient
Hopf-pairing rows.

Run:

```sh
python3 compute/verify_finite_hall_pairing_matrix_firewall.py \
  --fixture certificates/hall/finite_hall_pairing_matrix_firewall --check
```

Expected status:

```text
FINITE_HALL_PAIRING_MATRIX_FIREWALL_OBSTRUCTION_VERIFIED
```
