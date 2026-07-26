# quotient_after_correspondence_thom_sebastiani

This packet records correction row 249: quotient-after-correspondence
preserves reduced Thom-Sebastiani transport.

It proves that an \(E\)-equivariant reduced Thom-Sebastiani
isomorphism
\[
\operatorname{TS}^{\mathrm{red}}_e:p_e^*K_{\mathrm{src}}\simeq K_{\mathfrak E_e}
\]
descends uniquely to
\[
\overline{\operatorname{TS}}^{\mathrm{red}}_{\overline e}:
\overline p_e^*\overline K_{\mathrm{src}}\simeq
\overline K_{\mathfrak E_e}
\]
after the coefficient-descent and orientation-descent interfaces are
supplied.

It does not construct the unreduced BBDJS Thom-Sebastiani row, prove
orientation existence, construct \(Q_{E,R}\) on Borel-Moore chains
inside this packet, or populate the aggregate carrier.
Quotient-first exclusion is supplied separately by
`certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion`.
The Borel-Moore chain functor is supplied separately by
`certificates/hybrid/quotient_after_correspondence_bm_chain_functor`.
The operation-comparison maps \(\theta^Q_{\mu,R}\) are supplied
separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`.
The theta_mu associativity compatibility row is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_associativity`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_thom_sebastiani_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_thom_sebastiani --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_THOM_SEBASTIANI_VERIFIED
```
