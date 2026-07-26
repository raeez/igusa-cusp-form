# Source/Target Anchor Memory Definition

This packet records correction row 212. At finite HN height \(R\), the
mixed and wrapped correspondence types retain the source and target
wrapped anchors before the reduced \(E\)-quotient is taken. The datum
uses the abstract wrapped anchor maps
\(\lambda_{\eta,R}:\mathcal M_{\eta,R}^{\mathrm{wr,rig}}\to E\)
already named by the wrapped prequotient sector; it does not construct
those maps as determinant anchors. The determinant construction is
separated in `certificates/hybrid/determinant_anchor_construction`.
The determinant-anchor translation weight is separated in
`certificates/hybrid/determinant_anchor_translation_weight`.
The determinant-anchor chi-zero degeneracy is separated in
`certificates/hybrid/determinant_anchor_chi_zero_degeneracy`.
The determinant-anchor extra-anchor datum is separated in
`certificates/hybrid/determinant_anchor_extra_anchor_data`.
The anchor-residual definition is separated in
`certificates/hybrid/anchor_residual_definition`.

The four typed anchor-memory maps are \(LW\), \(WL\), \(WW\), and
\(LWL\). Local/local correspondences have no wrapped input and carry no
wrapped anchor-memory row.

This packet does not prove \(o^\lambda_R=0\), full anchor losslessness,
or quotient descent.

Run:

```sh
python3 compute/verify_source_target_anchor_memory_definition_obstruction.py \
  --fixture certificates/hybrid/source_target_anchor_memory_definition --check
```

Expected status:

```text
SOURCE_TARGET_ANCHOR_MEMORY_DEFINITION_VERIFIED
```

This status verifies the four typed before-quotient definition rows,
the local/local exclusion row, and the fail-closed open obligations for
later anchor construction, losslessness, quotient descent, and
transition rows.
