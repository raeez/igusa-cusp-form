# A196 -- E1 / EK Post-Follow-Up Verifier

## Result

Read-only verification found the core barred E1/EK claims guarded, with
two nearby structural remarks still needing D1--D5 guards.

## Findings

- Clean: `e1_modular_koszul.tex:3794` makes the \(\Delta_5\) inversion
  theorem conditional on D1--D5 and says the displayed arrow is only a
  target without them.
- Clean: `e1_modular_koszul.tex:3946` makes BD factorisation
  compatibility conditional and repeats compact source, source datum,
  parity/root fixture, PBW/no-extra, completion, and comparison maps.
- Clean: `e1_modular_koszul.tex:4105` keeps the same guard for
  \(\mathcal A=\mathbf H_{\Delta_5}\).
- Clean: `algebraic_foundations.tex:2880` says the available EK statement
  is a conditional quantisation target, not a uniqueness theorem.
- Residual: `e1_modular_koszul.tex:3854` and `3868` had structural
  \(\mathbf H_{\Delta_5}\) remarks not explicitly guarded by D1--D5.

## Checks

- Targeted `rg` over both scoped files for \(\mathbf H_{\Delta_5}\),
  \(\Delta_5\), counit/quasi-isomorphism, BD factorisation, \(E_1\)
  inversion, EK/Etingof--Kazhdan, uniqueness/gauge, PBW/no-extra,
  completion, and comparison maps.
- `git diff --check -- chapters/theory/e1_modular_koszul.tex chapters/theory/algebraic_foundations.tex`
  passed.

## Main-Thread Follow-Up

The main thread patched the two structural remarks so the ordering/averaging
and Siegel-modular associator claims are explicitly conditional on D1--D5,
and scalar target data absent those hypotheses.

