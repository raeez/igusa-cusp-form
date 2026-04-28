# Seventh Chain Normal-Ordering Attack-Heal Report

Date: 2026-04-28.
Role: S7-NO.
Worktree: `/tmp/igusa-seventh-chain-normal`.
Branch: `agent/igusa-seventh-chain-normal-20260428`.

## Claim Attacked

Obligation (6): realize chain-level normal ordering on compact Hall
correspondences and kill the finite tests `(NO1)--(NO7)` where the
mathematics permits it:

- Picard normal-ordering lift for `Theta_Pi`;
- negative-cyclic lift `Theta_Pi^-`;
- finite-fibre HN topology;
- product, coproduct, pairing, Hochschild, triple, Jacobi, Frobenius,
  cyclic trace, and Hopf-radical compatibility.

## Valid Attacks

1. Lattice normal ordering does not itself act on Hall pull-push
   correspondences.  It gives the central translation formula, not the
   geometric action on vanishing-cycle coefficients, orientations, cyclic
   complexes, or HN transitions.
2. The Hochschild equation is partly formal.  Once the finite coefficient
   dg category exists,
   `Theta_Pi(c)=T_{-Pi_X(c)}` satisfies
   `d_Hoch Theta_Pi = B_ch`.  Treating this as still open was too coarse.
3. Finite fibres split from transition compatibility.  Finite support
   makes each fibre of `overline Pi_X` finite; the non-formal part is
   compatibility of transition maps, product, coproduct, and pairing.
4. Negative-cyclic normal ordering is not a Hochschild consequence.  The
   lift `(b+uB_C)Theta_Pi^- = B_ch^-` remains source-side cyclic data.
5. Frobenius kills the Lie-ideal half of the radical, but not the coideal
   half.  The coideal half is killed by finite Hopf adjointness plus
   non-degeneracy of the quotient tensor pairing.
6. The scalar determinant, OP square, and target denominator algebra do
   not supply the cyclic trace, two-step flag homotopies, Hopf adjointness,
   or closed transition-compatible radical kernels.

## Attacks Rejected

- `B=-delta Pi_X` does not trivialize all chain coherences.  It kills the
  Picard/Hochschild degree defect only after the coefficient category is
  supplied.
- Non-degeneracy of the Hopf pairing alone does not imply Frobenius or
  radical coideal stability.  It detects an already supplied equality; it
  does not construct the cyclic trace or coproduct adjointness.
- The finite `D_0` notation does not itself define completed tensor
  products.  Completion remains an inverse limit of finite diagrams.

## Repairs Inscribed

- Added `lem:finite-picard-normal-ordering-lift`.
  It proves:
  `B_ch,R(c,c')=T_{B(c,c')}` is a normalized Hochschild 2-cocycle;
  `d_Hoch Theta_Pi,R^phys=B_ch,R`;
  the extended cochain
  `hat Theta_Pi,R(c,T)=T_{-\overline Pi_X(c,T)}=T_{T-Pi_X(c)}`
  has zero Hochschild boundary on allowed finite channels; and degree
  truncation kills the finite-fibre square `(NO1)`.
- Added `lem:finite-hopf-adjointness-radical-test`.
  It proves the coideal square in `(NO7)` from finite Hopf adjointness,
  non-degeneracy on the radical quotient tensor square, and two-sided
  radical equality.  Together with Frobenius, it kills finite `(NO7)`.
- Added `prop:finite-normal-ordering-closure-criterion`.
  It maps `(N1)--(N7)` source data to `(NO1)--(NO7)` and states exactly
  which finite datum kills each obstruction.
- Updated `D0-N`, `(D_X)`, and the open `D_0` descent obligation to
  reference the closure criterion and separate the formal Picard/fibre
  part from the cyclic/flag/Frobenius/Hopf-adjointness part.

## Claim Status

Proved:

- the lattice extension `widehat Gamma_X` and additive
  `overline Pi_X`;
- the finite Picard/Hochschild normal-ordering lift inside the supplied
  finite coefficient dg category;
- finite-fibre descent for degree-truncation transitions;
- finite radical coideal stability from Hopf adjointness and quotient
  non-degeneracy;
- finite Lie-ideal radical stability from Frobenius.

Conditional:

- action of central translations on actual Hall correspondences,
  orientation lines, cyclic complexes, and transition-compatible product,
  coproduct, and pairing;
- negative-cyclic lift;
- two-step flag coherence;
- CY-3 cyclic trace/Frobenius on the compact reduced sector;
- transition-compatible closed radical in the completed HN topology.

Open:

- construction of the compact finite-HN Hall/factorization source,
  reduced compact/wrapped quotient, cyclic model, and Hopf-adjoint
  coproduct;
- verification of `(N1)--(N7)` for every successor arrow and composite
  non-successor transition.

## Manuscript Anchors

- `lem:finite-picard-normal-ordering-lift`
- `prop:finite-normal-ordering-verification-diagrams`
- `lem:finite-hopf-adjointness-radical-test`
- `prop:finite-normal-ordering-closure-criterion`
- `(D0-N)` in `def:first-order-d0-certificate`
- `(D_X)` in `def:compact-igusa-realization-datum`
- open `D_0` descent obligation in the final construction list

## Commands Run

- `sed -n` reads of local `AGENTS.md`, `CLAUDE.md`, ecosystem invariants,
  ecosystem harness, attack-heal skill, and attack-heal protocol.
- `git status --short --branch`
- `rg --files`
- `rg -n` scans for normal ordering, Hall descent, `Theta`, finite fibre,
  Hochschild, negative cyclic, Frobenius, radical, and `(NO1)--(NO7)`.
- `nl -ba` / `sed -n` reads of the normal-ordered Gram descent section,
  the coefficient dg category, `thm:ptvv-joyce-pi-descent`, the finite
  verification diagrams, `D0-N`, `(D_X)`, primitive recognition, and prior
  chain reports.
- `git diff --check -- main.tex notes/seventh_chain_normal_ordering_attack_heal_report.md`
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-seventh-chain-normal-texcheck main.tex`
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-seventh-chain-normal-texcheck/main.log`

## Verification

- `git diff --check -- main.tex notes/seventh_chain_normal_ordering_attack_heal_report.md`
  passed.
- The first `pdflatex` invocation failed before reading `main.tex` because
  the temporary output directory did not yet exist and pdfTeX could not
  open `main.log`.  After creating
  `/tmp/igusa-seventh-chain-normal-texcheck`, the one-pass `pdflatex`
  syntax check passed and produced `main.pdf`.  It reported expected
  first-pass undefined references/citations because BibTeX and reruns were
  not invoked.
- The fatal-error log scan found no `Undefined control sequence`,
  `Emergency stop`, `Fatal error`, or TeX `!` error lines.

## Residual

NO1 and the Hochschild part of NO3 are now theorem-level finite Picard
facts once the coefficient dg category exists.  NO7 is reduced to
Frobenius plus Hopf adjointness and finite quotient non-degeneracy.  The
surviving obstruction is geometric: construct the compact source and
prove the cyclic lift, flag pentagon, trace Frobenius, product/coproduct
transition compatibility, and closed Hopf-radical subsystem at every
finite HN stage.
