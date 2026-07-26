# finite_hall_pairing_invariance

This packet records correction row 361.

It proves the relative invariance criterion for supplied finite Hall
data: row 360 supersymmetry, row 357 bracket parity, and vanishing
Frobenius cyclic defect rows imply
`< [x,y], z > = < x, [y,z] >` for homogeneous primitive vectors.

The packet imports the row 360, row 357, row 355, and row 337 packets,
plus the compact Hall source obstruction ledger.  The current compact
source still has no `B_entries.csv` rows, `G_entries.csv` rows, parity
blocks, Frobenius defect rows, cyclic three-point correspondences,
Serre-sign rows, or orientation-transport rows.

Run:

```sh
python3 compute/verify_finite_hall_pairing_invariance.py \
  --fixture certificates/hall/finite_hall_pairing_invariance --check
```

Expected status:

```text
FINITE_HALL_PAIRING_INVARIANCE_OBSTRUCTION_VERIFIED
```
