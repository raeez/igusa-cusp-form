# rhomred_finite_stabilizer_odd_transfer

This packet verifies row 298: odd-order transfer kills positive-degree
\(\mathbb F_2\)-group cohomology.

If \(H\) has odd order, then multiplication by \(|H|\) is invertible
over \(\mathbb F_2\), and transfer gives
\[
H^i(BH;\mathbb F_2)=0,\qquad i>0.
\]
Thus, after a retained odd finite-stabilizer class has been reduced to
the classifying-space edge, both the degree-two Borel target and the
degree-one residual character target vanish.

The packet is local.  It does not supply a retained odd-order stratum,
an equivariant Cech--Borel representative, an edge-reduction row,
all-retained-stabilizer coverage, compatible null-trivialisations,
transition compatibility, BBDJS vanishing cycles, or protected
integration.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_odd_transfer.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_odd_transfer --check
```
