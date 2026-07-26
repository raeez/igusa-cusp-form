This packet records row 353: the finite primitive Hall subspace is
the kernel of the reduced coproduct.

For a supplied finite counital Hall coalgebra stage, set
\[
I_R=\ker\epsilon_R,\qquad
\bar\Delta_R(x)=\Delta_Rx-\eta_R(1)\otimes x-x\otimes\eta_R(1),
\]
and define
\[
P_R=\ker(\bar\Delta_R:I_R\to I_R\otimes I_R).
\]

The present compact source does not supply coproduct matrices, unit or
counit rows, augmentation-ideal bases, reduced-coproduct matrices,
primitive kernel rows, or primitive projection matrices.  This packet
therefore verifies the definition and obstruction ledger, not a
populated primitive source.

Run:

```sh
python3 compute/verify_finite_hall_primitive_subspace_definition.py \
  --fixture certificates/hall/finite_hall_primitive_subspace_definition --check
```

The expected status is
`FINITE_HALL_PRIMITIVE_SUBSPACE_DEFINITION_OBSTRUCTION_VERIFIED`.
