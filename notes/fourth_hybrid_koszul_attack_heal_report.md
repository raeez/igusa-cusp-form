# Fourth Hybrid/Koszul Attack-Heal Report

Date: 2026-04-28.
Role: H04.
Worktree: `/tmp/igusa-fourth-hybrid`.
Branch: `agent/igusa-fourth-hybrid-20260428`.

## Stable Core

Conditional stable core only.  The manuscript now treats
`\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}` as a finite source
obstruction problem with named correspondence data and residuals.  A
global Fock/Hecke factor, a scalar determinant, and the target
bar-cobar counit do not construct the compact source.

## Valid Attacks

- `A4-H04-01`: The mixed local/wrapped operation was one-sided.  It did
  not explicitly contain ordered local inputs on both sides of a wrapped
  input, so `WL`, `LW`, `LWL`, `WLW`, and related words could be silently
  collapsed.
- `A4-H04-02`: The flag associativity clause used "evident local
  variants."  That did not name the eight local/wrapped triple words,
  the two iterated fibre products, or the four-input pentagon.
- `A4-H04-03`: Quotient-after-correspondence descent named
  `Q_{E,R}` and `\theta^Q_{\mu,R}` but did not isolate formation,
  admissibility, flag, and transition defects.
- `A4-H04-04`: Protected integration was too weakly specified.  The
  `s^{b_R}` law was present, but the chain, product-by-word, coproduct,
  primitive, and transition defects were not named.
- `A4-H04-05`: The target-internal bar-cobar counit was separated in
  prose, but the Koszul lane lacked a local lemma stating that a target
  inverse cannot define `C_{X,R}`, `F^{co}`, `\Delta^{ch}`, or `b_{X,R}`.

## Repairs Inscribed

- `main.tex:228-232` and `main.tex:445-449` now state the compact/hybrid
  repair as local-local, ordered local/wrapped, wrapped-wrapped
  correspondences, full flag coherence, quotient-after-correspondence
  descent, and protected integration.
- `main.tex:5191-5278` adds ordered two-sided mixed correspondences
  `\mathfrak E_{\alpha_-;\eta;\beta_+,R}^{hyb}` and maps
  `\mu_{\alpha_-;\eta;\beta_+,R}^{hyb}`.
- `main.tex:5287-5341` replaces vague flag associativity by the eight
  words `LLL, LLW, LWL, WLL, LWW, WLW, WWL, WWW`, with two iterated
  correspondence fibre products, anchor retention, defects
  `\mathfrak o^{assoc}_{w,R}`, and the four-input pentagon.
- `main.tex:5343-5399` strengthens quotient descent with reduced
  correspondences, admissibility/properness witnesses, anchor kernels,
  and residuals
  `\mathfrak o^{Q,form}_R`, `\mathfrak o^{Q,adm}_R`,
  `\mathfrak o^{Q,flag}_R`, `\mathfrak o^{Q,tr}_{R'R}`.
- `main.tex:5401-5473` strengthens protected integration with chain,
  product-by-word, coproduct, and primitive defects, then records the
  finite hybrid obstruction tuple `\mathfrak O_{hyb,R}`.
- `main.tex:4729-4779` adds the source-target separation lemma: the
  target counit `\varepsilon_{\Delta,R}` is internal to
  `\mathsf{Den}_{\Delta_5,E,\le R}` and cannot define source coalgebra
  data.
- `main.tex:4781-4916` threads `\mathfrak O_{hyb,R}=0` into the chiral
  Koszul certificate and ties `\mathfrak o^{sep}_R` to the separation
  lemma.
- `main.tex:7422-7437`, `main.tex:7580-7615`,
  `main.tex:8253-8263`, and `main.tex:9003-9012` propagate the same
  finite hybrid/Koszul obligations into the full Dirac-Igusa
  certificate, the open full-certificate list, and the final synthesis.

## Exact Data Added

- Ordered mixed stacks:
  `\mathfrak E_{\alpha_-;\eta;\beta_+,R}^{hyb}` with local inputs on both
  sides of the wrapped input.
- Ordered mixed operations:
  `\mu_{\alpha_-;\eta;\beta_+,R}^{hyb}`.
- Full flag atlas:
  `\mathfrak{Flag}^{w}_{\xi_1,\xi_2,\xi_3,R}` for all
  `w in {L,W}^3`.
- Quotient package:
  reduced correspondences, quotient maps, admissibility/properness
  witnesses, orientation-descent isomorphisms, anchor kernel
  `K_{\lambda,R}`, and `\theta^Q_{\mu,R}` coherence.
- Integration package:
  `\mathfrak o^{I,ch}_R`, `\mathfrak o^{I,prod}_{w,R}`,
  `\mathfrak o^{I,co}_R`, `\mathfrak o^{I,\Prim}_R`.
- Hybrid residual tuple:
  `\mathfrak O_{hyb,R}`.
- Koszul separation:
  `\varepsilon_{\Delta,R}` and the rule that target-side bar-cobar data
  can only be compared to an independently constructed source coalgebra.

## Commands

- Read/inspection: `sed -n`, `nl -ba`, `rg -n` on `AGENTS.md`,
  `CLAUDE.md`, inherited ecosystem rules, attack-heal protocol,
  `main.tex`, and the two third-round reports.
- `git diff --check -- main.tex`: first run found one trailing space in
  the eight-word display; fixed.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-fourth-hybrid-texcheck main.tex`:
  passed.  The run reports expected first-pass unresolved references and
  citations plus layout warnings.
- `git diff --check -- main.tex`: passed after the whitespace repair.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-fourth-hybrid-texcheck main.tex`:
  passed after the whitespace repair.
- `git add main.tex notes/fourth_hybrid_koszul_attack_heal_report.md`:
  staged only owned paths.
- `git diff --cached --check -- main.tex notes/fourth_hybrid_koszul_attack_heal_report.md`:
  passed.

## Files Changed And Staged

- `main.tex`
- `notes/fourth_hybrid_koszul_attack_heal_report.md`

## Residual Obligations

1. Construct the compact extension-closed Hall category and finite HN
   quotients.
2. Construct rigidified wrapped prequotients and anchors.
3. Construct the local-local, all ordered local-wrapped, and
   wrapped-wrapped extension stacks with vanishing-cycle pull-push
   admissibility.
4. Prove the full eight-word flag coherences and four-input pentagon.
5. Construct `Q_{E,R}` as a quotient-after-correspondence functor with
   all quotient residuals zero.
6. Construct protected integration with all `I`-residuals zero and
   coefficientwise `s^{b_R}` trace law.
7. Construct `C_{X,R}`, `F^{co}_{R,\bullet}`, `\Delta_R^{ch}`,
   `b_{X,R}`, and `\Theta_{Kos,R}` from the source, not from the target
   counit.
8. Prove primitive recognition, parity bases, relations, Hopf pairing,
   radical quotient, no-extra-relations, and completed PBW.
