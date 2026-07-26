This packet records row 350: the criterion proving finite Hall
bialgebra compatibility
\[
\Delta m=(m\otimes m)(1\otimes\tau\otimes1)(\Delta\otimes\Delta)
\]
for supplied compact Hall product and coproduct operations.

For retained charges \(a,b,u,v\) with \(u+v=a+b\), the criterion uses
the finite decomposition set
\[
\mathsf S(a,b;u,v)=\{(a_1,a_2,b_1,b_2)\mid
a=a_1+a_2,\ b=b_1+b_2,\ u=a_1+b_1,\ v=a_2+b_2\}.
\]
It requires populated product and coproduct legs, a retained
product-splitting square stack, base-change, projection-formula and
product-coproduct Thom-Sebastiani comparison rows, the Koszul middle
braiding sign, and compact-support choice-independence for the final
pushforwards.

The current repository state does not supply compact Hall product
rows, compact Hall coproduct rows, mixed product-splitting square
rows, mixed square functorial comparison rows, \(M\)-matrices,
\(D\)-matrices, or Hall-bialgebra compatibility rows.  This packet
therefore verifies the criterion and obstruction ledger, not a
populated Hall bialgebra.

Run:

```sh
python3 compute/verify_finite_hall_bialgebra_compatibility.py \
  --fixture certificates/hall/finite_hall_bialgebra_compatibility --check
```

The expected status is
`FINITE_HALL_BIALGEBRA_COMPATIBILITY_OBSTRUCTION_VERIFIED`.
