# rhomred_orientation_e_quotient_descent

This packet verifies row 302 as a criterion and obstruction ledger:
orientation descent through the \(E\)-quotient is a Picard-groupoid
descent datum, not a collection of scalar zero tests.

The row requires an actual orientation line, null-trivialisations of
\(\alpha^{\mathrm{red}}\), \(\alpha^{E,\mathrm{free}}\), and every
finite-stabilizer \(\beta^H\), together with zero residual
linearization characters \(\lambda^H\).  The choices must be compatible
on quotient-presentation overlaps, retained subgroup restrictions,
and the retained extension/flag charts.

The current reduced-orientation tables supply no `orientation_lines`,
`quotient_borel`, or `finite_stabilizers` rows.  The imported packets
therefore remain obstruction ledgers.

Run:

```sh
python3 compute/verify_rhomred_orientation_e_quotient_descent.py \
  --fixture certificates/orientation/rhomred_orientation_e_quotient_descent --check
```
