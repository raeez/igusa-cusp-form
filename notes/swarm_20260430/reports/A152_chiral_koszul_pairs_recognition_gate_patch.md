# A152 -- Chiral Koszul-Pairs Recognition-Gate Patch

## Claim Attacked

`chapters/theory/chiral_koszul_pairs.tex` presented \(H_{\Delta_5}\) as
a Koszul pair in the Hall subcategory of \(\CoHA_{K3\times E}\), with
self-duality and a denominator-supplied differential, without a finite
recognition gate.

## Patch

The section is now conditional. A finite Hall--Borcherds recognition
datum is required. The conductor claim, Koszul triple, self-Koszulness,
and differential are restricted to finite recognized windows, completed
double/pairing/source-differential data, and completion compatibility.
The Koszul differential now comes from \(d_{\mathrm{Hall}}\), not from
the denominator factor.

## Verification

```text
git diff --check -- chapters/theory/chiral_koszul_pairs.tex
```

passed. Targeted search found no remaining old phrases such as
`with differential supplied by`, `canonical quasi-isomorphism`, `The
Koszul complex computes`, or `presents as a chiral Koszul pair`.

## Changed Paths

- `/Users/raeez/chiral-bar-cobar/chapters/theory/chiral_koszul_pairs.tex`
