# Seventh Attack–Heal Swarm — Integrated Ledger

**Date:** 2026-04-28
**Wave:** Seventh (orthogonal-lens reaudit, post-wave-6 ledger)
**Targets:** `reconstitution_plan_20260428.md`, `architecture_realization_status_20260428.md`,
the Dirac–Igusa architecture memory, and `main.tex` post-2A2 deep scrub.
**Six independent attackers, no cross-pollination during attack phase.**
**This document:** main-thread deep-semantic-merge of the six reports per
`~/ecosystem/skills/shared/attack-heal-swarm/protocol.md` §3 "Consolidate".

The wave was deliberately chosen to attack at angles **orthogonal** to wave 6:
concrete small-case computations, renormalization/anomaly content, higher
categorical coherence of the inverse limit, Hall convolution via Borel–Moore
homology, manuscript internal consistency, and boundary/degeneration behavior.

---

## 0. Lens panel

| Agent | Primary lens | Secondary | Report |
|-------|--------------|-----------|--------|
| A1 | Gelfand — concrete examples, small-case verification | Arithmetic check on B(δ_i,δ_j) and Borcherds exponents | summary in agent task output |
| A2 | Polyakov — renormalization, anomalies | RG vs modularity, BV pairing, Wess–Zumino consistency | summary in agent task output |
| A3 | Kapranov — higher categorical coherence | A∞ vs E∞, Mittag–Leffler, completed PBW, pro-Lie algebra | summary in agent task output |
| A4 | Ginzburg — Borel–Moore homology, Hall convolution | Chriss–Ginzburg pull-push, Joyce vanishing-cycle CoHA | `agent4_ginzburg_bm_homology.md` |
| A5 | Manuscript migration — reference integrity | Theorem-status ledger, forbidden language, isolated reads | `agent5_manuscript_migration_consistency.md` |
| A6 | Boundary/degeneration — cusps, walls | Singular K3, nodal E, walls of marginal stability, imprimitive classes | `agent6_boundary_degeneration.md` |

Three reports landed as files (A4, A5, A6). Three (A1, A2, A3) returned through
their task summaries because of a tooling regression mid-wave; their analyses
are quoted from the task notifications and treated with the same evidence
standards as the on-disk reports.

---

## 1. Stable core (cross-confirmed across waves 6 and 7)

The wave-6 stable core S-1 through S-11 holds. Wave 7 added concrete arithmetic
verification on top of the algebraic verification of wave 6.

| Item | Wave-7 confirmation | Status |
|------|--------------------|--------|
| **S-1** Borcherds–Gritsenko–Nikulin product `D₅ = 64⁻¹Δ₅` | A1 (arithmetic), A2 (RG-side) | Imported, externally verified |
| **S-2** Cocycle `B(c,c')` symmetric, polarization `B(c,c) = 2Π_X(c)` | A1 small-case check: `B(δ_1, δ_2) = (1, 1, 1)` triggers no-go correctly | **Proved** |
| **S-3** Normal-ordered map `Π̂_X(c,T) = Π_X(c) − T` | A4 (lattice algebra clean), A6 (correctly grades) | **Proved** |
| **S-4** Central extension `Γ_X = Γ_X^phys ⊕_B Γ_gram` abelian | A4, A6 | **Proved** |
| **S-5** Raw-Π descent no-go | A4 (Hall-convolution side), A6 (boundary side) | **Proved** at lattice level |
| **S-6** D6–D2–D0 Mukai–Gram dictionary on K3×E threefold | A5: zero "fourfold" hits; A6 PASS A7-6-04 | **Proved** |
| **S-7** Connected `BE` cohomology separated from finite-stabilizer | A5 (no stale references) | **Proved** |
| **S-8** Maass character `ν_{Δ_5}(s_{δᵢ}) = −1` | A1 confirms via Borcherds product sign computation; `c(0,1)` exponent = −2 ⇒ sign | **Imported** |
| **S-9** OP/DT scalar `Z^X_{OP/DT} = −4096 Δ₅⁻²` orientation-forgetful | A2 RG-side: this is a Behrend-weighted scalar count, not orientation transport | **Imported + correctly framed** |
| **S-10** Primitive lift lemma | A6 PASS A7-6-04 | **Proved** |
| **S-11** Naming hygiene | A5 confirms all renames in place | Implemented |

**Wave-7 specific positive evidence (concrete-examples lens, Gelfand A1):**

- The polarization identity `B(δ_i, δ_i) = 2δ_i ≠ 0` was verified arithmetically
  on the three real simple roots `δ_1 = 2f_2 − f_3`, `δ_2 = 2f_{−2} − f_3`,
  `δ_3 = f_3` with explicit lifts `c = (Q, P)`. The no-go contradiction is
  triggered as advertised in every case.
- The arithmetic check `c(1,1) = 29` for `2φ_{0,1}` and `c(0,1) = −2` together
  with the leading exponent in the Borcherds product reproduce the expected
  signed sub-product structure; the architecture survives the small-case test.
- The DMVV-like exponent `f(0, l)` boundary contribution at `m = 0` is
  consistent with the cusp/Weyl boundary statement of A6.

---

## 2. Refuted attacks (do **not** drive any rewrite)

### A7-3-01 (Kapranov / higher coherence) — Soft, not refuted but reframed

The agent flagged `A∞ vs E∞` for the source factorization algebra and worried
that the "completed PBW" was being claimed without strict coassociativity.

**Main-thread verdict:** the manuscript already states the completed PBW step
as conditional in the recognition certificate (S5/S7 conditions of the
certificate), not as a strict theorem. A∞ vs E∞ is captured by CV-1 (operadic
model unspecified) and is not a separate attack.

**Action:** subsume into CV-1 / CV-3.

### A7-2-02 (Polyakov / RG) — Soft

The agent worried about a central charge mismatch between the source theory
and the Igusa target. **Main-thread verdict:** there is no claim in the
manuscript that the source CFT and the Igusa cusp form share a central charge.
Δ_5 is a Siegel cusp form of weight 5; the central charge of a putative
source CFT is a separate datum.

**Action:** none. The "central charge mismatch" is a category error; we are
comparing a representation count (cusp form coefficients) against a hypothetical
CFT, and the manuscript does not commit to a CFT realization.

---

## 3. Cross-validated severity-2 attacks (drive the next heal pass)

Each is independently flagged by ≥2 agents from different lenses or
cross-validates against a wave-6 attack.

### CV7-A (= wave-6 CV-1 + Polyakov + Kapranov + Ginzburg)
**The operadic model is still unspecified, AND the BV scheme for anomaly
cancellation is still unwritten.**

| Source | ID |
|--------|-----|
| Wave 6 | CV-1 |
| A2 (Polyakov) | A7-2-01 (BV scheme unspecified), A7-2-03 (Costello–Li connection unnamed), A7-2-06 (Wess–Zumino consistency) |
| A3 (Kapranov) | A7-3-02 (A∞ vs E∞), A7-3-04 (orientation operadic) |
| A4 (Ginzburg) | A7-4-08 (CoHA convolution order ambiguous) |

**Status:** wave 6 recommended naming Costello–Gwilliam holomorphic
factorization on holomorphic polydiscs, OR removing E_3 from theorem-level
clauses. Wave 7 confirms the same heal is needed and adds: the BV master
equation must be stated explicitly as a hypothesis of the supplied datum, not
asserted as a derivable consequence.

**Minimal heal:** in `main.tex` near the source-algebra definition (~5283),
add a line naming the factorization model and explicitly listing
"BV master equation `{S, S} = 0` (open obligation)" as a separate item of
the open problem.

---

### CV7-B (= wave-6 CV-3 + Ginzburg's full A7-4 package)
**Hybrid `F^{hyb}_X` is operadically informal AND its Hall convolution is
unproved at the level of properness, transversality, and orientation.**

| Source | ID |
|--------|-----|
| Wave 6 | CV-3 |
| A4 (Ginzburg) | A7-4-01 (properness), A7-4-02 (TS transversality), A7-4-03 (orientation O1), A7-4-04 (infinite fibers), A7-4-05 (coproduct via p_!), A7-4-07 (NO7 unverified) |
| A6 (Boundary) | A7-6-10 (wall-of-marginal-stability) |

This is the **largest cross-validated attack** in either wave. Six independent
defects are identified:

1. Properness of source/target maps `p, q` on the extension stack ℰ.
2. Thom–Sebastiani transversality on ℰ.
3. Joyce–Upmeier orientation O1 (still open).
4. Finite-dimensionality of fibers of `p`.
5. Coproduct via `p_!` (same issue as #4).
6. Hopf-radical-as-coideal verification at finite stage.

**Wave-6 heal proposal stands:** reframe `F^{hyb}_X` as `(factorization
algebra) ⋊ (graded module)`, name obstruction cochain complex.

**Wave-7 strengthening:** **explicitly list properness, transversality, and
orientation as hypotheses of the Dirac–Igusa certificate**, not as derived
features. Then the certificate is honest: *if* these data exist, *then* the
Hall product is well-defined and the primitive recognition target is `𝔤_{Δ_5}`.

This is the recommendation made by Ginzburg (A4) and aligns with the
Etingof/Kazhdan recommendation in wave 6. **Heal is decisive.**

---

### CV7-C (Mittag–Leffler descent, new in wave 7)
**The pro-Lie inverse limit `lim_R 𝔇^DI_{X,R}` is not shown to satisfy
Mittag–Leffler.**

| Source | ID |
|--------|-----|
| A3 (Kapranov) | A7-3-03 (Mittag–Leffler not verified) |
| A3 (Kapranov) | A7-3-06 (pro-Lie vs Lie distinction) |

**Concrete defect:** The compact Dirac–Igusa pro-object is `lim_R 𝔇^DI_{X,R}`
where `R` is the HN-height truncation parameter. For this inverse limit to
behave well (lim¹ = 0), the transition maps `ρ_{R'R}` must be surjective on
finite-stage homotopy groups.

The manuscript names `ρ_{R'R}` (~line 6905 area) but does not prove
Mittag–Leffler.

**Severity:** 2. If Mittag–Leffler fails, the recognition target is *not* a
Lie algebra in the strict sense — it is only a pro-Lie object, and
`Π̂_*P_X ≅ 𝔤_{Δ_5}` becomes a pro-comparison statement, not an isomorphism.

**Minimal heal:** add Mittag–Leffler / `lim¹ = 0` to the supplied datum as an
explicit hypothesis. Or weaken the recognition statement to a pro-isomorphism
and acknowledge in the open problem text.

---

### CV7-D (= wave-6 CV-4 + Polyakov RG-vs-modular)
**Wall-crossing / RG / chamber dependence still unstated.**

| Source | ID |
|--------|-----|
| Wave 6 | CV-4 |
| A2 (Polyakov) | A7-2-05 (RG-vs-modular bridge unnamed) |
| A6 (Boundary) | A7-6-10 (BPS splitting at walls) |

**Status:** wave 6 heal pending. Wave 7 confirms.

**Minimal heal:** add a conditional statement marking chamber-independence as
conjectural, as proposed in wave 6.

---

### CV7-E (Manuscript-level conditional phrasing — A7-5-01)
**Line 12070 reads "is constructed" without conditional qualifier in the
sentence.**

| Source | ID |
|--------|-----|
| A5 (Migration) | A7-5-01 |

**Status:** isolated phrasing issue confirmed. Local heal: change to "If [...]
were constructed, then [...]".

---

## 4. High-severity single-agent attacks worth promoting

### SI7-1. Wrapped chiral Koszul not constructed (Kapranov A7-3-03)

The wrapped sector requires its own Koszul comparison; the local sector's
Koszul is operadic (E_3) but the wrapped sector lacks a written Koszul-Tate
duality.

**Severity:** 2. The recognition certificate expects `BE`-equivariant
descent through Koszul on both strata.

**Minimal heal:** state the wrapped Koszul comparison as an open obligation
in the certificate, not as a derivable feature.

---

### SI7-2. CY3 cyclic structure on factorization side (Kapranov A7-3-08)

PTVV gives `(−1)`-shifted symplectic on CY3, hence cyclic A∞ structure on
the moduli's tangent complex. The manuscript references "cyclic" indirectly
through the Pfaffian / orientation language but does not state cyclicity
explicitly.

**Severity:** 2 (expository / structural). The cyclic structure is what makes
Joyce–Upmeier orientation theory applicable.

**Minimal heal:** one-line addition to the orientation section: "Joyce–Upmeier
orientation requires the cyclic A∞ structure induced by the `(−1)`-shifted
symplectic on the CY3 moduli, supplied by PTVV."

---

### SI7-3. m=0 sector physical identification open (Boundary A7-6-05)

The m=0 sector is correctly named as a cusp/Weyl boundary, but the
physical identification (wrapped sector? wall-crossing? degenerate D-branes?)
is not justified.

**Severity:** 2. Foundational clarity.

**Minimal heal:** add a remark that the m=0 boundary terms in the Borcherds
product are imported from Gritsenko–Nikulin's automorphic regularization,
NOT derived from a microscopic count, and that their physical identification
is part of the open compact-realization problem.

---

### SI7-4. Constructions/Algorithms not labeled as environments (Migration A7-5-03)

The 220-page critique demanded 15 Constructions and 8 Algorithms. The current
manuscript has zero `\begin{Construction}` or `\begin{Algorithm}` environments;
the procedures are embedded in lemma proofs.

**Severity:** 1 (presentation, not content). May be by design.

**Disposition:** keep procedures embedded in proofs but cross-reference them
by procedure name in the introduction. Do not add 15 Construction blocks
unless explicitly requested by user.

---

### SI7-5. Higher braces on chiral side (Kapranov A7-3-07)

The chiral algebra side carries higher braces (Tamarkin) and the manuscript
uses bracket notation `{,}` without specifying which `n`-bracket.

**Severity:** 1 (taxonomic / mostly cosmetic).

**Minimal heal:** add a footnote stating that brace operations beyond the
2-bracket are not used in the present construction; if higher braces appear
in the wrapped Koszul, they must be supplied as explicit hypotheses.

---

## 5. Lower-severity attacks (residuals to track)

| ID | Source | Issue | Disposition |
|----|--------|-------|-------------|
| A7-2-04 | A2 | Path-integral measure unspecified | Subsumed under CV7-A (BV scheme) |
| A7-2-07 | A2 | BV pairing not stated | Subsumed under CV7-A |
| A7-3-09 | A3 | Vanishing-cycle transport up the inverse system | Subsumed under CV7-B |
| A7-4-06 | A4 | Primitive subspace category unspecified | Specify category in recognition certificate as super-vector spaces |
| A7-5-02 | A5 | 62 orphan labels | Hygiene; either cite or remove |
| A7-5-04 | A5 | Abstract does not headline thesis (ii) | Optional one-sentence addition |
| A7-5-06 | A5 | Abstract does not foreground (n,l,m) as Gram-degree, not Hall-charge | One-sentence addition to abstract |
| A7-6-06 | A6 | s=0 cusp boundary not analyzed | Add open-question remark |
| A7-6-07 | A6 | Imprimitive curve classes deferred | Add deferral remark |
| A7-6-08 | A6 | Singular K3 limit not addressed | Add explicit "S smooth K3" assumption |
| A7-6-09 | A6 | Nodal E limit not addressed | Add explicit "E smooth elliptic" assumption |
| A7-6-11 | A6 | Multi-component charges deferred | Subsumed under CV7-B |
| R7-4-01 to R7-4-03 | A4 | Global TS multiplicativity, normal-ordering compatibility, Behrend-weighted count | Listed as residuals in §4 of A4 report; cross-link from open obligations |

---

## 6. Convergence assessment

Per protocol §"Convergence Rule":

1. **Severity 1–3 attack closure across both waves:**
   - Refuted: wave 6 (A6-2-01, A6-3-08) + wave 7 (A7-3-01 reframed, A7-2-02 category error). Total 4.
   - Cross-validated severity 2 (driving heal): wave 6 CV-1 through CV-5 + wave 7 CV7-A through CV7-E. CV7-A subsumes CV-1; CV7-B subsumes CV-3; CV7-D subsumes CV-4. **Net unique cross-validated:** CV7-A, CV7-B, CV7-C (new), CV7-D, CV7-E (new), CV-2, CV-5.
   - Single-lens severity 2: SI-1 through SI-4 (wave 6) + SI7-1 through SI7-5 (wave 7). Total 9.
2. **Healing verification:** no heals attempted before wave 7; this ledger feeds the heal pass that immediately follows.
3. **Live agents:** all 12 agents (waves 6 + 7) have returned. No live agents block.
4. **Worktree isolation:** all agents read-only; no isolation metadata required.
5. **Stable core:** S-1 through S-11 hold across both waves and survive the
   Gelfand small-case arithmetic stress test.

**Verdict:** the **algebraic / lattice-theoretic spine is robust, confirmed
twice from orthogonal lenses**. The **factorization / hybrid / Hall-convolution
layer is open in named, surgical ways**, and Mittag–Leffler / pro-Lie
descent has been added to the open list. The roadmap has not collapsed; it
has been refined twice.

The manuscript is in a state where the heal pass should focus on:
(a) explicit naming of the operadic model and BV scheme,
(b) reframing F^{hyb} as factorization+module with named obstructions,
(c) stating finite-type / Mittag–Leffler / orientation as standing
hypotheses of the certificate,
(d) splitting the recognition theorem,
(e) one-paragraph hedges on Mukai sector, Sp_4, and (n,l,m) Gram nature.

---

## 7. Recommended heal queue (combined waves 6 + 7)

In supremum-discipline order — heal the structurally load-bearing first.

| Priority | Attack(s) | Heal type | Where in main.tex |
|----------|-----------|-----------|-------------------|
| 1 | CV7-A (operad+BV) | Name Costello–Gwilliam holomorphic factorization OR remove E_3 from theorem-level | ~5283–5316 |
| 2 | CV7-B (hybrid+Hall) | Reframe F^{hyb} as factorization+module; list properness/TS/orientation as hypotheses | ~6307–6451 |
| 3 | CV7-C (Mittag–Leffler) | Add lim¹ = 0 hypothesis to supplied datum | def:first-order-d0-certificate |
| 4 | CV-2 (Sp^{ch}_{K3,E}) | Pick one interpretation, name source/target categories | ~5331–5337 |
| 5 | SI-1 (K3×E finite-type) | State as standing hypothesis [K3×E-fin] | def:first-order-d0-certificate |
| 6 | CV7-D (chamber/wall) | Add conditional chamber statement | wall section |
| 7 | CV-5 (Theorem 3.10 split) | Split into Theorem A (Pfaffian), Theorem B (Orientation), Definition C (certificate) | Section 3 / Theorem 10.30 area |
| 8 | SI-2 (0_E origin) | Fix 0_E in hybrid datum | hybrid section |
| 9 | SI-3, SI-4, SI7-3 | One-paragraph remarks (algebraic Mukai sector, Sp_4 scope, m=0 boundary identification) | charge lattice section, cusp form section |
| 10 | A6-3-07 + A7-5-06 | One-line "[B] nontrivial because Π_X is genuinely quadratic"; abstract note on (n,l,m) being Gram-degree | abstract + cocycle lemma |
| 11 | CV7-E + A7-5-01 | Fix line 12070 conditional phrasing | line 12070 |
| 12 | SI7-1, SI7-2, SI7-5 | Wrapped Koszul as open obligation; cyclic A∞ note; brace footnote | orientation/Koszul sections |
| 13 | A7-6-06 to A7-6-09 | Smooth K3 / smooth E assumption stated in introduction | introduction |
| 14 | A7-5-02, A7-5-04 | Orphan labels audit; abstract clarity (optional) | various |

Items 1–7 are mathematics; items 8–14 are exposition. Per user authorization
"rewrite the manuscript if need be", the main thread proceeds with items 1–11
in `main.tex`.

---

**End of integrated ledger.** Twelve agent reports preserved across the
sixth and seventh wave directories. No commits made.
