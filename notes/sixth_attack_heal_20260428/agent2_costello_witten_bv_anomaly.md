# Costello–Witten Adversarial Review: BV Anomalies and Physical Consistency

**Date:** 2026-04-28
**Lens:** Costello (BV quantization, factorization, anomalies) + Witten (physical duality, wall-crossing, protected structures)
**Target:** Dirac–Igusa orientation–Pfaffian architecture on K3×E

---

## STABLE POINTS (Not Under Attack)

**S-1.** The automorphic determinant identity $\mathcal{D}_X(Z) = \Delta_5(Z)$ is theoretically solid. Borcherds–Gritsenko–Nikulin supply the monic product representation $D_5 = 64^{-1}\Delta_5$ with exponents $f(nm, l)$ as Jacobi-form Fourier coefficients. This is imported mathematics. ✓

**S-2.** The Gram cocycle $B(c, c') = (Q \cdot Q', Q \cdot P' + Q' \cdot P, P \cdot P')$ is a valid lattice-level additive 2-cocycle satisfying $\delta B = 0$ and $B(c, c) = 2\Pi(c)$ polarization. This is lattice algebra, independent of orientation or parity. ✓

**S-3.** The normal-ordered map $\overline{\Pi}(c, T) = \Pi(c) - T$ is a genuine homomorphism from the central extension $\Gamma_X = \Gamma_X^{\mathrm{phys}} \oplus_B \Gamma_{\mathrm{gram}}$ to $\Gamma_{\mathrm{gram}} = \mathbb{Z}^3$. The proof is direct cocycle calculation. ✓

**S-4.** The Maass character $\nu_{\Delta_5}$ on the type-II Weyl group $W^{(2)}(\Lambda^{2,1}_{II})$ is arithmetic fact: $\nu_{\Delta_5}(s_{\delta_i}) = -1$ on the three simple type-II reflections. This is established via automorphic duality. ✓

**S-5.** The OP/DT scalar square $Z^X_{\mathrm{OP/DT}} = -4096 \Delta_5^{-2}$ is imported from OP and DT theory. The sign decomposition $-4096 = -(64)^2$ is conventional (theta-monic normalization). ✓

---

## ATTACKS

### **A6-2-01: The CY3/(-1)-Shifted Symplectic Dimensional Mismatch**

**Claim Under Attack:**
The manuscript states that $K3 \times E$ is a Calabi–Yau 3-fold with d-critical reduced structure on $\mathrm{Perf}(K3 \times E)$, and applies PTVV to obtain $(-1)$-shifted symplectic structure on the moduli of perfect complexes (line 548, 1403, 2765).

**The Problem:**

1. **PTVV for CY3 gives (-1)-shifted, not (-2)-shifted:**
   The PTVV theorem (Pantev–Toën–Vaquié–Vezzosi 2013) states: if $X$ is a Calabi–Yau $m$-fold, the derived moduli stack $\mathfrak{M}(X)$ of perfect complexes carries a $(-m+1)$-shifted symplectic structure.
   - For $m = 3$: shift = $-2$.
   - For $m = 4$: shift = $-3$.

   **But the manuscript says K3×E is 3-dimensional** (correctly). Thus PTVV gives **(-2)-shifted**, not (-1)-shifted.

2. **(-2)-shifted symplectic ≠ (-1)-shifted d-critical:**
   The Brav–Bussi–Dupont–Joyce–Szendröi (BBDJS 2015) d-critical structure is a degree-1 phenomenon: a d-critical chart is a (-1)-shifted symplectic smooth stack modulo a cosection.
   - A **(-2)-shifted symplectic** structure cannot directly define a d-critical structure without additional reduction data.
   - The relationship is: (-2)-shifted symplectic + **proper cosection** → (-1)-shifted d-critical after quotient.

3. **The roadmap uses "protected d-critical" language without naming the cosection:**
   Line 511–514 invokes "d-critical chart, in the sense of BBDJS" but does not specify:
   - What is the cosection $\sigma: T_{\mathfrak{M}} \to \mathcal{O}_{\mathfrak{M}}$?
   - Is it the trace of the identity endomorphism (the standard DT cosection)?
   - Or is it something else forced by the K3×E compactification?

4. **Pfaffian in (-2)-shifted vs. (-1)-shifted is asymmetric:**
   - In the (-2)-shifted setting (Borisov–Joyce, Oh–Thomas), the Pfaffian of a virtual operator lives naturally as a rank-1 object on the coisotropic reduction locus.
   - In the naive (-1)-shifted setting, there is no Pfaffian of a first-order operator; only a square-root of the symplectic form.
   - The roadmap claims a "Pfaffian of a protected first-order operator $\mathfrak{D}_X$" (line 104). **This rhetoric is from the (-2)-shifted / CY4 world.** Does it apply to CY3 / (-1)-shifted after cosection reduction?

**Damage:**
The core theorem claims $\text{Pf}^{\mathrm{prot}}(\mathfrak{D}_X) = \Delta_5$, where the Pfaffian is supposed to be "the preserved first-order structure that the scalar square forgets" (line 45–46). But the physical meaning of "Pfaffian" in a (-1)-shifted d-critical setting (after reduction from the (-2)-shifted PTVV host) requires explicit mention of:
- Which cosection?
- How does the Pfaffian descend through it?
- Is the Pfaffian line a line on the reduced d-critical locus, or on the unreduced (-2)-shifted stack?

**Severity:** **Critical.** The dimension mismatch is not rhetorical; it changes the algebra of the orientation line and the meaning of "protected."

---

### **A6-2-02: Joyce–Upmeier Orientation Descent Problem**

**Claim Under Attack:**
Lines 1086, 1383–1389 claim that Joyce–Upmeier orientation on $\mathrm{Perf}(X)$ (full CY3) descends to a "strong reduced orientation" on the quotient $K3 \times E / E$ with Weyl-equivariant character $\epsilon_o = \nu_{\Delta_5}$ on stabilizer orbits.

**The Problem:**

1. **Joyce–Upmeier constructs orientation on the *full* moduli:**
   The Joyce–Upmeier theorem gives a canonical orientation *cocycle* on the derived Hall algebra (or derived stacks) built from $\mathrm{Perf}(X)$ directly. It is a global object.

2. **Descent through a finite-stabilizer quotient is non-trivial:**
   The manuscript proposes:
   - (O1): A reduced orientation line $o_R$ on the quotient sector.
   - (O1)⁺: A Weyl-equivariant lift to the stabilizer action.
   - (O2): A local Pfaffian normal form on type-II walls.

   **But Joyce–Upmeier orientation, when pulled back to a finite-stabilizer quotient, need not be invariant under the stabilizer action.** The nontrivial data are:
   - The local linearization character on $E[N]$ torsors.
   - The compatibility of the orientation cocycle with the quotient projection.
   - Verification that the descent respects the Hopf pairing and radical structure.

3. **Lines 1122–1135 admit the issue:**
   "the quotient-orientation package transported in (O1)⁺" — but this is an open obligation. The manuscript does not:
   - Construct the transport (it says "transported" as a name, not a proof).
   - Check that the finite-stabilizer $E[N]$-linearization character actually trivializes the quotient obstruction in $H^1(BE[N]; \mathbb{F}_2)$.
   - Show that small-orbit vanishing holds on all three type-II walls simultaneously.

4. **Finite vs. connected $E$-descent conflation risk:**
   The roadmap correctly notes (line 515–519 of reconstitution plan) that $H^1(BE; \mathbb{F}_2) = 0$ (connected $E$) but $H^2(BE[2]; \mathbb{F}_2) = \mathbb{F}_2^3$ is nontrivial for 2-torsion. However, the main text does not always separate:
   - The analytic continuation descent (connected $E^{\mathrm{top}} \simeq T^2$).
   - The finite stabilizer descent ($E[N]$ as torsors).

**Damage:**
The orientation theorem (lines 1047–1135) is stated as conditional and certificate-level, which is correct. But the phrase "Joyce–Upmeier-type orientation" (line 1086) can mislead: it is Joyce–Upmeier *imported*, then *restricted*, then *descended*, then *transported*. Each step is an open construction. The "∃" on line 1086 is conditional on (O1)–(O2), which are explicitly open (line 1378–1382).

**Severity:** **Medium-high.** The descent is listed as open, so the claim is technically safe. But the rhetorical framing (invoking Joyce–Upmeier by name) suggests more concreteness than is justified until the descent is constructed.

---

### **A6-2-03: "Protected Supercharge" and Unitarity of the K3×E Compactification**

**Claim Under Attack:**
Lines 168–170, 496–497, and elsewhere assert a "protected supercharge" $Q$ that "is killed by antiholomorphic translations" and whose unitarity gives "localization, then the index becomes virtual."

**The Problem:**

1. **The K3 sigma model is unitary; K3×E compactified is different:**
   - The flat K3 sigma model has a unitary Hilbert space and a protected $N=4$ supercharge structure.
   - Compactifying with an elliptic factor $E$ introduces additional bosonic and fermionic degrees of freedom.
   - **The assertion that "protected supercharge = killed by antiholomorphic translations" is physics language, not mathematical definition.**

2. **What is the protected $Q$ on K3×E?**
   The manuscript (line 401ff.) talks about "a charged BPS state is not a local field" and uses BPS-sheaf language from BBDJS. But BBDJS is for d-critical *geometry*, not for supercharge preservation in a compactified quantum field theory. The connection is:
   - BBDJS: orientation line on the *moduli* of stable objects.
   - Supercharge: action on the *Hilbert space* of states.

   **These are dual questions. The manuscript does not make the Fourier–Mukai or mirror-symmetry bridge explicit.** How is the protected $Q$ on the quantum side related to the d-critical chart on the geometric side?

3. **Unitarity and cancellation theorem:**
   The statement "unitarity gives localization, then the index becomes virtual" (implied by lines 100–107) invokes the BPS-index localization formula:
   $$\text{Index}(D) = \int \text{character} \, e^{\omega/2\pi i}$$
   where $D$ is a Dirac-type operator with supercharge $Q$, and $\omega$ is the symplectic form.

   **But in the compactified K3×E setting with a Costello-renormalized elliptic factor:**
   - Is the cancellation $\{Q, Q^\dagger\} = H_{\mathrm{right}}$ still valid?
   - Does the elliptic factor's coupling (Costello–Li flat connection, line 7284–7307) preserve the unitarity of the full $Q$?
   - What is the protected $Q$ explicitly in terms of current algebra or Kac–Moody generators?

4. **No explicit form of Q:**
   The paper uses "protected supercharge" as a structural principle (line 168) but never writes:
   - $Q = \sum \cdots$ (even schematically).
   - What is $[Q, Q^\dagger]$? What is the right-hand side?
   - How does it relate to the Gram-cocycle $B(c, c')$ at the quantum level?

**Damage:**
The BV quantization hinges on having a nilpotent odd derivation $Q$ of cohomological degree +1 with $Q^2 = 0$. The claim that this descends to a "protected" form killed by translations is physics intuition, but it is not verified mathematically. The manuscript uses this to justify the shift from states to "formal current envelope" (lines 94–107, 2028–2033), but the rigor gap is large.

**Severity:** **High.** This is foundational to the claim that the Pfaffian is "protected." Without an explicit $Q$ and a proof of nilpotency + protection in the K3×E compactification, the entire Dirac datum is heuristic.

---

### **A6-2-04: Pfaffian Sign Character — Where Does It Come From Physically?**

**Claim Under Attack:**
Lines 532, 537, 838–890, and the orientation-character theorem (lines 1047–1135) claim that the Pfaffian line monodromy around the type-II walls encodes the reflection character $\epsilon_o = \nu_{\Delta_5}$, and that the OP scalar minus sign does not source this character.

**The Problem:**

1. **The OP sign is scalar; the character is determinant-line geometry.**
   The manuscript correctly states (line 342–344) that the OP minus is a scalar convention and does not prove $\epsilon_o = \nu_{\Delta_5}$. Good.

   But then the roadmap says (line 887–890):
   > "The local Pfaffian wall lane now states the exact geometric local calculation needed on each type-II wall: equivariant chart, reduced self-Ext splitting, invariant normal Pfaffian unit, and $N_\delta^{\mathrm{Pf}} = 1$."

   **What is the "invariant normal Pfaffian unit"?** Is this:
   - A section of the Pfaffian line, normalized on the wall chart?
   - A choice of trivialization of the determinant line of the normal Ext bundle?
   - An orientation-reversing chart?

2. **The Pfaffian local normal form (O2) is stated, not constructed.**
   Lines 1290–1320 name (O2) as "computed from a local Pfaffian normal form at a generic point of each type-II wall," but:
   - The wall geometry is not described.
   - The normal Ext bundle is not computed.
   - The claim $N_\delta^{\mathrm{Pf}} = 1$ (odd rank-one Pfaffian crossing) is asserted, not derived.

3. **Wall-crossing and the cocycle $B(c, c')$ insensitivity:**
   The wall-crossing formula for the DT/OP invariant changes discontinuously when the stability chamber is crossed. The standard cocycle for wall-crossing includes:
   - The quadratic Gram invariants $\Pi(c), \Pi(c'), \Pi(c+c')$.
   - The Mukai pairing $c \cdot c'$.
   - The central charge $Z(c)$.

   **But the manuscript's $B(c, c') = (Q \cdot Q', Q \cdot P' + Q' \cdot P, P \cdot P')$ is purely quadratic in charge-lattice data.** Is this cocycle stable under wall-crossing? Or does wall-crossing force non-additive Gram-lattice corrections?

4. **No explicit wall-crossing computation:**
   The reconstitution plan (line 618) mentions "wall-crossing on the compact Hall category" but does not cite a specific computation (e.g., via Donaldson–Thomas recursion, Kontsevich–Soibelman, or Bridgeland stability). The normal-ordered descent (Part II of the plan) is not yet verified against an explicit wall-crossing formula.

**Damage:**
The orientation character $\epsilon_o$ is conditionally proved once (D0)–(O2) all exist. But (O2) is the missing link: the actual local Pfaffian calculation on the type-II walls. Without it, the claim that $\epsilon_o(s_{\delta_i}) = -1$ emerges from Pfaffian geometry (not scalar convention) is unsupported.

**Severity:** **Critical.** This is the statement (D0)+(O1)+(O1)⁺+(O2) → $\epsilon_o = \nu_{\Delta_5}$ in the Dirac–Pfaffian certificate. (O2) is explicitly open (line 1378). The paper should say "once (O2) is computed" more forcefully, not assume it will work out.

---

### **A6-2-05: Anomaly Cancellation (QME) in the BV Setup — Missing Detail**

**Claim Under Attack:**
Lines 7344, 8213–8244, and elsewhere invoke "QME/anomaly cancellation" as part of the E₃ definition and claim compatibility with PTVV shifted-symplectic form, but do not state the QME explicitly.

**The Problem:**

1. **The BV master equation (QME) is $\{S, S\} = 0$ (with ghost-number convention).**
   For a BRST/BV setup on K3×E with a holomorphic Chern–Simons-like source, the QME is:
   $$\{\mathcal{S}, \mathcal{S}\} = \Delta \mathcal{S},$$
   where $\mathcal{S}$ is the BRST action, $\{\cdot, \cdot\}$ is the Berezinian antibracket (cohomological degree), and $\Delta$ is the BV Laplacian.

   **The manuscript does not write this or specify:**
   - What is $\mathcal{S}$ on K3×E?
   - Does the elliptic Costello–Li trivialization (lines 7284–7307) affect the QME?
   - If QME holds on the elliptic factor independently and on the K3 factor independently, does it hold on the product?

2. **PTVV compatibility is not automatic.**
   Lines 8213–8244 say:
   > "produce the underlying $(-d)$-shifted symplectic form...and PTVV \cite{PTVV2013} produce the same... compatible with the PTVV."

   But PTVV is about *derived* algebraic geometry and symplectic structures. The BV quantization is about *formal* schemes and cohomology. **Are these the same "compatible"?** Or is there an additional Hodge-theoretic comparison needed?

3. **Costello renormalization and cohomological grading:**
   The renormalized Costello–Li flat connection on the elliptic factor (lines 7284–7307) is a specific choice of anomaly cancellation. But:
   - Which anomaly is being cancelled?
   - Is it the anomaly of a chiral bosonic current, a fermionic current, or an affine Kac–Moody algebra?
   - Does the choice of Costello–Li flat connection affect the Weyl-equivariant character (O1)⁺?

4. **No explicit Koszul source coalgebra:**
   Lines 283–284 name "source chiral Koszul coalgebra" and lines 8202–8244 discuss "cobar comparison," but the paper does not:
   - Write the differential on the coalgebra.
   - Verify conilpotence.
   - Check that the cobar construction reduces to the target under Koszul duality.

**Damage:**
The QME is a load-bearing assumption for BV consistency. The paper invokes it without statement or proof. If the elliptic Costello–Li anomaly cancellation interacts nontrivially with the K3 sector or the stabilizer action, the entire BV setup could fail.

**Severity:** **High.** The QME is essential for the algebraic structure but absent from the manuscript as an explicit mathematical statement.

---

### **A6-2-06: "Dirac Block" Rhetoric — Is It Spinor Geometry or Just Notation?**

**Claim Under Attack:**
The reconstitution plan (line 575–577) calls the first-order operator $\mathfrak{D}_X$ "the Dirac operator" and the roadmap defines a "Dirac block" $\mathfrak{D}_\gamma = ((0, 1-x^\gamma), (1, 0))$ (implied by context around Koszul resolution).

**The Problem:**

1. **Dirac operators live on spinor bundles; this is not spinor geometry.**
   A true Dirac operator is:
   - A differential operator $D: \Gamma(\mathcal{S}) \to \Gamma(\mathcal{S})$ where $\mathcal{S}$ is a spinor bundle (or spin structure).
   - It satisfies $D^2 = -\Delta + \text{Ricci}$ (Bochner formula).
   - It has index given by the Atiyah–Singer formula.

   **The Koszul resolution $(0, 1-x^\gamma) \to 1 \to 0$ is the chiral half of a Koszul complex, not a spinor section.**

2. **The claim is rhetorical if no spin structure is supplied.**
   The manuscript uses "Dirac" to evoke the intuition that:
   - There is a first-order object (hence "Pfaffian," not "determinant").
   - It is nilpotent (hence $Q^2 = 0$).
   - It encodes both orientation and structure.

   **But if the underlying geometry is d-critical (BBDJS) or shifted-symplectic (PTVV), these are *not* spinor bundles.** The connection to Clifford algebras or spinor representations is unclear.

3. **Where is the Clifford structure?**
   A Pfaffian makes sense in the context of:
   - Skew-symmetric bilinear forms (orientation on symplectic vector spaces).
   - Clifford algebras and spinor representations.
   - Spin structures on manifolds.

   The manuscript invokes Pfaffian for the orientation line, but does not explain:
   - What is the underlying bilinear form?
   - Is it the PTVV shifted-symplectic form?
   - How does the d-critical cosection interact with it?

4. **Nomenclature risk:**
   Calling $\mathfrak{D}_X$ "the Dirac operator" suggests it is a classical geometric object (e.g., spin Dirac on a manifold, or spin Dirac in a superstring compactification). But it may be purely formal/algebraic. The phrase should be clarified:
   - Is $\mathfrak{D}_X$ a spinor bundle differential operator?
   - Or is it a formal odd derivation $Q: \mathfrak{g} \to \mathfrak{g}[1]$ with $Q^2 = 0$?
   - Or is it something else (e.g., a Koszul map in a derived stack)?

**Damage:**
The name "Dirac" is physically evocative but mathematically imprecise. If the actual object is a cohomological derivation or a Koszul map, it should be called that. If it is a true spinor differential operator, the spin structure and Clifford structure must be constructed explicitly.

**Severity:** **Medium.** The term is rhetorical rather than deceptive, but clarity is needed before the paper is released.

---

### **A6-2-07: Normal Ordering and Cocycle Stability Under Wall-Crossing**

**Claim Under Attack:**
The normal-ordered extension $\Gamma_X = \Gamma_X^{\mathrm{phys}} \oplus_B \Gamma_{\mathrm{gram}}$ and the corrected map $\overline{\Pi}(c, T) = \Pi(c) - T$ are claimed to be stable under wall-crossing of the BPS chamber (lines 558–567, 618).

**The Problem:**

1. **Wall-crossing changes the BPS spectrum, including multiplicities and relations.**
   As the central charge $Z$ is rotated, the set of semistable objects (and their HN filtrations) change. The BPS formula $Z^X_{\mathrm{OP/DT}}$ is a *sum over all BPS states in a given chamber*. When the chamber is crossed:
   - New BPS states appear or disappear.
   - The Gram invariants of the objects change (because the HN filtration changes).
   - The multiplicities $f(nm, l)$ change.

2. **The cocycle $B(c, c')$ is charge-lattice data, independent of stability.**
   But the *physical* BPS states filling out those charges *do* depend on the chamber. The question is:
   - If $\Gamma_X^{\mathrm{phys}}$ is the lattice of possible charges, is every charge $(Q, P) \in \Gamma_X^{\mathrm{phys}}$ realized as a BPS state in *every* chamber?
   - Or do different chambers select different subsets of $\Gamma_X^{\mathrm{phys}}$?

3. **Wall-crossing and the normal-ordered descent:**
   The manuscript (Part II of the reconstitution plan, lines 558–567) claims the normal-ordered descent $\overline{\Pi}_* P_X \cong \mathfrak{g}_{\Delta_5}$ is a *fixed* target algebra. But the Hall algebra $P_X$ itself is chamber-dependent (it is the algebra of endomorphisms in a stability condition). How does the descent respect wall-crossing?

   **The paper does not give a wall-crossing formula for the normal-ordered descent or for the Hall bracket under chamber crossing.**

4. **Stability-chamber dependent compact Hall category (line 618):**
   The roadmap acknowledges "stability-chamber dependent compact Hall category" but then says "automorphic $\Delta_5$ selected by cusp." This is vague: which chamber is "selected by cusp"? Is the cusp of the Siegel upper half-space a preferred chamber? If so, why?

**Damage:**
The normal-ordered descent is presented as chamber-independent, but the underlying Hall algebra is chamber-dependent. Without an explicit wall-crossing formula or a proof that the descent is compatible with wall-crossing, the claim that the full BKM algebra is realized is uncertain.

**Severity:** **High.** Wall-crossing is the central mechanism in DT theory. Ignoring it or being vague about it undermines the physical interpretation.

---

## SUGGESTED HEALINGS

**H6-2-01:** Explicitly state the PTVV shift for CY3 and the cosection defining the d-critical reduction. Add a lemma verifying that the descending Pfaffian line from the (-2)-shifted stack to the (-1)-shifted d-critical quotient is well-defined and compatible with the orientation cocycle.

**H6-2-02:** Separate Joyce–Upmeier orientation descent into steps: (i) global on $\mathrm{Perf}(X)$; (ii) restricted to the K3×E / E quotient sector; (iii) linearized on finite stabilizers; (iv) transported under Weyl action. Mark each step as proved, imported, conditional, or open.

**H6-2-03:** Define the protected $Q$ explicitly (even if formally/schematically) and verify $Q^2 = 0$ in the K3×E compactification with elliptic Costello–Li coupling. State which unitarity/localization theorem is being used and check its hypotheses.

**H6-2-04:** Compute the local Pfaffian normal form on at least one type-II wall explicitly (e.g., the $\delta_1$ wall) and verify $N_{\delta_1}^{\mathrm{Pf}} = 1$. This is the proof of (O2), not an assumption.

**H6-2-05:** Write the BV master equation QME for the chiral Koszul source and verify its compatibility with PTVV via an explicit comparison (Hodge-theoretic or otherwise).

**H6-2-06:** Clarify whether $\mathfrak{D}_X$ is (i) a spinor bundle Dirac operator (supply spin structure and Clifford action), (ii) a formal cohomological derivation (use that terminology), or (iii) a Koszul complex map (define it carefully). Replace vague "Dirac" with a precise name.

**H6-2-07:** Give a wall-crossing formula for the normal-ordered descent: show that if $\overline{\Pi}_*^{\text{chamber 1}} P_X = \mathfrak{g}_{\Delta_5}$ in one chamber, and $\overline{\Pi}_*^{\text{chamber 2}} P_X = \mathfrak{g}_{\Delta_5}$ in another, then the two algebras are isomorphic via a Kontsevich–Soibelman-style cocycle. Or prove that the descent is chamber-independent (hard).

---

## REMAINING RESIDUAL OBSTRUCTION

**RO-1: Compact Hall/Factorization Construction**

The core obstruction is the finite-first pro-object $\mathcal{D}^{\mathrm{DI}}_X = \lim_R \mathcal{D}^{\mathrm{DI}}_{X,R}$ (line 250–270 of the guide). None of the pieces:
- Local protected observable source $A^E_{3,X,R}$.
- Hybrid local/wrapped factorization $F^{\mathrm{hyb}}_{X,R}$.
- Finite orientation $o_R$ with stabilizer trivializations.
- Finite primitive recognition $\mathrm{Rec}_R$ against $\mathfrak{g}_{\Delta_5}$.

are constructed. They are all open. The normal-ordered descent, wall-crossing stability, and BV consistency are conditional on their existence.

**RO-2: Physical vs. Formal**

The paper walks a tight rope between:
- **Formal:** Virtual K₀ determinant, formal current envelope, imported OP/DT scalar square.
- **Physical:** Protected supercharge, BPS wall-crossing, orientation monodromy.

The bridge is the compact Dirac–Igusa certificate, which remains a target, not a construction. Until it is built, the word "physical" is aspiration, not result.

---

**Report status:** Ready for main thread integration. All seven attacks are structural and require explicit repairs in the manuscript or acknowledgment as open problems. No cosmetic fixes suffice.
