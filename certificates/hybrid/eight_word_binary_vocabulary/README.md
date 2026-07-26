# Eight-Word Binary Vocabulary

This packet records correction row 228.  It defines the hybrid alphabet
\(\{\mathrm L,\mathrm W\}\), with type product
\(\mathrm L\star\mathrm L=\mathrm L\) and all other binary products
equal to \(\mathrm W\).  It records the eight length-three words
\[
\mathrm{LLL},\mathrm{LLW},\mathrm{LWL},\mathrm{WLL},
\mathrm{LWW},\mathrm{WLW},\mathrm{WWL},\mathrm{WWW}
\]
and the left/right parenthesization symbols.

This packet does not construct the two-step flag stacks and does not
prove associativity, pentagon coherence, quotient descent, or
transition compatibility.

Run:

```sh
python3 compute/verify_eight_word_binary_vocabulary_obstruction.py \
  --fixture certificates/hybrid/eight_word_binary_vocabulary --check
```

Expected status:

```text
EIGHT_WORD_BINARY_VOCABULARY_DEFINED
```
