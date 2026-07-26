# rhomred_finite_stabilizer_two_primary_class

This packet verifies row 296: the local even \(N\ge4\) two-primary
class computation.

For \(2^a\parallel N\), \(a\ge2\), the two-primary group is
\((\mathbb Z/2^a)^2\), and
\[
H^*(B(\mathbb Z/2^a)^2;\mathbb F_2)
=\Lambda(x_1,x_2)\otimes\mathbb F_2[y_1,y_2].
\]
The degree-two basis is \(y_1,x_1x_2,y_2\).  Hence an edge-reduced
finite-stabilizer Borel class has the unique form
\[
\beta^{E,N}_{\mathcal C,S}
=A_1^{(N)}y_1+A_{12}^{(N)}x_1x_2+A_2^{(N)}y_2.
\]

The packet does not supply a retained two-primary edge row,
coefficient values, beta vanishing, zero linearization, quotient
orientation, transition compatibility, BBDJS vanishing cycles, or
protected integration.  The mixed-term cyclic-detection firewall for
\(A_{12}^{(N)}\) is deferred to row 297.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_two_primary_class.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_two_primary_class --check
```
