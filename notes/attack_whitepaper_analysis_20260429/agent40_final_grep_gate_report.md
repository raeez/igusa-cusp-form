# Agent 40 Final Grep/Static Gate Report

Scope: final static gates for the rewrite of `main.tex`.  Sources mined:
`materials/raw/2026-04-29-attack-whitepaper-analysis.pdf` through its extracted
text at `materials/processed/2026-04-29-attack-whitepaper-analysis.txt`, live
`main.tex`, and reports from agents 19, 21, 23, 24, 26, 32, and 35.

No manuscript source, bibliography, appendix, build artifact, git index, or
existing report was edited.  This file is the only write.

Run all commands from `/Users/raeez/igusa-cusp-form`.

## Required grep gates

These gates are post-rewrite gates.  They are not a current-state pass report.
The current manuscript still contains known offenders such as
`\section{The physical question}`, `\section{The one-particle index and its determinant}`,
the `CHL boundary physics` row part title, `thm:factorization-square-root`,
and the `s^{b_R}` degree collision.  A clean rewrite must make the following
commands pass under the allowed-hit policy below.

### 1. Banned conflations and overclaim language

Zero-hit gate:

```bash
rg -n -i 'constructed compact BPS|compact BPS partition function|BPS partition function|physical Hall charge|Hall charge degree|realization theorem|compact realization theorem|recognition theorem|BPS determinant theorem|Igusa square-root theorem|canonical half|canonical BPS|canonical source|operator with a spectrum|analytic square root|orientation from scalar|Borcherds product.*constructs.*Hall|determinant.*constructs.*Hall|CHL boundary physics|physical question' main.tex appendices
```

Expected: zero hits.

Review gate:

```bash
rg -n -i 'one-particle index|one-particle object|one-particle Hilbert|one-particle K3|physical host|physical charge lattice|physical derivation|physical meaning|compact source|Hall source|BPS object|operator/algebra|first-order operator|realization|recognition|canonical|certificate' main.tex appendices
```

Allowed hits:

- `one-particle` only inside negated warning text or a historical false-identification box.  No section title may contain it.
- `physical host` should become `row-host certificate`; if retained, the same sentence must say `certificate checklist` and `not a host construction`.
- `physical charge lattice` only if the same local paragraph distinguishes formal full-Mukai data from a microscopic compactification charge lattice.
- `compact source` and `Hall source` only with `open`, `supplied`, `if constructed`, `certificate`, `not constructed`, or `target check only` in the same paragraph.
- `operator` only for an algebraic/Pfaffian protected datum, or in a sentence explicitly denying an analytic operator with a spectrum.
- `recognition` only as `recognition certificate`, `criterion`, or `comparison after supplied source data`; never as a construction theorem.
- `canonical` only when backed by a named normalization/universal property.  No `canonical half`, no `canonical source`, no branch called canonical unless the branch convention is stated.

Guarded `E_3` gate:

```bash
rg -n -i 'E_3-factorization algebra|E3-factorization algebra|holomorphic E_3-factorization algebra|bare E_3|compact E_3 source' main.tex appendices
```

Expected: zero hits unless the hit is in a sentence containing at least one of:
`open`, `supplied`, `interface`, `chosen operadic model`, `formality`,
`framing`, `not constructed`.

Required guardrail gate:

```bash
rg -n -i 'not.*Hilbert|not.*state space|not.*operator product|not.*compact.*source|not.*constructed|not.*existence theorem|orientation-forgetful|not.*orientation character|not.*additive Hall grading|Gram.*quadratic|source.*target|target.*source|signed root supermultiplicities|not.*Hall constants' main.tex
```

Expected: positive hits in the abstract/introduction and again near the compact
source section.  Absence is a failure.  Minimum required concepts:

- `\mathbb U_{n,l}` is an arbitrary `K_0` representative.
- `\mathcal V` is a virtual `K_0` determinant package, not a Hilbert-space half.
- `(n,l,m)` is a Gram/Fourier/root degree, not additive Hall charge.
- `\mathfrak g_{\Delta_5}` is imported denominator target data.
- `Z^X_{\mathrm{OP/DT}}` is a reduced scalar branch and orientation-forgetful.
- `64` is theta-leading normalization; `4096` is scalar normalization; neither is orientation.
- compact Hall/factorization/source data are not constructed.
- recognition is a certificate, not an existence theorem.

### 2. Notation collisions

Legacy physical lattice gate:

```bash
rg -n -F '\Gamma_X^{\mathrm{phys}}' main.tex appendices
```

Allowed hits: only in explicit legacy warnings or compatibility formulas that
say `\Gamma_X^{\mathrm{phys}}:=\Gamma_X^{\mathrm{form}}`, `legacy`,
`mnemonic`, or `not the full physical charge lattice`.  New prose should use
`\Gamma_X^{\mathrm{form}}` or actual support
`\Gamma_{X,\sigma}^{\mathrm{eff}}`.

Bare/colliding Gamma gate:

```bash
rg -n -P '\\Gamma_X(?!\s*\^)' main.tex appendices
```

Expected: zero hits, except a deliberate warning saying that bare `\Gamma_X`
is banned.  The corrected normal-ordered extension is `\widehat\Gamma_X`.

Gram/Fourier versus Hall support gate:

```bash
rg -n -F -e '\Gamma_{\mathrm{ind}}' -e '\Gamma_{\mathrm{eff}}' main.tex appendices
```

Allowed hits:

- `\Gamma_{\mathrm{ind}}` only as automorphic/Fourier/denominator index data.
- `\Gamma_{\mathrm{eff}}` only as cusp-positive product semigroup or target
  active support.
- No hit may grade a compact Hall category directly by either symbol.

Raw/corrected `Pi` gate:

```bash
rg -n -F -e '\Pi_X:\widehat\Gamma_X' -e '\Pi_{X,*}' -e '\Pi_*' main.tex appendices
```

Expected: zero hits.  The raw map is
`\Pi_X:\Gamma_X^{\mathrm{form}}\to\Gamma_{\mathrm{gram}}`; the corrected
additive map is `\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}`;
the chain descent is `\overline\Pi_{X,*}^{\Theta}`.

`B` collision gate:

```bash
rg -n -i 'B-cocycle|the B cocycle|Connes operator \(B\)|operator \(B\)|B for chiral|B for Connes' main.tex appendices
```

Expected: zero hits.  Use `B` for the lattice-valued Gram polarization,
`B_{\mathrm{ch}}` for the translation-valued Hochschild/chiral cocycle,
`B_{\mathrm C}` for the Connes operator, and `\bar B_E^{\mathrm{ch}}` for
the chiral bar construction.

`D` collision gate:

```bash
rg -n -F -e 'DX' -e '\Dalg' -e '\Hpre' -e '\Htw' -e '\H^{pre}' -e '\H^{tw}' -e 'FXhyb' -e 'PRPi' -e 'DXR' main.tex appendices
```

Expected: zero hits unless matching macros are explicitly defined in the
preamble and used consistently.  Default safe notation is literal
`D^{\mathrm{alg}}`, `\mathcal H_X^{\mathrm{pre}}`,
`\mathcal H_X^{\mathrm{tw}}`, and `\mathcal F_X^{\mathrm{hyb}}`.
Never use `\H` as a state-space macro.

Certificate `D_X` gate:

```bash
rg -n -F 'D_X' main.tex appendices
```

Allowed hits: only parenthesized certificate labels such as `\textup{(D_X)}`
or a clearly displayed component of `\mathfrak K_X`.  No running prose may use
`D_X` for `\mathcal D_X`, `\mathfrak D_X`, or `D_5`.

OP scalar notation gate:

```bash
rg -n -P '\\chi_\{10\}(?!\^\{\\mathrm\{OP\}\})|\\Phi_\{10\}' main.tex appendices
```

Expected: zero hits, except a source-quotation sentence immediately defining
that OP's product is written in this manuscript as `\chi_{10}^{\mathrm{OP}}`.

Denominator target typography gate:

```bash
rg -n -P '(?<!\\mathsf\{)Den_\{\\Delta_5,E\}|Denalg|Den\^\{\\mathrm\{alg\}\}' main.tex appendices
```

Expected: zero hits.  Use `\mathsf{Den}_{\Delta_5,E}` for the existing target
current envelope.  If a curve-universal target is imported, define
`\mathsf{Den}^{\mathrm{alg}}_{\Delta_5,C,L}` once before use.

Forbidden comparison-symbol equality gate:

```bash
rg -n -F -e '\Phi^{\mathrm{cmp}}_5=F_5' -e '\Phi^{\mathrm{cmp}}_7=F_7' -e '\Phi^{\mathrm{cmp}}_8=F_8' main.tex appendices
```

Allowed hits: only in explicit false-equality warnings.  Never as asserted
row identifications.

### 3. Theorem-label hygiene

Known bad semantic-label gate:

```bash
rg -n '\\label\{(thm:factorization-square-root|thm:protected-denominator-shadow|thm:eight-formal-current-rows|thm:microscopic-hall-drinfeld-criterion|prop:sectorial-hall-truncation|lem:imaginary-wall-orientation-extension|prop:no-unbuilt-denominator|conj:nonabelian-row-extension)' main.tex appendices
```

Expected: zero hits after final label cleanup.  During moves, compatibility
aliases may survive temporarily, but they must not survive the final gate.

Dangerous theorem/title gate:

```bash
rg -n -i 'Compact realization theorem|Recognition theorem|BPS determinant|Igusa square-root theorem|CHL boundary physics|factorization-square-root|microscopic-hall|protected-denominator-shadow|eight-formal-current-rows|physical host|compact source theorem|BPS object theorem|operator theorem' main.tex appendices
```

Expected: zero hits, except inside a warning list of banned names.

Environment-prefix static check:

```bash
perl -ne 'if(/\\begin\{(theorem|proposition|lemma|corollary|remark|definition|openproblem|conjecture)\}/){$env=$1} if(/\\end\{(theorem|proposition|lemma|corollary|remark|definition|openproblem|conjecture)\}/){$env=""} while(/\\label\{([^{}]+)\}/g){$l=$1; print "$ARGV:$.:$env:$l\n" if (($l=~/^thm:/ && $env ne "theorem") || ($l=~/^prop:/ && $env ne "proposition") || ($l=~/^lem:/ && $env ne "lemma") || ($l=~/^cor:/ && $env ne "corollary") || ($l=~/^rem:/ && $env ne "remark") || ($l=~/^def:/ && $env ne "definition") || ($l=~/^conj:/ && $env ne "conjecture") || ($l=~/^op:/ && $env ne "openproblem")); }}' main.tex appendices/*.tex
```

Expected: zero output.  If a label is intentionally an alias, its prefix must
match the enclosing environment or be replaced by a neutral compatibility
label.

### 4. Scalar orientation firewall

Scalar-orientation offender gate:

```bash
rg -n -i '4096.*orientation|orientation.*4096|64.*orientation|orientation.*64|-4096.*Pfaffian|OP minus.*orientation|OP scalar sign.*orientation|scalar.*orientation character|orientation.*scalar constant' main.tex appendices
```

Allowed hits: only negative firewall sentences.  The same line or paragraph
must say `not`, `no`, `orientation-forgetful`, `separate`, `scalar
convention`, `unused`, `does not`, `cannot`, or `independent`.

Hard zero scalar-to-orientation implication gate:

```bash
rg -n -i '4096.*proves.*orientation|64.*proves.*orientation|scalar.*proves.*orientation|scalar.*constructs.*orientation|OP.*sign.*is.*orientation|OP.*minus.*is.*orientation|Delta_5\^2.*orientation character|D_5\^2.*orientation character' main.tex appendices
```

Expected: zero hits.

Maass versus Hall orientation gate:

```bash
rg -n -i 'Maass.*orientation|automorphic.*orientation|nu_\\Delta|\\nu_{\\Delta_5}|epsilon_o|\\epsilon_o' main.tex appendices
```

Allowed hits: every assertion equating or comparing Maass/automorphic
character with Hall orientation must be conditional on supplied O1/O1+/O2
data, Weyl transport, quotient gerbe descent, and finite-stabilizer checks.
Automorphic target character alone is not Hall orientation.

### 5. Row and spin quarantine

Row/spin title gate:

```bash
rg -n -i '^\\part\{.*CHL|^\\section\{.*CHL|^\\section\{.*Spin|CHL boundary physics|Spin L-factor|L_\\{\\mathrm\\{spin\\}\\}|Andrianov|Saito-Kurokawa' main.tex appendices
```

Expected:

- zero hits in the active main theorem spine;
- if spin remains, the section title must say `independent arithmetic
  normalization`, or the block must be moved to a companion note;
- row material must be titled as an independent row ledger/certificate, not
  `CHL boundary physics`.

Opening quarantine gate:

```bash
perl -ne 'print "$ARGV:$.:$_" if $.<=700 && /(CHL|Spin|L_\{\\mathrm\{spin\}\}|Andrianov|Saito-Kurokawa|F_[2-8]|\\nabla_|Q_1|physical host)/i' main.tex
```

Expected: zero hits.  Rows/spin do not belong in the abstract, introduction,
first theorem spine, or first ten pages except for one sentence saying row
material is independent extension data.

Dependency closure gate:

```bash
rg -n -i 'depend(s|ency|encies).*(row|spin)|row.*depend|spin.*depend|F_[2-8].*(theorem|dependency|closure)|L_\\{\\mathrm\\{spin\\}\\}.*(theorem|dependency|closure)|Andrianov.*(theorem|dependency|closure)|Saito-Kurokawa.*(theorem|dependency|closure)' main.tex appendices
```

Allowed hits: only negative independence statements.  Rows and spin must never
appear as dependencies of the `N=1` determinant, normal-ordering, denominator,
compact-source obstruction, or OP scalar-square claims.

Required independence disclaimers:

```bash
rg -n -i 'independent.*row|row.*independent|spin.*independent|arithmetic side note|not used in the N=1|not used in the Dirac|not used in the determinant|not used in the scalar-square' main.tex appendices
```

Expected: positive hits if rows or spin remain in the active PDF.  Absence is
a failure.

### 6. Degree-shift corruption

Hard zero degree gate:

```bash
rg -n -F -e 's^{b_R}' -e 's^{\,b_R' -e 'trace degree \(s^{b_R}' -e 'elliptic degree \(m' -e 'elliptic degree is \(m' -e 'm=b_R' -e 'b_R(\eta)=1' -e 'b_R(\delta_2)=1' -e 'b_R(\\eta_2)=1' -e 'elliptic degree \(d-1\)' -e 'elliptic-degree \(d-1\)' -e 'p=P=e^{iu}' -e 't=Q' -e 'q=T' main.tex appendices
```

Expected: zero hits.

Review degree gate:

```bash
rg -n -F -e 'positive elliptic degree' -e 'positive \(s\)-direction' -e 'q_{\mathrm{DT}}^{d-1}' -e '\widetilde q_{\mathrm{OP}}^{d-1}' main.tex appendices
```

Allowed hits:

- `positive elliptic degree` only for projection-to-`E` support locality.
- positive `s`-power only as `m_R>0`, not as geometric degree.
- OP/DT exponents may contain `d-1` only in the variable dictionary saying
  geometric degree is `d` and Gram/Borcherds exponent is `m=d-1`.

Required degree-split gate:

```bash
rg -n -F -e 'M=d-1' -e 'm=d-1' -e 'm_R' -e 'b_R^{\mathrm{geom}}' main.tex
```

Expected: positive hits near the D6--D2--D0 theorem, the OP/DT variable
dictionary, and the hybrid source definitions.  Absence is a failure.

### 7. Source/target firewall

Hard zero source-from-target gate:

```bash
rg -n -i 'target.*constructs.*source|target.*defines.*source|source.*from.*target current|C_X.*from.*target|C_\{X,R\}.*from.*target|C_X.*bar B_E|C_\{X,R\}.*bar B_E|target.*bar.*cobar.*defines.*C|Den.*compact source|formal current envelope.*compact source|BKM.*compact Hall source|g_\\Delta_5.*compact Hall source|Borcherds product.*compact source|scalar square.*compact source' main.tex appendices
```

Expected: zero hits unless the sentence is an explicit negation.  If a hit is
negative, it must say `not`, `never`, `cannot`, `does not`, or `is not`.

Target-object review gate:

```bash
rg -n -F -e '\mathsf{Den}_{\Delta_5,E}' -e '\mathfrak g_{\Delta_5}' -e 'formal current envelope' -e 'target current envelope' main.tex appendices
```

Allowed hits: every paragraph containing these target objects must say or
imply target-internal status unless a supplied source-to-target comparison is
being stated.  No target object may define compact source data.

Required firewall gate:

```bash
rg -n -i 'source.*target|target.*source|target-internal|not.*compact source|does not construct.*compact source|not.*constructed.*source|source-to-target|target.*not.*source|formal current envelope.*target' main.tex appendices
```

Expected: positive hits in the introduction, compact realization section,
Koszul/bar-cobar discussion, primitive recognition discussion, and final
synthesis.

### 8. Section-title and order gate

Run:

```bash
rg -n '^\\(part|appendix|input|bibliography|bibliographystyle)\b|^\\section\{' main.tex
```

Expected order after rewrite:

1. Abstract.
2. Introduction / Dirac problem / claim strength.
3. Virtual `K_0` determinant and Borcherds product.
4. Normalized Igusa target.
5. D6--D2--D0 Mukai--Gram dictionary.
6. Normal-ordered Gram descent.
7. Denominator algebra.
8. Compact Dirac--Igusa realization problem.
9. OP/DT scalar square.
10. Coefficient dictionary and theorem-status synthesis.
11. Optional independent row ledger.
12. Appendices.
13. Bibliography last.

Forbidden titles in the section-order output: `The physical question`,
`one-particle index`, `CHL boundary physics`, `Spin L-factor` in the main
spine, `compact realization theorem`, `recognition theorem`.

## Allowed hits policy

1. A zero-hit gate is literal.  Any output is a failure unless the command's
   allowed-hit clause explicitly says otherwise.
2. Allowed hits must be local, not deferred.  A dangerous word is not saved by
   a caveat two sections later.
3. Allowed hits must be negative, conditional, or status-marked:
   `constructed`, `imported`, `computed`, `conditional`, `certificate`,
   `open`, or `not constructed`.
4. If a gate allows negative disclaimers, the disclaimer must be on the same
   line or in the same paragraph.  Do not rely on the reader remembering a
   status table.
5. Internal attack reports may appear in `notes/`, but not as public
   bibliography or manuscript citations.  The paper cites primary mathematical
   sources in `proj.bib`, not swarm reports.
6. Row and spin hits are allowed only after the `N=1` theorem spine has
   closed, and only with independence language.
7. `\Gamma_X^{\mathrm{phys}}` is allowed only as a legacy alias with its
   warning.  It is never allowed as new compact charge notation.
8. `D_X` is allowed only as a parenthesized certificate slot.  It is never
   allowed as determinant, Dirac object, or monic Borcherds product.
9. `m=d-1` is required in the D6 and OP/DT dictionary.  `m=d` is banned.
10. Any exception must be recorded in a residual manual-review ledger with
    source line, reason, and the exact theorem/source context.

## Static label/cite checks

Run these after the rewrite and after every large block move.

Missing reference target scan:

```bash
perl -0777 -ne 'while(/\\(?:ref|eqref|pageref|autoref|cref|Cref)\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){$r{$x}=1}} while(/\\label\{([^{}]+)\}/g){$l{$1}=1} END{for $x(sort keys %r){print "$x\n" unless $l{$x}}}' main.tex appendices/*.tex
```

Expected: zero output.

Duplicate label scan:

```bash
perl -0777 -ne 'while(/\\label\{([^{}]+)\}/g){$c{$1}++} END{for $k(sort keys %c){print "$c{$k} $k\n" if $c{$k}>1}}' main.tex appendices/*.tex
```

Expected: zero output, unless deliberate compatibility aliases are still
temporarily retained during moves.  Final gate: zero duplicate labels.

Missing cite scan:

```bash
comm -23 \
  <(perl -0777 -ne 'while(/\\(?:cite|citep|citet|nocite)(?:\[[^\]]*\])*\{([^{}]+)\}/g){for $x(split /\s*,\s*/,$1){print "$x\n"}}' main.tex appendices/*.tex | sort -u) \
  <(perl -ne 'if(/^\s*@\w+\s*\{\s*([^,\s]+)\s*,/){print "$1\n"}' proj.bib | sort -u)
```

Expected: zero output.

Environment-prefix scan:

```bash
perl -ne 'if(/\\begin\{(theorem|proposition|lemma|corollary|remark|definition|openproblem|conjecture)\}/){$env=$1} if(/\\end\{(theorem|proposition|lemma|corollary|remark|definition|openproblem|conjecture)\}/){$env=""} while(/\\label\{([^{}]+)\}/g){$l=$1; print "$ARGV:$.:$env:$l\n" if (($l=~/^thm:/ && $env ne "theorem") || ($l=~/^prop:/ && $env ne "proposition") || ($l=~/^lem:/ && $env ne "lemma") || ($l=~/^cor:/ && $env ne "corollary") || ($l=~/^rem:/ && $env ne "remark") || ($l=~/^def:/ && $env ne "definition") || ($l=~/^conj:/ && $env ne "conjecture") || ($l=~/^op:/ && $env ne "openproblem")); }}' main.tex appendices/*.tex
```

Expected: zero output.

Undefined macro preflight for proposed notation:

```bash
rg -n -F -e '\Dalg' -e '\Hpre' -e '\Htw' -e '\D' -e '\H' main.tex appendices
```

Expected: zero output unless the preamble defines those macros deliberately.
Never define or use `\H` as a Hilbert/state-space macro; TeX already uses it
as an accent.

Appendix input order check:

```bash
rg -n '^\\appendix|^\\input\{appendices/|^\\bibliographystyle|^\\bibliography' main.tex
```

Expected: every appendix `\input{appendices/...}` appears after `\appendix`
and before `\bibliography{proj}`.  Bibliography remains last.

## Build/log gates

Use the Makefile.  Do not use `make clean`, `make veryclean`, `release`, or
destructive git commands during integration.

Small checkpoint after local edits:

```bash
make fast
```

Final build:

```bash
make
```

Fatal/log correctness gate:

```bash
rg -n '(^! |Emergency stop|Fatal error|Undefined control sequence|Runaway argument|File ended while scanning|No pages of output|LaTeX Warning: (Reference|Citation).*undefined|There were undefined|Label .* multiply defined|Warning--|I couldn.t open database file|Citation .* undefined)' .build_logs/main-pass4.log out/main.log out/main.blg
```

Expected: zero hits.

Overfull audit gate:

```bash
rg -n 'Overfull \\hbox' .build_logs/main-pass4.log out/main.log
```

Expected: no new overfulls introduced by the rewrite.  Current Apr 29 logs
already show severe overfulls, including approximately 580pt at old line 7771,
201pt at old line 11598, 124pt at old line 6942, 104pt at old line 3423,
95pt at old line 4784, and 82pt in the boundary appendix.  The rewrite must
not hide behind that baseline: every surviving overfull must be listed with
source line, width, and reason.

Severe overfull release-blocker gate:

```bash
rg -n 'Overfull \\hbox \(([5-9][0-9]|[1-9][0-9]{2,})\.[0-9]+pt too wide\)' .build_logs/main-pass4.log out/main.log
```

Expected: zero hits for publication-grade handoff.  If any hit remains, the
handoff must name it explicitly as residual layout debt; hits over 100pt are
release blockers.

BibTeX gate:

```bash
rg -n 'Warning--|I couldn.t open database file|I found no|Database file|Repeated entry|missing' .build_logs/main-bibtex.log out/main.blg
```

Expected: zero missing-entry or repeated-entry warnings.  `out/main.blg`
should report all cited keys resolved.

Output existence gate:

```bash
test -s out/main.pdf
```

Expected: exit code 0 after `make`.

## Visual inspection gates

These are mandatory because grep cannot see theorem flow or layout.

1. First ten pages:
   - Must expose determinant, normalized target, D6/Mukai--Gram dictionary,
     normal-ordered Gram descent, denominator target, OP scalar square as a
     late scalar check, and compact realization as open.
   - Must not begin with row atlas, spin `L`-factor, residual certificate
     ledgers, or physical mission language.
   - Every sentence containing `physical`, `BPS`, `operator`, `one-particle`,
     `compact`, `E_3`, `Hall source`, `orientation`, `canonical`, or
     `recognition` must be classifiable in isolation as constructed,
     imported, computed, conditional, certificate, or open.

2. Table of contents:
   - Must show the theorem spine before appendices.
   - Rows, if retained, appear only after the main synthesis and under
     independent ledger language.
   - Spin, if retained, appears only as an independent arithmetic appendix,
     not before proof appendices and not in the main dependency chain.

3. Scalar square section:
   - Must visibly say OP/DT proves the scalar square, not the first-order
     square root.
   - Must visibly separate `64`, `4096`, and the OP minus sign from Hall
     orientation monodromy.

4. Normal-ordering section:
   - Must define raw placement `i_0(c)=(c,0)`, split section
     `s(c)=(c,\Pi_X(c))`, and corrected additive map `\overline\Pi_X`.
   - Must not claim a nonzero ordinary `H^2_{\mathrm{sym}}` class if the real
     obstruction is absence of compatible linear homogeneous trivialization.
   - Must show the flag formula before the raw fixed-lift no-go theorem.

5. D6--D2--D0 dictionary:
   - Must state the K3 Mukai pairing before the Gram triple.
   - Must use `n_0` for Euler/D0 count when the first Gram coordinate `N` is
     also present.
   - Must state `M=d-1`, not `m=d`, and split geometric degree from trace
     exponent in hybrid sections.

6. Source/target sections:
   - `\mathsf{Den}_{\Delta_5,E}` and `\mathfrak g_{\Delta_5}` must read as
     target-internal.
   - `C_X`, `C_{X,R}`, source coalgebra, primitive source, and Dirac object
     must not be defined from a target bar/cobar counit.

7. Dense displays and tables:
   - Inspect any page corresponding to overfull log hits.
   - Pay special attention to old tuple-display zones near old lines 7771,
     11598, 6942, 3423, 4784, 10330, and the boundary appendix array.
   - Do not move current dense row/status tables into the introduction as-is.

## Patch queue

P0. Rename the visible overclaim titles:

- `The physical question` -> `The compact source problem` or
  `Protected-source problem`.
- `The one-particle index and its determinant` -> `The virtual K_0 determinant
  and its Borcherds product`.
- `Diagonal-divisor rows and CHL boundary physics` -> `Independent
  diagonal-divisor denominator row ledger`, or move rows to a companion note.

P0. Add an opening notation/status firewall:

- `\mathcal D_X` virtual determinant.
- `D_5=64^{-1}\Delta_5` monic Borcherds product.
- `\Delta_5` theta-normalized target.
- `\chi_{10}^{\mathrm{OP}}=D_5^2` scalar OP product.
- `\Gamma_X^{\mathrm{form}}`, actual Hall support
  `\Gamma_{X,\sigma}^{\mathrm{eff}}`, `\Gamma_{\mathrm{gram}}`,
  `\Gamma_{\mathrm{ind}}`.
- raw `\Pi_X`, corrected `\widehat\Gamma_X`, `\overline\Pi_X`,
  chain descent `\overline\Pi_{X,*}^{\Theta}`.
- `B`, `B_{\mathrm{ch}}`, `B_{\mathrm C}`.
- `\mathfrak D_X` as open first-order algebraic/Pfaffian datum, not analytic
  operator.

P0. Promote the D6--D2--D0 dictionary to theorem-level and repair its
variables:

- define `\widetilde H(S,\mathbb Z)` and the Mukai pairing first;
- use `n_0` for `\chi(\mathcal O_Y)`;
- write `N=h-1`, `L=n_0`, `M=d-1`;
- state that geometric elliptic degree is `d`, while Borcherds/Gram exponent
  is `M=d-1`.

P0. Split hybrid degree notation:

- `b_R^{\mathrm{geom}}` for projection-to-`E` support degree;
- `m_R=\operatorname{pr}_3\overline\Pi_X` for the `s`-exponent;
- replace `s^{b_R}` with `s^{m_R}`;
- repair every `\delta_2` requirement to ask for `m_R=1` plus wrapped support,
  not unqualified `b_R=1`.

P0. Repair scalar/orientation wording:

- add a boxed sentence near OP/DT scalar square: OP/DT proves `D_5^2`, not
  `D_5`; scalar constants are not orientation data.
- ensure `64`, `4096`, and the OP minus sign never feed Hall orientation.

P0. Normalize theorem labels:

- remove or rename `thm:factorization-square-root`,
  `thm:protected-denominator-shadow`, `thm:eight-formal-current-rows`,
  `thm:microscopic-hall-drinfeld-criterion`,
  `prop:sectorial-hall-truncation`,
  `lem:imaginary-wall-orientation-extension`,
  `prop:no-unbuilt-denominator`,
  `conj:nonabelian-row-extension`.

P0. Source/target firewall:

- do not define `C_X` or `C_{X,R}` from
  `\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E})`;
- name `\mathsf{Den}_{\Delta_5,E}` as target-internal;
- primitive recognition must depend on supplied source coalgebra, source
  representatives, parity split, radical/PBW data, and source-to-target
  comparison.

P1. Reorder sections into the theorem spine described in the section-order
gate.  Move orientation obstruction algebra and compact-source residual
ledgers into appendices after a short main source-problem section exists.

P1. Quarantine rows and spin:

- move spin `L`-factor to a companion note unless a main theorem genuinely
  cites it;
- if retained, begin with the independence disclaimer;
- keep one row ledger only, not duplicate main and appendix atlases at full
  length.

P1. Move detailed Maass/reflection computations and Bott/sign convention
remarks to an appendix.  Main text keeps only the automorphic target character
values and the warning that they do not construct Hall orientation.

P2. Add macros only after notation stabilizes.  Safe macro candidates:
`\Gform`, `\Ggram`, `\GhatX`, `\PiRaw`, `\PiNO`, `\Dvirt`, `\DenE`,
`\Fhyb`, `\bgeomR`, `\mgramR`.  Do not add `\H`.

## Residual manual review

1. Primary-source anchoring:
   - Verify theorem/equation anchors for Borcherds, Gritsenko--Nikulin,
     Clery--Gritsenko, Oberdieck--Pixton, Oberdieck--Pandharipande,
     Govindarajan, Cheng--Dabholkar, and Andrianov/Saito--Kurokawa if spin
     remains.
   - Attack reports are evidence to check, not public mathematical sources.

2. Theorem-status review:
   - Every theorem title must be one of: constructed theorem, imported
     theorem, internal computation, or conditional theorem.
   - Every certificate must state supplied/open/nonempty status.
   - Every open compact construction must be an open problem, not a hidden
     theorem hypothesis.

3. First-ten-pages cold-reader review:
   - Print/read only pages 1--10.
   - Mark every claim as constructed, imported, computed, conditional,
     certificate, or open.
   - Any sentence that resists classification must be rewritten.

4. Scalar contamination review:
   - No path from `Z^X_{\mathrm{OP}}=-4096\Delta_5^{-2}` to Pfaffian,
     orientation, or compact source without explicit supplied first-order data.

5. Gram-charge review:
   - No Hall category is graded directly by `(n,l,m)`.
   - Additive compact/source support is upstairs; Gram/Fourier degree appears
     only after normal-ordered descent.

6. Row boundary review:
   - Every row promotion beyond automorphic product must name row, group/cover,
     character, seed, product lattice, scalar theorem if claimed, orientation
     data, charge lattice, and primitive comparison.
   - If any of that is missing, the row remains an independent ledger or
     companion note.

7. Visual layout review:
   - Inspect all pages with overfull boxes after `make`.
   - Treat any overfull over 100pt as a release blocker.

8. Stop condition:
   - Stop after the rewritten paper has the target section order, passes the
     zero-hit/static gates, has clean labels/cites, and builds with `make`.
   - Do not attempt in the same pass to solve the full compact source,
     `H^{\mathrm{pre}}`, `H^{\mathrm{tw}}`, global orientation, row physical
     hosts, or spin `L`-factor verification.
