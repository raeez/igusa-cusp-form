# rhomred_finite_stabilizer_klein_four_b02

This packet verifies row 294: the local second cyclic restriction
identity for the \(E[2]\) Klein-four class.

Starting from
\[
\beta^{E,2}_{\mathcal C,S}
=b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2,
\]
the second cyclic restriction sends \(x_1\mapsto0\) and
\(x_2\mapsto t\).  Hence
\[
\iota_2^*\beta^{E,2}_{\mathcal C,S}=b_{02}t^2.
\]
Writing the retained second cyclic restriction as \(r_2t^2\), if it
is supplied, gives \(b_{02}=r_2\).

The packet is local.  It does not supply a retained \(E[2]\) edge
row, a second cyclic restriction row, the value of \(r_2\), the value
of \(b_{02}\), beta vanishing, zero linearization, quotient
orientation, transition compatibility, BBDJS vanishing cycles, or
protected integration.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_klein_four_b02.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_klein_four_b02 --check
```
