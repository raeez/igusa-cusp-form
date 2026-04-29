# Agent 15 Formal Current Envelope Report

Date: 2026-04-29

Scope: formal-current-envelope / curve-universal algebraic target / `D^{alg}_{\Delta_5,C,L}` consequences, mined from `materials/processed/2026-04-29-attack-whitepaper-analysis.txt` and current `main.tex`.

Verdict: current `main.tex` has the imported Gritsenko-Nikulin denominator algebra, the normal-ordered charge extension, and the formal current envelope over the elliptic curve `E`. It does not yet define the source-free lifted algebraic target `D^{alg}_{\Delta_5,C,L}` demanded by the attack notes. That target is mathematically constructible now, but only as a formal algebraic regrading/current-envelope/Pfaffian-product package. It is not compact geometry, not a Hall source, not an OP/DT theory, and not a source coalgebra.

## Stable theorem-level construction

1. Current theorem-level lattice input:
   `main.tex` defines
   `\Gamma_X^{form}=\Lambda_S\oplus\Lambda_S`, `\Gamma_{gram}=\mathbb Z^3`,
   `\Pi_X(Q,P)=(Q^2/2,Q\cdot P,P^2/2)`, and the bilinear defect
   `B(c,c')=(Q\cdot Q', Q\cdot P' + Q'\cdot P, P\cdot P')`.
   It proves the central normal-ordered extension
   `\widehat\Gamma_X=\Gamma_X^{phys}\oplus_B\Gamma_{gram}` with
   `(c,T)\star(c',T')=(c+c',T+T'+B(c,c'))` and additive
   `\overline\Pi_X(c,T)=\Pi_X(c)-T`.
   This is stable and already theorem-level.

2. Current theorem-level denominator input:
   `main.tex` imports the Gritsenko-Nikulin BKM superalgebra
   `\mathcal A_{den}=\mathfrak g_{\Delta_5}`, graded by
   `\gamma=(n,l,m)` via
   `\alpha(\gamma)=2nf_2-lf_3+2mf_{-2}`. Its visible signed
   multiplicities are `f(nm,l)` and its denominator is
   `64^{-1}\Delta_5(2Z)`. This is an imported denominator theorem, not a
   compact Hall construction.

3. Current theorem-level formal current object:
   `main.tex` defines
   `Cur_E(\mathcal A_{den})=\mathcal A_{den}\otimes\mathcal O_E` and
   `\mathsf{Den}_{\Delta_5,E}=U_E^{ch}(Cur_E(\mathcal A_{den}))`.
   It correctly says this is a formal Beilinson-Drinfeld target and not a
   compact BPS state space.

4. Constructible now, but not yet in `main.tex`:
   for any homomorphism
   `L:\Gamma_{gram}\to\Gamma_X^{form}`, define
   `s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)\in\widehat\Gamma_X`.
   Then
   `\overline\Pi_X(s_L(\gamma))=\gamma` and
   `s_L(\gamma+\eta)=s_L(\gamma)\star s_L(\eta)`.
   This is immediate from the polarization identity for `B`.

5. Constructible now, but only as target regrading:
   define `\mathfrak g_{\Delta_5,L}` by
   `(\mathfrak g_{\Delta_5,L})_{s_L(\gamma)}=\mathfrak g_{\Delta_5,\gamma}`
   and zero in all other `\widehat\Gamma_X`-degrees, with bracket
   transported from `\mathfrak g_{\Delta_5}`. Since `s_L` is monoidal,
   this is a genuine `\widehat\Gamma_X`-graded Lie superalgebra and
   `\overline\Pi_{X,*}\mathfrak g_{\Delta_5,L}\cong\mathfrak g_{\Delta_5}`.
   It is a source-free algebraic target, not a compact source.

6. Constructible now, curve-universally:
   for any smooth complex curve `C`,
   `Cur_C(\mathfrak g_{\Delta_5,L})=\mathfrak g_{\Delta_5,L}\otimes\mathcal O_C`
   in left `D`-module conventions, or
   `\mathfrak g_{\Delta_5,L}\otimes\omega_C` in right conventions, and
   `Den^{alg}_{\Delta_5,C,L}:=U_C^{ch}(Cur_C(\mathfrak g_{\Delta_5,L}))`.
   Its normal-ordered pushforward should be
   `\overline\Pi_{X,*}Den^{alg}_{\Delta_5,C,L}\cong Den^{alg}_{\Delta_5,C}`.
   This uses only the formal current construction on a curve.

## Missing construction demanded by PDF

1. The attack notes demand an explicit algebraic object
   `D^{alg}_{\Delta_5,C,L}`. Current `main.tex` has no definition of
   `L`, no `s_L`, no `\mathfrak g_{\Delta_5,L}`, no
   `Den^{alg}_{\Delta_5,C,L}`, and no named `D^{alg}_{\Delta_5,C,L}`.

2. The attack notes demand curve-universality. Current `main.tex` defines
   the formal current envelope only over `E`, even though the proof text
   itself says the BD current construction sends a Lie superalgebra to a
   Lie-* algebra on a smooth curve.

3. The attack notes demand a clean split:
   `Den^{alg}_{\Delta_5,C,L}` is formal and curve-parametric;
   the compact `K3\times E` realization specializes to `C=E` only after
   the geometric source enters. Current `main.tex` partially says this,
   but the notation `\mathsf{Den}_{\Delta_5,E}` still makes the formal
   target look elliptic-physical.

4. The attack notes demand a formal algebraic Dirac/Pfaffian package.
   Current `main.tex` has finite target windows and a minimal target-window
   parity model, but it does not package the source-free target as
   `D^{alg}_{\Delta_5,C,L}`. A formal product/Pfaffian identity can be
   stated, but only after defining finite windows, positive root support,
   zero-degree Cartan exclusion, completion, parity convention, and the
   exact `64` / `2Z` normalization.

5. The attack notes demand source objects (`H_X^{pre}`, twisted Hall
   object, hybrid wrapped source). Current `main.tex` keeps these as
   certificates/open constructions. For this report's scope, the safe
   rewrite is to construct only the source-free algebraic target now and
   leave compact source construction open unless the manuscript actually
   defines the derived stacks, correspondences, orientations, integration,
   and hybrid wrapped operations as objects.

## Exact rewrite target

Insert, before the compact `K3\times E` realization problem, a new
subsection with this content.

1. Definition: curve-universal formal denominator current.
   Let `C` be a smooth complex curve. Define
   `Cur_C(\mathfrak g_{\Delta_5})=\mathfrak g_{\Delta_5}\otimes\mathcal O_C`
   in left `D`-module conventions, and
   `Den^{alg}_{\Delta_5,C}:=U_C^{ch}(Cur_C(\mathfrak g_{\Delta_5}))`.
   State: this is a formal target object. It is not a compact
   `K3\times C` BPS theory.

2. Definition: normal-ordered lift of labels.
   For a chosen group homomorphism
   `L:\Gamma_{gram}\to\Gamma_X^{form}`, define
   `s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)`.
   Prove:
   `\overline\Pi_Xs_L=id` and
   `s_L(\gamma+\eta)=s_L(\gamma)\star s_L(\eta)`.

3. Definition: lifted denominator algebra.
   Define `\mathfrak g_{\Delta_5,L}` by placing
   `\mathfrak g_{\Delta_5,\gamma}` in degree `s_L(\gamma)` and zero
   elsewhere. Transport the bracket. Prove:
   `[g_c,g_{c'}]\subset g_{c\star c'}` and
   `\overline\Pi_{X,*}\mathfrak g_{\Delta_5,L}\cong\mathfrak g_{\Delta_5}`.

4. Definition: curve-universal lifted current envelope.
   Define
   `Den^{alg}_{\Delta_5,C,L}:=U_C^{ch}(Cur_C(\mathfrak g_{\Delta_5,L}))`.
   Prove:
   `\overline\Pi_{X,*}Den^{alg}_{\Delta_5,C,L}\cong Den^{alg}_{\Delta_5,C}`.

5. Definition: algebraic target package.
   If the manuscript wants the name `D^{alg}_{\Delta_5,C,L}`, define it as
   a tuple, not as compact geometry:
   ```
   D^{alg}_{\Delta_5,C,L}
   :=
   (\mathfrak g_{\Delta_5,L},
    Den^{alg}_{\Delta_5,C,L},
    \bar B_C^{ch}(Den^{alg}_{\Delta_5,C,L}),
    \operatorname{Pf}^{alg}_{\Delta_5})
   ```
   The final factor is only a formal completed product/Pfaffian section,
   normalized by the imported Borcherds product. Do not identify it with a
   compact Pfaffian line.

6. Elliptic specialization paragraph:
   For the compact realization problem set `C=E`. The reason is not the
   formal current construction. It is the compact source geometry:
   `S\times E` is Calabi-Yau threefold, `E` acts by translation in the
   reduced OP/DT quotient, the Igusa `s`-variable is elliptic degree, and
   wrapped-sector anchors use `Pic^0(E)\cong E`.

## Forbidden inferences

1. `Den_{\Delta_5,E}` or `Den^{alg}_{\Delta_5,C,L}` does not imply a
   compact BPS Hilbert space, Hall algebra, chiral source, or protected
   integration functor.

2. `\overline\Pi_{X,*}\mathfrak g_{\Delta_5,L}\cong\mathfrak g_{\Delta_5}`
   is a regrading identity. It is not a compact realization theorem.

3. A linear lift `L` is not canonical. It is also not a section of the
   quadratic map `\Pi_X`. The whole point is that `s_L`, not `L`, becomes
   monoidal after normal ordering.

4. Pointwise formal primitive lifts of Gram triples do not give a linear
   lift, algebraic/effective Hall support, nonempty compact moduli, or
   duality-compatible source.

5. Curve-universality of `Den^{alg}_{\Delta_5,C,L}` does not produce a
   `K3\times C` OP/DT theorem. The OP scalar square and quotient theory
   are elliptic-specific.

6. The target bar-cobar counit
   `\Omega_C^{ch}\bar B_C^{ch}(Den^{alg}_{\Delta_5,C,L})\to Den^{alg}_{\Delta_5,C,L}`
   cannot define the compact source coalgebra `C_X`.

7. The denominator theorem fixes signed root supermultiplicities and the
   Weyl-Kac-Borcherds denominator. It does not fix compact Hall structure
   constants, parity lifts, orientation monodromy, Pfaffian torsors, or
   radical quotients.

8. The formal product `\Delta_5` does not prove the automorphic
   reflection character is the geometric orientation character. The OP
   constant `-4096` is also not an orientation character.

9. A formal algebraic Pfaffian block is not an analytic Dirac operator
   and not a compact first-order protected operator unless the source
   finite-dimensional complexes, pairing, skew-adjointness, and Pfaffian
   line are constructed.

10. The zero-degree Cartan part of the BKM algebra must not be included
    blindly in the positive-root determinant product.

## Required definitions and notation

1. `\Gamma_X^{form}`: formal full-Mukai dyonic lattice
   `\Lambda_S\oplus\Lambda_S`. Avoid calling it genuinely physical except
   as legacy notation.

2. `\Gamma_{gram}`: `\mathbb Z^3`, with elements
   `\gamma=(n,l,m)`.

3. `\Pi_X` and `B`: quadratic Gram map and its bilinear polarization
   defect.

4. `\widehat\Gamma_X`: the normal-ordered extension with product
   `\star`; this is the actual upstairs grading group for the algebraic
   lift.

5. `\overline\Pi_X`: additive normal-ordered Gram map.

6. `L`: a chosen element of
   `Hom_{\mathbb Z}(\Gamma_{gram},\Gamma_X^{form})`. It is a choice, not
   a canonical construction.

7. `s_L`: the monoidal normal-ordered section
   `s_L(\gamma)=(L\gamma,\Pi_X(L\gamma)-\gamma)`.

8. `\mathfrak g_{\Delta_5}`: the imported Gritsenko-Nikulin denominator
   BKM superalgebra, graded by `\gamma` through
   `\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}`.

9. `\mathfrak g_{\Delta_5,L}`: the `\widehat\Gamma_X`-graded regraded
   copy of `\mathfrak g_{\Delta_5}` supported on `s_L(\Gamma_{gram})`.

10. `Cur_C`: current Lie-* algebra on an arbitrary smooth curve `C`;
    left/right `D`-module convention must be fixed once.

11. `Den^{alg}_{\Delta_5,C}` and `Den^{alg}_{\Delta_5,C,L}`: formal
    target current envelopes.

12. `D^{alg}_{\Delta_5,C,L}`: only if introduced as a formal algebraic
    package. It must not be named `D_X` and must not be confused with a
    compact Dirac-Igusa source.

13. `C=E`: elliptic specialization for the compact `K3\times E` source,
    not part of the formal current envelope.

## main.tex anchors

1. Normal-ordered lattice setup:
   `main.tex:4312-4381` defines `\Gamma_X^{form}`, `\Pi_X`, `B`,
   `\widehat\Gamma_X`, `\star`, and `\overline\Pi_X`.

2. Formal primitive lift, not support:
   `main.tex:4523-4587` proves every Gram triple has a primitive saturated
   formal lift, then says this does not prove algebraicity, effectivity,
   compact moduli, or functorial Hall compatibility.

3. Central extension theorem:
   `main.tex:4590-4805` proves additivity defect, cocycle, star
   associativity, additivity of `\overline\Pi_X`, and the absence of a
   linear trivialization of `B`.

4. Denominator algebra import:
   `main.tex:5560-5702` defines/imports `\mathcal A_{den}` and states the
   Gritsenko-Nikulin denominator identity.

5. Current formal envelope:
   `main.tex:5704-5768` defines
   `\mathsf{Den}_{\Delta_5,E}` over `E` and says compact
   `E_3`/Hall/chiral realization needs more input.

6. Target-internal bar-cobar:
   `main.tex:6404-6503` proves the target bar-cobar counit is internal to
   the imported current envelope and cannot define the compact source
   coalgebra.

7. Conditional normal-ordering source theorem:
   `main.tex:8603-8661` begins the conditional Hall descent certificate,
   explicitly limiting the source to supplied compact data.

8. D0 certificate:
   `main.tex:9973-10270` defines a first-order compact certificate, not a
   source-free algebraic target.

9. Source-to-target comparison:
   `main.tex:10442-10496` states the source object is supplied first and
   the arrow points source-to-target.

10. Conditional first-order object:
    `main.tex:10592-10622` defines `\mathfrak D_X` only as conditional
    finite-stage compact data, not as `D^{alg}_{\Delta_5,C,L}`.

11. Status ledger:
    `main.tex:11518-11661` says target objects are imported and compact
    source construction remains open.

12. Compact realization certificate:
    `main.tex:11750-11796` defines `\mathfrak K_X` as data whose
    construction would turn `\mathcal D_X=\Delta_5` into a compact
    realization.

13. Open compact source:
    `main.tex:13276-13414` lists the source-side construction of `D_0` and
    the full certificate as open.

14. Summary separation:
    `main.tex:14062-14109` says the normal-ordered charge extension is a
    degree-level bridge and the denominator theorem does not determine
    compact Hall constants or microscopic brackets.

15. Eight formal current rows:
    `main.tex:15323-15395` shows the manuscript already knows how to build
    formal current/product objects, but currently still pins them to `E`.

## Patch queue

1. Rename the existing formal target:
   replace displayed `\mathsf{Den}_{\Delta_5,E}` definition with
   `Den^{alg}_{\Delta_5,E}` or `CurEnv_E(\mathfrak g_{\Delta_5})`, keeping
   an alias only if needed for backward references.

2. Generalize the formal envelope definition from `E` to arbitrary smooth
   `C`. Then specialize to `C=E` at the compact source boundary.

3. Insert the linear-lift theorem:
   define `L`, define `s_L`, prove monoidality, define
   `\mathfrak g_{\Delta_5,L}`, prove pushforward to the GN algebra.

4. Insert the lifted curve-current theorem:
   define `Den^{alg}_{\Delta_5,C,L}` and prove pushforward to
   `Den^{alg}_{\Delta_5,C}`.

5. Define `D^{alg}_{\Delta_5,C,L}` as an algebraic target package only.
   Do not call it compact, protected, geometric, or physical.

6. Add a short "dependence on `L`" paragraph:
   `L=0` is allowed but physically trivial upstairs; two lifts differ by
   a homomorphism `\Gamma_{gram}\to\Gamma_X^{form}`; no gauge equivalence
   is asserted until an action groupoid is defined.

7. Add the elliptic specialization paragraph:
   `C=E` is forced only for `K3\times E` compact source geometry,
   translation quotient, elliptic degree, and wrapped anchors.

8. Keep the compact realization section as source-side open work. Do not
   let the new `D^{alg}` target erase the existing source/target
   separation.

9. Move any algebraic Dirac/Pfaffian formula behind a formal determinant
   definition with finite windows, positive chamber, Cartan exclusion,
   completion, and normalization.

10. Add a forbidden-implications table near the section opening:
    `D^{alg}` does not imply `D_X`; target current envelope does not imply
    compact source; `\Delta_5^2` does not imply orientation character;
    denominator theorem does not imply Hall bracket constants.

## Residual mathematical checks

1. Check `U_C^{ch}` against infinite-dimensional/ind Lie superalgebras:
   the manuscript must state the completed ind category and finite
   homogeneous root-space condition used by BD/Kac.

2. Check that regrading and chiral enveloping commute:
   prove `\overline\Pi_{X,*}U_C^{ch}(Cur_C(g_L))\cong
   U_C^{ch}(Cur_C(\overline\Pi_{X,*}g_L))` in the chosen graded completed
   category.

3. Check the D-module convention:
   left convention uses `\mathcal O_C`, right convention uses `\omega_C`.
   Do not mix them in one theorem.

4. Check zero-degree Cartan handling:
   `\mathfrak g_{\Delta_5,0}` is Cartan; the determinant product is over
   positive roots/effective support, not over the full current algebra.

5. Check `2Z` versus `Z` normalization:
   the GN denominator is `64^{-1}\Delta_5(2Z)`, while the cusp product for
   `\Delta_5(Z)` carries the leading coefficient `64`. The algebraic
   Pfaffian statement must say exactly which variable convention it uses.

6. Check parity:
   signed superdimension is not the same as full parity dimension. If the
   formal algebraic target uses actual GN root spaces, say so. If it uses a
   Grothendieck representative, say it is a virtual product object.

7. Check the formal Pfaffian block:
   a displayed matrix such as `[[0,1-x_gamma],[1,0]]` does not by itself
   define a skew-adjoint odd Dirac operator or Pfaffian line. It is a
   determinant emulator until the coefficient algebra, pairing, parity, and
   Berezinian/Pfaffian convention are fixed.

8. Check `L` functoriality:
   arbitrary `L` is not Weyl-equivariant, not duality-equivariant, and not
   geometric. If equivariance is desired, it is a new condition.

9. Check curve assumptions:
   formal BD current envelopes work on smooth curves; compact source
   statements require smooth projective elliptic `E` with chosen origin.

10. Check source-free use of `\Lambda_S`:
    the algebraic lift uses the abstract K3 Mukai lattice as a label
    lattice. It does not use a moduli stack of `S` and does not prove
    nonempty objects on `S\times E`.

11. Check source coalgebra language:
    `\bar B_C^{ch}(Den^{alg}_{\Delta_5,C,L})` is target-internal. The
    compact `C_X` must be constructed independently from the source
    factorization/Hall object.

12. Check that the new construction does not delete the open problem:
    the compact theorem remains a comparison from a source object to
    `D^{alg}_{\Delta_5,E,L}` after protected integration, primitive
    pushforward, radical quotient, PBW/no-extra-relations, and Pfaffian
    trivialization.
