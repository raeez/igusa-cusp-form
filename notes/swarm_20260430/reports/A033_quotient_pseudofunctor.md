# A033 report: quotient-after-correspondence pseudofunctor

Runtime id: `019ddbe7-3811-7571-b343-e9f7afc73fb5`.
Nickname: Jason.
Status: completed.
Files changed by agent: none.

## Claim Attacked

\(Q_{E,R}\) is a quotient-after-correspondence pseudofunctor on the
finite correspondence/BM category, preserving \(p/q\) spans, flags,
BBDJS coefficients, orientations, Thom-Sebastiani transports,
base-change squares, and associativity 2-morphisms.

## Verdict

Partially healed, conditional. The main hybrid definition specifies
\(Q_{E,R}\) as a supplied pseudofunctorial datum, not an objectwise
quotient: `main.tex:7893`, `main.tex:7907`. It also names the required
comparison
\[
\theta^Q_{\mu,R}:Q_{E,R}q_!\operatorname{TS}p^*
\cong
\bar q_!\bar{\operatorname{TS}}\bar p^*(Q_{E,R}^{\boxtimes k})
\]
at `main.tex:7932`.

This is a specification target, not a construction. The later geometric
atlas weakens the assertion by saying \(Q_{E,R}\) is "obtained by
applying" equivariant BM chains and orientation descent at
`main.tex:13679`. That does not by itself supply pseudofunctor
coherence.

## Failure Mode

Missing construction-level data:

- Explicit reduced spans for every generator
  \(e=(Y\xleftarrow p\mathfrak E_e\xrightarrow q Z)\), with quotient
  squares for both \(p\) and \(q\), admissibility of
  \(\bar p^*,\bar q_!,\bar p_!\), and Beck-Chevalley/projection-formula
  witnesses.
- Composition 2-isomorphisms
  \(Q(f\circ e)\Rightarrow Q(f)\circ Q(e)\), unit coherences,
  pentagon/triangle identities, and compatibility with two-step flag
  associators.
- Descent of BBDJS coefficient complexes and orientation lines on
  object, extension, mixed, wrapped, flag, and higher colored-tree
  strata.
- Compatibility of reduced Thom-Sebastiani maps with quotient, flags,
  and base change.
- Finite stabilizer Borel-Cech null-trivializations on every retained
  stratum:
  \[
  \alpha^{\mathrm{red}}=0,\quad \alpha^{E,\mathrm{free}}=0,\quad
  \widetilde\beta^H=0,\quad \lambda^H=0.
  \]
  For \(E[2]\):
  \((r_1,r_2,r_3;\rho_1,\rho_2,\rho_3)=0\). For \(2^a\parallel N\):
  \((A_1^{(N)},A_{12}^{(N)},A_2^{(N)};
  \lambda_1^{(N)},\lambda_2^{(N)})=0\). Anchors:
  `main.tex:13454`, `main.tex:13519`.
- Wrapped-anchor transport through subobjects, quotients, outputs, and
  two-step intermediates. The determinant anchor has weight \(\chi(F)\),
  not unit weight automatically: `main.tex:7593`.
- Higher colored tree flags, units, refinement maps, symmetry/order
  conventions, and overlap coherences. The eight binary words only give
  arity-three associativity: `main.tex:7887`.

## Recommendation

Keep the current \(Q_{E,R}\) language only as conditional finite-stage
datum. Strengthen any geometric theorem using it so "orientation descent
+ equivariant BM chains" is not read as constructing the pseudofunctor.
The exact missing item is the quotient pseudofunctor package with
coefficient, orientation, TS, base-change, flag, stabilizer, anchor, and
transition coherences.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `ls`, and
`git status --short`; no build or tests.
