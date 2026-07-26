# quotient_after_correspondence_theta_mu_comparison

This packet records correction row 252: construct the comparison maps
\(\theta^Q_{\mu,R}\).

For a quotient-presented operation row
\[
Y_1\times\cdots\times Y_k \xleftarrow{p_e} \mathfrak E_e
\xrightarrow{q_e}Y_0
\]
with descended input coefficients, descended Thom-Sebastiani
transport, and a quotient-presented compact-support pushforward row
\(\delta_{q,e}\), it constructs
\[
\theta^Q_{\mu,e,R}:
Q_{E,R}q_{e,!}^{cs}\operatorname{TS}^{red}_ep_e^*
\simeq
\overline q_{e,!}^{cs}\overline{\operatorname{TS}}^{red}_{\overline e}
\overline p_e^*(Q_{E,R}^{\boxtimes k}).
\]

Associativity compatibility is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_associativity`.
Coproduct compatibility is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_coproduct`.
Primitive-projection compatibility is supplied separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_primitives`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.
The packet does not prove Hall-operation transition compatibility,
protected-integration compatibility, or aggregate hybrid population.
The protected integration definition is supplied separately by
`certificates/hybrid/protected_integration_definition`.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_theta_mu_comparison_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_theta_mu_comparison --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_COMPARISON_VERIFIED
```
