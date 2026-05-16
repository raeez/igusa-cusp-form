# A116 -- BKM Signed-Coefficient Dimension Patch

## Claim Attacked

`chapters/examples/k3e_bkm_chapter.tex` treated signed Borcherds
coefficients \(|c(D)|\) as full ordinary root or primitive dimensions.

## Patch

The chapter now treats \(c(D)\) as a signed primitive
character/superdimension. Ordinary dimensions are gated by a parity
fixture or a finite Hall presentation. The compact CoHA comparison now
requires finite recognition data, and the three-way comparison is stated
as signed indices/superdimensions/bar Euler exponents rather than
ordinary dimensions. The Fourier table was retitled/rephrased as signed
root characters, with parity fixtures separated from dimension.

## Verification

Targeted searches were run before and after for `|c(D)|`, `signed`, and
`superdimension`.

```text
git diff --check -- chapters/examples/k3e_bkm_chapter.tex
```

passed.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex`
