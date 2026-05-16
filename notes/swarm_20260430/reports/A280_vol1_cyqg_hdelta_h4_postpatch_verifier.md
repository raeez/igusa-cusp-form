# A280 -- Vol I/CYQG HDelta/H4 postpatch verifier

Status: completed; fail repaired by master thread.

Verdict: fail. H4 scalar repair passed, but CYQG introduction still had
stale one-loop/fourth-taxon and H1-only support language.

Pass evidence:
- `modular_trace.tex` preserved
  `\operatorname{div}(\Delta_5)=H_1+2H_4`,
  `\operatorname{div}(\Phi_{10}^{\mathrm{un}})=2H_1+4H_4`, and
  eighth-root H4 monodromy `-1`, order `2`.
- `quantum_groups_foundations.tex` preserved
  `\operatorname{ord}_{H_4}(\Delta_5)=2`,
  `\operatorname{ord}_{H_4}(\Phi_{10}^{\mathrm{un}})=4`, and made the
  primitive `\mu_{16}` claim conditional on a non-split
  Kuga--Satake/metaplectic banding lemma.
- Vol I `derived_langlands.tex` frames the K3 target as recognition,
  not equality.

Residuals repaired:
- `introduction.tex` one-loop-output phrases were rewritten as scalar
  threshold/trace language.
- "fourth taxon" headings were rewritten as K3 target-package language.
- The H1-only support sentence was broadened to
  `\operatorname{div}(\Delta_5)=H_1+2H_4`.

Checks:
- `git diff --check` passed on the CYQG touched files.
- Targeted greps for the stale exact phrases returned no matches after
  the repair.

Follow-up:
- A286 should verify the CYQG micro-repair after the current isolated
  Vol II patches are integrated.
