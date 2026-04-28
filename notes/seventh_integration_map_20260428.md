# Seventh Swarm Integration Map

Purpose: main-thread semantic merge checklist for the six worktree
reports. The present manuscript is already organized around finite
certificates and obstruction tuples. New material enters `main.tex` only
when it strengthens one of these certificates without making an
unsupported compact existence claim.

## Main-thread merge ledger

Reports imported losslessly:

- `notes/seventh_d0_source_attack_heal_report.md`
- `notes/seventh_orientation_weyl_attack_heal_report.md`
- `notes/seventh_o2_hybrid_attack_heal_report.md`
- `notes/seventh_chain_normal_ordering_attack_heal_report.md`
- `notes/seventh_koszul_cobar_attack_heal_report.md`
- `notes/seventh_recognition_global_attack_heal_report.md`

Manuscript merge rule applied: labels and proof blocks from all six
worktree manuscripts were audited against `main.tex`; source-only
material was either inscribed in the appropriate certificate section or
kept as a report-level residual when it would overstate the construction
as completed. No compact existence theorem was upgraded beyond the
geometric data actually supplied.

Global side-branch audit:

- `close-strictrect-2c0bec4` supplied the correction that the protected
  chain-level product is \(A_\infty\)/homotopy \(E_3\), with strict
  \(E_3\)-rectification left as a residual not used by the \(H^0\)
  recognition theorem. This has been semantically merged into
  Theorem~`thm:ptvv-joyce-pi-descent`.
- `close-w2-vs-aut-2c0bec4` supplied the correction that
  \(W^{(2)}(\Lambda^{2,1}_{II})\) and
  \(\operatorname{Aut}(\operatorname{Poly}_{II})\) must not be conflated.
  The current manuscript preserves the stronger honest form: it proves the
  \(W^{(2)}\)-character statement and records the \(\operatorname{Aut}\)
  values as automorphic target data unless a semidirect Hall lift is
  separately supplied.

## D0 finite source

Primary anchors:

- `def:first-order-d0-certificate`
- `prop:finite-pfaffian-window-obstruction`
- `prop:finite-d0-atlas-parity-obstruction`
- `thm:first-order-d0-certificate`

Stable core already present:

- finite HN support and cofinal target windows;
- normal-ordered charge extension and additive Gram homomorphism;
- finite Hall--Dirac atlas as the exact missing source object;
- compact parity ambiguity separated from signed determinant data;
- Pfaffian line and support/parity/leading residuals typed.

Merge acceptance:

- accept any actual construction of a finite Hall--Dirac atlas from named
  compact moduli/correspondence inputs;
- accept sharper obstruction typing for Pfaffian square roots or parity
  lifts;
- reject any derivation of compact parity pieces from the scalar product
  alone.

## O1 and O1+

Primary anchors:

- `lem:E-equivariant-descent-obstruction`
- `lem:bmu2-klein-four-vanishing`
- `lem:even-finite-stabilizer-residuals`
- `cor:finite-stabilizer-o1-obstruction`
- `lem:weyl-quotient-orientation-obstruction`
- `cor:semidirect-wall-transport-obstruction`

Stable core already present:

- connected `BE` and finite `E[N]` descent are separated;
- odd `N` vanishes cohomologically;
- `E[2]` requires both degree-two gerbe bits and degree-one character
  bits;
- even `N >= 4` has an independent mixed two-primary class and
  degree-one characters;
- Weyl-equivariance requires determinant-line lifts and a braid/cocycle
  obstruction, not only target Maass signs.

Merge acceptance:

- accept a proof of trivial finite-stabilizer characters only with an
  actual equivariant orientation-line calculation;
- accept a Weyl cocycle theorem only if it is source-side and checks the
  braid/cocycle law;
- reject any argument from ordinary translation invariance to trivial
  linearization.

## O2 and Hybrid

Primary anchors:

- `def:type-ii-pfaffian-wall-certificate`
- `prop:o2-local-obstruction-certificate`
- `def:hybrid-wrapped-factorization-certificate`
- `prop:hybrid-certificate-scope`
- `prop:o2-hybrid-compatibility-obstruction`
- `op:hybrid-wrapped-factorization`

Stable core already present:

- the three type-II wall labels are fixed;
- the local model is a finite wall certificate, not a global Hall
  construction;
- positive elliptic degree cannot be projection-finite over `E`;
- hybrid source requires rigidified wrapped prequotients, ordered mixed
  correspondences, eight-word flags, quotient-after-correspondence, and
  protected integration;
- the `delta_2` wall must pass through the wrapped lane.

Merge acceptance:

- accept geometric O2 rank/parity computations only if attached to the
  finite wall chart and reduced self-Ext splitting;
- accept hybrid construction only if it builds the mixed correspondence
  category before quotienting;
- reject a detached Fock, Hecke, or scalar `s`-degree replacement.

## Chain Normal Ordering

Primary anchors:

- `def:normal-ordering-coefficient-dg-category`
- `thm:ptvv-joyce-pi-descent`
- `prop:finite-normal-ordering-verification-diagrams`
- `lem:F-frobenius-from-hopf-nondegeneracy`

Stable core already present:

- `Theta_Pi(c)=T_{-Pi_X(c)}` is formal only after the coefficient dg
  category exists;
- finite fibres are inverse-limit data, not uncontrolled infinite
  products;
- `NO1--NO7` type topological, Hochschild, triple, Jacobi, Frobenius,
  cyclic, and radical obstructions.

Merge acceptance:

- accept any finite-stage chain realization that proves the seven diagrams
  commute;
- accept independent constructions of the negative-cyclic lift or radical
  coideal condition;
- reject promotion of the lattice identity `dTheta=B` to chain-level
  normal ordering without the Hall correspondence action and finite HN
  topology.

## Koszul Source

Primary anchors:

- `lem:source-target-koszul-separation`
- `def:chiral-koszul-source-certificate`
- `prop:canonical-source-bar-coalgebra`
- `cor:source-bar-remaining-cobar-obstruction`
- `prop:chiral-koszul-source-certificate-consequence`

Stable core already present:

- source/target separation is explicit;
- after the hybrid source is supplied, the reduced chiral bar coalgebra
  gives a canonical finite source coalgebra;
- conilpotence and the collision coproduct are source-bar consequences;
- the remaining obstruction is the source-to-target cobar
  quasi-isomorphism.

Merge acceptance:

- accept sharpened finite bar/cobar comparison theorems only if the
  hybrid source appears first;
- accept a target comparison only as a source-to-target map with checked
  primitive restriction;
- reject use of the target bar-cobar counit to define the source
  coalgebra.

## Primitive Recognition

Primary anchors:

- `thm:primitive-recognition`
- `prop:low-degree-denominator-brackets`
- `prop:determinant-does-not-determine-hall-constants`
- `prop:delta123-presentation-count`
- `prop:first-saturated-primitive-recognition-window`

Stable core already present:

- recognition is presentation-level: representatives, relations, Hopf
  pairing, radical quotient, no-extra-relations, generation, completed
  PBW, and full parity dimensions;
- `W_{\le3}` is the first saturated finite target window;
- the first timelike channel requires `29|93`, not just signed `-64`;
- height four already shows new residuals not determined by additive
  coefficients alone.

Merge acceptance:

- accept compact recognition only with source representatives and Hall
  relation checks;
- accept target-side computations when clearly labeled as target
  certificates;
- reject determinant or signed-dimension arguments as no-extra-relations,
  radical, or PBW proofs.
