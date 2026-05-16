# A136 -- Chiral-Bar-Cobar Recognition Audit

## Findings

Critical:

- `compute/lib/cy_bkm_algebra_engine.py` conflates root
  multiplicities, Borcherds product exponents, \(c(D)\), \(c(n,l)\),
  \(\phi_{0,1}\), and \(2\phi_{0,1}\), then hardcodes a verified
  coefficient table. This collapses target automorphic coefficients into
  source/root data without a finite recognition gate.
- `chapters/theory/cobar_construction.tex` claims
  \(\Omega_X(B_{\mathrm{ch}}(\mathcal H_{\Delta_5}))\simeq
  \mathcal H_{\Delta_5}\), a Hall-subcategory equivalence, and a
  proved convolution dGLA with basis over BKM generators and
  Gritsenko--Nikulin multiplicities.

High:

- `compute/tests/test_cy_bkm_algebra_engine.py` advertises broad BKM
  verification while mostly checking hardcoded coefficient tables.
- `chapters/theory/chiral_koszul_pairs.tex`, Vol II worked examples,
  and W-algebra chapters identify \(H_{\Delta_5}\), CoHA, or
  positive-half data without the finite Hall--Borcherds gate.
- `higher_genus_foundations.tex` contains exact \(\Delta_5\) one-loop /
  Borcherds-pushforward claims without finite coefficient recognition.

Medium:

- some CoHA/bar-cobar propositions are already conjectural but still need
  positive-half/full-double and finite source-data gates.
- an ADE chain-level engine promotes finite toy checks to a uniform
  theorem.

## Good Guardrails

Vol II contains a useful scalar-to-chain firewall in
`hall_borcherds_gravity_residual.py`, and a positive-half/full-double
distinction in `bar_chain_models_chiral_quantum_groups.tex`.

## Files Changed By Agent

None.
