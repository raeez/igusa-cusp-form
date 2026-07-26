# quotient_after_correspondence_base_change

This packet records correction row 248: quotient-after-correspondence
preserves retained cartesian base-change squares of finite-height
\(E\)-equivariant stacks.

It proves the comparison
\[
[X'/E]\simeq [X/E]\times_{[Y/E]}[Y'/E]
\]
for every retained equivariant cartesian square
\[
X' \simeq X\times_Y Y'.
\]
The packet records source, target, open, and compactified square
families as preserved by quotient.

Thom-Sebastiani descent is supplied separately by
`certificates/hybrid/quotient_after_correspondence_thom_sebastiani`.
Quotient-first exclusion is supplied separately by
`certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion`.
The Borel-Moore chain functor is supplied separately by
`certificates/hybrid/quotient_after_correspondence_bm_chain_functor`.
This packet does not prove compact-support pushforward base change,
coefficient pullback for vanishing cycles, the projection formula, flag
coherences, or aggregate population.  The
operation-comparison maps \(\theta^Q_{\mu,R}\) are supplied separately
by
`certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_base_change_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_base_change --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_BASE_CHANGE_VERIFIED
```
