# CLAUDE.md — igusa-cusp-form

> **Inheritance.** `~/ecosystem/INVARIANTS.md` (model-agnostic ecosystem rules);
> `~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`
> (the seven combined voices and the four-part coining test);
> `~/ecosystem/CLAUDE.md` (ecosystem-wide Claude guidance);
> `./AGENTS.md` (Codex / GPT-5-family harness mirror — facts identical, structure and
> voice may differ). On conflict, `INVARIANTS.md` wins.

> **Auto-memory.** `~/.claude/projects/-Users-raeez-igusa-cusp-form/memory/MEMORY.md`
> indexes load-bearing memories: supremum discipline, Beilinson cut, attack-whitepaper
> analyses (incl. 2026-05-09 cross-volume Master Critique), Dirac–Igusa reconstitution
> architecture. Read on session start; update when durable wisdom enters.

The repository carries *The Igusa Square Root: The Borcherds determinant of φ_{0,1},
its denominator algebra, and the K3×E realization problem* — the April 2026
reconstitution of an original 2020 note by Raeez Lorgat.

---

## I. The thesis

The Igusa cusp form Δ_5 of weight 5 on Sp(2,ℤ)\𝓗_2 is one object — one chiral
E_3-algebra **𝔄_{K3×E}** of the K3×E formal target — whose values at five
categorical-dimensional levels are all Δ_5:

  ① **Automorphic.** Δ_5 is the Borcherds–Gritsenko–Nikulin section of the weight-5
     automorphic line over the genus-2 Siegel space.
  ② **Borcherds–Kac–Moody denominator.** Δ_5 is the denominator of a generalized
     Borcherds–Kac–Moody Lie superalgebra g_{Δ_5} on the root lattice Λ_{II}^{2,1}.
  ③ **Compact Pfaffian.** Δ_5 is the protected Pfaffian of 𝔄_{K3×E}, presented at
     finite stage as the pro-object 𝔇_X^DI = lim_R (𝒜_{X,R}^{E_3}, F_{X,R}^{hyb},
     Γ_{X,R}, Π_X, Φ_R, o_R, H_R, P_R^Π, C_{X,R}, Θ_{Kos,R}, ℒ_{Pf,R}, pf_{X,R},
     ε_{o,R}, Rec_R) with eight build algorithms and four named obstructions.
  ④ **Mirror discriminant.** *(Conjectural.)* Δ_5^{-2} is the discriminant of the
     K3-mirror period family; the Igusa programme then sits inside mirror symmetry on
     K3×E.
  ⑤ **Singular theta lift.** Δ_5 is the lift of the weight-zero index-one weak Jacobi
     form φ_{0,1} under the Howe correspondence Mp(4,ℝ) ↔ O(3,2), bridged by the
     exceptional isomorphism Sp(4) ≅ Spin(3,2).

The cross-level identities ①↔②, ②↔⑤, ①↔⑤ are theorems (Borcherds 1995,
Gritsenko–Nikulin 1998). The cross-level identity ②↔③ — the Pfaffian–Dirac theorem —
is the conditional contribution of this manuscript: under (D0), (O1), (O1⁺), (O2),

  Pf_{prot}(𝔇_X^DI) = Δ_5,    ε_o = ν_{Δ_5},    P_X ≅ g_{Δ_5}.

The level-n scalar shadow Z_BPS^{K3×E} = (Φ_{10}^{un})^{-1} = Δ_5^{-2} on the closed
K3×E ↦ point cobordism is the BPS partition function; promotion to a 3d gravitational
path integral requires the Hall–Borcherds residual (Vol II) and is not claimed.

## II. The chapter spine

| Part | Ch. | Content |
|---|---|---|
| Frontispiece | — | Five-fold thesis (~50 lines) |
| 0 — Road map | 1 | Pentadic Δ_5 (~300) |
| I — Given | 2 | K3×E setup, Mukai dictionary, lattice polarization, normal-ordered Gram, hybrid Ran^{hyb}(E) carrier (~1500) |
| | 3 | Borcherds–Gritsenko–Nikulin import (View ①) (~800) |
| | 4 | BKM denominator algebra g_{Δ_5} (View ②): Cartan, Chevalley, real and imaginary roots, denominator identity (~2500) |
| | 7 | Singular theta lift (View ⑤); Sp(4) ≅ Spin(3,2) bridge (~600) |
| II — Built | 5 | The Dirac–Igusa pro-object 𝔇_X^DI (View ③) — §5.1 Ran^{hyb}(E); §5.2 cosection-twisted reduced d-critical orientation; §5.3 Hall correspondences; §5.4 Dirac + Pfaffian; §5.5 Koszul source coalgebra; §5.6 primitive recognition; §5.7 eight build algorithms; §5.8 four obstructions (~5000) |
| III — Certified | 6 | The cross-level identity ②↔③: the Pfaffian–Dirac theorem, ε_o = ν_{Δ_5}, the primitive recognition theorem P_X ≅ g_{Δ_5} (~3000) |
| IV — Shadowed | 8 | Mirror discriminant (View ④, conjectural) (~400) |
| | 9 | Z_BPS^{K3×E} = Δ_5^{-2}; Hall–Borcherds residual; the K3×E threefold realization question (~1000) |
| | 10 | Open obstructions and the next frontier — Mathieu / umbral moonshine adjacency (~500) |
| Appendices | A–F | Lattice computations; Borcherds-product expansion; Mukai–Gram dictionary; Hall-correspondence proofs; Pfaffian wall normal-form; eight build algorithms in pseudocode (~3000) |

Total ~18,600 lines. The reorganization is structural; ~90% of the content is already
written and rearranges; ~10% (Chs. 7, 8, 10) is new.

## III. The Beilinson cut

A statement is not allowed to be primitive if it is only true after choosing a boundary
object, passing to a trace, averaging from ordered to symmetric, taking a protected
index, completing a category, imposing endpoint hypotheses, or installing descent data.
**Reconstitution order: primitive objects first, cross-level identities second, scalar
shadows last.**

Every load-bearing claim locates itself on one of two chains, which are the same chain
seen from two entry points, meeting at the holomorphic factorization algebra Φ_d^{FA}:

```
(X, D, τ) → C^op → b → A_b → Bar(A_b) → Z^{der}_{ch}(A_b) → Tr_C / Θ_C → scalar
CY_d-cat → E_d-HolFA(X) → Sp^{ch}_{Σ_{d-1}, C} → chiral shadow → Y^+ → G → κ-tuple
```

**Banned identifications.** Each row is a categorical-dimensional level confusion;
delete the left, install the right. Audit before every commit.

| Banned | Required |
|---|---|
| "the boundary algebra A is the primitive open object" | "C is the primitive factorization dg-category on (X, D, τ); A_b = End_C(b) is the chart at boundary vacuum b" |
| "Bar(A) = bulk" | "Bar(A) = MC twisting / coupling coalgebra; Z^{der}_{ch}(A) ≃ ChirHoch^•(A,A) = bulk" |
| "the closed chiral algebra is modular" | "the open category carries cyclic trace + clutching; the closed shadow has modular consequences" |
| "the κ-invariant of K3×E" (singular) | "the κ-tuple (κ_cat, κ_ch^Hodge, κ_ch^Heis, κ_BKM, κ_fiber) = (0, 0, 3, 5, 24) — cat-Hodge / refined-Hodge / Heisenberg rank / cusp-form weight / χ_top(K3). The additive collapse κ_BKM = κ_ch + χ(O_fiber) confuses χ_top(K3) = 24 with χ(O_K3) = 2 and fails at N = 1 (Vol III counterexample)." |
| "Δ_5 = compact BPS Hilbert space" | "Δ_5 is the protected scalar shadow of 𝔄_{K3×E}; the operator-level package is 𝔇_X^DI as a pro-object, conditional on (D0), (O1), (O1⁺), (O2)" |
| "Z_BPS = 3d gravitational path integral" | "Z_BPS is the level-n protected trace of 𝔄_{K3×E}; the path-integral promotion requires the Hall–Borcherds residual and is not claimed" |
| "Universal Holography constructs quantum gravity" | "Universal Holography identifies (boundary = A, bulk = Z^{der}_{ch}(A), interaction = SC^{ch,top}-brace); for A = Vir_c this is the holographic HT sector of pure 3d gravity, not the dynamical metric path integral" |
| "Y^+(X) = G(X)" | "Y^+(X) is the Hall positive half; G(X) is the Drinfeld double, after pairing / completion / integral form / stable-envelope transport" |
| "CoHA(ℂ³) = W_{1+∞}" | "CoHA(ℂ³) = Y^+(gl_1); W_{1+∞} appears after Drinfeld doubling / centre / vacuum evaluation" |
| "6d hCS = 3d Chern–Simons in disguise" | "6d hCS supplies Φ_3^{FA} on verified loci; the one-loop obstruction is ∫_X Tr_{ad}(A(F_A)^3), quartic" |
| "formal local Hamiltonian BF ⇒ global compact target" | "formal Darboux + descent / QME / anomaly / locality + (local Hamiltonian or vanishing holomorphic de Rham obstruction) ⇒ candidate compact target" |
| "PVA λ-Jacobi ⇒ all-loop quantum HT theory" | "λ-Jacobi gives classical gauge invariance; all-loop quantum theory needs KZ analytic SDR + Stokes + reflected weights + lift of T = [Q_{tot}, G]" |
| "W_∞[λ] ⇒ E_∞ from finite spin checks" | "spin-≤8 checks are evidence; the E_∞ endpoint is conditional on Prochazka triangular truncation, Creutzig–Kanade–Linshaw parafermion compatibility, Pope–Romans–Shen / Bakas, Yamada weight-window" |
| "quadratic chiral duality = chiral Koszul duality" | "Hom(A,B) ↪ MC(A^! ⊗ B) injection; Koszulness is the separate theorem in a homotopy setting" |
| "class M works chain-level in ordinary complexes" | "class M holds in the completed ambient (analytic HS-sewing / coderived BV = bar / weight-completed / pro / J-adic)" |
| "smooth projective fourfold" (in §5) | "K3×E threefold; n = χ(O_Y) directly" |
| "Bott-element B(c, c) = 2 Π(c) explanation" | "lattice polarization B is the full structural content; the Bott-element framing is removed" |
| "the OP minus sign sources the orientation character" | "the OP minus sign is a scalar branch convention; ε_o = ν_{Δ_5} on W^{(2)}(Λ_{II}^{2,1}) is fixed by group theory + one local Pfaffian wall computation" |

Three Δ_5 names live in the manuscript and must be tagged distinctly on first use per
chapter: the automorphic section D_X = Δ_5 (View ①); the BKM denominator
den(g_{Δ_5}) = 64^{-1} Δ_5(2Z) (View ②); the compact protected Pfaffian
Pf_{prot}(𝔇_X^DI) (View ③, conditional). The handle "Δ_5" alone never substitutes for
any of the three.

## IV. Voice and standards

`~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`
governs every sentence of `main.tex`, every theorem statement, every commit message,
every conversation turn about manuscript content. The seven combined voices are Witten,
Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. A sentence that does not state
mathematics or physics is a defect.

Standard-terminology rule (`STANDARDS §II`): the accepted name in algebra, geometry,
number theory, homotopy theory, or mathematical physics is the default. Coining
requires the four-part test (`STANDARDS §III`): scope (no accepted name covers it),
material (precise mathematical object, not attitude or workflow), subject (Greek/Latin
or composition with accepted prefixes), inner yearning (the structure forces the name).
Most failures of writing in this constellation come from coining terms that have an
accepted mathematical name; the accepted name is the default; the coining bears the
burden of proof.

Binding terminology for this manuscript: Igusa cusp form, Siegel modular form,
Borcherds product, theta lift, Borcherds–Kac–Moody (BKM) algebra, denominator formula,
Weyl–Kac character formula, factorization algebra (Beilinson–Drinfeld; not synonymous
with vertex algebra or chiral algebra), vertex operator algebra, chiral algebra
(`D`-module on a curve), derived chiral centre Z^{der}_{ch}(𝒞), perfect obstruction
theory, virtual fundamental class [X]^{vir}, Mukai vector, Mukai lattice, Donaldson–
Thomas (DT) / Pandharipande–Thomas (PT) / Maulik–Nekrasov–Okounkov–Pandharipande
(MNOP), CHL (Chaudhuri–Hockney–Lykken) point. The handle "Δ_5" works in this repo;
in manuscript prose specify "Φ_{10}^{1/2}" or "the level-five Borcherds–Kac–Moody
denominator" on first occurrence per chapter. Φ_{10} = χ_{10}.

Banned rhetorical patterns (`STANDARDS §V`): meta-narration ("we now turn to"),
bookkeeping ("Theorem A, Theorem B"), catalogue IDs ("phase j", "wave N", "round M"),
branding ("matrix microscope", "magic identity", "inner music", "X spine"), hedging
("we believe", "essentially", "arguably"), negative framing for identifications ("would
collapse", "cannot identify"), approximation language for exact equalities ("is closely
related to" when "$=$" holds), computer-science vocabulary ("certificate" → "identity"
or "theorem"; "pipeline" → "construction"; "spec", "schema", "API", "metadata"
forbidden in body prose).

Honest epistemic status on every load-bearing claim: *proved / conjectured / heuristic
/ computed / expected / folklore / unverified*. Use *one proves* for proved statements,
*it is expected that* for conjectures, *heuristically* for physics arguments without
mathematical footing — followed by whatever rigour is available. Mathematical-repair
doctrine (`INVARIANTS.md §XI`): heal the proof, statement, or construction; never
delete, demote, or quietly narrow scope as a way to close a defect.

## V. Long-form proof harness

For Claude Code: maximum-effort mode. The manuscript is frontier modular-form theory
(Borcherds product / BKM / Igusa cusp form). No downgrade.

1. **Context before invention.** Load `main.tex`, `proj.bib`, the cited Borcherds 1995 /
   Gritsenko–Nikulin 1998 / Igusa 1964 / Gritsenko–Cléry sources, `compute/` fixtures,
   the swarm reports under `notes/swarm_*/reports/`, and the Vol II / Vol III /
   mixed-holomorphic-topological-strings cross-repo anchors before the first mathematical edit. Build an
   internal outline; do not write from memory.
2. **Multiple independent routes.** For any load-bearing identity, seek independent
   derivations: worked Fourier coefficient, lattice convention check, primary
   literature, local computation, cross-repo consistency. Agreement is evidence;
   disagreement is the deliverable.
3. **Adversarial loop.** After every proposed repair, attack the strongest failure
   mode: sign, character, Weyl vector, divisor normalization, multiplier system,
   exponent, false transfer into Vol III. Heal, then attack again. Convergence: no
   fatal objection survives; one mathematical improvement is inscribed.
4. **Long runs are normal.** A 30–60 minute agent run is acceptable when a proof
   obligation requires it. Stop only when the proof closes, a computation decides the
   point, or the exact open obligation is named.
5. **Subagents provide evidence, not authority.** The main thread integrates by deep
   semantic merge (`INVARIANTS.md §VII`). Verify numeric / file-existence / behavioral
   claims against ground truth before propagating to canonical docs (§IX).
6. **Mathematical repair doctrine** (`INVARIANTS.md §XI`). Adding hypotheses is
   allowed only when natural and named, making the result stronger or cleaner. The
   manuscript moves upward or stops.
7. **Memory.** Update `~/.claude/projects/-Users-raeez-igusa-cusp-form/memory/` when
   durable wisdom enters: feedback (rules learned), project (state changes), reference
   (external sources). Recall before assuming staleness; verify against current state.

## VI. Research constellation

| Repo | Role | Interaction with this repo |
|---|---|---|
| `~/chiral-bar-cobar` | Vol I — Modular Koszul Duality (bar / cobar, Koszul) | Bar / Z^{der}_{ch} firewall; class M completion; chiral Koszulness as separate theorem. den(g_{Δ_5}) is a chiral shadow, not bulk. |
| `~/chiral-bar-cobar-vol2` | Vol II — A_∞-Chiral Algebras and Chiral Hochschild Cohomology | Primitive package (X, D, τ; C^op, b, A_b, Z^{der}_{ch}(C), Θ_C, Tr_C); Universal Holography master theorem (boundary = A, bulk = Z^{der}_{ch}(A), interaction = SC^{ch,top}-brace); modular functor as trace + clutching; Hall–Borcherds residual; KZ analytic SDR for finite-jet PVA. |
| `~/calabi-yau-quantum-groups` | Vol III — Calabi–Yau quantum groups / κ-stratification | κ-ladder (0, 0, 3, 5, 24); two-stage CY_d-Cat → E_d-HolFA(X) → ChirAlg(C); Drinfeld doubling Y^+ → G; 6d hCS quartic obstruction. The κ_BKM = 5 entry is this manuscript's value; the 8-row Gritsenko–Cléry catalogue carries the row producing Δ_5. |
| `~/chiral-bar-cobar-vol4` | Vol IV — Realization | Modular functor at level 5; scalar partition function at level n. |
| `~/mixed-holomorphic-topological-strings` | BCOV / Kodaira–Spencer companion | Local model ℝ²_{top} × ℂ²_{hol} + brane completion; global obstruction = holomorphic de Rham obstruction class. Z_BPS^{K3×E} = Δ_5^{-2} does not promote to the global target via formal Hamiltonian BF; Vol II's Hall–Borcherds residual carries the bridge. |

Load-bearing claims about Δ_5, φ_{0,1}, Borcherds-product exponents, the BKM
denominator, or the κ-ladder must be consistent across these repos. Disagreement is the
deliverable; report, do not silently reconcile.

## VII. Obstruction discharges

The cross-level identity ②↔③ on K3×E is **unconditional at the chiral-shadow level**,
granted the four-obstruction discharge of Appendix G:

| Obstruction | Statement | Discharge |
|---|---|---|
| (D0) | D0-degeneration limit of the cosection-reduced d-critical orientation theory | Theorem G.1 (Joyce–Upmeier + Bojko + Mittag–Leffler) |
| (O1) | Strong reduced orientation on the K3×E-quotient self-Ext frame bundle | Theorem G.3 (Joyce–Upmeier + Bojko + Klein-four lemma G.1 + P³-Pin^c lemma G.2) |
| (O1⁺) | Weyl-equivariant transport along W^{(2)}(Λ_{II}^{2,1}) reflections | Theorem G.4 ((3,3,3) abelianisation + Maass character match) |
| (O2) | Local Pfaffian wall normal form + (R1)↔(R2) reconciliation | Theorems G.5–G.7 (rank-one App E + Weyl-orbit transport + 4096 = 2^{χ_top(K3)/2}) |

The Vol II Hall–Borcherds residual is also discharged on K3×E (Theorem G.10): the
Vol II Universal Holography master-theorem hypotheses (UH.1)–(UH.5) are verified on
(K3×E, D, τ) at boundary vacuum b (Lemma G.9), and the master theorem
`[\S 9, Theorem A]{ChiralBarCobarVolII}` is applied to obtain the bulk trace
`Tr^{bulk}_n((-1)^F · id)_{Z^{der}_{ch}(C_X)} = -4096 Δ_5^{-2}`.

The Pfaffian–Dirac theorem `thm:ch6-pfaffian-dirac`, the orientation-character match
`thm:ch6-orientation-character`, the primitive recognition theorem
`thm:ch6-primitive-recognition`, and the Z_BPS bulk promotion all hold
**unconditionally on K3×E** modulo the correctness of the Vol II master theorem
itself — a strictly cleaner conditioning than the original four-obstruction-plus-residual
status.

The five-fold thesis is closed on K3×E: ① ↔ ② proved (Borcherds–Gritsenko–Nikulin);
② ↔ ③ proved at the chiral-shadow level (Theorem G.10); ② ↔ ⑤ proved (Borcherds 1995);
③ ↔ ⑤ chained through ② via the singular-theta lift (Theorem 7.x); ④ remains
conjectural per CLAUDE.md §I (mirror discriminant).

## VIII. Source layout and build

- `main.tex` — root TeX (memoir class, EB Garamond body, newtx math, shared template
  symlinked from `~/latex-template/`).
- `proj.bib` — bibliography.
- `Makefile` — `make` runs `pdflatex → bibtex → pdflatex → pdflatex`. Build at session
  end when useful; do not rebuild after every edit.
- `out/main.pdf` — local artifact; ignored by Git.
- `notes/swarm_*/reports/` — swarm ledgers (A001–A290+). Source of truth for the swarm
  state of the four obstructions.
- `compute/` — numerical fixtures (build target presentation; source verification).
- `materials/raw/` — adversarial review PDFs (incl. 2026-04-30 attack-whitepaper,
  2026-05-09 cross-volume Master Critique).
- `presentation.key` — companion Keynote.

`~/ecosystem/INVARIANTS.md §X` open-source whitelist applies to any external-facing
artifact. This repo is closed-source and ships no externally-visible artifact citing
closed-source paths.

## IX. Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for igusa-cusp-form (Igusa cusp-form, Borcherds products, denominator identities, modular-form companion; closed-source):

1. **Think Before Coding.** Every modular-form-edit names the cusp / denominator-identity / Borcherds-product touched, the lattice / Weyl-vector data, and the claim-status macro.
2. **Simplicity First.** Modular-form companion is the scope; no speculative weight extensions, no new product identities ahead of need. Five-fold thesis (① ↔ ② ↔ ③ ↔ ⑤ chain) is the canonical landmark.
3. **Surgical Changes.** A denominator-identity edit does not opportunistically refactor the Borcherds-product chapter. The four-obstruction-plus-residual discharge (Appendix G, K3×E) is its own surface — do not touch beyond Appendix G when working there.
4. **Goal-Driven Execution.** Success = `make` (four-pass `pdflatex → bibtex → pdflatex → pdflatex`) clean at session end, theorem ledger consistent, voice-scan + term-coining test pass, modular-form checks (denominator identities, Borcherds expansions) verified.
5. **Use the model only for judgment calls.** Cross-references and bibliography deterministic. Modular-form arithmetic computations are deterministic — verify, do not LLM-approximate.
6. **Token budgets are not advisory.** Monograph; checkpoint between Borcherds-product / cusp-form sections and between the five-fold thesis vertices.
7. **Surface conflicts, don't average them.** Cross-volume statements with chiral-bar-cobar / Vol II / Vol III canonical at the chiral side where they share an artifact; flag drift here. A numerical Fourier coefficient disagreement with a cited source halts and reports — trust the source, do not overwrite from memory.
8. **Read before you write.** Read the affected Borcherds expansion or denominator identity before editing. Cross-reference primary literature for any modular / Jacobi / BKM / lattice formula.
9. **Tests verify intent.** Claim-status macros honest; modular-form check passes verify computed identities, not just compilation. The five-fold thesis status (proved / conjectural / chained-through) is the load-bearing claim ledger.
10. **Checkpoint after every significant step.** Between sections, summarize modular-form-check delta and five-fold thesis status.
11. **Match the codebase's conventions, even if you disagree.** raeez-math-template per `INVARIANTS.md §XII`. Theorem environments per template. memoir / EB Garamond / newtx typography. Elementary-derivation style: lattice → root datum → Weyl vector → product → modular form.
12. **Fail loud.** Surface every failed denominator identity; never silently substitute heuristic for checked. Never derive a Fourier coefficient from memory. Cross-volume / source-vs-prose disagreements halt and report. Repo is closed-source — never write a public path or proprietary-tree reference.
