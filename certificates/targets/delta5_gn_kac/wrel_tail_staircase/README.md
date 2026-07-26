# W_rel six-row tail staircase

This target-side certificate proves the symbolic two-step tail
`A_N -> B_N -> A_{N+2}` for every even `N >= 14`.  The proof uses
only the Lorentzian pairing, real-string exponents, and the
`q^0` support `y^{-1}+10+y` of `phi_{0,1}`.  The `finite_anchor.csv`
table verifies the six rows of `A_14` inside the finite
`wrel_degree_closure` packet.  The `unbounded_tail.csv` table records
a strictly increasing coordinate subsequence, so finite target-degree
enumeration cannot close this target-only audit.  It is not a compact
source theorem and does not prove primitive recognition.

Run:

```sh
python3 compute/verify_wrel_tail_staircase.py \
  --fixture certificates/targets/delta5_gn_kac/wrel_tail_staircase \
  --wrel-fixture certificates/targets/delta5_gn_kac/wrel_degree_closure \
  --check
```

A positive result is `WREL_TAIL_STAIRCASE_VERIFIED`.
