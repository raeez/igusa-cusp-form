# A162 -- BPS Root Multiplicities Signed-Index Patch

## Result

Patched the CYQG physics note so K3 elliptic-genus coefficients are
protected BPS indices / signed BKM root characters, not ordinary generator
counts without a parity fixture or finite Hall--Borcherds recognition.

## Changed Path

- `/Users/raeez/calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex`

## Anchors

- `339`: \(f(nm,l)\) is the protected BPS index.
- `346`: subsection retitled to signed BKM root character.
- `360`: coefficient identified as \(\operatorname{sdim}\).
- `366`: parity fixture / finite Hall--Borcherds recognition requirement
  added.
- `380`: \(|f(nm,l)|\) count replaced by conditional ordinary odd
  dimension.
- `857`: conclusion now says signed root character/protected BPS index,
  not ordinary count.

## Checks

- `git diff --check -- notes/physics_bps_root_multiplicities.tex` passed.
- Targeted `rg` for `|f`, `odd generator`, `multiplicity`,
  `superdimension`, and `recognition` found no remaining stale
  \(|f|\)-as-count hit.

## Status

The note preserves the strongest true statement: the coefficient is the
protected signed datum. Ordinary even/odd dimensions require an additional
presentation or recognition fixture.

