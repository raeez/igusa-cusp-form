# rhomred_free_e_vanishing

This packet verifies the row-283 obstruction ledger for the vanishing of
the connected free \(E\)-Borel class.

After row 282 supplies
\[
\alpha^{E,\mathrm{free}}=a_1u_1+a_2u_2
\in H^2(BE;\mathbb F_2),
\]
row 283 is exactly the pair of zero-coordinate checks
\[
a_1=0,\qquad a_2=0.
\]

This packet imports the row-282 free \(E\)-Borel packet and records that
the current tables supply no \(a_1,a_2\) coefficient values and no
zero-coordinate rows.  It does not construct the row-284
null-trivialization, quotient orientation, transition compatibility,
vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_free_e_vanishing_obstruction.py \
  --fixture certificates/orientation/rhomred_free_e_vanishing --check
```
