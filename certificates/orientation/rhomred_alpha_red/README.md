# rhomred_alpha_red

This packet verifies the row-280 formula and obstruction ledger for the
reduced orientation gerbe class
\[
\alpha^{\mathrm{red}}_{\mathcal C}
=w_2(\det K^{\mathrm{red}}_{\mathcal C})
+\operatorname{CS}_{\mathcal C}^{*}
w_2(\det\operatorname{coker}\operatorname{CS}_{\mathcal C}).
\]

It records the zero-sum criterion for proving
\(\alpha^{\mathrm{red}}_{\mathcal C}=0\) and verifies that the retained
finite tables supply neither determinant \(w_2\)-values, nor cosection
cokernel rank-zero rows, nor cokernel \(w_2\)-values, nor the zero-sum
row.

This packet does not construct the row-281 null-homotopy, does not
construct quotient orientation, and does not supply transition
compatibility, vanishing cycles, or protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_alpha_red_obstruction.py \
  --fixture certificates/orientation/rhomred_alpha_red --check
```
