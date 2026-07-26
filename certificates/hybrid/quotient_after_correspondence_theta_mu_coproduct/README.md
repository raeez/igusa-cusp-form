# quotient_after_correspondence_theta_mu_coproduct

This packet records correction row 254: prove that the quotient
comparison maps \(\theta^Q_{\mu,R}\) are compatible with supplied
finite Hall coproduct and bialgebra rows.

It proves the product-coproduct naturality square for quotient-presented
finite rows:
\[
(Q_{E,R}\boxtimes Q_{E,R})\Delta_R\mu_R
\rightrightarrows
(\overline\mu_R\boxtimes\overline\mu_R)
(1\boxtimes\tau\boxtimes1)
(\overline\Delta_R\boxtimes\overline\Delta_R)Q_{E,R}^{\boxtimes2}.
\]
The two arrows agree by quotient descent from the same retained
four-leg extension-splitting correspondence.

Primitive-projection compatibility is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_primitives`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.
The packet does not construct the compact Hall source bialgebra
tables, prove Hall-coproduct transition compatibility, define
protected-integration compatibility, or populate the aggregate hybrid
carrier.  The protected integration definition is supplied separately by
`certificates/hybrid/protected_integration_definition`.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_theta_mu_coproduct_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COPRODUCT_VERIFIED
```
