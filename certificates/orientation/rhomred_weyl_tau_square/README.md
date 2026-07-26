# rhomred_weyl_tau_square

This packet verifies row 307 as a criterion and obstruction ledger:
after Weyl wall transports \(\tau_i\) are supplied, proving
\(\tau_i^2=1\) requires a two-edge source loop, determinant-square
compatibility, quotient-cocycle transport around the loop, and a
finite `tau_square_defect_rank=0` row.  A target reflection relation
and the Maass character value squared are not enough.

Run:

```sh
python3 compute/verify_rhomred_weyl_tau_square.py \
  --fixture certificates/orientation/rhomred_weyl_tau_square --check
```
