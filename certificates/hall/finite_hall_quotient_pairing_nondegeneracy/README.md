# finite_hall_quotient_pairing_nondegeneracy

This packet records correction row 363.

It proves the relative quotient non-degeneracy criterion for supplied
finite Hall data: once `G`, left/right radical bases `K`, and quotient
splittings `Q` are supplied, full rank of
`Q_gamma^t G_gamma Q_-gamma` is exactly non-degeneracy of the induced
quotient pairing.

The packet imports row 362, row 360, row 358, the pairing-kernel
lim1 obstruction packet, the transition-radical obstruction packet, and
the compact Hall source obstruction ledger.  The current compact source
still has no `G_entries.csv`, `K_entries.csv`, `Q_entries.csv`,
quotient pairing matrices, quotient-rank rows, determinant rows, or
radical-identification rows.

Run:

```sh
python3 compute/verify_finite_hall_quotient_pairing_nondegeneracy.py \
  --fixture certificates/hall/finite_hall_quotient_pairing_nondegeneracy --check
```

Expected status:

```text
FINITE_HALL_QUOTIENT_PAIRING_NONDEGENERACY_OBSTRUCTION_VERIFIED
```
