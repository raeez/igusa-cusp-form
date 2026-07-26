# Wrapped Prequotient Finite Type

This packet records correction row 220.  It proves that the
scalar-rigidified wrapped prequotient
\[
\mathcal M_{\eta,R}^{\mathrm{wr,rig}}
\]
of row 219 is of finite type over \(\mathbb C\) at a fixed finite HN
height \(R\).

The proof uses three finite-stage inputs:

- the retained class set \(C_R\) is finite;
- the retained semistable substacks \(\mathfrak M^{ss}_{R,c}\) are
  finite type;
- rigidification by the central scalar \(\mathbb G_m\) preserves finite
  type by fppf descent.

It does not prove properness, anchor population, anchor losslessness,
quotient descent, transition compatibility, or aggregate hybrid-carrier
population.

Run:

```sh
python3 compute/verify_wrapped_prequotient_finite_type_obstruction.py \
  --fixture certificates/hybrid/wrapped_prequotient_finite_type --check
```

Expected status:

```text
WRAPPED_PREQUOTIENT_FINITE_TYPE_VERIFIED
```
