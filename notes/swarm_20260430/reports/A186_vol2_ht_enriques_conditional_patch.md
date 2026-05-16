# A186 -- Vol II HT Origins / Enriques Conditional Patch

## Result

Patched Vol II physical-origin and Enriques W-algebra lanes so scalar
physical / elliptic-genus evidence no longer asserts
\(\mathbf H_{\Delta_5}\), \(\Delta_5\), \(\log\Phi_{10}\), or Enriques
BKM orbifold recognition as chain theorems.

## Changed Paths

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/ht_physical_origins.tex`
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras-conditional.tex`

## Anchors

- `ht_physical_origins.tex:1713`: twisted 11D SUGRA is scalar comparison
  evidence, conditional on finite Hall--Borcherds/BV source recognition.
- `ht_physical_origins.tex:1877`: one-loop/two-loop BV is comparison
  datum, not a chain theorem producing \(\Delta_5\) or \(\log\Phi_{10}\).
- `w-algebras-conditional.tex:1707`: scalar Enriques weight/elliptic-genus
  facts preserved; \(\mathbf H_{\Delta_5}^{\mathrm{Enr}}\) orbifold
  recognition is conditional.
- `w-algebras-conditional.tex:1917`: multiplicity-halving theorem changed
  to conditional supermultiplicity/orbifold-denominator language.
- `w-algebras-conditional.tex:2008`, `2055`: Enriques SC
  face/topologisation follow-ons conditioned.

## Checks

- Targeted negative `rg`: old unsafe phrases had no hits.
- Targeted positive `rg`: new finite Hall--Borcherds, source/orbifold
  recognition, scalar-evidence, and non-chain-theorem language present.
- `git diff --check -- chapters/connections/ht_physical_origins.tex chapters/examples/w-algebras-conditional.tex`
  passed.

## Residual Obligation

Finite Hall--Borcherds source recognition, BV anomaly-complex comparison
to the Borcherds datum, and Enriques orbifold/root-sector recognition
remain explicit mathematical obligations.

