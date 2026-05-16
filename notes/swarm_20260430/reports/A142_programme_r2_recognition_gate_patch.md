# A142 -- Programme R2 Recognition-Gate Patch

## Claim Attacked

The R2 row in `chapters/examples/k3e_cy3_programme.tex` asserted a
chiral-bialgebra equivalence with \(\mathbf H_{\Delta_5}^{(N)}\) pinned
by three invariants.

## Patch

The R2 row now says the three data are target comparison invariants, not
a pinned equivalence. The displayed comparison with
\(\mathbf H_{\Delta_5}^{(N)}\) is putative and the chiral-bialgebra
equivalence is gated by finite Hall--Borcherds recognition, compact
provenance, parity, \(M,D,B,G,K,Q,A\), radical/no-extra/PBW, orientation,
and completion gates.

## Verification

```text
git diff --check -- chapters/examples/k3e_cy3_programme.tex
```

passed. Targeted search found no remaining R2 "pinned by three
invariants" claim.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
