# Mixed Local/Wrapped Correspondence Definition

This packet records correction row 208. At finite HN height \(R\), the
one-sided mixed correspondence datum consists of the two ordered
unreduced extension diagrams \(LW\) and \(WL\). A local colour map
\(\alpha:I\to\Gamma_R^{\mathrm{loc}}\) has total colour
\(|\alpha|=\sum_{i\in I}\alpha_i\), a wrapped input has colour
\(\eta\in\Gamma_R^{\mathrm{wr}}\), and the target colour is
\(\zeta=|\alpha|+\eta\in\Gamma_R^{\mathrm{wr}}\) or
\(\zeta=\eta+|\alpha|\in\Gamma_R^{\mathrm{wr}}\), according to the
order.

The two typed diagrams are:

\[
\mathfrak E^{LW}_{\alpha,\eta;\zeta,R,I}
\xrightarrow{p^{LW}}
\mathfrak M^{\mathrm{loc,cl}}_{\alpha,R,I}
\times
\mathcal M^{\mathrm{wr,rig}}_{\eta,R},
\qquad
\mathfrak E^{LW}_{\alpha,\eta;\zeta,R,I}
\xrightarrow{q^{LW}}
\mathcal M^{\mathrm{wr,rig}}_{\zeta,R},
\]
classifying \(0\to W_\eta\to B_\zeta\to A_\alpha\to0\), and
\[
\mathfrak E^{WL}_{\eta,\alpha;\zeta,R,I}
\xrightarrow{p^{WL}}
\mathcal M^{\mathrm{wr,rig}}_{\eta,R}
\times
\mathfrak M^{\mathrm{loc,cl}}_{\alpha,R,I},
\qquad
\mathfrak E^{WL}_{\eta,\alpha;\zeta,R,I}
\xrightarrow{q^{WL}}
\mathcal M^{\mathrm{wr,rig}}_{\zeta,R},
\]
classifying \(0\to A_\alpha\to B_\zeta\to W_\eta\to0\).

This packet only defines the one-sided mixed correspondence type. It is
not the local-local correspondence, not the wrapped-wrapped
correspondence, not the ordered two-sided mixed correspondence, not the
source/target anchor-memory definition separated in
`certificates/hybrid/source_target_anchor_memory_definition`, and not a
quotient-first Hall product.

Run:

```sh
python3 compute/verify_mixed_local_wrapped_correspondence_definition_obstruction.py \
  --fixture certificates/hybrid/mixed_local_wrapped_correspondence_definition --check
```

Expected status:

```text
MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED
```

This status verifies the two typed definition rows and records the
missing extension-stack, source/target-map, populated anchor-memory,
admissibility, base-change, projection-formula, Thom--Sebastiani, and
transition rows fail-closed for this definition packet.  Target
admissibility is separated in
`certificates/hybrid/mixed_local_wrapped_extension_admissibility`.
