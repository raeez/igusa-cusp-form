# A087 compact source provenance gate

Status: proposal only. No files edited.

Insert before the finite source matrix criterion, logically before any
A067 packet may be called populated.

```tex
\begin{theorem}[Compact source provenance gate]
Fix a finite downward-saturated window \(W\), put
\(S_W=W\cup(-W)\cup\{0\}\), and fix a finite Hall height \(R\).
A source fixture on \(S_W\) is populated only after the following
compact provenance datum is supplied.

\begin{enumerate}
\item A finite retained Liu--Hilbert schedule
\[
\mathcal X_R=\{\Xi=(\gamma,[a,b],(P_i)_{i=a}^b,N)\}
\]
closed under retained sums, subobjects, quotients, duals, local/wrapped
anchors, and all intermediate flag classes.

\item Retained object stacks
\[
\mathfrak M^{\rm sc}_{\Xi},\qquad
\mathfrak M^{\rm loc}_{\Xi,I},\qquad
\mathfrak M^{\rm wr}_{\Xi},
\]
and compactified extension/flag stacks
\[
\overline{\mathfrak E}^{\rm ret}_{\Xi_A,\Xi_B;\Xi_C},
\qquad
\overline{\mathfrak F}^{\rm ret}_{\Xi_1,\Xi_2,\Xi_3;\Xi_{12},\Xi_{23},\Xi_{123}},
\]
formed as closed retained Quot/flag-Quot/Postnikov-Quot substacks, or
else equipped with explicitly admissible exceptional compact-support
\(q_!\)-realizations.

\item Oriented d-critical data: BBDJS complexes \(\Phi_\Xi\), reduced
orientation lines \(o_\Xi\), global square-root/gerbe trivializations,
and coherent reduced Thom--Sebastiani transports on binary, flag, and
colored-tree correspondences.

\item Finite residual inertia after scalar, translation, and wrapped
anchor rigidification, with finite-stabilizer Borel obstruction classes
\[
\widetilde\beta^H_{R,S}=0\in H^2_H(S;\mathbb F_2),
\qquad
\lambda^H_{R,S}=0\in H^1_H(S;\mathbb F_2)
\]
on every retained object, extension, mixed/wrapped, and flag stratum.

\item A fixed constructible compact-support six-functor theory supplying
\(p^*\) or Gysin pullback, \(q_!\), \(p_!\), finite cohomological
dimension, base change, projection formula, and finite compact-support
realization.

\item A quotient-after-correspondence pseudofunctor \(Q_{E,R}\) and a
chain-level protected integration character \(I_R^{\rm prot}\), compatible
with product, coproduct, primitive projection, orientation descent, and
trace degree
\[
m_R=\operatorname{pr}_3\overline\Pi_X .
\]

\item Successor transition morphisms on stacks, coefficients,
orientations, Thom--Sebastiani transports, quotient functors, protected
integration, source bases, radical kernels, PBW filtrations, and parity
pieces, satisfying product/coproduct naturality, radical preservation,
strict PBW preservation, and finite-slice Mittag--Leffler.
\end{enumerate}

Then every row of `basis_provenance.csv` determines, relative to these
choices, a homogeneous compact-source class
\[
b^X_{R,\beta,\bar p,a}
\in
P^{\Pi,\mathrm{geom}}_{R,\beta,\bar p}
\]
represented by a retained stack stratum, irreducible critical cycle or
IC/vanishing-cycle summand, orientation trivialization, stabilizer
descent datum, Thom--Sebastiani transport, and protected-integration
row.

The matrices \(M,D,G\), hence \(B,K,Q\), are then source matrices
computed from compact-support vanishing-cycle pull-push. They are
eligible input for the finite source matrix criterion. Conversely, a
basis or matrix row without this provenance is not a source row. Target
labels may occur only in comparison rows \(A_\beta\); they cannot
populate the source fixture.
\end{theorem}
```

Proof skeleton: A025/A027/A028 supply the retained stack and admissible
pull-push conditions; A026 supplies the d-critical, vanishing-cycle, and
orientation separation; A029 supplies the finite-inertia gate for finite
protected cohomology; A030 supplies transition and ML conditions. A067
gives the packet fields; A075 makes `basis_provenance.csv` the first
source gate.

Main anchors: finite source kernel around `main.tex:11356`, finite
retained sector datum around `main.tex:13007`, primitive matrices around
`main.tex:13841`, conditional Dirac-Igusa stages around
`main.tex:14450`, finite source matrix criterion around
`main.tex:15275`.

Supremum check: `certificates/`, `data/finite_source`, and
`compute/finite_source` are absent, so no populated certificate exists.

