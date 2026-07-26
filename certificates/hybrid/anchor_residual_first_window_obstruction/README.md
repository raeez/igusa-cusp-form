# Anchor Residual First-Window Obstruction

This packet records the honest state of correction row 218.  The
first-window vanishing criterion is formal from
`certificates/hybrid/anchor_residual_definition`: all five components
of \(\mathfrak o^\lambda_R\) must vanish in the first relation-closed
window.

The current first-window scaffold
`certificates/first_window/k3e_relation_closed_window` is still
`first_window_scalar_firewall_blocked`.  Its compact-source window,
target-source representative, theorem, and strict transition rows are
empty.  Therefore this packet does not certify
\(\mathfrak o^\lambda_R|_{W_1}=0\); it records the exact missing data
needed for that proof.

Run:

```sh
python3 compute/verify_anchor_residual_first_window_obstruction.py \
  --fixture certificates/hybrid/anchor_residual_first_window_obstruction --check
```

Expected status:

```text
ANCHOR_RESIDUAL_FIRST_WINDOW_OBSTRUCTION_VERIFIED
```
