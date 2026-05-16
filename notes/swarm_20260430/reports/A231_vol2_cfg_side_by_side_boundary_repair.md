# A231 -- Vol II `cfg_side_by_side` boundary repair

## Claim attacked

`appendices/cfg_side_by_side.tex` asserted an hCS-to-\(U(\mathfrak g_{\Delta_5})\)
identification.

## Repairs

- Added local `\cB` shorthand.
- Replaced the Row 14 hCS-to-BKM assertion with a boundary object
  \(\cB^{\hCS}_{K3}\) and a scalar characteristic-map statement.
- Added explicit Vol III recognition hypotheses: scalar comparator
  \(\Delta_5\), finite Hall--Borcherds model
  \(\mathbf H_{\Delta_5}\), and primitive target
  \(\mathfrak g_{\Delta_5}\).
- Repaired the proof, table row, and obstruction remark so hCS/BV stops
  at the boundary object and characteristic series.

## Verification

`git diff --check -- appendices/cfg_side_by_side.tex` passed. Targeted
`rg` found no direct `U(\fg_{\Delta_5})` assertion; remaining
\(\mathbf H_{\Delta_5}\) and \(\mathfrak g_{\Delta_5}\) hits are
recognition-target language.

## Residual obligation

The actual Vol III recognition data remain external: scalar
\(\mathrm{ch}_{K3}=\Delta_5\), finite Hall--Borcherds model, and
primitive BKM extraction.
