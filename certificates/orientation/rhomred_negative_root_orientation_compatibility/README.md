# rhomred_negative_root_orientation_compatibility

This packet verifies row 333 as a negative-root orientation-compatibility
criterion.  It does not prove compatibility.

The criterion requires compact Hall source data:

- retained positive and negative source charts,
- a compact-source duality lift,
- parity decompositions on both signs,
- a source positive-negative Hopf-pairing matrix with off-parity blocks
  zero,
- radical quotient rows,
- orientation square roots on both signs,
- the Calabi-Yau threefold Serre-duality sign line,
- quotient-orientation transport and Picard-groupoid transition rows.

The current target presentation has formal positive-negative blocks, and
the retained moduli window is closed under duals.  Those facts are
inputs only.  They do not construct compact Hall source pairings or
orientation-line transport.

Verifier:

```bash
python3 compute/verify_rhomred_negative_root_orientation_compatibility.py \
  --fixture certificates/orientation/rhomred_negative_root_orientation_compatibility \
  --check
```

A positive result is
`RHOMRED_NEGATIVE_ROOT_ORIENTATION_COMPATIBILITY_OBSTRUCTION_VERIFIED`.
