# E-Equivariant Wrapped Prequotient Definition

This packet records correction row 219.  For
\(\eta\in\Gamma_R^{\mathrm{wr}}\), it defines the scalar-rigidified
wrapped prequotient
\[
\mathcal M_{\eta,R}^{\mathrm{wr,rig}}
\]
before the reduced \(E\)-quotient is taken.  The superscript
`\(\mathrm{rig}\)' means scalar rigidification; it does not mean that
the \(E\)-translation direction has already been removed.

For a test affine \(T\), a section \(a:T\to E\) acts by relative
translation on the elliptic factor:
\[
a\cdot A=(1_{K3}\times\tau_a)_*A .
\]
The action has identity \(0_E\), satisfies the group law, and preserves
the wrapped colour because translation acts trivially on the numerical
class and preserves the geometric elliptic degree.

Run:

```sh
python3 compute/verify_equivariant_wrapped_prequotient_definition_obstruction.py \
  --fixture certificates/hybrid/equivariant_wrapped_prequotient_definition --check
```

Expected status:

```text
E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_VERIFIED
```

This status verifies the definition and the \(E\)-action row.  Finite
type is separated in
`certificates/hybrid/wrapped_prequotient_finite_type`.  Properness,
final anchor population, anchor losslessness, quotient descent,
transition compatibility, and aggregate hybrid carrier population
remain open obligations.
