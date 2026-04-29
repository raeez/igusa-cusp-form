# Agent62 Build-Risk Latest Report

Role: proposal-only build-risk reviewer.  Scope: current `main.tex` diff
only, after target-reference and degree patches.  I did not edit source and
did not run a LaTeX build.  Static-only report.

## Claim Attacked

The current `main.tex` patch should still be LaTeX-buildable after:

- adding the finite algebraic Dirac--Igusa target reference tower;
- replacing the D6--D2--D0 dictionary lemma by a theorem;
- separating geometric elliptic degree \(b_R^{\mathrm{geom}}\) from the
  Borcherds/Gram trace exponent \(m_R\);
- changing the monic Borcherds product from
  `\Gamma_{\mathrm{eff}}^+` to `\Gamma_{\mathrm{eff}}`.

## Static Verdict

Likely build status: no obvious fatal LaTeX syntax error in the patched
regions.  Static scans found no missing labels, no duplicate labels, no
missing BibTeX keys, and no whitespace errors in `main.tex`.

Residual build risk is layout-heavy rather than macro-heavy: the new and
modified target-reference displays sit near already-overfull zones, and
the degree patch left several old `b_R` occurrences that compile but can
make the text inconsistent.

## Attacks

### A62-01: Undefined macro risk in target-reference notation

Status: no fatal current hit found.

Evidence:

- New added control words are standard or already defined:
  `\mathsf`, `\operatorname`, `\overline`, `\widehat`, `\Pi`,
  `\Gamma`, `\Delta`, and `\sdim`.
- `\sdim` is defined in `main.tex:38`.
- The new target tower uses `\operatorname{sPf}^{\mathrm{alg}}_R`, not an
  undefined shorthand `\sPf`.
- The new realization functor uses `\mathsf{Real}_{X,R}`, not `\Real`;
  `\Real` is defined anyway at `main.tex:15`.

Likely fixes if a later patch changes notation:

- Do not introduce `\sPf`, `\DI`, `\Dalg`, `\Hpre`, or `\Htw` without
  defining them.
- Do not use `\H^{...}` for a Hilbert/source object: plain TeX `\H` is an
  accent, not a local macro.
- Safe macro additions, if repetition warrants them:
  ```tex
  \newcommand{\Dalg}{D^{\mathrm{alg}}}
  \newcommand{\Hpre}{H^{\mathrm{pre}}}
  \newcommand{\Htw}{H^{\mathrm{tw}}}
  ```

### A62-02: Label/ref risk around theorem promotion

Status: no missing-reference hit in active TeX.

Evidence:

- The D6--D2--D0 statement is now
  `\begin{theorem}` with label
  `thm:d6-d2-d0-mukai-gram-dictionary` at `main.tex:2703`.
- The old label `lem:mukai-vector-ideal-sheaf-sxe` is not referenced by
  active `main.tex` or appendix scans.
- Static label scan returned empty for missing targets and duplicate labels.

Likely fix if external notes or old aux consumers matter:

- Add a compatibility alias label immediately after the new theorem label:
  ```tex
  \label{thm:d6-d2-d0-mukai-gram-dictionary}
  \label{lem:mukai-vector-ideal-sheaf-sxe}
  ```
  This is not needed for current active TeX, only for backward anchor
  stability.

### A62-03: Theorem/proof placement risk in D6--D2--D0 block

Status: current placement looks syntactically safe.

Evidence:

- The theorem closes at `main.tex:2740`.
- The proof opens at `main.tex:2742` and closes at `main.tex:2796`.
- The following explanatory paragraph begins outside the proof at
  `main.tex:2798`.
- The next proposition opens at `main.tex:2807`.

No immediate fix needed.

### A62-04: Target-reference tower environment placement

Status: current placement looks syntactically safe.

Evidence:

- The previous proof closes at `main.tex:5887`.
- New definition opens at `main.tex:5889` and closes at `main.tex:5965`.
- New proposition opens at `main.tex:5967`, proof closes at
  `main.tex:5999`.
- New open problem opens at `main.tex:6001` and closes at `main.tex:6019`.
- The next definition starts at `main.tex:6021`.

No immediate fix needed.

### A62-05: Stale degree notation that compiles but may mislead

Status: valid notation-consistency risk; not a LaTeX fatal.

Evidence:

- `main.tex:6794`--`6795`: still says the source object has `b_R=0` and
  `b_R>0` parts.  After the patch this should probably be
  `b_R^{\mathrm{geom}}=0` and `b_R^{\mathrm{geom}}>0`.
- `main.tex:7384`: the tuple still names `b_R` as a datum, while the
  defining map immediately below is `b_R^{\mathrm{geom}}` at
  `main.tex:7413`.
- `main.tex:8082`: transition compatibility still states
  `b_R(\gamma)=b_{R'}(\gamma')`; likely should be
  `b_R^{\mathrm{geom}}(\gamma)=b_{R'}^{\mathrm{geom}}(\gamma')` if it is
  about geometric support degree.
- `main.tex:11262`: "A projection-finite source has `b_R=0`" should likely
  become `b_R^{\mathrm{geom}}=0`.
- `main.tex:12122`--`12123`: says homogeneous `s`-degree is elliptic
  degree `b_R`; after the degree patch this should likely be
  `m_R`, with `b_R^{\mathrm{geom}}` reserved for source support degree.

Likely fixes:

- Replace old support-degree prose with `b_R^{\mathrm{geom}}`.
- Replace old `s`-trace-degree prose with `m_R`.
- Keep both names when both concepts are intended:
  "geometric support degree \(b_R^{\mathrm{geom}}\) and trace exponent
  \(m_R=\operatorname{pr}_3\overline\Pi_X\)".

### A62-06: Table-width and overfull risk in early claim-status tables

Status: valid layout risk.

Evidence:

- The first patched table is at `main.tex:377`--`422`, with columns
  `p{0.22\textwidth}p{0.22\textwidth}p{0.46\textwidth}`.
- The second nearby table is at `main.tex:433`--`475`, with columns
  `p{0.20\textwidth}p{0.18\textwidth}p{0.52\textwidth}`.
- Prior build logs already recorded overfull boxes in this zone:
  `.build_logs/main-pass4.log` has overfulls at old lines 406, 413, and
  433.  Current line numbers shifted, so the next build must re-check.

Likely fixes if overfull persists:

- Reduce long inline math in table cells; move formulas to prose before or
  after the table.
- Replace `tabular` with a compact prose list if the table is not essential.
- If keeping the table, prefer `\raggedright\arraybackslash` p-columns only
  if the template supports the needed column declarations; do not add
  `tabularx` without loading the package.

### A62-07: New target-reference displays may introduce overfull boxes

Status: plausible layout risk; no fatal syntax issue seen.

Evidence:

- The target tower has long displays at `main.tex:5891`--`5960`,
  especially the tuple at `main.tex:5951`--`5959`.
- The realization functor display at `main.tex:6003`--`6010` is moderate,
  but the following prose list at `main.tex:6011`--`6016` is long.
- Prior logs show already severe overfulls elsewhere in this manuscript,
  including `.build_logs/main-pass4.log` line reports at old lines 6042,
  7771, and 11598.

Likely fixes if the build log reports new overfulls near this zone:

- Break the target tuple into an `aligned` display with one component per
  line.
- Move the long preservation list in the open problem into an `enumerate`.
- Avoid adding the target notation into existing very long tuple displays.

### A62-08: Math syntax risk in normal-ordering patch

Status: likely syntactically safe; semantic notation should be reviewed.

Evidence:

- New display `d_{\mathrm{Hoch}}(-\Pi_X)=B` at `main.tex:4873`--`4876`
  is syntactically valid.
- New display
  `\widehat\Theta_{\Pi,R}(c,T)=\mathsf T_{T-\Pi_X(c)}` at
  `main.tex:9463`--`9467` and again at `main.tex:10777`--`10782` is
  syntactically valid.
- `\mathsf T` is a math alphabet use, not a macro; it should compile.

Likely fix only if the author wants operator consistency:

- Consider `\mathsf{T}_{...}` rather than `\mathsf T_{...}` for clarity;
  both forms should compile.

### A62-09: Product-domain patch from `\Gamma_{\mathrm{eff}}^+` to `\Gamma_{\mathrm{eff}}`

Status: no build risk found.

Evidence:

- Current product display at `main.tex:1993`--`1998` compiles
  syntactically.
- Active manuscript already uses products over `\Gamma_{\mathrm{eff}}`
  in many places, including `main.tex:75`, `main.tex:843`--`848`,
  `main.tex:4460`, and `main.tex:13868`.

No immediate fix needed from a build perspective.

## Commands Already Run

```sh
git diff -- main.tex
git diff --check -- main.tex
perl -0777 -ne 'while(/\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){$r{$x}=1}} while(/\\label\{([^{}]+)\}/g){$l{$1}=1} END{for $x(sort keys %r){print "$x\n" unless $l{$x}}}' main.tex appendices/*.tex
perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){$c{$1}++} END{for $k(sort keys %c){print "$c{$k} $k\n" if $c{$k}>1}}' main.tex appendices/*.tex
comm -23 <(perl -0777 -ne 'while(/\\(?:cite|citep|citet|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){print "$x\n"}}' main.tex appendices/*.tex | sort -u) <(perl -ne 'if(/^\s*@\w+\s*\{\s*([^,\s]+)\s*,/){print "$1\n"}' proj.bib | sort -u)
perl -ne 'while(/\\(begin|end)\{([^{}]+)\}/g){print "$.:$1:$2\n"}' main.tex | rg -n "theorem|lemma|proposition|definition|remark|openproblem|proof"
git diff --unified=0 -- main.tex | perl -ne 'next unless /^\+/ && !/^\+\+\+/; while(/\\([A-Za-z@]+)/g){print "\\$1\n"}' | sort | uniq -c | sort -nr
rg -n -F 'b_R' main.tex
rg -n -F 'm_R' main.tex
rg -n -F 'target reference' main.tex
rg -n -F 'target-reference' main.tex
rg -n -F '\mathsf{Real}_{X,R}' main.tex
rg -n -F 'sPf' main.tex
rg -n -F 'Overfull \hbox' out/main.log .build_logs/main-pass4.log
```

Observed results:

- `git diff --check -- main.tex`: clean.
- Missing-reference scan: empty.
- Duplicate-label scan: empty.
- Missing-citation scan: empty.
- Environment listing shows patched theorem/proof and target-reference
  environments close in the expected order.

## Exact Verification Commands Still Needed

Run these after any source fix, or directly if the main thread wants build
confirmation of the current patch:

```sh
make
```

Then gate the logs:

```sh
rg -n '(^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Warning: (Reference|Citation).*undefined|There were undefined|Label .* multiply defined|Overfull \\hbox)' .build_logs/main-pass4.log out/main.log out/main.blg
```

If a faster smoke test is desired before the full BibTeX cycle:

```sh
pdflatex -interaction=nonstopmode -file-line-error -synctex=0 -output-directory=out main.tex
```

Static rechecks:

```sh
git diff --check -- main.tex
perl -0777 -ne 'while(/\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){$r{$x}=1}} while(/\\label\{([^{}]+)\}/g){$l{$1}=1} END{for $x(sort keys %r){print "$x\n" unless $l{$x}}}' main.tex appendices/*.tex
perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){$c{$1}++} END{for $k(sort keys %c){print "$c{$k} $k\n" if $c{$k}>1}}' main.tex appendices/*.tex
comm -23 <(perl -0777 -ne 'while(/\\(?:cite|citep|citet|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){print "$x\n"}}' main.tex appendices/*.tex | sort -u) <(perl -ne 'if(/^\s*@\w+\s*\{\s*([^,\s]+)\s*,/){print "$1\n"}' proj.bib | sort -u)
```

Degree-patch consistency gate:

```sh
rg -n -F 'b_R' main.tex
rg -n -F 's^{b_R' main.tex
rg -n -F 'elliptic degree \\(b_R\\)' main.tex
```

Expected after cleanup:

- old `b_R` survives only where it is deliberately the name of a tuple
  component or in legacy text explicitly defining the new convention;
- trace-degree statements use \(m_R\);
- geometric support-degree statements use \(b_R^{\mathrm{geom}}\).

## Remaining Open Questions

- Whether to preserve the old D6--D2--D0 label
  `lem:mukai-vector-ideal-sheaf-sxe` as an alias is a document-anchoring
  decision, not a current build blocker.
- Whether the remaining `b_R` occurrences are intentional legacy shorthand
  or stale after the degree separation needs author/integration-thread
  adjudication.
- A current LaTeX build is still required before declaring the patch
  build-clean; this report is static only by instruction.
