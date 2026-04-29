# Agent58 degree audit latest report

CONTROL: proposal-only `b_R` / `m_R` degree-audit reviewer.  No source
edits.  Writable surface limited to this report.

Audited inputs:

- `main.tex`, observed during live concurrent edits; stable audit hash at
  one full grep pass: `sha256 0b6b7abbe20c6cafde4839ed812ac01d0928ac9136ecbc6065c7b35dcffbd900`.
- latest extracted PDF text:
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`,
  `sha256 c2035d6ce0f995ad41b16ad295d2bba1d110612385aea3a7d6197f8d1f7e5b17`.
- Agent53 report:
  `notes/attack_whitepaper_analysis_20260429/agent53_hybrid_wrapped_source_latest_report.md`,
  `sha256 e78b110f4716aa4d29f316d12564a49064cf8e4621a32158272b8da68fe71d44`.

Line numbers in `main.tex` moved during the audit because the worktree was
being edited concurrently.  The grep evidence below records the current
anchors from the cited pass; the replacement rules are semantic and should be
applied by symbol search, not by blind line-number patching.

## Verdict

Agent53 is right on the degree issue.

The manuscript must keep three notions separated:

1. \(m_R=\operatorname{pr}_3\overline\Pi_X\): the Gram / Borcherds trace
   exponent.  This is the exponent of \(s\) in protected integration and in
   the automorphic monomial.
2. \(b_R^{\mathrm{geom}}\): the geometric elliptic curve-class degree.  This
   decides projection-finite versus wrapped support.
3. The displayed shadow parameter \(b\) in
   \(\operatorname{Ran}^{\mathrm{hyb}}(E)=\bigsqcup_{b\ge0}\operatorname{Ran}(E)_{[b]}\):
   a degree shadow of the hybrid base, not the whole source category.

For \(\delta_2\), the safe statement is:

\[
\delta_2\leftrightarrow(0,1,1),\qquad m_R(\delta_2)=1,\qquad
b_R^{\mathrm{geom}}(\delta_2)>0.
\]

On the rank-one D6--D2--D0 branch the statement should be stronger:

\[
m_R=d-1,\qquad b_R^{\mathrm{geom}}=d=m_R+1,
\]

so the \(\delta_2\) lift with \(m_R=1\) has
\[
b_R^{\mathrm{geom}}(\delta_2)=d=2.
\]

Do not write \(b_R(\delta_2)=1\) unless \(b_R\) has first been explicitly
renamed as a trace exponent.  In the current manuscript \(b_R\) is repeatedly
introduced as elliptic/geometric degree, so \(b_R(\delta_2)=1\) is unsafe and
is false on the rank-one D6--D2--D0 dictionary.

## Evidence

### Dictionary and latest PDF

- `main.tex` proves the D6--D2--D0 dictionary:
  `\Pi_X(Q_Y,P_Y)=(h-1,n,d-1)` at current grep anchors around
  `main.tex:2702-2737`, with the proof repeating \(P_Y^2/2=d-1\) around
  `main.tex:2791-2798`.
- The OP/DT table also states:
  `Borcherds/Gram exponent \(m=d-1\) from elliptic degree \(d\)` at
  `main.tex:13986`.
- Latest PDF extracted text says the same in its repair proposal:
  `mBorch(\gamma)=m`, `bell(\gamma)=m+1` at
  `materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt:29083-29096`,
  and `m = d - 1, bell = d = m + 1` at extracted line `30083`.
- Agent53 records the same conclusion at report lines `73-93` and recommends
  replacing `b_R(\delta_2)=1` by `m_R(\delta_2)=1` plus
  `b_R^{\mathrm{geom}}(\delta_2)>0`, with `=2` on the rank-one branch.

### Current `main.tex` conflations

Current grep for `b_R` found these load-bearing instances:

```text
1642:\qquad b_R(\eta)=1,\qquad \overline\Pi_X(\eta)=(0,1,1),
6290:one has \(b_R(\delta_1)=b_R(\delta_3)=0\) and
6291:\(b_R(\delta_2)=1\).  Thus the \(\delta_2\) primitive cannot live in the
6659:Its \(b_R=0\) part comes from the \(K3\)-specialized
6660:\(E_3\)-source; its \(b_R>0\) part is present only through the rigidified
7249:b_R,\,
7278:b_R:\Gamma_{\sigma,S}^{HN}(R)\longrightarrow \Z_{\ge0}
7281:\(\Gamma_R^{\mathrm{loc}}=\{\alpha\mid b_R(\alpha)=0\}\) and
7282:\(\Gamma_R^{\mathrm{wr}}=\{\eta\mid b_R(\eta)>0\}\).
7285:\(b_R\) is additive on extensions that remain in the quotient:
7287:b_R(0)=0,\qquad
7288:b_R(\gamma+\gamma')=b_R(\gamma)+b_R(\gamma')
7547:\(b_R(\eta_1+\eta_2)\).
7804:\(I_R^{\mathrm{prot}}(Q_{E,R}x)\) has \(s\)-degree \(b_R(\gamma)\):
7815:\(b_R^{\mathrm{geom}}(\gamma)\) records geometric elliptic support degree.
7825:For products, the displayed character law and additivity of \(b_R\) give
7827:s^{b_R(\gamma_1+\cdots+\gamma_k)}
7829:\prod_i s^{b_R(\gamma_i)}
7853:The coefficient of a monomial \(q^nr^ls^{b_R(\gamma)}\) is a protected
7944:b_R(\gamma)=b_{R'}(\gamma').
8134:s^{b_R(\gamma)}\C[q^{\pm1},r^{\pm1}],
8138:because \(b_R\) is additive inside the finite quotient.
8314:\overline\Pi_X(x_{\delta_2,R})=(0,1,1),\qquad b_R(\eta)=1,
11097:b_R(\eta_2)=1,\qquad \overline\Pi_X(\eta_2)=(0,1,1),
11121:the same datum.  A projection-finite source has \(b_R=0\), hence cannot
11982:degree \(b_R\).  Equivalently,
14292:\(b_R^{\mathrm{geom}}\), a Gram trace exponent
```

Current grep for `m_R` shows the intended repair is already partly present:

```text
267:\(m_R=\operatorname{pr}_3\overline\Pi_X\), rigidified wrapped prequotients
272:trace degree \(s^{m_R}\).
7808:s^{\,m_R(\gamma)}\C[q^{\pm1},r^{\pm1}]
7814:the Gram trace exponent \(m_R(\gamma)=m\), while
8185:the trace degree \(s^{m_R}\), does not define the hybrid source.
14293:\(m_R=\operatorname{pr}_3\overline\Pi_X\), rigidified wrapped prequotients, mixed
14300:\(s^{m_R}\).  Equivalently,
```

Thus the latest state is internally inconsistent: the abstract/summary and one
display use \(m_R\), while the certificate definition and several operative
conditions still use \(b_R\) as the \(s\)-exponent.

## Safe replacements

Apply these by search in the current file.

| Current language | Problem | Safe replacement |
|---|---|---|
| `the positive \(s\)-direction ... records elliptic degree` and `protected integration whose \(s\)-degree is the elliptic degree` | Collapses \(m_R\) and \(b_R^{\mathrm{geom}}\). | `the positive \(s\)-direction records the Gram trace exponent \(m_R\), which on the rank-one D6--D2--D0 branch is \(d-1\); the geometric elliptic degree \(b_R^{\mathrm{geom}}\) controls wrapped support.` |
| `b_R` as an entry of the hybrid certificate datum | Ambiguous after later use of \(m_R\). | Replace the datum entry by `b_R^{\mathrm{geom}},\,m_R` or define \(m_R=\operatorname{pr}_3\overline\Pi_X\) immediately after the datum. |
| `b_R:\Gamma_{\sigma,S}^{HN}(R)\to\mathbb Z_{\ge0}` is the elliptic-degree component | Correct only if never used as \(s\)-exponent. | `b_R^{\mathrm{geom}}:\Gamma_{\sigma,S}^{HN}(R)\to\mathbb Z_{\ge0}` is the geometric elliptic-degree component; `m_R=\operatorname{pr}_3\overline\Pi_X` is the Gram trace exponent. |
| `\Gamma_R^{loc}=\{\alpha\mid b_R(\alpha)=0\}`, `\Gamma_R^{wr}=\{\eta\mid b_R(\eta)>0\}` | This is a geometric support split. | Use `b_R^{\mathrm{geom}}` in both sets. |
| `b_R` additive on extensions | If this refers to wrapped degree, keep geometric name; if it supports monomial multiplication, it must be \(m_R\). | State two laws separately: `b_R^{\mathrm{geom}}` is additive for curve-class degree in the finite quotient; `m_R` is additive after the normal-ordered Gram descent and is used for \(s\)-powers. |
| `b_R(\delta_2)=1`, `b_R(\eta)=1`, `b_R(\eta_2)=1` with \((0,1,1)\) | Wrong if \(b_R\) is geometric elliptic degree. | `m_R(\eta)=1,\ \overline\Pi_X(\eta)=(0,1,1),\ b_R^{\mathrm{geom}}(\eta)>0`; add `b_R^{\mathrm{geom}}(\eta)=2` when explicitly in the rank-one D6--D2--D0 branch. |
| `I_R^{prot}(Q_{E,R}x) has \(s\)-degree \(b_R(\gamma)\)` | Direct conflation. | `... has \(s\)-degree \(m_R(\gamma)\)`. |
| `s^{b_R(\gamma_1+\cdots+\gamma_k)}=\prod_i s^{b_R(\gamma_i)}` | Uses geometric degree as automorphic exponent. | `s^{m_R(\gamma_1+\cdots+\gamma_k)}=\prod_i s^{m_R(\gamma_i)}`.  Justification: additivity of \(m_R\) under the normal-ordered Gram law. |
| `q^nr^ls^{b_R(\gamma)}` | Direct conflation. | `q^nr^ls^{m_R(\gamma)}`. |
| `A projection-finite source has \(b_R=0\), hence cannot produce this \(s\)-degree` | Overstates the reason. Projection-finite excludes positive geometric support; \(s\)-degree is \(m_R\). | `A projection-finite source has \(b_R^{\mathrm{geom}}=0\).  The rank-one \(\delta_2\) lift has \(m_R=1\) and \(b_R^{\mathrm{geom}}=2\), so projection-finite Ran locality cannot supply the wrapped source object needed for this trace degree.` |
| `homogeneous \(s\)-degree is the elliptic degree \(b_R\)` | Direct conflation. | `homogeneous \(s\)-degree is the Gram trace exponent \(m_R\); \(b_R^{\mathrm{geom}}\) supplies the local/wrapped colour.` |

## Places that are safe or nearly safe

- The abstract/recent opening around the current `b_R^{\mathrm{geom}}` and
  `m_R=\operatorname{pr}_3\overline\Pi_X` language is conceptually correct.
  It should be propagated into the body.
- The final checklist around current grep anchors `14292-14300` is also
  conceptually correct: it names \(b_R^{\mathrm{geom}}\), \(m_R\), and trace
  degree \(s^{m_R}\).
- The hybrid base shadow
  \(\bigsqcup_{b\ge0}\operatorname{Ran}(E)_{[b]}\) may keep a plain \(b\) as
  a displayed shadow coordinate, provided the prose says it is only a
  geometric wrapped-degree shadow and not the \(s\)-exponent.

## Latest PDF / Agent53 firewall

The latest PDF has one useful correction and one unsafe overclaim.

Useful: extracted lines `29083-29096` explicitly separate
`mBorch(\gamma)=m` from `bell(\gamma)=m+1` on the D6--D2--D0 branch.
This supports the repair above.

Unsafe: extracted lines `29208-29243` define a finite colored PROP
`\mathsf{Hyb}_R`, claim eight diagrams commute because degree addition and
`AJ_R` are homomorphisms, and then say this is "an actual finite hybrid
local/wrapped source, not a certificate."  Agent53 correctly rejects this.
It proves color-label associativity, not geometric Hall pull-push equality
over local/wrapped stacks, anchors, quotient-after-correspondence, protected
integration, or HN transitions.

Do not import that overclaim into `main.tex`.  If the PDF material is used,
call it a universal algebraic comparison PROP
\(\mathsf{Hyb}^{\mathrm{univ}}_R\), and require a separate geometric
realization functor from \(\mathsf{Corr}^{E,\mathrm{hyb}}_R\).

## Minimal patch plan

1. In the hybrid certificate definition, replace the single `b_R` datum by
   `b_R^{\mathrm{geom}}` plus `m_R=\operatorname{pr}_3\overline\Pi_X`.
   Define local/wrapped sectors only with `b_R^{\mathrm{geom}}`.

2. Replace every \(s\)-exponent occurrence of `b_R` by `m_R`:
   `s^{b_R(...)}`, `q^nr^ls^{b_R(...)}`, and prose saying protected
   integration has `s`-degree `b_R`.

3. Replace every \(\delta_2\) assertion `b_R(...)=1` by:
   ```tex
   m_R(...)=1,\qquad \overline\Pi_X(...)=(0,1,1),\qquad
   b_R^{\mathrm{geom}}(...)>0.
   ```
   In rank-one D6--D2--D0 passages add:
   ```tex
   b_R^{\mathrm{geom}}(...)=2
   ```
   by the dictionary \((h-1,n,d-1)\).

4. Repair transition language: preservation of wrapped-sector color uses
   `b_R^{\mathrm{geom}}`; preservation of the automorphic trace exponent uses
   `m_R`.

5. Add one local warning after the hybrid Ran shadow:
   ```tex
   The displayed \(b\)-coordinate is only the geometric wrapped-degree
   shadow of the hybrid base.  It is not the Gram trace exponent and does
   not replace the wrapped moduli, anchors, mixed extension stacks,
   quotient-after-correspondence descent, or protected integration.
   ```

6. Add one local warning after the eight-word flag requirement:
   ```tex
   Degree-label associativity in a universal colored PROP is not this axiom;
   the axiom is equality of the two geometric pull-push operations over the
   supplied two-step flag stack.
   ```

7. Re-run:
   ```bash
   rg -n --fixed-strings 'b_R' main.tex
   rg -n 's\^\{b_R|s\^\{\\,?b_R|monomial .*b_R|s\)-degree .*b_R|b_R\(.*\)=1|b_R=0|b_R>0' main.tex
   rg -n --fixed-strings 'b_R^{\\mathrm{geom}}' main.tex
   rg -n --fixed-strings 'm_R' main.tex
   ```
   The only surviving `b_R` uses should be `b_R^{\mathrm{geom}}` or legacy
   unrelated multiplication maps named `m_R` in the algebraic sections.  No
   automorphic \(s\)-power should use `b_R`.

## Bottom line

State \(\delta_2\) as \(m_R=1\) and \(b_R^{\mathrm{geom}}>0\).  In the
rank-one D6--D2--D0 branch, state \(b_R^{\mathrm{geom}}=d=2\).  The current
manuscript has already started the repair in the opening and final summary,
but the certificate body still conflates \(b_R\) with the \(s\)-exponent.
