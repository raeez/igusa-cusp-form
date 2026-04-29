# Agent 28 Formal Pfaffian Normalization Report

Date: 2026-04-29

Scope: formal algebraic Pfaffian/product normalization lane. Sources mined:
`materials/raw/2026-04-29-attack-whitepaper-analysis.pdf` via `pdftotext`,
`materials/processed/2026-04-29-attack-whitepaper-analysis.txt`, live
`main.tex`, and prior swarm reports in `notes/`.

Verdict: current `main.tex` does not define
`D^{alg}_{\Delta_5,C,L}`, `Den^{alg}_{\Delta_5,C,L}`, `s_L`, a
curve-universal lifted current target, or an algebraic Dirac/Pfaffian
operator package. The attack PDF asks for this construction
(`materials/processed/2026-04-29-attack-whitepaper-analysis.txt:18689`,
`:18749`, `:18778`, `:18789`, `:22483`, `:22928`, `:23021`). The safe
addition is possible only as a source-free algebraic target package built
from the imported Gritsenko--Nikulin BKM algebra, the normal-ordered
charge extension, and a completed formal product. It is not a compact
Dirac operator and not a compact Hall/Pfaffian construction.

## Safe formal product statement

The safe theorem-level product already in `main.tex` is the
theta-normalized Borcherds product:
```tex
\mathcal D_X(Z)
=64q^{1/2}r^{1/2}s^{1/2}
\prod_{\gamma=(n,l,m)\in\Gamma_{\mathrm{eff}}}
(1-q^nr^ls^m)^{f(nm,l)}
=\Delta_5(Z).
```
Status: constructed `K_0` superdeterminant package plus imported
Borcherds--Gritsenko--Nikulin identification. It is not a compact
one-particle Hilbert space and not an operator with a spectrum
(`main.tex:766-823`, `main.tex:853-880`, `main.tex:2530-2558`).

The corresponding monic product is
```tex
D_5(Z):=64^{-1}\Delta_5(Z)
=q^{1/2}r^{1/2}s^{1/2}
\prod_{\Gamma_{\mathrm{eff}}}(1-q^nr^ls^m)^{f(nm,l)}.
```
This is the product GNII denotes by `\Delta_5`; this paper reserves
`\Delta_5` for the theta-constant normalization (`main.tex:2541-2552`).

The denominator identity is a different normalization:
```tex
\operatorname{den}(\mathfrak g_{\Delta_5})
=D_5(2Z)
=64^{-1}\Delta_5(2Z)
=e^{-2\pi i(\rho,z)}
\prod_{\alpha\in\mathcal R_+}
(1-e^{-2\pi i(\alpha,z)})^{\smult(\alpha)}.
```
The `2Z` is forced by the conversion from
`q^nr^ls^m=\exp(-\pi i(\alpha(n,l,m),z))` to the usual denominator
character `\exp(-2\pi i(\alpha,z))` (`main.tex:5690-5699`,
`main.tex:13543-13563`, `main.tex:14796-14824`).

If `D^{alg}_{\Delta_5,C,L}` is introduced, the safe statement is:
```tex
D^{alg}_{\Delta_5,C,L}
:=
(\mathfrak g_{\Delta_5,L},
 Den^{alg}_{\Delta_5,C,L},
 \bar B_C^{ch}(Den^{alg}_{\Delta_5,C,L}),
 \operatorname{Pf}^{alg}_{\Delta_5})
```
where `\operatorname{Pf}^{alg}_{\Delta_5}` is only the completed formal
product above, or a finite-window inverse limit of that product after all
completion and parity conventions are fixed. This tuple is a target
package. It must not be denoted `D_X`, `\mathfrak D_X`, or "compact".

## Pfaffian terminology constraints

1. The unconditional formal identity in the paper is a superdeterminant:
```tex
\sdet_V(1-x)=\prod_{\lambda}(1-x^\lambda)^{\sdim V_\lambda}.
```
This is `main.tex:743-755`. Calling it a Pfaffian is false unless a
skew form, a Pfaffian line, a squaring map, and a Pfaffian section are
also specified.

2. A formal algebraic Pfaffian may be introduced only finite-window first.
For a finite positive window `W`, one may define a block model with
homogeneous super spaces `V_\gamma` and a skew block
```tex
J_\gamma=
\begin{pmatrix}
0&1-x^\gamma\\
-(1-x^\gamma)&0
\end{pmatrix}.
```
The attack PDF sometimes displays a non-skew `[[0,1-x],[1,0]]` block; that
is a determinant emulator, not a Pfaffian block. Current `main.tex`
correctly uses the skew sign in the conditional compact section
(`main.tex:10656-10678`).

3. The Pfaffian exponent is still only signed superdimension unless the
actual parity model is named:
```tex
\sdim V_\gamma
=\dim V_{\gamma,\bar0}-\dim V_{\gamma,\bar1}.
```
If `V_\gamma=\mathfrak g_{\Delta_5,\gamma}` is used, the parity is the
imported GN/Kac super root-space parity. If a minimal `K_0` representative
is used, it is only a virtual product model. The product alone never
selects the full pair `(dim even, dim odd)`; see the finite target-window
obstruction (`main.tex:10860-10918`, `main.tex:11282-11483`).

4. A section-level statement
`\operatorname{Pf}^{alg}_{\Delta_5}=\Delta_5` requires an automorphic line
comparison if it is anything more than equality of cusp expansions. The
compact theorem makes this explicit:
```tex
\iota_{\mathrm{aut}}:\mathscr L_{\mathrm{Pf},X}\simeq
\mathcal L^5\otimes\nu_{\Delta_5}.
```
Without `\iota_{\mathrm{aut}}`, the strongest compact statement is equality
of normalized formal products at the cusp (`main.tex:1481-1495`,
`main.tex:1708-1727`).

5. A formal target Pfaffian is not the compact `\operatorname{Pf}_{prot}`
of `\mathfrak D_X`. Current `main.tex` already says `\mathfrak D_X` is
supplied data inside `D0`, not constructed from the determinant
(`main.tex:1139-1174`, `main.tex:11518-11661`, `main.tex:11750-11766`).

## Normalization ledger

| item | safe value | forbidden drift |
|---|---|---|
| K3 elliptic genus | `Z_{K3}=2\phi_{0,1}`; `\phi_{0,1}=\sum f(n,l)q^nr^l` | using `2f(nm,l)` in the `\Delta_5` half-product |
| first coefficients | `\phi_{0,1}=r^{-1}+10+r+q(10r^{-2}-64r^{-1}+108-64r+10r^2)+...` | reading negative `f` as negative Hilbert dimension |
| theta-normalized cusp form | `[q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64` | treating `64` as an orientation or Pfaffian sign |
| monic product | `D_5=64^{-1}\Delta_5` | writing the monic product as theta-normalized `\Delta_5` |
| virtual determinant | `\mathcal D_X=\Delta_5` | saying this constructs a compact operator |
| denominator algebra | `den(\mathfrak g_{\Delta_5})=D_5(2Z)=64^{-1}\Delta_5(2Z)` | using `D_5(Z)` or `\Delta_5(Z)` in the BKM denominator |
| positive product exponents | `f(nm,l)` on active/effective support | inferring zero root spaces from zero signed exponent |
| OP square | `\chi_{10}^{OP}=D_5^2=4096^{-1}\Delta_5^2` | using theta-normalized `\Delta_5^2` as OP's monic product |
| OP scalar branch | `Z^X_{OP/DT}=-4096\Delta_5^{-2}` | reading `-4096` as a Hall/Pfaffian orientation sign |
| `Z` versus `2Z` | product for `\Delta_5(Z)`; denominator for `\Delta_5(2Z)` | mixing cusp-product variables with denominator-character variables |
| parity | product fixes `dim even - dim odd` | inferring compact parity bases or minimal parity lift |

The arithmetic `-4096=(-1)_{OP}\cdot64^2` is scalar normalization only
(`main.tex:13724-13804`, `main.tex:13857-13955`, Agent 04).

## Required completions/cones

1. Product completion. All products live in the Borcherds cusp-completed
semigroup algebra with
```tex
0<|s|\ll |q|\ll |r|^{-1}\ll1.
```
Every coefficient must receive finitely many contributions in that
completion (`main.tex:766-769`).

2. Product support. The product support is `\Gamma_{\mathrm{eff}}`, and
the active support is
```tex
\Gamma_{\mathrm{act}}
=\{\gamma=(n,l,m)\in\Gamma_{\mathrm{eff}}\mid f(nm,l)\ne0\}.
```
Inactive triples have exponent zero only. They do not prove absence of
zero-superdimension root spaces (`main.tex:5396-5414`).

3. Positive root cone. Under
```tex
\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
=n\delta_1+m\delta_2+(n+m-l)\delta_3,
```
the proof-grade Borcherds cone is
```tex
\Cone_{\mathrm{Borch}}
=\mathbb R_{\ge0}\delta_1+
 \mathbb R_{\ge0}\delta_2+
 \mathbb R_{\ge0}\delta_3.
```
This is an active-support cone in the type-II chamber, not a compact
effective-support theorem (`main.tex:5416-5458`).

4. Cartan exclusion. The zero degree of
`\mathcal A_{\mathrm{den}}` is the even Cartan
`\Lambda_{II}^{2,1}\otimes\mathbb C`; it is not governed by `f(0,0)` and
must not enter the determinant product (`main.tex:5590-5603`). The product
is over positive roots/effective degrees, never over the whole current
algebra.

5. Finite windows before inverse limits. A formal algebraic Pfaffian must
be defined first on finite positive windows, then completed. Current
compact `D0-Pf` uses `\Gamma_R^{test,+}`, source coverage, support
residuals, parity residuals, and a leading coefficient residual
(`main.tex:10624-10753`). The source-free target shadow uses the finite
`K_0` section
```tex
\operatorname{pf}^{K_0}_{\Delta,R}
=64q^{1/2}r^{1/2}s^{1/2}
\prod_{\gamma\in\Gamma_R^{test,+}}(1-x^\gamma)^{a_\Delta(\gamma)}.
```
It is explicitly not a compact Hall object, not a Pfaffian line, and not a
first-order operator (`main.tex:10884-10918`).

6. Normal-ordered lift if `D^{alg}` is added. Choose a noncanonical group
homomorphism
```tex
L:\Gamma_{\mathrm{gram}}\to\Gamma_X^{form}
```
and define
```tex
s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)\in\widehat\Gamma_X.
```
Then `\overline\Pi_X(s_L(\gamma))=\gamma` and
`s_L(\gamma+\eta)=s_L(\gamma)\star s_L(\eta)` by the polarization
identity. Regrade `\mathfrak g_{\Delta_5,\gamma}` to degree `s_L(\gamma)`.
This is a target regrading. It is not algebraic/effective support and not
a compact source.

7. Curve current convention. If the formal current envelope is generalized
from `E` to a curve `C`, fix one convention:
left `D`-module notation uses `\mathfrak g\otimes\mathcal O_C`; right
`D`-module notation uses `\mathfrak g\otimes\omega_C`. Do not mix them in
one theorem. The current envelope is curve-formal; `C=E` is forced only by
the compact `K3\times E` source, translation quotient, elliptic degree,
and wrapped anchors.

## Forbidden analytic/operator inferences

1. `\mathcal D_X=\Delta_5` does not construct `\mathfrak D_X`.

2. `D^{alg}_{\Delta_5,C,L}` does not imply a compact BPS Hilbert space,
compact Hall source, compact chiral source, protected integration functor,
or compact Pfaffian line.

3. A formal algebraic block product does not define an analytic Dirac
operator: no domain, Hilbert completion, self-adjointness, ellipticity,
Fredholm property, spectrum, heat kernel, zeta determinant, or index
theorem is present.

4. A superdeterminant/Berezinian product is not a Pfaffian unless the
skew-adjoint two-term block, Pfaffian line, square map, and sign convention
are fixed.

5. The denominator theorem supplies the imported GN/Kac target bracket only
because `\mathfrak g_{\Delta_5}` is imported. The product alone does not
determine bracket constants, primitive representatives, closed radical,
PBW compatibility, or no-extra-relations (`main.tex:13603-13650`,
`main.tex:13652-13699`).

6. The OP scalar square does not construct a square-root object, a
Pfaffian line, or an orientation sign. `64`, `4096`, and the OP minus sign
are scalar normalizations (`main.tex:13924-13955`).

7. The automorphic Maass character is not the compact Hall orientation
character. Equality
`\epsilon_o=\nu_{\Delta_5}` requires O1 quotient orientation, O1+ Weyl
transport, and O2 local Pfaffian wall charts (`main.tex:1407-1476`,
`main.tex:1754-1784`; Agent 05; fourth Pfaffian report).

8. The target bar-cobar counit of a formal current envelope is not the
compact source coalgebra. The source coalgebra must be constructed from
compact geometry and compared to the target afterward (Agent 15).

9. A linear lift `L` is not canonical, not Weyl-equivariant, not
duality-equivariant, and not a section of the quadratic raw map `\Pi_X`.
If equivariance or gauge equivalence is wanted, it is extra structure.

10. Curve-universality of `Den^{alg}_{\Delta_5,C,L}` does not produce an
OP/DT theorem for `K3\times C`. OP/DT quotient theory is elliptic-specific
in this manuscript.

## main.tex anchors

- Opening product and normalization: `main.tex:58-81`.
- Opening denominator target/source separation: `main.tex:83-98`.
- Opening Dirac/Pfaffian target remains open: `main.tex:100-115`.
- OP scalar conversion in abstract: `main.tex:117-129`.
- Grothendieck half-index representative: `main.tex:722-740`.
- Superdeterminant lemma and cusp completion: `main.tex:743-769`.
- Normalized `K_0` determinant: `main.tex:818-838`.
- Virtuality and no operator product: `main.tex:853-880`.
- Dirac/Pfaffian target presently typed too strongly as a proposition:
  `main.tex:882-905`.
- Conditional D0/Pfaffian theorem assumes the compact object:
  `main.tex:1139-1174`, `main.tex:1678-1727`.
- Pfaffian-to-automorphic comparison: `main.tex:1481-1495`.
- Scalar-square proof and OP constant: `main.tex:1729-1752`.
- Normalized cusp form and coefficient `64`: `main.tex:2383-2424`.
- BGN monic/theta normalization: `main.tex:2530-2558`.
- Normalization table: `main.tex:2560-2599`.
- Active support and cone: `main.tex:5396-5458`.
- Denominator algebra and Cartan exclusion: `main.tex:5560-5702`.
- Formal current envelope over `E`: `main.tex:5704-5756`.
- Conditional finite Pfaffian line/product: `main.tex:10624-10753`.
- Finite `K_0` Pfaffian shadow and parity ambiguity:
  `main.tex:10860-10918`.
- Finite Hall--Dirac atlas and parity-lift obstruction:
  `main.tex:11282-11483`.
- D0 status ledger: `main.tex:11518-11661`.
- Compact realization certificate, not construction: `main.tex:11750-11766`.
- Denominator identity and `2Z`: `main.tex:13543-13601`.
- What the denominator determines/forgets: `main.tex:13603-13699`.
- OP normalization and scalar square: `main.tex:13724-13955`.
- Main synthesis currently mixes theorem and ledger: `main.tex:14031-14264`.
- Two exponential normalizations: `main.tex:14796-14824`.
- Eight formal current rows show the formal-product pattern but not compact
  sources: `main.tex:15348-15379`.

Negative current-main check: `rg` found no `D^{alg}`, no
`Den^{alg}_{\Delta_5,C,L}`, no `s_L` theorem, and no curve-universal
formal target in `main.tex`.

## Patch queue

1. Decide whether the manuscript wants `D^{alg}_{\Delta_5,C,L}` at all. If
minimal, omit it and state the compact algebraic lift is not constructed.

2. If `D^{alg}` is added, insert it before the compact realization problem
and after the normal-ordering lattice theorem. Required sequence:
`Den^{alg}_{\Delta_5,C}`, `L`, `s_L`, `\mathfrak g_{\Delta_5,L}`,
`Den^{alg}_{\Delta_5,C,L}`, then `D^{alg}_{\Delta_5,C,L}` as a tuple.

3. Define `L` only as a chosen homomorphism. Add a dependence paragraph:
different lifts differ by an element of
`Hom_Z(\Gamma_{\mathrm{gram}},\Gamma_X^{form})`; no canonical or gauge
equivalence statement exists until a lift groupoid/action is defined.

4. Define any algebraic Pfaffian behind a finite-window product:
positive support, Cartan exclusion, completion, parity model, skew block,
Pfaffian/Berezinian convention, and leading coefficient.

5. Use `\sdet` unless the Pfaffian line and skew block convention are
actually specified. If using `\operatorname{Pf}^{alg}`, say it is a formal
algebraic Pfaffian section, not compact.

6. Generalize the formal current envelope from `E` to arbitrary smooth
`C`, then alias `\mathsf{Den}_{\Delta_5,E}` to the elliptic specialization
for `K3\times E`.

7. Convert `main.tex:882-918` from proposition to open problem or
definition. It names a missing object.

8. Add a normalization ledger near the first product display: `D_X`,
`D_5`, `Delta_5`, `64`, `2Z`, `chi_{10}^{OP}`, `-4096`.

9. Add a forbidden-implication box:
`\mathcal D_X=\Delta_5 \not\Rightarrow \mathfrak D_X`;
`\Delta_5^2 \not\Rightarrow` orientation/Pfaffian;
`\mathfrak g_{\Delta_5}\not\Rightarrow` compact Hall source;
`\Gamma_{\mathrm{gram}}\ne` Hall charge lattice.

10. Keep O1/O1+/O2 separate from scalar normalization. Do not let
automorphic divisor order replace local Pfaffian normal-mode rank.

11. State explicitly that the zero-degree Cartan is excluded from the
formal product.

12. Run label hygiene after edits: theorem labels only on theorem
environments; remove unsafe aliases such as `thm:factorization-square-root`
for the formal current envelope.

## Residual proof/source checks

1. Source-check GN/GNII for the monic product, theta factor `64`,
coefficient convention, `m(a)`, isotropic `\tau(a)`, and
`D_5(2Z)` denominator normalization. Agent 11 marks this high priority.

2. Source-check OP/Oberdieck/Oberdieck--Pandharipande for
`\chi_{10}^{OP}=D_5^2`, the variable map, chamber, and the sign in
`Z^X_{OP}=-(\chi_{10}^{OP})^{-1}`. Agent 12 did only local arithmetic.

3. Verify the BD chiral enveloping construction for completed ind
Lie-* superalgebras with finite homogeneous root spaces. State the
filtration/conilpotence/completion used.

4. Prove or clearly assume that regrading and chiral enveloping commute:
```tex
\overline\Pi_{X,*}U_C^{ch}(Cur_C(\mathfrak g_{\Delta_5,L}))
\cong
U_C^{ch}(Cur_C(\overline\Pi_{X,*}\mathfrak g_{\Delta_5,L})).
```

5. Fix the `D`-module convention: left `\mathcal O_C` versus right
`\omega_C`.

6. If the formal product uses actual GN root spaces, verify the imported
super parity convention. If it uses a minimal `K_0` model, state that it
is not the GN root-space parity.

7. Check the formal Pfaffian block: skew sign, parity shift `\Pi`,
dualization, Berezinian/Pfaffian convention, and exponent sign for even
versus odd basis vectors.

8. Prove finite-window completions have coefficientwise finite products
before inverse limit. Do not hide infinite products inside notation.

9. Keep compact source obligations open: finite Hall stages, extension
correspondences, orientation quotient, first-order complex, Pfaffian line,
source parity bases, transition maps, radical quotient, PBW, and
Mittag--Leffler exactness.

10. Add or remove the group cohomology source gap for finite-stabilizer
orientation computations. Agent 20 reports no Cartan--Eilenberg/Brown
source in `proj.bib`.

11. Verify Maass/GN reflection values independently of local Pfaffian rank:
`\nu_{\Delta_5}(s_{\delta_i})=-1` for the three type-II simple reflections
and `+1` on the three chamber-permuting reflections.

12. After any `D^{alg}` insertion, rerun grep checks for false arrows:
```bash
rg -n 'D\\^\\{alg\\}.*compact|compact.*D\\^\\{alg\\}|operator.*spectrum|4096.*orientation|orientation.*4096|Den\\^\\{alg\\}.*source' main.tex
```
