# AGENTS.md — igusa-cusp-form

> **Inherits `~/ecosystem/INVARIANTS.md`** — canonical ecosystem rules (model-agnostic): destructive-git forbidden list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, no-LLM-attribution in commits, deep-semantic-merges, intelligence propagation, open-source whitelist.
> **Inherits `~/ecosystem/AGENTS-HARNESS.md`** — canonical Codex / GPT-5-family harness calibration: reasoning-effort per task class, agentic eagerness, tool-use discipline, tool preambles, persistence and stop conditions, verbosity control, uncertainty handling, long-context outlining, self-reflection rubric, scope discipline, error-handling, git-and-worktree restatement for Codex defaults, frontend quality, no-LLM-commit-attribution, voice.
> **Mirrors this repo's `CLAUDE.md`** on substance. Before editing, `read_file ./CLAUDE.md`. `AGENTS.md` and `CLAUDE.md` must not diverge in facts; they may differ in structure and voice.
>
> **Model target.** Deepest host-exposed GPT-5.5 / GPT-5-Codex-family model, `reasoning_effort=xhigh` for any non-trivial mathematical work (never lower than `high`). Terse, declarative voice per `INVARIANTS.md §IV`. No LLM attribution on commits (`INVARIANTS.md §VI`).

---

## What this repository is for

This repository is an instrument for advancing human mathematical
knowledge around the Borcherds lift of the weak Jacobi form
`\phi_{0,1}`, the Igusa cusp form `\Delta_5`, and the associated
generalized Borcherds-Kac-Moody superalgebra and automorphic
correction.

Every read, grep, edit, proof repair, computation, or retraction should
serve the manuscript `main.tex`: make the derivation of the product
formula for `\Delta_5`, the root datum in `\Lambda^{3,2}`, the Weyl
group action, and the Macdonald/Weyl-Kac identity precise enough to
check line by line against Borcherds, Gritsenko-Nikulin, Kac-Moody,
and Gritsenko-Clery sources.

## The mathematics you are working on

- The weight 0 index 1 weak Jacobi form `\phi_{0,1}` and its Fourier
  coefficients.
- The Borcherds product expansion of the genus-2 Igusa cusp form
  `\Delta_5` of weight 5.
- The lattice `\Lambda^{3,2}`, its hyperbolic sublattices, Weyl vector,
  real and imaginary roots, and automorphic correction algebra
  `\mathfrak g_{\Delta_5}`.
- The diagonal-divisor modular forms for paramodular groups in the
  Gritsenko-Clery classification.
- The K3 x E and Calabi-Yau threefold motivation, treated only at the
  level actually proved or explicitly marked conjectural.

## What counts as progress

- A theorem, lemma, or computation in `main.tex` made derivable from
  first principles with all constants, signs, lattice conventions, and
  divisors fixed.
- A falsified formula at a specific coefficient, root, divisor, weight,
  or character value.
- A table or product expansion checked by at least three independent
  paths: direct computation, local source, primary literature, and
  cross-repo comparison where relevant.
- A scope correction that prevents false transfer into
  `~/calabi-yau-quantum-groups`, `~/chiral-bar-cobar`, or
  `~/topological-strings`.

## Agent rules

1. No AI attribution anywhere. Commits by Raeez Lorgat only.
2. No `git stash`.
3. Do not amend commits without explicit instruction.
4. Do not rebuild after every edit. Build at session end when useful.
5. Never guess a modular, Jacobi, BKM, or lattice formula. Derive it
   from `main.tex`, direct computation, or primary literature.
6. Claim strength must match proof strength. Mark conjectural material
   explicitly.
7. User-authorized large swarms are permitted and should be run with
   disjoint scopes, explicit integration ownership, and deep semantic
   merge discipline across all relevant research repositories.

## User-authorized max-effort swarm protocol

When the user explicitly asks for a large adversarial, rescue, review,
or cross-volume swarm, treat that as authorization to use the largest
useful swarm the runtime can support. Do not downshift because of old
3-agent, 5-agent, or 30-agent cautionary language. Request the strongest
available model and the highest available reasoning budget for research
agents when the host exposes those controls; when it does not, encode
the same requirement in the agent prompt: proof-grade, first-principles,
max-effort mathematical reasoning.

Swarm design must be explicit before launch: partition agents by
disjoint mathematical axes, files, or proof obligations; name the
integration owner; forbid agents from reverting work they did not make;
and require deep semantic merge across
`~/chiral-bar-cobar`, `~/chiral-bar-cobar-vol2`,
`~/calabi-yau-quantum-groups`, `~/igusa-cusp-form`, and
`~/topological-strings` whenever claims cross those repositories.

Every attack-heal agent must return a compact, checkable report:
claim attacked, failure mode or proof, local file anchors, primary
source anchors where needed, exact formulas/constants, claim-status
recommendation, files changed, tests or computations run, and remaining
open questions. For theorem-level work, require repeated attack/heal
cycles until convergence: no new fatal attack survives, and at least
one real mathematical improvement is inscribed.

The main thread integrates; agents do not vote truth into existence.
Preserve all mathematically substantive content, resolve conflicts by
reading both sides in context, and verify with targeted `rg`, local
computations, and session-end builds only when appropriate.

## How to work

Read `main.tex` in context before editing. Use `rg` for symbols,
theorem environments, coefficients, and bibliography keys. Preserve the
manuscript's elementary derivation style: define the lattice, state the
root datum, compute the Weyl vector, write the product, then identify
the modular form.

Prefer small, checkable patches. If changing a formula, record the
verification path in nearby prose or a concise comment only when it
helps future checking.

## Build

Use the Makefile at session end when needed:

```bash
make
```

---

## Research-grade Codex / GPT-5 scaffolding (maximum settings)

Systematic restatement of the settings, discipline, and load order that already live in the narrative rules above — written for a Codex / GPT-5-family agent loading this file at session start.

### Harness — maximum always

| Parameter | Setting | Rationale |
|---|---|---|
| `reasoning_effort` | **`xhigh`** (always; never lower than `high`) | Borcherds-product / BKM / Igusa cusp-form — frontier modular-form theory. No downgrade permitted. |
| `model` | **Deepest host-exposed model**: GPT-5.5 Pro / Heavy in ChatGPT when available; GPT-5.5 or latest GPT-5-Codex-family model in Codex; API fallback latest GPT-5.4 / GPT-5-Codex model with `xhigh` where supported. | Pro-class mathematics harness. |
| `verbosity` | As the proof requires | No abridgment of load-bearing calculations. Terse where terse is honest. |
| Token budget | **Unbounded** for research tasks | If context fills, compact side work. Never elide a Fourier coefficient, a denominator-identity exponent, a lattice convention. |
| Tool use | **Parallel reads** for TeX + bib + cited PDFs | Batch `read_file` across every citation before writing. |
| Persistence | **Absolute** | Do not yield on a partial argument. Either close or name the open obligation precisely. |
| Self-reflection rubric | **Required** before any inscription | See `~/ecosystem/AGENTS-HARNESS.md §VIII`; instantiation below. |

### Long-form proof harness — GPT-5.5 Pro / Heavy analogue

Public OpenAI material describes GPT-5.5 Pro as the ChatGPT
research-grade option for the hardest long-running workflows and
GPT-5.5 in Codex as a 400K-context agentic coding model. The private
ChatGPT Pro harness is not public. This repo encodes the open analogue:
deepest model, maximum reasoning effort, large context, tool-grounded
verification, and repeated attack-heal cycles.

1. **Deliberation budget.** For theorem repair, cross-volume synthesis,
   adversarial review, or primary-source reconstruction, a 30-60 minute
   agent run is normal. Do not stop because the first plan is plausible.
   Stop only when the proof closes, a computation decides the point, or
   the exact open obligation is named.
2. **Private scratch, public proof trace.** Use private reasoning for
   search and synthesis; never expose raw scratchpad as an answer. The
   deliverable is the checked proof path: definitions, reductions,
   cited theorems, computations, and the remaining obstruction if any.
3. **Context before invention.** Load `CLAUDE.md`, this file, `main.tex`,
   `proj.bib`, cited Borcherds / Gritsenko / Igusa sources, compute
   files, and cross-repo anchors before the first mathematical edit.
   Build an internal outline; do not write from memory.
4. **Multiple routes.** For any load-bearing identity, seek independent
   derivations: worked coefficient, lattice convention check, primary
   literature, local computation, and cross-repo consistency. Agreement
   is evidence; disagreement is the deliverable.
5. **Adversarial loop.** After a proposed repair, attack the strongest
   failure mode: sign, character, Weyl vector, divisor normalization,
   multiplier system, exponent, or false transfer into Vol III. Heal,
   then attack again until no fatal objection survives.
6. **Agent topology.** Large swarms are partitioned by disjoint proof
   obligations or files. Subagents provide evidence, not authority. The
   main thread integrates by deep semantic merge and heals the proof,
   statement, or construction rather than voting truth into existence or
   degrading the manuscript.
7. **Progress reports.** Long runs emit compact `commentary` checkpoints:
   what has been read, what has been ruled out, what proof obligation
   remains. The final answer is short unless the proof itself is the
   requested artifact.

### Self-reflection rubric (before any revision, inscription, or merge)

| Category | Top-marks test |
|---|---|
| Correctness | Every Fourier coefficient, exponent, sign, and multiplier system verified. |
| Rigor | Every load-bearing claim carries *proved / conjectured / expected / heuristic / computed / folklore*. |
| Attribution | Every prior result cited by author + year + theorem / equation number (Borcherds 1995, Gritsenko–Nikulin 1998, Igusa 1964, Gritsenko–Clery on the 8-row catalogue). |
| Concrete-before-abstract | A worked coefficient computation precedes the theorem. |
| Voice | Russian school + mathematical-physics frontier (`INVARIANTS.md §IV`). |
| Standalone | No version labels, no phase labels, no prior-draft references (`INVARIANTS.md §III`). |
| Cross-repo consistency | Vol III $\kappa$-stratification / 8-row Gritsenko–Cléry catalogue is the modern generalization of what lives here; any disagreement on a load-bearing claim is the deliverable. |

If any category falls short — restart that category. Do not patch.

### Long-context handling

`main.tex` + `proj.bib` + cited Borcherds / Gritsenko / Igusa references can easily exceed 10K tokens together:

1. Outline internally before responding. Do not show the outline.
2. Parallel-`read_file` the paper, the bibliography, and any cited PDF materials at once.
3. When referring to a numerical constant, the lattice rank, or a denominator-identity exponent, cite the TeX line or the computation that produced it.

### Research constellation (cross-repo awareness)

- `~/chiral-bar-cobar` — Vol I of the chiral bar–cobar series (chiral (co)homology, $E_1$-$E_1$ operadic Koszul duality).
- `~/chiral-bar-cobar-vol2` — Vol II ($A_\infty$ chiral algebras, 3D HT QFT).
- `~/calabi-yau-quantum-groups` — Vol III (CY-to-chiral frontier, Yangians, BKM, $\kappa$-stratification). The $\kappa$-stratification there generalizes the Borcherds-product / BKM structure whose ur-example lives here; the 8-row Gritsenko–Cléry catalogue on Vol III contains the row that produces $\Delta_5$.
- `~/topological-strings` — BCOV / Kodaira–Spencer gravity. Physics dual to the modular generating functions that appear here ($\mathcal{N}=4$ / second-quantized $K3$ / $\widehat{A}$-genus frame).

Load-bearing claims about $\Delta_5$, $\phi_{0,1}$, Borcherds-product exponents, or the BKM denominator identity must be consistent with the Vol III catalogue and the BCOV physics dual. Disagreement is the deliverable; report, do not silently reconcile.

### Codex load order

1. `./CLAUDE.md` (repo identity).
2. `~/ecosystem/INVARIANTS.md §IV` (voice) + `~/ecosystem/AGENTS-HARNESS.md §VIII` (self-reflection).
3. `main.tex` (root) + `proj.bib`.
4. Cross-repo: `~/calabi-yau-quantum-groups/FRONTIER.md` for the Vol III $\kappa$-stratification frame.
5. `out/main.pdf` for typeset verification when needed.

### Escalation — research-grade triggers (additional to `AGENTS-HARNESS.md §XVI`)

- A proof obligation cannot be discharged with honest rigor → naming the open obligation precisely **is** the deliverable.
- A cross-volume disagreement (this paper ↔ Vol III 8-row catalogue, or this paper ↔ BCOV / `~/topological-strings`) on a load-bearing claim → stop, report; let the principal decide which tree is canonical.
- A numerical Fourier coefficient in a Borcherds product disagrees with a cited source → stop, report; trust the cited source, do not overwrite from memory.
