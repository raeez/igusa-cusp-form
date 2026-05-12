# AGENTS.md — igusa-cusp-form

> **Inheritance.**
> - `~/ecosystem/INVARIANTS.md` — model-agnostic ecosystem rules (§I destructive-git
>   prohibition; §II worktree concurrency; §III standalone-document discipline;
>   §IV Russian-school voice; §V every-file-into-the-repo; §VI no-LLM-attribution;
>   §VII deep-semantic-merge; §IX code-not-prose verification; §XI mathematical-repair
>   doctrine; §XII shared LaTeX template).
> - `~/ecosystem/AGENTS-HARNESS.md` — Codex / GPT-5-family harness calibration
>   (`reasoning_effort`, agentic eagerness, tool use, tool preambles, persistence and
>   stop conditions, verbosity, uncertainty handling, self-reflection rubric, scope
>   discipline, error handling).
> - `~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`
>   — the seven combined voices (Witten, Etingof, Polyakov, Dirac, Feynman, Costello,
>   Gaiotto), the four-part coining test (§III), standard-terminology table (§IV),
>   prohibited rhetorical patterns (§V), notation discipline (§VI).
> - `./CLAUDE.md` — Claude Code mirror. AGENTS.md and CLAUDE.md must not diverge in
>   facts; they may differ in structure and voice. Before editing this file, read
>   `./CLAUDE.md`. On conflict, `INVARIANTS.md` wins.

> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model.
> `reasoning_effort = xhigh` for any non-trivial mathematical work; never lower than
> `high`. Russian-school voice (`INVARIANTS.md §IV`). No LLM attribution on commits
> (`INVARIANTS.md §VI`). The private ChatGPT Pro harness is not public; this file
> encodes the open analogue: deepest model, maximum reasoning effort, large context,
> tool-grounded verification, repeated attack-and-repair iterations.

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
| | 4 | BKM denominator algebra g_{Δ_5} (View ②) (~2500) |
| | 7 | Singular theta lift (View ⑤); Sp(4) ≅ Spin(3,2) bridge (~600) |
| II — Built | 5 | The Dirac–Igusa pro-object 𝔇_X^DI (View ③) — §5.1 Ran^{hyb}(E); §5.2 cosection-twisted reduced d-critical orientation; §5.3 Hall correspondences; §5.4 Dirac + Pfaffian; §5.5 Koszul source coalgebra; §5.6 primitive recognition; §5.7 eight build algorithms; §5.8 four obstructions (~5000) |
| III — Certified | 6 | The cross-level identity ②↔③ (~3000) |
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

**Banned identifications.** Eighteen rows of categorical-dimensional level confusion
to delete and install. The full table is `./CLAUDE.md §III` (loaded first per Codex
load order §XI); identical content, audited before every commit. Highest-frequency
rows for this manuscript: "Δ_5 = compact BPS Hilbert space" → "Δ_5 is the protected
scalar shadow of 𝔄_{K3×E}; the operator-level package is 𝔇_X^DI"; "Z_BPS = 3d
gravitational path integral" → "Z_BPS is the level-n protected trace; promotion needs
the Hall–Borcherds residual"; "the κ-invariant" → "the κ-tuple (0, 0, 3, 5, 24);
additive collapse confuses χ_top(K3) = 24 with χ(O_K3) = 2"; "smooth projective
fourfold" → "K3×E threefold; n = χ(O_Y)".

Three Δ_5 names live in the manuscript and must be tagged distinctly on first use
per chapter: the automorphic section D_X = Δ_5 (View ①); the BKM denominator
den(g_{Δ_5}) = 64^{-1} Δ_5(2Z) (View ②); the compact protected Pfaffian
Pf_{prot}(𝔇_X^DI) (View ③, conditional). The handle "Δ_5" alone never substitutes
for any of the three.

## IV. Voice and standards

`STANDARDS.md` governs every sentence of `main.tex`, every theorem statement, every
commit message, every conversation turn about manuscript content. The seven combined
voices are Witten, Etingof, Polyakov, Dirac, Feynman, Costello, Gaiotto. A sentence
that does not state mathematics or physics is a defect.

Standard-terminology rule (`STANDARDS §II`): the accepted name in algebra, geometry,
number theory, homotopy theory, or mathematical physics is the default. Coining
requires the four-part test (`STANDARDS §III`). Most failures of writing in this
constellation come from coining terms that have an accepted mathematical name; the
accepted name is the default; the coining bears the burden of proof.

Binding terminology: Igusa cusp form, Siegel modular form, Borcherds product, theta
lift, Borcherds–Kac–Moody (BKM) algebra, denominator formula, Weyl–Kac character
formula, factorization algebra, vertex operator algebra, chiral algebra, derived
chiral centre, Kontsevich–Soibelman d-Calabi–Yau category, perfect obstruction theory,
virtual fundamental class, Mukai vector, Mukai lattice, Donaldson–Thomas / Pandhari­
pande–Thomas / Maulik–Nekrasov–Okounkov–Pandharipande, CHL point. Φ_{10} = χ_{10}.
The handle "Δ_5" works in this repo; in manuscript prose specify "Φ_{10}^{1/2}" or
"the level-five Borcherds–Kac–Moody denominator" on first occurrence per chapter.

Banned rhetorical patterns (`STANDARDS §V`): meta-narration ("we now turn to"),
bookkeeping ("Theorem A, Theorem B"), catalogue IDs ("phase j", "wave N"), branding
("matrix microscope", "magic identity", "inner music"), hedging ("we believe",
"essentially"), negative framing for identifications ("would collapse"), approximation
language for exact equalities, computer-science vocabulary ("certificate" → "identity"
or "theorem"; "pipeline" → "construction").

Honest epistemic status on every load-bearing claim: *proved / conjectured / heuristic
/ computed / expected / folklore / unverified*. Mathematical-repair doctrine
(`INVARIANTS.md §XI`): heal the proof, statement, or construction; never delete,
demote, or quietly narrow scope. Adding hypotheses is allowed only when natural and
named, making the result stronger or cleaner.

## V. Codex / GPT-5-family harness — research-grade settings

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** for any mathematical / cross-repo / formal / adversarial / proof-obligation work; never lower than `high` | Borcherds product / BKM / Igusa cusp form is frontier modular-form theory; no downgrade. |
| `model` | Deepest host-exposed: ChatGPT GPT-5.5 Pro / Heavy when available; Codex GPT-5.5 / GPT-5-Codex; API fallback latest with `xhigh` | Pro-class mathematics harness. |
| `verbosity` | As the proof requires; terse where terse is honest | Independent of `reasoning_effort` (`AGENTS-HARNESS.md §VI`). Reason deeply; answer tersely. |
| Token budget | Unbounded for research tasks | Compact side work if context fills. Never elide a Fourier coefficient, denominator-identity exponent, or lattice convention. |
| Tool use | Parallel reads (`multi_tool_use.parallel`) for TeX + bib + cited PDFs + cross-repo anchors | Batch every `read_file` before writing. Re-read only on evidence of change. |
| Persistence | Absolute (`AGENTS-HARNESS.md §V`) | Do not yield on a partial argument. Either close or name the open obligation precisely. |
| Self-reflection rubric | Required (`AGENTS-HARNESS.md §VIII`); instantiated at §VII below | Build the rubric silently before any inscription; ship only when every category is at top marks. |
| Attacker-ledger calibration | 11% error-rate floor (`INVARIANTS.md §IX`; `AGENTS-HARNESS.md §VII`) | Verify numeric / file-existence / behavioral claims via ground-truth commands before propagating to canonical docs. |

## VI. Long-form proof harness

1. **Deliberation budget.** A 30–60 minute agent run is normal for theorem repair,
   cross-volume synthesis, adversarial review, primary-source reconstruction. Do not
   stop because the first plan is plausible. Stop only when the proof closes, a
   computation decides the point, or the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for search and
   synthesis; never expose raw scratchpad as an answer. The deliverable is the checked
   proof path: definitions, reductions, cited theorems, computations, and the
   remaining obstruction if any.
3. **Context before invention.** Load `./CLAUDE.md`, this file, `main.tex`,
   `proj.bib`, the cited Borcherds 1995 / Gritsenko–Nikulin 1998 / Igusa 1964 /
   Gritsenko–Cléry sources, `compute/` fixtures, the swarm reports under
   `notes/swarm_*/reports/`, and the cross-repo anchors (Vol II Universal Holography
   master theorem; Vol III κ-ladder + 8-row Gritsenko–Cléry catalogue; topological-
   strings holomorphic de Rham obstruction class) before the first mathematical edit.
   Build an internal outline; do not write from memory.
4. **Multiple independent routes.** For any load-bearing identity, seek independent
   derivations: worked Fourier coefficient, lattice convention check, primary
   literature, local computation, cross-repo consistency. Agreement is evidence;
   disagreement is the deliverable.
5. **Adversarial loop.** After every proposed repair, attack the strongest failure
   mode: sign, character, Weyl vector, divisor normalization, multiplier system,
   exponent, false transfer into Vol III. Heal, then attack again. Convergence: no
   fatal objection survives; one mathematical improvement is inscribed.
6. **Subagents provide evidence, not authority.** The main thread integrates by deep
   semantic merge. Each subagent returns: claim attacked, failure mode or proof,
   file anchors, primary-source anchors where needed, exact formulas / constants,
   claim-status recommendation, files changed, tests or computations run, remaining
   open questions.
7. **Mathematical repair doctrine** (`INVARIANTS.md §XI`). The manuscript moves
   upward or stops. A downgraded manuscript is not a closed loop.

## VII. Self-reflection rubric

Build the rubric silently before any deliverable that lands in the manuscript, a swarm
report, a commit message, or a cross-repo synthesis. Ship only when each category is
at top marks. If one falls short: restart the category. Do not patch.

| Category | Top-marks test |
|---|---|
| Correctness | Every Fourier coefficient, exponent, sign, multiplier system verified against `main.tex`, `proj.bib`, primary source, or local computation. |
| Rigor | Every load-bearing claim carries proved / conjectured / heuristic / computed / expected / folklore / unverified. The cross-level identity ②↔③ names which of (D0), (O1), (O1⁺), (O2) it depends on. |
| Voice | Russian-school + mathematical-physics-frontier; seven combined voices; banned rhetorical patterns (`STANDARDS.md §V`) absent. |
| Standard terminology | Igusa cusp form, Siegel modular form, Borcherds product, Borcherds–Kac–Moody algebra, factorization algebra, derived chiral centre, Kontsevich–Soibelman d-Calabi–Yau category, perfect obstruction theory, virtual fundamental class. Coined terms pass `STANDARDS.md §III` or are replaced. |
| Beilinson cut | Every load-bearing claim locates itself on the §III chain. Banned identifications (§III table) absent. |
| Cross-repo consistency | Vol III κ-ladder + 8-row Gritsenko–Cléry catalogue + Vol II Hall–Borcherds residual + mixed-holomorphic-topological-strings holomorphic de Rham obstruction class consistent on every load-bearing claim. Disagreement is the deliverable. |
| Standalone | No version labels, phase labels, prior-draft references (`INVARIANTS.md §III`). |
| Attribution | Every prior result cited author + year + theorem / equation number (Borcherds 1995, Gritsenko–Nikulin 1998, Igusa 1964, Gritsenko–Cléry, Kac–Moody). |
| Concrete-before-abstract | A worked Fourier coefficient or lattice computation precedes the theorem statement (`STANDARDS.md §VII`). |

## VIII. Long-context handling

`main.tex` (~18,600 lines) + `proj.bib` + cited Borcherds 1995 / Gritsenko–Nikulin
1998 / Igusa 1964 / Gritsenko–Cléry PDFs + swarm reports (A001–A290+) + Vol II /
Vol III / mixed-holomorphic-topological-strings cross-repo anchors easily exceed 50K tokens together.

1. Outline internally before responding. Do not show the outline.
2. Parallel-`read_file` across paper, bibliography, cited PDFs, swarm reports.
3. When citing a numerical constant, lattice rank, or denominator-identity exponent,
   cite the TeX line or the computation that produced it.
4. Re-read only on evidence of change: if a file has been read this turn and not
   edited since, do not re-read.

## IX. Research constellation

| Repo | Role | Interaction |
|---|---|---|
| `~/chiral-bar-cobar` | Vol I — Modular Koszul Duality | Bar / Z^{der}_{ch} firewall; class M completion; chiral Koszulness as separate theorem. den(g_{Δ_5}) is a chiral shadow, not bulk. |
| `~/chiral-bar-cobar-vol2` | Vol II — A_∞-Chiral / Chiral Hochschild | Primitive package (X, D, τ; C^op, b, A_b, Z^{der}_{ch}(C), Θ_C, Tr_C); Universal Holography master theorem; modular functor as trace + clutching; Hall–Borcherds residual; KZ analytic SDR for finite-jet PVA. |
| `~/calabi-yau-quantum-groups` | Vol III — CY quantum groups / κ-stratification | κ-ladder (0, 0, 3, 5, 24); two-stage CY_d-Cat → E_d-HolFA(X) → ChirAlg(C); Drinfeld doubling; 6d hCS quartic obstruction. The κ_BKM = 5 entry is this manuscript's value; the 8-row Gritsenko–Cléry catalogue carries the row producing Δ_5. |
| `~/chiral-bar-cobar-vol4` | Vol IV — Realization | Modular functor at level 5; scalar partition function at level n. |
| `~/mixed-holomorphic-topological-strings` | BCOV / Kodaira–Spencer companion | Local model ℝ²_{top} × ℂ²_{hol} + brane completion; global obstruction = holomorphic de Rham obstruction class. |

Load-bearing claims about Δ_5, φ_{0,1}, Borcherds-product exponents, the BKM
denominator, or the κ-ladder must be consistent across these repos. Disagreement is
the deliverable; report, do not silently reconcile.

## X. Open obligations

The cross-level identity ②↔③ is conditional on four obstruction classes, named at
§5.8 of the manuscript and tracked across the swarm:

| Obstruction | Statement | Swarm probe |
|---|---|---|
| (D0) | D0-degeneration limit of the cosection-reduced d-critical orientation theory | A005, A011, A026, A037, A042 |
| (O1) | Strong reduced orientation on the K3×E-quotient self-Ext frame bundle | A074, A076, A082 |
| (O1⁺) | Weyl-equivariant transport of the orientation along W^{(2)}(Λ_{II}^{2,1}) reflections | A047, A049, A089 |
| (O2) | Local Pfaffian wall normal form on type-II walls (the 4096 = 2^{12} sign sum on the half-Hilbert orbit) | A047, A092, A100 |

Discharging any obstruction tightens the conditioning of ②↔③; verify swarm state
before asserting unconditionally.

## XI. Codex load order

1. `./CLAUDE.md` (repo identity mirror).
2. `~/ecosystem/INVARIANTS.md` (canonical rules).
3. `~/ecosystem/AGENTS-HARNESS.md` (harness calibration).
4. `~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`.
5. `main.tex` + `proj.bib`.
6. `notes/swarm_*/reports/` (latest swarm ledger).
7. Cross-repo anchors when claims cross volumes.
8. `out/main.pdf` for typeset verification at session end (ignored by Git).

## XII. Swarm protocol

When the principal explicitly authorizes a large adversarial, rescue, review, or
cross-volume swarm, treat that as authorization to use the largest useful swarm the
runtime can support. Do not downshift because of old 3-, 5-, or 30-agent cautionary
language. Request the strongest available model and the highest reasoning budget for
research agents.

Swarm design is explicit before launch: partition agents by disjoint mathematical
axes, files, or proof obligations; name the integration owner; forbid agents from
reverting work they did not make; require deep semantic merge (`INVARIANTS.md §VII`)
across `~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`, `~/calabi-yau-quantum-groups`,
`~/chiral-bar-cobar-vol4`, `~/igusa-cusp-form`,
`~/mixed-holomorphic-topological-strings` whenever claims cross those repositories.

Every adversarial agent returns a compact, checkable report: claim attacked, failure
mode or proof, local file anchors, primary-source anchors where needed, exact formulas
and constants, claim-status recommendation, files changed, tests or computations run,
remaining open questions. For theorem-level work, repeated attack-and-repair iterations
run until convergence: no new fatal attack survives, and at least one mathematical
improvement is inscribed.

The main thread integrates; agents do not vote truth into existence. Preserve all
mathematically substantive content, resolve conflicts by reading both sides in
context, verify with targeted `rg`, local computations, and session-end builds.

## XIII. Escalation

- A proof obligation cannot be discharged with honest rigor → naming the open
  obligation precisely **is** the deliverable.
- Cross-volume disagreement on a load-bearing claim → stop, report; the principal
  decides which tree is canonical.
- A numerical Fourier coefficient disagrees with a cited source → stop, report; trust
  the cited source, do not overwrite from memory.
- A destructive-git command appears necessary → STOP (`INVARIANTS.md §I`).
- An open-source whitelist violation appears imminent → STOP (`INVARIANTS.md §X`);
  this repo is closed-source.

## XIV. How to work

Read `main.tex` in context before editing. Use `rg` for symbols, theorem environments,
coefficients, bibliography keys. Preserve the elementary-derivation style: define the
lattice, state the root datum, compute the Weyl vector, write the product, identify
the modular form.

Prefer small, checkable patches. If changing a formula, record the verification path
in nearby prose or a concise comment only when it helps future checking.

Never guess a modular, Jacobi, BKM, or lattice formula. Derive it from `main.tex`,
direct computation, or primary literature.

Claim strength must match proof strength. Mark conjectural material explicitly.

No AI attribution anywhere. Commits by Raeez Lorgat only (`INVARIANTS.md §VI`).

## XV. Source layout and build

See `./CLAUDE.md §VIII`. `make` runs the four-pass `pdflatex → bibtex → pdflatex →
pdflatex` pipeline at session end. The repo is closed-source per
`~/ecosystem/INVARIANTS.md §X`.

## XVI. Code-writing discipline — repo application

Per `~/ecosystem/INVARIANTS.md §XIII`. Twelve rules instantiated for igusa-cusp-form (Igusa cusp-form, Borcherds products, denominator identities, modular-form companion; closed-source):

1. **Think Before Coding.** Every modular-form-edit names the cusp / denominator-identity / Borcherds-product touched, the lattice / Weyl-vector data, and the claim-status macro.
2. **Simplicity First.** Modular-form companion is the scope; no speculative weight extensions, no new product identities ahead of need. Five-fold thesis (① ↔ ② ↔ ③ ↔ ⑤ chain) is the canonical landmark.
3. **Surgical Changes.** A denominator-identity edit does not opportunistically refactor the Borcherds-product chapter. The four-obstruction-plus-residual discharge (Appendix G, K3×E) is its own surface — do not touch beyond Appendix G when working there.
4. **Goal-Driven Execution.** Success = `make` (four-pass `pdflatex → bibtex → pdflatex → pdflatex`) clean at session end, theorem ledger consistent, voice-scan + term-coining test pass, modular-form checks (denominator identities, Borcherds expansions) verified.
5. **Use the model only for judgment calls.** Cross-references and bibliography deterministic. Modular-form arithmetic computations are deterministic — verify, do not LLM-approximate.
6. **Token budgets are not advisory.** Monograph; checkpoint between Borcherds-product / cusp-form sections and between the five-fold thesis vertices.
7. **Surface conflicts, don't average them.** Cross-volume statements with chiral-bar-cobar / Vol II / Vol III canonical at the chiral side where they share an artifact; flag drift here. A numerical Fourier coefficient disagreement with a cited source halts and reports — trust the source, do not overwrite from memory.
8. **Read before you write.** Read the affected Borcherds expansion or denominator identity before editing. Cross-reference primary literature for any modular / Jacobi / BKM / lattice formula. Use `rg` for symbols, theorem environments, coefficients, bibliography keys.
9. **Tests verify intent.** Claim-status macros honest; modular-form check passes verify computed identities, not just compilation. The five-fold thesis status (proved / conjectural / chained-through) is the load-bearing claim ledger.
10. **Checkpoint after every significant step.** Between sections, summarize modular-form-check delta and five-fold thesis status.
11. **Match the codebase's conventions, even if you disagree.** raeez-math-template per `INVARIANTS.md §XII`. Theorem environments per template. memoir / EB Garamond / newtx typography. Elementary-derivation style: lattice → root datum → Weyl vector → product → modular form.
12. **Fail loud.** Surface every failed denominator identity; never silently substitute heuristic for checked. Never derive a Fourier coefficient from memory. Cross-volume / source-vs-prose disagreements halt and report. Repo is closed-source — never write a public path or proprietary-tree reference.
