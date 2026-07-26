This packet records row 352: without an antipode datum the finite Hall
bialgebra stage is not a finite Hall Hopf algebra in the verified
source package.

The packet imports row 351, row 350, and the compact Hall source
ledger.  It checks that the current source has no antipode rows, no
left or right convolution identity rows, and no finite Hall
Hopf-algebra claim.  It also records the opposite boundary: this is
not a theorem that no antipode can exist after the missing rows are
eventually supplied.

Run:

```sh
python3 compute/verify_finite_hall_nonhopf_boundary.py \
  --fixture certificates/hall/finite_hall_nonhopf_boundary --check
```

The expected status is `FINITE_HALL_NONHOPF_BOUNDARY_VERIFIED`.
