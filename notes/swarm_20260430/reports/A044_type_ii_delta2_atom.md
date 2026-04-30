# A044 report: type-II wall \(\delta_2\) wrapped middle atom

Runtime id: `019ddbef-1d88-7e02-b0ac-8c1aa27e6a4e`.
Nickname: Ramanujan.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The graph-isogeny or reducible-curve middle atom constructs the Type-II
wall
\[
\delta_2\leftrightarrow(n,l,m)=(0,1,1)
\]
and proves the O2 rank-one Pfaffian wall theorem.

## Verdict

Not constructed. The only theorem-strength statement is that
\(\delta_2\) is wrapped, not projection-finite local. The graph-isogeny
and reducible-curve models are candidates with correct shadow numerics
and a local unreduced rank-one Ext calculation. They do not close
O2/hyb.

## Failure / Proof

Wrapped color / elliptic degree:
passes only as shadow data. Main requires source color by
\(b_R^{\mathrm{geom}}\), not target \(m\): `main.tex:7479`,
`main.tex:8015`. For \(\delta_2\), \(m=1\), OP gives \(d=m+1=2\), hence
positive elliptic degree and wrapped support: `main.tex:13419`.

Graph-isogeny candidate:
the critique constructs \(B_2=i_{\Gamma_\varphi,*}L\),
\(\deg\varphi=2\), \(\deg L=1\), hence \(d=2\), \(\chi(L)=1\),
\(h-1=0\), shadow \((0,1,1)\). But the wall object is then declared
\(C_{\delta_2}=A_2\oplus B_2\). The full charge of \(A_2\oplus B_2\) is
not proved to satisfy \(\overline\Pi_X(\widehat c_{\delta_2})=\delta_2\).
Main requires \(\widehat a\star\widehat b=\widehat c\) and
\(\overline\Pi_X(\widehat c)=\delta\): `main.tex:13306`.

Reducible-curve candidate:
the critique gives a reducible
\[
Y_{\delta_2}=C_1\times\{0_E\}\cup \{p_1\}\times E\cup\{p_2\}\times E
\]
with one node and shadow \((0,1,1)\). This is still only a shadow model;
the spectator elliptic component and global deformations are not shown
to disappear from the reduced normal quotient.

Semistability / wall equality:
not proved. The critique itself lists \(A_2,B_2\in\mathcal A_{s,t}\),
adjacent-chamber stability, and exact phase wall equality as remaining
obligations.

Reduced normal Ext splitting:
not proved. The local Koszul computation gives unreduced local
\(\operatorname{Ext}^1\simeq\mathbb C\),
\(\operatorname{Ext}^2\simeq\mathbb C\). Main requires reduced
off-diagonal normal lines \(L^\pm\), no other reduced normal directions,
nonzero reduced Kuranishi pairing, anti-invariant coordinate, and
quotient-compatible orientation: `main.tex:13328`.

Quotient orientation / invariant unit:
not proved. O2/hyb demands
\[
x_{\delta_2,R}\in\mathcal M_{\eta,R}^{\mathrm{wr,rig}},
\]
unit-weight lossless anchor, unreduced and reduced complexes,
\(s_{\delta_2}(u)=-u\), invariant \(\upsilon\), and vanishing quotient
orientation gerbes/characters: `main.tex:8515`. No candidate computes
these.

Pfaffian rank:
candidate rank-one is a local model, not theorem. Main says the sign
theorem computes only after residuals vanish and does not construct
charts, reduced Ext complexes, splittings, quotient orientations, or
transitions: `main.tex:1040`. Automorphic
\(d_{\delta_2}^{\mathrm{aut}}=1\) is separate from
\(N_{\delta_2}^{\mathrm{Pf}}\): `main.tex:1959`.

## Claim Status Recommendation

State as theorem only:
\(\delta_2\) is wrapped and cannot be projection-finite local.

State as candidate:
graph-isogeny \(B_2\) and reducible \(Y_{\delta_2}\) match the
\((0,1,1)\) shadow and give a local rank-one Ext target.

Keep O2 as conditional/open until semistability, full
\(\widehat\Gamma\)-charge matching, wall equality, reduced normal Ext
splitting, quotient orientation, invariant unit, Pfaffian rank, and
atlas overlaps are proved.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, `ls`; no build.
