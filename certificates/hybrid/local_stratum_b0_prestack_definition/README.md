# Local Stratum \(b=0\) Prestack Definition

This packet records correction row 206.  At finite HN height \(R\), the
local stratum of the hybrid carrier is the full subprestack
\[
\operatorname{Ran}^{\mathrm{loc}}_{R,\mathrm{pre}}(E)
\subset
\operatorname{Ran}^{\mathrm{hyb}}_{R,\mathrm{pre}}(E)
\]
cut out by the condition \(J=\varnothing\) in the hybrid indexing
category and by colour labels in
\(\Gamma_R^{\mathrm{loc}}=\{b_R^{\mathrm{geom}}=0\}\).  Equivalently,
\[
\operatorname{Ran}^{\mathrm{loc}}_{R,\mathrm{pre}}(E)
=
\operatorname*{colim}_{(I,\alpha)}
E^I,
\qquad
\alpha:I\to\Gamma_R^{\mathrm{loc}},
\]
with relabelling and collision maps as in the ordinary Ran prestack.

This is a carrier definition.  It is not the local sheaf
\(\mathcal F_R^{\mathrm{loc}}\), not the closed-configuration incidence
stack \(\mathfrak M_{\alpha,R,I}^{\mathrm{loc,cl}}\), and not a
stackification/descent theorem.

Run:

```sh
python3 compute/verify_local_stratum_b0_prestack_definition_obstruction.py \
  --fixture certificates/hybrid/local_stratum_b0_prestack_definition --check
```

Expected status:

```text
LOCAL_STRATUM_B0_PRESTACK_DEFINITION_VERIFIED
```

This status verifies the subprestack definition and records the missing
closed-configuration, descent, and transition rows fail-closed.
