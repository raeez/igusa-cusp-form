# A182 -- Six-Dimensional HCS Feynman Coefficients Gate Patch

## Result

Patched the Vol II six-dimensional HCS coefficient lane so finite scalar
Igusa target evidence is not promoted to BV/BKM chain recognition.

## Changed Path

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/theory/six_d_hcs_feynman_coefficients.tex`

## Changed Anchors

- `130`: rewrote the \(24\) one-loop theorem as finite scalar Igusa target
  evidence, not BV/BKM recognition.
- `191`: separated \(\phi_{-2,1}\) holomorphic-at-cusp facts from the K3
  elliptic-genus/Jacobi input lane for the Igusa denominator.
- `511`: downgraded the four-channel table to scalar comparison and
  required Hall/BV source recognition, parity/root fixtures, and comparison
  maps for chain-level equality.
- `605`: kept Gritsenko--Nikulin coefficients as finite scalar targets
  only.
- `632`: made the all-loop BV-to-Igusa comparison conditional on missing
  finite Hall/BV, root/parity, and comparison-map data.

## Checks

- Targeted `rg` for \(\phi_{-2,1}\), scalar/BV/BKM phrases, Hall/BV
  fixtures, and stale overclaim phrases.
- `git diff --check -- chapters/theory/six_d_hcs_feynman_coefficients.tex`
  passed.

## Residual Obligation

Construct finite Hall/BV source recognition, specify parity/root fixtures
for \(\mathfrak g_{\Delta_5}\), and define comparison maps to the
Borcherds denominator lattice before asserting chain-level BV/BKM
coefficient identities.

