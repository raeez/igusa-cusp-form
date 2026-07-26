# rhomred_finite_stabilizer_klein_four_b11

This packet verifies row 293: the local mixed coefficient extraction
for the \(E[2]\) Klein-four class.

Starting from
\[
\beta^{E,2}_{\mathcal C,S}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,
\]
the second cyclic restriction sends \(x_1\mapsto0\), \(x_2\mapsto t\),
and the diagonal cyclic restriction sends \(x_1\mapsto t\),
\(x_2\mapsto t\).  Together with the first cyclic identity
\(b_{20}=r_1\), this gives
\[
b_{11}=r_1+r_2+r_3.
\]

The packet is local.  It does not supply a retained \(E[2]\) edge
row, cyclic restriction rows, values of \(r_1,r_2,r_3\), the value of
\(b_{11}\), beta vanishing, zero linearization, quotient orientation,
transition compatibility, BBDJS vanishing cycles, or protected
integration.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_klein_four_b11.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_klein_four_b11 --check
```
