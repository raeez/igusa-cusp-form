# Wrapped/Wrapped Correspondence Definition

This packet records correction row 209. At finite HN height \(R\), the
wrapped/wrapped correspondence is the ordered unreduced extension
diagram
\[
\mathfrak E^{\mathrm{WW}}_{\eta_1,\eta_2;\zeta,R}
\xrightarrow{p^{\mathrm{WW}}}
\mathcal M^{\mathrm{wr,rig}}_{\eta_1,R}
\times
\mathcal M^{\mathrm{wr,rig}}_{\eta_2,R},
\qquad
\mathfrak E^{\mathrm{WW}}_{\eta_1,\eta_2;\zeta,R}
\xrightarrow{q^{\mathrm{WW}}}
\mathcal M^{\mathrm{wr,rig}}_{\zeta,R},
\]
for \(\eta_1,\eta_2\in\Gamma_R^{\mathrm{wr}}\) and retained
\(\zeta=\eta_1+\eta_2\in\Gamma_R^{\mathrm{wr}}\). It classifies
extensions
\[
0\to W_{\eta_2}\to B_\zeta\to W_{\eta_1}\to0.
\]

This packet only defines the wrapped/wrapped correspondence type. It is
not the mixed local/wrapped correspondence, not the local/local
correspondence, not the ordered two-sided mixed correspondence, not
the source/target anchor-memory definition separated in
`certificates/hybrid/source_target_anchor_memory_definition`, not
symmetric descent, and not a quotient-first Hall product.

Run:

```sh
python3 compute/verify_wrapped_wrapped_correspondence_definition_obstruction.py \
  --fixture certificates/hybrid/wrapped_wrapped_correspondence_definition --check
```

Expected status:

```text
WRAPPED_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED
```

This status verifies the typed definition row and records the missing
extension-stack, source/target-map, populated anchor-memory, admissibility,
Thom--Sebastiani, symmetric-descent, and transition rows fail-closed
for this definition packet.  Target admissibility is separated in
`certificates/hybrid/wrapped_wrapped_extension_admissibility`.
