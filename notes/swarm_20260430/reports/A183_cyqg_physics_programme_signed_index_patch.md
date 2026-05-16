# A183 -- CYQG Physics / Programme Signed-Index Patch

## Result

Patched the CYQG physics note and programme chapter so signed
\(f(nm,l)\) data are no longer read as ordinary bosonic/fermionic
generator counts without parity-recognition data.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex`
- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`

## Anchors

- `physics_bps_root_multiplicities.tex:422`: \(f(0,0)=20\) and
  \(f(1,1)=-128\) now read as signed index/superdimension; ordinary
  \(20\)- or \(128\)-dimensional spaces require a parity fixture or finite
  Hall--Borcherds recognition.
- `k3e_cy3_programme.tex:4837`: product exponent
  \(\mathrm{mult}\,\alpha\) is explicitly signed root character /
  superdimension.
- `k3e_cy3_programme.tex:4862`: generators-and-relations presentation is
  conditional on a parity-split source fixture or finite Hall--Borcherds
  recognition.
- `k3e_cy3_programme.tex:4881`: bare
  \(\mathrm{mult}(\alpha)=f(nm,l)\) assembly was replaced by signed
  supercharacter identity.

## Checks

- Targeted `rg` for stale `20-dimensional space`,
  `128 fermionic generators`, and `mult(alpha) = f` returned no matches.
- Positive `rg` confirmed signed root character, signed
  index/superdimension, parity fixture, parity-split source fixture, and
  finite Hall--Borcherds recognition vocabulary.
- `git diff --check -- notes/physics_bps_root_multiplicities.tex chapters/examples/k3e_cy3_programme.tex`
  passed.

## Residual Obligation

Ordinary parity-split \(20\)- or \(128\)-dimensional spaces remain
conditional data requiring a target parity fixture or finite
Hall--Borcherds recognition.

