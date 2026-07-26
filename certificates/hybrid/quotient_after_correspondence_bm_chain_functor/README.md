# quotient_after_correspondence_bm_chain_functor

This packet records correction row 251: construct \(Q_{E,R}\) on
Borel-Moore chains.

The construction is descent-defined.  For a quotient-presented
coefficient object
\[
q_Y^*\overline K_Y\simeq K_Y,\qquad \overline Y=[Y/E],
\]
it sets
\[
C_*^{BM,E}(Y,K_Y)=C_*^{BM}(\overline Y,\overline K_Y)
\]
and sends descended coefficient morphisms to the induced
Borel-Moore chain maps.  Thus it constructs the chain functor
\[
Q_{E,R}:\mathsf{BM}^{E,\mathrm{hyb}}_R
\to \mathsf{BM}^{\mathrm{red},\mathrm{hyb}}_R .
\]

The operation-comparison maps \(\theta^Q_{\mu,R}\) are supplied
separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`.
The theta_mu associativity compatibility row is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_associativity`.
This packet does not prove compact-support pushforward base change,
prove protected-integration compatibility, or populate the aggregate
hybrid carrier.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.
The protected integration definition is supplied separately by
`certificates/hybrid/protected_integration_definition`.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_bm_chain_functor_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_bm_chain_functor --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_BM_CHAIN_FUNCTOR_VERIFIED
```
