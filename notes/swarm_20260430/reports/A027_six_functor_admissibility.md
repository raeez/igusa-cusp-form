# A027 report: six-functor admissibility for retained Hall pull-push

Runtime id: `019ddbe2-35fe-7b83-acb3-2425ce34e2a1`.
Nickname: Gauss.
Status: completed.
Files changed by agent: none.

## Claim Attacked

The retained compact Hall product
\[
m_R=q_!\operatorname{TS}^{\mathrm{red}}p^*
\]
at `main.tex:13163`, `main.tex:13664`, and `main.tex:11353`.

## Verdict

Conditionally admissible only as a supplied finite atlas theorem. It is
not admissible as a constructed compact Hall product until the
hypotheses below are stated explicitly.

## Failure Mode

Source/target maps are not enough if the middle stack is raw exact
triangles. The safe compactified convention is:
\[
0\to A\to C\to B\to0,\qquad
p(C,A\subset C)=(A,C/A),\qquad q(C,A\subset C)=C.
\]
Then
\(\overline{\mathfrak E}^{\mathrm{ret}}_{\Xi_A,\Xi_B;\Xi_C}\)
must be a closed derived substack of a relative
Quot/flag-Quot/Postnikov-Quot stack over the output. Only then is \(q\)
proper/projective in the compactified model. Raw exact triangles fail
properness; the DVR cone example appears at `main.tex:8222` and
`main.tex:13724`.

\(q_!\) is acceptable only as exceptional compact-support pushforward in
a fixed six-functor theory. The text says \(f_!\) is exceptional direct
image, not ordinary proper pushforward, at `main.tex:11381`. Every
theorem using \(q_!\) must say the formalism supplies constructibility,
finite cohomological dimension, base change, projection formula, and
finite compact-support realization. The affine Ext-stratum normalization
is:
\[
R\Gamma_c(\mathbb A^d,\mathbb C)=\mathbb C(-d)[-2d].
\]

Finite type is not finite protected cohomology. Residual
\(\mathbb G_m\) gives
\[
H^\bullet(B\mathbb G_m,\mathbb C)=\mathbb C[u],
\]
so scalar, direct-sum, parabolic, and translation stabilizers must be
rigidified to finite inertia before finite protected cohomology is
claimed; anchor `main.tex:11401`.

Quotient by \(E\) must occur after correspondences. \(Q_{E,R}\) must be
a pseudofunctor on the finite correspondence/BM category, not a quotient
of object stacks followed by a new product; anchor `main.tex:7893`. The
comparison
\[
\theta^Q_{\mu,R}:\;
Q_{E,R}q_!\operatorname{TS}p^*
\cong
\overline q_!\overline{\operatorname{TS}}\,\overline p^*
(Q_{E,R}^{\boxtimes k})
\]
must be part of the data.

Finite stabilizers require Borel, not pointwise, descent. For every
retained object, extension, mixed/wrapped, and flag stratum \(S\),
require
\[
\widetilde\beta^H_{R,S}=0\in H^2_H(S;\mathbb F_2),\qquad
\lambda^H_{R,S}=0\in H^1_H(S;\mathbb F_2),
\]
with overlap, correspondence, flag, and transition compatibility. The
full-level checks specialize as in `main.tex:13519`: for \(N=2\),
\(r_1=r_2=r_3=0\) and \(\rho_1=\rho_2=\rho_3=0\); for
\(2^a\parallel N\), require vanishing of the \(y_1,x_1x_2,y_2\)
coefficients and the two degree-one characters.

Vanishing cycles and Thom-Sebastiani are not automatic from
boundedness. Need oriented d-critical stacks, BBDJS coefficients,
reduced orientation lines, and coherent reduced TS transports on binary,
flag, and colored-tree stacks. The cosection compatibility formula must
be part of the atlas:
\[
q^*\operatorname{CS}_{C}=p_1^*\operatorname{CS}_{A}
+p_2^*\operatorname{CS}_{B}.
\]
Local BBDJS/TS assumptions are isolated at `main.tex:485` and
`main.tex:523`.

## Required Wording

Before any compact Hall product theorem, state:

"Fix a finite retained Liu-Hilbert schedule \(\mathcal X_R\) of classes
\[
\Xi=(\gamma,[a,b],(P_i)_{i=a}^b,N)
\]
closed under retained sums, subobjects, quotients, duals, local/wrapped
anchors, and all intermediate flag classes. For every compatible product
and flag, suppose finite-type finite-inertia quasi-smooth oriented
d-critical Artin stacks, compactified closed-filtration/flag-Quot
correspondences or explicitly admissible exceptional
\(q_!\)-correspondences, BBDJS vanishing-cycle coefficients, reduced
orientation lines, quotient-orientation trivializations,
finite-stabilizer zero characters, Thom-Sebastiani flag coherences,
base-change/projection-formula witnesses, \(E\)-quotient
pseudofunctoriality, protected integration as a chain-level character,
and HN transition compatibilities are supplied. Then
\(q_!\operatorname{TS}^{\mathrm{red}}p^*\) defines the finite retained
Hall product."

Do not say fixed full Liu classes \(C_R\) alone construct the compact
Hall source. That is the weak point at `main.tex:13008`.

## Critique Anchors

A004:
compactified correspondences and colored-tree gap.

A022:
\(q_!\) only exceptional/proper-support.

A025:
exact retained stack package and maps \(p,q\).

A026:
d-critical/vanishing-cycle/orientation status.

CYQG AP-CY375:
raw exact triangles are not proper Hall correspondences.

## Residual Obligations

Replace \(C_R\) by retained Liu-Hilbert schedules in the theorem spine;
define compactified mixed/wrapped and colored-tree flag stacks with
anchors; verify \(p^*,q_!,p_!\), flag base change, Thom-Sebastiani
coherence, quotient descent, finite-stabilizer characters, protected
integration character laws, and \(R'\to R\) transition compatibility.

Commands run by agent:
read-only `sed`, `nl -ba | sed -n`, and `rg`; no build, tests,
staging, or git mutation.
