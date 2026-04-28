# Beilinson–Drinfeld Adversarial Review: Factorization-Algebra Spine
**Date:** 2026-04-28
**Lens:** Beilinson (sheaf-theoretic descent, spectral sequences, exactness) + Drinfeld (chiral/factorization algebras, operads, hidden moduli).
**Target:** The factorization-algebra claims in the Dirac–Igusa reconstitution roadmap.
**Evidence standard:** Theorem-strength claims require explicit operadic/categorical construction or precise reduction; "expected from BV" or "natural from PTVV" is insufficient.

---

## Stable Points

1. **The normal-ordered Gram map ̄Π(c,T) = Π(c) − T as a lattice-level homomorphism** is proved and correctly placed at theorem strength. The cocycle B is verified, and the additive law ̄Π((c,T) ⋆ (c',T')) = ̄Π(c,T) + ̄Π(c',T') is a clean algebraic statement. This is stable.

2. **The raw-descent no-go theorem** (Theorem E in reconstitution plan) stating that raw Π-pushforward cannot realize full BKM real-root strings is a structural necessity statement, correctly separates B-isotropic channels from forced B-nonzero channels, and is already framed conditionally ("can be... only on bracket channels where B(c,c')=0"). This is stable as a negative result.

3. **The projection-to-E support-locality obstruction** (positive elliptic degree curves cannot localize at finitely many points of E) is a correct K3 × E × E geometry fact and does not claim full locality obstruction. Current phrasing constraints in the manuscript ("projection-to-E support-locality obstruction") protect it from physics confusion. Stable as a geometric fact.

4. **The Borcherds product and Gritsenko–Nikulin denominator algebra** are imported and externally verified. No attack targets imported theorems.

---

## Attacks

### A6-1-01: "Holomorphic E₃-factorization algebra" is a placeholder without operad or category specification

**Severity:** 2 (breaks a load-bearing theorem statement if uncontested)

**Lens:** Beilinson-Costello–Gwilliam operadic structure; chiral algebra operad.

**Target:** Definition 10.29 and repeated references to "a holomorphic E₃-factorization algebra A^E₃_X on K3×E" as though it is a named, navigable object.

**Claim:** The manuscript states (main.tex:5287–5302): "By a holomorphic E₃-factorization algebra is meant here: a factorization algebra on X in the sense of Costello–Gwilliam..., locally constant in real directions and holomorphic in three complex directions, whose factorization structure maps are governed by holomorphic polydiscs in ℂ³; equivalently a factorization algebra in the holomorphic E₃-operadic sense, together with whatever homotopy/framing datum is required by the chosen operadic model." But then it immediately says: "This symbol, and the placeholder Φ³^FA(X), denote the source object required in the Calabi–Yau-to-chiral construction; they are not a constructed functor evaluated on X."

**Broken step:** The phrase "equivalently a factorization algebra in the holomorphic E₃-operadic sense" does not name the operad. Is this the operad of holomorphic little-3-disks? Costello–Gwilliam's factorization algebra operad Act^O(Fact_hol(X))? A topological E₃ operad applied to holomorphic polydiscs? The answer determines the category: does A^E₃_X land in ChC_hol (chiral complexes), in Ch(Vect_hol), or in a sheaf-of-cochains category on Ran(X)?

The manuscript admits it is a "placeholder" and "not a constructed functor." This is honest. However:
- Definition 5283 calls it a "quantum upgrade" starting from a "supplied holomorphic E₃-factorization algebra," treating it as a supply, not a construction target.
- The same definition then lists it in the Dirac–Igusa datum tuple as a component of the "finite-first chain datum" (line 5389–5393).
- If the datum is supplied but not constructed, it should not appear as a load-bearing input to a theorem.

**Evidence type:** Textual claim + definitional context
**Evidence ref:** main.tex:5283–5316, esp. lines 5291–5302, 5389–5394; attack_whitepaper_analysis_20260428_090346_guide.md:550–557 (critique: "If 'E₃' is only heuristic, remove it from theorem-level statements and say 'holomorphic factorization algebra on X' until the operadic structure is specified.")

**Blast radius:** All factorization-algebra theorems (Bracket Theorem, Chiral Koszul Theorem) that cite the existence of A^E₃_X rest on an undefined operad. The K3→E specialization functor Sp^ch_{K3,E} has no specified source category.

**Minimal heal:**
1. In Definition 5283, replace "equivalently a factorization algebra in the holomorphic E₃-operadic sense" with a precise statement: *"a factorization algebra A^hol_X ∈ Alg_O(Fact_hol(X; ChC)) in the sense of Costello–Gwilliam [CG2 §10], where O is [specify: holomorphic little-3-disks operad / topological E₃ operad with holomorphic disk realizations / other]."*
2. If no specific operad is specified, drop "E₃" from theorem statements (keep it in conjectures/open problems).
3. Make clear: is the source *supplied* (Definition 5383–5425) or *constructed* (Open Problem 5427)? It cannot be both.

**Residual:** Even with a named operad, the "homotopy/framing datum" required by the operadic model remains informal. Costello–Gwilliam require a formality quasi-isomorphism and a framing; neither is specified here. This becomes a secondary severity-3 attack on the QME/anomaly cancellation "witnesses" (Definition 5383:5404) — what algebra do they live in?

---

### A6-1-02: The K3→E specialization Sp^ch_{K3,E} is stated in three distinct ways with no unified functor

**Severity:** 2 (breaks a central load-bearing mechanism)

**Lens:** Drinfeld chiral pushforward vs. Beilinson-Drinfeld factorization vs. ordinary derived pushforward.

**Target:** Definition 5322–5355 (the triple chain of maps) and Definition 5381–5425 (the source interface).

**Claim:** The manuscript decomposes specialization into three steps:
1. A^E₃_X --Sp^ch_{K3,E}-→ F_X^(0) (chiral pushforward, K3-integration in Costello–Gwilliam sense)
2. F_X^(0) --κ_E-→ F_X^(1) (chiral-Koszul comparison)
3. F_X^(1) --π_*^ch-→ (p_E)_* A^E₃_X (closing identification comparing CG push to topological pushforward)

It then says (line 5331–5335): "Sp^ch_{K3,E} is the Beilinson–Drinfeld chiral pushforward along the K3-fibration p_E: K3×E → E with K3-integration in the Costello–Gwilliam sense."

**Broken step:**
- "Beilinson–Drinfeld chiral pushforward" is not a standard functor. Beilinson–Drinfeld defined a *chiral algebra* structure (vertex-algebra-like objects on curves), not a pushforward along a fibration. Drinfeld's chiral algebras live on Ran(X) and respect the Ran(X) operad.
- "K3-integration in the Costello–Gwilliam sense" (pointwise on E, fibre-K3 direction integrated) is a different operation: a fiber integration of a factorization algebra along a proper holomorphic submersion. This is closer to Hopkins–Singer pushforward or a fiber integral in the factorization-algebra setting, not Drinfeld's chiral machinery.
- The target of Sp^ch_{K3,E} is described as "a chiral algebra on E (equivalently a factorization algebra on Ran(E))" — but chiral algebras (Beilinson–Drinfeld) and factorization algebras (Costello–Gwilliam) on Ran(E) are *different* structures. A chiral algebra is a sheaf of vertex-algebra-like objects on Ran(E); a CG factorization algebra is a functor from opens to cochains. Equivalence requires formality (Gaitsgory).

**Evidence type:** Terminological collision + unspecified functor + category mismatch
**Evidence ref:** main.tex:5331–5337; attack_whitepaper_analysis.txt:559–599 (critique: "Sp^ch_{K3,E} is not a known functor in the paper. It is a desired operation. You admit that construction is open... all compact physics is hidden inside the undefined functor.")

**Blast radius:**
- The entire chain-level normal-ordering theorem (Θ-descent) assumes Sp^ch_{K3,E} produces F_X^(0) ∈ Fact(Ran(E)). If Sp^ch_{K3,E} is not a functor, the target does not exist.
- The recognition of π_* P_X ≅ g_{Δ₅} depends on applying normal-ordered descent to the output of Sp^ch_{K3,E}. If that output is undefined, recognition is vacuous.
- The hybrid wrapped factorization certificate (Definition 6197–6400) claims to stratify Sp^ch_{K3,E}(A^E₃_X) into projection-finite and wrapped sectors. But if Sp^ch_{K3,E} is not constructed, this stratification is premature.

**Minimal heal:**
1. Choose *one* of three interpretations:
   - *Interpretation A:* Sp^ch_{K3,E} is a Costello–Gwilliam fiber integral: A^E₃_X ⊗ Ω_K3 → (p_E)_* A^E₃_X in the factorization-algebra setting, with subsequent formality to chiral shadow.
   - *Interpretation B:* Sp^ch_{K3,E} is a Drinfeld-style chiral algebra obtained by vertex-algebra fiber integration (if K3 were replaced by a curve; here K3 is 2-dimensional, so this is forced to be formal/heuristic).
   - *Interpretation C:* Sp^ch_{K3,E} is an ordinary pushforward (p_E)_* followed by a formality quasi-isomorphism.
2. Define Sp^ch_{K3,E} explicitly: source category, target category, functoriality, compatibility with transition maps.
3. If the functor is not yet constructed, move Sp^ch_{K3,E} to an open problem (not a data supply).

**Residual:** Even after specifying the functor, the chiral-Koszul comparison κ_E: F_X^(0) → F_X^(1) and the proper-pushforward identification π_*^ch remain open. The manuscript acknowledges this (line 5344, 5349–5350: "identification of chiral and ordinary pushforward is the open chiral-Koszul comparison"; "is open in the wrapped sectors"). So Sp^ch_{K3,E} → (p_E)_* is a chain of three open maps, none of which is proved. This is severity-2 because the roadmap places all three in the "datum" (Definition 5383), not in "open problems."

---

### A6-1-03: The hybrid Ran^hyb(E) does not have a proved associativity law for 8 two-step words

**Severity:** 2 (breaks the factorization structure itself)

**Lens:** Drinfeld operadic associativity and obstruction theory in the factorization-algebra category.

**Target:** Definition 6197 (hybrid factorization certificate) and Definition 6307–6350 (four operation types: local-local, local-wrapped, wrapped-local, wrapped-wrapped).

**Claim:** The hybrid object F_X^hyb is defined to have four operation types. Associativity requires the eight two-step words (LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW) to commute. The definition supplies correspondences for each but records defect classes: proper-support defects mathfrak{o}^{prop,LL}_R, mathfrak{o}^{prop,mix}_R, mathfrak{o}^{prop,WW}_R (lines 6366–6377).

**Broken step:**
- The definition says (line 6378–6379): "They vanish exactly when all pull-push maps used below are honest finite-stage operations, not formal correspondences without a defined pushforward."
- But the definition does not assert that these defects vanish. It supplies them as possible future witness data. The wrapped sector uses an "anchor λ_{η,R}" (lines 6282–6291) to remember relative E-position. This anchor is not a canonical choice ("No canonical rigidification is asserted").
- Without a canonical rigidification or a proof that defects vanish, the wrapped-wrapped correspondences E^{wr}_{η₁,η₂,R} are *formal correspondences*, not finite operations. Line 6393–6394 notes: "The finite correspondence keeps this relation, not only the total degree" — i.e., the wrapped-wrapped product does not automatically compose.

**Evidence type:** Definitional claim + missing axiom
**Evidence ref:** main.tex:6197–6400, esp. 6307–6350, 6366–6394; attack_whitepaper_analysis.txt:316–327 (critique: "Associativity is checked on the eight two-step words... Each word should have an obstruction class. The hybrid factorization object exists at finite stage only after these classes vanish with compatible transition maps.") and 5500–5600 (critique: "Does the proposed obstruction tuple actually witness the failure of associativity, or only its degree shadow?").

**Blast radius:** The claim that F_X^hyb is a factorization object (Definition 6197:line 6201: "factorization certificate") requires:
- Factorization maps: F(U₁) ⊗ ⋯ ⊗ F(Uₖ) → F(U₁ ∪ ⋯ ∪ Uₖ) for disjoint opens and their operadic associativity.
- Wrapped extension correspondences (Definition 6307–6335) have three types. Associativity of their 8 two-step compositions is not asserted.
- If wrapped-wrapped correspondences are only formal (not honest), then the wrapped sector does not carry a factorization algebra structure — it is a module acted on by the local factorization algebra. The definition conflates (module action) with (factorization object).

**Minimal heal:**
1. Clarify: is F_X^hyb a full factorization algebra, or is it a factorization object on the b=0 stratum plus a module on the b>0 strata?
2. If full factorization: supply a proof or a named open problem that the eight defects mathfrak{o}^{prop,LL}_R, mathfrak{o}^{prop,mix}_R, mathfrak{o}^{prop,WW}_R vanish with compatible transition maps.
3. If module structure: redefine Definition 6197 as "(Factorization algebra) ⋊ (Module)" and move the wrapped-wrapped product to a separate "interaction term" section (as already suggested in attack_whitepaper_analysis.txt line 2485: "Wrapped-wrapped extensions give W_{X,m} ⊗ W_{X,m'} → W_{X,m+m'+interaction}").

**Residual:** Even with module structure, the "mixed Hall correspondences" (Definition 6318–6325, 6340–6350) that connect local and wrapped sectors must satisfy compatibility axioms with the ordinary factorization structure of F^loc_R. These are not stated. Residual severity-3 attack on mixed-action associativity.

---

### A6-1-04: The wrapped anchor λ(A) ∈ Pic⁰(E) ≅ E is origin-dependent and breaks E-equivariance

**Severity:** 2 (breaks the claimed equivariance of the hybrid object)

**Lens:** Beilinson equivariant descent and determinant-line transport.

**Target:** Definition 6281–6291: the E-equivariant anchor λ_{η,R}: M^{wr,rig}_{η,R} → E with λ_{η,R}(t·W) = t + λ_{η,R}(W).

**Claim:** The anchor λ is defined to be "E-equivariant" in the sense that it respects translation by t ∈ E. The definition says (line 6282–6285): "an E-equivariant anchor λ_{η,R}: M^{wr,rig}_{η,R} → E, λ_{η,R}(t·W) = t + λ_{η,R}(W)."

**Broken step:** The anchor λ is described in attack_whitepaper_analysis.txt (line 304–306) as "det Rp_{E,*}A ⊗ O_E(−χ(A)·0_E) ∈ Pic⁰(E) ≅ E." This is determinant-of-pushforward times a degree correction. But:
- Pic⁰(E) ≅ E is an isomorphism only *after choosing an origin 0_E*.
- Once 0_E is fixed, λ is a map M^{wr,rig}_{η,R} → E ⊂ Pic⁰(E). If the origin changes (0'_E ≠ 0_E), the map changes by a constant translation.
- The hybrid object definition must choose 0_E at the finite stage and carry it through the inverse limit. But the definition does not state this. Line 6285 says "λ_{η,R}(t·W) = t + λ_{η,R}(W)" — the "+" is a group operation on E, which requires an origin.

**Evidence type:** Missing data (choice of origin) in definition
**Evidence ref:** main.tex:6282–6285 (definition of anchor without specifying origin); attack_whitepaper_analysis.txt:304–306 (the formula "det Rp_{E,*}A ⊗ O_E(−χ(A)·0_E)" explicitly shows origin dependence); reconstitution_plan.md:296–310 (the wrapped anchor section acknowledges but does not resolve the choice).

**Blast radius:**
- The E-equivariance of the hybrid object (claimed in Definition 6197 and used in Definition 6382–6391 where relative E-positions are tracked) depends on λ being a group homomorphism.
- If λ is only defined after choosing 0_E, then the compatibility under transition maps ρ_{R'R} (Definition 5381–5425) must preserve the choice of origin across all finite stages R.
- The orientation line o_{η,R} on M^{wr,rig}_{η,R} interacts with the E-equivariance. If the origin shifts, does o_{η,R} carry a companion transport? This is a degree-one gerbe-theoretic question (related to orientation-character theorem (O1)).

**Minimal heal:**
1. In Definition 6197, add a fixed choice: "0_E ∈ E(C) a chosen closed point" (or equivalent algebraic choice).
2. In Definition 6382–6391, state explicitly: "Before quotienting by E, the anchor λ_{η₁,R} and λ_{η₂,R} are relative to the fixed 0_E. Quotient compatibility requires that the determinant-line transport on o_{η,R} compensates for the origin choice."
3. State how the origin 0_E is preserved under transition maps ρ_{R'R}.

**Residual:** The origin choice is not canonical. Different choices of 0_E give different rigidifications (e.g., different Abel–Jacobi centers). The definition says (line 6289: "For example an Abel–Jacobi center, determinant trivialization, framed marked point, or a named equivalent"). This is flexibility, not ambiguity, if the choice is fixed and transported. But the manuscript does not fix it. Residual severity-3 attack: is rigidification data part of the "supply," and if so, where is it specified in Definition 5383–5425?

---

### A6-1-05: The chain-level normal-ordering cochain Θ_{Π,R} has an underdetermined Hochschild-cocycle equation

**Severity:** 2 (breaks the claim that Θ realizes lattice normal-ordering at chain level)

**Lens:** Hochschild cohomology, cyclic homology, and Lie-theoretic enveloping algebra.

**Target:** Definition of Θ_{Π,R} in context of (NO1)–(NO7) (the chain-level normal-ordering obstruction package).

**Claim:** The roadmap (architecture_realization_status.md:89, lines 27) states: "Chain-level normal ordering now distinguishes the formal central translation cochain from its compact Hall realization, and records the finite verification diagrams (NO1)--(NO7)." The definition says Θ is a cochain satisfying d_{Hoch}Θ = B^ch (Hochschild boundary of Θ equals the "Hall-chain defect").

**Broken step:**
- A Hochschild 2-cocycle φ: C ⊗ C → C satisfying d_{Hoch}φ = 0 can be zero (cohomologous cocycle) or genuinely nonzero (obstruction). The equation d_{Hoch}Θ = B^ch determines Θ up to a Hochschild 2-coboundary. This under-determines Θ.
- The lattice normal-ordering ̄Π is a *homomorphism* (additive law proved algebraically). At chain level, Θ should be a homotopy-compatible operation that *shifts* degree by subtraction, not just a Hochschild coboundary. The paper does not specify whether Θ is a degree-shift isomorphism, a natural transformation, or a Hochschild cocycle in the classical sense.
- The "scalar pentagon Pent_Θ = 0" (attack_whitepaper_analysis.txt, line 5-ish) is mentioned as a separate condition on the normal-ordering cochain. If the pentagon is a separate condition, it must be verified (not derived from d_{Hoch}Θ = B^ch alone).

**Evidence type:** Missing axiom specification + underdetermined Hochschild equation
**Evidence ref:** main.tex: search for "Theta_Pi" and "Hochschild"; attack_whitepaper_analysis.txt (line ~820): "Does this Hochschild-cocycle equation actually pick out a Lie-theoretic normal-ordering, or is it underdetermined? Does the scalar pentagon Pent_Θ = 0 follow from associativity of ⋆, or is it a separate condition the roadmap has confused?"

**Blast radius:** If Θ is underdetermined, the chain-level normal-ordering descent is not unique. Different choices of Θ (all satisfying d_{Hoch}Θ = B^ch) could give different Hall brackets after specialization. The recognition theorem (primary claim) "π_*P_X ≅ g_{Δ₅}" depends on this chain descent being canonical.

**Minimal heal:**
1. Define Θ_{Π,R} precisely: is it a normalized Hochschild 2-cocycle (with chosen section), a graded Lie algebra central extension cochain, or a natural transformation/homotopy in the factorization-algebra category?
2. State all axioms: d_{Hoch}Θ = B^ch, AND the scalar pentagon Pent_Θ = 0 (not "follows from" — explicitly verify).
3. Prove uniqueness (up to homotopy): if two cochains Θ, Θ' both satisfy the axioms, show they are Hochschild-cohomologous.
4. Supply the finite verification diagrams (NO1)–(NO7) in a detailed lemma, not as a summary.

**Residual:** Even with uniqueness, the Hochschild cocycle method is local (each open U ⊂ E needs its own cochain). Gluing Θ_R(U) over E to a global chain-level descent Θ_R requires Čech-Deligne compatibility or a sheaf-theoretic descent spectral sequence. This is residual severity-3.

---

### A6-1-06: The Koszul comparison Θ_{Kos}: Ω^ch_E C_{X,R} → Den_{Δ₅,E,≤R} conflates chiral and ordinary coalgebras

**Severity:** 2 (breaks the target of normal-ordering descent)

**Lens:** Beilinson chiral coalgebra vs. ordinary coalgebra; Koszul duality.

**Target:** Definition 5322–5355 and the stated chiral-Koszul comparison κ_E and π_*^ch.

**Claim:** The manuscript (Definition 5338–5344) defines κ_E as "the chiral-Koszul comparison F_X^(0) → F_X^(1), where F_X^(1) is the candidate identification of the chiral pushforward with the ordinary derived pushforward (p_E)_* A^E₃_X regarded as a sheaf-of-cochain factorization algebra on Ran(E); identification of chiral and ordinary pushforward is the open chiral-Koszul comparison."

The roadmap (attack_whitepaper_analysis.txt:283–289) lists "C_{X,R}: source chiral Koszul coalgebra" and "Θ_{Kos,R}: source-to-target cobar comparison."

**Broken step:**
- A chiral coalgebra (Beilinson–Drinfeld) is a sheaf on Ran(E) with a compatible co-multiplication in the chiral sense (using disjoint-union support constraints).
- An ordinary coalgebra C_{X,R} is a cochain complex with a coproduct and counit satisfying Hopf axioms.
- The "Koszul comparison" is a statement in ordinary algebra: Koszul duality says a Koszul algebra and its Koszul dual are quasi-isomorphic under formal geometry. But a *chiral* Koszul statement requires formality of the chiral algebra (Gaitsgory–Lurie) *before* comparing to an ordinary coalgebra.
- The definition says (line 5344): "identification of chiral and ordinary pushforward is the open chiral-Koszul comparison." This is phrased as open, but it appears as a component of the finite-stage datum (Definition 5381–5425) supplied at each R.

**Evidence type:** Category mismatch + open/closed status ambiguity
**Evidence ref:** main.tex:5338–5344; attack_whitepaper_analysis.txt:283–289, and the general critique on chiral vs. ordinary algebra (lines 500–600 approximately).

**Blast radius:** The recognition of π_*P_X ≅ g_{Δ₅} (the bracket theorem) uses the Koszul comparison to identify a chiral algebra (output of specialization) with the BKM denominator algebra g_{Δ₅} viewed as a coalgebra. If Θ_{Kos} is only an open problem, the recognition is conditional on it.

**Minimal heal:**
1. Define the source chiral coalgebra C_{X,R} explicitly: is it the chiral bar construction B^ch(F_X^(0)), or is it a different object?
2. Define the target ordinary coalgebra Den_{Δ₅,E,≤R}: is it the degree-≤R part of an ordinary (not chiral) Koszul dual of the BKM Lie algebra g_{Δ₅}?
3. State whether the Koszul comparison Θ_{Kos} is (a) conjectured to be a quasi-isomorphism, (b) open, or (c) a consequence of formality of the chiral pushforward (in which case, what is the formality witness?).

**Residual:** Even after defining Θ_{Kos}, the "ordinary derived pushforward (p_E)_* A^E₃_X" (line 5342) is ambiguous: derived pushforward in what category? Quasi-coherent sheaves? Coherent sheaves? Complexes? Dg-modules over a dg-algebra? The target category of the Koszul comparison depends on this. Residual severity-3.

---

### A6-1-07: Positive elliptic-degree wrapping is claimed to be a factorization phenomenon, but arises from sheaf-theoretic descent obstruction

**Severity:** 3 (breaks a section if uncontested, but does not attack the central spine)

**Lens:** Beilinson sheaf-theoretic descent and spectral sequences.

**Target:** The claim that "hybrid local/wrapped factorization" is a single factorization structure with two strata, vs. the claim that it is a local factorization algebra acting on a wrapped module.

**Claim:** The roadmap (attack_whitepaper_analysis.txt:295–327, "Hybrid Local/Wrapped Factorization") asserts: "Projection-finite Ran locality on E sees only the m=0 / local sector. Positive elliptic degree is not a failure of spacetime locality. It is a wrapped sector... The hybrid object must have four operation types: local-local; local-wrapped; wrapped-local; wrapped-wrapped. Associativity is checked on the eight two-step words... The hybrid factorization object exists at finite stage only after these classes vanish with compatible transition maps."

**Broken step:** The phrasing "hybrid factorization object" suggests a single factorization algebra with two strata. But the underlying geometry is a sheaf-theoretic descent problem:
- Projection to E kills positive-degree curve classes (they dominate E, not finitely many points).
- This is a *failure of ordinary descent* for the factorization structure along the projection p_E.
- A sheaf-theoretic descent spectral sequence (Beilinson-style) would address this: start with the factorization algebra on K3×E, project to E, and ask where descent obstruction classes live.
- The obstruction to descent is not "positive elliptic degree is wrapped," but rather "positive elliptic degree curves have global support on E, so their BM cohomology is a global section (module over the projection-finite sector), not a local factorization piece."

This is physically correct (attack_whitepaper_analysis.txt:2400–2500 confirms the physics), but mathematically the phrasing "factorization with wrapped sector" obscures that the wrapped sector is a *module* over the local factorization algebra, and the "eight two-step words" are associativity of module and algebra actions, not factorization operad associativity.

**Evidence type:** Phrasing ambiguity + category-theoretic distinction
**Evidence ref:** main.tex:6197–6400 (hybrid definition); attack_whitepaper_analysis.txt:601–622 (critique on projection-to-E obstruction); reconstitution_plan.md:295–327 (hybrid object description).

**Blast radius:** Section-level: the entire "Compact Holomorphic E₃ Source" part (Part III) relies on the hybrid object being a genuine factorization object. If it is a module, the operadic approach is not applicable.

**Minimal heal:** Reframe the hybrid object as:
- F_X^{loc} = projection-finite factorization algebra (ordinary Ran(E)-factorization).
- W_X,m = wrapped module graded by elliptic degree m > 0.
- F_X^{hyb} = (F_X^{loc}, W_X, ⋊) = factorization algebra with action on module.

State that the "eight two-step words" test associativity of (local-local operations) ⊙ (local-wrapped actions) ⊙ (wrapped-wrapped interactions), not associativity of a single operad. This moves the logical center from "factorization" to "algebra with module action."

**Residual:** After reframing, the mixed Hall correspondences (Definition 6318–6350) need compatible axioms with both the local factorization structure and the wrapped module structure. A Beilinson-style descent spectral sequence would formalize this, but it is not written. Residual severity-3 (compatibility axioms).

---

## Suggested Healings

### Healing A6-1-01 (E₃-factorization operad)
**Action:** Define the operad explicitly in Definition 5283.
- If using Costello–Gwilliam: state "A^E₃_X ∈ Alg_O(Fact_hol(X; ChC)) where O = Cos-Gwil holomorphic E₃ operad."
- Supply the formality/framing datum as a separate input (not "required by the operadic model" but "a choice to be supplied").
- Move the E₃ reference to open problems if operad unspecified.

**Result:** Attacks A6-1-01 → closed. Residual: QME/anomaly cancellation is still informal (severity-3 residual).

### Healing A6-1-02 (K3→E specialization functor)
**Action:** Choose one interpretation and define Sp^ch_{K3,E} as a named functor with source and target categories specified.
- *Preferred:* Sp^ch_{K3,E} is a fiber integral (Costello–Gwilliam pushforward along p_E) followed by formality to chiral shadow. Define formality explicitly.
- If unconstructed: move Sp^ch_{K3,E} to open problems (Open Problem 5427 is already defined; make it the *only* statement on Sp^ch_{K3,E} in the theorem spine).

**Result:** Attacks A6-1-02 → closed if functor is defined, severity-2 residual if open (but explicit).

### Healing A6-1-03 (Hybrid associativity)
**Action:** Reframe F_X^{hyb} as a factorization algebra plus module, not as a single factorization object. State the eight two-step words as axioms for (local ⊙ local), (local ⊙ wrapped), (wrapped ⊙ local), (wrapped ⊙ wrapped interactions), with explicit obstruction classes and a statement of when they vanish.

**Result:** Attacks A6-1-03 → severity-3 (module compatibility axioms are still open, but clearly separated from factorization associativity).

### Healing A6-1-04 (Wrapped anchor origin)
**Action:** Fix a choice of 0_E ∈ E in Definition 6197 and state how it is preserved under transition maps ρ_{R'R}. If multiple rigidifications are allowed (Abel–Jacobi vs. determinant trivialization), state that one is chosen globally at the finite stage.

**Result:** Attacks A6-1-04 → closed (origin dependence is now explicit).

### Healing A6-1-05 (Θ Hochschild equation)
**Action:** Define Θ_{Π,R} as a normalized Hochschild 2-cocycle or as a Lie-algebra central-extension cochain. State all axioms (d_{Hoch}Θ = B^ch AND Pent_Θ = 0). Prove uniqueness or state it as open.

**Result:** Attacks A6-1-05 → closed if axioms are complete. Residual: gluing Θ to a global descent spectral sequence (severity-3 residual).

### Healing A6-1-06 (Koszul comparison)
**Action:** Define C_{X,R} and Den_{Δ₅,E,≤R} in separate, precise definitions. State whether Θ_{Kos} is (a) a quasi-isomorphism (conjectured/open), or (b) follows from formality of the chiral pushforward. If (b), supply the formality witness.

**Result:** Attacks A6-1-06 → severity-3 residual (Koszul duality is conditional on formality, which is open).

### Healing A6-1-07 (Wrapped as module, not factorization)
**Action:** Rewrite Definition 6197 as defining F_X^{loc} ⊗ W_X (factorization algebra acting on modules), not a single factorization object. State the axioms of module action and Hall convolution separately.

**Result:** Attacks A6-1-07 → closed (but requires upstream fixes to open-problem statements about the hybrid object).

---

## Remaining Residual

**After the proposed healings are implemented:**

1. **QME/anomaly cancellation (severity-3):** The "descent, QME, and anomaly-cancellation witnesses at every finite height R" (Definition 5404) remain undefined. What algebra do they live in? How are they computed from the E₃-source? This requires a full BV-BFV construction, which is outside the scope of the roadmap but should be marked as an open problem.

2. **Formality of the chiral pushforward (severity-2):** If the K3→E specialization Sp^ch_{K3,E} is defined as a fiber integral followed by formality, what is the formality datum? The current definition says "chosen E₃-formality point" (line 5406) but does not specify what this is. This must be either (a) constructed from the compact source or (b) supplied as an external choice.

3. **Gluing Θ_{Π,R} along E (severity-3):** The chain-level normal-ordering cochain Θ_{Π,R} is defined at each finite height R and each open U ⊂ E locally. Gluing these into a global descent spectral sequence requires Čech-Deligne sheaf descent. This is not addressed.

4. **Module-action associativity (severity-3):** The mixed Hall correspondences (local ⊙ wrapped ⊙ local) and (wrapped ⊙ wrapped interactions) have explicit obstruction classes (Definition 6366–6377) but no proof that they vanish. This must be verified for the hybrid object to exist.

**What would close all residuals (even severity-3):**
- A complete BV-BFV construction on K3×E (supplying the QME and anomaly-cancellation witnesses).
- An explicit choice (or construction) of the E₃-formality point and homotopy/framing datum.
- A detailed computation of the module-action obstruction classes at a concrete finite stage (e.g., R=5 or R=10) showing they vanish.
- A formality quasi-isomorphism (or reference to a formality result) for the K3→E chiral pushforward in the wrapped sectors.

These are the 8 still-open constructions listed in architecture_realization_status.md:109–125. The attacks above do not add new open problems; they clarify which components are open and which are slogan-heavy.

---

**Conclusion:** The roadmap is mathematically honest in stating that the compact E₃-source is open. However, **severity-2 attacks A6-1-01, A6-1-02, A6-1-03, A6-1-04, A6-1-05, A6-1-06** arise from ambiguous phrasing of operadic/categorical structures and must be healed before any load-bearing theorem uses them. The proposed healings are straightforward but require explicit choices and definitions where the current text offers placeholders.
