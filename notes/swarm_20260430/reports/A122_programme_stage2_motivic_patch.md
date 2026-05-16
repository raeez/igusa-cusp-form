# A122 -- Programme Stage-2 / Motivic Recognition Patch

## Claim Attacked

`chapters/examples/k3e_cy3_programme.tex` still identified Stage-2 and
motivic DT / CoHA data with the Borcherds target without the finite
recognition gate.

## Patch

The Stage-2 identification is now gated by compact source provenance,
source orientation monodromy, Hall--Borcherds recognition, and
completion data. Corollary hypotheses name \(M,D,B,G,K,Q,A\),
radical/no-extra/PBW certificates, and strict completion transitions.

Davison character data are recast as compact-source Hilbert-series data
and target arithmetic tests. The statement \(Y^+=\CoHA(K3\times E)\) no
longer follows from character data alone; it requires recognition,
quotient/PBW, and completion checks. The Maass--Gritsenko sign is a
target orientation test, not a source identification.

## Verification

```text
git diff --check -- chapters/examples/k3e_cy3_programme.tex
```

passed. Targeted search for `Y^+`, `CoHA`, `Stage-2`, `Maass`, and
`Gritsenko` found the updated guarded anchors.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
