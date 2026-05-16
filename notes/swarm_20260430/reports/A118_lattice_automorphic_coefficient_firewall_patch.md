# A118 -- Lattice-Automorphic Coefficient Firewall Patch

## Claim Attacked

`chapters/theory/gluing/sec_7_lattice_automorphic.tex` converted
Fourier/Jacobi/Borcherds coefficients directly into CoHA multiplication
or structure constants.

## Patch

The file now separates automorphic/BKM target arithmetic and
Euler/superdimension shadows from Hall multiplication constants.
\(\Phi_N\) is treated as a recognition target rather than a direct CoHA
structure-constant table. The conjectural synthesis is preserved, but
it now passes through a finite source fixture and Euler/superdimension
projection.

## Verification

```text
git diff --check -- chapters/theory/gluing/sec_7_lattice_automorphic.tex
```

passed. Targeted search for `structure constants`, `CoHA`, and
`Fourier coefficient` found only guarded recognition/target-shadow
statements or ordinary Jacobi/Borcherds coefficient uses.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/gluing/sec_7_lattice_automorphic.tex`
