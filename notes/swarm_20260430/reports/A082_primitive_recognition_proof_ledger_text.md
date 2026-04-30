# A082 - Primitive Recognition Proof-Ledger Text

No files edited by the agent. The agent used the rectify workflow and
verified the target arithmetic with `compute/verify_lattice.py` and
`compute/verify_square_root.py`; both passed. `certificates/` is absent,
so no source certificate exists yet.

## Proposed Insertion Point

After the proof of `thm:primitive-recognition`, before
`def:cofinal-primitive-recognition-datum` near `main.tex` line 12853.

## Proposed Text

```tex
\subsection{Proof ledger for primitive recognition}
\label{subsec:primitive-recognition-proof-ledger}

This ledger records proof status, not claim weakening.  A
source-certificate entry is a theorem target: once the named finite
compact source datum is supplied and verified, the stated recognition
theorem follows.

\begin{center}
\small
\begin{tabular}{p{0.22\textwidth}p{0.22\textwidth}p{0.48\textwidth}}
\hline
\textbf{Object} & \textbf{Status} & \textbf{Proof content} \\
\hline
Borcherds product and denominator algebra &
proved/imported &
Borcherds, Gritsenko--Nikulin, and Kac supply the target algebra
\(G(\mathscr B_{\Delta_5})=\mathfrak g_{\Delta_5}\), the root map
\(\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}\), the real-root Gram matrix, and
\(\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)\).  This
is the target denominator algebra, not a compact Hall source. \\

OP/DT scalar square &
proved/imported &
The scalar branch gives \(Z^X_{\mathrm{DT}}=Z^X_{\mathrm{OP}}
=-4096\Delta_5^{-2}\).  It is orientation-forgetful and does not fix the
Pfaffian sign character or the compact source bracket. \\

First target window \(W_{\le3}\) &
computed target-only &
The target table is
\(\delta_i:1|0\), \(\delta_i+\delta_j:10|0\),
\(2\delta_i+\delta_j:1|0\), and
\(\delta_{123}:29|93\).  The equality \(29-93=-64=f(1,1)\), the \(27\)
mixed real-isotropic target words, and \(T_1+T_2+T_3=0\) are target
presentation data.  They are not source bases, source brackets, or
source radical data. \\

Height-four and height-seven relation closure &
computed target-only; open source target &
The target arithmetic gives height-four \(108|90|18\), doubled-isotropic
\(10|9|1\), real-real Serre exponent \(3\), and complementary
isotropic-string exponent \(5\).  Hence \(W_{\le3}\) is the first
arithmetic window but not relation-closed.  A relation-closed compact
source theorem must use a larger window, at least the \(W_{\le7}\)
string-closure packet. \\

\(W_{\le3}\) primitive recognition &
source-certificate theorem target &
If a compact Hall stage supplies neutral source bases with provenance on
\(W_{\le3}\cup(-W_{\le3})\cup\{0\}\), matrices \(M,D,B,G,K,Q\), maps
\(A_{\beta,\bar p}\), Chevalley/Serre/orthogonality/Jacobi/mixed rows,
NO7 radical descent, no-extra kernel equality, PBW associated-graded
comparison, and strict transition/Mittag--Leffler rows, then
\(G(\mathscr B_{\Delta_5})_{W_{\le3}}\cong
P^{\Pi,\mathrm{red}}_{X,W_{\le3}}\).  The missing datum is the populated
source certificate. \\

NO7 Hopf radical &
source-certificate theorem target &
The radical quotient is legitimate only after exact checks
\(QB(P\otimes K)=QB(K\otimes P)=0\),
\((Q\otimes Q)DK=0\), Hopf adjointness, quotient-tensor
nondegeneracy, and transition preservation of \(K\).  NO7 does not imply
no-extra-relations or PBW. \\

No-extra-relations and PBW &
source-certificate theorem target &
Injectivity requires
\(\ker\pi_W=(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_{\le W}\).
PBW requires an associated-graded isomorphism, not only ordinary PBW for
a quotient Lie superalgebra.  Both are independent certificate rows. \\

Comparison maps \(A_{\beta,\bar p}\) &
source-certificate theorem target &
The maps \(A_{\beta,\bar p}:L_{\beta,\bar p}\to
\mathfrak g_{\Delta_5,\beta,\bar p}\) are supplied after \(K\oplus L\)
and \(Q\) exist.  Target labels
\(e_i,E_{ij},u_{ij,r},T_i,M_{ij,r},w_s\) may appear only in target
fixtures or \(A\)-codomain columns, never as source basis names. \\

Cofinal completion &
source-certificate theorem target &
Compatible finite certificates on a cofinal sequence of downward-saturated
windows, with strict transitions and finite-slice Mittag--Leffler stable
images, give
\(P_X^{\Pi,\mathrm{red}}\cong\mathfrak g_{\Delta_5}\) after completion.
The current target computations do not supply these transition systems. \\

Compact Dirac--Igusa realization &
open theorem target &
The compact theorem still requires the geometric source:
retained Hall stacks and correspondences, orientation gerbes, Pfaffian
wall data, protected integration, the source chiral coalgebra, the Koszul
comparison, and the primitive certificates above.  The target reference
tower and point-atlas normal form do not construct this source. \\
\hline
\end{tabular}
\end{center}
```

## Core Anchors

`main.tex` near lines 5719, 12472, 12853, 13841, 14017, 14701, 15011,
15275, 15380, and 15781.

## Report Anchors

A049-A066 establish the source/target firewall and finite-window
obligations; A067/A072/A076 define the certificate/verifier/repo layout;
A069-A071 give the theorem ladder and `W_{\le7}` closure target; A074
confirms Vol III consistency and flags the coefficient-projection
overclaim.

