# Wrapped Stratum \(b>0\) Prestack Definition

This packet records correction row 207. At finite HN height \(R\), the
wrapped stratum of the hybrid carrier is the full subprestack
\[
\operatorname{Ran}^{\mathrm{wr}}_{R,\mathrm{pre}}(E)
\subset
\operatorname{Ran}^{\mathrm{hyb}}_{R,\mathrm{pre}}(E)
\]
cut out by the condition \(I=\varnothing\) in the hybrid indexing
category and by colour labels in
\(\Gamma_R^{\mathrm{wr}}=\{b_R^{\mathrm{geom}}>0\}\). Equivalently,
\[
\operatorname{Ran}^{\mathrm{wr}}_{R,\mathrm{pre}}(E)
=
\operatorname*{colim}_{(J,\eta)}
\prod_{j\in J}\mathcal M_{\eta_j,R}^{\mathrm{wr,rig}},
\qquad
\eta:J\to\Gamma_R^{\mathrm{wr}},
\]
with finite relabelling, and with the anchor maps
\(\lambda_{\eta_j,R}: \mathcal M_{\eta_j,R}^{\mathrm{wr,rig}}\to E\)
retained as part of each wrapped point.

This is a carrier definition. It is not the wrapped coefficient object
\(\mathcal G_R^{\mathrm{wr}}\), not the determinant anchor by itself,
not a support-realization theorem for retained objects, and not a
stackification/descent theorem.

Run:

```sh
python3 compute/verify_wrapped_stratum_bpositive_prestack_definition_obstruction.py \
  --fixture certificates/hybrid/wrapped_stratum_bpositive_prestack_definition --check
```

Expected status:

```text
WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED
```

This status verifies the subprestack definition and records the missing
wrapped component, populated prequotient, anchor, support-realization,
descent, and transition rows fail-closed.  The separate packet
`certificates/hybrid/equivariant_wrapped_prequotient_definition`
defines the \(E\)-equivariant wrapped prequotient before the reduced
\(E\)-quotient.
