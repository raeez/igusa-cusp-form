# finite_hall_pairing_coproduct_adjointness

This packet records correction row 362.

It proves the relative Hopf-adjointness criterion for supplied finite
Hall data: if product rows `M`, coproduct rows `D`, pairing rows `G`,
and tensor-pairing Koszul sign rows are supplied, then vanishing of
the adjointness defect rows is exactly
`< m(x,y), z > = < x tensor y, Delta z >`.

The packet imports the row 361, row 342, row 347, and row 350 packets,
plus the compact Hall source obstruction ledger.  The current compact
source still has no `M_entries.csv`, `D_entries.csv`, `G_entries.csv`,
Hopf-adjointness rows, tensor-pairing sign rows, product/coproduct
correspondence rows, or orientation-transport rows.

Run:

```sh
python3 compute/verify_finite_hall_pairing_coproduct_adjointness.py \
  --fixture certificates/hall/finite_hall_pairing_coproduct_adjointness --check
```

Expected status:

```text
FINITE_HALL_PAIRING_COPRODUCT_ADJOINTNESS_OBSTRUCTION_VERIFIED
```
