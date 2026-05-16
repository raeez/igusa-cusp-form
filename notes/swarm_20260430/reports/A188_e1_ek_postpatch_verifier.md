# A188 -- E1 / EK Postpatch Verifier

## Result

Read-only verification found the main A185 E1/EK target fixed, but one
later `e1_modular_koszul.tex` block still instantiated
\(\mathbf H_{\Delta_5}\) unconditionally.

## Findings

- Residual: `e1_modular_koszul.tex:3938` still stated, with
  `\ClaimStatusProvedHere{}`, that for
  \(\mathcal A=\mathbf H_{\Delta_5}\) the bar-cobar counit is a
  quasi-isomorphism. `4084` then gave a BD-factorisation equivalence.
- Clean: `e1_modular_koszul.tex:3794` is conditional, names D1-D5 finite
  Hall--Borcherds recognition, source datum, parity/root fixtures,
  PBW/no-extra, and comparison maps; `3833-3835` says the arrow is only a
  target without D1-D5.
- Clean: `algebraic_foundations.tex:2880` is a conditional quantisation
  target, not uniqueness theorem; Q1-Q4 name BKM/parity data, Hall source,
  exact EK theorem source, and PBW/no-extra/comparison-map defects.

## Checks

- Targeted `rg` for Etingof--Kazhdan, uniqueness, conditional
  quantisation target, Hall--Borcherds, PBW/no-extra, comparison,
  bar-cobar inversion, unconditional, and \(\Delta_5\).
- `git diff --check -- chapters/theory/e1_modular_koszul.tex chapters/theory/algebraic_foundations.tex`
  passed.

## Main-Thread Follow-Up

A192 patched the later bar-cobar counit / BD-factorisation block.

