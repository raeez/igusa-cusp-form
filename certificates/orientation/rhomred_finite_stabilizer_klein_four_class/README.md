# rhomred_finite_stabilizer_klein_four_class

This packet verifies row 291: the local \(E[2]\) Klein-four
classifying-space computation.

For \(E[2]\simeq(\mathbb Z/2)^2\),
\[
H^*(BE[2];\mathbb F_2)=\mathbb F_2[x_1,x_2],\qquad |x_i|=1,
\]
so
\[
H^2(BE[2];\mathbb F_2)
=\mathbb F_2\langle x_1^2,x_1x_2,x_2^2\rangle.
\]
An edge-reduced finite-stabilizer Borel class therefore has the unique
form
\[
\beta^{E,2}=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2.
\]

This packet does not supply a retained \(E[2]\)-edge row, coefficient
values, cyclic-restriction values, beta vanishing, zero linearization,
quotient orientation, transition compatibility, vanishing cycles, or
protected integration.  Rows 292-294 derive the identities
\(b_{20}=r_1\), \(b_{11}=r_1+r_2+r_3\), and \(b_{02}=r_2\).

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_klein_four_class.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_klein_four_class --check
```
