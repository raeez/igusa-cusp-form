# A189 -- Six-Dimensional HCS Postpatch Verifier

## Result

Read-only verification found the A182 overclaim repair closed. A189 made no
edits.

## Findings

- `six_d_hcs_feynman_coefficients.tex:131-141` and `209-221`: one-loop
  Igusa evidence is scalar only.
- `142-145`, `198-202`, `582-586`, `617-618`, `652-658`: \(\phi_{-2,1}\)
  is no longer conflated with the Igusa/K3 input lane.
- `137-141`, `516-519`, `637-642`: BV/BKM chain equality is conditional on
  finite Hall/BV source recognition, parity/root fixtures, and comparison
  maps.
- `252-257`, `315-318`, `423-434`: higher-loop Igusa/MZV comparisons are
  fenced by normalization/projection language, not literal coefficient
  equality.

## Residual

`176` had a minor notation slip: it wrote \(w_1=-1/24\) although the file
defines \(\widetilde w_1\) as the signed quantity and \(w_1\) as the
absolute scalar. The main thread patched this to \(\widetilde w_1\).

## Checks

- Targeted `rg` over \(\phi\), Igusa, BV, BKM, Jacobi, Hall, parity/root,
  comparison maps, scalar language, and overclaim verbs.
- `git diff --check -- chapters/theory/six_d_hcs_feynman_coefficients.tex`
  passed.

