# A073 - main.tex Recognition Patch Plan

No edits made by the agent. The agent used `chriss-ginzburg-rectify` and
verified the target arithmetic with `compute/verify_lattice.py` and
`compute/verify_square_root.py`.

## Patch Plan

1. `main.tex` near line 12469: rewrite `((R_X)) Primitive recognition`
   as a **source certificate datum**, not a recognition assertion.

Sketch:

```tex
\item[\((R_X)\)] \emph{Primitive-recognition certificate.}
This is a source-side certificate \(\mathsf{Cert}^{\mathrm{prim}}_X\).
It consists of compact primitive representatives, source matrices
\(M,D,B,G,K,Q\), source-to-target maps \(A_{\beta,\bar p}\), relation rows,
Hopf-radical ideal/coideal rows, no-extra kernel equality, PBW associated
graded rows, and strict transition/Mittag--Leffler rows. The
Gritsenko--Nikulin algebra is the target checked against this certificate;
it is not the certificate.
```

2. `main.tex` near line 12488: rename theorem to

```tex
\begin{theorem}[Primitive recognition certificate theorem]
```

Keep S1-S10, but rewrite the theorem lead so S5-S10 are explicit
certificate clauses, not consequences of target arithmetic. Add one
sentence after line 12531: GN Sections 3-4/Proposition 3.1 supply the
correction algebra; GNII supplies product data; Kac/Borcherds supply
presentation/PBW conventions.

3. `main.tex` near line 12846: insert a global proof-status ledger.
Rows: `target denominator algebra: imported/proved`; `W_{\le3} target
arithmetic: computed target-only`; `W_{\le3} source matrices: not
constructed`; `NO7 radical: conditional on M,D,G,K,Q`; `no-extra/PBW:
separate unproved source certificate rows`; `W_{\le7} terminal strings:
target rows known, source closure open`; `ML transitions: conditional
stable-image datum`.

4. `main.tex` near line 12848: retitle definition:

```tex
\begin{definition}[Cofinal finite-window primitive-recognition certificate]
```

Add an `(R0) Source-target firewall` before `(R1)`: target labels and
target arithmetic are codomain/reference data only. Strengthen `(R5)` and
`(R7)` by saying NO7 radical descent does not imply kernel equality or
PBW comparison.

5. `main.tex` near line 13836: soften proposition wording. Current text
can read as if compact matrices exist. Rewrite lead:

```tex
Assume a compact Hall stage supplies the following finite bases,
correspondences, compact-support integrals, and base-change identities...
```

Keep formulas. End proof with: ordinary PBW holds for the finite source
quotient; comparison with GN/Kac PBW is a separate `A_\beta`/no-extra/PBW
certificate.

6. `main.tex` near line 14012: add target-label quarantine to the
comparison-map proposition.

Sketch:

```tex
The symbols \(e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s\) are target basis labels.
They may occur only in the codomain of \(A_{\beta,\bar p}\). Source basis
vectors are denoted \(b^X_{R,\beta,\bar p,a}\) until \(Q_{\beta,\bar p}\)
and \(A_{\beta,\bar p}\) are supplied.
```

7. `main.tex` near line 14696: rewrite `Low-degree bracket information`
as target-only:

```tex
\begin{proposition}[Low-degree target bracket templates]
```

Move source obligations out of this proposition into the certificate
theorem below. Keep the table, Chevalley rows, `10=1+9`, `29|93`, and
`m(\delta_{123})=-93` as target facts.

8. `main.tex` near line 15004: strengthen to:

```tex
\begin{theorem}[\(W_{\le3}\) primitive-recognition certificate]
```

Structure: `Target fixture`: parity table and target templates. `Source
certificate`: neutral source bases with provenance; `M,D,B,G,K,Q`;
`A_{\beta,\bar p}`; relation rows; NO7; no-extra kernel equality; PBW
ranks; strict transitions. `Conclusion`: restricted isomorphism iff the
certificate verifies. Dimension equality alone is not recognition.

9. `main.tex` near line 15148: replace the height-four prose tail with a
ledger, not narrative drift:

```tex
\[
\begin{array}{c|c|c|c}
\text{row family} & \text{first outside }W_{\le3} & \text{target check} & \text{source status}\\
\text{real Serre terminal} & h=4 & \smult(3\delta_i+\delta_j)=0 & \text{open}\\
2a_{ij} & h=4 & 10-9=1 & \text{open}\\
[e_i,w_s]\text{ string} & h=4,5,6 & 108,-64,10 & \text{open}\\
(\operatorname{ad}e_k)^5u_{ij,r} & h=7 & -64,108,-64,10,0 & \text{open}
\end{array}
\]
```

10. Insert new theorem immediately after `main.tex` line 15227, before
the generic matrix criterion:

```tex
\begin{theorem}[\(W_{\le7}\) string-closure certificate]
```

Define

```tex
W_{\le7}=\{\sum c_i\delta_i:c_i\ge0,\ 1\le c_1+c_2+c_3\le7\}.
```

State: `W_{\le3}` is the first arithmetic window, not relation-closed.
`W_{\le7}` is the first window containing the terminal complementary
isotropic strings. A compact source closes this window only after
supplying the same certificate packet on
`W_{\le7}\cup(-W_{\le7})\cup\{0\}`, including terminal zero rows.

11. `main.tex` near line 15268: retitle:

```tex
\begin{theorem}[Finite primitive-recognition certificate verifier]
```

Add explicit verifier obligations:

```tex
\pi_{R,W}:\widehat{\mathfrak F}(\mathscr B_{\Delta_5})_{\le W}
\to P^{\Pi,\mathrm{red}}_{X,R,\le W}
```

is source-defined by `QB^X`, not by target bases.
Require separately:

```tex
\ker\pi_{R,W}
=
(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_{\le W},
```

PBW rank/isomorphism on associated gradeds, quotient tensor
nondegeneracy, strict PBW transitions, and finite-slice ML stable images.

12. `main.tex` near line 15373: demote to corollary:

```tex
\begin{corollary}[\(W_{\le3}\) NO7 sub-verifier]
```

Make it explicit: NO7 verifies radical descent only. It does not prove
no-extra-relations, PBW comparison, or source-to-target recognition.

13. Citation side patch: `main.tex` near line 5818 should not say GNII
Theorem 2.1 constructs `\autcor`. Replace with the GN/GNII split above.
If citing Borcherds 1988 in `main.tex`, a companion `proj.bib` entry is
needed.

