# A151 -- Cobar Construction Recognition-Gate Patch

## Claim Attacked

`chapters/theory/cobar_construction.tex` claimed an unconditional
\(\Omega_X(B_{\mathrm{ch}}(H_{\Delta_5}))\to H_{\Delta_5}\), a
Hall-subcategory equivalence at \(\hbar^2=-1/8\), and a proved
convolution dGLA basis over BKM generators with Gritsenko--Nikulin
multiplicities.

## Patch

The \(H_{\Delta_5}\) block now has a finite Hall--Borcherds recognition
gate. The cobar map, Hall-subcategory equivalence, four-piece cobar
decomposition, Hom identification, and BKM-generator basis are
conditional on compatible finite gates: positive-half CoHA, Drinfeld
double completion, source provenance, parity/root fixture, and
independent coefficient matching. The cobar-side convolution dGLA status
was changed from `ClaimStatusProvedHere` to `ClaimStatusConditional`.

## Verification

```text
git diff --check -- chapters/theory/cobar_construction.tex
```

passed. Targeted search found no `ClaimStatusProvedHere` remaining in
the edited \(H_{\Delta_5}\) block.

## Changed Paths

- `/Users/raeez/chiral-bar-cobar/chapters/theory/cobar_construction.tex`
