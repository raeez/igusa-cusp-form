# A180 -- K3e BKM Signed-Coefficient Residual Patch

## Result

Patched the CYQG K3e BKM chapter so residual \(|c(D)|\), ordinary
multiplicity, BPS cardinality, and generator-count claims are signed
protected index / root-character statements unless a parity fixture or
finite Hall--Borcherds recognition theorem supplies ordinary spaces.

## Changed Path

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`

## Anchors

- `1009-1016`, `1054-1076`: replaced \(|c(4nm-\ell^2)|\) / ordinary
  `mult` claims with signed root-character/superdimension language.
- `3137`, `3280`, `3298-3299`, `3640-3651`: made KS/BPS/scattering and
  dictionary entries protected-index statements.
- `3713-3716`: made \(1/\Phi_{10}\) coefficients protected signed BPS
  indices with absolute Rademacher asymptotics.
- `3964-3969`, `4045-4069`: kept generator ranges only as
  parity-fixtured target presentation data.
- `12891`, `12905`, `13217-13221`, `13721`: made `64`, GV primitives,
  and Fourier-table ordinary dimensions conditional on parity fixture or
  finite Hall--Borcherds recognition.

## Checks

- Targeted `rg` for `|c(D)|`, `|c(4nm`, `mult`, `BPS degeneracies`,
  `count BPS`, `dim g`, `primitive dimension`, and `generators`.
- `|c(4nm` and `BPS degeneracies` now have no hits.
- Remaining \(|c(D)|\) hits are Rademacher absolute-growth statements or
  explicitly parity-fixtured.
- `git diff --check -- chapters/examples/k3e_bkm_chapter.tex` passed.

## Residual Obligation

No ordinary compact Hall source dimensions or generator counts are proved;
those still require the parity fixture or finite Hall--Borcherds
recognition data.

