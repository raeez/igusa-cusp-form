# Higher-Coloured Residual Vanishing Criterion

This packet records correction row 240 as a conditional finite-stage
criterion.  It proves that
\[
\mathfrak o^{\mathrm{col}}_R=0
\]
once the six component rows are supplied.  The tree-contraction
component is discharged by the eight length-three associativity rows
and the four-input pentagon.

The unit object, local unit compatibility, and wrapped unit
compatibility are supplied separately in
`certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences` and
`certificates/hybrid/local_unit_compatibility` and
`certificates/hybrid/wrapped_unit_compatibility`.  Local configuration
symmetric descent is supplied in
`certificates/hybrid/local_configuration_symmetric_descent`, and wrapped
insertion order conventions are supplied in
`certificates/hybrid/wrapped_insertion_order_conventions`.  The packet
still does not supply closed-chart refinement, ordered-chart descent, or
overlap compatibility.  It therefore does not claim unconditional
vanishing.

Run:

```sh
python3 compute/verify_higher_coloured_residual_vanishing_criterion_obstruction.py \
  --fixture certificates/hybrid/higher_coloured_residual_vanishing_criterion --check
```

Expected status:

```text
HIGHER_COLOURED_RESIDUAL_CONDITIONAL_CRITERION_VERIFIED
```
