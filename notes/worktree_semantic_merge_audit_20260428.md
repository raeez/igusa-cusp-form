# Worktree Semantic Merge Audit -- 2026-04-28

## Merge principle

The merge rule used here is semantic, not textual.  A worktree is counted
as merged when its strongest true mathematical content is represented in
`main.tex`, in a stronger form if possible, and when its false or weaker
claim is either explicitly rejected in this ledger or demoted inside the
manuscript.  No branch is allowed to vote an existence theorem into the
paper merely by being present in the worktree graph.

## First attack-heal swarm

Integrated or subsumed in `main.tex`:

- `agent/igusa-d0-20260428`: replaced the informal compact Dirac datum by
  a finite-stage `D0` certificate with explicit charge windows,
  residuals, and conditional status.
- `agent/igusa-orient-20260428`: separated connected `BE` descent,
  finite stabilizer descent, and the Klein-four obstruction.
- `agent/igusa-weyl-20260428`: demoted automorphic signs to target checks
  and kept Weyl/Pfaffian monodromy conditional on orientation data.
- `agent/igusa-hybrid-20260428`: replaced global Fock/Hecke language by a
  projection-finite local sector plus wrapped repair problem.
- `agent/igusa-chain-20260428`: inserted the normal-ordered Hall descent
  lane and its obstruction classes.
- `agent/igusa-recognition-20260428`: replaced dimension-only
  recognition by presentation-level obligations: generators, parities,
  relations, pairing, radical quotient, and PBW.

Copied the corresponding reports into `notes/worktree_*_report.md` and
`notes/agent_*_report.md` where available.

## Second attack-heal swarm

Integrated into `main.tex` by semantic merge, not wholesale patch:

- `agent/igusa-next-d0-20260428`: finite-stage `D0`, transition residuals, source/observable residual, full finite support Pfaffian test.
- `agent/igusa-next-orientation-20260428`: separated connected `BE`, Klein-four `E[2]`, and higher even `E[N]` obstruction packages; Weyl transport now preserves quotient trivializations.
- `agent/igusa-next-chain-20260428`: six-class chain normal-ordering descent, exact Frobenius obstruction, Hopf-radical obstruction.
- `agent/igusa-next-hybrid-20260428`: finite hybrid data `b_R`, `lambda_R`, `Q_{E,R}`, `theta^Q_R`, and protected `s^{b_R}` trace degree.
- `agent/igusa-next-koszul-20260428`: source-side chiral Koszul certificate, `C_X` reserved for the coalgebra, scalar renamed `C_{\square,X}`.
- `agent/igusa-next-recognition-20260428`: full parity recognition and the `delta_1+delta_2+delta_3` real-string test.

Copied the corresponding reports into `notes/next_*_attack_heal_report.md`.

## Third attack-heal swarm

Integrated into `main.tex` by semantic merge, with all reports copied to
`notes/third_*_attack_heal_report.md`:

- `agent/igusa-third-d0-source-20260428`: strengthened `D0` from a formal
  certificate to a finite test-window system.  The survivor is
  `Gamma_R^{test}=(Gamma_R^Pi\setminus {0})\cup Gamma_{\Delta,R}`,
  transition residuals on test windows, source/observable residuals, and
  separate support/parity/leading Pfaffian residuals.  No compact
  existence theorem was inferred.
- `agent/igusa-third-orientation-20260428`: replaced the incomplete
  even-stabilizer package by the full even `N>=4` mod-2 cohomology
  calculation
  `H^*(B(Z/2^a)^2;F_2)=Lambda(x_1,x_2) otimes F_2[y_1,y_2]`,
  `|x_i|=1`, `|y_i|=2`, `x_i^2=0`, and the obstruction
  `A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2`.  The mixed coefficient
  `A_{12}^{(N)}` is now explicitly not detected by cyclic order-two
  restrictions.
- `agent/igusa-third-chain-20260428`: lifted normal ordering to a
  `widehat Gamma_X`-graded coefficient formula and split the radical
  obstruction into Lie-ideal and coideal pieces.  The manuscript no
  longer treats Frobenius compatibility or coideal stability as a formal
  consequence of cyclicity.
- `agent/igusa-third-hybrid-20260428`: upgraded the hybrid object from
  datum-plus-trace to finite anchored wrapped prequotients, mixed and
  wrapped correspondences, quotient-after-correspondence descent, and the
  protected integration law with the `s^{b_R}` exponent.
- `agent/igusa-third-koszul-20260428`: separated the target-internal
  bar-cobar counit from the source-side chiral Koszul certificate.  The
  survivor is the separation obstruction `mathfrak o_R^{sep}` and the
  requirement that `C_X`, `F^{co}`, and `Delta_R^{ch}` are supplied
  source data.
- `agent/igusa-third-recognition-20260428`: strengthened primitive
  recognition at the first timelike test channel.  The manuscript and
  computation now record
  `[qrs]D_5/(qrs)^{1/2}=93`,
  `m(delta_1+delta_2+delta_3)=-93`, and the compact target split
  `rootmult_bar0=29`, `rootmult_bar1=93`.

## Fourth attack-heal swarm

Integrated into `main.tex` by main-thread semantic merge, with all
reports copied to `notes/fourth_*_attack_heal_report.md`:

- `agent/igusa-fourth-d0-20260428`: separated finite HN height from the
  automorphic target window by a cofinal schedule `N_R^Delta`, required
  finite null-trivializations rather than Grothendieck zeros, and
  enforced source-to-target direction for the `D0` observable comparison.
- `agent/igusa-fourth-orientation-20260428`: split degree-two gerbe
  obstruction classes from degree-one finite-stabilizer linearization
  characters; the manuscript now requires both `E[2]` and higher even
  `E[N]` linearization triviality, not merely cyclic or Klein-four gerbe
  vanishing.
- `agent/igusa-fourth-pfaffian-20260428`: separated local Pfaffian
  normal-mode ranks `N_delta^Pf` from automorphic divisor orders
  `d_delta^aut`; the Maass/Borcherds calculation is now target-side only,
  while the Hall orientation sign remains conditional on (O1), (O1)+, and
  (O2).
- `agent/igusa-fourth-hybrid-20260428`: upgraded the hybrid source to
  ordered two-sided local/wrapped correspondences, the full eight-word
  flag atlas, quotient formation/admissibility/flag/transition residuals,
  and protected integration residuals.  The Koszul lane now has a formal
  source-target separation lemma for the target bar-cobar counit.
- `agent/igusa-fourth-chain-20260428`: added finite-fibre HN topology to
  normal-ordering descent, finite-stage pushforward formulae for
  `overline Pi_*^Theta`, the topological obstruction
  `mathfrak o_Theta^top`, and finite-window radical/no-extra-relations/PBW
  requirements.
- `agent/igusa-fourth-recognition-20260428`: replaced the first timelike
  coefficient check by a finite Laurent computation and recorded the
  presentation split `29|93` against `[qrs]D_5=93` and
  `m(delta_1+delta_2+delta_3)=-93`.

## Older side branches

Audited the chained `close-*`, `heal/*`, and `cgr/*` worktrees by theorem labels and bibliography keys.

Already present or subsumed in stronger form:

- Dyonic Mukai lattice, `B`-cocycle, and normal-ordered descent.
- PTVV/Joyce descent theorem and cyclic/Frobenius routes.
- Explicit orientation obstruction package for ordinary, connected `BE`, and finite stabilizer descent.
- Klein-four `E[2]` calculation, cyclic-character/Wu/Pin-c formulations, and orbifold-stratum subtlety.
- Higher-rank Pin-c and Brauer-gerbe orientation lanes as conditional reductions.
- Type-II three-wall Pfaffian sign and Weyl-character lanes.
- Gritsenko-Nikulin imaginary-root anchors and low-degree recognition tests.

Intentionally not resurrected:

- The Bott-element sign-normalization remark from `close-bottnorm-*`; the critique identified the Bott explanation as a false source for the lattice identity `B(c,c)=2Pi(c)`. The current manuscript keeps the identity as pure lattice polarization.
- Older Hopf-Frobenius arguments that inferred cyclicity from non-degeneracy or `B^2=0`; these are replaced by the exact obstruction `mathfrak o_F`.

Bibliography audit:

- `JoyceKinjoParkSafronov` and `LiuYalongOrientations` occur in older branches but are not cited in the current manuscript after the stronger conditional rewrite. They were not copied into `proj.bib` to avoid uncited-source drift.

Status:

- The first, second, third, and fourth attack-heal swarms have been
  semantically merged into `main.tex` and their reports copied into
  `notes/`.
- No old side branch has an unmatched theorem lane that should be
  directly reintroduced without weakening the current draft.
- Remaining old-branch content is either already represented in stronger
  finite-stage form or explicitly rejected as mathematically misleading.

## Verification after fourth integration

Commands run in the main worktree after the fourth semantic merge:

- `git diff --check`
- `python3 compute/verify_lattice.py`
- `python3 compute/verify_square_root.py`
- `python3 -m py_compile compute/verify_square_root.py`
- `make`
- `rg -n -i "undefined|multiply defined|fatal|error|warning|rerun" out/main.log`

Results:

- The whitespace diff check passed.
- The lattice verification passed.
- The square-root verification produced the first timelike Laurent check,
  `[qrs]D_5=93`, the presentation split `29|93`, and
  `m(delta_1+delta_2+delta_3)=-93`.
- `make` built `out/main.pdf`.
- The log scan reported only package/rerun infrastructure lines and
  `amsrefs` style warnings; no undefined references, fatal errors, or TeX
  errors were reported.

## Fifth attack-heal swarm

Integrated into `main.tex` and `compute/verify_square_root.py` by
main-thread semantic merge, with all reports copied to
`notes/fifth_*_attack_heal_report.md`:

- `agent/igusa-fifth-d0-pf-20260428`: made the `D0` stages genuinely
  finite via a cofinal discrete HN subsystem `mathcal R`, successor
  transitions, finite operator defects, finite Pfaffian square data, and
  the `finite-pfaffian-window-obstruction` proposition.  The automorphic
  product supplies only a finite `K_0` Pfaffian shadow; compact parity
  pieces remain source data.
- `agent/igusa-fifth-orientation-weyl-20260428`: separated the ordinary
  reduced orientation from Weyl equivariance, added the finite
  `H^1(BE[N];F_2)` zero-character requirement, and inserted the
  Weyl quotient-orientation obstruction package.
- `agent/igusa-fifth-o2-walls-20260428`: inserted the local obstruction
  certificate for (O2), requiring equivariant charts, reduced self-Ext
  splittings, invariant Pfaffian units, and rank-one normal-mode
  computations on all three type-II walls.
- `agent/igusa-fifth-hybrid-real-20260428`: added quotient and
  integration transition residuals and proved that quotient-first or
  determinant/Fock-only categories do not define the hybrid source.
- `agent/igusa-fifth-chain-koszul-20260428`: typed the finite Koszul
  source coalgebra with coaugmentation, counit, finite filtration,
  collision coproduct, conilpotence, coassociativity, counit, and
  transition-continuity defects; the full certificate now propagates
  `mathfrak o_Theta^top`.
- `agent/igusa-fifth-recognition-pbw-20260428`: added the first saturated
  primitive-recognition window `W_{<=3}`, its parity table, finite
  kernel/radical/PBW requirements, and the next monic-product checks
  `m(2delta_1+delta_2+delta_3)=90`,
  `m(delta_1+2delta_2+delta_3)=90`,
  `m(delta_1+delta_2+2delta_3)=90`,
  `m(2delta_123)=-540`.

Status:

- All returned fifth-swarm worktree materials that survived attack were
  merged into the main worktree.
- No fifth-swarm branch was fast-forwarded or blindly applied; seeded
  diffs were treated as evidence and merged by theorem/content anchor.
- Remaining fifth-swarm content is represented by the copied reports.
- The worktrees remain on disk as audit evidence; they were not removed
  or rewritten.

## Sixth attack-heal swarm

Integrated into `main.tex` and `compute/verify_square_root.py` by
main-thread semantic merge, with all reports copied to
`notes/sixth_*_attack_heal_report.md`:

- `agent/igusa-sixth-d0-construct-20260428`: added the finite
  Hall--Dirac atlas and Pfaffian/parity-lift obstruction.  The target
  `K_0` Pfaffian shadow still does not choose compact parity lifts or a
  Pfaffian square root in `Pic(Q_R)[2]`.
- `agent/igusa-sixth-orientation-construct-20260428`: inserted the
  finite-stabilizer obstruction to `(O1)` for odd, `N=2`, and higher even
  `E[N]`, and sharpened Weyl equivariance to a semidirect quotient
  orientation problem.
- `agent/igusa-sixth-o2-hybrid-20260428`: added the `(O2)`/hybrid
  compatibility obstruction, including the three type-II wall labels and
  the positive `s`-degree obstruction on `delta_2`.
- `agent/igusa-sixth-chain-normal-20260428`: separated the formal central
  translation cochain from its Hall realization and added the finite
  verification diagrams `(NO1)--(NO7)`.
- `agent/igusa-sixth-koszul-cobar-20260428`: constructed the canonical
  finite source-bar coalgebra once the hybrid source is supplied, and
  isolated the remaining source-to-target cobar comparison obstruction.
- `agent/igusa-sixth-recognition-presentation-20260428`: extended the
  computation script and manuscript to the height-four signed residuals
  `108|90|18`, doubled isotropic residuals `10|9|1`, and real-string
  exponents.

Status:

- All sixth-swarm materials that survived semantic attack were merged.
- No sixth-swarm branch was fast-forwarded or blindly applied.
- Unsupported existence claims were rejected or rewritten as conditional
  finite constructions and exact obstruction classes.

## Verification after sixth integration

Commands run in the main worktree after the sixth semantic merge:

- `git diff --check`
- `python3 compute/verify_lattice.py`
- `python3 compute/verify_square_root.py`
- `python3 -m py_compile compute/verify_square_root.py`
- `make`
- `rg -n -i "undefined|multiply defined|fatal|error|warning|rerun" out/main.log`

Results:

- The whitespace diff check passed.
- The lattice verification passed.
- The square-root verification produced the first timelike split,
  next additive coefficients, height-four residuals, doubled isotropic
  residuals, and real-string exponents.
- `make` built `out/main.pdf`.
- The log scan reported only package/rerun infrastructure and `amsrefs`
  style warnings; no undefined references, TeX errors, or fatal errors
  were reported.

## Lossless-audit correction after sixth integration

After the sixth merge, a stricter worktree-label audit was run against
the current uncommitted `main.tex`.  This audit proves that a literal
"all side worktrees and dangling tmp work have been losslessly folded
into the paper" claim is not yet justified.

Residual labels present in older side worktrees but not present as labels
in current `main.tex` include:

- `rmk:bmu2-three-additional-routes`;
- `prop:determinant-does-not-determine-hall-constants`;
- `rem:thm3-deliverable`, `rem:thm3-status`;
- `lem:bmu2-small-orbit-vanishing`;
- `lem:bmu2-cohomological-computation`;
- `lem:bmu2-w1-vanishing`;
- `lem:bmu2-orbifold-lift`;
- `rmk:bmu2-cross-check`;
- `rmk:bmu2-orbifold-lift-residual`;
- `lem:elliptic-degree-locality-obstruction`.

Semantic status:

- The determinant/Hall-constants point is present in the current
  recognition certificate and in the first saturated window, but not under
  the old proposition label.  It may still deserve a dedicated compact
  proposition if the manuscript needs the old branch to be represented
  verbatim as a no-go.
- The elliptic-degree locality point is present in stronger form as
  `lem:projection-e-support-locality-obstruction` and in the hybrid
  source certificate.
- The old `bmu2` vanishing routes are deliberately not copied as theorems:
  the current manuscript replaces them by the Klein-four criterion,
  finite-stabilizer linearization characters, and higher even `E[N]`
  residuals.  The older routes contain stronger vanishing language and
  additional hypotheses; copying them directly would weaken rigor unless
  each route is re-attacked and either proved under precise hypotheses or
  rewritten as an optional conditional route.

Conclusion:

- The recent swarms are semantically merged.
- Many older worktree ideas are represented in stronger form.
- A literal lossless global merge across every older side branch and every
  tmp directory has not yet been certified.
- The remaining supremum task is a branch-by-branch semantic diff that
  either inscribes each residual label's valid mathematical content,
  records it as subsumed by a stronger current statement, or explicitly
  rejects it as false/unsupported.

## Supremum semantic merge closure pass

The residual worktree and branch labels listed above were merged into
`main.tex` in theorem-strength form where true, and in explicitly
conditional or rejected form where the old statement overclaimed.

Inscribed as true current content:

- `prop:determinant-does-not-determine-hall-constants` now states the
  determinant/Hall-constant no-go directly in the primitive-recognition
  lane.
- `lem:elliptic-degree-locality-obstruction` is merged as an alias of the
  stronger projection-to-`E` locality obstruction.
- `thm:bracket-level-square-root`, `thm:factorization-square-root`,
  `thm:microscopic-hall-drinfeld-criterion`, and
  `thm:eight-formal-current-rows` are represented by the current
  denominator-algebra, formal-current, primitive-recognition, and
  eight-row current-envelope statements.
- `rem:thm3-status` and `rem:thm3-deliverable` are represented by the
  honest-status remark following the Dirac/Pfaffian theorem.
- `rem:bott-sign-normalization` is represented by the polarization
  remark: Bott/Grothendieck-Witt sign conventions do not prove the Gram
  polarization identity and do not construct orientation linearization.

Preserved without overclaim:

- `rmk:bmu2-three-additional-routes`,
  `lem:bmu2-small-orbit-vanishing`,
  `lem:bmu2-w1-vanishing`,
  `lem:bmu2-cohomological-computation`,
  `lem:bmu2-orbifold-lift`,
  `rmk:bmu2-cross-check`,
  `rem:bmu2-honest-status`, and
  `rmk:bmu2-orbifold-lift-residual` now live in a single current remark
  explaining the three attempted two-torsion routes.  The hyperelliptic,
  Wu-class, and orbifold Pin-c routes are recorded as conditional
  programmes or checks, not as unconditional vanishing theorems.  The
  manuscript keeps the stronger and more accurate finite criterion:
  degree-two gerbe bits and degree-one linearization characters must both
  vanish.

Audit commands run after this pass:

- label comparison of every registered git worktree against current
  `main.tex`;
- label comparison of every local branch under `refs/heads` against
  current `main.tex`;
- label comparison of non-registered `/private/tmp/igusa-*` and
  `/tmp/igusa-*` manuscript copies, excluding primary-source snapshots and
  unrelated cross-repo worktrees, against current `main.tex`;
- duplicate-label scan on current `main.tex`;
- `git diff --check`.
- `python3 compute/verify_lattice.py`.
- `python3 compute/verify_square_root.py`.
- `python3 -m py_compile compute/verify_square_root.py`.
- `make`.
- `rg -n -i "undefined|multiply defined|fatal|error|warning|rerun" out/main.log`.

Results:

- Registered worktree label audit: zero missing labels.
- Local branch label audit: zero missing labels.
- Filtered dangling tmp manuscript audit: zero missing labels.
- Duplicate-label scan: zero duplicate labels.
- Whitespace diff check: passed.
- Lattice verification: passed.
- Square-root verification: passed, including height-four and doubled
  isotropic residual checks.
- Python bytecode check for the square-root verifier: passed.
- TeX build: `out/main.pdf` rebuilt successfully.
- Log scan: only package/rerun infrastructure and `amsrefs` style
  warnings; no undefined references, multiply-defined labels, TeX errors,
  or fatal errors.

## Seventh attack-heal swarm

Integrated into `main.tex` by main-thread semantic merge, with all
reports copied to `notes/seventh_*_attack_heal_report.md`:

- `agent/igusa-seventh-d0-source-20260428`: inserted the finite Hall
  source kernel, its finite Hall source construction, and the cofinal
  target-window parity model.  The paper now separates the constructed
  finite source core from the still-open Dirac/Pfaffian atlas.
- `agent/igusa-seventh-orientation-weyl-20260428`: added the
  finite-stage quotient-orientation character system and the
  finite-stage Weyl cocycle/character system.  The manuscript still
  requires actual finite-stabilizer character triviality; it does not
  infer it from translation invariance.
- `agent/igusa-seventh-o2-hybrid-20260428`: added the stable finite
  type-II local theorem and made the hybrid object an actual
  correspondence-module functor after properness/admissibility and
  Thom--Sebastiani residuals vanish.
- `agent/igusa-seventh-chain-normal-20260428`: added the finite Picard
  normal-ordering lift, Hopf-adjointness radical test, and finite
  normal-ordering closure criterion for `(NO1)--(NO7)`.
- `agent/igusa-seventh-koszul-cobar-20260428`: strengthened the source
  bar coalgebra by bounded non-vacuum length, transition maps, and the
  split residual
  `o^{epsilon,src}_R` versus `o^vartheta_R`.
- `agent/igusa-seventh-recognition-global-20260428`: added the cofinal
  primitive-recognition certificate and global recognition proposition
  covering representatives, relations, pairing, radical quotient,
  no-extra-relations, generation, parity dimensions, and completed PBW.

Additional side-branch closure after the seventh pass:

- `close-strictrect-2c0bec4` had no unmatched labels but contained a
  no-label mathematical correction: the protected chain-level product is
  \(A_\infty\)/homotopy \(E_3\), while strict \(E_3\)-rectification is a
  separate residual not consumed by the \(H^0\) primitive-recognition
  theorem.  This is now explicit in
  Theorem~`thm:ptvv-joyce-pi-descent`.
- `close-w2-vs-aut-2c0bec4` had no unmatched labels but supplied the
  warning not to conflate the infinite Coxeter group
  \(W^{(2)}(\Lambda^{2,1}_{II})\) with the finite chamber-permutation
  group \(\operatorname{Aut}(\operatorname{Poly}_{II})\).  The current
  manuscript preserves this in stronger form: the Hall orientation
  character is asserted only on \(W^{(2)}\), while the
  \(\operatorname{Aut}\)-values are target Maass data unless a semidirect
  Hall lift is supplied.

Verification after this pass:

- Six seventh-swarm worktree reports are byte-identical after copying
  into `notes/`.
- The theorem-label audit against all six seventh worktree manuscripts
  has zero missing labels.
- The theorem-label audit against `close-strictrect-2c0bec4` and
  `close-w2-vs-aut-2c0bec4` has zero missing labels.
- Duplicate-label scan on `main.tex`: zero duplicate labels.
- `git diff --check`: passed.
- `python3 compute/verify_lattice.py`: passed.
- `python3 compute/verify_square_root.py`: passed.
- `python3 -m py_compile compute/verify_square_root.py`: passed.
- `make`: rebuilt `out/main.pdf`.
- Fatal TeX log scan: no undefined control sequences, emergency stops,
  fatal errors, or hard `!` errors.

## Fourteenth attack-heal and current lossless side-work audit

Integrated into `main.tex` and `proj.bib` by main-thread semantic merge,
with report copied to `notes/fourteenth_reconstitution_attack_heal_20260428.md`:

- Status/standalone: time-bound process language was removed from the
  finite closure and first-order certificate statements; supplied
  comparison maps are displayed as supplied quasi-isomorphisms.
- Lattice/normal-ordering: `Gamma_X^{phys}` is explicitly identified with
  the formal full-Mukai bookkeeping lattice, finite primitive layers are
  typed by `(c,T)`, and the no-overcount residual is a cone whose
  acyclicity is required.
- Orientation/Pfaffian: finite stabilizer descent uses Borel classes
  before point-stabilizer reductions; Weyl and semidirect obstruction
  classes live on action groupoids unless complete orbits are supplied;
  Pfaffian section equality invokes the q-expansion principle after the
  supplied automorphic comparison.
- Hybrid/O2/Koszul: `(O2)` includes the full type-II wall atlas package;
  unreduced `tau^{E,hyb}` transitions are separated from reduced
  `bar tau^{hyb}` maps; the hybrid tuple includes the colored
  protected-integration residual; source bar notation is augmented.
- D0/Pfaffian/recognition: compact Pfaffian parity lifts are restricted to
  the cusp-positive window; the Pfaffian block records even/odd factors;
  cofinal primitive recognition is triangular and has an exact-completion
  clause.
- Automorphic/source cross-check: Igusa 1962/1964 primary references are
  cited, and CHL square labels are made source-specific for
  `nabla_3`, `nabla_2`, and the composite `N=4` `F_7` scalar square.

Current audit commands after this pass:

- registered worktree label comparison against current `main.tex`;
- local branch-head label comparison against current `main.tex`;
- unreachable-commit label comparison for every unreachable commit that
  still contains `main.tex`;
- `git diff --check -- main.tex proj.bib`;
- `python3 compute/verify_square_root.py`;
- `python3 compute/verify_lattice.py`;
- `make`.

Results:

- Registered worktrees audited: 78.
- Local branches audited: 80.
- Unreachable commits with `main.tex` audited: 99.
- Sources with labels absent from current `main.tex`: 0.
- Whitespace diff check: passed.
- Square-root verifier: passed.
- Lattice verifier: passed.
- TeX build: `out/main.pdf` rebuilt successfully.
