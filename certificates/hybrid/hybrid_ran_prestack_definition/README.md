# Hybrid Ran Prestack Definition

This packet records correction row 205.  At finite HN height \(R\), the
hybrid carrier is a prestack
\[
\operatorname{Ran}^{\mathrm{hyb}}_{R,\mathrm{pre}}(E):
\mathrm{Aff}_{\mathbb C}^{op}\to \infty\mathrm{Gpd},
\]
not a set-theoretic disjoint union with a scalar degree attached.

For a test affine \(T\), a point consists of finite local configuration
maps \(T\to E\), retained local colour labels, finitely many wrapped
colour labels, and \(T\)-families in the corresponding rigidified
wrapped prequotient stacks equipped with their anchor maps to \(E\).
The construction is the symmetric finite-colour colimit over finite
indexing sets.  Its stackification is a later descent datum, not part
of this definition.

Run:

```sh
python3 compute/verify_hybrid_ran_prestack_definition_obstruction.py \
  --fixture certificates/hybrid/hybrid_ran_prestack_definition --check
```

Expected status:

```text
HYBRID_RAN_PRESTACK_DEFINITION_VERIFIED
```

This status verifies the prestack definition row and records the
missing local-stratum, wrapped-stratum, descent, stackification, and
transition rows fail-closed.  The row-206 local \(b=0\) subprestack is
separated in `certificates/hybrid/local_stratum_b0_prestack_definition`.
The row-207 wrapped \(b>0\) subprestack is separated in
`certificates/hybrid/wrapped_stratum_bpositive_prestack_definition`.
