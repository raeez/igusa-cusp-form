# A093 compact source provenance integration audit

No files edited by the agent.

## Safest integration

Insert one short mathematical gate, not schema prose.

Required new label:

```tex
\label{thm:finite-compact-source-provenance-gate}
```

Insertion point: after the proof of
`prop:first-saturated-primitive-recognition-window`, before
`thm:executable-finite-source-matrix-criterion`.

Purpose: make provenance the first admissibility gate for the strongest
finite source theorem. The matrix criterion becomes a compact-source
theorem only after the source vectors are genuinely compact-source
vectors.

Patch skeleton:

```tex
\begin{theorem}[Finite compact-source provenance gate]
\label{thm:finite-compact-source-provenance-gate}
Let \(W\subset Q_+\setminus\{0\}\) be finite and downward saturated, and put
\[
S_W=W\cup(-W)\cup\{0\}.
\]
A compact Hall stage \(R\) is source-admissible on \(S_W\) only after every
basis vector
\[
b^X_{R,\beta,\bar p,a}\in P^X_{R,\beta,\bar p},
\qquad \beta\in S_W,
\]
has compact source provenance: a retained charge lift
\(\widehat c\) with \(\overline\Pi_X(\widehat c)=\beta\), a retained
stack/stratum or vanishing-cycle/IC summand representative, reduced
orientation and quotient-orientation data, Thom--Sebastiani transport,
finite-stabilizer linearization, protected integration data, and
successor-transition compatibility. Product, coproduct, pairing, and
comparison rows must be computed from these source representatives and
their compact correspondences.

The target labels
\(e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s\) may occur only in target
reference tables or in the codomain coordinates of
\(A_{\beta,\bar p}\). If the provenance gate fails, the packet is a
target or mock fixture and cannot serve as the compact-source hypothesis
in Theorem~\ref{thm:executable-finite-source-matrix-criterion}.
After the gate passes, the matrix, relation, no-extra, PBW, and
Mittag--Leffler clauses of that theorem are source-side clauses; when
they pass, finite primitive recognition holds on \(W\).
\end{theorem}
```

Then change the first sentence of the finite source matrix criterion to
require a source-admissible compact Hall stage \(R\) in the sense of the
new theorem.

## Retitle/fence recommendations

- Retitle `(R_X)` from `Primitive recognition` to
  `Primitive-recognition certificate`.
- Retitle the cofinal datum as `Cofinal finite-window
  primitive-recognition certificate`.
- Add an `(R0)` source-provenance and target-firewall clause in the
  cofinal datum.
- Fence target normal forms as target normal forms, not compact
  \(K3\times E\) sources.
- Make NO7 a subprotocol/corollary: it verifies radical descent only,
  not no-extra or PBW.

