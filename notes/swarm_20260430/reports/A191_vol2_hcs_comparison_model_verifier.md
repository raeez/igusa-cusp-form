# A191 -- Vol II HCS / Comparison-Model Wording Verifier

## Result

Read-only verification found the HCS lane and comparison-model vocabulary
mostly clean, with two minor signed-\(w_1\) ambiguities.

## Findings

- Signed \(w_1\) lane is basically consistent: oriented
  \(\widetilde w_1=-1/24\), scalar \(w_1=|\widetilde w_1|=1/24\) at
  `six_d_hcs_feynman_coefficients.tex:126`, `129`, `176`, `597`.
- Minor ambiguity: `232` and `542` still flowed from the signed expression
  to positive \(1/24\) without explicit absolute value/orientation
  normalization.
- \(\phi_{-2,1}\)/Igusa/BV/BKM lane is scalar/conditional at `137`,
  `142`, `198`, `516`, `637`.
- Exact `certified comparison model` is gone from the scoped files.

## Checks

- Targeted `rg` for \(w_1\), \(\phi_{-2,1}\), Igusa, BV, BKM,
  scalar/conditional, and proof-status vocabulary.
- `rg -n "certified comparison model" ...` returned no matches.
- `git diff --check -- <both files>` passed.

## Main-Thread Follow-Up

The main thread patched `232` and `542` to state
\(\widetilde w_1=-1/24\) and \(w_1=|\widetilde w_1|=1/24\) explicitly.

