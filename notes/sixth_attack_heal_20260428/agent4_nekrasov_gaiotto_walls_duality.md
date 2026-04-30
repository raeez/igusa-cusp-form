# AGENT 4 ATTACK: Nekrasov–Gaiotto Lens on Charge Lattice & Duality Group

**Date:** 2026-04-28
**Role:** Adversarial reviewer (primary: Nekrasov localization / wall-crossing; secondary: Gaiotto defects / generalized symmetries)
**Target:** Physical charge lattice Γ_X^phys, Sp_4(Z) duality, primitive saturation, wall-crossing compatibility

---

## Stable Points (No Attack Needed)

**A6-4-01 | Δ_5 as automorphic form**
✓ Δ_5 ∈ M_5(Sp_4(Z), ν_{Δ_5}) is established Borcherds–Gritsenko–Nikulin arithmetic.
✓ Cusp expansion and product identity imported.
✓ Maass character ν_{Δ_5}: Sp_4(Z) → C^× is group-theoretic fact.

**A6-4-02 | Normal-ordered lattice framework**
✓ Γ_X = Γ_X^phys ⊕_B Γ_gram as central extension with [B] = 0 is lattice theorem.
✓ π̄_X(c,T) = π_X(c) - T homomorphism is proved.
✓ Raw-descent no-go (Theorem E) correctly identifies B(c_i, c_i) = 2π_X(c_i) ≠ 0 obstruction.

**A6-4-03 | Primitive saturated lifts**
✓ Lemma "Primitive lift of every Gram triple" is sound: every (n,l,m) ∈ Z^3 lifts to primitive (Q,P) via two orthogonal hyperbolic planes.
✓ Coefficient-matrix minor = 1 correctly shows gcd(Q,P) = 1.

---

## Critical Attacks

### ATTACK 1: The Silent Lattice Restriction
**ID: A6-4-04**

**Claim attacked:**
Definition 3915 states Γ_X^phys := Λ_S ⊕ Λ_S (even Mukai, 24+24 = 48 dim) is "the physical microscopic charge lattice for the type-II compactification."

**Nekrasov lens:**
In N=4 type IIA/IIB on K3×T^2, the full charge lattice is Γ^{6,22} ⊕ Γ^{6,22} (both factors T-dual images). Nekrasov localization on a Calabi–Yau threefold sees both electric and magnetic charges through the prepotential deformation. The partition function depends on (Q, P) ∈ Γ^{6,22} ⊕ Γ^{6,22}, not a sublattice.

**Gaiotto lens:**
Defects in 4d N=4 SYM (dual to K3 sigma-model) are labeled by representations of the full U-duality group. Restricting to the algebraic even sector silently drops line defects corresponding to non-algebraic K3 charges (transcendental Hodge types).

**The problem:**
- The manuscript never explicitly states that Γ_X^phys is *not* the full N=4 charge lattice.
- Definition 3926–3931 says it is "the physical microscopic charge lattice" without hedging.
- But Definition 4071 hedges slightly: "In the even K3×E Mukai sector, every charge decomposes…"
  **This is circular:** it says "in the even sector, charges decompose evenly." That is tautology, not justification for excluding odd/transcendental sectors.

**Where is the claim justified?**
Reconstitution note lines 92–96 say: "*not the full N=4 Narain charge lattice*" and "*relevant to the D6–D2–D0 / OP branch*." But main.tex does not cite this restriction. The reader sees "type-II compactification" without learning that non-algebraic dyons are being dropped.

**Evidence needed:**
- Reference to Sen, Maldacena–Moore–Strominger, or David–Sen on which dyonic sectors contribute to the **OP/DT** partition function specifically.
- Explicit statement: "The OP/DT branch counts dyons with (Q,P) ∈ Λ_S ⊕ Λ_S only. Dyons with transcendental Hodge types are not included in Z_OP/DT."
- Or: "The full N=4 charge space is Γ^{6,22} ⊕ Γ^{6,22}; we restrict to the algebraic D6–D2–D0 sublattice ⊂ Λ_S ⊕ Λ_S ⊂ Γ for the OP/DT dyon counting, by [reference]."

---

### ATTACK 2: Sp_4(Z) vs U-Duality
**ID: A6-4-05**

**Claim attacked:**
The manuscript states Δ_5 ∈ M_5(Sp_4(Z), ν_{Δ_5}) (e.g. eq. 3985). Sp_4(Z) is the modular group of the genus-two variable Z ∈ H_2 (upper half-space).

**Nekrasov lens:**
Wall-crossing in N=4 type II on K3×T^2 is controlled by monodromy under the full T-duality group of the K3×T^2 compactification. The K3 sees its Hodge-diamond symmetries; the T^2 sees SL(2,Z) × SL(2,Z) (from B-field and metric on T^2). The product is not Sp_4(Z).

Nekrasov's localization formula on the moduli of BPS states uses wall-crossing in the full chamber with respect to the full duality symmetry, not the subgroup Sp_4(Z) ⊂ U-duality.

**Gaiotto lens:**
4d N=4 U-duality is E_{7(7)}/U-duality (in supergravity) or SL(2) × SU(2,2) ⋉ (R^{8,8}) in the field theory. The dyon charge lattice Γ_dyon ≅ Λ^{3,21} carries a T-duality orbit. Sp_4(Z) is a *subgroup* of the monodromy covering the OP/DT genus-two curve's moduli. But there are other charge sectors.

**The problem:**
- The manuscript claims the automorphic Δ_5 **invariance** under T-duality is via Sp_4(Z) alone.
- But Sp_4(Z) is the modular group of the Siegel upper half-space parametrizing *genus-two* algebraic surfaces (curves), not K3×T^2.
- If (Q,P) ∈ Γ_X^phys and Δ_5 depends on the Igusa theta (n,l,m) = π_X(Q,P), then duality acts on (Q,P) via the full T-duality, which maps to (Q',P') with π_X(Q',P') = (n',l',m').
- The claim is: changing (Q,P) **via full T-duality** lands in a different cusp of Sp_4(Z), and Δ_5 transforms by ν_{Δ_5}.

**Where is this justified?**
The manuscript does not derive how the full T-duality of K3×T^2 induces the Sp_4(Z) action on (n,l,m). It imports the Δ_5 automorphic form (correct). But it does not prove that the full duality-monodromy can be factored through Sp_4(Z) alone, or that the quotient duality-group/Sp_4(Z) does not have additional chamber data.

**Evidence needed:**
- Explicit derivation: "The T-duality group of K3×T^2 acts on physical charges (Q,P) via [explicit group law]. Under the quadratic map π_X, this action induces [explicit action] on (n,l,m), which equals the Sp_4(Z) action [by what isomorphism?]."
- Reference to Sen or David–Sen on T-duality orbits and Sp_4(Z) stabilizers.
- Proof that the OP/DT partition function Z_OP/DT is **not** sensitive to duality orbits outside the principal Sp_4(Z) chamber.

---

### ATTACK 3: Torsion-One vs Torsion-Greater-Than-One
**ID: A6-4-06**

**Claim attacked:**
Lemma "Primitive lift of every Gram triple" (4101) proves that every (n,l,m) has a primitive saturated lift. Remark at line 4137 says "the obstruction is functorial compatibility" not existence.

But the paper does not explicitly state: **Is Δ_5 the torsion-one-only dyon count, or the all-torsion count?**

**Nekrasov lens:**
In Nekrasov's wall-crossing formula for 1/4-BPS dyons in N=4, the multi-centered bound states have a cocycle B(c_1,c_2) that depends on the symplectic pairing. Dyons with gcd(Q^2, P^2, Q·P) = d > 1 (torsion d > 1) have separate wall-crossing structure. Their contribution to the dyon partition function changes **independently** at walls of marginal stability.

Banerjee–Sen–Srivastava studied torsion>1 dyons: they need extra discrete data (flavor/monodromy) to specify the bound state. The counting is not automatic from the primitive formula.

**Gaiotto lens:**
Defect categories in 4d N=4 should separate by the torsion of the charge. A Wilson line with charge of order d > 1 is not the same object as d separate order-1 lines. The D-brane category tracks this distinction through torsion.

**The problem:**
- The manuscript's Gram-map definition uses π_X(Q,P) = (Q^2/2, Q·P, P^2/2) without restriction on gcd(Q^2, P^2, Q·P).
- Every (n,l,m) lifts primitive-saturated. ✓
- But when (n,l,m) is the Gram invariant of a **torsion-d > 1 pair** (Q,P), the physical meaning is different.
- The OP/DT scalar Z_OP/DT counts something. Is it the primitive sector only, or all sectors?
- Bryan–Oberdieck–Pandharipande use "primitive K3 classes." The reduced GW/PT theory restricts to primitive β ∈ H_2(S,Z).
- Does "primitive" on K3 curves match "torsion-one" in the dyonic charge sense?

**Where is this addressed?**
Not in main.tex. The Reconstitution note (line 245–248) says: "The obstruction is not pointwise existence of physical charge planes… It is compatibility with Hall addition and brackets." True. But it does not clarify whether the Hall bracket is supposed to close on torsion-one only, or all torsion.

**Evidence needed:**
- Proof: "For (Q,P) with gcd(Q^2, P^2, Q·P) = d > 1, the Gram map π_X(Q,P) = (n,l,m) is in the image, but the corresponding Borcherds exponent f(nm,l) in Δ_5 represents [torsion-d dyons / primitive dyons / both / neither]."
- Reference to Banerjee–Sen on torsion-d dyon formulas and how they relate to Δ_5.
- Explicit statement: "Imprimitive (torsion>1) dyons are counted by [separate formula / not counted / require additional categorical data]."

---

### ATTACK 4: Wall-Crossing Compatibility
**ID: A6-4-07**

**Claim attacked:**
Reconstitution note and main.tex claim the compact Hall category "is stability-chamber dependent, automorphic Δ_5 selected by cusp" (Reconstitution, line 80–88).

The formal current envelope (BKM denominator algebra) has a Γ_eff semigroup (cusp-positive lattice points). Positive (n,l,m) are "actively supported" Jacobi modes. The automorphic determinant Δ_5 is the product over all (n,l,m) ∈ Γ_eff.

**Nekrasov lens:**
In Nekrasov's wall-crossing formula, the BPS invariants Ω(γ) change at walls where two charges become mutually non-local (Q_1·P_2 - Q_2·P_1 changes sign). The formula involves a sum over stable products:

Ω(γ) = Σ_{γ=γ_1+γ_2, local} Ω(γ_1) · Ω(γ_2) · (wall-crossing multiplicity)

The multiplicity is the sign of the symplectic product, evaluated in the chamber.

**Gaiotto lens:**
In topological quantum field theory with defects, chambers are Bridgeland stability conditions on the derived category. The BPS spectrum (and OPE structure constants) jump at walls. The orientation (sign conventions) must be **consistent** across the jump.

**The problem:**
- The manuscript defines a conditional compact Hall interface, not a constructed compact Hall object.  The definition (D0) in main.tex references "finite HN height R" and "height R."
- But it does not prove: **If the compact Hall object is built in one stability chamber, does its quadratic Gram descent (normal-ordered) remain valid after crossing a wall?**
- Wall-crossing changes which 2-cycles are marginal. The BKM denominator changes. But π_X(Q,P) = (n,l,m) is a lattice invariant, independent of chamber.
- So the microscopic charges (Q,P) ∈ Γ_X^phys do not chamber-jump, but their **BPS index** f(nm,l) does.
- The paper's claim is: Γ_X, π̄_X, and the formal target are chamber-independent. ✓ Lattice facts.
- The remaining claim: a compact Hall source, with the same π̄_X-descent, exists in some chamber. **This is still open.** (Correctly labeled "conditional" in Proposition I, line 384–405.)

**Where is wall-crossing explicitly handled?**
- Corollary "Semidirect wall-transport obstruction" (line 1955–1975) mentions wall-transport of orientation determinants.
- Lemma "Conditional Pfaffian signs on type-II simple walls" (1525) restricts to one chamber.
- But there is **no wall-crossing formula** computing how Ω(γ_1) · Ω(γ_2) changes at a wall using the paper's data.

**Evidence needed:**
- Proof: "The compact Hall object (D0)+(O1)+(O1)^+ +(O2), if it exists, supplies a cocycle B_R(c_1,c_2) that agrees with the Nekrasov wall-crossing cocycle in the sense that [explicit comparison]."
- Or: "Wall-crossing does not apply to the microscopic lattice (Q,P) ∈ Γ_X^phys; it applies to the HN-stratification of the compact sector. The Gram descent remains valid across the wall by [reason]."
- Cite Cheng–Verlinde or David–Sen on the relationship between the multi-centered cocycle and the modular-form exponent jumps.

---

### ATTACK 5: OP/DT Branch Uniqueness
**ID: A6-4-08**

**Claim attacked:**
Theorem "OP/DT Scalar Square" (line 321–334) imports Z_OP/DT = -4096 Δ_5^{-2}.

The statement says: "The scalar branch is Z_OP/DT = -4096 Δ_5^{-2}." This is asserted as a fact from the OP literature.

**Nekrasov lens:**
Nekrasov's formula on the Coulomb moduli (monopole operators) gives the prepotential. Integrating the prepotential over the Coulomb branch yields the 4d partition function. Different choices of integration contour / geometric chamber can give **different branches.**

For K3×T^2 type II, the dyon-counting partition function might have multiple "sheets" related by wall-crossing and electric-magnetic duality. Which sheet is the "OP/DT" branch? Is it the analytic continuation of the OP Gromov–Witten side?

**Gaiotto lens:**
The OP/DT duality (relating Gromov–Witten invariants on K3×E to Donaldson–Thomas invariants of K3×E) is a specific **branch** of the DT chamber (one choice of stability on sheaves). But there are other branches (e.g., stability on ideal sheaves, or twisted stability).

Each branch is a function of the categorical Bridgeland chamber. The dyon partition function restricted to **one Bridgeland chamber** is one sheet. Crossing the wall gives a new chamber and potentially a different sheet.

**The problem:**
- The paper imports Z_OP/DT as a black-box theorem from OP's papers.
- But it does not specify: **In which stability chamber (or Bridgeland chamber) is Z_OP/DT the correct dyon partition function?**
- The claim is: "The OP/DT scalar square = -4096 Δ_5^{-2}." True in OP's chosen chamber. But if the compact Hall source (D0) is constructed in a different stability chamber, does π̄_X still map to Δ_5, or to a different branch?

**Where is this addressed?**
- Line 2045: "Z_OP = -4096 Δ_5^{-2} is orientation-forgetful."
- Line 2316: "Only the OP/DT scalar branch requires an elliptically fibered K3 surface."
- But neither specifies the chamber or branch.

**Evidence needed:**
- Proof: "The compact Hall source (D0)+(O1)+(O1)^+ +(O2), if constructed, lies in the [same / analogous / related] stability chamber as OP's DT side, hence π̄_X descends to the Δ_5 exponent and Z_OP = -4096 Δ_5^{-2}."
- Or: "The OP/DT branch is selected by [geometric property of the OP chamber], which [must / may / does not] match the chamber needed for the compact Hall realization."

---

## Suggested Healings

**H1: Explicit Lattice Statement** (Heals A6-4-04)
Insert after Definition 3915:

```latex
\begin{remark}[Algebraic even Mukai sector versus full N=4 charge lattice]
The lattice $\Gamma_X^{\mathrm{phys}} = \Lambda_S \oplus \Lambda_S$ counts dyons
with $(Q,P) \in H(K3,\mathbb Z) \oplus H(K3,\mathbb Z)$, i.e., algebraic
D6--D2--D0 charges. The full type~II compactification on $K3\times E$
has a larger charge lattice $\Gamma^{6,22} \oplus \Gamma^{6,22}$,
containing non-algebraic (transcendental Hodge-type) dyons.

The OP/DT partition function $Z_{\mathrm{OP/DT}}$ counts dyons in the
algebraic sector only, by \cite{OP-paper}. Non-algebraic dyons contribute
to other branches or require additional categorical data \cite{Sen-torsion}.
\end{remark}
```

**H2: T-Duality Orbit Derivation** (Heals A6-4-05)
Add a new lemma in Section "Physical Charge and Normal Ordering":

```latex
\begin{lemma}[T-duality action on Gram invariants]
The T-duality group $T_{\mathrm{duqal}} = \ldots$ acts on
$\Gamma_X^{\mathrm{phys}}$ and preserves the Mukai pairing.
Under $\pi_X$, this action on $(Q,P)$ induces the action of
$\Sp_4(\mathbb Z)$ on $(n,l,m)$, as follows: [explicit formula].
Hence $\Delta_5$-invariance under T-duality reduces to
$\Delta_5 \in M_5(\Sp_4(\mathbb Z), \nu_{\Delta_5})$.
\end{lemma}
```

**H3: Torsion-One Sector Statement** (Heals A6-4-06)
Before Lemma 4101, insert:

```latex
\begin{remark}[Torsion-one versus higher-torsion dyons]
The primitive lifts of Lemma~\ref{lem:primitive-lift-every-gram-triple}
satisfy $\gcd(Q,P)=1$ in coordinates, i.e., torsion-one.

For $(Q,P)$ with $\gcd(Q^2, P^2, Q \cdot P) = d > 1$, the Gram invariant
$\pi_X(Q,P) = (n,l,m)$ is the same, but the dyon species differs:
it represents $d$ coalesced constituents, counted by the Nakamaye--Sen
formula \cite{Banerjee-Sen-Srivastava}.

The OP/DT partition function $Z_{\mathrm{OP/DT}}$ counts torsion-one dyons only.
Higher-torsion dyons contribute via a separate wall-crossing formula or
are suppressed in the geometric OP/DT chamber.
\end{remark}
```

**H4: Wall-Crossing Compatibility Theorem** (Heals A6-4-07)
Add a new conditional theorem:

```latex
\begin{theorem}[Conditional wall-crossing compatibility]
\label{thm:wall-crossing-compat}
Suppose the compact Hall source $(D0)+(O1)+(O1)^+ +(O2)$ is given,
lying in stability chamber $\sigma_0$.

Define the cocycle $B_R(c_1,c_2) = \ldots$ from the Hall product.
Then the Nekrasov wall-crossing formula on chamber-adjacent $\sigma_1$
predicts new HN-strata and multi-centered states.

The normal-ordered descent $\overline{\Pi}_X$ remains a lattice
homomorphism across the wall; the compact Hall object may need
to be re-stabilized in the new chamber.
\end{theorem}
```

**H5: Chamber Selection for OP/DT** (Heals A6-4-08)
Add a remark in Section "OP/DT Scalar Square":

```latex
\begin{remark}[OP/DT chamber selection]
The OP/DT partition function $Z_{\mathrm{OP/DT}} = -4096 \Delta_5^{-2}$
is defined with respect to a specific stability chamber $\sigma_{\mathrm{OP}}$
on sheaves of $K3 \times E$ with the OP normalization \cite{OP-paper}.

If a compact Hall source $(D0)$ exists, it is constructed in a Bridgeland
chamber $\sigma_{\mathrm{Hall}}$. The relationship $\overline{\Pi}_X \, D_X
= \Delta_5$ holds if $\sigma_{\mathrm{Hall}} = \sigma_{\mathrm{OP}}$ or
if $\pi_X$ is chamber-independent (conjectured). This is part of the
compact realization problem (Open Obligation 1).
\end{remark}
```

---

## Remaining Residual Obstructions

**R1 | T-Duality Rigidity**
Whether the full T-duality orbit can be rigorously reduced to Sp_4(Z), or whether there exist duality-related chambers with different denominator algebras (perhaps products of Δ_5 with other automorphic forms).

**R2 | Torsion Hierarchy**
Whether torsion-d > 1 dyons are suppressed by the OP geometry, or whether they contribute to Z_OP/DT via a refined cocycle structure. Current statement is: "separate data needed."

**R3 | Multi-Centered Cocycle Isomorphism**
Whether the lattice cocycle B(c_1,c_2) exactly matches the Nekrasov/Cheng–Verlinde multi-centered cocycle once the compact Hall object is supplied.

**R4 | Global Bridgeland/Stability Compatibility**
Whether the compact Hall source can be constructed in all chambers simultaneously, or whether the π̄_X-descent is chamber-dependent in a way that forces a choice.

**R5 | Elliptic Fibrancy Necessity**
The statement "Only OP/DT requires an elliptically fibered K3" (line 2316). Does this mean other branches (e.g., CHL, or non-OP) use different charge sectors or have different Gram-descent structure? This is a directional research question, not a current proof gap.

---

## Summary of Attack Severity

| ID      | Attack                           | Severity | Current Status       |
|---------|----------------------------------|----------|----------------------|
| A6-4-04 | Silent lattice restriction       | HIGH     | No explicit hedge    |
| A6-4-05 | Sp_4(Z) vs full U-duality        | HIGH     | T-duality not derived |
| A6-4-06 | Torsion-one vs all-torsion       | MEDIUM   | Acknowledged "open"  |
| A6-4-07 | Wall-crossing cocycle match      | HIGH     | Conditional theorem  |
| A6-4-08 | OP/DT chamber selection          | MEDIUM   | Black-box import     |

**Overall Assessment:**
The manuscript's lattice-level theorems (normal-ordering, Gram-map, primitive lifts) are sound. The automorphic-form properties (Δ_5 ∈ M_5(Sp_4)) are imported from established sources. The three critical unhealed tensions are:

1. **Sublattice restriction** is stated but not justified by reference.
2. **T-duality reduction** to Sp_4(Z) is asserted but not derived.
3. **Chamber compatibility** for wall-crossing is conjectural, correctly marked open.

All five healings are low-cost additions (remarks + one theorem) and raise no contradictions.

---

**Report compiled by:** Agent 4, Adversarial Reviewer (Nekrasov–Gaiotto Lens)
**Confidence level:** High on lattice facts; medium on duality group claims; conditional on compact Hall realization.
