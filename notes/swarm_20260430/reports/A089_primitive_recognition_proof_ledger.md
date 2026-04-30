# A089 primitive-recognition proof ledger

No edits made. The agent reran `compute/verify_lattice.py` and
`compute/verify_square_root.py`; both passed. The working tree was
already dirty.

Primary insertion anchor: after the proof of `thm:primitive-recognition`,
before `def:cofinal-primitive-recognition-datum` around `main.tex:12851`.

```tex
\subsection{Primitive-recognition proof ledger}
\label{subsec:primitive-recognition-proof-ledger}

The proof has six stages.  The Borcherds product fixes target signed
superdimensions, and the Gritsenko--Nikulin/Kac presentation fixes target
parity dimensions where that presentation has been computed.  A compact
\(K3\times E\) source is recognized only after finite source
representatives, pairings, radicals, relations, PBW, and transitions are
supplied and verified.

\begin{center}
\small
\begin{tabular}{p{0.17\textwidth}p{0.40\textwidth}p{0.34\textwidth}}
\hline
\textbf{Stage} & \textbf{Proof content} & \textbf{Boundary} \\
\hline
Target arithmetic &
The imported target is
\(G(\mathscr B_{\Delta_5})=\mathfrak g_{\Delta_5}\), with denominator
\(64^{-1}\Delta_5(2Z)\).  On \(W_{\le3}\) the target parity table is
\(\delta_i:1|0\), \(a_{ij}:10|0\),
\(2\delta_i+\delta_j:1|0\), \(\tau:29|93\), so
\(29-93=-64=f(1,1)\). &
These are target data.  They do not construct compact source primitives,
source pairings, radical kernels, or source bracket constants. \\

Source fixture &
For a finite window \(W\), put \(S_W=W\cup(-W)\cup\{0\}\).  A source
fixture \(\mathcal C_R(W)\) supplies neutral source bases
\(b^X_{R,\beta,\bar p,a}\), parity pieces, matrices
\(M,D,B,G,K,Q\), comparison maps \(A_{\beta,\bar p}\), relation rows,
no-extra kernel equality, PBW associated gradeds, and strict
transition/Mittag--Leffler rows. &
Target labels \(e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s\) occur only in the
target fixture or in the codomain of \(A_{\beta,\bar p}\). \\

Finite verifier &
The finite verifier is the theorem that
\(QB(P\otimes K)=QB(K\otimes P)=0\), \((Q\otimes Q)DK=0\), Hopf
adjointness, \(J_{\mathrm{BK}}\subset\ker\pi_W\),
\[
\ker\pi_W=
(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_{\le W},
\]
PBW associated-graded comparison, and strict ML transitions imply finite
recognition on \(W\). &
NO7 verifies radical descent only.  It does not imply no-extra-relations,
PBW, full parity matching, or source-to-target recognition. \\

Relation-closed window &
\(W_{\le3}\) is the first arithmetic window, not a relation-closed one.
The first relation-closed test should use
\[
W_{\mathrm{rel}}^+
=W_{\le3}^{\mathrm{act}}\cup R_4\cup I_4\cup C_{\le7}\cup\{2\tau\},
\]
or its downward closure when Definition~\ref{def:cofinal-primitive-recognition-datum}
is invoked literally. &
The added rows close the real Serre terminals, doubled isotropic rows,
\(\tau\)-real strings, odd--odd \(\tau\) rows, and complementary
height-seven strings.  Target arithmetic gives the expected rows; the
source theorem still requires \(\mathcal C_R(W_{\mathrm{rel}})\). \\

Cofinal limit &
A cofinal system \(\mathcal C_{R_\nu}(W_\nu)\), with downward-saturated
windows, strict transitions, and finite-slice ML stable images, passes to
\[
P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}.
\]
Exactness says no generator, relation, radical element, or
parity-cancelling summand appears only after completion. &
The target reference tower does not supply the source transition system. \\

Remaining obstruction &
The compact theorem still requires the geometric source: retained Hall
stacks and correspondences, quotient orientations, Pfaffian wall data,
protected integration, source chiral coalgebra, Koszul comparison, and
the primitive fixtures above. &
Until these are constructed, the compact Dirac--Igusa realization remains
an open theorem target, not a consequence of the target product. \\
\hline
\end{tabular}
\end{center}
```

Secondary anchors:

- Retitle/interpret first window near `main.tex:15011` as target
  arithmetic plus conditional source certificate.
- Insert any expanded \(W_{\mathrm{rel}}\) theorem after `main.tex:15234`,
  before the finite verifier at `main.tex:15275`.
- Keep NO7 as a sub-verifier at `main.tex:15380`.

Dependencies/labels: `thm:primitive-recognition`,
`def:cofinal-primitive-recognition-datum`,
`prop:global-recognition-cofinal-datum`,
`prop:first-saturated-primitive-recognition-window`,
`thm:executable-finite-source-matrix-criterion`,
`prop:finite-wlethree-no7-source-protocol`,
`prop:target-reference-normalization`.

Anti-patterns to avoid: target labels as source basis names; signed
dimension as parity data; NO7 as no-extra/PBW; \(W_{\le3}\) as
relation-closed; target reference tower as compact source; schema,
CSV, or verifier-file prose in `main.tex`.

