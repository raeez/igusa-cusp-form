# rhomred_finite_stabilizer_gerbe_linearization_independence

This packet verifies the row-290 firewall:
\[
\beta^H_{\mathcal C,S}=0 \not\Rightarrow
\lambda^H_{\mathcal C,S}=0.
\]

For \(E[2]\), the degree-two gerbe coordinates
\((b_{20},b_{11},b_{02})=(0,0,0)\) may coexist with the nonzero
degree-one character \((\lambda_1,\lambda_2)=(1,0)\).  For
\((\mathbb Z/2^a)^2\), the values
\((A_1,A_{12},A_2)=(0,0,0)\) may coexist with
\((\lambda_1,\lambda_2)=(1,0)\).  Thus row 286 gerbe vanishing and row
287 gerbe null-trivialization do not replace row 288 computation or
row 289 zero-linearization.

This packet imports the row-289 zero-linearization obstruction packet
and records that the current tables still supply no lambda values and
no zero-linearization rows.  The independence firewall is proved; the
zero-linearization theorem is not.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_gerbe_linearization_independence.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_gerbe_linearization_independence --check
```
