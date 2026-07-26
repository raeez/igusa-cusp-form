# rhomred_free_e_nulltrivialization

This packet verifies the row-284 obstruction ledger for a
null-trivialization of the connected free \(E\)-Borel class.

For a Cech--Borel cocycle \(a^{E,\mathrm{free}}_{\mathcal C}\)
representing \(\alpha^{E,\mathrm{free}}_{\mathcal C}\), a
null-trivialization is a \(1\)-cochain
\(h^{E,\mathrm{free}}_{\mathcal C}\) satisfying
\[
\delta h^{E,\mathrm{free}}_{\mathcal C}
=a^{E,\mathrm{free}}_{\mathcal C}.
\]

This packet records the criterion and verifies that the retained finite
tables supply no cocycle representative, no zero-class row, no
\(1\)-cochain, and no coboundary-defect-zero row.  It does not construct
quotient orientation, transition compatibility, vanishing cycles, or
protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_free_e_nulltrivialization_obstruction.py \
  --fixture certificates/orientation/rhomred_free_e_nulltrivialization --check
```
