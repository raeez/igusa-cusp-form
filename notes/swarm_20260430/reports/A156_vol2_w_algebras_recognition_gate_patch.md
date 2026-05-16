# A156 -- Vol II W-Algebras Recognition-Gate Patch

## Result

Patched `chiral-bar-cobar-vol2` W-algebra examples so K3/Igusa
statements no longer promote protected characters, scalar Borcherds data,
or \(N\)-row heuristics to compact-source BKM recognition.

## Changed Path

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/w-algebras.tex`

## Anchors

- `1803-1840`: \(\mathbf H_{\Delta_5}\) and the cohomology class are
  conditional on finite Hall--Borcherds recognition plus parity/root
  fixtures.
- `1847-1868`, `1925-1943`: \(\mathbf H^{(N)}_{\Delta_5}\) is replaced
  by the protected VOA \(\chi_N\) unless recognition exists.
- `1947-1966`: BKM Chevalley/root-multiplicity and K3 elliptic-genus
  coefficient identifications are conditional.
- `1993-2082`: the \(N=2\) Borcherds/\(\Delta_5\) statement is kept as
  proved; \(N\ge3\) constant coefficient and weight are conditional
  fixtures.
- `2085-2190`, `2231-2296`: umbral, \(N=6\), \(N=24\), and cross-volume
  \(k_N\) language now require recognition or square-root-multiplier
  conditions.
- `2312-2386`: later \(H_{\Delta_5}\) Schur-index/elliptic-genus
  coefficient identifications are conditional.

## Checks

- `git diff --check -- chapters/examples/w-algebras.tex` passed.
- Targeted `rg` covered `H_{\Delta_5}`, `k_N`, `ClaimStatus`,
  `Delta_5`, `recognition`, `N\ge`, and `N \ge`.

## Status

The file now treats scalar/protected data as target-side unless the finite
Hall--Borcherds source gate supplies the missing source, parity, and root
fixtures.

