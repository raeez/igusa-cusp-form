# A043 report: type-II wall \(\delta_1\) local atom

Runtime id: `019ddbee-cf81-7010-aee5-fc3602111c1f`.
Nickname: Ampere.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The manuscript constructs a theorem-level \(\delta_1\) type-II local wall
atom, with source charge, local color, semistability, wall equality,
reduced Ext normal form, invariant Pfaffian unit, quotient orientation,
and Pfaffian rank all fixed.

## Verdict

Not proved. The manuscript constructs a target/local formal rank-one
crossing and a conditional source criterion. It does not construct an
actual retained \(\delta_1\) source atom.

## What Is Safe

Target charge:
\(\delta_1=2f_2-f_3\), with Gram label \((n,l,m)=(1,1,0)\), square
\(2\), signed multiplicity \(1\), and automorphic divisor order
\[
d^{\mathrm{aut}}_{\delta_1}=f(0,1)=1.
\]
Anchors: `main.tex:1855`, `main.tex:1965`, `main.tex:14708`.

Formal local Pfaffian block:
if a rank-one crossing \(K^{\mathrm{cross}}_{\delta_1}=[R\xrightarrow u
R]\) with invariant unit is supplied, then
\(\operatorname{pf}_{\delta_1}=u\), \(s_{\delta_1}(u)=-u\), and the
local sign is \(-1\). Anchors: `main.tex:868`, `main.tex:907`,
`main.tex:1040`.

Conditional source criterion:
if retained charges
\(\widehat a_{\delta_1},\widehat b_{\delta_1},\widehat c_{\delta_1}\)
exist with \(\widehat a\star\widehat b=\widehat c\),
\(\overline\Pi_X(\widehat c)=\delta_1\), stable adjacent factors \(A,B\),
one-dimensional reduced normal off-diagonal pieces, nonzero reduced
Kuranishi pairing, quotient-compatible orientation, and anti-invariant
real coordinate, then the normal form is \(\operatorname{Crit}(uv)\) and
\(N^{\mathrm{Pf}}_{\delta_1}=1\). Anchor: `main.tex:13306`.

## What Is Not Safe

Full source charge is not constructed. The manuscript assumes a retained
lift or uses the formal central target lift
\(\widehat c^0_{\delta_1}=(0,-\delta_1)\), but that point atlas is not a
geometric \(K3\times E\) wall atom. Anchor: `main.tex:14345`.

"Local color" is unsafe if inferred from \(m=0\). Source color is
determined by \(b_R^{\mathrm{geom}}\), not by the third Gram coordinate.
On the OP rank-one branch, \(m=d-1\); hence \(\delta_1\) has \(d=1\),
positive elliptic degree, so the reducible-curve candidate is
wrapped/mixed, not projection-finite local. Anchors: `main.tex:7357`,
`main.tex:7479`, `main.tex:15884`; see A031.

Semistability and wall equality are not proved for \(\delta_1\). They
are hypotheses in the self-Ext criterion, not outputs. Anchor:
`main.tex:13328`.

The reduced Ext normal form is not computed for an actual \(\delta_1\)
object. The local node calculation in the critique gives an unreduced
rank-one Ext shadow; it does not prove trace/K3-semiregularity
reduction, quotient normal quotient, absence of extra normal directions,
or equivariant real Morse normal form. Critique anchor:
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44621`.

The invariant unit is supplied, not derived.
\(s_{\delta_1}(\upsilon_{\delta_1})=\upsilon_{\delta_1}\) is exactly an
O2 residual. Anchor: `main.tex:994`.

Quotient orientation is not evaluated for \(\delta_1\). One must compute
\(\alpha_{\mathrm{red}}\), \(\alpha_{E,\mathrm{free}}\),
\(\widetilde\beta^H\), and \(\lambda^H=0\) on the actual retained
object, extension, mixed/wrapped, and flag strata. Anchor:
`main.tex:13454`.

Pfaffian rank \(N^{\mathrm{Pf}}_{\delta_1}=1\) is theorem-safe only
inside the supplied rank-one model or conditional criterion. It is not a
geometric consequence of \(d^{\mathrm{aut}}_{\delta_1}=1\).

## Candidate Atom

The critique proposes
\[
Y_{\delta_1}=C_2\times\{0_E\}\cup \{p\}\times E,
\]
with one transverse node, line bundles of degrees \(a_1,b_1\) satisfying
\(a_1+b_1=3\), giving \(\chi=1\) and OP shadow
\((h-1,n,d-1)=(1,1,0)\). This is a useful candidate. It is not
theorem-level: Liu-heart membership, semistability, exact wall equality,
full \(\widehat\Gamma_X\)-charge matching, reduced normal quotient,
invariant unit, quotient orientation, and O2/hybrid overlap
compatibility remain open.

## Recommendation

State \(\delta_1\) as target root and conditional rank-one local-sign
model proved; retained geometric wall atom candidate only. Do not call it
a constructed local atom. If the reducible OP candidate is used,
classify it as mixed/wrapped by \(b_R^{\mathrm{geom}}>0\), not local by
\(m=0\).

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, and `git status --short`; no build or
mutation.
