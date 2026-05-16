# A174 -- Cross-Repo Static Verifier

## Result

Read-only cross-repo static verifier completed with no edits.

## Commands

- In each repo: `git status --short`, `git diff --name-only`,
  `git diff --cached --name-only`.
- In each repo: `git diff --check` and `git diff --cached --check`.
- Focused `rg --pcre2 -i` over current touched text paths, excluding PDFs,
  `out/`, raw/processed materials, cache/catalogue/report paths, for
  `CERTIFIED|certified`, `SCHEMA_COMPLETE`, signed \(c(D)\) /
  \(f(nm,l)\) / \(|c(D)|\) / \(|f|\) count language, and
  Schur/celestial/umbral/DT/PT recognition language.

`git diff --check` was clean in all five repos.

## Findings

- Fatal: `calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex:421`
  used signed \(f(nm,l)\) signs as bosonic/fermionic ordinary generator
  counts.
- Fatal: `calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:3273`
  said \(c(D)\) BPS states produce \(c(D)\) Stokes line pairs and walls,
  a cardinality error for signed coefficients.
- High: `calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex:4874`
  used \(\mathrm{mult}(\alpha)=f(nm,l)\) in a generators-and-relations
  presentation.
- Medium: `calabi-yau-quantum-groups/chapters/examples/k3e_bkm_chapter.tex:13711`
  retained guarded \(|c(D)|\) ordinary-dimension surface language.
- Medium: `chiral-bar-cobar-vol2/chapters/examples/examples-complete-conditional.tex:233`
  and `385` used “certified comparison model” proof-status vocabulary.
- Medium: `chiral-bar-cobar/chapters/connections/arithmetic_shadows.tex:1089`
  used “certified by” equation language.

## Non-Findings

- Igusa `SCHEMA_COMPLETE` / `certified` hits were properly guarded as
  schema/status/payload checks, not compact-source certification.
- Vol II `w-algebras.tex` Schur/Borcherds hits checked as negative
  guardrails.
- `topological-strings` DT/PT and Schur hits checked as scalar
  normalization/provenance language.

## Main-Thread Follow-Up

The main thread patched the unassigned certificate-vocabulary and compute
docstring items locally. CYQG BKM/Yangian and physics/programme items were
assigned to focused workers.

