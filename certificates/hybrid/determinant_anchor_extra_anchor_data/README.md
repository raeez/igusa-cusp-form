# Determinant Anchor Extra Anchor Data

This packet records correction row 216.  On a finite row where the
elliptic pushforward is represented by a degree-zero semistable vector
bundle \(V\), write
\[
\operatorname{gr}^{\mathrm{JH}}(V)=L_1\oplus\cdots\oplus L_r,
\qquad L_i\in\operatorname{Pic}^0(E).
\]
Atiyah's classification and the S-equivalence description of
semistable bundles on an elliptic curve make the unordered divisor
\[
\operatorname{sp}^{\mathrm{JH}}(V)
= [L_1]+\cdots+[L_r]\in \operatorname{Sym}^r\operatorname{Pic}^0(E)
\]
independent of the Jordan-Hoelder filtration.  This is the extra anchor
datum.  Its Abel sum is \(\det V\), so it refines the determinant
anchor rather than replacing it.

For the rank-two determinant-zero test pair,
\[
V_0=\mathcal O_E^{\oplus2},\qquad
V_L=L\oplus L^{-1},\quad L\ne\mathcal O_E,
\]
the determinant anchor is \(\mathcal O_E\) for both objects, while
\[
\operatorname{sp}^{\mathrm{JH}}(V_0)=2[\mathcal O_E],
\qquad
\operatorname{sp}^{\mathrm{JH}}(V_L)=[L]+[L^{-1}],
\]
and the two divisors in \(\operatorname{Sym}^2\operatorname{Pic}^0(E)\)
are unequal.

This packet does not prove full anchor losslessness, quotient descent,
stabilizer linearization, transition compatibility, or
\(o^\lambda_R=0\).  The residual definition is separated in
`certificates/hybrid/anchor_residual_definition`.

Run:

```sh
python3 compute/verify_determinant_anchor_extra_anchor_data_obstruction.py \
  --fixture certificates/hybrid/determinant_anchor_extra_anchor_data --check
```

Expected status:

```text
DETERMINANT_ANCHOR_EXTRA_ANCHOR_DATA_VERIFIED
```
