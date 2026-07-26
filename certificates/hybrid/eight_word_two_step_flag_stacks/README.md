# Eight-Word Two-Step Flag Stacks

This packet records correction row 229.  For each word in
\[
\{\mathrm{LLL},\mathrm{LLW},\mathrm{LWL},\mathrm{WLL},
\mathrm{LWW},\mathrm{WLW},\mathrm{WWL},\mathrm{WWW}\}
\]
it records a retained two-step filtration stack
\(\mathfrak F^{(2),w}_{\xi_1,\xi_2,\xi_3,R}\) and the two comparison
maps to the left and right iterated binary correspondence fibre
products.

This packet constructs the stacks and comparison maps only.  It does
not prove associativity, the four-input pentagon, quotient descent, or
transition compatibility.

Run:

```sh
python3 compute/verify_eight_word_two_step_flag_stacks_obstruction.py \
  --fixture certificates/hybrid/eight_word_two_step_flag_stacks --check
```

Expected status:

```text
EIGHT_WORD_TWO_STEP_FLAG_STACKS_CONSTRUCTED
```
