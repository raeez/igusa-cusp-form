# A197 Cross-Repo Static Verifier

## Checks

- `git diff --check` clean in all five repositories.
- `git diff --cached --check` clean in all five repositories.
- Semantic scan scope at final snapshot: `igusa-cusp-form` 7 scoped hits
  after exclusions, `calabi-yau-quantum-groups` 188, `chiral-bar-cobar`
  78, `chiral-bar-cobar-vol2` 66, `topological-strings` 5.
- Excluded PDFs, `out/`, `raw/`, `processed/`, cache, and swarm/report
  files.

## Fatal

- `~/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex` around
  7492-7542 promoted Schur scalar data to proved recognition of
  `\mathbf H_{\Delta_5}`. The theorem asserted
  `\chi[\mathcal T]=\mathbf H_{\Delta_5}` and then proved
  `\mathcal I^{Schur}(q)=\mathrm{ch}[\mathbf H_{\Delta_5}](q)` from
  class-S/Schur/EOT data. Cross-repo anchor:
  `~/calabi-yau-quantum-groups/chapters/examples/k3_chiral_bialgebra_platonic.tex`
  says the Schur-to-`\Delta_5` relation is a two-step composite, not a
  direct equality.

## High

- `~/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex`
  around 3541 asserted Humbert/class-S scalar data as a proposition
  proving `Z^{mix}|_{H_1}=\Delta_5`; the proof said Bruinier reciprocity
  forces the identification.
- The same file around 3799 displayed an isomorphism realizing
  `H_{\Delta_5}` from BRST-screened derived global sections before the
  source comparison had been built.
- `~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex` around
  5381 identified 24 local BV/HCS obstruction summands with BKM root-space
  multiplicities `c(n,\ell)` and called this the BV origin of
  `\mathbf H_{\Delta_5}`.

## Medium

- `~/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex`
  around 473 said the `24-5=19` deficit accounts for 19 imaginary root
  families, risking conversion of signed Borcherds coefficients into
  ordinary root-family structure.

## Status

The fatal/high/medium findings were split into A199, A200, and A201
worker scopes. A197 found no active `SCHEMA_COMPLETE` misuse, Enriques
halving, `\phi_{0,1}/\phi_{-2,1}` conflation, or unconditional E1/EK
`H_{\Delta_5}` uniqueness at its final snapshot.

