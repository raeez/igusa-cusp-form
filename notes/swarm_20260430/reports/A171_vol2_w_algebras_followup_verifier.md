# A171 -- Vol II W-Algebras Follow-Up Verifier

## Result

Read-only verification found no high or medium issue after the main-thread
follow-up to A167.

## Findings

- `w-algebras.tex:2195`: the umbral divisor rule is now only a Niemeier
  root-system label and explicitly not a recognized class-\(\mathcal S\)
  Schur/Borcherds object.
- `w-algebras.tex:2314` and `2327`: the five-class Schur comparison is
  conditional and depends on finite Hall--Borcherds recognition.
- `w-algebras.tex:2365`: the Schur index is a protected-VOA invariant, not
  a Borcherds denominator identity without the recognition package.
- `w-algebras.tex:2484`, `2519`, `2524`: the celestial comparison assumes
  finite-recognition transport, and the displayed equality is explicitly
  not itself a Schur/Borcherds recognition theorem.

## Checks

- `git diff --check -- chapters/examples/w-algebras.tex` passed.
- Targeted `rg` confirmed the gating phrases at the divisor rule,
  five-class theorem, and celestial remark.
- `\ClaimStatusConditional` is defined in `main.tex`.
- Begin/end environment stack scan was clean.
- `chktex` produced style warnings only, no local fatal TeX syntax issue.

## Residual Obligation

The finite Hall/Jacobi/Borcherds recognition package and explicit
Schur/celestial source-target transport must be proved before the
displayed five-class comparisons can be promoted.

