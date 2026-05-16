# A192 -- E1 Modular Koszul Follow-Up Patch

## Result

Patched the remaining `e1_modular_koszul.tex` block that instantiated the
bar-cobar counit and BD-factorisation equivalence for
\(\mathbf H_{\Delta_5}\) unconditionally.

## Changed Path

- `/Users/raeez/chiral-bar-cobar/chapters/theory/e1_modular_koszul.tex`

## Anchors

- `3804`: D1-D5 hypotheses now explicitly include compact Hall source and
  completion/comparison maps.
- `3946`: BD theorem retagged `\ClaimStatusConditional`; no unconditional
  \(\mathcal A=\mathbf H_{\Delta_5}\) instantiation.
- `4105`: BD corollary retagged conditional and tied to D1-D5.
- `4181`: downstream formality remark uses the conditional theorem and
  conditions the \(\mathbf H_{\Delta_5}\) passage on D1-D5.

## Checks

- Targeted `rg`: no hits for old
  `Let $\cA=\mathbf H_{\Delta_5}$` or `\ClaimStatusProvedHere{}`
  residuals; conditional anchors present.
- `git diff --check -- chapters/theory/e1_modular_koszul.tex` passed.

## Residual Obligation

Compact Hall source, source datum, parity/root fixture, PBW/no-extra,
completion, and comparison maps remain hypotheses; the manuscript no
longer uses them as proved for \(\mathbf H_{\Delta_5}\).

