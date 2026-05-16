# A199 Chiral Schur/`\mathbf H_{\Delta_5}` Conditional Patch

## Claim Attacked

`~/chiral-bar-cobar/chapters/examples/w_algebras_deep.tex` promoted
Schur scalar/class-S/EOT data to proved recognition of
`\mathbf H_{\Delta_5}`.

## Patch

- The theorem around `w_algebras_deep.tex:7496` now states a conditional
  finite/completed target character comparison and is marked
  `\ClaimStatusConditional`.
- The upgrade criterion around `w_algebras_deep.tex:7553` now requires
  an explicit completed source algebra, parity/supertrace fixture,
  finite-window root-space maps, denominator identity comparison, and
  normalization.
- The proof around `w_algebras_deep.tex:7681` now states that the
  coefficient `45` is target-character data, not a source generator
  count. Conway/McKay--Thompson remarks were adjusted to remain at
  character-target level.

## Checks

- Targeted `rg` found no remaining local hits for the old direct
  recognition strings.
- Targeted `rg` confirmed new `\ClaimStatusConditional`,
  finite/completed character, parity/supertrace fixture, root-space map,
  and Humbert divisor anchors.
- `git diff --check -- chapters/examples/w_algebras_deep.tex` passed.

## Status

Conditional. Genuine `\mathbf H_{\Delta_5}` recognition remains open
until `(R1)`--`(R5)` are supplied.

