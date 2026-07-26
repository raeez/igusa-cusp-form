# rhomred_finite_stabilizer_two_primary_mixed_term_detection

This packet verifies row 297: the local detector for the mixed term
\(A_{12}^{(N)}x_1x_2\) in the even two-primary finite-stabilizer
class.

The rank-two coefficient functional
\[
\pi_{12}(y_1)=0,\qquad \pi_{12}(x_1x_2)=1,\qquad \pi_{12}(y_2)=0
\]
extracts \(A_{12}^{(N)}\).  Every cyclic subgroup restriction kills
\(x_1x_2\): order-two cyclic subgroups lie in
\(2(\mathbb Z/2^a)^2\), while cyclic subgroups of order at least four
have \(H^*(BC;\mathbb F_2)=\Lambda(u)\otimes\mathbb F_2[v]\) and
\(u^2=0\).

The packet does not supply a retained two-primary edge row, an
\(A_{12}^{(N)}\)-value, beta vanishing, zero linearization, quotient
orientation, transition compatibility, BBDJS vanishing cycles, or
protected integration.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_two_primary_mixed_term_detection.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_two_primary_mixed_term_detection --check
```
