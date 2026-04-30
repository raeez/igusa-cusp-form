# A014 report: OP variable dictionary and \(m=d-1\) firewall

Runtime id: `019ddbd1-a9b6-7da2-833a-6a546911f3ba`.
Nickname: Ptolemy.
Status: completed.
Files changed by agent: none.

## Claim Attacked

OP variable dictionary and \(m=d-1\) firewall.

## Formula Status

Proved. In `main.tex:2737`, with
\[
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n),
\]
the Mukai pairing gives
\[
Q_Y^2/2=\beta^2/2,\qquad
Q_Y\cdot P_Y=n,\qquad
P_Y^2/2=d-1.
\]
For \(\beta_h^2=2h-2\), this is exactly
\[
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
\]
Symbolic calculation confirms the formula. No hidden Todd/fourfold
residue remains in `main.tex`; the only hit is the guide's warning.

The OP scalar dictionary is also consistent:
`main.tex:15884` maps \(h-1\), \(d-1\), \(n\) to
\(q_{\rm Bch}\), \(s_{\rm Bch}\), \(r_{\rm Bch}\);
`main.tex:15922` has
\[
\chi_{10}^{\rm OP}=D_5^2=(64^{-1}\Delta_5)^2,\qquad
Z_{\rm OP}^X=-4096\Delta_5^{-2}.
\]
This matches A009 and CYQG `AP-CY357` / `AP-CY360`.

## Firewall Risks

### \(m\) As Wrapped/Local Classifier

Main live risk:
\[
m_{\rm Bch}=d_E-1
\]
only on the rank-one OP/D6 branch. Hence \(m_{\rm Bch}=0\) corresponds
to \(d_E=1\), still positive elliptic degree. Do not infer
projection-finite/local from \(m=0\).

Risk anchors:
`main.tex:8416`, `main.tex:14263`.

Replacement:
"local/wrapped color is determined by \(b_R^{\rm geom}\) /
\(d_{E,R}^{\rm geom}\), not by \(m_R\)."

### \(m_R\) Overload

\(m_R\) means trace exponent at `main.tex:8008`, but Hall multiplication
at `main.tex:10601` and `main.tex:13165`.

Recommended replacement:
keep \(m_R\) for multiplication; rename trace exponent to
\(m_R^{\rm Bch}\) or
\[
\deg_R^s:=\operatorname{pr}_3\overline\Pi_X.
\]

### \(n\) Overload

\(n\) is overloaded between Euler/D0 index and first Borcherds
coordinate. In the D6 theorem \(n=\chi(\mathcal O_Y)\), but generic
\((n,l,m)\) uses \(n\) as \(Q^2/2\).

Recommended replacement:
\[
(n_{\rm Bch},\ell_{\rm Bch},m_{\rm Bch})
=(h-1,\chi_Y,d_E-1).
\]

### \(P,Q,T\) Collision

Bare \(P,Q,T\) in the OP/DT variable theorem collide with Mukai
\(P_Y,Q_Y\) and normal-ordering \(T\). Use
\(P_{\rm DT},Q_{\rm DT},T_{\rm DT}\), or OP-labelled variables
throughout.

### \(b_R\) Collision

The older \(b_R\) collision is mostly healed: no surviving `s^{b_R}`
hits. Keep \(b_R^{\rm geom}\), or better \(d_{E,R}^{\rm geom}\), for
geometric support degree, and never identify it with \(m_R\) except by
an explicit branch-local formula.

### Broader Notation Collision

\((D_X)\) as a realization-data entry collides with \(\mathcal D_X\),
\(\mathfrak D_X\), and \(D_5\); \(R_{X,R}\) collides with finite height
\(R\). Anchors: `main.tex:12116`, `main.tex:14512`.

## Residual Obligations

Patch proposal only:
rename the trace exponent, replace \(m\)-based local/wrapped wording,
and rewrite the D6/OP dictionary with
\[
(n_{\rm Bch},\ell_{\rm Bch},m_{\rm Bch})
=(h-1,\chi_Y,d_E-1).
\]
Primary-source OP/GN audit remains as in A009; this report only verifies
the algebra and notation firewall.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`; inline `python3` symbolic check;
`git status --short`.
