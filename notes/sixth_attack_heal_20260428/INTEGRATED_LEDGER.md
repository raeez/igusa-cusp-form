# Sixth Attack–Heal Swarm — Integrated Ledger

**Date:** 2026-04-28
**Wave:** Sixth (post-220-page-critique reconstitution audit)
**Targets:** `reconstitution_plan_20260428.md`, `architecture_realization_status_20260428.md`,
`attack_whitepaper_analysis_20260428_090346_guide.md`, and `main.tex`.
**Six independent attackers, no cross-pollination during attack phase.**
**This document:** main-thread deep-semantic-merge of the six reports per
`~/ecosystem/skills/shared/attack-heal-swarm/protocol.md` §3 "Consolidate".

---

## 0. Lens panel

| Agent | Primary lens | Secondary | Report |
|-------|--------------|-----------|--------|
| A1 | Beilinson — sheaf-theoretic descent, spectral sequences | Drinfeld — chiral/factorization, operads | `agent1_beilinson_drinfeld_factorization.md` |
| A2 | Costello — BV/factorization perturbative QFT, anomalies | Witten — physical consistency, dualities | `agent2_costello_witten_bv_anomaly.md` |
| A3 | Etingof — tensor categories, semisimplicity, deformation | Kazhdan — rigidity, hidden equivalences | `agent3_etingof_kazhdan_algebraic_rigidity.md` |
| A4 | Nekrasov — localization, partition functions, wall-crossing | Gaiotto — defects, generalized symmetries, dualities | `agent4_nekrasov_gaiotto_walls_duality.md` |
| A5 | Standalone reader — cold mathematician | Epistemic status, claim ladder, manuscript form | `agent5_standalone_reader_epistemic_form.md` |
| A6 | Boundary/finite-stage — pro-object existence | Orientation/equivariant cohomology — BE descent | `agent6_orientation_finite_stage_d0.md` |

---

## 1. Stable core (cross-confirmed across ≥2 lenses)

These survive every lens that touched them. They are the dependency-closed
part of the roadmap that the next iteration should not relitigate.

| Item | Confirmed by | Status |
|------|--------------|--------|
| **S-1** Borcherds–Gritsenko–Nikulin product `D₅ = 64⁻¹Δ₅` (imported) | A1, A2, A4 | Imported, externally verified |
| **S-2** Cocycle `B(c,c') = (Q·Q', Q·P'+Q'·P, P·P')` is symmetric, bilinear, normalized 2-cocycle, with polarization identity `B(c,c) = 2Π_X(c)` | A1, A2, A3 | **Proved** (lattice algebra) |
| **S-3** Normal-ordered map `Π̂_X(c,T) = Π_X(c) − T` is a homomorphism `Γ_X → Γ_gram` | A1, A2, A3, A6 | **Proved** |
| **S-4** Central extension `Γ_X = Γ_X^phys ⊕_B Γ_gram` is abelian (via symmetry of B), with explicit identity and inverse | A3 | **Proved** |
| **S-5** Raw-Π descent no-go theorem | A1, A2, A6 | **Proved** at lattice level (see §4 for the one challenged step) |
| **S-6** D6–D2–D0 Mukai–Gram dictionary `Π_X(Q_Y, P_Y) = (h−1, n, d−1)` on K3×E **threefold** with `n = χ(O_Y)`, no Todd correction | A5 | **Proved** (Lemma 5.1 currently rephrased correctly) |
| **S-7** Connected `BE` cohomology `H¹(BE; F₂) = 0`, `H²(BE; F₂) = F₂u₁ ⊕ F₂u₂`, separated from finite stabilizer `E[N]` cohomology | A5, A6 | **Proved**, manuscript fix applied |
| **S-8** Maass character values `ν_{Δ_5}(s_{δᵢ}) = −1` on the three type-II simple reflections (arithmetic, group-theoretic) | A2, A4 | **Imported** |
| **S-9** OP/DT scalar `Z^X_{OP/DT} = −4096 Δ₅⁻²` is orientation-forgetful; the −4096 prefactor is a scalar-branch convention, not orientation data | A2, A4, A5 | **Imported + correctly framed** |
| **S-10** Primitive lift lemma: every `(n,l,m) ∈ ℤ³` lifts to a primitive saturated `(Q,P)` via two orthogonal hyperbolic planes; coefficient-matrix minor = 1 verifies primitivity | A3, A4 | **Proved** |
| **S-11** Naming hygiene: "Dirac–Igusa realization certificate" replaces "compact realization datum" | A5 | Implemented in main.tex:9933 |

---

## 2. Refuted attacks (do **not** drive any rewrite)

The protocol requires the main thread to verify load-bearing attacks before
acting. Two cross-checked here turn out to be mistaken.

### A6-2-01 (Costello/Witten) — INVALID. PTVV dimension was inverted.

The agent claimed PTVV on a CY3 gives a `(−2)`-shifted symplectic structure
(citing `m = 3 → shift = −2`), and concluded the Pfaffian rhetoric belongs in
the CY4 / Borisov–Joyce / Oh–Thomas world rather than CY3.

This is wrong. PTVV (2013) for the moduli of perfect complexes on a Calabi–Yau
`d`-fold gives `(2 − d)`-shifted symplectic. So:

- CY3, `d = 3` → `(−1)`-shifted symplectic. ✓
- CY4, `d = 4` → `(−2)`-shifted symplectic.

`(−1)`-shifted is **exactly** the d-critical / BBDJS / Joyce setting in which
Joyce–Upmeier orientation lives. The roadmap correctly imports CY3 orientation
technology and is not silently using the CY4 mechanism. The Pfaffian rhetoric
in the `(−1)`-shifted setting is the orientation/square-root line bundle on the
moduli of compactly supported coherent sheaves — the right object for K3×E.

**Action:** None. The dimensional mismatch the agent flagged does not exist.
The valid sub-concern (cosection that produces the d-critical chart, i.e. how
the unreduced PTVV `(−1)`-shifted form descends to BBDJS d-critical with a
named cosection) is real but unrelated to the dimension; it is captured by
A6-2-04 below, not A6-2-01.

### A6-3-08 (Etingof/Kazhdan) — INVALID. Polarization identity is universal.

The agent worried that the raw-Π no-go theorem might depend on a specific
choice of physical lift `c_i` of a real simple root `δ_i`, and that a
"different lift" `c'_i` with `Π_X(c'_i) = δ_i` might evade the contradiction
`B(c'_i, c'_i) = 2δ_i ≠ 0`.

This is false. The polarization identity `B(c, c) = 2Π_X(c)` is a *universal
lattice identity*, valid for every `c ∈ Γ_X^phys`. Once `Π_X(c) = δ_i ≠ 0`, we
get `B(c, c) = 2δ_i ≠ 0` regardless of which lift was chosen. The no-go
contradiction is robust under lift choice.

**Action:** None. The no-go theorem (S-5) stands.

The agent's *companion* request — that `[B] ∈ H²_sym(Γ_X^phys; Γ_gram)` be
explicitly stated as nontrivial (A6-3-07) — is valid as exposition. Since
`Π_X` is a genuine quadratic form (not linear), the polarization `B` cannot
be a coboundary `δL` of any linear cochain `L`, so `[B]` is automatically
nontrivial; but the manuscript should say so in one line.

---

## 3. Cross-validated severity-2 attacks (drive the next heal pass)

Each of these is independently flagged by ≥2 agents from different lenses and
survives main-thread verification.

### CV-1. The "holomorphic E₃-factorization algebra" is operadically unspecified

| Source | ID |
|--------|-----|
| A1 (Beilinson/Drinfeld) | A6-1-01 |
| A6 (finite-stage) | A6-6-09 (chiral vs factorization mismatch) |
| A2 (Costello/Witten) | A6-2-05 (QME never written) |

**Broken step:** main.tex:5283–5316 says the source is *equivalently* a
factorization algebra in the holomorphic-E₃-operadic sense, then immediately
that it is "not a constructed functor." It is then used as load-bearing input
in Definition 5283 (the supplied datum) AND as the conclusion of Open Problem
5427. It cannot be both.

**Concretely missing:**
- The operad is unnamed (Costello–Gwilliam holomorphic little-3-disks?
  topological E₃ on holomorphic polydiscs? Francis–Gaitsgory?).
- The formality/framing datum is not specified.
- The QME `{S, S} = 0` and anomaly cancellation are referenced but not written.

**Minimal heal:** pick one operadic model, name it, and state explicitly
which part of the datum is *supplied* vs *open*. If no operad is chosen,
remove "E₃" from theorem-level statements and use "holomorphic factorization
algebra on X" in the conditional clauses; keep "E₃" only in conjectural slogans.

**Blast radius if uncontested:** every theorem citing `A^{E_3}_X` rests on an
undefined operad. The K3→E specialization, hybrid factorization, and primitive
recognition all reference this object.

---

### CV-2. The K3→E specialization `Sp^{ch}_{K3,E}` is three different functors

| Source | ID |
|--------|-----|
| A1 | A6-1-02 |
| A6 | A6-6-09 |

**Broken step:** main.tex:5331–5337 calls `Sp^{ch}_{K3,E}` the
"Beilinson–Drinfeld chiral pushforward along the K3-fibration with K3-integration
in the Costello–Gwilliam sense." This conflates three distinct constructions:
(i) Beilinson–Drinfeld chiral algebras live on Ran(curve) with their own operad;
(ii) Costello–Gwilliam fibre integrals along proper holomorphic submersions;
(iii) ordinary derived pushforward composed with formality. Equivalence between
chiral and factorization algebras requires Gaitsgory-style formality, which is
neither stated nor proved here.

**Minimal heal:** choose **one** interpretation and name source/target
categories. If `Sp^{ch}_{K3,E}` is not yet constructed, mark it as the *only*
component of Open Problem 5427; remove it from the supplied datum.

**Blast radius if uncontested:** the recognition theorem `Π̂_* P_X ≅ 𝔤_{Δ_5}`
quantifies over the output of `Sp^{ch}_{K3,E}`. If the functor is not defined,
the recognition target is vacuous.

---

### CV-3. Hybrid `Ran^{hyb}(E)` associativity is not proved (eight two-step words)

| Source | ID |
|--------|-----|
| A1 | A6-1-03 |
| A6 | A6-6-07 |

**Broken step:** main.tex:6307–6394 lists four operation types
(local-local, local-wrapped, wrapped-local, wrapped-wrapped) and the eight
two-step words `{LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW}`. It records "flag
defects" but does not state which obstruction cochain complex they live in,
and does not prove they vanish.

**Real categorical question:** is `F^{hyb}_X` a *single* factorization
algebra with two strata, or is it `(local factorization algebra) ⋊ (wrapped
module)`? The two have different associativity laws. The wrapped-wrapped
correspondence (with elliptic anchor) is currently a *formal* correspondence,
not an honest finite operation; without rigidification it does not compose.

**Minimal heal:** reframe `F^{hyb}_X` as factorization algebra acting on a
graded module, separate the eight words by which type of structure they test,
and either prove the obstructions vanish at finite stage or list them as open
problems with a named ambient cochain complex.

**Blast radius:** the entire Part III "Compact Dirac–Igusa realization"
hinges on `F^{hyb}_X` being an associative factorization-algebraic object.

---

### CV-4. Wall-crossing compatibility of the normal-ordered descent is unstated

| Source | ID |
|--------|-----|
| A2 (Costello/Witten) | A6-2-04, A6-2-07 |
| A4 (Nekrasov/Gaiotto) | A6-4-07, A6-4-08 |

**Broken step:** the lattice cocycle `B(c,c')` is chamber-independent (it
depends only on Mukai pairings of fixed lattice vectors), but the compact
Hall category is Bridgeland-stability-dependent. The roadmap says the compact
Hall is "stability-chamber dependent, automorphic Δ₅ selected by cusp." This
is a slogan; there is no Kontsevich–Soibelman-style wall-crossing formula
proved compatible with the Π̂_X-descent.

**Specific concerns:**
- Multi-centered BPS bound states in N=4 (Cheng–Verlinde / Sen) record more
  than `(Q²/2, Q·P, P²/2)`: they record splittings and symplectic pairings
  of constituents. The cocycle `B` sees only the Mukai-pairing layer.
- OP/DT is computed in a specific stability chamber; the manuscript imports
  `Z^X_{OP/DT} = −4096 Δ₅⁻²` without specifying which Bridgeland chamber.
- If the compact Hall realization lives in a different chamber than the OP
  chamber, the descent target may shift.

**Minimal heal:** add a conditional theorem (proposed by A4): "If the compact
Hall source `(D0)+(O1)+(O1)⁺+(O2)` is supplied in chamber σ, then `Π̂_X`
remains a homomorphism (lattice fact) and the recognition target is
`𝔤_{Δ_5}` provided the chamber identifications hold." Explicitly
mark chamber-independence as conjectural.

---

### CV-5. Recognition certificate is a checklist, not a constructor

| Source | ID |
|--------|-----|
| A3 (Etingof/Kazhdan) | A6-3-10 |
| A6 (finite-stage) | A6-6-12 |
| A5 (manuscript form) | A6-5-08 |

**Broken step:** Conditions (S1)–(S9) (Cartan, simple representatives,
Chevalley, real Serre, imaginary orthogonality, generation, completed PBW,
Hopf radical, no-extra-relations, full parity dimensions) are *necessary* for
`P_X^Π ≅ 𝔤_{Δ_5}`. The manuscript correctly uses "certificate" terminology
(Definition 10.30). But Theorem 3.10 / Proposition 3.9 still phrase the
implication as "if the certificate exists, then `𝔇_X` is constructed,"
which conflates a precondition list with an existence theorem.

**Minimal heal:** split Theorem 3.10 cleanly into:
- Theorem A (Pfaffian sign, conditional on `(D0)+(O2)`)
- Theorem B (Orientation character, conditional on `(O1)+(O1)⁺` and the
  three sign computations)
- Definition C (the certificate template)

State explicitly: signed dimensions alone are insufficient (zero-bracket
graded super-VS counterexample) — the parity dimensions condition is essential.

**Blast radius:** if the certificate is read as a constructor, the manuscript
overstates. The current renaming + Definition 10.30 mostly fix this, but
upstream theorem statements should be aligned.

---

## 4. High-severity single-agent attacks worth promoting

These were flagged by only one lens but survive main-thread verification and
are mathematically incisive.

### SI-1. Finite-type semistable moduli on K3×E is an unproved hypothesis

**Source:** A6 / A6-6-05.

Lemma `prop:sectorial-hall-truncation` assumes finite-typeness of semistable
substacks at bounded HN height as a hypothesis. Bayer–Macri prove this for
K3 *surfaces*; the K3×E threefold case is not in the cited literature.
Bridgeland stability on `D^b(Coh(K3×E))` is partially developed but a
named finitude theorem at bounded height is not in scope.

**Severity:** 2. If this hypothesis fails, `F_{σ,S}(R)` may be infinite,
`Γ_R^{HN}` may be infinite, the inverse limit loses cofinal finiteness, and
Mittag–Leffler fails.

**Minimal heal:** state the hypothesis explicitly as a standing assumption
in Definition `def:first-order-d0-certificate`, name it as Open Hypothesis
[K3×E-fin], and either cite the closest available result or list it as
the most concrete subordinate problem of the compact realization.

---

### SI-2. Wrapped anchor `λ(A) = det Rp_{E,*}A ⊗ O_E(−χ(A)·0_E)` requires a fixed origin

**Source:** A1 / A6-1-04.

`Pic⁰(E) ≅ E` requires choosing an origin `0_E ∈ E`. The hybrid factorization
asserts E-equivariance of the anchor. The manuscript writes `λ(t·W) = t + λ(W)`
with `+` interpreted as the group law on `E`, which presumes a fixed origin.
Different origins shift `λ` by a constant; transition maps must preserve the
choice.

**Severity:** 2. The E-equivariance of `F^{hyb}_X` is load-bearing in the
hybrid associativity argument; without fixed `0_E` the equivariance is up
to constant, which is a torsor.

**Minimal heal:** fix `0_E ∈ E` once, globally, in the definition of the
hybrid datum. State that the determinant-line transport on the orientation
line `o_{η,R}` compensates for any change of origin (or that no compensation
is needed because `0_E` is part of the fixed datum).

---

### SI-3. Algebraic-Mukai vs full N=4 charge lattice is silent in main.tex

**Source:** A4 / A6-4-04.

`Γ_X^phys = Λ_S ⊕ Λ_S` is the algebraic D6–D2–D0 sector. The full N=4
type-II charge lattice on K3×T² is `Γ^{6,22} ⊕ Γ^{6,22}` (Narain-extended).
The reconstitution plan acknowledges this; main.tex does not, and a hostile
physicist will read "physical microscopic charge lattice" and assume the
full microscopic lattice is meant.

**Severity:** 2 (sociological/expository, but a referee will treat it as
foundational).

**Minimal heal:** insert a one-paragraph remark after the definition of
`Γ_X^phys` stating: "This is the algebraic even Mukai sector relevant to
the OP/DT D6–D2–D0 branch. The full N=4 charge lattice is larger; the
restriction to the algebraic sublattice is the classical OP/DT setup, cf.
[Sen, David–Sen, Maldacena–Moore–Strominger]."

---

### SI-4. Sp₄(ℤ) vs the full T-duality / U-duality group is not derived

**Source:** A4 / A6-4-05.

Sp₄(ℤ) is the modular group of the genus-two automorphic variable, not
the U-duality group of K3×T². A hostile physicist will ask why the full
T-duality of K3×T² factors through Sp₄(ℤ) on `(n,l,m)`.

**Severity:** 2 (same flavor as SI-3).

**Minimal heal:** add a remark/lemma: "Sp₄(ℤ) is the arithmetic symmetry
of the genus-two chemical potential and of the invariant Gram plane; it
is not asserted to be the full U-duality of the compactification." This
matches the language already in the reconstitution plan.

---

## 5. Lower-severity attacks (residuals to track, not to drive rewrite)

| ID | Source | Issue | Disposition |
|----|--------|-------|-------------|
| A6-1-05 | A1 | Hochschild equation `d_Hoch Θ = B_ch` is underdetermined; pentagon is a separate axiom | Keep NO1–NO7 as listed obstructions, state pentagon as an axiom not a consequence |
| A6-1-06 | A1 | Koszul comparison `Θ_{Kos}` mixes chiral and factorization coalgebras | Specify source coalgebra category once; mark Koszul comparison as conjectural |
| A6-2-03 | A2 | Protected supercharge `Q` and unitarity bridge are physics intuition, not written | Cite as open BV/QFT consistency requirement; do not promise more than current scope |
| A6-2-06 | A2 | "Dirac block" rhetoric without spinor data | Cosmetic/expository: clarify in one footnote that "Dirac" means *first-order/Pfaffian*, not classical spinor geometry |
| A6-3-07 | A3 | `[B]` nontriviality not stated explicitly | One-line addition after the cocycle lemma |
| A6-3-11 | A3 | Hopf radical = Lie ideal AND coideal is NO7, not automatic | Already correctly flagged in NO7; cross-reference from recognition certificate |
| A6-4-06 | A4 | Torsion-one vs higher-torsion dyons | Add remark citing Banerjee–Sen–Srivastava for higher-torsion sectors |
| A6-4-08 | A4 | OP/DT chamber selection vs Hall chamber | Subsumed under CV-4 |
| A6-5-06 to A6-5-10 | A5 | Five exposition/order issues in main.tex (OP-sign reading order, Gram-non-additivity foregrounding, abstract clarity, etc.) | Already substantially fixed; small surgical edits |
| A6-6-06 | A6 | Transition maps `ρ_{R'R}` invoked but not constructed | Write at one explicit charge example to ground the inverse limit |
| A6-6-07 | A6 | Eight-word obstruction classes lack ambient cochain complex | Subsumed under CV-3 |
| A6-6-10 | A6 | E[2] linearization characters not computed | Listed as Open Obligation in `architecture_realization_status`; keep open |
| A6-6-11 | A6 | Pro-stack inverse limit may not be representable | Add disclaimer: the compact Dirac–Igusa object is a pro-object, not a stack; recognition is pro-comparison |

---

## 6. Convergence assessment

Per protocol §"Convergence Rule":

1. **Severity 1–3 attack closure:** five severity-2 cross-validated attacks
   (CV-1 through CV-5) and four single-agent severity-2 attacks (SI-1 through
   SI-4) are *open*. Two attacks (A6-2-01, A6-3-08) are *invalid* and closed.
   Eleven lower-severity attacks are residuals.
2. **Healing verification:** no heals attempted in this wave. Heals are
   queued for the next pass.
3. **Live agents:** all six agents have returned. No live agents block.
4. **Worktree isolation:** all six agents were read-only; no isolation
   metadata required.
5. **Stable core:** S-1 through S-11 form a dependency-closed stable core.
   The recognition target `Π̂_*P_X ≅ 𝔤_{Δ_5}` is **not** in the stable core;
   it remains a conditional theorem awaiting CV-1 through CV-5 closure.

**Verdict:** the **algebraic / lattice-theoretic spine is robust**. The
**factorization / hybrid / wall-crossing layer is open in named, surgical
ways** that the next pass should address. The roadmap has not collapsed; it
has been refined.

---

## 7. Recommended next pass (heal queue)

In supremum-discipline order — heal the structurally load-bearing first.

| Priority | Attack(s) | Heal type |
|----------|-----------|-----------|
| 1 | CV-1, CV-2 | Specify operadic model + name `Sp^{ch}_{K3,E}` precisely; or move to Open Problem and remove from supplied datum |
| 2 | CV-3 | Reframe `F^{hyb}_X` as `(factorization) ⋊ (module)`; name obstruction cochain complex |
| 3 | SI-1 | State K3×E semistable finitude as an explicit standing hypothesis; cite closest known result |
| 4 | CV-4 | Add conditional wall-crossing/chamber statement; mark chamber-independence as conjectural |
| 5 | CV-5 | Split Theorem 3.10 into Pfaffian-sign + orientation-character + certificate definition |
| 6 | SI-2 | Fix `0_E ∈ E` in hybrid datum |
| 7 | SI-3, SI-4 | One-remark hedges in main.tex (algebraic Mukai sector, Sp₄ scope) |
| 8 | A6-3-07 | One-line "[B] is nontrivial because Π_X is genuinely quadratic" |
| 9 | A6-5-06 to A6-5-10 | Small surgical edits to main.tex order/emphasis |
| 10 | A6-6-06, A6-6-10, A6-6-11 | Either spell at one example or explicitly mark as residual in the open-obligations ledger |

Items 1–5 are mathematics; items 6–10 are exposition. The mathematics
should be addressed first (heal pass with focused subagents per item) and
exposition swept after.

---

**End of integrated ledger.** Six agent reports preserved alongside in this
directory. No commits made.
