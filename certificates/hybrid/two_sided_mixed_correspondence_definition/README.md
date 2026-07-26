# Ordered Two-Sided Mixed Correspondence Definition

This packet records correction row 211. At finite HN height \(R\), the
ordered two-sided mixed correspondence is the unreduced three-input
flag diagram
\[
\mathfrak E^{\mathrm{LWL}}_{\alpha_-;\eta;\beta_+,R,I_-,I_+}
\xrightarrow{p^{\mathrm{LWL}}}
\mathfrak M^{\mathrm{loc,cl}}_{\alpha_-,R,I_-}
\times
\mathcal M^{\mathrm{wr,rig}}_{\eta,R}
\times
\mathfrak M^{\mathrm{loc,cl}}_{\beta_+,R,I_+},
\qquad
\mathfrak E^{\mathrm{LWL}}_{\alpha_-;\eta;\beta_+,R,I_-,I_+}
\xrightarrow{q^{\mathrm{LWL}}}
\mathcal M^{\mathrm{wr,rig}}_{\zeta,R},
\]
where
\(\alpha_-:I_-\to\Gamma_R^{\mathrm{loc}}\),
\(\eta\in\Gamma_R^{\mathrm{wr}}\),
\(\beta_+:I_+\to\Gamma_R^{\mathrm{loc}}\), and
\(\zeta=|\alpha_-|+\eta+|\beta_+|\in\Gamma_R^{\mathrm{wr}}\).
It classifies flags
\[
0\subset A_{\beta_+}\subset B_{\eta+\beta_+}\subset C_\zeta
\]
with quotients \(A_{\beta_+}\), \(W_\eta\), and \(A_{\alpha_-}\) in
that order.

This packet only defines the ordered two-sided mixed correspondence
type. It is not the one-sided mixed correspondence, not the local/local
correspondence, not the wrapped/wrapped correspondence, not the full
eight-word flag atlas, not the source/target anchor-memory definition
separated in `certificates/hybrid/source_target_anchor_memory_definition`,
and not a quotient-first Hall product.

Run:

```sh
python3 compute/verify_two_sided_mixed_correspondence_definition_obstruction.py \
  --fixture certificates/hybrid/two_sided_mixed_correspondence_definition --check
```

Expected status:

```text
TWO_SIDED_MIXED_CORRESPONDENCE_DEFINITION_VERIFIED
```

This status verifies the typed definition row and records the missing
flag-stack, source/target-map, populated anchor-memory, admissibility,
base-change, projection-formula, Thom--Sebastiani, and transition rows
fail-closed.
