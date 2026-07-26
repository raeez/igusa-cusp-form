# quotient_after_correspondence_composition

This packet records correction row 247: quotient-after-correspondence
preserves composition for finite-height retained spans.

It proves the comparison
\[
[(\mathfrak E_e\times_{Y_1}\mathfrak E_f)/E]
\simeq
[\mathfrak E_e/E]\times_{[Y_1/E]}[\mathfrak E_f/E],
\]
and records zero defect for the associativity cocycle of three
composable spans.

Base-change square preservation is supplied separately by
`certificates/hybrid/quotient_after_correspondence_base_change`.  This
packet does not prove Thom-Sebastiani transport; that descent is
supplied separately by
`certificates/hybrid/quotient_after_correspondence_thom_sebastiani`.
Quotient-first exclusion is supplied separately by
`certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion`.
The Borel-Moore chain functor is supplied separately by
`certificates/hybrid/quotient_after_correspondence_bm_chain_functor`.
The operation-comparison maps \(\theta^Q_{\mu,R}\) are supplied
separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`.
Flag coherences are supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_associativity`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.
Aggregate population remains absent here.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_composition_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_composition --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_COMPOSITION_VERIFIED
```
