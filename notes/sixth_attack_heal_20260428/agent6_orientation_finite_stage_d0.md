# Adversarial Review: Compact Dirac–Igusa Pro-Object Finitude and Orientation

**Date:** 2026-04-28
**Lens:** Boundary/finite-stage construction (does the inverse limit exist?) + Orientation/equivariant cohomology (E^{top} descent structure)
**Status:** Report mode (no commits).

---

## Stable Points (A6-6-01 through A6-6-04)

**A6-6-01: Lattice normal-ordering is proved solid.**
The manuscript correctly separates Γ_X^{phys}, Γ_gram, and the extension Γ_X = Γ_X^{phys} ⊕_B Γ_gram. The homomorphism π̄_X(c,T) = π_X(c) - T is additive and proved. No attack here.

**A6-6-02: Raw descent no-go is theorem-level.**
The claim that raw π_X descent cannot realize the full BKM bracket is correctly stated. The proof via B(c_i, c_i) = 2π_X(c_i) ≠ 0 is sound. This forces the B-corrected extension; no closure.

**A6-6-03: Orientation descent structure (connected vs. finite) is separated.**
The manuscript now correctly states H^1(BE; F_2) = 0 for connected E ≅ T^2, and distinguishes the connected descent from E[N] finite-stabilizer descent. Translation invariance is no longer claimed as sufficient; equivariant linearization is flagged as an open task. Honest framing.

**A6-6-04: Eight-word flag atlas is recorded finitely.**
The eight two-step words (LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW) are explicitly listed as generators of collision correspondences at finite stage R. The coassociativity and pentagon identities are stated as finite equalities. Not proved; but the statement is precise and testable.

---

## Major Attacks (A6-6-05 through A6-6-12)

### A6-6-05: Semistable moduli finite-type assumption is not proved for K3×E.

**The attack:**
Lemma prop:sectorial-hall-truncation (line 8589-8591 in main.tex) explicitly assumes "finite type of the semistable stacks in bounded h_S-height" as a hypothesis, not a conclusion. The lemma then deduces F_{σ,S}(R) and Γ_{σ,S}^{HN}(R) are finite **under this assumption**.

For K3 surfaces, Bayer-Macri prove Bridgeland stability and hence finitude of Harder–Narasimhan stratified moduli. For K3×E (a Calabi–Yau threefold), the literature is less complete:
- Bridgeland stability on D^b(Coh(K3×E)) is known for the K3 surface piece.
- Compact B-brane moduli in physical Mukai charge on K3×E with height truncation: no explicit finitude theorem cited.
- The reduction from height-truncated semistable substack to finite-type atlas requires bounded Chern character support, which requires the stability sector to be strictly bounded.

**Status:** The roadmap imports Bayer–Macri K3 fibre finitude but does not cite a K3×E moduli finitude theorem. The manuscript uses this as an assumption to make subsequent constructions finite.

**Consequence:** If semistable stacks at fixed height R fail to be finite-type over the base (or their restricted stacks under compactness cuts are not finite-type), then:
- F_{σ,S}(R) may be infinite,
- Γ_R^{HN} and Γ̂_R may not be finite,
- The finite charge-support Hall quotient $\mathsf F_R\mathcal H_{\sigma,S}^{or}$ is not geometrically finite by charge support alone,
- The inverse limit does not proceed by a cofinal finite system; it becomes a dense filtering, and Mittag-Leffler fails.

---

### A6-6-06: Transition maps are invoked but not constructed.

**The attack:**
The inverse limit proof (line 6087-6095) states: "The inverse limit exists by the transition compatibility, bounded exhaustive finite charge filtration, finite coassociative and counital collision coproduct, and continuity hypotheses."

But where is the explicit transition map constructed?
- For R' ≥ R, there should be a map ρ_{R'R}: 𝔇_{X,R'}^{DI} → 𝔇_{X,R}^{DI}.
- This map must restrict vanishing-cycle coefficients, orientation lines, Hall operations, and the chiral Koszul coalgebra.
- The restriction of a d-critical stack under HN truncation is not automatic: derived completions can obstruct the transition.

The manuscript defines the transition maps as "the inclusions Γ_R^Π ⊂ Γ_{R'}^Π" (line 8691) but does not show:
- The inclusion is compatible with the Hall product/coproduct at every stage.
- Restriction of extension correspondences to height-bounded substacks preserves associativity.
- The chiral coalgebra C_{X,R} injects into C_{X,R'} (or what the inverse relation is).

**Status:** Transition maps are assumed to exist and be compatible ("compatible with transition maps" appears 5+ times) but are not explicitly written down.

---

### A6-6-07: The eight associativity classes lack a cochain-complex host.

**The attack:**
The roadmap (attack-whitepaper-analysis.txt, page 45) asks: "The eight associativity obstruction classes 𝔬^{abc}_{assoc,R} ∈ ? for words in {L,W}^3 — what ambient cochain complex hosts them?"

Reading main.tex:
- The mixed-word classes (LWL, WLW, etc.) are listed as "flag defects" that must vanish.
- The pentagon identity at finite height is stated as an equality: "vanishing of all flag defects is exactly the strict pentagon condition at height R" (line 3694).
- But what is the obstruction group? If all eight words are forced to close at the level of finite-stage associators, then there is no independent obstruction class — every word is an input axiom, not a computed residual.

The manuscript does not:
- Define an obstruction cochain complex O^*_R in which the eight classes live.
- Explain how to choose associators to kill the classes (Hochschild-type calculation).
- Show that vanishing is independent of the other obstruction packages (NO1-NO7, orientation, Pfaffian wall).

**Status:** The eight words are treated as a finite list of equalities to verify, not as a moduli of obstructions. If they are equalities, the term "obstruction class" is misleading.

---

### A6-6-08: Normal-ordering obstruction package NO1-NO7 is not fully spelled out.

**The attack:**
The architecture document lists NO1-NO7:
1. finite-fibre compatibility for the normal-ordering functor
2. Hochschild boundary equation
3. pentagon
4. Jacobi compatibility
5. Frobenius/cyclic pairing
6. negative-cyclic lift
7. Hopf radical closure

The main manuscript cites these (line 89 of architecture_realization_status) but does not write out the obstruction classes or solve them. The phrase "finite verification diagrams (NO1)--(NO7)" is mentioned but the diagrams are not in main.tex.

**Where is the NO2 obstruction?** If d_Hoch Θ_{Π,R} = B_{ch,R}, does this Hochschild equation uniquely pin Θ up to coboundary, or is there a moduli of solutions? If there is a moduli, its relative dimension must vanish or the transition compatibility fails.

**Status:** NO1-NO7 are architecture items marked as "finite verification" but the actual obstruction calculations are not in the manuscript. They are residuals awaiting implementation.

---

### A6-6-09: The Koszul coalgebra C_{X,R} source-build is not proved to be compatible with the target.

**The attack:**
The manuscript states (lines 5646-5647): "A finite-stage chiral Koszul source certificate is a coaugmented finite source coalgebra with counit, finite filtration, collision coproduct, coassociativity, counit, conilpotence, and transition-continuity defects."

But:
- The chiral bar construction B^{ch}_E is defined for chiral algebras over E, not factorization algebras.
- The hybrid source F^{hyb}_{X,R} is said to be a factorization algebra (or shadow thereof) over K3 × E.
- Is B^{ch}_E applied to a *factorization* algebra, or do you first reduce to a chiral subalgebra?

The cobar comparison Θ_{Kos,R}: Ω^{ch}_E C_{X,R} ≃ Den_{Δ_5,E,≤R} is stated to be a quasi-isomorphism (line 6060) but:
- Beilinson–Drinfeld cobar functors on chiral algebras require strict Koszul duality.
- If C_{X,R} is constructed from factorization data, mixing cobar with non-chiral factorization structure breaks duality.
- The source-to-target separation is assumed, not derived.

**Status:** The Koszul source is defined by axioms, not constructed. The cobar comparison is imported (via the formal target) without verifying Koszul duality for the finite-stage hybrid factorization.

---

### A6-6-10: Orientation descent does not verify E[2] linearization explicitly.

**The attack:**
Proposition prop:finite-stage-quotient-orientation-character-system (line 3634) states that the finite-stage system includes "the E[2] (r_i; ρ_i) tuple and higher even (A_1, A_{12}, A_2; λ_1, λ_2) residuals."

But for E[2] ≅ (ℤ/2)^2:
- H^2(BE[2]; F_2) = F_2⟨x_1^2, x_1 x_2, x_2^2⟩ (three generators).
- H^1(BE[2]; F_2) = F_2⟨x_1, x_2⟩ (two generators).

The manuscript says (line 102 of architecture_realization_status): "The odd case is transfer. The N=2 case is Lemma lem:bmu2-klein-four-vanishing together with Proposition prop:rank-one-e2-linearization-obstruction."

But where is the actual computation of (r_1, r_2, r_3; ρ_1, ρ_2, ρ_3) ∈ H^2(BE[2]) × H^1(BE[2])? The manuscript does not show that vanishing of these characters is compatible with (O1) orientation descent and the Pfaffian wall models (O2).

**Status:** The E[2] linearization is listed as a finite obstruction package, but the actual characters are not computed. This is flagged as "residual" in the architecture; but if it is residual, it cannot be imported from Joyce–Upmeier.

---

### A6-6-11: Pro-stack limit may not be representable.

**The attack:**
In derived/∞-categories, the inverse limit of finite-type stacks is not finite-type. If 𝔇_{X,R}^{DI} is a finite derived stack at stage R, then:

lim_R 𝔇_{X,R}^{DI}

is a pro-object, not a stack. For the "compact" Dirac–Igusa object to be a stack (not a pro-stack), there must be:
- A representable limit (universal property + descent), or
- A finite bound R_0 beyond which the systems stabilize (they don't — the architecture says cofinality is explicit).

The recognition theorem (line 6059-6070) compares $\overline{Π}_* P_X$ with 𝔤_{Δ_5}. But does this comparison happen at a finite stage, or only in the limit? If only in the limit and the limit is a pro-object, then the comparison is a pro-comparison, which is weaker.

**Status:** The inverse limit is called "the compact Dirac–Igusa object" but may be a pro-stack, not a stack. The distinction affects whether it can be used directly in further constructions.

---

### A6-6-12: D0-certificate (D0-S) is explicitly conditional, not a construction.

**The attack:**
Definition def:first-order-d0-certificate and the (D0-S) clause (line 8803-8809) state:

"Each finite quotient carries finite-type semistable substacks, extension correspondences, vanishing-cycle coefficients, orientation lines, Hall product and coproduct maps, and protected integration. All products, coproducts, brackets, pairings, and comparison maps are defined on the finite quotients and are continuous for the inverse limit. **This clause is a conditional datum;** Lemma prop:sectorial-hall-truncation proves only the finite-first formal shape once the Hall object and the HN/support hypotheses are supplied."

So (D0-S) is explicitly marked as conditional on:
1. The oriented critical Hall object $\mathcal H_{\sigma,S}^{or}$ to exist.
2. The support and HN properties.
3. Finite-type semistable stacks (which are assumed, not proved, for K3×E).

**Status:** The (D0) certificate is not constructed; it is a certificate template that would follow if hypotheses were supplied. The hypotheses are not verified for K3×E.

---

## Suggested Healings (A6-6-13 through A6-6-18)

### A6-6-13: State explicitly that finite-type semistable moduli on K3×E is an open hypothesis.

Add a remark after Definition def:sectorial-hall-truncation stating: "For K3×E, finitude of 𝔐_{σ,S,c}^{ss} in bounded h_S-height is not proved here. It is a standing hypothesis. If true, Lemma prop:sectorial-hall-truncation makes the sectorial truncation finite. If false, F_{σ,S}(R) and Γ_R^{HN} are infinite and the inverse limit is a pro-system without cofinal finiteness."

### A6-6-14: Write the transition maps explicitly at one example.

For a small charge like (1,0,1) ∈ Γ_R^{HN}, write the restriction map:

ρ_{R'R}: (𝔐_{R',c}^{ss} × vanishing-cycle complex) → (𝔐_{R,c}^{ss} × vanishing-cycle complex)

and verify that the Hall product on 𝔐_R is the pullback of the product on 𝔐_{R'}.

### A6-6-15: Define the obstruction cochain complex for the eight words.

For each word w ∈ {LLL, LLW, ...}, define the pentagon obstruction δ_w ∈ H^*(flag stack; coefficient system) and show that vanishing is a finite-dimensional system of equations. If all eight equations are independent, explain why they are called "obstructions" rather than "axioms."

### A6-6-16: Compute the NO2 Hochschild obstruction explicitly.

Either show that d_Hoch Θ_{Π,R} = B_{ch,R} uniquely determines Θ up to coboundary (so NO2 is automatic), or compute the moduli of solutions and verify that the moduli is zero-dimensional.

### A6-6-17: Verify that the chiral Koszul duality applies to the hybrid factorization source.

Clarify whether C_{X,R} is built from a chiral algebra or a factorization algebra. If factorization, explain how the chiral bar/cobar functors (which are Chern–character and require chiral algebras) are applied.

### A6-6-18: State the E[2] linearization characters as explicit cocycles.

For each reflection r_i ∈ W(Λ_{II}^{2,1}), compute ρ_i ∈ H^1(BE[2]; F_2) and verify that (r_1; ρ_1), (r_2; ρ_2), (r_3; ρ_3) are linearly independent. Show that vanishing is a non-degenerate obstruction.

---

## Remaining Residuals (A6-6-19)

The compact Dirac–Igusa pro-object 𝔇_X^{DI} = lim_R 𝔇_{X,R}^{DI} cannot be claimed as constructed until:

1. **Finite-type semistable moduli K3×E:** Prove or import a finitude theorem for 𝔐_{σ,S,c}^{ss} in bounded height for K3×E.

2. **Explicit transition maps:** Write ρ_{R'R} in coordinates and verify composition and compatibility with all eight words and all obstruction packages.

3. **Eight-word obstruction vanishing:** Either prove the pentagon defects vanish, or state them as an open obstruction package.

4. **Normal-ordering NO1-NO7:** Complete the finite verification diagrams for all seven normal-ordering obstructions.

5. **Koszul duality for hybrid factorization:** Reconcile the chiral bar construction with factorization algebra source data.

6. **E[2] linearization characters:** Compute explicitly and verify vanishing of (A_1^{(2)}, A_{12}^{(2)}, A_2^{(2)}; λ_1^{(2)}, λ_2^{(2)}) and all even E[N] characters for N ≥ 4.

Without these, the inverse limit exists *formally* (as a pro-object graded by R) but may not be *effective* (compact, representable, or useful for recognition).

---

**Report complete. No commits. All files read-only.**
