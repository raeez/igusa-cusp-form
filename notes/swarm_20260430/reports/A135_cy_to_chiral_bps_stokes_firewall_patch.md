# A135 -- `cy_to_chiral` BPS/Stokes Firewall Patch

## Claim Attacked

`chapters/theory/cy_to_chiral.tex` said the BKM root multiplicities
\(c(D)\) from \(\phi_{0,1}\) simultaneously count BPS states, walls, and
Stokes lines.

## Patch

The sentence now separates status: \(c(D)\) is the BKM/Stokes arithmetic
datum and signed superdimension target. BPS, wall, and Stokes
multiplicity interpretations require a chamber, DT/Hall identification,
orientation, and the finite Hall--Borcherds recognition gate.

## Verification

```text
git diff --check -- chapters/theory/cy_to_chiral.tex
```

passed. Targeted search found no remaining `simultaneously count`.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/cy_to_chiral.tex`
