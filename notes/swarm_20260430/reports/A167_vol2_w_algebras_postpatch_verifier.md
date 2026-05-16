# A167 -- Vol II W-Algebras Postpatch Verifier

## Result

Read-only verification found no fatal TeX issue, but found one high-risk
remaining Schur/celestial comparison and one medium-risk umbral label
phrase.

## Findings

- High: `w-algebras.tex:2483`, `2491`, `2515` still made the
  \(M_{24}\)-equivariant Schur index identify with the K3/celestial
  twining package and said the cross-volume arrow completes. This bypassed
  the finite Hall--Borcherds / finite-recognition gate just imposed above
  for Schur-index coefficient transport.
- Medium: `w-algebras.tex:2195` said the naive umbral label admits a
  direct umbral-moonshine attachment. The local divisor-rule theorem is
  root-system arithmetic, but the wording could be read as recognized
  class-\(\mathcal S\) Schur/Borcherds structure.

## Main-Thread Follow-Up

The main thread patched both exposed phrases:

- The umbral line now says the attachment is a Niemeier root-system label,
  not a recognized class-\(\mathcal S\) Schur/Borcherds object.
- The Schur/celestial comparison is now conditional on finite-recognition
  transport and is explicitly not, by itself, a compact-source
  Schur/Borcherds recognition theorem.

## Checks Run By Agent

- `git -C /Users/raeez/chiral-bar-cobar-vol2 status --short -- chapters/examples/w-algebras.tex`
- `git -C /Users/raeez/chiral-bar-cobar-vol2 diff -- chapters/examples/w-algebras.tex`
- Targeted `rg` over \(H_{\Delta_5}\), K3 coefficients, `k_N`, `N >= 3`,
  umbral, `N=6`, `N=24`, Schur-index, and finite-recognition gates.
- Line review of `chapters/examples/w-algebras.tex:1788-2535`.
- `git diff --check -- chapters/examples/w-algebras.tex` passed.

