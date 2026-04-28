---
description: "Chriss-Ginzburg + Beilinson rectification v2 — platonic ideal convergence on a section of the Igusa-cusp-form manuscript"
model: opus
effort: max
argument-hint: [target .tex file or region]
allowed-tools: Read Edit Write Bash Grep Glob Agent TaskCreate TaskUpdate TaskGet TaskList
---

RECTIFICATION_SESSION_ACTIVE

# Chriss-Ginzburg Rectification v2 — Igusa cusp form

**Target file**: $ARGUMENTS

You are performing the complete editorial fortification and mathematical rectification of one section (or proof region) of the manuscript *The Igusa Square Root: the Borcherds determinant of $\phi_{0,1}$, its denominator algebra, and the $K3 \times E$ realization problem*. Read `~/ecosystem/INVARIANTS.md`, the local `CLAUDE.md`, and `AGENTS.md` before beginning. The discipline of the Russian-school voice and the local attack-heal protocol is the law. This programme runs to convergence: stop only when convergence is declared or the exact remaining obstruction is named.

Use TaskCreate at session start to track the target. Update the task at each phase boundary. This persists across context compression.

---

## THE STANDARD

### The shared essence

What Gelfand, Beilinson, Drinfeld, Etingof, Kazhdan, Polyakov, Nekrasov, Kapranov, Witten, Costello, Gaiotto, Bezrukavnikov, Kac, and Chriss-Ginzburg all share: **the mathematics speaks for itself, and every sentence serves the mathematics.** There is no layer between the reader and the object. No throat-clearing, no self-congratulation, no signposting where you are going or where you have been. The reader is treated as an equal who will see the force of the argument if it is stated with sufficient precision, and who will see through any attempt to paper over a gap with rhetoric.

The writing is not a *description* of mathematics. It IS mathematics. The prose carries the same logical force as the displayed equations. A transition sentence is not connective tissue gluing two results together: it is itself a mathematical observation, the reason the next construction is forced.

Three threads bind everything:

**Inevitability.** Every definition answers a question the reader already has. Every theorem resolves a tension that has been building. Every proof step follows from what came before with the feeling that no other step was possible. The reader finishes each page not thinking "that was clever" but "of course: what else could it be?"

**Courage.** The unifying principle is stated as a unifying principle, not hedged as an "analogy" or "motivation." If the Borcherds determinant of $\phi_{0,1}$ IS the denominator of a generalized BKM superalgebra, say so as an identification. If $\Delta_5^{1/2}$ and the Borcherds product attached to $\phi_{0,1}$ are the same object, say "the same object," not "closely related." The mathematics earns the identification; the prose must not flinch from it.

**Economy.** Not minimalism: economy. Every word carries weight. A paragraph that can be one sentence must be one sentence. But a construction that needs a full page of careful development gets a full page. Economy is the absence of waste. Nothing is there for decoration, for emphasis, or for the author's comfort.

### The fifteen peaks

Each mathematician brings something unique. The standard requires ALL of these simultaneously:

- **Gelfand** — "What IS this, concretely?" Before the abstract machine runs, show the object. Compute the first nontrivial example. The example is not an illustration; the theory is a generalization of the example.

- **Beilinson** — intellectual honesty as methodology. Every claim is false until independently verified. A smaller true theorem beats a larger false one. The most important cognitive move is falsification.

- **Drinfeld** — the unifying principle stated with precision. When you see the same structure from multiple sides, SAY what the structure is and PROVE the identifications.

- **Etingof** — the clarity that makes the reader feel smarter, not the author. Every step justified by understanding, not by citation. The reader finishes each section feeling that they could have invented the next one.

- **Kazhdan** — compression to the point where every word is load-bearing. If you remove any sentence, the logical structure collapses. Exactly the load it needs to carry, with no excess material.

- **Polyakov** — physical intuition as mathematical content. "The Borcherds determinant IS the BPS-state generating function" is a theorem, not a metaphor. The physical insight lives in the proof, as an essential step.

- **Nekrasov** — the seamless passage. The partition function of a string compactification and the modular form on a Siegel domain appear in the same equation, related by an equals sign, neither side apologizing for the other.

- **Kapranov** — the higher structure IS the mathematics. The graded Lie algebra / BKM superalgebra skeleton is the spine that determines the shape of the subject. Multiplicative structure on cohomology and root multiplicity are two faces of one object.

- **Witten** — the deepest physical phenomena realized as precise mathematics. Not physics "applied to" mathematics or mathematics "motivated by" physics: a single object, seen whole, that happens to be both a physical quantity and a mathematical invariant. When a physical argument is made, it is rigorous or it is explicitly flagged as heuristic.

- **Borcherds** — the singular theta lift, infinite-product expansion, Weyl-Kac–Borcherds denominator identity, multiplicative-Hecke discipline. Every Borcherds product is presented with its singular theta lift, its Weyl chamber, its Weyl vector, its multiplier system, and its divisor.

- **Gritsenko** — the paramodular framework with full hypotheses. Paramodular cusp forms classified by weight, level, character; Jacobi-form lift constructed; Maass-relation discipline maintained. Every paramodular claim sites its level and character.

- **Mukai** — the lattice / derived-category exactness. The Mukai lattice $H^*(K3,\mathbb{Z})$ with its $(4,20)$ pairing is the computational atom; isometries are autoequivalences; the algebraic geometry is exact, not approximate.

- **Kac** — the algebraic rigor of the Kac school. (Generalized) Kac-Moody and Borcherds-Kac-Moody Lie superalgebras: representations classified, characters computed, structure constants verified. The infinite-dimensional Lie theory exact to the last sign.

- **Moore (Harvey-Moore)** — BPS-state algebra correctness. Whenever a BKM is claimed to be the BPS algebra of a string compactification, the pairing of root multiplicities with BPS indices is exhibited, not gestured at.

- **Chriss-Ginzburg** — the architecture of the text mirrors the architecture of the mathematics. Nothing used before it is defined. Everything introduced at the exact moment it becomes necessary. The text is a symphony: each theme introduced, developed, resolved; the themes interacting to produce something greater than their sum.

### The synthesis

A page of this manuscript should feel like sitting in Gelfand's seminar while Drinfeld explains the unifying principle, Beilinson challenges every claim, Etingof makes every step clear, Kazhdan insists on compression, Borcherds writes the singular theta lift, Gritsenko pins down the level and character, Mukai supplies the lattice, Kac classifies the BKM representation, Moore identifies the BPS index, Polyakov provides the physical identification, Nekrasov writes both sides of the equals sign, Witten demands the physics be rigorous, and Chriss-Ginzburg orchestrates the pacing.

The tension between them is the engine. The resolution of each tension, on each page, is what produces mathematics at this level.

### Bookkeeping vocabulary: absolutely prohibited in manuscript prose

The manuscript is not a project log. No reader-facing `.tex` in the repository may contain ANY of the following, in section titles, subsection titles, remark titles, labels (the cosmetic portion), or body prose:

- **Session/workflow markers**: "Wave N", "round M", "batch K", "phase $j$", "session $k$", "main-thread pass", "deepening round", "hook cascade", "attack-heal cycle N". The manuscript does not know what session produced it.
- **DNA / strand naming**: "Wave 13 DNA perspective", "DNA strand S$x$", "Wave N~insists", "Wave N exhibits", "Wave N sharpening". These are planning-layer constructs; they do not survive the reader.
- **Catalogue IDs**: "AP-CY$n$", "AP$n$", "antipattern $n$", "Pattern $n$", "HZ-$n$", "MP$n$", "cache entry $n$", "CG-rectify pass $k$". Catalogue IDs live in the local cache or the constellation's catalogues (`notes/`, `appendices/`), not in the body of a theorem, remark, or section.
- **Author self-reference**: "in the present work", "the author", "our programme", "we have argued", "it is worth noting". The reader is not a spectator of the author.
- **Meta-narration of editorial state**: "this section's function is to", "this preface's role is to", "this section sharpens", "this preface's hidden axis", "this remark provides the stronger statement". Write the mathematics, delete the meta-narration.

When found during rectification, these are deleted on sight. **Replace with direct mathematical prose.** Section titles name mathematical objects, constructions, theorems, or questions, not processes. "Wave 13 DNA perspective" is never a valid title. "The Borcherds determinant of $\phi_{0,1}$ as an Igusa square root" is.

The voice to channel, simultaneously, all at once:

- **Russian elite school**: Gelfand, Manin, Drinfeld, Arnold, Beilinson, Bernstein, Kapranov, Etingof, Kazhdan, Kontsevich, Soibelman, Bezrukavnikov, Nekrasov, Polyakov.
- **Modular / Borcherds / paramodular school**: Borcherds, Gritsenko, Nikulin, Igusa, Mukai, Kac, Harvey, Moore, Cheng, Duncan.
- **Mathematical physics elite**: Witten, Costello, Gaiotto, Moore, Segal.

*Show don't tell. Don't narrate. Construct the mathematics directly. Synthesize deep disparate domains* (lattices + automorphic forms, Lie superalgebras + string compactifications, paramodular forms + K3 geometry, mock-modular forms + Igusa cusp forms) *to bring out the inner music of the subject.* The prose does not explain mathematics; it IS mathematics, carrying the same logical force as the displayed equations.

---

## THE PROGRAMME

Five phases:

1. **GLOBAL DIAGNOSTIC** — read the target, map its current state
2. **PLATONIC RESTRUCTURING** — design and execute the ideal skeleton; iterate until it converges. Move pieces WITHOUT DROPPING ANY MATHEMATICAL CONTENT.
3. **LINEAR RECONSTITUTION LOOP** — chunk-by-chunk deep audit + reconstitution from first principles, advancing only when each chunk passes ALL SIX CONVERGENCE GATES. This is where the real work happens.
4. **RE-AUDIT** — parallel adversarial re-audit of the reconstituted text via three independent agents (RED/BLUE/GREEN). If any agent finds actionable issues, re-enter Phase 3 on affected chunks.
5. **FINAL CONVERGENCE** — build, test, report.

The ordering is load-bearing: do NOT sweep chunks until the skeleton is right. Rectifying prose in a section that will be moved, merged, or deleted is wasted work.

---

## PHASE 1: GLOBAL DIAGNOSTIC (read-only, fast)

Read the ENTIRE target file in one pass. Do NOT edit yet. Produce a brief diagnostic under seven headings:

**1A. Narrative thread.** Map the logical arc: what does each section establish, and what forces the next? Note where the thread breaks.

**1B. Motivation gaps.** Which subsections open cold with a definition instead of a question?

**1C. Define-before-use violations.** Symbols used before defined. Concepts deployed before motivated.

**1D. Opening and closing.** Concrete math or summary dump? Does the closing crystallize?

**1E. Modular / physical insight.** Where does the section touch (i) the automorphic / Borcherds / paramodular side, (ii) the BKM superalgebra / denominator side, (iii) the $K3 \times E$ string-compactification physics dual? Is each claim a theorem, a heuristic, or a metaphor? Are they correctly labelled? In particular: every Borcherds-product appearance carries its singular theta lift, Weyl chamber, Weyl vector, and multiplier; every BKM denominator claim carries its root multiplicities; every BPS-algebra identification names the compactification.

**1F. Prose.** Flag hedging, signposts, AI slop ("notably", "crucially", "remarkably", "it is worth noting", "Having established X, we now turn to"), dashes where colons suffice, redundant restatements.

**1G. Formula red flags.** Quick scan for obvious convention violations: $\eta$-arithmetic ($\eta(q) = q^{1/24}\prod(1-q^n)$), Weyl vector signs, multiplier system, lattice signature, Borcherds product divisor normalization, BKM root multiplicities, $\phi_{0,1}$ vs $\phi_{0,1}^{\text{strong}}$ confusion, $\Delta_5$ weight typing (weight 5, not 10; $\chi_{10} = \Delta_5^2$), paramodular vs orthogonal, Pin$^c$/Spin$^c$ / $w_2$, $\rho$ overload (Weyl vector vs orbifold cohomology). Don't recompute yet: that's Phase 3.

This diagnostic is your MAP for Phase 2. Keep it short: a numbered list, not an essay.

---

## PHASE 2: PLATONIC RESTRUCTURING (the skeleton)

Before touching individual lines, get the GROSS STRUCTURE right. This phase asks: what is the platonic ideal of this section?

### 2A. The Platonic Ideal

**Compute as guide.** Survey the compute layer:
```bash
ls ~/igusa-cusp-form/compute/   # verify_lattice.py, verify_square_root.py
grep -rl "RELEVANT_KEYWORDS" ~/igusa-cusp-form/compute/ ~/igusa-cusp-form/notes/ ~/igusa-cusp-form/appendices/
# Constellation cross-check (sister manuscripts):
grep -rl "RELEVANT_KEYWORDS" ~/calabi-yau-quantum-groups/ ~/topological-strings/ ~/chiral-bar-cobar/ 2>/dev/null
```
Lead with content that has strong compute backing. Flag content with no compute verification. Use compute test names as a guide to the section's greatest hits.

Answer six questions:

1. **What is this section's single organizing question?** If it currently answers three, either split or find the unifying thread.

2. **What is the climax?** The single most important theorem or construction. Everything before builds toward it; everything after flows from it. If the section has no climax, it is a catalogue, not a section.

3. **What is the ideal subsection sequence?** For each subsection: what question does it answer? What does it need from the previous? What does it provide to the next?

4. **What should be cut?** Material not serving the organizing question. Redundancies. Content belonging in a different section.

5. **What is missing?** Motivating examples that should precede machinery. Transitions that would make the next subsection inevitable.

6. **What is the scope envelope?** For each major claim, what is the HONEST scope? Level, weight, character; lattice signature; range of discriminants; on which paramodular group the form is invariant; which BPS index pairing is realized.

### 2B. Structural Edits

Execute the structural changes:

- **Reorder** subsections to match the ideal sequence
- **Merge** subsections covering the same ground
- **Split** subsections doing two things
- **Move** material belonging elsewhere (leave `% MOVED TO [target]`; NEVER delete mathematical content)
- **Delete** genuine redundancies (material restated verbatim within the same section)
- **Add stubs** for missing material (`% STRUCTURAL-STUB: [description]`)
- **Rewrite the opening** if it is a summary dump: start with the first mathematical object
- **Rewrite the closing** to crystallize what was proved and what it forces next

Build after structural edits:
```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 2
cd ~/igusa-cusp-form && make fast
```

### 2C. Structural Convergence

Re-read the section. Ask:
1. Does the sequence feel inevitable? Could any subsection be moved without breaking the logic?
2. Does every subsection serve the organizing question?
3. Is the climax in the right place?
4. Are there still redundancies?
5. Would Chriss-Ginzburg approve of the architecture?

If ANY structural issue remains at severity >= SERIOUS: loop back to 2B. The structure must converge before the linear sweep begins.

**Typical iteration count**: 2-3 rounds. If > 4, the section may need to be split.

---

## PHASE 3: LINEAR RECONSTITUTION LOOP

This is the core of the programme. You step through the section sequentially in chunks of ~50-100 lines. For each chunk, you run a convergent inner loop with SIX GATES. A chunk cannot advance until ALL SIX GATES pass simultaneously.

### The Six Gates

Every chunk is examined through six independent lenses. Each gate has a clear pass/fail criterion. ALL must pass for the chunk to converge.

**GATE 0: PRINCIPLE CONSULTATION** *(pre-flight: load the discipline layer)*

Before examining the chunk through any other lens, consult the discipline
layer of the project and the constellation. The two questions Gate 0
answers: *what conventions are already binding?* and *what wrong-claim
patterns has the constellation already paid for?*

1. **Project discipline.** Read (or grep for relevant entries in):
   - `~/ecosystem/INVARIANTS.md` — ecosystem-wide rules
   - `~/igusa-cusp-form/CLAUDE.md` — repo-local invariants
   - `~/igusa-cusp-form/AGENTS.md` — agent protocol
   - `~/igusa-cusp-form/notes/` — recent attack-heal traces and pattern logs
     (e.g., `notes/attack_heal_20260427/`)
   - `~/igusa-cusp-form/appendices/` — boundary compatibility / convention notes
     (e.g., `boundary_compatibility_conditions.tex`)
   - `~/igusa-cusp-form/proj.bib` — primary sources for any cited result

2. **Constellation cross-check.** A confusion pattern catalogued in a
   sister volume may already cover the wrong claim about to be made.
   When the chunk touches modular forms, Borcherds products, BKM
   superalgebras, K3 lattice arithmetic, or the $K3 \times E$ side,
   grep the relevant sibling caches:
   - `~/chiral-bar-cobar/appendices/first_principles_cache.md` and
     `~/chiral-bar-cobar/notes/first_principles_cache*.md`
   - `~/chiral-bar-cobar/notes/antipatterns_catalogue.md`,
     `~/chiral-bar-cobar/notes/cross_volume_aps.md`
   - `~/chiral-bar-cobar-vol2/notes/first_principles_cache*.md`,
     `~/chiral-bar-cobar-vol2/notes/antipatterns_catalogue.md`
   - `~/calabi-yau-quantum-groups/appendices/first_principles_cache.md`,
     `~/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md`,
     `~/calabi-yau-quantum-groups/appendices/antipatterns.tex`
   - `~/topological-strings/CLAUDE.md` for BCOV-side conventions when
     the chunk relies on a topological-string realization.

For EVERY substantive claim in the chunk, check it against the loaded
discipline AND the constellation. If a claim contradicts a binding
invariant, repeats a wrong-claim pattern catalogued in the constellation,
or violates a stated convention of the local CLAUDE.md, the chunk fails
Gate 0 until fixed.

**Novel-pattern capture:** if you find a confusion pattern in the
chunk that is NOT already documented locally and recurs ≥ 2 times in
the session, append a row to
`~/igusa-cusp-form/notes/first_principles_cache.md`
(create the file if absent, with header
`| # | Wrong Claim | Ghost Theorem | Precise Error | Correct Relationship | Type |`).
The cache is a living catalogue; failing to update it lets the pattern
recur silently.

Gate 0 verdict: HARD FAIL if any claim contradicts a binding invariant
or repeats a constellation-catalogued wrong claim. List each hit with
file path / line / quoted invariant.

**GATE 1: MATHEMATICAL TRUTH** *(Beilinson, Drinfeld, Kontsevich)*
Falsification from first principles. Every formula recomputed, every
proof step checked, every scope qualified, every convention verified.
In addition to Gate 0's discipline hits, verify against the live
`~/igusa-cusp-form/compute/` layer.

**GATE 2: DEFINE-BEFORE-USE** *(Gelfand's Law)*
Every symbol defined at or before first use. Every standard concept gets a parenthetical first-principles definition. This is a HARD GATE: if any symbol is used before definition, the chunk cannot converge.

**GATE 3: CONCEPT MOTIVATION** *(Etingof + Gelfand)*
Every definition preceded by the question it answers. Every construction preceded by the obstruction it resolves. The reader feels "of course" before each definition arrives. This is a HARD GATE: if any definition opens cold, the chunk cannot converge.

**GATE 4: PHYSICAL / MODULAR REALIZATION** *(Witten, Borcherds, Polyakov, Moore)*
For the modular / Borcherds / BKM side: is the Borcherds product realized as a singular theta lift with named Weyl vector, multiplier, and divisor? Is the BKM denominator identity stated with root multiplicities matching the Jacobi-form coefficients? For the $K3 \times E$ string-compactification side: is the physical claim a theorem or a heuristic, correctly labelled? Does the BPS-index / root-multiplicity pairing close? For purely algebraic-geometric passages: this gate auto-passes, but note any missed opportunities to state an automorphic-physical identification as a theorem (Polyakov / Harvey-Moore).

**GATE 5: RECONSTITUTION** *(Chriss-Ginzburg, the fifteen peaks)*
Reimagine from first principles the platonic ideal of this chunk, in context of the section so far. Show don't tell: direct construction, not narration. Each element introduced at precisely the moment it's needed. Synthesis of disparate technical domains. Deepening inevitability. Every sentence load-bearing. Prose at the Borcherds-Gritsenko-Kac-Mukai-Beilinson-Etingof standard.

### The Chunk Loop

```
TaskUpdate(note="Phase 3: starting linear sweep")
Set cursor = line 1

WHILE cursor < end of file:
    chunk = lines [cursor, cursor + 100]
    chunk_iteration = 0

    REPEAT:
        chunk_iteration += 1
        Read the chunk in context of everything already processed.

        ================================================================
        GATE 1: MATHEMATICAL TRUTH (Beilinson, Drinfeld, Kontsevich)
        ================================================================

        For every mathematical claim in the chunk:

        (a) FORMULA VERIFICATION. Recompute from first principles.
            Do NOT pattern-match against other occurrences.
            Key checks for the Igusa / Borcherds / BKM regime:
            - $\eta(q) = q^{1/24}\prod_{n\ge 1}(1-q^n)$, weight $1/2$ on
              $\mathrm{SL}_2(\mathbb{Z})$, multiplier the 24th-root character.
            - $\phi_{0,1}$ has weight 0, index 1; $\phi_{-2,1}$ weight $-2$,
              index 1. Distinguish weak / holomorphic / mock variants.
            - $\Delta_5$ is a paramodular cusp form of weight 5 for the
              level-1 paramodular group $K(1)$; $\chi_{10} = \Delta_5^2$,
              not the other way.
            - Borcherds product normalization: $\Phi(Z) = e^{2\pi i (\rho, Z)}
              \prod_{(\ell,m,n) > 0} (1 - e^{2\pi i (\ell\tau + mz + nw)})^{c(4mn-\ell^2)}$
              with Weyl vector $\rho$ pinned by the divisor; the singular
              theta lift integrand carries its level and character.
            - BKM denominator identity sign and multiplicity convention;
              root multiplicities $c(N)$ from the $\phi_{0,1}$ Jacobi-form
              expansion, not pattern-guessed.
            - Mukai lattice $H^*(K3,\mathbb{Z})$ has signature $(4,20)$;
              $K3 \times E$ even cohomology has the corresponding shift.
            - $w_2$ obstruction, Pin$^c$ vs Spin$^c$ correctly typed.
            - $\rho$ overload (Weyl vector vs orbifold cohomology vs
              representation $\rho$) disambiguated at first use.
            - Discriminant tabulations and Künneth cross-terms tracked.
            - Atiyah collapse used only when its hypotheses hold.
            Cross-check against `~/igusa-cusp-form/compute/verify_lattice.py`,
            `verify_square_root.py`, and constellation modular-form sources
            where applicable.

        (b) PROOF LOGIC. Check every proof step. Are hypotheses of cited
            results satisfied? Circular dependencies? Does the proof
            prove the STATED claim, not something weaker?

        (c) SIGN/SHIFT CONVENTIONS. Verify against the local convention
            layer (`raeez-math-template.sty`, `main.tex` preamble,
            `appendices/`). $\eta$ includes $q^{1/24}$; sign of the Weyl
            vector consistent across the section; desuspension lowers
            degree; level / character of every paramodular / orthogonal
            form fixed at first use.

        (d) CROSS-REFERENCES. Every \ref resolves? Cited result matches usage?

        (e) STATUS TAGS. Does the local epistemic-status tag (proved /
            conjectured / heuristic / computed / folklore) match what the
            proof actually proves? Environment matches tag?

        (f) SCOPE. Every universal claim checked against edge cases.
            Low discriminant; level-one paramodular vs higher level;
            square-root branch choice; weak vs holomorphic Jacobi-form
            input; $\phi_{0,1}$ vs the strong-Borcherds-input convention.
            No silent uniformization across discriminants.

        Gate 1 verdict: list findings with severity.

        ================================================================
        GATE 2: DEFINE-BEFORE-USE (Gelfand's Law)
        ================================================================

        For every symbol in every formula of this chunk:

        (a) Is it defined at or before this point in the section?
            - If standard concept (Jacobi form, paramodular form, singular
              theta lift, Mukai lattice, Heegner divisor, Weyl vector,
              BKM superalgebra, etc.): add a parenthetical first-principles
              definition at first use. E.g.: "(the Mukai lattice
              $\widetilde\Lambda = H^*(K3,\mathbb{Z})$ with the Mukai
              pairing of signature $(4,20)$)".
            - If novel concept: add a full defining sentence before use.
            - If forward reference: either remove or qualify it
              ("a scalar $c_\rho$, to be defined in §X").

        (b) Is every SUBSCRIPT and SUPERSCRIPT meaningful?
            No undefined decorations. If $\rho$ appears, the reader must
            know whether this is the Weyl vector, an orbifold representation,
            or a separate scalar.

        (c) Is every piece of NOTATION consistent with the rest of the
            manuscript? Check against the notation index if one exists.

        Gate 2 verdict: HARD FAIL if any symbol undefined. List each.

        ================================================================
        GATE 3: CONCEPT MOTIVATION (Etingof + Gelfand)
        ================================================================

        For every definition, construction, or new object in this chunk:

        (a) QUESTION FIRST. Is there a question, obstruction, or tension
            BEFORE the definition that the definition resolves? The reader
            should already be asking "how do we handle X?" before the
            definition of X arrives.

        (b) INEVITABILITY. Does the definition feel forced by what came
            before? Or does it appear ex nihilo? If the latter, the
            preceding material is incomplete: add the forcing question.

        (c) EXAMPLE FIRST (Gelfand). For major constructions: is there
            a concrete example BEFORE the abstract machine runs? The
            reader should understand the example so well that the general
            definition feels like a formality.

        (d) CONNECTIVE TISSUE. At every section/subsection boundary in
            this chunk, ensure:
            1. Where are we? (one sentence: what was just established)
            2. What forces the next step? (the obstruction or question)
            3. What is the answer? (the construction that resolves it)
            These must be MATHEMATICS, not signposts.

        Gate 3 verdict: HARD FAIL if any definition opens cold (no
        motivating question within the preceding 10 lines). List each.

        ================================================================
        GATE 4: PHYSICAL / MODULAR REALIZATION
        (Witten, Borcherds, Polyakov, Harvey-Moore)
        ================================================================

        Examine the chunk for modular / physical content:

        (a) MODULAR / BORCHERDS CLAIMS. For each Borcherds-product or
            singular-theta-lift claim:
            - Is the input Jacobi form named with weight, index, and
              multiplier?
            - Is the Weyl vector exhibited?
            - Is the divisor on the orthogonal / paramodular variety stated?
            - Is the multiplier system on the output form stated?
            - Is the BKM denominator identity (when invoked) stated with
              root multiplicities matched to Jacobi-form coefficients?

        (b) PHYSICAL CLAIMS ($K3 \times E$ side). For each claim
            connecting the Borcherds / BKM construction to a string
            compactification ($\mathcal{N}=4$ heterotic on $K3 \times T^2$,
            type II on $K3 \times T^2$, BPS-index pairings):
            - Is it stated as a theorem (with proof), a heuristic
              (with evidence), or a metaphor (with honest labelling)?
            - Does the BPS-index / root-multiplicity pairing close
              numerically?

        (c) MISSED IDENTIFICATIONS (Polyakov / Harvey-Moore test). Is there
            an identification hiding in the mathematics that should be
            stated as a theorem? "The Borcherds determinant of $\phi_{0,1}$
            IS the BKM denominator" is not a metaphor: it is the content.

        For chunks with no modular/physical content: Gate 4 auto-passes.
        For chunks with modular/physical claims: findings at severity
        >= MODERATE fail the gate.

        ================================================================
        GATE 5: RECONSTITUTION (Chriss-Ginzburg, the fifteen peaks)
        ================================================================

        Reimagine from first principles the platonic ideal of this chunk.
        The chunk sits in context of the entire section processed so far.
        Ask:

        (a) SHOW DON'T TELL. Is this chunk direct construction of
            mathematics, or narration ABOUT mathematics? If narration:
            delete the narration, write the mathematics. The reader
            sees the object, not a description of the object.

        (b) PRECISE MOMENT. Is each element introduced at precisely
            the moment it becomes necessary? Not one paragraph early
            (the reader isn't ready), not one paragraph late (the
            reader is lost). Chriss-Ginzburg pacing.

        (c) SYNTHESIS. Where disparate technical domains meet in this
            chunk (lattices + automorphic forms, BKM + string compactification,
            paramodular + K3 geometry): is the synthesis seamless? Does
            each domain appear because the mathematics FORCES it, not
            because the author wants to display breadth?

        (d) INEVITABILITY. After reading this chunk, does the reader
            feel that the next chunk is FORCED? That the mathematics
            could not stop here?

        (e) PROSE.
            - Delete every signpost ("we now turn to", "having
              established", "it is worth noting", "let us now",
              "this brings us to", "with this in hand").
            - Delete every hedge. Replace with direct statement.
            - Merge every redundancy into a single clean version.
            - No "notably/crucially/remarkably/furthermore/moreover."
            - No dashes where colons or periods suffice.
            - No AI slop of any kind.
            - Standard: Borcherds, Gritsenko, Kac, Mukai, Beilinson,
              Etingof, Bezrukavnikov, Gelfand.
            - BOOKKEEPING SCRUB (HARD). Delete on sight:
              * Session/workflow markers: "Wave N", "round M",
                "batch K", "phase j", "main-thread", "deepening",
                "attack-heal cycle N".
              * DNA/strand naming: "Wave 13 DNA perspective",
                "Wave 13 base point", "DNA strand Sx",
                "Wave N insists/exhibits/sharpens".
              * Catalogue IDs in prose: "AP-CY<n>", "AP<n>",
                "Pattern <n>", "HZ-<n>", "MP<n>", "cache entry <n>".
                These belong in `notes/` or the constellation's
                catalogues, not in theorem/remark/section bodies.
              * Section/subsection/remark titles containing any
                bookkeeping term are INVALID. Rename to name the
                mathematical object/construction/theorem.
              * Author self-reference: "in the present work",
                "the author", "this section's function is to",
                "this preface's role is to", "this remark provides".
              When found, delete the wrapper and replace with direct
              mathematical prose.

        (f) OPENING (first chunk only). If the section opens with a
            summary dump (conclusions before constructions): delete it.
            Start with the first mathematical object.

        (g) COURAGE (Drinfeld + Polyakov + Nekrasov). Are identifications
            stated as identifications, or hedged as analogies? If the
            Borcherds determinant IS the BKM denominator, say "is," not
            "is closely related to." The mathematics earns the equals sign.

        Gate 5 verdict: findings at severity >= MODERATE fail the gate.

        ================================================================
        FIX
        ================================================================

        Apply all fixes to the chunk using the Edit tool.
        After every 3 fixes, build:
            pkill -9 -f pdflatex 2>/dev/null; sleep 2
            cd ~/igusa-cusp-form && make fast
        After every formula fix, grep the manuscript and the constellation
        for variants and propagate the correction (or annotate the
        intentional divergence — convention divergence is load-bearing,
        not silently reconciled):
            ~/igusa-cusp-form/main.tex
            ~/igusa-cusp-form/appendices/
            ~/igusa-cusp-form/notes/
            ~/calabi-yau-quantum-groups/  # the Vol III CY-to-chiral frontier
            ~/topological-strings/        # the BCOV physics dual
            ~/chiral-bar-cobar/  ~/chiral-bar-cobar-vol2/

        ================================================================
        CONVERGENCE TEST
        ================================================================

        ALL SIX GATES must pass at severity >= MODERATE simultaneously.

        If ALL pass: CONVERGED. Advance cursor to next chunk.
        If ANY gate fails: LOOP BACK on this same chunk.

        Safety valve: if chunk_iteration > 11, flag remaining issues
        with % RECTIFICATION-FLAG: [gate, reason] and advance. A
        flagged issue is better than an infinite loop. Document in report.

    END REPEAT

    cursor += (chunk size, adjusted for edits)

END WHILE
```

### Critical Rules for the Chunk Loop

1. **Progressive model.** Each chunk's audit is informed by everything already processed. If chunk 5 reveals a symbol was defined differently in chunk 2, go back and fix chunk 2 (only the specific issue, not a re-audit).

2. **Never skip forward.** If a chunk won't converge after 11 iterations, flag with `% RECTIFICATION-FLAG` and proceed. Document why. Eleven iterations is generous: most chunks converge in 2-3. If you're hitting 8+, the issue is likely structural (belongs in Phase 2) not local.

3. **Build discipline.** After every 3 edits, build. If a fix breaks the build, revert immediately. Never accumulate > 3 unfixed findings.

4. **Grep discipline.** After EVERY formula change, grep the manuscript and the constellation (sister manuscripts) for variants. Fix all instances — or, if a divergence is intentional, annotate it explicitly. Convention divergence is load-bearing; do not silently reconcile (per `CLAUDE.md`).

5. **The double-edged Beilinson.** Every correction must be independently verified. If you cannot verify, mark `% RECTIFICATION-FLAG: [reason]`. A wrong correction is worse than no correction.

6. **Compute verification.** For any numerical formula, verify against `~/igusa-cusp-form/compute/`. Run `verify_lattice.py` / `verify_square_root.py` (or write a targeted script) when a coefficient, multiplicity, or lattice invariant changes.

7. **Gate 2 and Gate 3 are HARD gates.** They cannot be overridden. An undefined symbol or an unmotivated definition is a structural defect that propagates into every subsequent chunk. Fix it or flag it, but never advance pretending it's fine.

---

## PHASE 4: RE-AUDIT (parallel adversarial verification)

After the linear loop completes (all chunks converged or flagged), deploy three independent adversarial agents to re-audit the reconstituted text. This catches errors that the linear sweep introduced or missed.

Launch THREE agents in a SINGLE message (parallel dispatch):

```
Agent(subagent_type="general-purpose", run_in_background=true,
  description="RED re-audit [target]",
  prompt="ADVERSARIAL RE-AUDIT of [TARGET in ~/igusa-cusp-form].
  The text was just fully reconstituted. FALSIFY everything:
  - NEW formulas: recompute from first principles. No pattern-matching.
  - NEW proofs: check every logical step. Hypotheses satisfied? Scope honest?
  - NEW definitions: well-formed? Conflict with existing?
  - UPGRADED claims: justified? Did the proof actually prove this?
  - REMOVED material: was anything load-bearing deleted?
  - Cascade check: did the rewrite chain multiple unchecked claims?
  - DEFINE-BEFORE-USE: every symbol still defined before use after edits?
  - CONVENTION: η-arithmetic, Weyl vector, multiplier system, lattice
    signature, divisor normalization, BKM root multiplicities, w_2 typing,
    paramodular vs orthogonal, Pin^c/Spin^c, ρ overload — all correctly
    tracked.
  - COMPUTE: cross-check ~/igusa-cusp-form/compute/verify_lattice.py and
    verify_square_root.py outputs against any numerical claim.
  Read the FULL file. Output: numbered findings.
  State 'CONVERGED: no actionable findings' if zero issues.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="BLUE re-audit [target]",
  prompt="CONSISTENCY RE-AUDIT of [TARGET in ~/igusa-cusp-form].
  Check after reconstitution:
  - All formulas match the local convention layer (preamble of main.tex,
    raeez-math-template.sty, appendices/) and the compute/ layer
    (verify_lattice.py, verify_square_root.py).
  - All cross-references resolve.
  - Constellation propagation: a formula or convention changed here is
    propagated to (or correctly diverges from, with an annotation) the
    sister manuscripts: ~/calabi-yau-quantum-groups, ~/topological-strings,
    ~/chiral-bar-cobar, ~/chiral-bar-cobar-vol2. Convention divergence is
    load-bearing — report, do not silently reconcile.
  - No regressions on prior attack-heal cycles (~/igusa-cusp-form/notes/).
  - Manuscript compiles cleanly: cd ~/igusa-cusp-form && make fast.
  Output: numbered findings. State 'CONVERGED' if zero.")

Agent(subagent_type="general-purpose", run_in_background=true,
  description="GREEN re-audit [target]",
  prompt="QUALITY RE-AUDIT of [TARGET in ~/igusa-cusp-form] against the
  fifteen-peak standard.
  Assess:
  - Does the prose meet the Russian-school + modular-Borcherds + math-physics
    standard (Beilinson / Drinfeld / Etingof / Kazhdan / Manin / Kac /
    Borcherds / Gritsenko / Mukai / Harvey-Moore / Witten / Polyakov /
    Chriss-Ginzburg)?
  - No AI slop, no hedging, no dashes where colons suffice.
  - Every object earns its place. Every definition motivated. Every
    symbol defined before use.
  - Honest epistemic status (proved / conjectured / heuristic / computed /
    folklore) on every load-bearing claim.
  - Modular and physical claims correctly labelled (theorem / heuristic /
    metaphor); no silent identification of a heuristic with a theorem.
  - Connective tissue at every boundary: where / what forces / what answers.
  - No bookkeeping leakage in prose: 'Wave N', 'AP$n$', 'phase $j$',
    'session $k$', 'in the present work', 'this section sharpens',
    'attack-heal cycle'.
  - Would a hostile referee at Inventiones / Duke / Compositio /
    Annals accept this section?
  Output: numbered findings. State 'CONVERGED' if zero.")
```

When all three report, merge findings. **Convergence test**: if ALL THREE report CONVERGED (zero actionable findings at severity >= MODERATE), proceed to Phase 5. Otherwise, re-enter Phase 3 on the affected chunks only (not the entire section).

---

## PHASE 5: FINAL CONVERGENCE

### 5A. Structural re-assessment

Re-read the ENTIRE file with fresh eyes. The linear sweep may have revealed structural issues invisible at the Phase 2 level:

1. Does it open with a concrete mathematical object?
2. Can a working algebraic geometer or modular-form specialist follow the first page?
3. Does each concept feel INEVITABLE?
4. Is every theorem stated exactly ONCE?
5. Does the section build to its CLIMAX?
6. Is there MOMENTUM? Does each page pull the reader to the next?
7. Would Gelfand say "yes, now I understand"? Would Borcherds say "yes, that is the singular theta lift"?

If structural rewrites needed: apply them, re-run Phase 3 on affected chunks only.

### 5B. Build and test

```bash
pkill -9 -f pdflatex 2>/dev/null; sleep 3
cd ~/igusa-cusp-form && make fast

# Local compute checks:
cd ~/igusa-cusp-form && python compute/verify_lattice.py
cd ~/igusa-cusp-form && python compute/verify_square_root.py

# Optional constellation rebuild for cross-volume sanity:
# cd ~/calabi-yau-quantum-groups && pdflatex main.tex 2>/dev/null || true
# cd ~/topological-strings && make fast
```

### 5C. Report

**CONVERGED.**

- Phase 2 structural iterations (rounds to converge skeleton)
- Total chunks processed in Phase 3
- Total chunk-loop iterations (sum across all chunks)
- Chunks requiring > 1 inner iteration (and which gates failed)
- Total findings fixed, by severity (CRITICAL/SERIOUS/MODERATE/MINOR)
- Total findings fixed, by class (A-logical, B-formula, C-structural, D-status, E-editorial)
- Gate failure distribution (which gates failed most often)
- RECTIFICATION-FLAGs left open (with gate and reason)
- Phase 4 agent verdicts (CONVERGED / re-entry count)
- Final line count
- Build status
- Compute-check status

---

## THE CONNECTIVE TISSUE STANDARD

The connective tissue is the difference between an encyclopedia and a manuscript.

**At every section boundary**, three sentences:
1. **Where are we?** (One sentence: what was just established)
2. **What forces the next step?** (One sentence: the mathematical question or obstruction)
3. **What is the answer?** (One sentence: the construction or theorem that resolves it)

**At every subsection boundary**, one sentence:
- The question this subsection answers, stated as mathematics.

**At every definition**, the reader should already feel: *of course*.

**At every theorem**, the reader should feel: *inevitable*.

Example:
> "The Jacobi form $\phi_{0,1}$ has a singular theta lift to a paramodular form on $\mathcal{H}_2$. The lift's divisor is supported on the Humbert surfaces, but their multiplicities are determined by the Fourier coefficients $c(4mn-\ell^2)$ of $\phi_{0,1}$ — which depend on a sign convention not yet fixed. Fix the sign by demanding that the leading coefficient of the Borcherds product agree with $e^{2\pi i (\rho, Z)}$ for the Weyl vector $\rho$ of $K(1)$."

Three sentences. The first locates. The second names the obstruction. The third announces the resolution. Every section break needs exactly this.
