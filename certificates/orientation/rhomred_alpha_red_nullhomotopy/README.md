# rhomred_alpha_red_nullhomotopy

This packet verifies the row-281 obstruction ledger for a
null-homotopy of the reduced gerbe class.

For a Cech--Borel cocycle \(a^{\mathrm{red}}_{\mathcal C}\)
representing \(\alpha^{\mathrm{red}}_{\mathcal C}\), a null-homotopy is
a \(1\)-cochain \(h^{\mathrm{red}}_{\mathcal C}\) satisfying
\[
\delta h^{\mathrm{red}}_{\mathcal C}=a^{\mathrm{red}}_{\mathcal C}.
\]

This packet records the criterion and verifies that the retained finite
tables supply no cocycle representative, no zero-class row, no
\(1\)-cochain, and no coboundary-defect-zero row.  It does not construct
quotient orientation, transition compatibility, vanishing cycles, or
protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_alpha_red_nullhomotopy_obstruction.py \
  --fixture certificates/orientation/rhomred_alpha_red_nullhomotopy --check
```
