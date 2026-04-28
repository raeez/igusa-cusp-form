# Ginzburg / Borel-Moore Homology Attack: Hall Product & Coproduct

**Date:** 2026-04-28
**Agent ID:** A7-4
**Adversarial Lens:** Chriss-Ginzburg (BM homology, perverse sheaves on convolution algebras) + Joyce (vanishing-cycle coefficients, Hall algebra structure)
**Target:** Hall product `μ_R = q_! ∘ TS_R ∘ p^*` and coproduct via Borel-Moore homology with vanishing-cycle coefficients on moduli of compact B-branes.

---

## Stable Points (No Attack Required)

1. **Gram Cocycle & Extension Lattice** (Reconstitution §C): The symmetric bilinear cocycle `B(c,c') = (Q·Q', Q·P'+ Q'·P, P·P')` satisfies `δB = 0` and `Γ_X = Γ_X^{phys} ⊕_B Γ_{gram}` is proven as a central extension. This is lattice-level and sound.

2. **Normal-Ordered Descent Map** (§C, main.tex:7333–7400): The map `π̄_X(c,T) = Π(c) - T` is proven to be a homomorphism on the central extension. This is algebra.

3. **No-Go for Raw Descent** (Reconstitution §E): Theorem states raw functorial pushforward along `Π: Γ_X^{phys} → Γ_{gram}` cannot realize full BKM bracket because `B(c_i,c_i) = 2Π(c_i) ≠ 0` forces self-interactions. Logically sound.

4. **Imported Automorphic Denominator** (Gritsenko–Nikulin 2012): The Borcherds product identity and supermultiplicities `smult α(n,l,m) = f(nm,l)` are external theorems. Not attacked here.

---

## Attacks (Ginzburg-Lens Critical Gaps)

### **A7-4-01: Properness of Source/Target Maps on Extension Stack**

**Claim (main.tex:6359–6361, 6410–6451):**
The Hall product is defined as `μ_R^• = q_! ∘ TS_{R}^• ∘ p^*` where:
- `p: ℰ_{R,c,c'} → M_{R,c} × M_{R,c'}` is the source map (sends extension to input pair)
- `q: ℰ_{R,c,c'} → M_{R,c⊕c'}` is the target map (sends extension to direct sum)

**Evidence of vulnerability:**
- **Line 6359–6361:** Manuscript states "proper-support or compact-support witnesses for q, admissibility witnesses for p^* and q_! on the chosen vanishing-cycle/Borel–Moore theory."
- **Line 6453:** "This functor is defined only after the properness/admissibility defects above vanish."
- **Defect objects listed (lines 6366–6376):** `𝔬^{prop}_{e,R}`, `𝔬^{adm}_{e,R}`, `𝔬^{TS}_{e,R}` — these are *defects*, not vanishing statements.

**Attack:** For Borel-Moore homology, `q_!` (proper pushforward) requires `q` to be proper; `p^*` (smooth pullback) requires `p` to be smooth or `p` proper with base-change hypothesis. On the extension stack ℰ_{R,c,c'} over moduli of finite-type stacks (B-brane objects with HN-filtered charges), properness fails generically:
- An extension `A' ↪ A ↠ A''` can slide continuously within the extension space as the "internal charge" redistributes.
- The fiber dimension of `p` (the space of extensions with fixed inputs) is often infinite-dimensional in the derived setting (infinite-dimensional Ext groups).
- Limiting to *semistable* extensions (Harder–Narasimhan truncation) restores properness of a *smaller* moduli, but the manuscript does not prove the finite-stage Hall product `μ_R` lands in semistable objects — it only asserts height≤R truncation.

**Exact failure mode:**
If `p` or `q` are not proper on ℰ_R,c,c', then `q_!` is not a well-defined functor on the derived category of coherent sheaves or perverse sheaves, and the composition `q_! ∘ TS ∘ p^*` is undefined. The manuscript names this defect `𝔬^{prop}_{e,R}` but does not supply a map making it vanish at finite stages.

**Evidence anchor:**
- Reconstitution, §B (line 199–200): "Remove every occurrence of 'fourfold'... K3×E is a Calabi–Yau threefold." (Correcting dimensional error, not resolving properness.)
- main.tex line 6777: "properness/admissibility after quotient" is asserted as a requirement, not proved.

---

### **A7-4-02: Thom-Sebastiani Transversality in Vanishing-Cycle Setting**

**Claim (main.tex:6361, 6518–6519):**
"The middle stacks classify exact triangles or exact sequences... with Thom-Sebastiani identifications for the coefficient systems."
"The equality is required after vanishing cycles, Thom–Sebastiani transport, orientation signs, and the quotient by height>R."

**Evidence of vulnerability:**
- **Defect object `𝔬^{TS}_{e,R}` (line 6368):** Named but not shown to vanish.
- **Manuscript fact:** Line 5518 (Thom-Sebastiani map TS): No explicit transversality hypothesis given for compact B-branes on K3×E with d-critical structure.

**Attack:** Thom-Sebastiani isomorphism `φ_f|_X ⊠ φ_g|_Y → φ_{f+g}|_{X×Y}` in vanishing cycles requires transversality of f and g along their critical loci. For Hall product:
- The critical locus is the support of the BPS sheaf.
- For extensions `A' ↪ A ↠ A''`, the obstruction to transversality (i.e., tangent-space non-transversality) lives in `Ext¹(A'', A') ⊠ Ext¹(A, A')`, the space of infinitesimal obstructions to smoothness of the extension.
- At generic extensions, TS holds. But at special extensions (including the BPS critical points), TS can *fail* — this is where the obstruction cocycle `B(c,c')` physically lives.

**Exact failure mode:**
The manuscript uses TS universally without proving transversality on ℰ_R at height R. If TS fails at a point of ℰ_R, then `q_! ∘ TS_{e,R} ∘ p^*` is not an isomorphism on vanishing cycles at that point, and the Hall product is not an honest morphism.

**Required evidence:**
The manuscript should prove: for every extension in ℰ_R,c,c', the obstruction to TS-transversality vanishes on the support of the vanishing-cycle sheaf. This is not done.

**Evidence anchor:**
- main.tex line 5510–5522: Perverse sheaf of vanishing cycles is named but its transversality properties are not stated.

---

### **A7-4-03: Multiplicative Orientation Transport (Open Obligation O1)**

**Claim (main.tex:6410–6451, combined with Orientation section):**
The Hall product `μ_R = q_! ∘ TS ∘ p^*` "transports orientation correctly."

**Evidence of vulnerability:**
- **Main.tex:** Architecture Realization Status (line 39): "Orientation now separates degree-two gerbe obstruction classes from degree-one finite-stabilizer linearization characters."
- **Reconstitution, §H (line 346–377):** Orientation character is stated as a *conditional* theorem: "If a compact orientation monodromy character ε_o: W^(2)(Λ^{2,1}_{II}) → {±1} exists and satisfies ε_o(s_{δ_i}) = -1, then ε_o = ν_{Δ_5}."
- **Status:** Open Obligation O1 (Orientation lane, architecture_realization_status.md line 39).

**Attack:** Joyce-Upmeier orientation on K3×E sheaf moduli requires:
1. A canonical Pfaffian line bundle `𝒰_c` on M_{R,c}.
2. Multiplicativity: `𝒰_{c⊕c'} ≃ 𝒰_c ⊗ 𝒰_{c'}` (after a Z/2-valued sign cocycle).

The Hall product is defined up to this sign cocycle. Without canonical orientation (O1 open), `μ_R` is defined only up to a Z/2 local system that can flip sign at non-generic extensions. This means:
- `μ_R` is not well-defined as a morphism of vector spaces; only up to sign.
- The coproduct Δ_R (which uses the opposite correspondence) inherits this ambiguity.
- The primitive subspace `P_R = ker(Δ_R - id⊗1 - 1⊗id)` is not a well-defined subspace, only defined up to sign choices on each generator.

**Exact failure mode:**
If O1 is not supplied, then `μ_R` and `Δ_R` are multivalued, and the primitive subspace is not an honest subobject.

**Evidence anchor:**
- Architecture status line 110: "Construct strong reduced orientation (O1) on the compact/wrapped sector" — *still open*.
- main.tex line 6785: "reduced Hall product after vanishing cycles, orientations, HN quotienting..." The word "orientations" suggests orientation data is a *requirement*, not a *derived consequence*.

---

### **A7-4-04: Infinite-Dimensional Fibers of Source Map p**

**Claim (main.tex:6448–6451, definition of ℰ):**
`ℰ_{c,c'} = {(A',A'') : A' ∈ M_c, A'' ∈ M_{c'}, ∃ A ∈ M_{c⊕c'} with A' ↪ A ↠ A''}`
The source map `p: ℰ_{c,c'} → M_c × M_{c'}` sends extension to input pair.

**Attack:** For derived moduli of perfect complexes or sheaves on K3×E, the fiber of p over a fixed pair (A', A'') is the "extension space" `Ext¹(A'', A')` modulo gauge equivalence. In the derived setting, this can be infinite-dimensional (e.g., Ext¹ can be non-zero in infinitely many degrees if A' and A'' are not sheaves but complexes). For `p_!` (proper pushforward along p) to be defined, the fibers must be finite-dimensional or carry a compactification. The manuscript does not address this.

**Evidence anchor:**
- main.tex line 5631: "Source chiral object. ... Its b_R > 0 part is present only through the rigidified wrapped prequotient."  The need for "rigidification" suggests the extension space is too large without auxiliary data.

**Evidence of vulnerability:**
- Coproduct definition (line 5664–5678) requires a "collision coproduct" which is built from pull-push on extension stacks. If fibers of p are infinite-dimensional, this construction is not standard.

---

### **A7-4-05: Coproduct via Opposite Correspondence (Properness of p)**

**Claim (main.tex, inferred from structure):**
By analogy with Hall algebra, the coproduct should be defined via the opposite correspondence:
`Δ_R = p_! ∘ TS^{-1} ∘ q^*`
where `(q, p)` are reversed in role (q is input, p is output).

**Attack:** This formula requires `p_!` (proper pushforward along p). But p is the source map of the extension stack, which sends an extension to its input pair (A', A''). The fibers of p are extensions, which can be infinite-dimensional (attack A7-4-04). Without finite-dimensionality, `p_!` does not exist in standard derived categories.

**Evidence anchor:**
- main.tex line 5665–5678: The "chiral coproduct Δ_R^{ch}" is defined as "collision coproduct attached to the finite Hall/factorization correspondences" via "a finite pull-push construction on the collision correspondence before Q_{E,R}." The term "collision coproduct" is non-standard; it is not clear whether this avoids the properness issue.

**Exact failure mode:**
If `p_!` does not exist, then either:
1. The coproduct is not defined as a pull-push; or
2. There is a non-obvious compactification or finiteness argument that is not stated.

---

### **A7-4-06: Primitive Subspace as Kernel of Difference in Specific Category**

**Claim (Architecture Realization Status line 23–24, and implicit in main.tex):**
`P_R = ker(Δ_R - id⊗1 - 1⊗id)` is the primitive subspace.

**Attack:** This kernel is defined in a specific abelian or stable ∞-category. The manuscript does not specify:
1. Are primitives computed in super-vector spaces over ℂ (graded modules)? Or in the derived category?
2. Is the kernel strict or up to homotopy?
3. After the quotient Q_{E,R}, are primitives still well-defined, or are they only defined up to the radical of the Hopf pairing?

If Δ_R is defined in a stable ∞-category (derived Hall algebra), then primitives are computed up to homotopy coherence, not as a strict kernel. This weakens the claim that P_R is a Lie subalgebra under the bracket [x,y] = μ_R(x,y) - (-1)^{|x||y|} μ_R(y,x).

**Evidence anchor:**
- main.tex line 5663: "Its reduced iterated coproduct is nilpotent on each finite stage." This suggests the coproduct is not strictly coassociative, only eventually.

---

### **A7-4-07: Closed Hopf-Pairing Radical is Coideal (NO7)**

**Claim (Architecture Status line 47, NO7):**
The radical of the Hopf pairing is a Lie ideal AND a coideal.

**Attack:** For a bialgebra or Hopf algebra, the radical of a pairing is a Lie ideal if [Rad, P] ⊆ Rad, and a coideal if Δ(Rad) ⊆ Rad ⊗ H + H ⊗ Rad. The manuscript names this as a "closed Hopf-radical quotient" but does not supply explicit computations verifying both properties even at a finite stage.

**Required evidence:**
At least one small charge c (e.g., c = (0,0,0) or a simple root), verify:
1. [Rad_R ∩ P_R^c, P_R^{c+c'}] ⊆ Rad_R ∩ P_R^{c+c'};
2. Δ_R(Rad_R) ⊆ (Rad_R ⊗ H_R) + (H_R ⊗ Rad_R).

**Evidence anchor:**
- Architecture Status line 47: "the Hopf-radical quotient" is mentioned as a requirement for the Koszul comparison (def_hybrid_wrapped_factorization_certificate), but the manuscript does not compute Rad_R for any specific R.

---

### **A7-4-08: Order of Operations in Convolution (CoHA Convention Check)**

**Claim (main.tex line 6410):**
`μ_R^• = q_! ∘ TS_R^• ∘ p^*`

**Attack:** In Kontsevich-Soibelman CoHA (2011) and Davison-Meinhardt, the Hall product is:
- First pull back from M_c × M_{c'} to the extension stack ℰ via p^*,
- Then apply TS for vanishing-cycle coefficients,
- Then push down from ℰ to M_{c⊕c'} via q_!.

The manuscript's formula matches this *in writing*, but does not verify:
1. That TS acts on the pulled-back perverse sheaves (i.e., after p^*).
2. That the composition is natural with respect to Borel-Moore homology.
3. That the order respects the vanishing-cycle structure (TS should be applied *before* the push-forward q_!, not as a coefficient system after).

**Evidence anchor:**
- main.tex line 6518–6521: "The equality is required after vanishing cycles, Thom–Sebastiani transport, orientation signs, and the quotient by height>R. Equivalently, the two pull-push maps are induced by the same Borel–Moore class on the corresponding two-step flag stack."

The phrase "same Borel–Moore class" suggests the actual implementation is via a flag stack (filtration data), not the formula `q_! ∘ TS ∘ p^*` in the naive order. This raises the question: is TS being applied in the fiber or before the push? The manuscript is ambiguous.

---

## Healings (Conditional Fixes)

### **H7-4-01: Semistable Truncation Properness**

**Claim to heal:** "The maps p and q are proper."

**Conditional healing:**
Replace the extension stack ℰ_{R,c,c'} with the *semistable extension stack* ℰ_{R,c,c'}^{ss}, where an extension A' ↪ A ↠ A'' is included if:
- A' and A'' are σ-semistable in fixed Bridgeland stability.
- A is σ-semistable.
- The extension does not split.

Then `p` and `q` are proper maps on ℰ_{R,c,c'}^{ss}. This requires:
1. **Supply:** A fixed Bridgeland stability σ on Db(Coh(K3×E)).
2. **Verify:** That the semistable extension category is extension-closed (products of semistable extensions are semistable).
3. **Verify:** That the Hall product on semistable objects descends to a product on the quotient by the radical.

**Status:** No Bridgeland stability is specified in the manuscript. The architecture uses Harder-Narasimhan filtration (height ≤ R), but HN filtration and Bridgeland stability are distinct tools. Healing requires explicit stability choice.

---

### **H7-4-02: Transversality via d-Critical Structure**

**Claim to heal:** "Thom-Sebastiani holds on ℰ_R."

**Conditional healing:**
Supply a d-critical structure on the extension stack ℰ_R (in the sense of Joyce-Safronov / Brav-Bussi). The d-critical locus is the subset where the "obstruction space" Ext¹(A'', A') is tangentially transverse to the extension map. If the d-critical structure is supplied with a compatible orientation, then TS holds for vanishing cycles on ℰ_R at generic points.

**Status:** No d-critical structure is mentioned in the manuscript. The moduli M_{R,c} are introduced as stacks with HN truncation, not as d-critical varieties. Healing requires:
1. Specify a symmetric obstruction theory on ℰ_R (e.g., from sheaf Ext).
2. Prove the critical locus is the BPS locus.
3. Supply an orientation.

---

### **H7-4-03: Joyce-Upmeier Orientation O1**

**Claim to heal:** "μ_R is canonical (not up to sign)."

**Conditional healing:**
Invoke Joyce-Upmeier orientation on K3×E sheaf moduli (Joyce 2018). This supplies:
1. A canonical Pfaffian line bundle 𝒰_c → M_{R,c}^ss for each semistable chamber.
2. Multiplicative isomorphisms: 𝒰_{c⊕c'} ≃ 𝒰_c ⊠ 𝒰_{c'} ⊗ det(Ext¹(A'', A')) on the extension stack.
3. A canonical section of 𝒰_{c⊕c'} restricted to generic extensions.

This resolves O1 (orientation line) but requires:
- Semistable truncation (H7-4-01) to make the moduli smooth enough for Joyce-Upmeier to apply.
- Explicit choice of K3 polarization (implicit in "compact B-branes").

---

### **H7-4-04: Finite-Type Extension Stack via Wrapped Rigidification**

**Claim to heal:** "The fibers of p are finite-dimensional."

**Conditional healing:**
The architecture (main.tex line 6335–6395) introduces "rigidified wrapped charge stacks" with an anchor map:
`λ_{η,R}: ℰ_{η_1,η_2,R}^{wr} → E × E × E`

This anchor "remembers the relative position between the finite local supports U_i and the wrapped leg." If the anchor is required to be a finite étale cover or a closed immersion, then the fibers of the source/target maps are controlled (finite-dimensional).

**Status:** The anchor is defined (main.tex line 6386–6391) but its role in controlling fiber dimension is not made explicit. Healing requires stating: "The fibers of p are finite-dimensional because the extension stack is cut out by the anchor conditions and the Harder-Narasimhan height bound."

---

### **H7-4-05: Collision Coproduct as Separated Dual Hall Product**

**Claim to heal:** "The collision coproduct Δ_R^{ch} is well-defined."

**Conditional healing:**
Define Δ_R^{ch} not via the opposite correspondence (which requires proper push along p), but via the *deconcatenation* map on the hybrid correspondence category. For every correspondence generator `e = (X ←p ℰ →q Y)`, define:
- Input: an object in the hybrid object space at charge c⊕c'.
- Deconcatenation: restrict to the two-step extension stack where ℰ has a canonical filtration A' ↪ A (first input), A/A' ≃ A'' (second input).
- Output: tensor of the two input object spaces.

This avoids defining p_! and instead uses flag structures. The manuscript's term "collision coproduct" may refer to this. Healing requires stating this explicitly, not as a "collision" metaphor.

---

### **H7-4-06: Radical Quotient Verification (NO7)**

**Claim to heal:** "The Hopf-pairing radical is a Lie ideal and coideal."

**Conditional healing:**
Supply a finite computation:

1. At R=R_min (lowest height with nontrivial primitives), compute Rad_R explicitly on a basis of primitive generators at low degrees (e.g., degrees α(1,0,0), α(0,1,0), α(0,0,1), and products).
2. Verify [Rad_R, P_R] ⊆ Rad_R by checking bracket relations on this basis.
3. Verify Δ_R(Rad_R) ⊆ (Rad_R ⊗ H_R) + (H_R ⊗ Rad_R) by inspecting the coproduct on basis elements.

Such a computation would be self-contained and verify NO7 locally.

---

## Residuals (Unhealed After Conditionals)

### **R7-4-01: Global Multiplicativity of TS (Requires Nontrivial Proof)**

Even with H7-4-02 (d-critical structure), Thom-Sebastiani is a *local* isomorphism on the critical locus. Globalizing to an isomorphism on all of ℰ_R requires a nontrivial proof of compatibility with the extension-stack structure. The manuscript does not attempt this; it asserts TS "identifications for coefficient systems" (line 6361) without proof.

**Residual statement:** "TS is globally multiplicative on ℰ_{R,c,c'}" is an open mathematical claim.

---

### **R7-4-02: Compatibility of Normal-Ordered Descent with Hall Product**

After the Hall product μ_R is defined, the normal-ordered pushforward (Π̄)_* μ_R must land in Γ_{gram}-graded Lie algebras. For this to recover 𝔤_{Δ_5}, the degree-shift T = B(c,c') must appear as a grading shift in M_{R,c} = M^{ss}_{R,σ,c} × {T}. The manuscript assumes this {T}-factor is a *grading*, not a new brane charge. Proving this is an open task.

**Residual statement:** "The cocycle B(c,c') correctly normalizes the pushed-forward Hall product to give additive grading in Γ_{gram}" requires a comparison theorem between the Hall-product kernel on M_{R,c⊕c'} and the Gram-descendent primitives on the tensor product.

---

### **R7-4-03: Behrend-Weighted Euler Characteristic (Finite D0 Certificate)**

The OP/DT scalar count uses χ_B(M^{ss}_{R,c}) (Behrend-weighted Euler characteristic). For this to be defined on K3×E threefold, a Behrend cosection (orientation) must exist. Joyce-Upmeier orientation on the moduli of sheaves does supply a cosection, but only if M^{ss}_{R,c} is cut out by the semistable condition and has no singularities (or is computed in a virtual class sense).

**Residual statement:** "The Behrend-weighted count χ_B(M^{ss}_{R,c}) equals the signed virtual multiplicity" is open; it requires either:
- Proof that M^{ss}_{R,c} is smooth (false — semistable moduli have singularities), or
- Supply of a virtual class and proof that χ_B recovers the virtual count.

---

## Summary Table

| ID | Claim | Failure Mode | Severity | Healing Required | Status |
|---|---|---|---|---|---|
| A7-4-01 | `p, q` proper on ℰ | Fiber dimension ∞ | **Critical** | Semistable truncation (H7-4-01) | Open |
| A7-4-02 | TS transversal on ℰ | Obstruction to TS at singular extensions | **Critical** | d-critical structure (H7-4-02) | Open |
| A7-4-03 | μ_R canonical | Defined up to sign (O1 open) | **Critical** | Joyce-Upmeier orientation (H7-4-03) | Open |
| A7-4-04 | `p_!` well-defined | Infinite fiber of p | **Critical** | Anchor rigidification (H7-4-04) | Open |
| A7-4-05 | Coproduct via `p_!` | Same issue as A7-4-04 | **Critical** | Deconcatenation dual (H7-4-05) | Open |
| A7-4-06 | P_R strict subspace | Kernel computed in wrong category | **Medium** | Specify category (no healing path shown) | Open |
| A7-4-07 | Radical is coideal (NO7) | No verification at finite stage | **Medium** | Explicit computation (H7-4-06) | Open |
| A7-4-08 | CoHA formula correct | Order ambiguous (TS before/after push?) | **Medium** | Clarify flag vs. formula | Partial |

---

## Conclusion

The Hall product μ_R = q_! ∘ TS_R ∘ p^* and coproduct Δ_R rest on three unproven conditionals:
1. **Properness** of p, q on the extension stack (requires semistable truncation or finite-type control).
2. **Transversality** of TS (requires d-critical structure with orientation).
3. **Canonical orientation** on the moduli (requires O1, conditional on Joyce-Upmeier).

None of these are supplied in the current manuscript. The defects `𝔬^{prop}_{e,R}`, `𝔬^{adm}_{e,R}`, `𝔬^{TS}_{e,R}` are *named* but their vanishing is *claimed*, not *proved*. This is a structural gap, not a typo: the Hall algebra construction is premature.

The manuscript's strength is its clarity in separating the automorphic square root, the normal-ordered descent, and the compact realization as distinct problems. The weakness is the apparent formality of the Hall product definition — it reads as if the pull-push machinery is available, when in fact three fundamental obstacles block its execution.

**Recommendation for the manuscript:** Rewrite §6 (Hybrid Wrapped Factorization Certificate) to explicitly list properness, transversality, and orientation as *hypotheses* of the Dirac-Igusa certificate, not derived features. Then the theorem statement is correct: *if* these three data exist, *then* the Hall product is well-defined and the primitive recognition problem has a canonical form.
