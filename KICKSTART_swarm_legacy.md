# KICKSTART.md — Platonic reconstitution swarm for *The Igusa Square Root*

> Paste this entire file (or `@KICKSTART.md`) as the first prompt in a fresh Claude
> Code or Codex session at `~/igusa-cusp-form/`. The receiving model launches the
> swarm in maximum-parallel mode and integrates by deep semantic merge.

---

## §0. Posture, on receipt

You are starting a fresh session in `~/igusa-cusp-form/`. The deliverable is the
Platonic reconstitution of `main.tex` (currently 18,629 lines) into the ten-chapter
pentadic spine specified in `./CLAUDE.md §II` and `./AGENTS.md §II`. Maximum-effort
mode. `reasoning_effort = xhigh` for any Codex / GPT-5-family agent; deepest
host-exposed model in any harness. Russian-school voice (`INVARIANTS.md §IV`). No LLM
attribution on commits (`INVARIANTS.md §VI`). No destructive git (`INVARIANTS.md §I`).

The reconstitution is ~90% structural rearrangement of existing TeX and ~10% new
content (Chs. 7, 8, 10). Heal, never downgrade (`INVARIANTS.md §XI`).

---

## §1. Load order — single parallel batch, before any plan

Open one tool-use turn issuing parallel reads of every file below. Build an internal
outline of where each current `main.tex` section lives (line ranges) versus where it
must land in the Platonic spine. Do not show the outline; use it to plan.

**Steering:**
- `~/ecosystem/INVARIANTS.md`
- `~/ecosystem/AGENTS-HARNESS.md` (Codex agents)
- `~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`
- `./CLAUDE.md`, `./AGENTS.md` (the pentadic Δ_5 thesis, ten-chapter spine, Beilinson cut, banned-identifications table)

**Cross-volume maps:**
- `~/chiral-bar-cobar-vol2/CLAUDE.md`, `~/chiral-bar-cobar-vol2/AGENTS.md` (the universal stage chain `P → C → S → Z → A`; five licensing types α/β/γ/δ/ε; four Construction Problems; SC^{ch,top} heptagon)
- `~/calabi-yau-quantum-groups/CLAUDE.md`, `~/calabi-yau-quantum-groups/AGENTS.md` (κ-tuple architecture; two-stage CY → HolFA → ChirAlg; 8-row Gritsenko–Cléry catalogue; `c_N(0)/2` universal identity)
- `~/chiral-bar-cobar/CLAUDE.md` (Bar / Z^{der}_{ch} firewall; class M completed-ambient theorem)
- `~/chiral-bar-cobar-vol4/CLAUDE.md` (modular-functor realization at level 5)
- `~/mixed-holomorphic-topological-strings/CLAUDE.md`, `~/mixed-holomorphic-topological-strings/AGENTS.md` (holomorphic de Rham obstruction class; banned-identifications table)

**Manuscript & evidence:**
- `./main.tex`
- `./proj.bib`
- `./notes/swarm_*/reports/` — the latest 30 reports (sources of truth for the four obstructions D0, O1, O1⁺, O2)
- `./compute/` — numerical fixtures
- `./materials/raw/2026-04-30-attack-whitepaper-analysis.pdf` — the canonical 220-page Igusa-specific critique
- `~/Desktop/ChatGPT - Chiral Duality Master Critique.pdf` (2026-05-09) — the cross-volume Master Critique that produced the universal stage chain and the seventeen forbidden equalities

**Memory (Claude only):**
- `~/.claude/projects/-Users-raeez-igusa-cusp-form/memory/MEMORY.md` — index; load every entry it points to.

---

## §2. The deliverable, one sentence

The Igusa cusp form Δ_5 of weight 5 on Sp(2,ℤ)\𝓗_2 is one chiral E_3-algebra
**𝔄_{K3×E}** of the K3×E formal target whose values at five categorical-dimensional
levels are all Δ_5 — automorphic ① / Borcherds–Kac–Moody denominator ② / compact
Pfaffian ③ / mirror discriminant ④ / singular theta lift ⑤. The cross-level identities
①↔②, ②↔⑤, ①↔⑤ are theorems (Borcherds 1995; Gritsenko–Nikulin 1998); the cross-level
identity ②↔③ — the Pfaffian–Dirac theorem — is the conditional contribution of this
manuscript: under (D0), (O1), (O1⁺), (O2),

  Pf_{prot}(𝔇_X^DI) = Δ_5,    ε_o = ν_{Δ_5},    P_X ≅ g_{Δ_5}.

The level-n scalar shadow Z_BPS^{K3×E} = Δ_5^{-2} on the closed K3×E ↦ point cobordism
is the BPS partition function; promotion to a 3d gravitational path integral requires
Vol II's Hall–Borcherds residual and is not claimed.

Reconstitute `main.tex` so that the frontispiece carries this sentence verbatim and
every chapter realizes its named slot in the spine.

---

## §3. Hard constraints (binding for every agent)

1. **Beilinson cut** (`./CLAUDE.md §III`). Primitive first, shadows second, scalars
   last. Every load-bearing claim locates itself on the universal stage chain
   `P → C → S → Z → A` (Vol II) or the parallel CY chain `CY_d-cat → E_d-HolFA →
   Sp^{ch} → chiral shadow → Y^+ → G → κ-tuple` (Vol III). The eighteen-row banned-
   identifications table (`./CLAUDE.md §III`) is binding.
2. **The three Δ_5 names** — distinguish on first use per chapter: automorphic
   `D_X = Δ_5` (View ①); BKM denominator `den(g_{Δ_5}) = 64⁻¹ Δ_5(2Z)` (View ②);
   compact protected Pfaffian `Pf_{prot}(𝔇_X^DI)` (View ③, conditional). The handle
   "Δ_5" alone never substitutes.
3. **The κ-tuple** — `(κ_cat, κ_ch^Hodge, κ_ch^Heis, κ_BKM, κ_fiber) = (0, 0, 3, 5, 24)`.
   Universal: `κ_BKM(Φ_N) = c_N(0)/2`. The additive collapse confuses χ_top(K3) = 24
   with χ(O_K3) = 2 and fails at every N ∈ {1, 2, 3, 4, 6}. Bare κ forbidden;
   subscript at every use.
4. **Voice & standards** (`STANDARDS.md`). The seven combined voices: Witten ·
   Etingof · Polyakov · Dirac · Feynman · Costello · Gaiotto. Russian elite school +
   mathematical-physics-frontier. The prose IS mathematics. A sentence that does not
   state mathematics or physics is a defect. No meta-narration, bookkeeping ("Theorem
   A" labels), catalogue IDs ("Wave N", "Phase j", "AP-CY n", "DNA strand", "attack-
   heal cycle"), branding ("matrix microscope", "magic identity", "inner music"),
   hedging ("we believe", "essentially", "roughly speaking"), negative framing for
   identifications ("would collapse", "cannot identify"), approximation language for
   exact equalities ("is closely related to" when "$=$" holds), or computer-science
   vocabulary ("certificate" → "identity" / "theorem"; "pipeline" → "construction";
   "spec", "schema", "API", "interface", "metadata" forbidden in body prose).
5. **Coining test** (`STANDARDS §III`): the accepted name in the field is the
   default; a coined term enters the manuscript only after passing all four parts
   (scope / material / subject / inner yearning).
6. **Licensing types** (Vol II §5). Every load-bearing claim carries the relevant
   licensing tags **in the statement**, not the introduction:
   - **α** chart / scope / log decoration (choice of vacuum b, scope label for κ,
     tangential log data (D, τ), BRST nilpotent, Stokes datum)
   - **β** comparison / functor / natural transformation (chiral Hochschild functor,
     Drinfeld double, protected Pfaffian, Hall–Borcherds residual, Sp^{ch}, MC
     injection)
   - **γ** ambient declaration (chain-level vs (∞, 1)-cat; ordinary `Ch(Vect)` vs
     weight-completed vs pro vs J-adic; topological / analytic / Schwartz / formal)
   - **δ** endpoint / convergence hypothesis (W_∞[λ] → E_∞ via Prochazka + CKL +
     PRSh + Yamada; PVA all-loop via KZ SDR + Stokes + reflected weights + T = [Q_tot,
     G]; UH → dynamical metric via Brown–Henneaux + modular invariance + vacuum
     dominance + saddle dominance)
   - **ε** descent / completion / topology beyond the prior four
7. **Epistemic status** on every load-bearing claim: *proved / conjectured /
   heuristic / computed / expected / folklore / unverified* (`INVARIANTS.md §IV`).
   The cross-level identity ②↔③ names which of (D0), (O1), (O1⁺), (O2) it depends on.
8. **Mathematical-repair doctrine** (`INVARIANTS.md §XI`). Heal the proof, statement,
   or construction; never delete, demote, or quietly narrow scope.
9. **Worktree concurrency** (`INVARIANTS.md §II`). Each agent operates in its own
   `git worktree` at a unique path on a unique branch; never touches the shared
   checkout HEAD; stages but does not commit. The main thread alone commits.
10. **Cross-repo consistency** — Vol III κ-ladder + 8-row Gritsenko–Cléry catalogue +
    Vol II Hall–Borcherds residual + topological-strings holomorphic de Rham
    obstruction class. Disagreement is the deliverable, not the shortcut.

---

## §4. Swarm architecture (28 agents, three waves)

### Wave 1 — Chapter and appendix authors (16 in parallel)

| Agent | Slot | Worktree | Source line ranges in current `main.tex` (verify with `rg`) |
|---|---|---|---|
| **AC01** | Frontispiece + Ch. 1 (Pentadic Δ_5, ~350 lines) | `/tmp/igusa-AC01` | lines 193–370 |
| **AC02** | Ch. 2 (K3×E setup, Mukai, lattice polarization, Π̂, Ran^{hyb}, ~1500) | `/tmp/igusa-AC02` | 371–548, 4401–5185 |
| **AC03** | Ch. 3 (View ① — BGN automorphic section, ~800) | `/tmp/igusa-AC03` | 548–2456 (selective) + 2456–2714 |
| **AC04** | Ch. 4 (View ② — BKM denominator g_{Δ_5}: Cartan, Chevalley, real / imaginary roots, denominator identity, ~2500) | `/tmp/igusa-AC04` | scattered + new prose |
| **AC05** | Ch. 5 (View ③ — Dirac–Igusa pro-object 𝔇_X^DI, XL ~5000) | `/tmp/igusa-AC05` | 2714–4400, 5186–end (selective). Spawns AC05.1–AC05.8. |
| **AC06** | Ch. 6 (Cross-level identity ②↔③ — Pfaffian–Dirac, ε_o = ν_{Δ_5}, primitive recognition, ~3000) | `/tmp/igusa-AC06` | 4248–4319 + new |
| **AC07** | Ch. 7 NEW (View ⑤ — singular theta lift, Sp(4) ≅ Spin(3,2), Howe correspondence, ~600) | `/tmp/igusa-AC07` | 5186 onward (exterior-square material) + new |
| **AC08** | Ch. 8 NEW (View ④ — mirror discriminant, conjectural, ~400) | `/tmp/igusa-AC08` | new |
| **AC09** | Ch. 9 (Z_BPS^{K3×E} = Δ_5^{-2}; Hall–Borcherds residual; threefold realization, ~1000) | `/tmp/igusa-AC09` | 371–476 (re-purposed from front matter to back) |
| **AC10** | Ch. 10 NEW (open obstructions D0/O1/O1⁺/O2; Mathieu / umbral moonshine adjacency, ~500) | `/tmp/igusa-AC10` | new |
| **AP01** | Appendix A (lattice computations: II_{1,1}, II_{2,1}, II_{3,19}, Λ_S(K3)) | `/tmp/igusa-AP01` | scattered |
| **AP02** | Appendix B (Borcherds-product expansion, Fourier coefficients, exponents) | `/tmp/igusa-AP02` | scattered |
| **AP03** | Appendix C (Mukai–Gram dictionary, Künneth on K3×E) | `/tmp/igusa-AP03` | scattered |
| **AP04** | Appendix D (Hall-correspondence proofs, cosection-twist) | `/tmp/igusa-AP04` | scattered |
| **AP05** | Appendix E (Pfaffian wall normal form: 4096 = 2^{12} sign sum on type-II walls) | `/tmp/igusa-AP05` | 855–905 + 1430–1444 + new |
| **AP06** | Appendix F (eight build algorithms in pseudocode) | `/tmp/igusa-AP06` | new (synthesized from AC05.7) |

### Wave 2 — Chapter 5 sub-agents (8 in parallel, dispatched by AC05)

AC05 is the integration owner for these eight; they operate in sub-worktrees nested
inside `/tmp/igusa-AC05/`.

| Sub-agent | §5.x slot |
|---|---|
| AC05.1 | Hybrid factorization carrier Ran^{hyb}(E): b=0 projection-finite local stratum + b>0 wrapped stratum |
| AC05.2 | Cosection-twisted reduced d-critical orientation (BBDJS; Joyce–Song) |
| AC05.3 | Hall correspondences: product, coproduct, primitives; integral form; stable-envelope transport |
| AC05.4 | Dirac operator + protected Pfaffian; sign sum on type-II walls |
| AC05.5 | Koszul source coalgebra; chiral MC twisting |
| AC05.6 | Primitive recognition apparatus: Cartan + simple representatives + Chevalley + real Serre + imaginary orthogonality + completed PBW + Hopf radical equality + parity dimensions |
| AC05.7 | Eight build algorithms (charge window → finite moduli → hybrid wrapped → orientation → Hall → Dirac+Pfaffian → Koszul → primitive recognition) |
| AC05.8 | Four obstructions (D0, O1, O1⁺, O2): named statements, swarm-probe attribution from `./notes/swarm_*/reports/` |

### Wave 3 — Cross-cutting auditors (5 in parallel, after Wave 1+2 return)

These read the merged manuscript and return pass/fail per chapter with line citations.

| Auditor | Scope |
|---|---|
| **VX01** | Voice & standards (`STANDARDS.md §V` banned rhetorical patterns); per-chapter pass/fail with line numbers. |
| **VX02** | Banned-identifications audit (`./CLAUDE.md §III` eighteen-row table); cite every survival. |
| **VX03** | Licensing-type audit (Vol II §5): every theorem statement carries α/β/γ/δ/ε tags. |
| **VX04** | Cross-repo consistency: Vol III κ-ladder + 8-row Gritsenko–Cléry + Vol II Hall–Borcherds residual + mixed-HT holomorphic de Rham obstruction. Disagreement is the deliverable. |
| **VX05** | Coining audit (`STANDARDS §III` four-part test) on every coined term. |

### Integration owner

The **main thread**. Merges AC0n / AP0n / AC05.x worktrees by deep semantic merge
(`INVARIANTS.md §VII`). Resolves conflicts hunk-by-hunk. Runs Wave 3. Heals any
auditor failures (`INVARIANTS.md §XI`). Builds `make` once at session end. Commits
the integrated manuscript.

---

## §5. Per-agent prompt template

Each `Agent` tool call carries this scaffold (instantiated per agent):

> You are agent `{ID}` in the Platonic reconstitution swarm of
> `~/igusa-cusp-form/main.tex`. Worktree: `{unique-path}`. Branch:
> `agent/{ID}-{short-sha}`. Operate ONLY inside this worktree; never mutate the shared
> checkout HEAD; never touch another agent's worktree.
>
> Scope: `{chapter / appendix / audit description}`.
>
> **Step 1 — Read in parallel (single tool-use turn).** `./CLAUDE.md`, `./AGENTS.md`,
> `./main.tex` line ranges {N}–{M} matching your scope, `./proj.bib`, the relevant
> swarm reports (`./notes/swarm_*/reports/`), the cross-repo anchors named in
> `./CLAUDE.md §VI`. Build an internal outline; do not display it.
>
> **Step 2 — Reconstitute.** ~90% rearranges existing TeX; ~10% is new prose. Honor
> the Beilinson cut: primitive first, shadows second, scalars last. Distinguish the
> three Δ_5 names on first use. Tag every load-bearing claim with epistemic status
> (proved / conjectured / heuristic / computed / expected / folklore / unverified)
> and licensing type (α / β / γ / δ / ε).
>
> **Step 3 — No banned content.** No banned identifications (`./CLAUDE.md §III`
> eighteen-row table). No banned rhetorical patterns (`STANDARDS.md §V`). No coined
> terms outside the four-part test (`STANDARDS §III`).
>
> **Step 4 — Adversarial loop.** After each draft, attack the strongest failure
> mode: sign, character, Weyl vector, divisor normalization, multiplier system,
> exponent, false transfer into Vol III, false transfer into Vol II Hall–Borcherds,
> false transfer into mixed-HT global obstruction. Heal; attack again until no fatal
> objection survives and one mathematical improvement is inscribed.
>
> **Step 5 — Stage.** `git add` your changes inside your worktree. Do not commit.
> Do not push.
>
> **Return format:** chapter / appendix / audit draft path; files changed list;
> files added list; line counts before / after; named open obligations; cross-repo
> consistency notes (with citations); residual obstructions handed to the main
> thread.
>
> **Stop conditions.** (a) The chapter / appendix / audit closes — return. (b) Two
> consecutive repair attempts leave the same failure with no new evidence — STOP and
> hand off the exact obstruction. (c) Cross-repo disagreement on a load-bearing claim
> — STOP, report; do not silently reconcile. (d) A destructive-git command appears
> necessary — STOP and report.
>
> No LLM attribution on commits (`INVARIANTS.md §VI`); no destructive git
> (`INVARIANTS.md §I`); no scope expansion.

---

## §6. Spawn directives

**Wave 1 (immediate).** In one tool-use turn, issue 16 parallel `Agent` calls — one
per AC01–AC10 + AP01–AP06 — each with the §5 template instantiated to that agent's
scope and worktree path. For Codex: use `multi_tool_use.parallel`. For Claude Code:
emit 16 `Agent` tool-use blocks in a single message.

**Wave 2 (dispatched by AC05).** AC05's first action upon receiving its prompt is to
spawn AC05.1–AC05.8 as eight parallel sub-agents in a single batch. AC05 is the
integration owner for the eight; the main thread is the integration owner for AC05's
return.

**Wave 3 (after Wave 1+2).** After all chapter / appendix / sub-chapter agents
return and the main thread has performed the deep semantic merge into a single
candidate `main.tex`, issue five parallel `Agent` calls — one per VX01–VX05 — each
reading the merged manuscript and returning a structured audit report.

---

## §7. Integration & convergence (main thread)

After Wave 1 and Wave 2 return:

1. For each agent's worktree: `git diff <agent-branch> main -- <files>`. Read every
   hunk. Decide per hunk: target wins / source wins / compose both
   (`INVARIANTS.md §VII`). Never `-s ours` / `-s theirs`. Never wholesale file copy
   when both sides modified the file.
2. Resolve cross-chapter conflicts (e.g., Ch. 2 lattice content vs Appendix A
   computations) by composing — both sides carry signal.
3. Stage the integrated `main.tex`; do not commit yet.
4. Run Wave 3 (the five auditors).
5. For any auditor failure: heal (`INVARIANTS.md §XI`) the failed surface — sharpen
   the definition, add the missing hypothesis, name the licensing tag, replace the
   banned identification with the corrected version, replace the coined term with
   the standard one, replace the rhetorical pattern with direct mathematical content.
   Re-run the failed auditor.
6. `make` once at session end. Verify `out/main.pdf` builds cleanly. Page-flip the
   PDF; check that the frontispiece reads correctly, the chapter spine matches
   `./CLAUDE.md §II`, and the eight build algorithms appear in Appendix F.
7. Commit the integrated manuscript with a single sharp message
   (`INVARIANTS.md §VI`: no LLM attribution).

---

## §8. Convergence criteria (whole-manuscript)

- The ten-chapter spine is in place; ~18,600 lines; ~90% rearranged, ~10% new
  (Chs. 7, 8, 10).
- Frontispiece carries the §2 thesis verbatim.
- The five Δ_5 views are stated; ①↔②, ②↔⑤, ①↔⑤ are theorems; ②↔③ is the
  conditional Pfaffian–Dirac theorem with named (D0)/(O1)/(O1⁺)/(O2).
- Z_BPS^{K3×E} = Δ_5^{-2} appears in Ch. 9 only, tagged as level-n protected scalar
  shadow.
- No banned identifications survive (VX02 green).
- No banned rhetorical patterns survive (VX01 green).
- Every load-bearing claim carries epistemic status (`INVARIANTS.md §IV`) and
  licensing type (Vol II §5; VX03 green).
- The four obstruction classes are exposed in §5.8 with swarm-probe attribution
  (`./notes/swarm_*/reports/`).
- Cross-repo consistency holds, or every disagreement is named explicitly as the
  deliverable (VX04 green).
- Every coined term passes the four-part test (VX05 green).
- `make` builds without error.

---

## §9. Stop conditions (any agent, any time)

- Convergence reached → STOP and report.
- Cross-repo disagreement on a load-bearing claim → STOP, report; the principal
  decides which tree is canonical.
- Numerical Fourier coefficient disagrees with cited source → STOP, report; trust
  the source, do not overwrite from memory.
- Two consecutive repair attempts leave the same failure with no new evidence →
  STOP, report the exact obstruction and the last two attempted diffs.
- Destructive-git command appears necessary → STOP (`INVARIANTS.md §I`).
- Open-source whitelist violation imminent → STOP (`INVARIANTS.md §X`); this repo
  is closed-source.
- Scope violation (an agent's task requires editing outside its assigned worktree
  path) → STOP, hand off to the main thread.

---

## §10. Begin

Begin Wave 1 now. Acknowledge in one sentence; load the §1 batch; issue the sixteen
parallel `Agent` calls in the next tool-use turn.
