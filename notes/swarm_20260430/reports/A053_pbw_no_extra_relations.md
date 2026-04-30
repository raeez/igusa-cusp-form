# A053 report: PBW/no-extra-relations finite window

Runtime id: `019ddbf9-3d68-7ba0-ae3b-805b11ef6c84`.
Nickname: Wegener.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Finite \(W_{\le3}\) source matrices plus radical quotient prove PBW and
no-extra-relations.

## Verdict

Not proved unconditionally. In the current manuscript,
PBW/no-extra-relations are part of the finite recognition datum, not
consequences of existing source matrices. The target PBW and \(29|93\)
block are imported from Gritsenko-Nikulin/Kac; a compact source must
still prove them by finite source bases, matrix ranks, kernel equality,
and transition-compatible PBW associated gradeds.

## Failure Mode / Proof

The radical quotient only becomes a Hopf quotient after the matrix
identities
\[
QB(P\otimes K)=0,\qquad QB(K\otimes P)=0,\qquad (Q\otimes Q)DK=0,
\]
plus Frobenius/Hopf adjointness and transition preservation of \(K\).
This proves descent of bracket/coproduct through the radical. It does
not prove
\[
\ker\pi_W=
(\overline{J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}})_{\le W},
\]
which is exactly the no-extra-relations theorem.

Likewise ordinary PBW holds for a finite-dimensional Lie superalgebra
once the source quotient is constructed, but the manuscript's required
statement is stronger:
\[
\operatorname{gr}_{\mathrm{PBW}}U(P_X^{\Pi,\mathrm{red}})_{\le W}
\cong
\operatorname{gr}_{\mathrm{PBW}}U(\mathfrak g_{\Delta_5})_{\le W}.
\]
That requires a source-to-target finite Lie isomorphism or an explicit
associated-graded rank check. It is not forced by the radical quotient
alone.

## Local Anchors

`main.tex:12714`:
S6 states no-extra-relations as a required source theorem.

`main.tex:12743`:
S8 states completed PBW as a required source theorem.

`main.tex:12911`:
R5 finite kernel equality.

`main.tex:12933`:
R7 finite PBW compatibility.

`main.tex:15004`:
\(W_{\le3}\) target table and \(29|93\).

`main.tex:15268`:
finite source matrix criterion includes kernel equality and PBW iso as
checks.

`main.tex:15373`:
NO7 \(W_{\le3}\) source protocol.

## Constants Checked

For
\[
W_{\le3}=\{\sum c_i\delta_i: c_i\ge0,\ 1\le\sum c_i\le3\},
\]
\[
\delta_i:1|0,\quad \delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\delta_{123}:29|93.
\]
The script verifies
\([qrs]D_5/(qrs)^{1/2}=93\),
\[
m(\delta_{123})=-93,\qquad 29-93=-64=f(1,1).
\]
Height-four target checks: \(90,90,90,-540\), with signed/m/gap
\(108|90|18\).

## Claim-Status Recommendation

Keep as a conditional finite-matrix-checkable recognition criterion. Do
not state PBW/no-extra-relations as proved for \(W_{\le3}\) until compact
source bases, \(M,D,B,G,K,Q\), \(A_\beta\), kernel ranks, PBW
associated-graded ranks, and strict transition/ML stable-image data are
supplied.

## Residual Obligations

Construct actual \(W_{\le3}\) compact source bases, especially the
\(29|93\) \(\delta_{123}\) block; compute source \(M,D,B,G,K,Q\); prove
kernel equality; prove PBW associated-graded comparison; verify radical
ideal/coideal; define transition matrices preserving kernels and PBW
filtrations; prove finite-slice Mittag-Leffler stable images and
\(R^1\varprojlim=0\).

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `rg --files`, `git status --short`;
`python3 compute/verify_square_root.py` for target arithmetic only.
