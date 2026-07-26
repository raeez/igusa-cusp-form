# quotient_after_correspondence_theta_mu_associativity

This packet records correction row 253: prove that
\(\theta^Q_{\mu,R}\) is compatible with associativity.

For each word \(w\in\{L,W\}^3\), it checks the naturality square
\[
\overline a_w\circ\Theta^L_w
=\Theta^R_w\circ Q_{E,R}(a_w)
\]
on the quotient of the retained two-step flag stack \(F^2_w\).  The
inputs are the eight wordwise associativity packets and the row-252
operation-comparison maps.

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
python3 compute/verify_quotient_after_correspondence_theta_mu_associativity_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_theta_mu_associativity --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_ASSOCIATIVITY_VERIFIED
```
