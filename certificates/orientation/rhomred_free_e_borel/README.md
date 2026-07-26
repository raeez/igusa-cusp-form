# rhomred_free_e_borel

This packet verifies the row-282 obstruction ledger for the connected
free \(E\)-Borel class.

For the connected \(E\)-translation action,
\[
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2,
\qquad
\alpha^{E,\mathrm{free}}=a_1u_1+a_2u_2.
\]

This packet imports the retained free \(E\)-actions and records that
the current orientation tables supply no equivariant Borel
representative, no edge-reduction row, and no \(a_1,a_2\) coefficient
rows.  It does not prove \(\alpha^{E,\mathrm{free}}=0\), construct its
null-trivialization, construct quotient orientation, prove transition
compatibility, construct vanishing cycles, or define protected
integration.

Verify with:

```sh
python3 compute/verify_rhomred_free_e_borel_obstruction.py \
  --fixture certificates/orientation/rhomred_free_e_borel --check
```
