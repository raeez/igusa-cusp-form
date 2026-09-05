# AGENTS.md — igusa-cusp-form

This repository contains *The Igusa Square Root*, the Borcherds determinant of φ_{0,1},
its denominator algebra, and the K3×E realization problem.

## Authority and scope

Inherit `~/ecosystem/INVARIANTS.md` and the applicable host guidance in
`~/ecosystem/AGENTS-HARNESS.md` or `~/ecosystem/CLAUDE.md`.
For Claude-specific model controls or context loading, consult `~/ecosystem/CLAUDE-HARNESS.md` when needed.
The root AGENTS.md and CLAUDE.md share this contract. Keep their substance aligned.
Work in an assigned isolated worktree. Preserve concurrent changes and principal authorship.
Never use destructive Git operations. Workers do not commit or push.
Research dependencies authorize reading. Write another repository only when the current task assigns it.
Local preparation does not authorize publication, cloud copying, or changes to shared templates.
Stored signatures require exact current authorization for document, capacity, and date.

## Mathematical integrity

Reader-facing manuscript sources contain mathematics or physics only, at every scale, including PDF metadata.
Keep task instructions, audit history, agent references, progress, and ownership records outside the manuscript.
Pass this rule to agents that write manuscript prose and inspect their returned prose.
State mathematical status explicitly: proved, conditional, conjectured, heuristic, computed, expected, folklore, or unverified.
Preserve theorem targets and proof obligations. Repair the argument or construction rather than hide a defect by deletion or demotion.
A bounded investigation may finish with an unresolved obligation, checked failed routes, and the next discriminating step.
That report does not prove the target or establish an obstruction theorem.
Never manufacture proof, coefficients, citations, or validation evidence.

## Read by task

Read the affected source region and its actual dependencies before editing.
Use `rg` to locate symbols, theorem labels, and bibliography keys.
Read [the research reference](docs/igusa-research-reference.md) for the affected thesis, categorical distinction, convention, or obstruction.
Its obstruction criteria preserve the conditional status of the compact Pfaffian and trace identities.
For manuscript prose, read the relevant sections of
`~/ecosystem/MATHEMATICAL_PHYSICS_NUMBER_THEORY_GEOMETRY_ALGEBRA_HOMOTOPY_THEORY_WRITING_STANDARDS.md`.
Use accepted mathematical terms, literal prose, and exact epistemic status. No mannered prose.
For citation or formula changes, consult the corresponding `proj.bib` entry, primary source, and local computation.
Consult `notes/swarm_*/reports/` or optional host memory only for relevant historical evidence, then verify current sources.
Consult companion volumes only when the claim depends on their results. Report discrepancies with exact anchors.
Do not silently reconcile them or assume that a cited source cannot contain an error.

## Verification and completion

Identify the cusp, denominator identity, Borcherds product, lattice, Weyl vector, and claim status affected by a mathematical edit.
Preserve the derivation order: lattice, root datum, Weyl vector, product, modular form.
Check consequential coefficients, exponents, signs, divisors, and multipliers by derivation, primary literature, or exact computation.
Use relevant `compute/` verifiers. `make verify` runs the arithmetic suite when the change affects the suite's shared assumptions.
Inspect the relevant theorem hypotheses and retained-data ledgers before strengthening a conditional conclusion.
Do not equate a clean build, a finite computation, or agent consensus with proof.
After a coherent TeX change, run a local build for the affected source in the assigned worktree without asking again.
Inspect `Makefile` to select the intended target: `make all` builds `main.tex`; the default target builds `platonic/main.tex`.
Use task-owned output and log directories. Inspect command exits and the relevant build logs.
Check references and bibliography, then inspect affected rendered pages. A pre-existing PDF is not evidence of the current build.
Never kill unrelated LaTeX processes. Stop only a verified task-owned process.
`release`, `icloud`, `mathematics-publish`, and architecture aggregation targets have external effects and require matching task authorization.
Instruction-only edits require diff, reference, and metadata review; they do not require a manuscript rebuild.
Report changed paths, checks with results, unresolved mathematical obligations, and the next concrete step.
Continue useful authorized work when another obligation is blocked. Do not prescribe fixed token budgets, timed runs, or subjective pass counts.

## Parallel research

When authorized, partition useful independent work by proof obligation or disjoint files and name the integration owner.
Use available reasoning controls according to mathematical uncertainty and verification cost; do not invent host tools or model names.
Each worker returns its claim, evidence, source anchors, formulas, files changed, checks, and residual obligations.
The accountable owner verifies evidence and integrates substantive content. Cross-repository integration stays within assigned scope.
