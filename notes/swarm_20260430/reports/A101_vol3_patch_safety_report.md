# A101 Vol III patch safety report

No files edited by the agent.

## Safe ranges

Primary replacement range in the current CYQG checkout:
`chapters/examples/k3e_cy3_programme.tex:177-207`. This is exactly the
old construction plus its proof. Replace the whole block; do not touch
the preceding definition ending at line 175 or the following subsection
at line 209.

Dependent same-file ranges:

- Line 106: replace only the final sentence beginning "The reduced
  Gromov--Witten/PT theory..."; preserve earlier sentences and
  `\end{proof}` at line 107.
- Line 4201: replace only the clause "the Hall--Borcherds comparison of
  Construction...," preserving surrounding hypothesis-list grammar.
- Line 4222: replace the full paragraph.

## Label and reference state

- New label `prop:k3e-borcherds-coefficient-recognition-gate` is absent
  in current TeX.
- Old label `constr:k3e-hcs-hall-borcherds-comparison` occurs once and
  should be preserved as alias in the new proposition.
- Required target theorem exists:
  `chapters/examples/k3e_bkm_chapter.tex` label
  `thm:k3e-positive-half-hall-borcherds-criterion`.
- Required definitions exist: `def:k3e-finite-rees-gluing`,
  `def:cy3-oriented-hcs-hall-comparison-datum`, and
  `def:cy-c-gx-representability-package`.

## Missed dependency prose

`chapters/theory/modular_trace.tex:279-288` and proof lines
`338-344` repeat the finite positive-half morphism into
`U^{\chir}(\mathfrak n_+(\mathfrak g_{\Delta_5}))^{\le N}` and cite the
old construction at line 342. This is outside the same-file ranges and
should be patched or explicitly reviewed with the same
coefficient-recognition discipline.

