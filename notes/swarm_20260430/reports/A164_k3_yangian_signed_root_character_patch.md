# A164 -- K3 Yangian Signed Root-Character Patch

## Result

Patched the CYQG K3 Yangian chapter so \(c(D)\) and related Borcherds
coefficients are protected signed root-character data, not ordinary
generator counts or BPS vector-space dimensions without a parity-refined
Hall--Borcherds presentation.

## Changed Path

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3_yangian_chapter.tex`

## Anchors

- `2285`: BKM side now uses signed protected root-character coefficients,
  not \(|c(D)|\) multiplicities.
- `2327`: spacelike sector treats \(c(D)\) as signed protected
  index/root-character target data.
- `2331`: added parity-refined \(E_D\) with
  \(\operatorname{sdim} E_D=c(D)\).
- `2353`: BPS states require parity-refined spaces with protected index
  \(c(D)\), not vector-space dimension \(|c(D)|\).
- `2405`: framework table/remark marks generator count as missing
  parity-refined Hall--Borcherds presentation data.
- `2570`, `6757`: later growth language now says protected
  root-character coefficients.

## Checks

- `git diff --check -- chapters/examples/k3_yangian_chapter.tex` passed.
- Targeted `rg` covered `|c(D)|`, `generator count`, `dimension`,
  `BPS states`, `recognition`, and `superdimension`.

## Status

No remaining \(|c(D)|\) hit was reported as an ordinary generator count
or BPS vector-space dimension.

