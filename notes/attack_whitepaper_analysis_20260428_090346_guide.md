# Attack Whitepaper Analysis - Reconstitution Guide

Date absorbed: 2026-04-28.
Source: `materials/raw/2026-04-28-090346-attack-whitepaper-analysis.pdf`.
Extracted text: `materials/processed/2026-04-28-090346-attack-whitepaper-analysis.txt`.

Status: internal guide.  This is an attack-and-construction source, not
primary literature.  Before any statement is inscribed in `main.tex`,
verify it against the manuscript, direct computation, and the cited
Borcherds--Gritsenko--Nikulin / OP / orientation sources.

## Governing Diagnosis

The source says that the paper is strongest when it separates five
layers:

1. the virtual `K_0` Borcherds determinant;
2. the imported Gritsenko--Nikulin denominator algebra;
3. the imported OP/DT scalar square;
4. the proved lattice-level physical charge and normal-ordered Gram
   descent;
5. the still-open compact Dirac--Igusa Hall/factorization realization.

The central failure mode is the triple `(n,l,m)`.  It was being used as
Fourier exponent, BKM root degree, and physical/Hall charge.  The first
two are additive.  The third is not additive when `(n,l,m)` is the Gram
invariant of physical charges.  The correct repair is not to downgrade
the ambition.  It is to build a two-layer charge theory:

```tex
\Gamma_X^{phys} = \Lambda_S \oplus \Lambda_S,
\qquad
\Gamma_{gram} = \mathbb Z^3,
```

with a quadratic Gram map

```tex
\Pi_X(Q,P)=\left(Q^2/2,\;Q\cdot P,\;P^2/2\right).
```

The compact Hall object must be graded first by physical charge, or by
the normal-ordered extension below, not directly by `Gamma_gram`.

## Central Construction

### Physical Charge Lattice

For `X = S x E`, with `S` a K3 surface,

```tex
\Lambda_S = H(S,\mathbb Z)
          = H^0(S,\mathbb Z)\oplus H^2(S,\mathbb Z)\oplus H^4(S,\mathbb Z),
```

with Mukai pairing

```tex
(r,D,s)\cdot(r',D',s')=D\cdot D' - rs' - r's.
```

The algebraic even dyonic Mukai lattice is

```tex
\Gamma_X^{phys}=\Lambda_S\oplus\Lambda_S.
```

The full `N=4` charge lattice is larger.  The paper must say explicitly
that this lattice is the algebraic D6--D2--D0 / OP sector.

### D6--D2--D0 Mukai--Gram Dictionary

For a one-dimensional subscheme `Y subset X = S x E` with

```tex
[Y]=(\beta,d),\qquad \chi(\mathcal O_Y)=n,
```

the ideal sheaf satisfies

```tex
v_X(I_Y)
=(1,0,1-d)\otimes 1_E+(0,-\beta,-n)\otimes\omega_E.
```

Set

```tex
P_Y=(1,0,1-d),\qquad Q_Y=(0,-\beta,-n).
```

Then

```tex
Q_Y^2/2=\beta^2/2,\qquad Q_Y\cdot P_Y=n,\qquad P_Y^2/2=d-1.
```

For `beta = beta_h`, `beta_h^2 = 2h-2`,

```tex
\Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
```

Consequences:

- `h-1` is the K3 Mukai norm.
- `n` is the Mukai pairing `Q_Y . P_Y`.
- `d-1` is the elliptic-degree Mukai norm.
- There is no vague Todd correction when `n = chi(O_Y)`.
- `K3 x E` is a Calabi--Yau threefold, not a fourfold.

### Gram Cocycle

For physical charges `c=(Q,P)` and `c'=(Q',P')`, define

```tex
B(c,c')=(Q\cdot Q',\;Q\cdot P'+Q'\cdot P,\;P\cdot P').
```

Then

```tex
\Pi_X(c+c')=\Pi_X(c)+\Pi_X(c')+B(c,c').
```

The form `B` is symmetric, bilinear, normalized, and satisfies the
additive two-cocycle identity.  Also

```tex
B(c,c)=2\Pi_X(c).
```

This is pure lattice polarization.  Do not attach it to Bott signs,
orientation choices, or parity conventions.

### Normal-Ordered Extension

Define

```tex
\Gamma_X=\Gamma_X^{phys}\oplus_B\Gamma_{gram}
```

with product

```tex
(c,T)\star(c',T')=(c+c',T+T'+B(c,c')).
```

Define the normal-ordered Gram map

```tex
\overline\Pi_X:\Gamma_X\to\Gamma_{gram},
\qquad
\overline\Pi_X(c,T)=\Pi_X(c)-T.
```

Then

```tex
\overline\Pi_X((c,T)\star(c',T'))
=\overline\Pi_X(c,T)+\overline\Pi_X(c',T').
```

This is the core repair.  Normal-ordering is not a post-processing
correction.  It is the source degree law.

For elementary charges `c_i`,

```tex
(c_1,0)\star\cdots\star(c_k,0)
=\left(\sum_i c_i,\sum_{i<j}B(c_i,c_j)\right),
```

and the normal-ordered degree is

```tex
\overline\Pi_X((c_1,0)\star\cdots\star(c_k,0))
=\sum_i \Pi_X(c_i).
```

### Raw-Descent No-Go

Raw `Pi_X` descent is too strong.  If a physical-charge-graded Lie
superalgebra has

```tex
[P_c,P_{c'}]\subset P_{c+c'},
```

then a raw Gram pushforward would require `B(c,c')=0` on every nonzero
bracket channel.  The BKM real-root strings require nonzero iterated
brackets, including channels where `B(c_i,c_i)=2\Pi_X(c_i) != 0`.  Hence
the full BKM bracket cannot come from raw Gram descent.  The
`B`-corrected normal-ordered source is forced.

### Primitive Saturated Descent

For `c=(Q,P)`, let `M_c = ZQ + ZP`.  The primitive/torsion-one condition
is

```tex
M_c=\Lambda\cap(M_c\otimes\mathbb Q),
```

equivalently `gcd(Q wedge P)=1` in coordinates.  In this sector, the
rank-two Gram form is the invariant shadow used by the Igusa variables.
For torsion greater than one, additional discrete data are required.

## Dirac Principle

The square root is first-order structure, not an analytic branch.

The paper should be ordered by the hierarchy

```tex
local protected operations
\to factorization/Hall algebra
\to primitive Lie algebra
\to BKM denominator target
\to Pfaffian determinant
\to OP/DT scalar square.
```

The OP/DT theorem supplies the scalar square

```tex
Z^{X}_{OP/DT}=-4096\,\Delta_5^{-2}.
```

It does not construct the compact Hall object, a primitive bracket, a
Pfaffian line, or the orientation monodromy character.  The scalar square
forgets the Maass reflection character.

The first-order object should be stated conditionally:

```tex
Pf^{prot}(D_X)=\Delta_5,
\qquad
Z^{X}_{OP/DT}=-4096\,Pf^{prot}(D_X)^{-2},
```

once the compact Dirac--Igusa datum, normal-ordered descent, orientation
package, and primitive recognition certificate are supplied.

## Compact Dirac--Igusa Object

The constructive target is a finite-first pro-object

```tex
\mathcal D^{DI}_X=\lim_R \mathcal D^{DI}_{X,R}.
```

A finite stage should carry:

```tex
(A^E_{3,X,R},
 F^{hyb}_{X,R},
 \Gamma_{X,R},
 \overline\Pi_X,
 \Phi_R,
 o_R,
 H_R,
 P_R^\Pi,
 C_{X,R},
 \Theta_{Kos,R},
 L_{Pf,R},
 pf_{X,R},
 \epsilon_{o,R},
 Rec_R).
```

Interpretation:

- `A^E_{3,X,R}`: finite local protected observable source on `X`.
- `F^{hyb}_{X,R}`: hybrid local/wrapped `K3 -> E` shadow.
- `Gamma_{X,R}`: finite normal-ordered physical charge extension.
- `Phi_R`: vanishing-cycle/BPS coefficient system.
- `o_R`: strong reduced orientation line with quotient and stabilizer
  trivializations.
- `H_R`: finite Hall state object.
- `P_R^Pi`: normal-ordered primitive Lie superalgebra.
- `C_{X,R}`: source chiral Koszul coalgebra.
- `Theta_{Kos,R}`: source-to-target cobar comparison.
- `L_{Pf,R}` and `pf_{X,R}`: Pfaffian line and finite protected
  Pfaffian section.
- `epsilon_{o,R}`: finite orientation-monodromy character.
- `Rec_R`: finite primitive recognition comparison with the
  Gritsenko--Nikulin target.

The inverse limit is taken only after finite products, coproducts,
quotients, orientation transports, normal-ordering shifts, and comparison
maps have been constructed.

## Hybrid Local/Wrapped Factorization

Projection-finite Ran locality on `E` sees only the `m=0` / local
sector.  Positive elliptic degree is not a failure of spacetime
locality.  It is a wrapped sector.

Use a hybrid base with local colors and wrapped elliptic degree.  The
wrapped anchor suggested by the source is

```tex
\lambda(A)=\det Rp_{E,*}A\otimes\mathcal O_E(-\chi(A)\cdot 0_E)
\in Pic^0(E)\simeq E.
```

The reduced `E` quotient should be applied after extension
correspondences are formed, not before.

The hybrid object must have four operation types:

1. local-local;
2. local-wrapped;
3. wrapped-local;
4. wrapped-wrapped.

Associativity is checked on the eight two-step words

```tex
LLL,\ LLW,\ LWL,\ WLL,\ LWW,\ WLW,\ WWL,\ WWW.
```

Each word should have an obstruction class.  The hybrid factorization
object exists at finite stage only after these classes vanish with
compatible transition maps.

## Orientation Package

Strong reduced orientation is not the same as ordinary CY3 orientation.
It has separate layers:

1. ordinary reduced orientation gerbe;
2. connected `E`-descent;
3. finite stabilizer gerbes;
4. finite stabilizer linearization characters.

The connected and finite cases must not be conflated.  For connected
`E^{top} ~= T^2`,

```tex
BE\simeq BT^2,\qquad H^1(BE;\mathbb F_2)=0,\qquad
H^2(BE;\mathbb F_2)\simeq \mathbb F_2^2.
```

For `E[2] ~= (Z/2)^2`,

```tex
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\qquad |x_i|=1,
```

so

```tex
H^2(BE[2];\mathbb F_2)
=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
```

Translation invariance of the underlying line is not enough.  The
equivariant determinant-line linearization must be computed.

The Pfaffian/orientation dependency graph should be:

```tex
Dirac--Pfaffian=(D0)+(O1)+(O1)^+ +(O2).
```

Here:

- `(D0)` is the finite first-order Hall--Dirac source.
- `(O1)` is strong reduced orientation.
- `(O1)^+` is Weyl-equivariant determinant-line transport.
- `(O2)` is the local Pfaffian normal form on the three type-II walls.

The Weyl group part is group theory after the geometric lift exists.  If
the three simple type-II reflection signs satisfy

```tex
\epsilon_o(s_{\delta_i})=-1,\qquad i=1,2,3,
```

then

```tex
\epsilon_o=\nu_{\Delta_5}
```

on the type-II Weyl group.  The geometric work is proving the signs from
the Pfaffian wall charts, not inferring them from the OP scalar sign.

The local wall normal form to construct is

```tex
K^{nor}\simeq [R \xrightarrow{u_i} R],
\qquad
s_{\delta_i}(u_i)=-u_i.
```

Then the local Pfaffian changes sign while the squared determinant is
fixed.

## Chain-Level Normal Ordering

The lattice theorem is proved by `Gamma_X` and `overline Pi_X`.  The
chain-level theorem is a categorification of that subtraction.

At finite HN height `R`, build `Gamma_{X,R}` from finite physical charge
sets:

```tex
\Gamma_{X,R}
=\{(c_1,0)\star\cdots\star(c_k,0):
  c_i\in F_{\sigma,S}(R),\ \sum_i h_S(c_i)\le R\}.
```

Then supply chain-level translation functors and a normal-ordering
cochain realizing the central shifts.  The obstruction package
`NO1--NO7` is:

1. finite-fibre/topological descent;
2. Hochschild boundary;
3. triple pentagon;
4. Jacobi compatibility;
5. Frobenius/cyclic pairing identity;
6. negative-cyclic lift;
7. Hopf radical ideal/coideal stability.

The source coalgebra must be built from the compact source, not from the
target current envelope:

```tex
C_{X,R}=B^{ch}_E(F^{hyb}_{X,R})
```

or a finite conilpotent model quasi-isomorphic to it.  The Koszul map is
source-to-target; it is not the target-internal bar--cobar counit.

## Primitive Recognition Certificate

The determinant fixes signed superdimensions.  It does not fix brackets,
parity splits, invisible zero-superdimension summands, simple-root
representatives, or relations.  A zero-bracket graded super vector space
with the same signed dimensions has the same determinant and the wrong
algebra.

Recognition of `g_{\Delta_5}` requires:

1. Cartan identification;
2. real simple representatives;
3. imaginary simple-root fibres with Gritsenko--Nikulin multiplicity and
   parity data;
4. Chevalley relations;
5. real Serre relations;
6. imaginary orthogonality;
7. generation by Cartan plus simple primitives;
8. completed PBW;
9. equality after completed Hopf-pairing radical quotient;
10. no extra completed relations;
11. full root-space parity dimensions, not merely signed dimensions.

The recognition theorem is a certificate theorem.  It does not construct
the compact Hall/factorization source.

## Clean Theorem Package

The source's final recommended spine is:

1. **Virtual Automorphic Determinant.**
   ```tex
   D_X(Z)=64q^{1/2}r^{1/2}s^{1/2}
   \prod_{\Gamma_{eff}}(1-q^nr^ls^m)^{f(nm,l)}
   =\Delta_5(Z).
   ```
2. **D6--D2--D0 Mukai--Gram Dictionary.**
   ```tex
   v_X(I_Y)=(1,0,1-d)\otimes1_E+(0,-\beta,-n)\otimes\omega_E,
   \qquad
   \Pi_X(Q_Y,P_Y)=(h-1,n,d-1).
   ```
3. **Normal-Ordered Charge Theorem.**
   ```tex
   \Gamma_X=\Gamma_X^{phys}\oplus_B\Gamma_{gram},
   \qquad
   \overline\Pi_X(c,T)=\Pi_X(c)-T.
   ```
   Then `overline Pi_X` is additive.
4. **Raw-Descent No-Go.**
   Raw `Pi_X` descent cannot realize the full BKM real-root strings.
5. **Conditional Normal-Ordered Descent.**
   If the finite-stage chain-level obstruction package vanishes
   compatibly, the protected primitive bracket descends to a
   `Gamma_gram`-graded bracket.
6. **Hybrid Locality Theorem.**
   If the finite hybrid certificates exist, the `b=0` sector is ordinary
   projection-finite factorization, while `b>0` sectors are wrapped
   modules acted on by mixed Hall correspondences.
7. **Dirac--Pfaffian Certificate.**
   If `D0+(O1)+(O1)^+ +(O2)` hold, then
   ```tex
   Pf^{prot}(D_X)=\Delta_5,\qquad
   Tr^{prot}((-1)^F D_X^{-2})=-4096\Delta_5^{-2}.
   ```
8. **Orientation Character.**
   If the Weyl lift is honest and the three simple reflection signs are
   `-1`, then `epsilon_o = nu_{Delta_5}` on the type-II Weyl group.
9. **Primitive Recognition.**
   If the full source primitive recognition certificate holds, then
   ```tex
   H^0 Prim^{prot}(\overline\Pi_{X,*}^{\Theta}F_X^{hyb})\simeq g_{\Delta_5}.
   ```

## Immediate Manuscript Rules From This Source

Use these as a checklist before future repairs:

1. Put a theorem-status ledger near the front: proved, imported,
   conditional, certificate, open.
2. State that `Delta_5` is first-order/Pfaffian data; `Delta_5^2` is the
   scalar square.
3. Use `D_X=\Delta_5` and `D_5=64^{-1}\Delta_5` consistently.
4. State the theta-leading coefficient `64`.
5. State that `4096` and the OP minus sign are scalar normalizations, not
   orientation data.
6. Replace all "half Hilbert space" language by "Grothendieck half-index
   representative" unless a compact Hilbert object is actually supplied.
7. Split `V=V_bulk \oplus V_cusp`; never call cusp/boundary factors
   physical one-particle K3 states.
8. Move the D6--D2--D0 Mukai--Gram theorem before the scalar OP theorem.
9. Remove "fourfold" for `K3 x E`.
10. Remove vague "Todd correction" language.
11. Make `Gamma_X` and `overline Pi_X` the primary descent mechanism.
12. Treat `Theta` as chain-level categorification of the lattice
    normal-ordering.
13. State the raw-descent no-go before the positive descent theorem.
14. Define hybrid local/wrapped factorization, not only its slogan.
15. Separate connected `BE` descent from finite `BE[N]` descent.
16. Downgrade any small-orbit `E[2]` vanishing claim to a criterion until
    linearization characters are computed.
17. Do not infer Weyl orientation monodromy from the OP scalar sign.
18. Use "formal target current envelope", not "compact current algebra",
    unless a compact source is constructed.
19. State source-to-target Koszul comparison; do not reconstruct the
    source from the target counit.
20. End with the exact open theorem: construct a finite-first,
    normal-ordered, orientation-sensitive, hybrid Hall factorization
    algebra on `K3 x E`.

## Open Obligations

The paper can claim the lattice and automorphic pieces only at the
strength verified.  The remaining construction obligations are:

1. construct the finite-first compact Hall--Dirac source `(D0)`;
2. prove strong reduced orientation `(O1)`;
3. prove Weyl-equivariant orientation transport `(O1)^+`;
4. compute the Pfaffian wall normal form `(O2)` at the three type-II
   walls;
5. construct the hybrid local/wrapped factorization object with all
   eight two-step flag compatibilities;
6. realize chain-level normal ordering and kill `NO1--NO7`;
7. construct the source chiral Koszul coalgebra and source-to-target
   comparison;
8. prove primitive recognition against `g_{\Delta_5}` at presentation
   level;
9. verify every numeric coefficient, character, divisor, and root-space
   parity against computation or primary literature before it enters
   `main.tex`.
