# A048 report: Weyl sign comparison and Maass-character firewall

Runtime id: `019ddbf6-5a8e-78f2-8e91-731b3f30f68c`.
Nickname: Franklin.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Whether the manuscript derives Hall/Pfaffian orientation signs from
Maass character, automorphic divisor order, or OP scalar normalization.

## Verdict

No direct Maass-as-source-sign proof found. The manuscript mostly keeps
the firewall correct. The comparison
\[
\epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
=\nu_{\Delta_5}|_{W^{(2)}(\Lambda^{2,1}_{II})}
\]
is stated as conditional on supplied source data: O1, O1+, O2, and
Pfaffian-to-automorphic line comparison.

## Key Anchors

Automorphic character only:
`main.tex:5294`, `main.tex:5446`.

Scalar normalization firewall:
`main.tex:15894`, `main.tex:16027`, `main.tex:16094`.

O1/O1+ determinant-line and quotient orientation data:
`main.tex:1166`, `main.tex:1307`.

O2/Pfaffian local sign data:
`main.tex:822`, `main.tex:950`, `main.tex:1040`.

Maass target check separated from Hall orientation:
`main.tex:1889`, `main.tex:2012`.

Conditional source theorem:
`main.tex:14445`, `main.tex:14651`.

## Exact Formulas / Constants

\[
\Delta_5(gZ)=\nu_{\Delta_5}(g)\det(CZ+D)^5\Delta_5(Z),
\qquad
\Delta_5^2\in\mathcal L^{10}.
\]
\[
\nu_{\Delta_5}(s_{\delta_i})=-1,\quad
\nu_{\Delta_5}(s_{f_{-2}-f_2})
=\nu_{\Delta_5}(s_{f_2-f_3})
=\nu_{\Delta_5}(s_{f_2+f_3})=+1.
\]
\[
D_5=64^{-1}\Delta_5,\quad
\chi_{10}^{\mathrm{OP}}=D_5^2=4096^{-1}\Delta_5^2,\quad
Z_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}.
\]
\[
d^{\mathrm{aut}}_{\delta_1}=f(0,1)=1,\quad
d^{\mathrm{aut}}_{\delta_2}=f(0,1)=1,\quad
d^{\mathrm{aut}}_{\delta_3}=f(0,-1)=1.
\]
These divisor orders are target checks only, not
\(N^{\mathrm{Pf}}_{\delta_i}\).

## Residual Risks

`main.tex:2528` defines
\(\epsilon_{\det}:=\nu_{\Delta_5}\). Search shows no later misuse, but
the notation is a possible confusion point with \(\epsilon_o\).

`main.tex:13306` and `main.tex:13409` remain hypothesis-heavy: the
rank-one normal form needs the equivariant real/parametric Morse and
invariant-unit checks.

`main.tex:14246` is safe only as formal target normal form; it should
not be cited as compact source geometry.

## Claim-Status Recommendation

Keep the theorem conditional. State Maass/divisor/scalar data as
target-side checks. State \(\epsilon_o=\nu_{\Delta_5}\) only after
O1/O1+/O2, quotient-orientation linearizations, determinant-line cocycle
killing, invariant Pfaffian units, and type-II wall atoms are supplied.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, and `git status --short`; no build or
mutation.
