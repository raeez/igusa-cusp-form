# Agent 26 LaTeX Build Hygiene Report

Scope: audit current `main.tex`, `appendices/boundary_compatibility_conditions.tex`, `Makefile`, `raeez-math-template.sty`, `proj.bib`, and current build logs/auxiliary output. I did not edit manuscript source. I did not run a new build because `out/main.pdf`, `out/main.log`, `out/main.blg`, and `.build_logs/main-pass1.log`--`.build_logs/main-pass4.log` are current from 2026-04-29 17:55 SAST and this task is a report-only audit.

## Current build tooling

- Canonical build is `make`, not `latexmk`. No `.latexmkrc` or `latexmkrc` is present in the active file list.
- `Makefile` uses:
  - `pdflatex -interaction=nonstopmode -file-line-error -synctex=0`
  - `bibtex`
  - four TeX passes via `PASSES := 4`
  - `OUT_DIR := out`
  - `.build_logs/main-pass1.log` through `.build_logs/main-pass4.log`
- Source dependency list is `TEX_SOURCES := main.tex $(wildcard appendices/*.tex)`. This correctly rebuilds if an appendix file changes, but a new appendix file still renders only if explicitly `\input` in `main.tex`.
- Bibliography is BibTeX, not biblatex: `main.tex:16084` uses `\bibliographystyle{amsrn}` and `main.tex:16085` uses `\bibliography{proj}`. `raeez-math-template.sty` loads `amsrefs` (`raeez-math-template.sty:424`), which creates citation-style warnings for some `\cite[...]` forms but does not block BibTeX.
- Current PDF evidence: `out/main.pdf` has 208 pages, created 2026-04-29 17:55 SAST. Root-level `proj.log`, `proj.aux`, `proj.blg`, and `proj.bbl` are stale Apr 24 artifacts for `proj.pdf` and should not be used as current truth.

## Label/ref/cite risks

- Parsed active source count:
  - 173 `\label{...}` occurrences across `main.tex` plus the one appendix.
  - 95 unique reference targets via `\ref`, `\eqref`, `\pageref`, `\autoref`, `\cref`, `\Cref`.
  - 80 unique citation keys in active TeX.
  - 91 BibTeX entries in `proj.bib`.
- Current parser results:
  - No duplicate `\label{...}` values found.
  - No missing `\ref`/`\eqref` targets found.
  - No cited key missing from `proj.bib`.
  - `out/main.blg` reports 80 used entries and `warning$ -- 0`.
  - `out/main.log` and `.build_logs/main-pass4.log` contain no undefined reference/citation warnings and no multiply-defined-label warnings.
- Risk: several labels intentionally alias one theorem/proposition. They compile, but a rewrite that renames theorem statements can silently leave stale semantic references:
  - `main.tex:5615` and `main.tex:5616`: `thm:denominator-algebra-identity`, `thm:bracket-level-square-root`.
  - `main.tex:5744` and `main.tex:5745`: `prop:formal-current-envelope`, `thm:factorization-square-root`.
  - `main.tex:12125`--`main.tex:12127`: `prop:compact-igusa-realization-criterion`, `thm:primitive-recognition`, `thm:microscopic-hall-drinfeld-criterion`.
  - `main.tex:15349` and `main.tex:15350`: `prop:eight-formal-current-rows`, `thm:eight-formal-current-rows`.
- Risk: some labels have theorem-type prefixes inconsistent with their enclosing environment:
  - `main.tex:2024` is a `remark`, but `main.tex:2025` labels it `lem:imaginary-wall-orientation-extension`.
  - `main.tex:9929` is a `lemma`, but `main.tex:9930` labels it `prop:sectorial-hall-truncation`.
  - `main.tex:13652` is a `proposition`, but `main.tex:13653` labels it `thm:protected-denominator-shadow`.
  - `main.tex:15841` is a `remark`, but `main.tex:15842` labels it `prop:no-unbuilt-denominator`.
  - `main.tex:15866` is an `openproblem`, but `main.tex:15867` labels it `conj:nonabelian-row-extension`.
- Risk: the rewrite will likely cite agent reports or attack materials. Do not add citations to `notes/...` material unless the manuscript is meant to cite internal files. For primary mathematical claims, cite `proj.bib` entries or add real bibliography entries.
- Risk: `amsrefs` warns at `main.tex:585` for `\cite[Theorem~6.9]{BBDJS2015}` and at `main.tex:609` for `\cite{MasseyST,SaitoMHM}`. These are not build failures. If the rewrite increases optional-argument citations, expect more warnings unless converted to amsrefs-preferred syntax.

## Macro/notation support risks

- Current custom macros in `main.tex:14`--`main.tex:47` cover basic fields/groups/operators and `\autcor`, `\Prim`, `\sdim`, `\sdet`, `\smult`. There are no macros for the proposed rewrite objects:
  - no `\Dalg`
  - no `\Hpre`
  - no `\Htw`
  - no macro for `D^{\mathrm{alg}}`
  - no macro for `H^{\mathrm{pre}}`
  - no macro for `H^{\mathrm{tw}}`
- Plain `D^{\mathrm{alg}}`, `H^{\mathrm{pre}}`, and `H^{\mathrm{tw}}` will compile. The danger is shorthand commands:
  - `\D` is not defined by the local preamble. If used as a macro, it will fail unless some package defines it unexpectedly.
  - `\H` is a TeX accent command, not a Hilbert/state-space macro. Do not write `\H^{pre}` or `\H^{tw}`.
  - `\Dalg`, `\Hpre`, `\Htw` are undefined.
- Current manuscript uses `\mathfrak D_X` heavily for the first-order Dirac/Pfaffian object, e.g. `main.tex:104`, `main.tex:894`, `main.tex:10257`, `main.tex:10610`, `main.tex:11562`. If the rewrite introduces `D^{\mathrm{alg}}_{\Delta_5,C,L}`, keep it visually distinct from `\mathfrak D_X`.
- Current manuscript uses `\mathcal H^{or}_R` and `\widehat{\mathcal H}^{or}_{\sigma,S}` around `main.tex:10255` and `main.tex:10266`. Proposed `H^{\mathrm{pre}}` and `H^{\mathrm{tw}}` need a declared convention: either literal roman superscripts or named macros. Otherwise readers will confuse them with current `\mathcal H^{or}`.
- Template provides theorem environments, `hyperref`, `bookmark`, `longtable`, `booktabs`, and `makecell`. I did not see `tabularx` or `adjustbox` loaded. Do not use `tabularx`, `X` columns, or `\adjustbox` in the rewrite without adding packages in the preamble.
- `raeez-math-template.sty` is a symlink to `../latex-template/raeez-math-template.sty`. Build reproducibility depends on that sibling path in this checkout.

## Appendix/sectioning risks

- The document class is `memoir`, but the manuscript uses `\part` plus `\section`, not `\chapter`.
- `main.tex:4`--`main.tex:5` set section numbering and hyperref anchors for the main text:
  - `\renewcommand{\thesection}{\arabic{section}}`
  - `\renewcommand{\theHsection}{\arabic{section}}`
- `main.tex:14554` starts appendices with `\appendix`.
- `main.tex:14555`--`main.tex:14556` resets visible section numbers and hyperref section anchors to appendix letters:
  - `\renewcommand{\thesection}{\Alph{section}}`
  - `\renewcommand{\theHsection}{appendix.\Alph{section}}`
- Current appendix labels resolve as:
  - `app:sk-shadow` -> Appendix A (`out/main.aux:610`)
  - `app:eight-row-boundary` -> Appendix B (`out/main.aux:626`)
  - `sec:n1-boundary-compatibility-conditions` -> Appendix C (`out/main.aux:711`)
- Risk: the appendix file `appendices/boundary_compatibility_conditions.tex` begins with `\section` and assumes `main.tex` has already issued `\appendix`. Building it standalone will not work without a wrapper.
- Risk: the appendix C label uses a `sec:` prefix, not `app:`. It compiles, but a rewrite should prefer `app:n1-boundary-compatibility-conditions` if references are being normalized.
- Risk: `main.tex:567` is `\subsection*{Schema of the local protected observable algebra}` followed by `\label{sec:local-protected-observable-algebra}` at `main.tex:568`. The aux label points to `section*.13` but carries visible number `2`. A `\ref` to this anchor will likely print the enclosing section number, not a subsection number. Avoid referencing it as a numbered section without changing the sectioning.
- Risk: adding new appendices after `main.tex:16081` but before bibliography is safe. Adding appendices after `\bibliography{proj}` is not.

## Table/layout risks

- Current Apr 29 build has no fatal TeX errors, but it has many overfull boxes. These are not hypothetical. Worst current overfulls:
  - `main.tex:7771`: 580.27945 pt too wide. This is a long obstruction/certificate tuple display.
  - `main.tex:11598`: 201.66995 pt too wide. Another long tuple display.
  - `main.tex:6942`: 124.37651 pt too wide.
  - `main.tex:3423`: 104.09726 pt too wide.
  - `main.tex:4784`: 95.50723 pt too wide.
  - `appendices/boundary_compatibility_conditions.tex:51`: 82.33887 pt too wide.
  - `main.tex:10330`: 81.14426 pt too wide.
- Current dense tables:
  - `main.tex:357`--`main.tex:387`: three `p{...}` columns under `\small`.
  - `main.tex:399`--`main.tex:452`: three `p{...}` columns under `\small`; current overfulls at lines 406, 413, 433 are here.
  - `main.tex:14374`--`main.tex:14444`: six-column `scriptsize` table using `p{...}` columns. It generates many underfull boxes and is fragile under rewrite.
  - `appendices/boundary_compatibility_conditions.tex:27`--`51`: two-column math `array`; current overfull at line 51.
- Risk: construction-first rewrite objects such as `D^{\mathrm{alg}}_{\Delta_5,C,L}`, `H^{\mathrm{pre}}_{X,\Gamma}`, and `H^{\mathrm{tw}}_{X,\Gamma}` will lengthen already wide tuple displays. Do not add them to the existing long tuple displays without breaking into `aligned`, `gathered`, `split`, or separate enumerated clauses.
- Risk: if the rewrite moves certificate tables into the introduction, the current tables will not survive as-is on letter paper. Use `longtable`/`booktabs`/`makecell` already available, or prose lists. Do not assume `tabularx`.
- Risk: repeated `$$ ... $$` displays are prevalent. They compile. If the rewrite introduces multiline theorem displays, prefer `\[...\]` with `aligned`/`split` to control overfull boxes and anchors.

## Build/check command plan

Run after any manuscript rewrite, in this order:

1. Static undefined-label scan:
   ```sh
   perl -0777 -ne 'while(/\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){$r{$x}=1}} while(/\\label\{([^{}]+)\}/g){$l{$1}=1} END{for $x(sort keys %r){print "$x\n" unless $l{$x}}}' main.tex appendices/*.tex
   ```
2. Static duplicate-label scan:
   ```sh
   perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){$c{$1}++} END{for $k(sort keys %c){print "$c{$k} $k\n" if $c{$k}>1}}' main.tex appendices/*.tex
   ```
3. Static missing-cite scan:
   ```sh
   comm -23 \
     <(perl -0777 -ne 'while(/\\(?:cite|citep|citet|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){print "$x\n"}}' main.tex appendices/*.tex | sort -u) \
     <(perl -ne 'if(/^\s*@\w+\s*\{\s*([^,\s]+)\s*,/){print "$1\n"}' proj.bib | sort -u)
   ```
4. Cheap compile smoke test if the change is small:
   ```sh
   make fast
   ```
   This catches undefined control sequences, syntax errors, and some overfull explosions. It does not validate bibliography or final references.
5. Canonical build before handoff:
   ```sh
   make
   ```
6. Log gate after `make`:
   ```sh
   rg -n '(^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Warning: (Reference|Citation).*undefined|There were undefined|Label .* multiply defined|Overfull \\hbox)' .build_logs/main-pass4.log out/main.log out/main.blg
   ```
7. If a visual release is intended, inspect `out/main.pdf` around any table/display touched by the rewrite, especially pages containing source lines listed in the Table/layout risks section.

## main.tex anchors

- Preamble and manuscript-owned macros: `main.tex:1`--`49`.
- Title metadata: `main.tex:7`--`9`.
- Abstract: `main.tex:57`--`172`.
- Table of contents: `main.tex:175`.
- Introduction and claim strength: `main.tex:177`.
- Early claim-status tables: `main.tex:357`--`387`, `main.tex:399`--`452`.
- Part I: `main.tex:462`; physical question begins `main.tex:464`; local protected observable schema begins `main.tex:567`; one-particle determinant section begins `main.tex:640`.
- Part II: `main.tex:2632`; D6--D2--D0 dictionary begins `main.tex:2634`; normal-ordered Gram descent begins `main.tex:4309`.
- Part III: `main.tex:5022`; denominator algebra begins `main.tex:5560`; compact Dirac--Igusa realization begins `main.tex:5704`.
- Current source-interface/certificate zone: `main.tex:5704`--`13278`. This is where proposed `D^{\mathrm{alg}}`, `H^{\mathrm{pre}}`, and `H^{\mathrm{tw}}` insertions will collide with existing notation.
- Primitive recognition theorem aliases: `main.tex:12124`--`12127`.
- Scalar square section: `main.tex:13701`; OP square theorem label at `main.tex:13807`.
- Synthesis theorem: `main.tex:14031`--`14032`.
- Diagonal-divisor rows part: `main.tex:14267`; dense row table starts `main.tex:14374`.
- Appendix transition: `main.tex:14554`--`14556`.
- Appendix A: `main.tex:14558`; Appendix B: `main.tex:14689`; Appendix C input: `main.tex:16081`.
- Bibliography: `main.tex:16084`--`16085`.
- External appendix file starts: `appendices/boundary_compatibility_conditions.tex:1`--`2`.

## Patch queue

1. Add notation macros if the rewrite repeatedly uses the proposed objects. Suggested safe forms:
   ```tex
   \newcommand{\Dalg}{D^{\mathrm{alg}}}
   \newcommand{\Hpre}{H^{\mathrm{pre}}}
   \newcommand{\Htw}{H^{\mathrm{tw}}}
   ```
   Do not define `\H`. Do not use `\D` unless deliberately defined and checked.
2. Normalize semantically wrong label prefixes and update references in one mechanical pass:
   - `lem:imaginary-wall-orientation-extension` -> `rem:imaginary-wall-orientation-extension`
   - `prop:sectorial-hall-truncation` -> `lem:sectorial-hall-truncation` or rename the environment to proposition if proposition status is intended
   - `thm:protected-denominator-shadow` -> `prop:protected-denominator-shadow`
   - `prop:no-unbuilt-denominator` -> `rem:no-unbuilt-denominator`
   - `conj:nonabelian-row-extension` -> `op:nonabelian-row-extension`
3. Decide which alias labels are intentional compatibility anchors. If the rewrite is allowed to break old anchors, collapse aliases to one canonical label per theorem/proposition. If not, keep aliases but document them near the theorem.
4. Add labels to any theorem-like environments that the rewrite will reference. Many current theorem-like environments are unlabelled; this is fine until the rewrite refers to them.
5. Split the worst tuple displays before adding new source-object notation. The highest-priority current breakpoints are `main.tex:7771`, `main.tex:11598`, `main.tex:6942`, `main.tex:3423`, and `appendices/boundary_compatibility_conditions.tex:51`.
6. Replace or compress the six-column row table at `main.tex:14374` if row material remains in the core manuscript. It already produces severe underfull boxes; added prose will degrade layout.
7. If new appendix files are created, add explicit `\input{appendices/...}` before `main.tex:16084`, and use `app:` labels for appendix sections.
8. Keep bibliography changes in `proj.bib`; do not cite internal attack reports from the paper unless they are meant to become public artifacts.

## Residual build checks

- I did not rerun `make` or `make fast`; existing Apr 29 logs were current and the task was report-only.
- Current build state is clean with respect to fatal TeX errors, undefined refs, undefined cites, duplicate labels, and BibTeX warnings.
- Current build state is not layout-clean. Overfull boxes are already present and severe; the planned construction-first rewrite must treat display width as a first-class build gate.
- After edits, the final handoff should include:
  - `make` success.
  - zero undefined reference/citation warnings in `.build_logs/main-pass4.log` and `out/main.log`.
  - zero duplicate-label warnings.
  - `out/main.blg` with no missing-entry warnings.
  - an explicit list of remaining overfull boxes, or a statement that all overfulls introduced by the rewrite were fixed.
  - visual inspection of pages containing the rewritten source-object definitions, the introduction tables, and appendices.
