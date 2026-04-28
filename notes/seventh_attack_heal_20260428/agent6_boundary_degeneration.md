# Agent 6 — Boundary and Degeneration Attack
**Date:** 2026-04-28
**Evidence Standard:** Explicit limit computations or named compactification required; "naturally extends" disqualified.

---

## Stable Points (Passed)

### A7-6-01: m=0 Sector Naming
**Claim:** The m=0 sector (V_cusp) carries Weyl/cusp boundary factors, not one-particle states.
**Finding:** PASSED. The manuscript states clearly:
- "The m=0 sector is a cusp/Weyl boundary package carrying the repeated boundary indices f(0,l). Neither sector is a microscopic one-particle Hilbert space."
- Distinction V = V_bulk ⊕ V_cusp is theorem-level (lines 698-712 of main.tex).
- The K₀-determinant definition explicitly notes the m=0 terms contribute only to signed superdimensions via DMVV.

**Evidence:** lines 690-735 main.tex, Definition "Normalized K₀-determinant"

---

### A7-6-02: Active Support Γ_eff Definition
**Claim:** The active-support semigroup Γ_eff is well-defined in the cusp-polarized chamber.
**Finding:** PASSED. Lemma "Active support gives the type-II chamber cone" (lines 4916-4970) proves:
- Γ_eff is cusp-positive with boundary cases (n+m-l ≥ 0).
- The weak modular form f(nm,l) has nonzero support only on this cone.
- The Borcherds cone Cone_Borch = R≥0(δ₁ + δ₂ + δ₃) is correctly matched.

**Evidence:** lines 4916-4970 main.tex; Lemma "Active support and Borcherds cone"

---

### A7-6-03: Gram Cocycle B(c,c') Symmetry
**Claim:** B is a symmetric 2-cocycle with B(c,c) = 2Π_X(c) polarization.
**Finding:** PASSED. Lemma "Symmetric bilinear 2-cocycle..." is a full proof:
- δB = 0 is computed explicitly.
- B(c,c) = 2Π_X(c) follows from expanding (Q+Q)²/2, (Q+Q)·(P+P), (P+P)²/2.
- The central extension Γ_X = Γ_X^phys ⊕_B Γ_gram is associative on the nose.

**Evidence:** lines 4175-4240 main.tex (lattice section)

---

### A7-6-04: Primitive Lift Existence
**Claim:** Every Gram triple (n,l,m) ∈ Z³ lifts to a primitive charge c=(Q,P) ∈ Λ_S ⊕ Λ_S.
**Finding:** PASSED. Lemma "Primitive lift of every Gram triple" gives explicit construction:
- Q = e₁ + nf₁, P = lf₁ + e₂ + mf₂ on two orthogonal hyperbolic planes.
- Primitivity is verified via a 2×2 determinant = 1.
- Does NOT claim this solves Hall functoriality or multi-component closure.

**Evidence:** lines 4055-4130 main.tex

---

## Attacks (Failed or Conditional)

### A7-6-05: m=0 Sector DMVV Realization — ATTACKED
**Question:** Does the manuscript prove that V_bulk = DMVV second-quantized K3 elliptic genus, and V_cusp is Borcherds boundary correction?

**Claim in MS:** "The m>0 sector is the K₀-level virtual half of the DMVV product... obtained by replacing Z_K3 = 2φ₀,₁ by φ₀,₁." (line 705)

**Attack:**
- The DMVV formula gives the second-quantized numerator for K3 elliptic genus as 2φ₀,₁.
- Dividing by 2 gives φ₀,₁ and a K₀ superdimension vector with exponents f(nm,l).
- **Missing:** Proof that this is *the* physical Hecke algebra representation, not just a K₀ shadow.
- The m=0 terms f(0,l) are imported from the Gritsenko-Nikulin automorphic product, not derived from BPS physics.
- No statement of how the Borcherds product boundary correction (the additive constants m(a), τ(a) in GN) aligns with the m=0 sector. Are they the same mechanism?

**Residual:** The m=0 sector is correctly named as boundary, but its **physical identification** (whether it represents wrapped sectors, wall crossings, or degenerate D-brane configurations) is not justified. The BKM denominator supplies the target; compact realization is open (line 110 of status).

**Evidence:** Lines 698-735, 2075-2240 (cusp form section); no reference to wrapped D0-branes at m=0.

---

### A7-6-06: s=0 Wall (Weyl Chamber Cusp) — NOT ATTACKED IN MS
**Question:** The cusp of the Sp₄(Z) fundamental domain occurs at the s=0 limit. What happens there?

**Claim in MS:** The s=0 cusp is implied in the Weyl-chamber definition but never explicitly discussed as a limit or boundary phenomenon.

**Attack:**
- The Maass character ν_Δ₅ is defined on type-II walls (s=0 walls, where δ₁, δ₃ occur at m=0).
- The manuscript proves the reflection signs at these walls (Lemma "Conditional Pfaffian signs...", line 1525).
- **Missing:** What does the compact Hall structure do as s→0? Does projection-finite locality survive? Is the wrapped sector singular there?
- The Igusa fundamental domain has a finite boundary at s=0; modular forms on this domain have expansions at this cusp. The manuscript does not verify that the Borcherds product's expansion at the s=0 cusp matches the compact Hall boundary behavior.

**Residual:** The s=0 wall is topologically present but physically unanalyzed. No degeneration limit computation.

**Evidence:** Line 4790 mentions "walls" but does not address the s=0 cusp boundary as a separate degeneration.

---

### A7-6-07: Imprimitive Curve Classes — ATTACKED
**Question:** The OP/DT count uses primitive K3 curve classes β only. Imprimitive classes (β = dβ', d>1) are in the Mukai lattice but not in OP scope. Does the architecture handle this?

**Claim in MS:** Not directly stated. The Mukai lattice Λ_S = H(K3,Z) contains all integral vectors.

**Attack:**
- The primitive-lift lemma supplies (Q,P) for any (n,l,m), but does not specify primitive vs. imprimitive K3 classes.
- If β is imprimitive, β² = 2(dh-1) is not of the form 2(h'-1) for any h' ∈ Z; the lift Q = e₁ + nf₁ still works algebraically, but which curve geometry does it represent?
- Bryan-Oberdieck-Pixton's OP/DT invariants count primitive classes only. The manuscript does not prove that the normal-ordered descent **eliminates** imprimitive contributions or maps them to primitive roots.
- Alternatively, if imprimitive classes are present in the Hall category, the Hall product on multi-component imprimitive charges must be verified.

**Residual:** The Gram triple (n,l,m) is invariant under (Q,P) rescalings; the manuscript does not identify which K3 curves appear in the compact category or how imprimitive classes decouple. This is **not an error** (the architecture is clear that this is open), but it is unresolved.

**Evidence:** Lines 4055-4130 (primitive lift); no explicit discussion of imprimitive curve degeneracies.

---

### A7-6-08: Singular K3 (A₁ Limit) — NOT ADDRESSED
**Question:** If K3 develops an A₁ singularity, the Mukai lattice changes (a (-2)-curve degenerates). Does the compact Hall realization extend?

**Claim in MS:** Assume S is a smooth K3.

**Attack:**
- The Bridgeland stability condition on D(K3×E) has discontinuities as K3 degenerates.
- The manuscript assumes Λ_S is fixed; no degeneration analysis of the lattice structure or orientation line appears.
- The hybrid wrapped factorization is defined for a *fixed* K3×E, not as an inverse limit over deformations or compactifications.

**Residual:** This is **open** by design (item 1 of "Still Open Mathematics" in status), but the manuscript does not even state a conjecture about singular limits.

---

### A7-6-09: Nodal E (Elliptic Degeneration) — PARTIALLY ADDRESSED
**Question:** At the nodal cubic limit of E, the factorization algebra structure on Ran(E) changes. Does the hybrid object extend?

**Claim in MS:** "The hybrid object now has ordered two-sided local/wrapped correspondences..." (line 42 of status).

**Attack:**
- Ran(E) is defined for smooth E. The nodal limit has two components: one smooth P¹ and one rational normal curve of degree 1 (a nodal point).
- The chiral algebra structure on Ran(smooth E) depends on translation-invariance. At the node, translation fails.
- Lemma "E-equivariant descent of the orientation line" (mentioned in fatal repairs) computes cohomology of BE; does this extend to singular E?
- The manuscript does not address the nodal limit explicitly.

**Residual:** The wrapped sector is tied to smooth E. **Degeneration to nodal E is not covered.** This is acceptable if stated as an open boundary.

---

### A7-6-10: Wall-of-Marginal-Stability (BPS Splitting) — FORMALIZED BUT UNCHECKED
**Question:** On a wall where a BPS state γ splits into γ₁ + γ₂, the Hall algebra changes by a Kontsevich-Soibelman factor. Does the compact construction handle the wall itself (not just across it)?

**Claim in MS:** "The ordinary projection-finite Ran object cannot supply the wall object..." (line 6983 main.tex, Proposition "(O2)/hybrid compatibility").

**Attack:**
- The manuscript treats walls as *charts* in the type-II Pfaffian wall certificate (Definition, line 840).
- The certificate requires a *generic point* on the wall, with tangent and normal splitting.
- On the wall *itself*, charges are marginal: γ and γ₁+γ₂ are both semistable. The Hall product is discontinuous in the stability parameter.
- The manuscript does not prove that the finite HN quotient at a fixed height R *stabilizes* the wall product. The residuals 𝔬^wall_δᵢ,R must vanish, but computing this requires the full geometric construction (which is open).

**Residual:** The wall-transport obstruction is named (Corollary "Semidirect wall-transport obstruction", line 1955) but not verified. The manuscript correctly flags this as needing the local Pfaffian model (O2) and the hybrid factorization object—both open.

**Evidence:** Lines 1955-2040, 6850-7050 (wall compatibility); flagged as open in line 121 of status ("Prove the Pfaffian local model (O2)...").

---

### A7-6-11: Multi-Component Charges — DEFERRED
**Question:** A charge c = (Q,P) ∈ Λ_S ⊕ Λ_S can have nonzero Q in one component and nonzero P in another. Do Hall products factor as tensor products locally?

**Claim in MS:** Not explicitly addressed.

**Attack:**
- If c₁ = (Q₁, 0) and c₂ = (0, P₂), then B(c₁, c₂) = (Q₁ · 0, Q₁ · P₂ + 0 · 0, 0 · P₂) = (0, Q₁ · P₂, 0).
- The Gram degree is purely in the middle component.
- For independent tensor factors (Q,P) ∈ Λ_S ⊕ Λ_S, the Hall bracket should respect this splitting.
- **Not proven:** The compact Hall category respects the component structure, i.e., extensions between (Q₁,0)-objects and (0,P₂)-objects have the claimed form.

**Residual:** No contradiction found, but no positive confirmation either. This is subsumed in the open hybrid-factorization problem.

---

### A7-6-12: (n,l,m) Additive Charge Confusion — ROOT CAUSE IDENTIFIED
**Question:** Is (n,l,m) an additive charge lattice or a Fourier/root invariant?

**Claim in MS:** "The map Π_X is an invariant map to Fourier/root degrees; it is not the Hall charge lattice." (Definition, line 4095)

**Attack (from attack whitepaper):**
- If (Q,P) ↦ (n,l,m) is the Gram map, then for two charges (Q₁+Q₂, P₁+P₂), we have
  ```
  (Q₁+Q₂)²/2 = Q₁²/2 + Q₂²/2 + Q₁·Q₂
  ```
  which is NOT additive in (n,l,m) unless Q₁·Q₂ = 0.
- The manuscript uses (n,l,m) as both:
  1. Fourier exponents in the Borcherds product (additive in the exponent).
  2. Gram invariants of physical charges (nonadditive).
  3. Root degrees in the BKM algebra 𝔤_Δ₅ (additive in the root lattice).

**Verdict:** The manuscript **correctly separates** Γ^phys (additive) from Γ_gram (nonadditive invariant) in the definition section. The normal-ordered extension Γ_X = Γ_X^phys ⊕_B Γ_gram ensures the physical charges add while the Gram shadow is corrected by the cocycle B.

**But:** The compact Hall category is indexed by (n,l,m), which requires a **proof** that the Hall product descends through Π_X. This is the "normal-ordered descent of the protected bracket" problem (line 7008 main.tex, Open Problem).

**Residual:** NOT AN ERROR, but the logical gap is confirmed: the Hall grading by (n,l,m) is not yet constructed, only the formal Gram/cocycle machinery.

---

## Healings

### H7-6-01: m=0 Sector as Non-Microscopic States
The manuscript's distinction V_bulk ⊕ V_cusp is sound. The cusp sector carries boundary and finite-system corrections (DMVV half + Borcherds regularization), not one-particle Hilbert space. **No repair needed.** This is correctly stated.

### H7-6-02: Active Support Γ_eff Boundary Cases
The active-support lemma correctly computes the Borcherds cone and boundary (n+m-l ≥ 0). The f(0,l) terms are explicitly boundary. **No repair needed.**

### H7-6-03: s=0 Wall as Open Question
Add a remark to Section "The Weyl chamber and the Weyl vector": "The s=0 cusp of Sp₄(Z) corresponds to the walls δ₁, δ₃ where m=0. The compact Hall behavior at this boundary is analyzed via the Pfaffian wall certificate (Open Problem (O2)) and the wrapped factorization (Open Problem on line ###)."

### H7-6-04: Nodal E Boundary Explicitly Stated as Open
Add to the "Compact Dirac-Igusa Realization Problem" section: "The hybrid wrapped factorization is defined for smooth E. Extension to singular limits (nodal E, cuspidal degeneration) is a separate degeneration-stability problem, not addressed here."

### H7-6-05: Imprimitive Classes Explicitly Deferred
In the primitive-lift lemma section, add: "The primitive-lift lemma shows that every Gram triple (n,l,m) has a lift to Λ_S ⊕ Λ_S. For imprimitive K3 curve classes (β = dβ', d>1), the lift is not unique up to scaling. The Hall category's treatment of imprimitive curves (whether they decouple or contribute to wall-crossing) remains open and is part of the compact realization problem."

---

## Residuals (Not Fixable Without New Mathematics)

### R7-6-01: Compact Hall Descent of the Bracket (Open Problem, Line 7008)
The normal-ordered map Π̄_X : Γ_X → Γ_gram is a homomorphism of groups, but the Hall bracket on Γ_X^phys must be **lifted and descended** to the Gram lattice while respecting the cocycle correction. This requires the full hybrid factorization construction. **Status: Open.**

### R7-6-02: Weyl-Equivariant Orientation Cocycle (Open Problem, Line 589)
The Maass character ν_Δ₅ provides the *target* reflection signs on type-II walls. A compact Hall orientation line must transport with these signs; this requires the Pfaffian local model (O2) and the full orientation-line monodromy computation. **Status: Open; Lemma "Weyl-equivariant orientation cocycle" is pure group theory, not geometric.**

### R7-6-03: Projection-Finite Ran Cannot Reach δ₂ Wall (Line 6952)
The δ₂ wall has m=1 (positive elliptic degree). Lemma "Projection-E-support locality obstruction" shows that finite-point Ran sectors have m=0 only. The wrapped prequotient + rigidified mixed correspondences + protected integration are necessary but **not yet constructed.** **Status: Open.**

### R7-6-04: Nodal E and Singular K3 Limits
The architecture does not extend to degenerations. This is acceptable but must be stated clearly. **Recommendation: Add to introduction: "We assume S smooth K3 and E smooth elliptic curve throughout; degenerate limits are not addressed."**

---

## Summary Score

| ID | Category | Verdict |
|---|---|---|
| A7-6-01 to A7-6-04 | Stable lattice/cocycle theorems | **PASS** ✓ |
| A7-6-05 | DMVV realization of m=0 | **PARTIAL** (named correctly, physical ID open) |
| A7-6-06 | s=0 cusp boundary | **UNANALYZED** (openly) |
| A7-6-07 | Imprimitive classes | **DEFERRED** (correctly) |
| A7-6-08 | Singular K3 limits | **OPEN** (by design) |
| A7-6-09 | Nodal E limits | **OPEN** (by design) |
| A7-6-10 | Wall-of-marginal-stability | **FORMALLY SKETCHED** (residual: compute (O2)) |
| A7-6-11 | Multi-component charges | **DEFERRED** (in open problem) |
| A7-6-12 | (n,l,m) additivity | **CORRECTLY SEPARATED** (Γ^phys vs Γ_gram) |

---

**Conclusion:** The boundary/degeneration attack finds no false theorems. The manuscript correctly separates proved/imported theorems (lattice cocycle, Borcherds product) from open problems (compact Hall realization, Pfaffian local models, orientation monodromy). The architecture is **honest about its boundaries.**

The principal residual is the **compact Hall descent**, which requires explicit geometric construction of the hybrid factorization and the type-II Pfaffian wall models—tasks flagged as open in the status document.
