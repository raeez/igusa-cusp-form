# A209 Vol II HCS/Kummer/Class-S Residual Patch

## Claim Attacked

A205 found remaining high/medium Vol II overclaims outside
`bv_brst.tex`: HCS boundary labels and BKM bilinear forms were still
used too strongly, and the KZ/DS K3/Kummer/Class-S lane still treated
`\mathbf H_{\Delta_5}` as an available anchor without source
recognition.

## Patch

- `~/chiral-bar-cobar-vol2/chapters/theory/six_d_hcs_feynman_coefficients.tex`
  now treats BKM boundary labels, bilinear form, tree pairing,
  root-multiplicity channels, and QME modulo `\hbar^4` as scalar or
  candidate target data unless the finite Hall/BV source, HCS chain map,
  parity/root fixtures, and denominator comparison are supplied.
- `~/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex`
  now makes KZ/DS deformations using `\mathbf H_{\Delta_5}`, Schur
  cocycle finite covers, Kummer restriction, and the three-topological-
  input lane conditional on Vol III/source recognition and scalar-lane
  selection where appropriate.

## Checks

- Targeted `rg` over both owned files; remaining risky phrases are in
  conditional/candidate contexts.
- `git diff --check -- chapters/theory/six_d_hcs_feynman_coefficients.tex chapters/examples/w-algebras-conditional.tex`
  passed.

## Open Obligations

Finite Hall/BV source, HCS-to-source chain map, parity/root fixtures,
denominator comparison, Vol III/source recognition, finite Schur cocycle
lift, and Kummer sublattice chain comparison.

