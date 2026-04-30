# A035 report: hybrid overlap descent and units

Runtime id: `019ddbe7-735c-7172-9cd4-5cf53e168cc0`.
Nickname: Halley.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Hybrid local/wrapped/mixed atlases glue on overlaps, with units
compatible with anchors, reduced \(E\)-quotient, Thom-Sebastiani
orientation transport, and O2 wall charts.

## Verdict

Not proved. The current text mostly heals the error by naming the needed
residuals, but the gluing/units/cocycles are supplied data, not
constructed vanishings.

## Failure Mode

The eight-word atlas proves at most binary two-step associativity:
\[
\mathfrak o^{\mathrm{assoc}}_{w,R}=0,\qquad w\in\{L,W\}^3.
\]
It does not prove full hybrid factorization. The manuscript says the
missing package is higher colored configurations, unit/vacuum maps,
symmetry/order conventions, refinement maps, descent, and overlap
coherences, recorded as \(\mathfrak o^{\mathrm{col}}_R\):
`main.tex:7832`, `main.tex:7887`, `main.tex:8118`.

Unit compatibility is only named. The source bar coalgebra has a vacuum
and counit after a supplied augmentation and after
\(\mathfrak O_{\mathrm{hyb},R}=0\): `main.tex:7051`,
`main.tex:7103`. That does not construct unit maps for the hybrid
colored atlas or prove their compatibility with mixed/wrapped
operations, \(Q_{E,R}\), anchors, and TS transports.

Anchor compatibility remains a real obstruction. The candidate
\[
\lambda(A)=\det Rp_{E,*}A\otimes\mathcal O_E(-\chi(A)0_E)
\]
has translation law
\[
\lambda(t\cdot A)=\lambda(A)+\chi(A)t,
\]
so it is unit-weight only after extra rigidification/cover data, and it
is not lossless on \(\chi(A)=0\) strata. The manuscript records this as
\(\mathfrak o^\lambda_R\), including unit, losslessness, mixed-flag, and
transition components: `main.tex:7587`, `main.tex:7623`.

Quotient compatibility is conditional. \(Q_{E,R}\) is required to be a
pseudofunctor on the finite correspondence/BM category, with comparison
maps
\[
\theta^Q_{\mu,R}:Q_{E,R}q_!\mathrm{TS}p^*
\cong
\bar q_!\overline{\mathrm{TS}}\bar p^*(Q_{E,R}^{\boxtimes k}),
\]
compatible with flag coherences and transitions. The residuals
\[
\mathfrak o^{Q,\mathrm{form}}_R,\mathfrak o^{Q,\mathrm{adm}}_R,
\mathfrak o^{Q,\mathrm{flag}}_R,\mathfrak o^{Q,\mathrm{tr}}_{R'R}
\]
are required to vanish, but no construction is supplied:
`main.tex:7893`, `main.tex:7930`, `main.tex:7945`.

Orientation/TS descent is a criterion, not a vanishing theorem. The
quotient-orientation system requires vanishing of ordinary, connected
\(BE\), finite Borel, and \(H^1(BH)\)-linearization defects, plus TS flag
pentagons: `main.tex:4107`, `main.tex:4144`, `main.tex:4202`. For
\(E[2]\),
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\quad
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2),
\]
and the residual character
\[
\lambda=\lambda_1x_1+\lambda_2x_2
\]
must also vanish. For \(2^a\parallel N,\ a\ge2\), the mixed term
\(A_{12}^{(N)}x_1x_2\) is separate: `main.tex:13519`.

The O2 overlap claim is explicitly residual. The wall atlas requires
\[
\mathfrak O^{\mathrm{O2/hyb}}_{\delta_i,R}
\]
including \(\mathfrak o^{\mathrm{unit}}_{\delta_i,R}\),
\(\mathfrak o^{\mathrm{atlas,ov}}_{\delta_i,R}\), quotient, and
integration components. For the middle wall,
\[
\delta_2\leftrightarrow(0,1,1),\quad m=1,\quad d=m+1=2,
\]
so the wall must pass through a wrapped/mixed stratum with a unit-weight
lossless anchor before quotienting: `main.tex:8415`, `main.tex:8481`,
`main.tex:8515`, `main.tex:13419`.

## Recommendation

Status: conditional/open, not theorem-strength. Keep
\(\mathfrak O_{\mathrm{hyb},R}=0\), \(\mathfrak o^{\mathrm{col}}_R=0\),
\(\mathfrak Q^{\mathrm{or}}_R\), and
\(\mathfrak O^{\mathrm{O2/hyb}}_{\delta_i,R}=0\) as explicit supplied
data until colored tree flag stacks, unit/vacuum maps, Cech overlap
cocycles, quotient pseudofunctor coherences, and orientation-gerbe
descent are constructed.

Commands run by agent:
read-only `sed`, `nl -ba | sed`, `rg`, `find`, and
`git status --short`; no build or tests.
