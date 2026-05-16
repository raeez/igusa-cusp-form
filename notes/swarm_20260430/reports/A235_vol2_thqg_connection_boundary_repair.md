# A235 -- Vol II THQG connection boundary repair

## Claim attacked

Four THQG connection files used direct \(H^2\), BV, complexity, or
perturbative-finiteness language as if \(\mathbf H_{\Delta_5}\) or
\(\mathfrak g_{\Delta_5}\) were already constructed.

## Repairs

- `thqg_anomaly_extensions.tex`: direct BKM \(H^2\) classification
  replaced by conditional Vol III Hall--Borcherds recognition plus
  Heegner characteristic comparison.
- `thqg_bv_ht_extensions.tex`: BV anomaly line made conditional on the
  recognised source package and HT graph-complex vanishing.
- `thqg_gravitational_complexity.tex`: complexity formula scoped to
  \(\mathbf H_{\Delta_5}^{\mathrm{src}}\) after recognition gates.
- `thqg_perturbative_finiteness.tex`: one-loop equality retained as
  scalar target; theorem status requires recognition and vanishing
  hypotheses.

## Verification

`git diff --check` passed on the four owned files. Targeted `rg` found
no direct \(H^2(\mathfrak g_{\Delta_5})\) pattern in the owned files;
remaining hits are guarded target/source-recognition language.
