This packet records row 345: the common-refinement criterion under
which the compact-support Hall target pushforward \(q_!^{cs}\) is
independent of the chosen compactification.

For a supplied retained \(q:\mathfrak E\to Z\), a supplied
constructible coefficient \(K_{\mathfrak E}\), two supplied
compactifications, and a supplied common proper refinement with
extension-by-zero comparison isomorphisms, proper functoriality gives
the same object
\[
\overline q_{12,*}j_{12,!}K_{\mathfrak E}
\]
from both compactifications.

The current repository state does not supply the concrete retained
\(q\)-map, compactification pair, common refinement, comparison
isomorphisms, or populated choice-independence row.  This packet
therefore verifies the criterion and obstruction ledger, not actual
compactification independence for the retained Hall product.

Run:

```sh
python3 compute/verify_finite_hall_product_compactification_independence.py \
  --fixture certificates/hall/finite_hall_product_compactification_independence --check
```

The expected status is
`FINITE_HALL_PRODUCT_COMPACTIFICATION_INDEPENDENCE_OBSTRUCTION_VERIFIED`.
