# Transition Parity Decomposition Preservation Obstruction

This packet records the missing data required to prove that finite
transition maps preserve the even and odd parity decompositions in the
primitive-recognition towers.

For a transition map \(T_{\nu+1,\nu}\), parity preservation is the
matrix identity
\[
J_\nu T_{\nu+1,\nu}=T_{\nu+1,\nu}J_{\nu+1},
\]
where \(J=(-1)^F\) is the finite fermion-parity involution.  Equivalently,
the off-diagonal blocks \(T_{\bar 0\bar 1}\) and \(T_{\bar 1\bar 0}\)
vanish in parity-homogeneous bases.  Target parity counts, signed
superdimensions, primitive-transition rows, radical-transition rows,
PBW-transition rows, and the formal parity-pushforward packet do not
substitute for this identity.

Run:

```sh
python3 compute/verify_transition_parity_decomposition_preservation_obstruction.py \
  --fixture certificates/hall/transition_parity_decomposition_preservation --check
```

Expected status:

```text
TRANSITION_PARITY_DECOMPOSITION_PRESERVATION_OBSTRUCTION_VERIFIED
```

This status is not a proof that transition maps preserve parity
decompositions.  It only certifies that the obstruction ledger is
complete while the core transition-parity tables remain empty.
