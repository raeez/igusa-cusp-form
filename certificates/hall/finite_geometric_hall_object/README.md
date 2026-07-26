This packet records row 341: the definition of the finite compact Hall
object \(\mathcal H_R^{\mathrm{geom}}\).

The definition is the finite \(\widehat\Gamma_R\)-graded Borel--Moore
object
\[
\mathcal H_R^{\mathrm{geom}} =
\bigoplus_{\widehat c\in\widehat\Gamma_R}
H_*^{\mathrm{BM}}(\mathfrak M^{\mathrm{red}}_{R,\widehat c},
\Phi^{\mathrm{red}}_{R,\widehat c}\otimes o_{R,\widehat c}).
\]
It requires retained finite-type rigidified stacks, finite residual
inertia, reduced vanishing-cycle coefficients, Joyce--Upmeier
orientation lines, compact-support Borel--Moore admissibility, and
homogeneous finite source bases.

The packet verifies only the definition and the obstruction ledger.  It
does not populate the object.  The imported compact Hall source packet
is still `mock_empty_blocked`; its degree, basis-provenance, product,
coproduct, unit, and counit tables are headers only.  Product, coproduct,
pairing, radical quotient, PBW, primitive, and transition data are not
part of row 341.

Run:

```sh
python3 compute/verify_finite_geometric_hall_object_definition.py \
  --fixture certificates/hall/finite_geometric_hall_object --check
```

The expected status is
`FINITE_GEOMETRIC_HALL_OBJECT_DEFINITION_VERIFIED`.
