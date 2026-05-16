# A147 -- BKM Residual Signed-Multiplicity Patch

## Claim Attacked

`chapters/examples/k3e_bkm_chapter.tex` retained ordinary BPS
multiplicity and `mult(alpha)=c(...)` language in later regions.

## Patch

Wall-crossing now uses signed root-character exponents, with ordinary
multipity/parity split gated. Bar-generator language records signed
Euler exponents. Denominator exponents now use `sdim`, and the
Harvey--Moore statement targets protected signed indices rather than
ordinary BPS counts or source dimensions. Proof-tower and imprimitive
formulas use signed-character/protected-index language.

## Verification

```text
git diff --check -- chapters/examples/k3e_bkm_chapter.tex
```

passed. Targeted search found no remaining hits for `|f(D`,
`multiplicity identity`, `mult(\alpha)=c`, or `BPS multiplicity`; only
expected `superdimension` hits remain.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`
