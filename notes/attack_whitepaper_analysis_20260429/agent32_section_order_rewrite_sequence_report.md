# Agent 32 Section-Order Rewrite Sequence Report

Scope: section-order rewrite plan only. I did not edit `main.tex`, `proj.bib`,
`appendices/`, or existing source. Sources mined: current `main.tex`, the Apr
29 attack transcript in `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`
backed by `materials/raw/2026-04-29-attack-whitepaper-analysis.pdf`, `Makefile`,
and the Apr 29 swarm reports present under
`notes/attack_whitepaper_analysis_20260429/`.

Adversarial premise: the final paper must not let a referee infer compact
Hall/factorization geometry from the Borcherds product, from the OP scalar
square, from the Gritsenko--Nikulin denominator algebra, or from orientation
normalization constants. The section order must make the theorem spine visible
before the residual ledgers.

## Target TOC

Target main paper:

1. **Abstract**
   - Five paragraphs only: protected K3 input and virtual determinant;
     imported Gritsenko--Nikulin denominator target; formal Mukai/Gram
     normal-ordering repair; OP/DT scalar square as second-order check;
     compact Dirac--Igusa realization as open.
   - No eight-row details. No spin \(L\)-factor. No full compact-source
     checklist.

2. **Introduction: The Dirac Problem**
   - Dirac principle: first-order protected object before scalar trace.
   - One theorem-program display:
     \[
     \text{K3 protected index}
     \to K_0\text{-Borcherds determinant}
     \to \text{GN denominator target}
     \to \text{normal-ordered Gram descent}
     \to \text{compact Dirac--Igusa realization problem}.
     \]
   - One status table: constructed here, imported, conditional, open.
   - One forbidden-implications table:
     \[
     \mathcal D_X=\Delta_5 \not\Rightarrow \mathfrak D_X,\quad
     \Delta_5^2 \not\Rightarrow \epsilon_o,\quad
     \mathfrak g_{\Delta_5}\not\Rightarrow\text{compact Hall source},\quad
     \Gamma_{\mathrm{gram}}\neq\text{Hall charge lattice}.
     \]
   - One notation table: \(\mathcal D_X,D_5,\Delta_5,\chi_{10}^{OP},
     \Gamma_X^{form},\Gamma_{gram},\widehat\Gamma_X,\mathfrak g_{\Delta_5},
     \mathfrak D_X\).

3. **Virtual Borcherds Package and the \(K_0\)-Determinant**
   - Current determinant core from `main.tex:640-918`.
   - Rename away from "one-particle" unless locally qualified as virtual.
   - Convert `prop:dirac-pfaffian-recognition-target` into a definition or
     open problem, not a proposition.

4. **The Normalized Igusa Target**
   - Current normalized cusp form and BGN normalization from
     `main.tex:2383-2630`.
   - Keep \(D_5=64^{-1}\Delta_5\), theta-leading coefficient \(64\),
     automorphic line, and the short Maass/reflection character summary.
   - Move detailed Maass generator computations and Bott/sign discussion to
     appendices.

5. **D6--D2--D0 Variables and the Mukai--Gram Dictionary**
   - Current `main.tex:2634-2845`.
   - Promote the Mukai-vector dictionary at `main.tex:2661` to theorem-level.
   - Resolve and state the \(d\) versus \(m=d-1\) convention before any
     hybrid/source section.

6. **Normal-Ordered Gram Descent**
   - Current `main.tex:4309-4977`.
   - This is the central new formal section. It must precede compact
     realization.
   - Include the flag formula and define raw fixed-lift pushforward before
     `thm:raw-gram-descent-no-go`.

7. **The Denominator Algebra**
   - Current `main.tex:5024-5702`, compressed.
   - Keep exterior-square model and Weyl chamber only to the extent needed
     for the denominator identity.
   - State active-support signed supermultiplicities and the determinant-does-
     not-determine-brackets warning.

8. **Compact Dirac--Igusa Realization Problem**
   - Current `main.tex:464-638` plus compressed current
     `main.tex:5704-13700`.
   - Start with protected operations before traces and the source/target
     firewall.
   - Main text contains only:
     - algebraic target current envelope, renamed as target-only and preferably
       curve-universal;
     - compact source interfaces \(H^{pre},H^{tw},\mathcal F^{hyb}\) as
       constructed/conditional/open with exact status;
     - orientation/Pfaffian summary theorem;
     - primitive recognition certificate.
   - Full O1/O1+/O2, finite-source, hybrid, Koszul, D0, and wall ledgers move
     to appendices.

9. **The OP/DT Scalar Square**
   - Current `main.tex:13701-13955`.
   - Keep late. Box the rule: OP/DT proves the scalar square, not the
     first-order square root. Constants \(64\), \(4096\), and the OP minus
     sign are scalar normalization data.

10. **Coefficient Dictionary and Claim-Strength Synthesis**
    - Current `main.tex:13957-14264`, compressed.
    - The final theorem should close only the N=1 determinant/normal-ordering/
      denominator/scalar-square story and explicitly leave compact realization
      open unless the source objects were actually built.

11. **Independent Diagonal-Divisor Row Ledger** optional main final part
    - Current `main.tex:14267-14552`.
    - Rename from "CHL boundary physics" to "Diagonal-divisor rows and
      denominator certificates" or move entirely to companion.
    - If retained, start with: "This part is independent of the N=1
      Dirac--Igusa theorem."

Target appendices:

1. **Fourier, Automorphic-Line, and Sign Conventions**
   - Move full Maass generator checks and Bott/sign remarks here.
2. **Orientation Gerbes, Quotient Characters, and Pfaffian Wall Signs**
   - Move current `main.tex:920-2381` and `main.tex:2848-4305` here, after
     compressing main-text orientation content.
3. **Compact-Source Residual Certificates**
   - Move most of current `main.tex:5704-13700` here after a short main
     section remains.
4. **Diagonal-Divisor Boundary Rows** optional
   - Current `main.tex:14689-16081`, only if not moved to companion.
5. **N=1 Boundary Compatibility**
   - Keep `\input{appendices/boundary_compatibility_conditions}`.

Move out of the paper by default:

- Current spin \(L\)-factor appendix `main.tex:14558-14686`. It is an
  independent arithmetic normalization note unless a main theorem cites it.

## Move Map With Current Anchors

| Current anchor | Current role | Action | Destination | Depends on |
|---|---|---|---|---|
| `main.tex:57-172` | overloaded abstract | Replace as a whole; keep only determinant, GN denominator, normal-ordering, OP scalar, open compact problem | Abstract | none |
| `main.tex:177-462` | introduction plus repeated status ledgers | Rewrite in place; rename section; merge tables; add forbidden implications and notation table | Section 1 | abstract rewrite |
| `main.tex:462` | `\part{The automorphic square root}` | Retitle or remove part boundary; do not let "square root" appear before Dirac principle | before Sections 3-4 | intro rewrite |
| `main.tex:464-638` | "physical question" and local protected observable schema | Rename to protected source problem; move later into compact realization section, or keep short summary in intro and move detailed schema to Section 8 | Section 8 plus orientation/source appendix | intro source/target table |
| `main.tex:640-918` | K3 index, \(K_0\) half, virtual determinant, Dirac target proposition | Keep as main technical opening; rename section; convert `prop:dirac-pfaffian-recognition-target` to definition/open problem | Section 3 | abstract and intro guardrails |
| `main.tex:920-2381` | early O1/O1+/O2 and Pfaffian wall package | Move out of early main; keep only a short conditional sign theorem in Section 8 | Appendix B | Section 8 summary must be inserted first |
| `main.tex:2383-2630` | normalized cusp form, Maass, Bott/sign, BGN | Split: keep normalization and BGN in main; move Maass details and Bott/sign to appendix | Section 4 plus Appendix A | determinant section before it |
| `main.tex:2509-2528` | Bott/sign/Gram polarization remark | Delete from main or move to sign conventions; keep negative framing only | Appendix A | after Section 4 split |
| `main.tex:2634-2845` | D6--D2--D0 dictionary and scalar quotient setup | Promote dictionary; keep before normal ordering; scalar quotient details can remain here only if not duplicating Section 9 | Section 5 | normalized target |
| `main.tex:2848-4305` | orientation monodromy, quotient cohomology, finite stabilizers | Move to orientation appendix; main gets theorem-status summary only | Appendix B | Section 8 summary |
| `main.tex:4309-4977` | physical charge and normal-ordered Gram descent | Move earlier and retitle; make central theorem section | Section 6 | D6 dictionary and notation table |
| `main.tex:5024-5702` | exterior-square model, Weyl chamber, denominator algebra | Keep after normal-ordering; compress automorphic checks | Section 7 plus Appendix A | Section 6 |
| `main.tex:5704-13700` | compact realization plus long source ledgers | Collapse main to source/target problem and exact missing certificates; move most detailed ledgers | Section 8 plus Appendix C | Sections 3, 6, 7 |
| `main.tex:13701-13955` | OP/DT scalar square | Keep late; strengthen orientation-forgetting warning | Section 9 | denominator and compact problem stated |
| `main.tex:13957-14264` | coefficient dictionary and synthesis | Compress final theorem; remove row/spin closure language | Section 10 | Sections 3-9 |
| `main.tex:14267-14552` | row main section | Rename and quarantine; optional final independent part | Section 11 or companion | synthesis closed first |
| `main.tex:14554-14556` | appendix transition | Keep transition after all retained main sections | before appendices | row decision |
| `main.tex:14558-14686` | spin \(L\)-factor appendix | Move out unless cited; if retained, make Appendix after all proof appendices and begin with independence disclaimer | companion by default | reference scan |
| `main.tex:14689-16081` | detailed eight-row boundary appendix | Compress or move to companion; if retained, make optional row appendix | Appendix D | row decision |
| `main.tex:16081` | N=1 boundary compatibility input | Keep; ideally last retained appendix before bibliography | Appendix E | appendix transition |
| `main.tex:16084-16085` | bibliography | Keep last | bibliography | all appendix inputs before this |

## Incremental Rewrite Sequence

This is the patch order that keeps the paper buildable after each stage. Do
not combine large moves with mathematical rewrites unless the static label scan
is clean.

0. **Preflight inventory.**
   - Run `git status --short`; do not revert other agents.
   - Run static duplicate/missing label scans before touching source.
   - Record current section anchors with:
     `rg -n '^\\(part|appendix|input|bibliography|bibliographystyle)\\b|^\\section\\{' main.tex`.
   - Rationale: the worktree already contains concurrent reports and generated
     artifacts.

1. **Apply mechanical P0 hygiene before moving blocks.**
   - Replace undefined `\Gamma_{\mathrm{eff}}^+` at `main.tex:1954`.
   - Add radical quotient to the early primitive comparison display at
     `main.tex:286-291`.
   - Repair `H^2_{\mathrm{sym}}`/cochain language at `main.tex:4366-4368`
     and `main.tex:4811-4830`.
   - Separate raw placement \(i_0(c)=(c,0)\) from split section
     \(s(c)=(c,\Pi_X(c))\) near `main.tex:4672-4682`.
   - Add the normal-ordering flag formula after `main.tex:4881`.
   - Define raw homogeneous/fixed-lift pushforward before
     `main.tex:4883`.
   - Build checkpoint: `make fast`; then static label scan. No section move
     yet.

2. **Rewrite abstract and introduction in place.**
   - Replace `main.tex:57-172`.
   - Rename `main.tex:177` to `Introduction: The Dirac Problem`; keep the old
     label as a compatibility label or update every reference in the same
     patch.
   - Merge `main.tex:357-453` into one status table.
   - Insert forbidden-implications and notation tables immediately after the
     status table.
   - Move row material out of first-page prose: compress `main.tex:339-355`
     to one independent-row sentence or delete from the opening.
   - Build checkpoint: `make fast`; inspect first 10 pages if possible.

3. **Retitle without moving.**
   - `main.tex:464`: rename `The physical question` to `Protected Operations
     Before Traces` or `The Compact Source Problem`.
   - `main.tex:640`: rename to `Virtual Borcherds Package and the
     \(K_0\)-Determinant`.
   - `main.tex:14267`: rename to `Independent Diagonal-Divisor Row Ledger` if
     retained.
   - Convert the environment around `main.tex:882-918` from proposition to
     definition/open problem. Preserve the old label until all refs are
     updated.
   - Build checkpoint: `make fast`.

4. **Split and place the normalized target.**
   - Move the safe core of `main.tex:2383-2630` directly after the determinant
     section.
   - Keep `prop:bgn-identification`, \(D_5=64^{-1}\Delta_5\), and the leading
     coefficient \(64\).
   - Move detailed Maass generator computations and `rem:bott-sign-normalization`
     to Appendix A in the same patch, preserving labels.
   - Build checkpoint: `make fast`; run label scan. If appendix headings are
     introduced, confirm they are before `\bibliography`.

5. **Promote the D6--D2--D0 dictionary.**
   - Keep `main.tex:2634-2845` after normalized target.
   - Promote `lem:mukai-vector-ideal-sheaf-sxe` to theorem/headline
     proposition, but preserve the old label or update all refs in the same
     patch.
   - Define the Mukai pairing before the first displayed Gram formula.
   - Add a single convention sentence: geometric elliptic degree \(d\) and
     Borcherds/Gram exponent \(m=d-1\) are not the same symbol.
   - Build checkpoint: `make fast`.

6. **Move normal-ordering forward.**
   - Move `main.tex:4309-4977` immediately after the D6 dictionary.
   - Rename `Physical charge and normal-ordered Gram descent` to
     `Normal-Ordered Gram Descent`.
   - Preserve `sec:duality-principle` as a compatibility label if any refs
     still use it; add a new `sec:normal-ordered-gram-descent` label if
     desired.
   - Dependencies: P0 cochain repairs and raw-pushforward definition must
     already be present.
   - Build checkpoint: `make fast`; inspect references to
     `thm:raw-gram-descent-no-go`.

7. **Move denominator algebra after normal-ordering.**
   - Keep `main.tex:5024-5702` after Section 6.
   - Compress exterior-square and Weyl material if needed, but do not move
     denominator labels during the same patch.
   - Keep `thm:denominator-algebra-identity`; treat
     `thm:bracket-level-square-root` as an alias only if current references
     require it.
   - Add the warning that signed dimensions do not determine brackets if not
     already present near the theorem.
   - Build checkpoint: `make fast`.

8. **Insert the short compact-realization main section.**
   - Before moving any long source/orientation block, write a short Section 8
     skeleton with:
     - source/target firewall;
     - \(H^{pre}\), \(H^{tw}\), hybrid source status;
     - orientation/Pfaffian status;
     - primitive recognition status and radical quotient;
     - forward references to appendices.
   - Use literal \(H^{\mathrm{pre}}\), \(H^{\mathrm{tw}}\) unless macros are
     added in a separate preamble patch. Do not use undefined `\Hpre` or
     `\Htw`.
   - Build checkpoint: `make fast`.

9. **Move orientation material to Appendix B.**
   - Move current `main.tex:920-2381` and `main.tex:2848-4305` after
     `\appendix` under `Orientation Gerbes, Quotient Characters, and Pfaffian
     Wall Signs`.
   - Preserve labels: `def:orientation-line`,
     `op:orientation-monodromy-character`, `lem:E-equivariant-descent-obstruction`,
     `prop:finite-stage-quotient-orientation-character-system`,
     `lem:local-pfaffian-wall-sign`, and related O1/O1+/O2 labels.
   - The main section must keep a short conditional theorem before this move,
     so all concepts still have an ordered narrative.
   - Build checkpoint: `make fast`; static label scan.

10. **Collapse compact source ledgers.**
    - Keep a short main compact section from current `main.tex:5704-13700`.
    - Move detailed formal current envelope, \(E_3\) interface, QME/anomaly,
      hybrid, normal-ordering cochain, D0, finite Hall source, Koszul, and
      primitive certificate ledgers to Appendix C.
    - Rename `\mathsf{Den}_{\Delta_5,E}` to a target-current name only after
      the source/target firewall is in place. Prefer curve-universal notation
      if actually introduced.
    - Do not state \(H^{pre}\) or \(H^{tw}\) as constructed unless the
      corresponding gerbes, correspondences, state spaces, products, coproducts,
      and primitives have been defined.
    - Build checkpoint: `make fast`; inspect overfull boxes because these
      blocks contain the worst current tuple displays.

11. **Keep OP scalar late and sharpen it.**
    - Keep `main.tex:13701-13955` after compact realization.
    - Add the boxed warning: OP/DT proves \(D_5^2\), not \(D_5\); scalar
      constants are not orientation data.
    - Do not move OP scalar earlier in the proof chain.
    - Build checkpoint: `make fast`.

12. **Rewrite final synthesis.**
    - Compress `main.tex:13957-14264`.
    - The theorem `thm:protected-igusa-determinant` should summarize only:
      virtual determinant, normal-ordering, GN denominator target, OP scalar
      square, open compact comparison.
    - Remove row and spin from the dependency closure. Mention rows only as an
      independent extension if retained.
    - Build checkpoint: `make fast`.

13. **Quarantine rows and spin.**
    - Run `rg -n 'app:sk-shadow|Spin|L_\\{\\mathrm\\{spin\\}\\}|andrianov|Andrianov' main.tex appendices`.
      If no main theorem references spin, move `main.tex:14558-14686` out to a
      companion note or remove from the active paper in one patch.
    - If rows stay, keep one independent main row ledger and one optional row
      appendix. Do not keep two duplicate row catalogues at full length.
    - Add row independence disclaimer at the start of retained row material.
    - Build checkpoint: `make fast`, then full `make`.

14. **Final label and environment cleanup.**
    - Normalize semantic label prefixes only after the final section order is
      stable.
    - Run duplicate-label, missing-ref, missing-cite scans.
    - Run full `make`.
    - Log gate:
      `rg -n '(^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Warning: (Reference|Citation).*undefined|There were undefined|Label .* multiply defined|Overfull \\hbox)' .build_logs/main-pass4.log out/main.log out/main.blg`.

## Label/Reference Preservation Plan

Preserve labels during physical moves. Rename labels only after the paper
builds in its new order.

| Current label | Final treatment | Reason |
|---|---|---|
| `sec:introduction-claim-strength` | Keep as compatibility label; add `sec:introduction-dirac-problem` if desired | References survive section rename |
| `sec:physical-question` | Keep if block becomes compact source problem; optionally add `sec:compact-source-problem` | Avoid broken refs during move |
| `sec:local-protected-observable-algebra` | Convert unnumbered subsection to numbered or avoid `\ref`; preserve label if referenced | Current label is on `\subsection*` and resolves weakly |
| `prop:virtuality-of-the-square-root` | Preserve | Stable theorem-spine warning |
| `prop:dirac-pfaffian-recognition-target` | Rename semantically to `op:dirac-pfaffian-target-problem`; keep old as alias until refs updated | Current proposition type overclaims |
| `def:type-ii-pfaffian-wall-certificate`, `prop:o2-local-obstruction-certificate` | Preserve in orientation appendix | Useful exact anchors |
| `thm:dirac-pfaffian-recognition-conditional` | Split theorem; keep old label on the short summary theorem only if refs require it | Current all-in-one theorem mixes datum, Pfaffian, scalar, sign, character |
| `def:orientation-line`, `op:orientation-monodromy-character` | Preserve in orientation appendix | Core open orientation anchors |
| `prop:bgn-identification` | Preserve in normalized target section | Core normalization theorem |
| `lem:mukai-vector-ideal-sheaf-sxe` | Promote environment but preserve label or add `thm:mukai-vector-ideal-sheaf-sxe` and update refs | Dictionary becomes theorem-level |
| `sec:duality-principle` | Preserve as compatibility; add `sec:normal-ordered-gram-descent` | Existing name is semantically stale |
| `def:dyonic-mukai-lattice`, `def:additive-physical-charge-lattice`, `lem:gram-additivity-defect`, `def:gram-corrected-charge-extension`, `thm:raw-gram-descent-no-go` | Preserve | Normal-ordering theorem spine |
| `thm:denominator-algebra-identity` | Preserve | Imported GN target theorem |
| `thm:bracket-level-square-root` | Treat as alias; rename only after refs are updated | Label name risks overclaim |
| `prop:formal-current-envelope` | Preserve but retitle statement as target current envelope | Stable target object |
| `thm:factorization-square-root` | Rename if touched; keep only as compatibility alias if necessary | False semantic signal for formal current envelope |
| `thm:primitive-recognition`, `prop:compact-igusa-realization-criterion`, `thm:microscopic-hall-drinfeld-criterion` | Preserve aliases until final ref cleanup | Multiple labels on same theorem currently compile |
| `thm:op-square`, `prop:op-normalization`, `def:op-normalization-branch` | Preserve | Scalar-square anchor |
| `sec:coefficient-dictionary-main-synthesis`, `thm:protected-igusa-determinant` | Preserve | Final synthesis anchor |
| `sec:eight-dd-rows-status` | Preserve if row ledger remains; add `sec:independent-dd-row-ledger` | Avoid breaking row refs |
| `app:sk-shadow` | Remove only after ref scan proves unused; otherwise keep with independence disclaimer | Spin appendix likely companion |
| `app:eight-row-boundary` | Preserve if row appendix remains | Row audit anchor |
| `sec:n1-boundary-compatibility-conditions` in appendix input | Preserve; optionally add `app:n1-boundary-compatibility-conditions` | Current prefix is semantically weak but buildable |

Label-prefix mismatches to normalize only after section order stabilizes:

- `lem:imaginary-wall-orientation-extension` is on a remark.
- `prop:sectorial-hall-truncation` is on a lemma.
- `thm:protected-denominator-shadow` is on a proposition.
- `prop:no-unbuilt-denominator` is on a remark.
- `conj:nonabelian-row-extension` is on an open problem.

Do not cite agent reports or the attack transcript from the public paper unless
they are intentionally made public sources. Use them as integration evidence,
not bibliography.

## What To Postpone

Postpone these until after the section-order rewrite builds cleanly:

1. **Actual construction of \(H^{pre}_{X,\Gamma}\) and \(H^{tw}_{X,\Gamma}\).**
   The attack transcript demands construction-first, but current `main.tex`
   does not contain the object-level construction. Do not upgrade certificate
   language to theorem language unless the objects, gerbes, lifted
   correspondences, anti-invariant state spaces, products, coproducts,
   primitives, and transition maps are all supplied.

2. **Full orientation theorem.**
   O1/O1+/O2 remain conditional. Maass values are automorphic target data, not
   Hall orientation proof. OP scalar signs and \(4096\) stay irrelevant to
   \(\epsilon_o\).

3. **Primitive presentation theorem.**
   Signed dimensions do not determine a Lie algebra. Source representatives,
   parity split, Serre/orthogonality constants, Hopf pairing, closed radical,
   no-extra-relations, PBW, and exact completion are separate obligations.

4. **Full hybrid local/wrapped source.**
   The projection-to-\(E\) support-locality obstruction is theorem-level, but
   the mixed LL/LW/WL/WW correspondences and eight flag atlas remain source
   construction work unless explicitly built.

5. **Eight-row atlas as core theorem.**
   Rows are a quarantine ledger and extension catalogue. They do not belong in
   the N=1 proof spine unless a row is used by a theorem in Sections 1-10.

6. **Spin \(L\)-factor appendix.**
   Move to companion unless a main theorem begins to use it. It adds a separate
   hostile-referee audit surface and contributes nothing to the Dirac--Igusa
   proof chain.

7. **Primary-source row bibliography pass.**
   Row source theorem/page checks are publication debt, but they should not
   block the section-order rewrite unless row material stays in the main paper.

8. **Macro refactor.**
   Add `\Dalg`, `\Hpre`, `\Htw` only if the rewritten source uses them
   repeatedly. Literal \(D^{\mathrm{alg}}\), \(H^{\mathrm{pre}}\),
   \(H^{\mathrm{tw}}\) compile without preamble changes. Never use `\H` as a
   macro; it is a TeX accent.

## Build Checkpoints

Use the Makefile. Do not use `make clean`, `make veryclean`, or release targets
during the integration pass unless the principal explicitly asks.

1. After every small retitle or local patch: `make fast`.
2. After every large block move: static label scan, then `make fast`.
3. After creating or moving appendices: verify all `\input{appendices/...}`
   calls occur before `\bibliography{proj}`.
4. After moving row/spin material: run missing-ref and missing-cite scans.
5. Before handoff: full `make`.

Static scans from Agent 26 should be used exactly:

```sh
perl -0777 -ne 'while(/\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){$r{$x}=1}} while(/\\label\{([^{}]+)\}/g){$l{$1}=1} END{for $x(sort keys %r){print "$x\n" unless $l{$x}}}' main.tex appendices/*.tex
```

```sh
perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){$c{$1}++} END{for $k(sort keys %c){print "$c{$k} $k\n" if $c{$k}>1}}' main.tex appendices/*.tex
```

```sh
comm -23 \
  <(perl -0777 -ne 'while(/\\(?:cite|citep|citet|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){print "$x\n"}}' main.tex appendices/*.tex | sort -u) \
  <(perl -ne 'if(/^\s*@\w+\s*\{\s*([^,\s]+)\s*,/){print "$1\n"}' proj.bib | sort -u)
```

Final log gate:

```sh
rg -n '(^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Warning: (Reference|Citation).*undefined|There were undefined|Label .* multiply defined|Overfull \\hbox)' .build_logs/main-pass4.log out/main.log out/main.blg
```

Known layout danger zones after rewrite:

- Long tuple displays currently around `main.tex:7771`, `main.tex:11598`,
  `main.tex:6942`, `main.tex:3423`, `main.tex:4784`,
  `main.tex:10330`.
- Six-column row table around `main.tex:14374-14444`.
- Appendix array overfull in `appendices/boundary_compatibility_conditions.tex:51`.

Do not move certificate tables into the introduction as-is. Use prose lists or
short `booktabs` tables with existing packages only; do not introduce `tabularx`
or `adjustbox` without a deliberate preamble patch.

## Risk Register

1. **Biggest mathematical-order risk: scalar-first relapse.**
   If OP/DT scalar square moves before determinant, normal-ordering, and
   denominator target, the paper again reads as analytic square-rooting of
   \(\Delta_5^2\). Keep scalar late.

2. **Biggest source/target risk: target envelope impersonates compact source.**
   `\mathsf{Den}_{\Delta_5,E}` is a target current envelope. It must not be
   presented as a compact \(K3\times E\) Hall/factorization source.

3. **Biggest charge risk: \(\Gamma_{gram}\) becomes Hall grading again.**
   Every compact Hall statement must grade upstairs and only then apply
   normal-ordered pushforward. Raw fixed-lift \(\Pi_X\)-descent fails for the
   type-II real-root strings.

4. **Biggest orientation risk: OP minus sign contaminates \(\epsilon_o\).**
   The OP minus sign is a scalar convention. \(\nu_{\Delta_5}\) is an
   automorphic multiplier. \(\epsilon_o\) is Hall orientation monodromy after
   O1/O1+/O2. These are different kinds of signs.

5. **Biggest claim-strength risk: certificates become constructions by title.**
   Section and theorem names must not say "construction" where the body lists
   required data. Use "source interface", "certificate", "obstruction", or
   "open problem" unless the object is defined.

6. **Biggest opening risk: caveat ledger before theorem spine.**
   The opening must show the theorem program first, then status. Too many
   residual lists on page one hide the actual contribution.

7. **Biggest normal-ordering risk: ordinary cohomology overclaim.**
   \(B=-\delta\Pi_X\) once quadratic cochains are allowed. The obstruction is
   not a nonzero ordinary symmetric \(H^2\) class; it is the absence of an
   additive linear trivialization compatible with raw physical grading and
   bracket channels.

8. **Biggest row risk: independent extension data dilute N=1 theorem.**
   Rows are useful as a quarantine ledger. They are not dependency closure for
   the Igusa row unless a specific theorem uses them.

9. **Biggest build risk: label aliases and semantic renames.**
   Current multiple labels on one theorem compile. Removing aliases before
   updating refs will break the build. Move first, rename labels last.

10. **Biggest layout risk: construction-first notation widens already-bad displays.**
    New \(D^{alg}\), \(H^{pre}\), \(H^{tw}\), and long obstruction tuples must
    be broken into aligned displays or prose. The current build already has
    severe overfull boxes.

11. **Biggest bibliography risk: internal attack reports leak into public paper.**
    The attack PDF and swarm reports are integration evidence, not mathematical
    sources. Public claims need `proj.bib` primary sources or no citation.

12. **Stop condition for the rewrite pass.**
    Stop after the paper has the target section order, clean labels/cites, and
    a successful full `make`. Do not attempt to solve \(H^{pre}\), \(H^{tw}\),
    full orientation, row physical hosts, or spin \(L\)-factor verification in
    the same pass.
