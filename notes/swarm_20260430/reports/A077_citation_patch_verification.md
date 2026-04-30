# A077 - Citation Patch Verification

## Verdict

Patch is substantially correct. The old defect "GNII constructs
`\autcor`" is removed.

## Observed Anchors

- Product lift separated: `main.tex` near lines 1948, 2614, and 17015.
  Borcherds95 supplies the general lift; GNII supplies the explicit
  product; GN fixes theta normalization.
- Automorphic correction separated: `main.tex` near lines 5726, 5818,
  and 17019. `\autcor` and the denominator identity are now attributed
  to GN Sections 3-4 / Proposition 3.1.
- GKM presentation separated: `main.tex` near lines 12516 and 12534.
  `BorcherdsGKM88` is present in `proj.bib` and cited near `main.tex`
  line 12537.
- PBW/source conventions separated: product data are not being used to
  prove PBW, radical, no-extra-relations, or compact Hall recognition.

## Remaining Citation Defects

Non-fatal only.

- The generator-relation presentation definition near `main.tex` line
  15646 is covered earlier by the target statement, but a strict
  standalone lane should repeat `\cite{BorcherdsGKM88,KAC:1}` there.
- `main.tex` near line 2689 uses broad `\cite{GN}` for the
  singular-theta/weight statement. Not a separation failure, but exact
  source discipline would point back to Borcherds95 + GNII or to
  Proposition `\ref{prop:bgn-identification}`.

## Files Changed

None by the agent.

