# finite_hall_pairing_supersymmetry

This packet records correction row 360.

It proves the relative supersymmetry criterion for supplied finite
positive-negative Hall pairing data: after row 359 homogeneity, the
signed-transpose rows
`G_{gamma,p;ab} = (-1)^p G_{-gamma,p;ba}` are exactly the even
supersymmetry identity for homogeneous primitive vectors.

The packet imports the row 358 and row 359 Hall packets, the reduced
Calabi-Yau threefold Serre-sign criterion packet, and the compact Hall
source obstruction ledger.  The current compact source still has no
`G_entries.csv` rows, parity blocks, signed-transpose rows,
Serre-sign rows, or orientation-transport rows.

Run:

```sh
python3 compute/verify_finite_hall_pairing_supersymmetry.py \
  --fixture certificates/hall/finite_hall_pairing_supersymmetry --check
```

Expected status:

```text
FINITE_HALL_PAIRING_SUPERSYMMETRY_OBSTRUCTION_VERIFIED
```
