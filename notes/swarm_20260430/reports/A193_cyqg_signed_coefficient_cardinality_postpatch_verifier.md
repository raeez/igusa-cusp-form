# A193 CYQG Signed-Coefficient/Cardinality Postpatch Verifier

## Claim Attacked

Residual language in `~/calabi-yau-quantum-groups` might still promote
signed Borcherds coefficients, protected indices, or Pfaffian shadows into
ordinary root multiplicities or dimensions.

## Findings

- `chapters/examples/k3e_cy3_programme.tex` still contained several
  root-multiplicity and dimension-count phrases around the older
  programme propositions.
- `notes/physics_bps_root_multiplicities.tex` kept a root-multiplicity
  title/header despite the corrected signed-index interpretation.
- `compute/lib/k3e_coha_structure.py` still exported the legacy
  `root_multiplicity` API without warning.
- `compute/tests/test_k3e_coha_structure.py` still called the legacy API
  in places where the signed character coefficient was the intended
  invariant.

## Recommendation

Patch to the signed root-character/protected-supertrace formulation.
Leave ordinary dimensions and root-space cardinalities behind an explicit
source/parity/fixture recognition gate.

## Status

Integrated by the main thread. Follow-up verification delegated to A204.

