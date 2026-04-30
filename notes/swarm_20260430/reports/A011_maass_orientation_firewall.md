# A011 report: Maass character and orientation firewall

Runtime id: `019ddbcc-4b6f-7e53-83da-7f850a321a6e`.
Nickname: Hypatia.
Status: completed.
Files changed by agent: none.

## Valid Attacks

### Automorphic Sign Language

`main.tex:5294` correctly says \(\Delta_5\) is a section of
\(\mathcal L^5\otimes\nu_{\Delta_5}\), not a scalar. The reflection
block at `main.tex:5355` is valid only as Maass /
orthogonal-trivialization character data:
\[
\nu_{\Delta_5}(s_{\delta_i})=-1,\qquad
\nu_{\Delta_5}(s_{f_{-2}-f_2})
=\nu_{\Delta_5}(s_{f_2-f_3})
=\nu_{\Delta_5}(s_{f_2+f_3})=+1.
\]
It must not be cited as determinant-line monodromy.

### Scalar Constants

The constants
\[
D_5=64^{-1}\Delta_5,\qquad
Z_{\mathrm{OP/DT}}=-4096\,\Delta_5^{-2}
\]
are scalar normalizations. They do not define \(\epsilon_o\).

CYQG anchor: `AP-CY365`.

### Divisor Order Versus Pfaffian Rank

The automorphic calculation gives
\[
d^{\mathrm{aut}}_{\delta_1}=f(0,1)=1,\quad
d^{\mathrm{aut}}_{\delta_2}=f(0,1)=1,\quad
d^{\mathrm{aut}}_{\delta_3}=f(0,-1)=1
\]
at `main.tex:1965`. This checks the target zero order only. It does not
prove
\[
N^{\mathrm{Pf}}_{\delta_i}=1
\]
for the reduced Hall normal self-Ext factor.

CYQG anchor: `AP-CY379`.

### Group-Theoretic Extension

Once O1+ gives an honest Weyl lift, the presentation
\[
W^{(2)}(\Lambda^{2,1}_{II})
=\langle s_{\delta_1},s_{\delta_2},s_{\delta_3}
\mid s_{\delta_i}^2=1\rangle
\]
implies characters are determined by three generator signs. This proves
only "three geometric signs imply a character"; it does not produce
those signs.

Anchor:
`main.tex:2047`.

## Theorem Boundaries

Automorphic character data:
\[
\Delta_5(gZ)=\nu_{\Delta_5}(g)\det(CZ+D)^5\Delta_5(Z),
\qquad \Delta_5^2\in\mathcal L^{10}.
\]
Anchor: `main.tex:5294`.

Weyl/BKM data:
\[
\delta_1=2f_2-f_3,\quad
\delta_2=2f_{-2}-f_3,\quad
\delta_3=f_3,
\]
with Cartan off-diagonal \(-2\), no finite braid relations, and
abelianization \((\mathbb Z/2)^3\).
Anchor: `main.tex:2047`.

Geometric Hall/Pfaffian data:
O1 requires reduced orientation plus quotient descent:
\[
\widetilde\beta^H_{R,S}\in H^2_H(S;\mathbb F_2),\qquad
\lambda^H_{R,S}\in H^1(BH;\mathbb F_2)=0.
\]
Anchor: `main.tex:4107`.

O1+ requires Weyl determinant-line lifts:
\[
[c_o]=0,\qquad \tau_i^2=1,\qquad \omega_{i,\mathcal C}=0.
\]
Anchor: `main.tex:1307`.

O2 requires actual wall atoms, charts, splittings, invariant units, and
rank-one normal Pfaffian factors:
\[
K^{\mathrm{nor}}_{\delta_i,R}\simeq[\mathbb R\xrightarrow{u_i}\mathbb R],
\quad s_{\delta_i}(u_i)=-u_i,\quad s_{\delta_i}(\upsilon_i)=\upsilon_i.
\]
Anchor: `main.tex:1040`.

Only after O1/O1+/O2:
\[
\epsilon_o(s_{\delta_i})=(-1)^{N^{\mathrm{Pf}}_{\delta_i}}=-1
\]
and then group theory gives
\[
\epsilon_o|_{W^{(2)}(\Lambda^{2,1}_{II})}
=\nu_{\Delta_5}|_{W^{(2)}(\Lambda^{2,1}_{II})}.
\]
Anchor: `main.tex:1756`.

## Residual Obligations

1. Compute \(\widetilde\beta^H\) and \(\lambda^H\) on every retained
   object, extension, wrapped, mixed, and flag stratum.
2. Kill \([c_o]\) and all \(\omega_{i,\mathcal C}\) for retained
   type-II wall transports.
3. Construct the three wall atoms, especially wrapped
   \(\delta_2\leftrightarrow(0,1,1)\), with semistability, charge
   match, reduced normal Ext splitting, invariant unit, and overlap
   compatibility.
4. Keep Maass values and divisor orders as target checks only.

Commands run by agent: read-only `sed`, `nl -ba`, `rg`, `find`,
`git status --short`. No build.
