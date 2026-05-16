# A200 CYQG Humbert/BRST/Root-Family Gate Patch

## Claim Attacked

`~/calabi-yau-quantum-groups/chapters/examples/k3_chiral_algebra.tex`
still overclaimed that `24-5=19` counts root families, that
Humbert/class-S scalar data proves
`Z^{\mathrm{mix}}|_{H_1}=\Delta_5`, and that BRST-screened CDO global
sections already realise `H_{\Delta_5}`.

## Patch

- Around lines 473, 481, and 627, `24-5=19` is now rank-codimension
  arithmetic only. Signed Borcherds coefficients are not ordinary
  root-family counts.
- Around line 3541, the class-S/Humbert lane is now a normalized scalar
  comparison target
  `\mathcal N_{H_1}(Z^{\mathrm{mix}}|_{H_1}) \overset?= \Delta_5`,
  explicitly not a proof of equality or `H_{\Delta_5}` realization.
- Around lines 3786, 3803, and 3881, BRST-screened global sections are
  stated as a recognition problem with source algebra
  `\mathcal A_{\mathrm{scr}}`, parity/supertrace fixture,
  root-space maps, denominator comparison, and normalization.

## Checks

- Targeted `rg` for old equality/isomorphism/root-count patterns; the
  remaining hits are negated or comparison-obligation statements.
- `git diff --check -- chapters/examples/k3_chiral_algebra.tex` passed.

## Status

Conditional recognition lane. The scalar equality and
`H_{\Delta_5}` realization remain open until `Q_{H_1}`, parity, root
maps, denominator identity, and normalization are constructed.

