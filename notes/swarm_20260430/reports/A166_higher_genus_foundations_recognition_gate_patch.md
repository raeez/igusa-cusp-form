# A166 -- Higher-Genus Foundations Recognition-Gate Patch

## Result

Patched `chiral-bar-cobar` higher-genus foundations so scalar
\(\Delta_5\), Borcherds, one-loop, pushforward, and coefficient claims no
longer promote to compact Hall/Borcherds source recognition.

## Changed Path

- `/Users/raeez/chiral-bar-cobar/chapters/theory/higher_genus_foundations.tex`

## Anchors

- `2833`: separating-node Igusa scalar gate.
- `4727`: genus-2 scalar target data separated from source recognition.
- `4765`: finite Hall--Borcherds source datum named.
- `4922`: one-loop SUGRA scalar fence.
- `9223`: Borcherds pushforward comparison made conditional.
- `9414`: synthesis source gate for \(\mathbf H_{\Delta_5}\).
- `9446`: denominator coefficients treated as target data.

## Checks

- Targeted `rg` over \(\Delta\), Borcherds, one-loop, pushforward,
  coefficient, Hall, CoHA, and source terms.
- Targeted stale-phrase scan for “coefficient is exactly,” “Borcherds
  pushforward gives,” and “is the higher-genus trace”: no hits.
- `git diff --check -- chapters/theory/higher_genus_foundations.tex`
  passed.

## Residual Obligation

Finite Hall--Borcherds source recognition remains conditional. The file
now names the missing data: oriented finite Hall/CoHA stages, parity
fixtures, compact source matrices, comparison maps, no-extra relations,
PBW, and strict transition compatibility.

