# wrapped_unit_compatibility

This packet records row 243: wrapped unit compatibility for the hybrid
factorization structure.

It proves that the split `LW` left vacuum correspondence and the
split `WL` right vacuum correspondence act as identity pull-push maps
on the wrapped coefficient `K_eta,R`.  The proof is before the reduced
`E`-quotient and keeps the wrapped anchor memory unchanged.

It does not prove quotient descent, transition compatibility, or
aggregate hybrid-carrier population.

Run:

```sh
python3 compute/verify_wrapped_unit_compatibility_obstruction.py \
  --fixture certificates/hybrid/wrapped_unit_compatibility --check
```
