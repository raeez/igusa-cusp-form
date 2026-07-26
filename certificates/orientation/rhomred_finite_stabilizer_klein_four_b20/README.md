# rhomred_finite_stabilizer_klein_four_b20

This packet verifies row 292: the local first cyclic restriction
identity
\[
b_{20}=r_1.
\]

For \(\iota_1:\langle e_1\rangle\hookrightarrow E[2]\), with
\(t\in H^1(B\langle e_1\rangle;\mathbb F_2)\),
\[
\iota_1^*(x_1)=t,\qquad \iota_1^*(x_2)=0.
\]
Thus
\[
\iota_1^*(b_{20}x_1^2+b_{11}x_1x_2+b_{02}x_2^2)=b_{20}t^2.
\]
If the first cyclic restriction is \(r_1t^2\), then \(b_{20}=r_1\).

This packet does not supply a retained first cyclic restriction row,
the value of \(r_1\), the value of \(b_{20}\), beta vanishing, zero
linearization, quotient orientation, transition compatibility,
vanishing cycles, or protected integration.  Rows 293 and 294 compute
the remaining coefficient identities.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_klein_four_b20.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_klein_four_b20 --check
```
