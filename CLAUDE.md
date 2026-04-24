# CLAUDE.md — igusa-cusp-form

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## Repo-local

This repository carries the paper *A Borcherds lift of the weak Jacobi form $\phi_{0,1}$, generalized Borcherds–Kac–Moody superalgebras and the Igusa cusp form $\Delta_5$* (2020; Raeez Lorgat). The construction ties a weight-one weak Jacobi form through a generalized BKM superalgebra to the weight-5 Igusa cusp form — a structural sibling of the $K3 \times E$ moonshine frontier held in `~/calabi-yau-quantum-groups` (Vol III) and the BCOV frontier in `~/topological-strings`.

**Source layout.**

- `proj.tex` — root TeX (memoir class, EB Garamond body, newtx math). Entry point.
- `proj.bib` + `proj.bbl` — bibliography.
- `proj.pdf` — rendered artifact.
- `Makefile` — `make` runs `pdflatex → biber → pdflatex → pdflatex`.
- `presentation.key` — companion presentation (Keynote).

**Research constellation role.** The Igusa cusp form $\Delta_5$ is the ur-example of the Borcherds-product / infinite-product structure that the Vol III $\kappa$-stratification generalizes. Any load-bearing claim about BKM superalgebras, Mukai-lattice modularity, or $K3 \times E$ on Vol III must be consistent with the construction here; disagreement is the deliverable, not the shortcut. The BCOV side (topological-strings) is the physics dual to the generating function's modular and mock-modular structure.

**Voice.** `~/ecosystem/INVARIANTS.md §IV` — Russian mathematical school + mathematical-physics frontier. Every load-bearing claim carries honest epistemic status (*proved / conjectured / heuristic / computed / folklore*).

## Long-form proof harness

For Claude Code, Codex CLI, and any GPT-5.5 / GPT-5-Codex-class agent,
frontier mathematics runs in maximum-effort mode. Use the deepest
host-exposed model and reasoning budget. If the host offers a
GPT-5.5 Pro / Heavy or `xhigh` setting, use it for theorem repair,
cross-repo synthesis, adversarial review, and primary-source
reconstruction. The private ChatGPT Pro harness is not public; this is
the open local analogue.

Long runs are normal. A 30-60 minute agent run is acceptable when a
proof obligation requires it. Load `proj.tex`, `proj.bib`, the cited
Borcherds / Gritsenko / Igusa sources, compute files, and Vol III /
topological-strings anchors before the first mathematical edit. Private
scratch stays private; the deliverable is the checked proof trace and
the exact remaining obstruction.

After every proposed repair, run an attack-heal loop: coefficient,
sign, Weyl vector, divisor normalization, multiplier system, exponent,
or false transfer into Vol III. Heal and attack again until the theorem
closes or the exact obstruction is named for the next repair cycle. Do
not downgrade the manuscript to close the loop. Subagents provide
evidence, not authority; the main thread integrates by deep semantic
merge.
