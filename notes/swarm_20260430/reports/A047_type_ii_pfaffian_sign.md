# A047 report: Pfaffian rank/sign extraction for type-II walls

Runtime id: `019ddbf1-1a4f-7fa3-ba03-f0a16d8a4b92`.
Nickname: Schrodinger.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Type-II wall sign extraction:
\[
\epsilon_o(s_{\delta_i})=(-1)^{N^{\mathrm{Pf}}_{\delta_i}}=-1
=\nu_{\Delta_5}(s_{\delta_i})
\]
for
\[
\delta_1=2f_2-f_3,\qquad
\delta_2=2f_{-2}-f_3,\qquad
\delta_3=f_3.
\]

## Verdict

No direct inference from OP scalar constants or Maass character was found
in the inspected current text. The firewall is mostly correct. The
remaining risk is not scalar leakage; it is promoting a supplied local
rank-one model to a retained global wall-atlas theorem before the wall
objects, quotient orientation, invariant units, overlaps, and Ext
splittings are constructed.

## Failure Mode / Proof

The safe local calculation is:
\[
K^{\mathrm{nor}}_\delta\simeq
\bigoplus_{j=1}^{N_\delta^{\mathrm{Pf}}}
[\mathbb R\xrightarrow{u_\delta}\mathbb R],\quad
s_\delta(u_\delta)=-u_\delta,\quad
\operatorname{Pf}=\upsilon_\delta u_\delta^{N_\delta^{\mathrm{Pf}}}.
\]
Thus
\[
s_\delta^*\operatorname{Pf}
=\chi_{\upsilon}(s_\delta)(-1)^{N_\delta^{\mathrm{Pf}}}\operatorname{Pf}.
\]
Only after the unit character is killed and \(N_\delta^{\mathrm{Pf}}=1\)
is computed from the reduced normal self-Ext chart does the local sign
equal \(-1\). Maass gives the target value
\(\nu_{\Delta_5}(s_{\delta_i})=-1\); divisor order gives
\(d_{\delta_i}^{\mathrm{aut}}=1\). Neither computes
\(N_\delta^{\mathrm{Pf}}\), \(\chi_\upsilon\), nor \(\epsilon_o\).

## Local Anchors

`main.tex:822`:
type-II local-sign datum explicitly lists chart, splitting, unit, rank.

`main.tex:950`:
O2 obstruction datum states rank-one model is not implied by
\((\delta,\delta)=2\), divisor order, or Maass character.

`main.tex:1040`:
finite local-sign theorem is conditional on
\(\mathfrak O^{\mathrm{O2}}_{\delta_i,R}=0\).

`main.tex:1307`:
O1+ requires Weyl determinant-line lifts and quotient torsor
compatibility.

`main.tex:1756`:
proof separates Hall-side Pfaffian sign from independent Maass target
sign.

`main.tex:1889`:
Maass check says it does not construct \(\epsilon_o\).

`main.tex:2047`:
three supplied generator signs extend by group theory only after O1+.

`main.tex:13306`:
local Ext criterion remains hypothesis-heavy; the "higher terms"
sentence needs an equivariant parametric Morse/unit check before theorem
use.

`main.tex:15894`, `main.tex:16094`:
OP constants are scalar normalization, not orientation data.

## Exact Constants / Formulas

\[
D_5=64^{-1}\Delta_5,\quad
\chi_{10}^{\mathrm{OP}}=D_5^2=4096^{-1}\Delta_5^2,\quad
Z_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
\(-4096=(-1)_{\mathrm{OP}}\cdot64^2\) is scalar normalization.

\[
\Delta_5(gZ)=\nu_{\Delta_5}(g)\det(CZ+D)^5\Delta_5(Z),\quad
\Delta_5^2\in H^0(\mathcal H_2,\mathcal L^{10}).
\]
\[
\nu_{\Delta_5}(s_{\delta_i})=-1,\quad
d_{\delta_1}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_2}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_3}^{\mathrm{aut}}=f(0,-1)=1.
\]
These are target data only.

## Data Needed Before A Wall Sign Theorem

Local:
retained wall objects for \(\delta_1,\delta_2,\delta_3\); Liu-heart
membership; semistability; exact wall equality; full
\(\widehat\Gamma_X\)-charge matching; for \(\delta_2\), wrapped/mixed
representative with \(b_R^{\mathrm{geom}}>0\); equivariant d-critical
chart; \(s_\delta(u)=-u\); reduced self-Ext complex; tangent/normal
splitting; vanishing splitting class; invariant Pfaffian unit; rank-one
normal quasi-isomorphism; overlap, boundary, component, transition, and
protected-integration compatibility.

Global:
O1 orientation gerbe section and quotient descent;
\(\alpha^{\mathrm{red}}=\alpha^{E,\mathrm{free}}
=\widetilde\beta^H=\lambda^H=0\) on object, extension, mixed, wrapped,
and flag strata; Borel mixed terms/differentials killed; O1+ Weyl action
with \([c_o]=0\), normalized \(\tau_i^2=1\), and
\(\omega_{i,\mathcal C}=0\); compatible cofinal HN transitions.

## Claim-Status Recommendation

Keep the type-II wall sign theorem conditional/open. State
\(\epsilon_o=\nu_{\Delta_5}\) only as a consequence of supplied
O1/O1+/O2 plus the independent Maass computation. Do not use OP scalar,
divisor order, or Maass values to infer Pfaffian rank parity.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `find`, and
`git status --short`; no build, tests, staging, revert, or mutation.
