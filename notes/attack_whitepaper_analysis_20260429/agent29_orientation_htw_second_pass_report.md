# Agent 29 Second-Pass Report: Orientation Gerbe and \(H^{\mathrm{tw}}_{X,\Gamma}\)

Scope: second-pass orientation-gerbe audit. Inputs mined: current
`main.tex`, `materials/raw/2026-04-29-attack-whitepaper-analysis.pdf`
through the extracted transcript
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt`,
and reports `agent04`, `agent05`, `agent06`, `agent07`, `agent10`,
`agent16`, and `agent22`.

Verdict: the current manuscript has mostly healed the old scalar-sign,
Maass-character, \(BE\)/\(BE[N]\), and local-Pfaffian overclaims. The
remaining architectural fault is earlier. The compact side still begins
too often from an oriented object or an orientation certificate. The next
rewrite must put the square-root gerbe first and define
\(H^{\mathrm{tw}}_{X,\Gamma}\) over that gerbe before any global
orientation is asserted. Global orientation is a section/trivialization of
the gerbe. It is not a prerequisite for twisted Pfaffian states.

## Gerbe-first construction hierarchy

The correct hierarchy is not
\[
\text{global orientation} \Rightarrow \text{Hall source}.
\]
It is
\[
H^{\mathrm{pre}}_{X,\Gamma}
\Rightarrow \operatorname{Or}_{R,\hat c}
\Rightarrow H^{\mathrm{tw}}_{X,\Gamma}
\Rightarrow H^{\mathrm{or}}_{X,\Gamma}\ \text{only after O1}
\Rightarrow \epsilon_o\ \text{only after O1+ and O2}.
\]

Concrete hierarchy:

1. **Pre-integrated normal-ordered source.** Define
   \(H^{\mathrm{pre}}_{X,\Gamma}\) from derived compact-object stacks
   \(\mathfrak M_{R,\hat c}\), exact-triangle stacks
   \(\mathfrak E_{R,\hat c,\hat c'}\), and two-step flag stacks. The target
   of an extension is \(\hat c\star\hat c'\), not a raw Gram degree. This is
   pre-orientation, pre-integration, and pre-primitive.

2. **Square-root gerbe.** For each finite stage \(R\) and normal-ordered
   charge \(\hat c\), define the determinant/canonical line
   \(K_{R,\hat c}\) of the reduced d-critical or shifted-symplectic stack.
   Then define the \(\mu_2\)-gerbe
   \[
   \operatorname{Or}_{R,\hat c}:=\sqrt{K_{R,\hat c}},
   \]
   whose objects over \(U\to\mathfrak M_{R,\hat c}\) are pairs
   \[
   (L,\phi),\qquad \phi:L^{\otimes2}\xrightarrow{\sim}K_{R,\hat c}|_U.
   \]
   This gerbe exists as a stack even when it has no global section. Attack
   transcript anchors: `materials/processed/2026-04-29-attack-whitepaper-analysis.txt:19068`,
   `:19095`, `:19166`, `:23274`, `:23298`, `:23345`.

3. **Tautological square-root line.** Over
   \(\pi_{R,\hat c}:\operatorname{Or}_{R,\hat c}\to\mathfrak M_{R,\hat c}\)
   there is a tautological line \(L^{1/2}_{R,\hat c}\) with
   \[
   (L^{1/2}_{R,\hat c})^{\otimes2}\cong \pi_{R,\hat c}^{*}K_{R,\hat c}.
   \]
   This is the Pfaffian coefficient line for twisted states. It is not a
   chosen global orientation.

4. **Orientation-gerbe lifted correspondences.** Lift exact-triangle and
   flag correspondences to the gerbes:
   \[
   \operatorname{Or}_{R,\hat c}\times \operatorname{Or}_{R,\hat c'}
   \xleftarrow{\ p^{\mathrm{or}}\ }
   \mathfrak E^{\mathrm{or}}_{R,\hat c,\hat c'}
   \xrightarrow{\ q^{\mathrm{or}}\ }
   \operatorname{Or}_{R,\hat c\star\hat c'}.
   \]
   Joyce-Upmeier multiplicativity is then a morphism of gerbes or a
   recorded \(\mu_2\)-twist. If the multiplicativity class is nontrivial,
   the theory remains a twisted correspondence object, not an oriented one.

5. **Twisted protected Hall object.** Define \(H^{\mathrm{tw}}\) on the
   quotient stack \([\operatorname{Or}_{R,\hat c}/E]\), retaining inertia and
   finite stabilizers. The \(\mu_2\)-anti-invariant summand is the Pfaffian
   sector. This is the first protected state object that can be defined
   without pretending O1 has been solved. Agent 16 gives this as the missing
   named object (`agent16_source_objects_hpre_htw_report.md:101-116`,
   `:341-345`). Agent 07 makes the same replacement (`agent07_orientation_gerbe_report.md:140-148`,
   `:392-413`).

6. **Untwisted oriented Hall object.** An ordinary oriented Hall object
   \(H^{\mathrm{or}}\) exists only after a section/trivialization of the
   gerbe, plus quotient descent and multiplicativity. This is O1. It is not
   the starting object.

7. **Orientation character.** A Hall orientation character
   \(\epsilon_o\) exists only after O1+ supplies coherent Weyl transport and
   O2 supplies local type-II Pfaffian wall charts. The Maass character is the
   automorphic target, not the Hall construction.

## What can be stated without global orientation

The following are safe without a global orientation section:

- The square-root gerbe \(\operatorname{Or}_{R,\hat c}\) and its
  tautological line \(L^{1/2}_{R,\hat c}\) exist as gerbe data once
  \(K_{R,\hat c}\) is defined.

- The twisted coefficient system
  \[
  \pi_{R,\hat c}^{*}\Phi_{R,\hat c}\otimes L^{1/2}_{R,\hat c}
  \]
  can be named over \(\operatorname{Or}_{R,\hat c}\), with \(\Phi\) the
  BBDJS/vanishing-cycle coefficient complex, if the finite d-critical
  stack and coefficient formalism are supplied.

- The \(\mu_2\)-anti-invariant Borel-Moore or compact-support group
  \[
  H^{\mathrm{tw}}_{R,\hat c}
  =
  H_*^{\mathrm{BM}}\!\left(
  [\operatorname{Or}_{R,\hat c}/E],
  \pi^*\Phi_{R,\hat c}\otimes L^{1/2}_{R,\hat c}
  \right)_{\mathrm{anti}}
  \]
  is the correct candidate state space. The anti-invariant summand is where
  the band acts by the sign character. This is not a scalar sign convention.

- Pull-TS-push product and reverse pull-push coproduct can be stated over
  lifted gerbe correspondences:
  \[
  m_R=q^{\mathrm{or}}_!\circ \operatorname{TS}^{\mathrm{or}}\circ
  (p^{\mathrm{or}})^*,
  \qquad
  \Delta_R=p^{\mathrm{or}}_!\circ(\operatorname{TS}^{\mathrm{or}})^{-1}
  \circ(q^{\mathrm{or}})^*,
  \]
  provided the six-functor and Thom-Sebastiani data are supplied. If the
  gerbe-multiplicativity residual is nonzero, this product is twisted. Do
  not silently identify it with an ordinary oriented product.

- Primitive extraction is formal once the coproduct exists:
  \[
  P_R^{\mathrm{tw}}
  =
  \ker(\Delta_R-\mathrm{id}\otimes1-1\otimes\mathrm{id})
  \cap\ker(\epsilon_R).
  \]
  Normal-ordered pushforward can then be named:
  \[
  P_R^{\Pi,\mathrm{tw}}
  =
  \overline\Pi_{R,*}^{\Theta_R}P_R^{\mathrm{tw}}.
  \]
  This still does not identify the result with \(\mathfrak g_{\Delta_5}\).

- Finite stabilizers \(E[N]\) remain visible as inertia in
  \([\operatorname{Or}_{R,\hat c}/E]\). Their degree-two Borel classes and
  degree-one linearization characters are data to compute, not assumptions
  erased by quotient notation.

Safe statement template:

> A compact source would first produce \(H^{\mathrm{pre}}_{X,\Gamma}\).
> Lifting its finite correspondences to the square-root gerbes defines the
> orientation-gerbe-twisted protected object \(H^{\mathrm{tw}}_{X,\Gamma}\).
> A global orientation is a section/trivialization of these gerbes and is
> needed only to descend to an ordinary untwisted Pfaffian theory.

## What requires O1/O1+/O2

O1, O1+, and O2 are not construction of \(H^{\mathrm{tw}}\). They are the
extra package needed to turn twisted gerbe states into an ordinary oriented
Hall theory with a Weyl reflection character.

**O1. Strong reduced quotient orientation.** O1 requires:

- ordinary reduced square-root gerbe vanishing
  \[
  \alpha^{\mathrm{red}}_{\mathcal C}=0;
  \]
- connected \(E\)-descent class vanishing
  \[
  \alpha^{E,\mathrm{free}}_{\mathcal C}
  =a_1(\mathcal C)u_1+a_2(\mathcal C)u_2=0
  \in H^2(BE;\mathbb F_2);
  \]
- finite Borel gerbe classes
  \[
  \widetilde\beta^{E,N}_{\mathcal C,S}\in H^2_{E[N]}(S;\mathbb F_2)
  \]
  vanish, not merely their point-stabilizer shadows;
- after those degree-two classes are null-trivialized, the residual finite
  characters
  \[
  \lambda^{E,N}_{\mathcal C}\in H^1(BE[N];\mathbb F_2)
  \]
  are chosen to be zero;
- extension, flag, Thom-Sebastiani, and HN-transition orientation
  coherences are trivialized.

The \(BE\) and \(BE[N]\) split must stay rigid:
\[
H^*(BE;\mathbb F_2)=\mathbb F_2[u_1,u_2],\quad |u_i|=2,\quad
H^1(BE;\mathbb F_2)=0.
\]
For \(E[2]\), the degree-two bits \(r_i\) and degree-one bits \(\rho_i\)
are different:
\[
(r_1,r_2,r_3)=0
\quad\text{does not imply}\quad
(\rho_1,\rho_2,\rho_3)=0.
\]
For even \(N\ge4\), the mixed coefficient \(A_{12}^{(N)}x_1x_2\) and the
degree-one characters \(\lambda_i^{(N)}\) are not detected by the \(E[2]\)
test.

**O1+. Weyl-equivariant determinant-line transport.** O1+ requires an
honest Weyl action on the quotient orientation package, not just on a line:
\[
[c_o]=0,\qquad \tau_i^2=1,\qquad \omega_{i,\mathcal C}=0.
\]
The transport must preserve
\[
(\alpha^{\mathrm{red}},\alpha^{E,\mathrm{free}},
\{(\beta^{E,N},\lambda^{E,N}=0)\}_{N\ge2})
\]
and their null-trivializations. The Maass character does not kill
\([c_o]\). Automorphic monodromy does not kill \(\omega_{i,\mathcal C}\).

**O2. Local type-II Pfaffian wall charts.** O2 requires, for each simple
type-II wall, a local chart with:
\[
s_\delta(u_\delta)=-u_\delta,
\]
a tangent/normal splitting,
\[
K^{\mathrm{red}}_\delta\simeq K^{\mathrm{tan}}_\delta\oplus
K^{\mathrm{nor}}_\delta,
\]
an invariant Pfaffian unit \(\upsilon_\delta\), and a normal rank
\[
K^{\mathrm{nor}}_\delta\simeq
\bigoplus_{j=1}^{N_\delta^{\mathrm{Pf}}}
[\mathbb R\xrightarrow{u_\delta}\mathbb R].
\]
Only after O1 and O1+ have made the quotient orientation and Weyl lift
honest does the local formula become a Hall orientation sign:
\[
\epsilon_o(s_\delta)=(-1)^{N_\delta^{\mathrm{Pf}}}.
\]
For the desired type-II simple walls, O2 must compute
\[
N_{\delta_1}^{\mathrm{Pf}}=N_{\delta_2}^{\mathrm{Pf}}
=N_{\delta_3}^{\mathrm{Pf}}=1.
\]
The automorphic divisor order \(d_\delta^{\mathrm{aut}}=1\) is a target
check, not this computation.

**Semidirect \(S_3\).** The Maass values on the chamber-permuting
\(S_3\)-reflections are \(+1\), but no Hall signs exist there unless a
semidirect-product Hall action and orientation lift are separately supplied.
Current `main.tex:1517-1522` and `main.tex:2253-2317` correctly enforce
this.

## Exact \(H^{\mathrm{tw}}\) candidate definition

Finite-stage candidate:

Let \(R\) be a finite HN height and let
\(\hat c\in\widehat\Gamma_{X,R}\). Assume:

- \(\mathfrak M_{R,\hat c}\) is a finite-type reduced d-critical Artin
  stack with finite residual inertia after the prescribed rigidifications;
- \(\Phi_{R,\hat c}\) is the BBDJS/vanishing-cycle coefficient complex;
- \(K_{R,\hat c}\) is the reduced virtual canonical/determinant line;
- the \(E\)-translation action lifts to the finite stack and to the gerbe.

Define the square-root gerbe
\[
\operatorname{Or}_{R,\hat c}
=\sqrt{K_{R,\hat c}}
\xrightarrow{\ \pi_{R,\hat c}\ }
\mathfrak M_{R,\hat c},
\]
with tautological line \(L^{1/2}_{R,\hat c}\). Define
\[
\Phi^{\mathrm{or}}_{R,\hat c}:=\pi_{R,\hat c}^{*}\Phi_{R,\hat c}.
\]
Then set
\[
H^{\mathrm{tw}}_{R,\hat c}
:=
H_*^{\mathrm{BM}}\!\left(
[\operatorname{Or}_{R,\hat c}/E],
\Phi^{\mathrm{or}}_{R,\hat c}\otimes L^{1/2}_{R,\hat c}
\right)_{\mu_2\text{-anti}}.
\]
The finite object is
\[
H^{\mathrm{tw}}_{R}:=
\bigoplus_{\hat c\in\widehat\Gamma_{X,R}}H^{\mathrm{tw}}_{R,\hat c}.
\]

For each extension correspondence
\[
\mathfrak M_{R,\hat c}\times\mathfrak M_{R,\hat c'}
\xleftarrow{\ p\ }
\mathfrak E_{R,\hat c,\hat c'}
\xrightarrow{\ q\ }
\mathfrak M_{R,\hat c\star\hat c'},
\]
define its gerbe lift
\[
[\operatorname{Or}_{R,\hat c}/E]\times
[\operatorname{Or}_{R,\hat c'}/E]
\xleftarrow{\ p^{\mathrm{or}}\ }
[\mathfrak E^{\mathrm{or}}_{R,\hat c,\hat c'}/E]
\xrightarrow{\ q^{\mathrm{or}}\ }
[\operatorname{Or}_{R,\hat c\star\hat c'}/E].
\]
The product and coproduct are
\[
m_R=q^{\mathrm{or}}_!\circ\operatorname{TS}^{\mathrm{or}}\circ
(p^{\mathrm{or}})^*,
\]
\[
\Delta_R=p^{\mathrm{or}}_!\circ(\operatorname{TS}^{\mathrm{or}})^{-1}
\circ(q^{\mathrm{or}})^*.
\]
Associativity/coassociativity require the gerbe-lifted two-step flag
coherences. No global orientation is used here.

Primitives:
\[
P^{\mathrm{tw}}_R
=\ker(\Delta_R-\mathrm{id}\otimes1-1\otimes\mathrm{id})
\cap\ker\epsilon_R.
\]
Normal-ordered primitive pushforward:
\[
P_R^{\Pi,\mathrm{tw}}
=\overline\Pi_{R,*}^{\Theta_R}P_R^{\mathrm{tw}}.
\]
Only after compatible transition maps and an ML/exactness condition may one
write
\[
H^{\mathrm{tw}}_{X,\Gamma}:=\varprojlim_R H^{\mathrm{tw}}_R,\qquad
P_X^{\Pi,\mathrm{tw}}:=\varprojlim_R P_R^{\Pi,\mathrm{tw}}.
\]

Recognition target, not definition:
\[
\overline\Pi_{X,*}H^0\operatorname{Prim}_{\mathrm{prot}}
(H^{\mathrm{tw}}_{X,\Gamma})/
\overline{\operatorname{Rad}}
\stackrel{?}{\cong}
\mathfrak g_{\Delta_5}.
\]
The question mark is load-bearing. This comparison is not part of the
definition of \(H^{\mathrm{tw}}\).

## False scalar/character inferences

These implications must be forbidden in the rewrite:

1. **Scalar OP square \(\Rightarrow\) Hall orientation.** False.
   \[
   Z^X_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}
   \not\Rightarrow
   \epsilon_o=\nu_{\Delta_5}.
   \]
   A scalar square kills every sign. Current safe anchors:
   `main.tex:100-115`, `main.tex:13724-13955`, `main.tex:14168-14179`.
   Agent 04 records the rule at `agent04_op_dt_scalar_report.md:59-75`.

2. **OP minus sign \(\Rightarrow\) Pfaffian wall sign.** False. The leading
   \(-1\) in
   \[
   Z^X_{\mathrm{OP}}=-(\chi_{10}^{\mathrm{OP}})^{-1}
   \]
   is the OP scalar convention. It is not \(\epsilon_o(s_\delta)\).
   Agent 05 flags this at `agent05_dirac_pfaffian_report.md:58-59`.

3. **Maass character \(\Rightarrow\) Hall orientation character.** False.
   Maass/Gritsenko-Nikulin compute the automorphic target character
   \(\nu_{\Delta_5}\). They do not construct a reduced quotient
   orientation, kill \(c_o\), kill \(\omega_{i,\mathcal C}\), or select zero
   finite-stabilizer characters. Current safe anchor: `main.tex:1887-2008`.

4. **Automorphic divisor order \(\Rightarrow N_\delta^{\mathrm{Pf}}\).**
   False. \(d_\delta^{\mathrm{aut}}=1\) is a divisor order of
   \(\Delta_5\). \(N_\delta^{\mathrm{Pf}}=1\) is a local reduced Hall
   normal-mode computation. The current manuscript correctly separates
   them at `main.tex:1800-1885` and `main.tex:1946-1973`.

5. **Ordinary fixed line \(\Rightarrow\) zero finite-stabilizer character.**
   False. After degree-two gerbe vanishing, linearisations form an
   \(H^1(BE[N];\mathbb F_2)\)-torsor. A fixed ordinary line can carry a
   nontrivial stabilizer character. Current anchors:
   `main.tex:3341-3348`, `main.tex:3731-3741`.

6. **\(E[2]\) check \(\Rightarrow\) all finite stabilizers.** False. The
   \(E[2]\) vector does not see the mixed coefficient
   \(A_{12}^{(N)}\) for even \(N\ge4\), and it does not prove the
   degree-one two-primary linearization. Current anchor:
   `main.tex:3816-3928`.

7. **O1/O1+/O2 \(\Rightarrow\) compact source \(D_X\).** False. O1/O1+/O2
   are orientation and local-sign hypotheses. They do not construct the
   compact Hall/factorization source, primitive representatives, PBW
   theorem, source coalgebra, or first-order operator. Agent 05 states this
   directly at `agent05_dirac_pfaffian_report.md:50-51`; Agent 16 states the
   missing \(H^{\mathrm{pre}}\)/\(H^{\mathrm{tw}}\) source at
   `agent16_source_objects_hpre_htw_report.md:14-20`.

8. **Orientation line exists \(\Rightarrow\) \(H^{\mathrm{tw}}\) constructed.**
   False. The gerbe, tautological line, lifted correspondences,
   anti-invariant state spaces, and pull-TS-push operations must be
   defined. Agent 16's forbidden shortcut is explicit at
   `agent16_source_objects_hpre_htw_report.md:404-405`.

## `main.tex` anchors

- `main.tex:94-98`: denominator algebra is target only; no compact Hall
  source, orientation, or BPS collision map.

- `main.tex:100-115`: Dirac square-root framing is correct and says the
  compact orientation system, Weyl transport, and type-II wall atlas are
  open.

- `main.tex:127-129`: \(4096\) and the OP minus sign do not fix character
  or monodromy.

- `main.tex:882-918`: Dirac/Pfaffian target is open. This should be a
  definition/open problem, not a proposition.

- `main.tex:921-1048`: local O2 certificate correctly separates local
  Pfaffian data from automorphic divisor order and scalar normalization.

- `main.tex:1054-1137`: finite local sign theorem computes only after O2
  residuals vanish; it constructs no charts or global character.

- `main.tex:1139-1539`: main conditional theorem is overloaded. O1/O1+/O2
  should be split from Pfaffian comparison, scalar square, local sign, and
  group-character extension.

- `main.tex:1177-1313`: O1 correctly includes ordinary square root,
  degree-two gerbes, finite Borel classes, and degree-one finite
  characters. This should become the trivialization/descent problem for the
  gerbe-first object, not the first definition of the source.

- `main.tex:1316-1404`: O1+ correctly names \(c_o\) and
  \(\omega_{i,\mathcal C}\). Keep this; move detailed algebra to an
  appendix or construction-target subsection.

- `main.tex:1407-1476`: O2 correctly requires local Pfaffian wall charts,
  \(s_\delta(u_\delta)=-u_\delta\), invariant unit, and rank-one normal
  model. Keep conditionality.

- `main.tex:1481-1495`: Pfaffian comparison requires
  \(\iota_{\mathrm{aut}}\). Without it the statement is only equality of
  normalized formal products at the cusp.

- `main.tex:1517-1522`: no Hall signs on the chamber-permuting \(S_3\)
  reflections without semidirect lift. Preserve.

- `main.tex:1632-1674`: orientation literature supplies technology and
  analogues; it does not prove the reduced \(K3\times E\) quotient
  orientation or type-II Weyl lift. Preserve.

- `main.tex:1729-1752`: scalar-square step is mostly safe, but the middle
  equality
  \[
  \det\operatorname{RHom}_{\mathrm{red}}(\mathcal C,\mathcal C)|_{\mathrm{tot}}
  =\Delta_5^2
  \]
  is too bare unless it is explicitly part of the supplied comparison. Safer:
  \[
  \iota_{\mathrm{aut}}^{\otimes2}
  (\operatorname{Pf}_{\mathrm{prot}}(\mathfrak D_X)^2)=\Delta_5^2.
  \]

- `main.tex:1800-2008`: local Pfaffian sign and Maass target check are
  separated. Preserve the separation.

- `main.tex:2045-2099`: the group-theoretic extension is pure group theory
  only after O1+ supplies an honest action.

- `main.tex:2101-2251`: Weyl quotient-orientation obstruction package
  names exactly the missing \(c_o\), \(\tau_i^2\), and \(\omega\) data.

- `main.tex:2253-2317`: semidirect \(S_3\) obstruction correctly blocks
  the \(+1\) Maass values from becoming Hall signs.

- `main.tex:2472-2507`: current orientation-line definition should be
  preceded by the square-root gerbe definition. As written, it starts with
  the global object O1 is supposed to prove.

- `main.tex:2817-2844`: protected Hall integration criterion is
  certificate-level and should consume \(H^{\mathrm{tw}}\), not an unnamed
  oriented \(\mathcal F_X\).

- `main.tex:2914-3195`: orientation monodromy open problem contains the
  right residuals. Reframe as O1/O1+/O2 after the gerbe-first definition.

- `main.tex:3197-3393`: connected \(BE\) and finite \(E[N]\) descent split
  is correct. Do not compress.

- `main.tex:3395-3814`: \(E[2]\) Klein-four criterion correctly separates
  degree-two \(r_i\) from degree-one \(\rho_i\).

- `main.tex:3816-4128`: higher even finite-stabilizer and finite-stage
  quotient orientation system are necessary residuals for O1.

- `main.tex:5287-5325`: Maass multiplier restriction is automorphic target
  data only.

- `main.tex:8540-8600`: multiplicative orientation criterion is restricted;
  it does not construct the full compact/wrapped orientation gerbe.

- `main.tex:10994-11174`: finite Hall source kernel currently uses
  oriented groups \(\mathcal H_R^{or}\). Add the twisted predecessor
  \(H_R^{\mathrm{tw}}\) before this oriented specialization.

- `main.tex:11750-12122`: Dirac-Igusa realization certificate should be
  rewritten around \(H^{\mathrm{pre}}\), \(H^{\mathrm{tw}}\), and then
  optional \(H^{or}\).

- `main.tex:13724-13955`: OP normalization and constants-not-orientation
  section is safe. Preserve and cross-reference from the orientation
  section.

- `main.tex:14168-14179`: synthesis correctly says compact Hall
  orientation must construct \(\epsilon_o\). Preserve.

## Patch queue

1. **Insert a gerbe-first definition before `main.tex:2472`.** Add
   `Definition. Square-root orientation gerbe and tautological Pfaffian
   line.` Define \(\operatorname{Or}_{R,\hat c}\), \(L^{1/2}_{R,\hat c}\),
   \(\mu_2\)-band, and global orientation as a section/trivialization.

2. **Demote/reframe `main.tex:2472-2507`.** Rename it to `Global
   orientation/trivialization of the protected sector`. Its object is not
   the first orientation object; it is the O1 solution of the gerbe problem.

3. **Add \(H^{\mathrm{tw}}_{R,\hat c}\) immediately after the gerbe
   definition.** Use the formula in this report. Include the
   \(\mu_2\)-anti-invariant summand and the quotient stack
   \([\operatorname{Or}_{R,\hat c}/E]\).

4. **Add lifted correspondence product/coproduct.** Define
   \(\mathfrak E^{\mathrm{or}}_{R,\hat c,\hat c'}\), gerbe Thom-Sebastiani,
   product, coproduct, primitives, and normal-ordered pushforward. Mark
   associativity as conditional on gerbe-lifted flag coherences.

5. **Split Theorem `main.tex:1139-1539`.** Replace the all-in-one theorem
   by:
   `Definition: compact Dirac-Igusa datum`;
   `Proposition: Pfaffian comparison after \(\iota_{\mathrm{aut}}\)`;
   `Theorem: OP scalar square is orientation-forgetting`;
   `Lemma: local Pfaffian sign after O1/O1+/O2`;
   `Lemma: group-theoretic character extension after O1+`.

6. **Move O1/O1+/O2 algebra out of the main theorem body.** Keep a short
   main-text statement with the residual names
   \[
   \alpha^{\mathrm{red}},\alpha^{E,\mathrm{free}},
   \beta^{E,N},\lambda^{E,N},c_o,\omega_{i,\mathcal C},
   N_\delta^{\mathrm{Pf}}.
   \]
   Put the full \(BE\)/\(E[N]\), \(c_o\), \(\omega\), and O2 wall chart
   algebra in an appendix.

7. **Tighten `main.tex:1729-1737`.** Remove the bare determinant equality
   to \(\Delta_5^2\) unless it is made an explicit supplied comparison
   hypothesis. Keep only the squared \(\iota_{\mathrm{aut}}\)-image.

8. **Add a false-implication box after the opening claim-status table.**
   Include:
   \[
   \Delta_5^2\not\Rightarrow\epsilon_o,\quad
   -4096\not\Rightarrow\text{Hall sign},\quad
   \nu_{\Delta_5}\not\Rightarrow c_o=0,\quad
   d_\delta^{\mathrm{aut}}\not\Rightarrow N_\delta^{\mathrm{Pf}}.
   \]

9. **Rewrite the finite Hall source kernel around \(H^{\mathrm{tw}}\).**
   At `main.tex:10994-11174`, define the gerbe-twisted finite state object
   first. Then say an O1 trivialization identifies it with the ordinary
   oriented \(\mathcal H_R^{or}\).

10. **Rewrite `O_X` in the Dirac-Igusa certificate.** At
    `main.tex:11861-11987`, replace "oriented compact Hall object" as the
    primary entry with "orientation-gerbe-twisted compact Hall object plus
    optional O1 trivialization." Keep O1/O1+/O2 as additional data, not the
    source itself.

11. **Preserve the \(S_3\) firewall.** Do not move the \(+1\) Maass values
    into a Hall orientation statement unless a semidirect-product Hall lift
    is added with its own \(c_o^G\) and \(\omega_g\) checks.

12. **Add one elementary finite-stabilizer warning example.** A one
    dimensional line fixed as an ordinary line can carry the nontrivial
    sign character of \(\mathbb Z/2\). This makes the
    degree-two/degree-one split readable and blocks the common \(r_i=\rho_i\)
    collapse.

## Residual orientation proof obligations

1. **Finite stacks.** Construct the finite-type d-critical or
   shifted-symplectic stacks \(\mathfrak M_{R,\hat c}\), extension stacks,
   and two-step flag stacks with finite residual inertia. A residual
   \(B\mathbb G_m\) destroys finite-dimensional protected cohomology.

2. **Determinant line.** Define \(K_{R,\hat c}\) as the reduced virtual
   canonical/determinant line, including cosection reduction and the
   parity shift. Verify compatibility on object, extension, and flag strata.

3. **Gerbe construction.** Construct \(\operatorname{Or}_{R,\hat c}\), its
   \(\mu_2\)-band, tautological \(L^{1/2}_{R,\hat c}\), and the lift of the
   \(E\)-action to the gerbe.

4. **Gerbe-lifted correspondences.** Lift exact-triangle and flag
   correspondences to square-root gerbes. Prove the multiplicativity
   morphism of gerbes or record the residual twist. Prove associativity of
   the gerbe product over two-step flags.

5. **Twisted six-functor formalism.** Supply a Borel-Moore or
   compact-support six-functor theory on quotient stacks
   \([\operatorname{Or}_{R,\hat c}/E]\), with \(p^*,q_!,p_!,q^*\) and
   Thom-Sebastiani maps admissible for the finite correspondences.

6. **Anti-invariant sector.** Prove that the \(\mu_2\)-anti-invariant
   summand is preserved by product, coproduct, transitions, and
   normal-ordering cochains.

7. **O1 ordinary gerbe and quotient descent.** Compute
   \(\alpha^{\mathrm{red}}\), \(\alpha^{E,\mathrm{free}}\),
   all finite Borel classes \(\widetilde\beta^{E,N}\), and all residual
   degree-one characters \(\lambda^{E,N}\). Kill them on every object,
   extension, flag, component, boundary, and transition stratum used by the
   Hall source.

8. **Higher finite stabilizers.** Complete the even \(N\ge4\) calculation:
   \(A_1^{(N)}=A_{12}^{(N)}=A_2^{(N)}=0\) and
   \(\lambda_1^{(N)}=\lambda_2^{(N)}=0\) on the two-primary generators.
   The \(E[2]\) calculation is insufficient.

9. **O1+ Weyl lift.** Construct determinant-line lifts \(\tau_i\), compute
   the projective cocycle \(c_o\), kill \([c_o]\), normalize
   \(\tau_i^2=1\), and prove all quotient torsor defects
   \(\omega_{i,\mathcal C}\) vanish. This must hold in finite action
   groupoids and compatibly in the HN inverse system.

10. **O2 local wall charts.** For each type-II simple wall, construct the
    wall object, real analytic \(s_{\delta_i}\)-equivariant chart, local
    equation \(u_i\), tangent/normal splitting, invariant unit, and normal
    rank computation \(N_{\delta_i}^{\mathrm{Pf}}=1\). Include component,
    boundary, overlap, quotient, and hybrid wrapped compatibility,
    especially for the \(\delta_2\leftrightarrow(0,1,1)\) wrapped sector.

11. **Hall character.** After O1/O1+/O2, prove the local signs define an
    honest character on \(W^{(2)}(\Lambda^{2,1}_{II})\). Only then compare
    with \(\nu_{\Delta_5}\). The comparison cannot precede the construction
    of \(\epsilon_o\).

12. **Pfaffian-to-automorphic comparison.** Supply
    \[
    \iota_{\mathrm{aut}}:\mathscr L_{\mathrm{Pf},X}
    \xrightarrow{\sim}\mathcal L^5\otimes\nu_{\Delta_5}
    \]
    compatible with cusp trivialization and squaring. Without it, the
    strongest statement is equality of normalized formal products.

13. **Primitive recognition after \(H^{\mathrm{tw}}\).** Construct
    primitive representatives, parity splits, Hall brackets, Hopf pairing,
    radical quotient, no-extra-relations theorem, PBW, and exact completion
    from \(H^{\mathrm{tw}}_{X,\Gamma}\). Signed dimensions alone do not
    produce \(\mathfrak g_{\Delta_5}\).

14. **Scalar square last.** Only after a source Pfaffian has been
    constructed and recognized may the OP/DT branch be used as the
    orientation-forgetting scalar trace
    \[
    \operatorname{Tr}_{\mathrm{prot}}((-1)^F\mathfrak D_X^{-2})
    =-4096\Delta_5^{-2}.
    \]
    It is a check on the square, not the source of the square root.

No edit to `main.tex`, `proj.bib`, or existing manuscript source was made.
