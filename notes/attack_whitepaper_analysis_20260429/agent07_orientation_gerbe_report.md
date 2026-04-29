# Agent 07 Orientation Gerbe / Finite Wall Signs / E-Descent Report

Scope: Lemma 5.8/5.9-style issues, connected \(E\)-descent,
finite \(E[N]\)-stabilizer descent, ordinary and equivariant orientation
gerbes, residual vanishing/null-trivialization, Klein-four residual
criteria, type-II Pfaffian wall charts, \(N_\delta^{\mathrm{Pf}}=1\),
and the conditional status of the orientation character.

Status: the old fatal \(BE\)-cohomology attack is healed in current
`main.tex`. The stable core is the separation
\[
BE \quad\hbox{versus}\quad BE[N],
\]
the degree-two gerbe versus degree-one linearization distinction, and the
conditional O1/O1+/O2 package for type-II wall signs. The live residual is
not a wrong cohomology formula. It is construction: the paper does not yet
construct the orientation-gerbe-twisted Hall source as an object, and it
does not compute the finite stabilizer residuals or the type-II local
Pfaffian charts.

## Fatal / Stale Attacks

1. **Old fatal, now healed: connected \(BE\)-cohomology.**
The attack at
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:4958-5076`
and `:6101-6168` was valid against the older Lemma 5.8: it used the
cohomology of \(B(\mathbb Z/2)^2\) for connected \(BE\). Current
`main.tex:3197-3393` fixes this:
\[
E^{\mathrm{top}}\simeq T^2,\quad
BE\simeq BT^2,\quad
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2.
\]
Therefore \(H^1(BE;\mathbb F_2)=0\) and
\[
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
\]
This attack is stale unless a later edit reintroduces
\(\langle\alpha^2,\alpha\beta,\beta^2\rangle\) as connected \(BE\).

2. **Old fatal, now healed as a conditional criterion: small-orbit
gerbe vanishing.**
The attack at
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:5078-5129`
and `:6169-6213` was valid: translation-invariance of the ordinary line
does not trivialize the equivariant orientation gerbe. Current
`main.tex:3395-3814` replaces vanishing by the Klein-four criterion and
the rank-one obstruction target. It explicitly says the manuscript
computes neither the degree-two vector \(r_i\) nor the degree-one vector
\(\rho_i\): `main.tex:3777-3784`.

3. **Old fatal, now healed: OP minus sign as orientation.**
The attack at
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:5131-5186`
and `:6235-6245` is stale in current text. `main.tex:1666-1671`,
`main.tex:13924-13955`, and `main.tex:14168-14179` correctly state that
the OP scalar minus sign is not a Hall reflection character and does not
determine \(\epsilon_o\).

4. **Stale if read as current claim: automorphic divisor order implies
Hall Pfaffian sign.**
Current `main.tex:1800-1885` and `main.tex:1887-2021` separate
\[
d_\delta^{\mathrm{aut}}=\operatorname{ord}_{\mathcal H_\delta}(\Delta_5)
\]
from \(N_\delta^{\mathrm{Pf}}\). The automorphic order is a target check;
the Hall sign is conditional on the supplied O2 local model.

5. **Stale if read as current claim: three local signs give a character
without Weyl transport.**
Current `main.tex:1316-1404`, `main.tex:2101-2184`, and
`main.tex:2186-2251` require the projective determinant-line cocycle
and quotient torsor defects to vanish before the three generator signs
extend to a Hall orientation character.

6. **Live residual: orientation-gerbe construction.**
The later attack/rebuild material at
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:19053-19347`,
`:20030-20218`, and `:23258-23433` forces the next upgrade:
construct the square-root gerbe and the twisted Hall source, rather than
assuming a global orientation. Current `main.tex` has the conditional
orientation-line and obstruction package, but no explicit
`Or_{R,c}`, tautological square-root line, anti-invariant twisted state
space, or orientation-gerbe correspondence construction. This is not a
contradiction while the paper stays certificate-form. It is fatal only if
the paper claims to have constructed the compact source.

## Forced Replacements

1. **Replace Lemma 5.8 by two statements.**

Connected free \(E\)-descent:
\[
E_2^{p,q}=H^p(BE;H^q(\mathfrak M_{\mathcal C}^{\mathrm{red}};\mathbb F_2)),
\qquad H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\ |u_i|=2.
\]
There is no \(E_2^{1,1}\) term from \(H^1(BE)\). The connected
equivariant obstruction is in total degree two, through
\[
E_2^{2,0}=H^2(BE;\mathbb F_2)\otimes H^0(\mathfrak M_{\mathcal C}^{\mathrm{red}};\mathbb F_2),
\]
and
\[
E_2^{0,2}=H^0(BE;H^2(\mathfrak M_{\mathcal C}^{\mathrm{red}};\mathbb F_2)).
\]

Finite stabilizer \(E[N]\)-descent:
small-orbit strata have stabilizer \(E[N]\simeq(\mathbb Z/N)^2\). The
finite class is first a Borel class
\[
\widetilde\beta^{E,N}_{\mathcal C,S}\in H^2_{E[N]}(S;\mathbb F_2),
\]
not automatically a point-stabilizer class. It restricts to
\[
\beta^{E,N}_{\mathcal C,S}\in H^2(BE[N];\mathbb F_2)
\]
only after mixed Borel terms, stabilizer action on
\(H^\bullet(S;\mathbb F_2)\), and spectral-sequence differentials have
vanished.

2. **Replace Lemma 5.9 by a criterion, not a vanishing theorem.**
Corrected form: for \(E[2]\), the degree-two gerbe class vanishes iff
the three cyclic degree-two residuals vanish:
\[
(r_1,r_2,r_3)=(0,0,0).
\]
After that null-trivialization, trivial finite linearization is a separate
degree-one condition:
\[
(\rho_1,\rho_2,\rho_3)=(0,0,0).
\]
The attack transcript's compressed phrase "trivial character iff gerbe
vanishes" must not be propagated. The current text is sharper: \(r_i\)
and \(\rho_i\) live in different cohomological degrees.

3. **Replace global-orientation assumption by orientation gerbe when
claiming construction.**
For each finite d-critical stack \(\mathfrak M_{R,c}\), define the
\(\mu_2\)-gerbe of square roots of the determinant/canonical line:
\[
\operatorname{Or}_{R,c}=\sqrt{K_{R,c}},\qquad
(L,\phi),\quad \phi:L^{\otimes2}\xrightarrow{\sim}K_{R,c}|_U.
\]
It has tautological line \(L_{R,c}^{1/2}\) over \(\operatorname{Or}_{R,c}\).
The twisted state space should be defined over the quotient stack
\([\operatorname{Or}_{R,c}/E]\), in the \(\mu_2\)-anti-invariant summand.
A global orientation is then a section/trivialization of the gerbe, not a
prerequisite for the twisted source.

4. **Replace Pfaffian sign proof by local O2 chart criterion.**
For each simple type-II wall, O2 must supply a wall point, an
\(s_\delta\)-equivariant real analytic chart, an anti-invariant local
equation \(u_\delta\), a tangent/normal splitting, an invariant Pfaffian
unit, and a rank-one odd normal crossing:
\[
K_\delta^{\mathrm{nor}}\simeq
[\mathbb R\xrightarrow{u_\delta}\mathbb R],
\qquad
N_\delta^{\mathrm{Pf}}=1.
\]
Only then
\[
s_\delta^*\operatorname{Pf}(K_\delta^{\mathrm{nor}})
=-\operatorname{Pf}(K_\delta^{\mathrm{nor}}).
\]

5. **Replace automorphic sign extension by O1+ plus group theory.**
The type-II Coxeter group has presentation
\[
W^{(2)}(\Lambda^{2,1}_{II})
\simeq C_2*C_2*C_2,
\]
so its abelianization is \((\mathbb Z/2)^3\). This group-theoretic fact
extends three signs only after O1+ supplies an honest determinant-line
action on the reduced quotient orientation.

## Exact Cohomology Assertions

Connected torus:
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,
\]
\[
H^1(BE;\mathbb F_2)=0,\qquad
H^2(BE;\mathbb F_2)=\mathbb F_2u_1\oplus\mathbb F_2u_2.
\]

Finite stabilizer:
\[
E[N]\simeq(\mathbb Z/N)^2.
\]
If \(N\) is odd,
\[
H^{>0}(BE[N];\mathbb F_2)=0.
\]

For \(N=2\):
\[
E[2]\simeq(\mathbb Z/2)^2,\qquad
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\quad |x_i|=1,
\]
\[
H^2(BE[2];\mathbb F_2)
=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
\]
Write
\[
\beta^{E,E[2]}_{\mathcal C}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2.
\]
For \(e_3=e_1+e_2\),
\[
r_1=b_{20},\qquad r_2=b_{02},\qquad
r_3=b_{20}+b_{11}+b_{02},
\]
hence
\[
b_{20}=r_1,\qquad b_{02}=r_2,\qquad
b_{11}=r_1+r_2+r_3.
\]
Thus
\[
\beta^{E,E[2]}_{\mathcal C}=0
\Longleftrightarrow
r_1=r_2=r_3=0.
\]
After this degree-two class has been null-trivialized,
\[
H^1(BE[2];\mathbb F_2)=\mathbb F_2\langle x_1,x_2\rangle,
\]
\[
\lambda_{\mathcal C}^{E[2]}=\lambda_1x_1+\lambda_2x_2,
\]
and the cyclic restrictions are
\[
\rho_1=\lambda_1,\qquad
\rho_2=\lambda_2,\qquad
\rho_3=\lambda_1+\lambda_2.
\]
Trivial finite \(E[2]\)-linearization is equivalent to
\[
\rho_1=\rho_2=\rho_3=0.
\]

For even \(N\ge4\), with \(2^a\parallel N\):
\[
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2],
\]
\[
|x_i|=1,\quad |y_i|=2,\quad x_i^2=0,
\]
\[
H^2(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\mathbb F_2\langle y_1,x_1x_2,y_2\rangle.
\]
Write
\[
\beta^{E,N}_{\mathcal C,(2)}
=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
\]
The coefficient \(A_{12}^{(N)}\) is invisible to cyclic restrictions and
is a genuine rank-two two-primary residual. After the degree-two class
vanishes, the residual linearisations form
\[
H^1(B(\mathbb Z/2^a)^2;\mathbb F_2)=\mathbb F_2\langle x_1,x_2\rangle,
\]
and must vanish on the two-primary generators \(g_1,g_2\), not merely on
the order-two elements \(h_i=2^{a-1}g_i\).

## Current `main.tex` Anchors

- Orientation line is defined only as an unresolved reduced compact
sector datum: `main.tex:2472-2507`.
- Open orientation monodromy problem separates Pin\(^c\), connected
\(BE\), finite stabilizers, and residual characters:
`main.tex:2914-3195`.
- Correct connected/free and finite \(E[N]\)-descent lemma:
`main.tex:3197-3393`.
- Klein-four criterion and rank-one obstruction target:
`main.tex:3395-3814`.
- Higher even finite-stabilizer residuals:
`main.tex:3816-3928`.
- Finite-stabilizer obstruction to O1:
`main.tex:3930-4019`.
- Finite-stage quotient-orientation character system:
`main.tex:4021-4128`.
- O1 inside the Dirac-Pfaffian theorem contains the correct full quotient
package: `main.tex:1177-1313`.
- O1+ contains the projective cocycle \(c_o\), quotient torsor defects
\(\omega_{i,\mathcal C}\), and finite-stage action groupoid:
`main.tex:1316-1404`, `main.tex:2101-2251`.
- O2 is conditional on local Pfaffian wall normal forms and
\(N_{\delta_i}^{\mathrm{Pf}}=1\): `main.tex:1407-1476`,
`main.tex:920-1052`, `main.tex:1054-1137`.
- Conditional Dirac-Pfaffian theorem uses O1/O1+/O2 as hypotheses:
`main.tex:1139-1798`.
- Local simple-wall sign lemma is conditional:
`main.tex:1800-1885`.
- Maass/automorphic target check is separate:
`main.tex:1887-2021`.
- Group-theoretic sign extension after O1+:
`main.tex:2045-2099`.
- Semidirect \(S_3\) wall-transport obstruction:
`main.tex:2253-2314`.
- Constants are not orientation data:
`main.tex:13924-13955`, `main.tex:14168-14179`.
- Orientation sources in the bibliography:
`proj.bib:556-585`, `proj.bib:617-635`, `proj.bib:512-543`,
`proj.bib:587-605`.

## Residual Calculations

1. **Ordinary reduced gerbe.**
\[
\alpha^{\mathrm{red}}_{\mathcal C}
=w_2(\det\operatorname{RHom}_{\mathrm{red}}(\mathcal C,\mathcal C))
+\mathrm{cs}^*w_2(\det(\operatorname{coker}\mathrm{cs})).
\]
This must vanish on every object, extension, and flag stratum used by
the Hall correspondences.

2. **Connected \(E\)-descent.**
\[
\alpha^{E,\mathrm{free}}_{\mathcal C}=a_1(\mathcal C)u_1+a_2(\mathcal C)u_2.
\]
Both coefficients must vanish. There is no \(H^1(BE)\) character term.

3. **Finite Borel descent.**
For every finite-stabilizer stratum \(S\), the actual class is
\[
\widetilde\beta^{E,N}_{\mathcal C,S}\in H^2_{E[N]}(S;\mathbb F_2).
\]
The point-stabilizer class \(\beta^{E,N}_{\mathcal C,S}\) is valid only
after the mixed Borel terms, stabilizer action on stratum cohomology, and
differentials have vanished.

4. **\(N=2\) residual tuple.**
\[
\mathfrak o^{E[2]}_{\mathcal C}
=(r_1,r_2,r_3;\rho_1,\rho_2,\rho_3).
\]
The first three entries null-trivialize the degree-two gerbe. The last
three select the trivial degree-one \(E[2]\)-linearization.

5. **Even \(N\ge4\) residual tuple.**
\[
\mathfrak o^{E[N]}_{\mathcal C}
=(A_1^{(N)},A_{12}^{(N)},A_2^{(N)};
\lambda_1^{(N)},\lambda_2^{(N)}).
\]
The \(E[2]\) calculation does not detect \(A_{12}^{(N)}\) and does not
prove the \(H^1\)-linearization.

6. **Weyl transport residuals.**
O1+ requires
\[
[c_o]=0
\]
in the retained action-groupoid cohomology, a killing cochain normalized
by \(\widetilde\tau_i^2=1\), and
\[
\omega_{i,\mathcal C}=0\in
H^1(\mathfrak M^{\mathrm{red}}_{s_{\delta_i}\mathcal C};\mathbb F_2)
\oplus\bigoplus_{N\ge2}H^1(BE[N];\mathbb F_2).
\]
The Maass character does not kill \(c_o\) or \(\omega\).

7. **O2 local wall residuals.**
At finite height \(R\), for each simple wall:
\[
\mathfrak O^{\mathrm{O2}}_{\delta_i,R}
=(
\mathfrak o^{\mathrm{chart}},
\mathfrak o^{\mathrm{wall}},
\mathfrak o^{\mathrm{split}},
\mathfrak o^{\mathrm{unit}},
\mathfrak o^{\mathrm{rank}},
\mathfrak o^{\mathrm{tr}}
).
\]
These mean: chart existence, wall anti-invariance, tangent/normal
splitting, invariant Pfaffian unit, rank-one normal crossing, and
transition compatibility. The global atlas also needs component,
boundary, and overlap compatibility, plus the hybrid wrapped wall object
for the middle wall \(\delta_2\leftrightarrow(0,1,1)\).

8. **Orientation-gerbe twisted source.**
Not yet present as a construction in `main.tex`. The residual is to build
twisted states over \([\operatorname{Or}_{R,c}/E]\), keep finite
stabilizers as inertia data, define product/coproduct/primitives over the
gerbe, and then state global orientation as a trivialization problem.

## Rewrite Actions

1. Preserve the current \(BE\) and \(BE[N]\) split. Do not compress it
back into a single "equivariant descent lemma."

2. Keep the \(N=2\) theorem as a Klein-four criterion. Do not call it a
vanishing theorem until \(r_i=0\) and \(\rho_i=0\) have been computed for
the actual reduced determinant line.

3. Add a short example: an ordinary line fixed by a finite group may carry
a nontrivial equivariant character. This would make the \(r_i/\rho_i\)
distinction readable without weakening the theorem.

4. If the paper claims source construction rather than certificate,
insert the orientation-gerbe-twisted Hall object:
\[
\operatorname{Or}_{R,c},\quad L^{1/2}_{R,c},\quad
H^{\mathrm{tw}}_{R,c}
=H_*^{BM}([\operatorname{Or}_{R,c}/E],
\pi^*\Phi_{R,c}\otimes L^{1/2}_{R,c})_{\mathrm{anti}}.
\]
Then define product, coproduct, primitives, and normal-ordered pushforward
over this gerbe.

5. Move the full O1/O1+/O2 obstruction algebra to an appendix if the main
text becomes unreadable. The main text must still retain the exact
degree-two/degree-one split, higher even \(N\) residual, \(c_o\), \(\omega\),
and O2 chart hypotheses.

6. Number the Joyce--Tanaka--Upmeier finite-band/orbifold hypothesis if it
is used for the Klein-four inertia stack. Mark exactly which statements
depend on it.

7. Keep the local Pfaffian wall charts independent of the automorphic
divisor. Required local data: chart, \(s_\delta(u_\delta)=-u_\delta\),
tangent/normal splitting, invariant unit, \(N_\delta^{\mathrm{Pf}}=1\),
and component/boundary/overlap compatibility.

8. Keep Hall signs on the three chamber-permuting \(S_3\) reflections out
of the manuscript unless a semidirect-product Hall lift is supplied. The
\(+1\) Maass values are automorphic target data only.

9. Preserve the sentence-level firewall: \(64\), \(4096\), and the OP
minus sign are scalar normalization data. They do not construct
\(\epsilon_o\), kill \(c_o\), trivialize finite \(H^1(BE[N])\), or prove
\(N_\delta^{\mathrm{Pf}}=1\).

No edit to `main.tex` was made by this agent.
