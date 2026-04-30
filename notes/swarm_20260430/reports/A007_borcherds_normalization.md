# A007 report: Borcherds normalization and constants

Runtime id: `019ddbcc-1332-7e41-87af-67e7bb5af691`.
Nickname: Epicurus.
Status: completed.
Files changed by agent: none.

## Claims Attacked

### \(\mathcal D_X\), \(D_5\), \(\Delta_5\), Leading \(64\)

Status: survives.

Manuscript convention is coherent:
\[
D_5(Z)=q^{1/2}r^{1/2}s^{1/2}
\prod(1-q^nr^ls^m)^{f(nm,l)}
=64^{-1}\Delta_5(Z),
\]
hence
\[
\mathcal D_X(Z)=64D_5(Z)=\Delta_5(Z).
\]

Local anchors:
`main.tex:73`, `main.tex:2453`, `main.tex:2606`,
`main.tex:2636`, `main.tex:16218`.

Primary spot-check:
GN 1995 has \((1/64)\Delta_5\) as the product and denominator
normalization; GN Part II calls the monic product \(\Delta_5\), matching
the manuscript's convention conversion. Sources checked by A007:
`alg-geom/9504006`, `alg-geom/9611028`.

### BKM Denominator Normalization

Status: survives.

The manuscript distinguishes product variables from
denominator-character variables:
\[
q^nr^ls^m=\exp(-\pi i(\alpha(n,l,m),z)),
\]
so the Weyl--Kac--Borcherds denominator uses \(2Z\):
\[
\operatorname{den}(\mathfrak g_{\Delta_5})
=D_5(2Z)=64^{-1}\Delta_5(2Z).
\]

Local anchors:
`main.tex:90`, `main.tex:15713`, `main.tex:16977`.

Primary spot-check:
GN 1995 Proposition 3.1 gives \((1/64)\Delta_5(2Z)=\Phi(z)\).

### OP Scalar Constant \(-4096\)

Status: survives as scalar normalization only.

\[
\chi_{10}^{\mathrm{OP}}=D_5^2
=(64^{-1}\Delta_5)^2=4096^{-1}\Delta_5^2,
\]
\[
Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}
=-4096\,\Delta_5^{-2}.
\]

Local anchors:
`main.tex:15894`, `main.tex:16027`, `main.tex:16094`,
`main.tex:16281`.

Primary spot-check:
Oberdieck--Pixton define \(\chi_{10}\) by the monic product and prove
the primitive partition function is the Laurent expansion of
\(-1/\chi_{10}\). Source checked by A007: `1706.10100`.

### Scalar Normalization Versus Geometry

Status: mostly healed. One residual theorem-status risk.

The manuscript explicitly says \(64\), \(4096\), and the OP minus are not
orientation data.

Anchors:
`main.tex:16094`, `main.tex:16340`, `main.tex:1658`,
`main.tex:3257`, `main.tex:4318`.

Residual risk:
`main.tex:1744` imports \(C_{\square,X}=-4096\) into the protected scalar
trace of a supplied \(\mathfrak D_X\). This is valid only if the datum
explicitly includes a trace comparison with the OP/DT branch. Otherwise
OP fixes the enumerative scalar branch, not the scalar trace of an
arbitrary compact first-order object.

### Notation Risk

\(\mathcal D_X\) is the virtual determinant, \(D_5\) is the monic
Borcherds product, \(\mathfrak D_X\) is the hypothetical first-order
operator, and `(D_X)` is also a compact-realization datum entry at
`main.tex:12116`, `main.tex:12353`. No formula error, but integration
should avoid bare \(D_X\). The guide line `D_X=\Delta_5` should read
\(\mathcal D_X=\Delta_5\) if propagated.

## Theorem-Status Recommendations

\(\mathcal D_X=\Delta_5\):
theorem-level only as normalized \(K_0\)-determinant form of the
GN/Borcherds product.

\(D_5=64^{-1}\Delta_5\):
convention/theorem from GN normalization conversion.

\(\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)\):
imported GN denominator theorem.

\(Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}\):
imported OP/Oberdieck scalar theorem, orientation-forgetful.

Compact \(\mathfrak D_X\), Pfaffian comparison,
\(\epsilon_o=\nu_{\Delta_5}\), and trace-to-OP comparison:
conditional/supplied, still open geometrically.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `git status --short`; arXiv source
spot-checks via `curl -Ls ... | gzip -dc | rg/sed` for
`alg-geom/9611028`, `alg-geom/9504006`, and `1706.10100`.
