# A131 -- Duplicate Lattice-Automorphic Note Patch

## Claim Attacked

`notes/gluing_ch_part_7_lattice_automorphic.tex` repeated the stale claim
that Fourier/Jacobi/Borcherds coefficients directly produce CoHA
structure constants.

## Patch

The note now says coefficients determine automorphic/BKM arithmetic and
Euler/superdimension shadows. CoHA constants require finite Hall fixture
recognition. The `\Phi_N` discussion is now an automorphic recognition
target rather than a direct CoHA structure-constant source. The K3 x E
conjectural statement now uses a finite Hall source fixture and
Euler/superdimension projection.

## Verification

Targeted search for `structure constants`, `CoHA`, and `Fourier
coefficient` was reviewed, and the stale direct-identification phrases
were absent.

```text
git diff --check -- notes/gluing_ch_part_7_lattice_automorphic.tex
```

passed.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/notes/gluing_ch_part_7_lattice_automorphic.tex`
