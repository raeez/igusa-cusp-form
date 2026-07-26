# rhomred_finite_stabilizer_klein_four_zero_restrictions

This packet verifies row 295 as a criterion and obstruction record.
It proves the classifying-space equivalence
\[
\beta^{E,2}_{\mathcal C,S}=0
\quad\Longleftrightarrow\quad
r_1=r_2=r_3=0
\]
using the coefficient identities from rows 292--294:
\[
b_{20}=r_1,\qquad b_{02}=r_2,\qquad
b_{11}=r_1+r_2+r_3.
\]

The packet does not prove the geometric assertion
\(r_1=r_2=r_3=0\) on retained \(K3\times E\) strata.  That proof
requires retained cyclic zero restriction rows, or an equivalent
edge-reduced finite-stabilizer vanishing row.  The current reduced
orientation fixture supplies neither.

Run:

```sh
python3 compute/verify_rhomred_finite_stabilizer_klein_four_zero_restrictions.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_klein_four_zero_restrictions --check
```
