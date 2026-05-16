# A132 -- Unifying Cell-Four Firewall Patch

## Claim Attacked

`chapters/theory/gluing/sec_10_unifying.tex` still said the
Borcherds-lifted modular form assembles local Fourier coefficients into
global CoHA structure constants.

## Patch

Cell 4 now says Borcherds-lifted forms assemble automorphic/BKM target
arithmetic and Euler/superdimension shadows. Global CoHA/Hall structure
constants are source-side comparison data, available only after a finite
source fixture, Hall--Borcherds recognition, radical/no-extra/PBW checks,
and completion compatibility.

## Verification

```text
git diff --check -- chapters/theory/gluing/sec_10_unifying.tex
```

passed. Targeted search found no remaining exact `CoHA structure
constants` overclaim in the file.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/gluing/sec_10_unifying.tex`
