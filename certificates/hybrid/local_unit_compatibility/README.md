# local_unit_compatibility

This packet records row 242: local unit compatibility for the hybrid
factorization structure.

It proves that the split `LL` left and right vacuum correspondences
act as identity pull-push maps on the local coefficient
`K_alpha,R,I`.  The proof is before the reduced `E`-quotient and at a
fixed finite HN height.

It does not prove wrapped unit compatibility, quotient descent,
transition compatibility, or aggregate hybrid-carrier population.

Run:

```sh
python3 compute/verify_local_unit_compatibility_obstruction.py \
  --fixture certificates/hybrid/local_unit_compatibility --check
```
