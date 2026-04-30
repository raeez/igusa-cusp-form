# A041 report: translation linearization versus underlying line invariance

Runtime id: `019ddbec-ae0f-7b32-8580-04f3c165a67f`.
Nickname: Kierkegaard.
Status: completed.
Files changed by agent: none.

## Claim Attacked

Whether an orientation, determinant, or anchor line is allowed to descend
to the reduced \(E\)-quotient merely because translations fix its
ordinary isomorphism class.

## Verdict

Mostly healed in the orientation formalism; still vulnerable in the
geometric atlas wording around determinant anchors. The manuscript says
fixedness is not descent: `main.tex:1303`, `main.tex:3434`,
`main.tex:3565`. But later phrases "fibre of the determinant anchor over
\(0_E\)" and "anchor imposed as a closed condition" still need to be
read only as supplied finite-stage data, not as construction-level
quotient descent: `main.tex:13212`, `main.tex:13703`.

## Failure Mode

For a stabilizer \(H\), \(g^*L\simeq L\) in \(\operatorname{Pic}\) does
not choose coherent isomorphisms \(\phi_g:L\to g^*L\), and after the
square-root gerbe is killed the choices form a character torsor. For
orientation signs this is
\[
\lambda^H\in H^1(BH;\mathbb F_2),
\]
and quotient orientation requires \(\lambda^H=0\), not only
\(g^*[L]=[L]\). The proof spine is correct at `main.tex:13482` and
`main.tex:13585`: the stabilizer action includes translation pullback,
trace/semiregularity reductions, anchors, framings, Thom-Sebastiani
maps, and flag coherences.

## Exact Computations Needed

\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,\quad
H^1(BE;\mathbb F_2)=0,
\]
so connected free descent requires
\[
\alpha^{E,\mathrm{free}}=a_1u_1+a_2u_2=0.
\]

For \(H=E[2]\),
\[
\beta=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,\quad
(b_{20},b_{11},b_{02})=(r_1,r_1+r_2+r_3,r_2),
\]
and after \(\beta=0\),
\[
\lambda=\lambda_1x_1+\lambda_2x_2,\quad
\rho_1=\lambda_1,\ \rho_2=\lambda_2,\ \rho_3=\lambda_1+\lambda_2.
\]
Need \(r_1=r_2=r_3=0\) and
\(\rho_1=\rho_2=\rho_3=0\).

For \(2^a\parallel N,\ a\ge2\),
\[
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
\]
\[
\beta=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2,\quad
\lambda=\lambda_1^{(N)}x_1+\lambda_2^{(N)}x_2.
\]
Need all five entries zero. The mixed \(A_{12}^{(N)}\) is invisible to
cyclic order-two tests. For odd \(N\), the mod-2 orientation obstruction
vanishes by transfer.

## Anchor-Line Addendum

The determinant anchor
\[
\lambda(A)=\det Rp_{E,*}A\otimes \mathcal O_E(-\chi(A)0_E)
\]
has translation law
\[
\lambda(t\cdot A)=\lambda(A)+\chi(A)t,
\]
not unit weight in general: `main.tex:7593`. For anchor descent, also
compute the actual stabilizer character on the chosen anchor
trivialization, in
\(\widehat H=\operatorname{Hom}(H,\mathbb C^\times)\), or define the
retained stabilizer as preserving that trivialization. The mod-2
orientation character does not by itself control odd-order anchor
characters.

## Claim-Status Recommendation

Keep all quotient-orientation and anchor descent statements
conditional/open. Replace any construction-sounding use of "determinant
anchor imposed as a closed condition" by an explicit finite-stage
anchor-transport and stabilizer-character package.

## Residual Obligations

Compute \(\alpha^{\mathrm{red}}\), \(\alpha^{E,\mathrm{free}}\),
\(\widetilde\beta^H\), \(\lambda^H\), and the anchor-trivialization
character on every retained object, extension, mixed, wrapped, and flag
stratum; prove compatibility under Thom-Sebastiani, flags, \(Q_{E,R}\),
and HN transitions.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, and `git status --short`; no
build or tests.
