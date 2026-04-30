# A031 report: hybrid base definitions and local-color classifier

Runtime id: `019ddbe4-1835-76b0-9e62-89e18fc02c42`.
Nickname: Carver.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The manuscript's hybrid base and local-color classifier should separate
projection-finite/Ran-local \(K3\)-fibre sectors from wrapped
\(E\)-direction sectors, and must not infer locality from
\(m_{\mathrm{Bch}}=0\).

## Verdict

Mostly healed in the source definitions, but not clean globally. The
main definitions use the correct support criterion, but the formal
colored normal form still contains a false \(m\)-based classifier.

## Failure / Proof

The first-principles separation is correct at the definition level:
projection-finite means
\[
p_E(\operatorname{Supp}A)\subset F\subset E
\]
finite; wrapped means positive elliptic degree
\[
(p_E)_*[C]=b[E],\qquad b>0.
\]
Since \(E\) is irreducible, positive elliptic degree forces
\(p_E(C)=E\), so ordinary \(\operatorname{Ran}(E)\)-support locality
cannot see it. Anchors: `main.tex:7357`, `main.tex:7400`,
`main.tex:7421`.

The hybrid datum also correctly separates support degree from trace
degree: local/wrapped color is defined by \(b_R^{\mathrm{geom}}\), while
the \(s\)-trace exponent is
\[
m_R=\operatorname{pr}_3\overline\Pi_X.
\]
Anchors: `main.tex:7479`, `main.tex:8015`, `main.tex:12207`.

Live failure:
`main.tex:14263` says a positive degree \(\beta=\alpha(n,l,m)\) has
local color when \(m=0\) and wrapped color when \(m>0\). This directly
violates the D6-D2-D0 dictionary: for \(Y\subset S\times E\),
\[
P_Y=(1,0,1-d),\quad Q_Y=(0,-\beta,-n),\quad
\Pi_X(Q_Y,P_Y)=\left(\frac{\beta^2}{2},n,d-1\right).
\]
Thus on the OP/D6 branch \(m_{\mathrm{Bch}}=d_E-1\), so
\(m_{\mathrm{Bch}}=0\) means \(d_E=1\), still wrapped, not
projection-finite. Anchors: `main.tex:2737`, `main.tex:15884`.

Secondary risk:
the table header "elliptic-degree shadow" at `main.tex:8416` should say
"Borcherds trace exponent" or explicitly include the branch-local
conversion \(d_E=m_{\mathrm{Bch}}+1\). As written it invites the same
false transfer.

## Replacement Criterion

A target Gram degree \(\beta=\alpha(n,\ell,m)\) has no intrinsic
local/wrapped color. A retained source lift \(\widehat c\) mapping to
\(\beta\) is local iff \(b_R^{\mathrm{geom}}(\widehat c)=0\) and it is
represented by the closed-configuration local stack over \(E^I\). It is
wrapped iff \(b_R^{\mathrm{geom}}(\widehat c)>0\) and a rigidified
wrapped prequotient with lossless anchor \(\lambda_{\eta,R}\) is
supplied. Products change color by additivity of \(b_R^{\mathrm{geom}}\),
not by addition of the third Gram coordinate. The trace weight is
separately
\[
\deg_R^s(\widehat c):=\operatorname{pr}_3\overline\Pi_X(\widehat c).
\]

## Critique Anchors

A004 supports the projection-to-\(E\) locality repair but keeps
colored-tree factorization open. A014 and A024 flag exactly the
\(m=0\Rightarrow\) local error. CYQG AP-CY367/AP-CY391 agree:
projection-to-\(E\) support locality is the issue, and
\(m_{\mathrm{Bch}}=0\) is not locality.

## Claim-Status Recommendation

Keep the support-locality lemma and
\(b_R^{\mathrm{geom}}\)/trace-degree split; patch the formal colored
normal form at `main.tex:14265` before it is used as source geometry;
rename the trace exponent to \(\deg_R^s\) or \(m_R^{\mathrm{Bch}}\);
keep full hybrid factorization conditional until colored-tree flags,
units, overlaps, quotient-after-correspondence, and anchor-losslessness
are supplied.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, fixed-string `rg`, and
`git status --short` over `CLAUDE.md`, `AGENTS.md`, the three skill
files, `main.tex`, reports A004/A014/A024/A025, the 2026-04-30 guide,
and CYQG cache/antipattern anchors.
