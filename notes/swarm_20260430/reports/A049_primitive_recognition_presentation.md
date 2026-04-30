# A049 report: primitive recognition presentation

Runtime id: `019ddbf8-ce74-7953-9793-5079ea3c75a5`.
Nickname: Cicero.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Primitive recognition of the compact source as \(\mathfrak g_{\Delta_5}\),
treated as a presentation-level theorem rather than a dimension or
signed-character count.

## Verdict

`main.tex` mostly gets the boundary right. It requires the full
Borcherds-Kac presentation package before claiming
\[
P_X^{\Pi,\mathrm{red}}\cong \mathfrak g_{\Delta_5}.
\]
The safe reading is conditional: recognition follows only after source
representatives, brackets, relations, pairing/radical quotient, parity
dimensions, no-extra-relations, PBW, strict transitions, and
source-to-target maps are supplied from compact geometry.

## Failure Mode / Proof

Signed dimensions do not identify the algebra. A graded super vector
space with
\[
\operatorname{sdim} P_{(n,l,m)}=f(nm,l)
\]
can have zero bracket, hidden \(W\oplus \Pi W\) cancelling pairs, extra
relations, or a bad Hopf radical, while preserving the determinant. This
is exactly AP-CY368/AP-CY378/AP-CY384.

The theorem-safe route is presentation-theoretic:
\[
\widehat{\mathfrak F}(\mathscr B_{\Delta_5})
\to P_X^{\Pi,\mathrm{red}}.
\]
Relations put \(J_{\mathrm{BK}}\) in the kernel; radical comparison gives
the same quotient; no-extra-relations gives injectivity; generation gives
surjectivity; PBW/exact completion prevents hidden completed relations;
full parity dimensions rule out determinant-invisible cancellation.

## Local Anchors

Safe presentation package:
`main.tex:12469`, `main.tex:12488`, `main.tex:12556`.

Required relations and data:
`main.tex:12603`, `main.tex:12627`, `main.tex:12680`,
`main.tex:12714`, `main.tex:12743`, `main.tex:12769`.

Finite matrix criterion:
`main.tex:15268`. It requires \(M,D,B,G,K,Q\), source bases,
comparison maps, kernel equality, PBW, and strict ML transitions.

Source-to-target maps are correctly directional:
`main.tex:6932`, `main.tex:14012`. The source is not defined by a target
homotopy inverse.

## Exact Constants

\[
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
=n\delta_1+m\delta_2+(n+m-l)\delta_3.
\]
\[
((\delta_i,\delta_j))=
\begin{pmatrix}
2&-2&-2\\
-2&2&-2\\
-2&-2&2
\end{pmatrix},
\qquad
\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z).
\]

First window:
\[
\delta_i:1|0,\quad
\delta_i+\delta_j:10|0,\quad
2\delta_i+\delta_j:1|0,\quad
\delta_{123}:29|93.
\]
Also \(m(\delta_{123})=-93\), \(29-93=-64=f(1,1)\). Height-four
checks: \(108-90=18\). Doubled isotropic checks: \(10-9=1\).

## Risky Statements

`main.tex:5818` overattributes algebra construction to GNII Theorem 2.1.
A010's critique stands: use GN Section 3/Proposition 3.1 for the
correction algebra, GNII for product/generalization, Kac for
presentation/PBW background.

The \(29|93\) split is locally checked, but the survival of the listed
mixed words after the GN/Kac radical should be explicitly source-backed
or proved in the text. Determinant data alone gives only \(-64\).

Any future use of target bases \(e_i,E_{ij},u_{ij,r},w_s\) must remain
target-side until compact source bases and \(A_{\beta,\bar p}\) maps are
supplied. This is AP-CY384.

## Claim Status Recommendation

Retain target denominator algebra, target finite-window arithmetic, and
primitive recognition as a conditional presentation criterion.

Do not upgrade compact source recognition, Pfaffian equality, or chiral
Koszul comparison unless the source matrix package,
radical/PBW/no-extra-relations, parity split, and strict transition/ML
data are actually constructed.

## Residual Obligations

Fix the GN/GNII citation sentence; add a primary-source or local proof
anchor for low-degree word survival after radical quotient; construct
actual compact \(W_{\le3}\) source bases, \(M,D,B,G,K,Q,A_\beta\)
matrices, radical coideal checks, PBW associated-graded maps,
no-extra-relations kernels, and strict transition/ML data.

Commands run by agent:
read-only `sed`, `rg`, `nl -ba`; `python3 compute/verify_lattice.py`;
`python3 compute/verify_square_root.py`; `git status --short`; no edits.
