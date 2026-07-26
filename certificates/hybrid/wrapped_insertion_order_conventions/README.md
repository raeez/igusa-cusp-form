# wrapped_insertion_order_conventions

This packet records correction row 245: braid/order conventions for
wrapped insertions in the hybrid tree category.

It proves that wrapped leaves are ordered by planar leaf order, that
binary vertices concatenate wrapped subsequences, and that the ordered
`WW` source pair `(eta1, eta2)` is represented by the Hall sequence
`0 -> W_eta2 -> B -> W_eta1 -> 0`.  The eight two-step flag comparison
maps preserve the same ordered wrapped subsequence.

No braid operator is introduced.  This packet does not prove unordered
wrapped-pair symmetric descent, ordered-chart descent to the symmetric
finite-colour colimit, overlap compatibility, quotient descent,
transition compatibility, or aggregate hybrid-carrier population.

Run:

```sh
python3 compute/verify_wrapped_insertion_order_conventions_obstruction.py \
  --fixture certificates/hybrid/wrapped_insertion_order_conventions --check
```

Expected status:

```text
WRAPPED_INSERTION_ORDER_CONVENTIONS_VERIFIED
```
