# A046 report: local Ext normal form for type-II wall atoms

Runtime id: `019ddbf0-ae26-7880-83fe-db11daed9eed`.
Nickname: Popper.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Local rank-one Ext/Koszul normal form for type-II wall atoms, and the
derived Pfaffian rank/sign formula
\[
K^{\mathrm{nor}}_\delta\simeq [\mathbb R \xrightarrow{u_\delta}\mathbb R],
\qquad
D_\delta(u)=\begin{pmatrix}0&u\\-u&0\end{pmatrix},
\qquad
\operatorname{pf}=u,\qquad
\epsilon_o(s_\delta)=(-1)^{N_\delta^{\mathrm{Pf}}}.
\]

## Verdict

The main O2 package is mostly correctly fenced as conditional/local. The
local Pfaffian algebra is correct, but it is not a geometric wall-sign
theorem until Liu-heart membership, semistability, wall equality, full
charge matching, reduced quotient, quotient orientation, invariant unit,
and atlas compatibility are proved.

## Key Anchors

Local-sign datum is explicitly finite/local and not global O2:
`main.tex:822`.

O2 obstruction tuple correctly requires chart, wall, split, unit, rank,
transition: `main.tex:950`.

Finite local-sign theorem is conditional on residual vanishing and says
it does not construct charts/splittings/orientations: `main.tex:1040`.

Hybrid/O2 compatibility correctly adds component, boundary, overlap,
quotient, and integration residuals: `main.tex:8409`.

Middle wall \(\delta_2\leftrightarrow(0,1,1)\), \(d=m+1=2\), is
correctly marked wrapped: `main.tex:13419`.

## Failure Modes

The rank-one self-Ext criterion is wording-dangerous at `main.tex:13380`:
"is obtained from" should be read only under all displayed hypotheses.
It does not by itself construct the retained wall object.

The proof line "Higher terms have order at least three and do not alter
the rank-one Pfaffian normal form" at `main.tex:13409` outruns the text
unless an equivariant real/parametric Morse lemma is supplied, preserving
quotient orientation and invariant unit.

The formal target normal form at `main.tex:14246` is safe only as target
algebra. It must not be cited as compact source geometry.

The color rule "local when \(m=0\), wrapped when \(m>0\)" at
`main.tex:14265` is a separate live risk: target Gram exponent \(m\) is
not intrinsic local/wrapped source color.

## Critique Anchors

Guide §11 states wall atoms remain local/unreduced until all source
checks are proved.

CYQG AP-CY379:
wall signs are not automorphic divisor data.

CYQG AP-CY388:
local rank-one Ext is not global type-II wall sign.

The critique overclaims at
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:44861`:
"This proves each wall atom..." should be rejected as theorem-strength.

A005 and A035 agree: local Ext/Koszul data do not close quotient
orientation, units, overlap descent, or O2/hybrid compatibility.

## Claim-Status Recommendation

Keep the local Pfaffian block as a proved formal/local calculation under
O2 hypotheses. Keep the geometric type-II wall atom theorem
conditional/open. Do not promote \(\epsilon_o(s_{\delta_i})=-1\) to
compact Hall monodromy until O1, O1+, O2, O2/hybrid, quotient
orientation, and transition residuals vanish.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `find`, and
`git status --short`; no build or tests.
