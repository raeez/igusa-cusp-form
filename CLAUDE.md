# CLAUDE.md — igusa-cusp-form

> **Inherits `~/ecosystem/INVARIANTS.md`.** That file holds the canonical ecosystem rules: destructive-git forbidden-command list, multi-agent worktree concurrency, standalone-documents discipline, Russian-school voice, every-file-into-the-repo rule, commits-carry-no-LLM-attribution, deep-semantic-merges, intelligence propagation. Read it first. Repo-local rules follow.

---

## Repo-local

This repository carries the paper *A Borcherds lift of the weak Jacobi form $\phi_{0,1}$, generalized Borcherds–Kac–Moody superalgebras and the Igusa cusp form $\Delta_5$* (2020; Raeez Lorgat). The construction ties a weight-one weak Jacobi form through a generalized BKM superalgebra to the weight-5 Igusa cusp form — a structural sibling of the $K3 \times E$ moonshine frontier held in `~/calabi-yau-quantum-groups` (Vol III) and the BCOV frontier in `~/topological-strings`.

**Source layout.**

- `proj.tex` — root TeX (AMS article class, 9pt, `mathpazo` body). Entry point.
- `proj.bib` + `proj.bbl` — bibliography.
- `proj.pdf` — rendered artifact.
- `Makefile` — `make` runs `pdflatex → biber → pdflatex → pdflatex`.
- `presentation.key` — companion presentation (Keynote).

**Research constellation role.** The Igusa cusp form $\Delta_5$ is the ur-example of the Borcherds-product / infinite-product structure that the Vol III $\kappa$-stratification generalizes. Any load-bearing claim about BKM superalgebras, Mukai-lattice modularity, or $K3 \times E$ on Vol III must be consistent with the construction here; disagreement is the deliverable, not the shortcut. The BCOV side (topological-strings) is the physics dual to the generating function's modular and mock-modular structure.

**Voice.** `~/ecosystem/INVARIANTS.md §IV` — Russian mathematical school + mathematical-physics frontier. Every load-bearing claim carries honest epistemic status (*proved / conjectured / heuristic / computed / folklore*).
