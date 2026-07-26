# quotient_after_correspondence_quotient_first_exclusion

This packet records correction row 250: the quotient-first construction
is not used.

It proves that every reduced generating arrow in
\(\mathcal Q^{\mathrm{corr}}_{E,R}\) carries a quotient presentation
from a preformed unreduced \(E\)-equivariant correspondence:
\[
(Y_0 \leftarrow \mathfrak E_e \rightarrow Y_1)
\mapsto
([Y_0/E] \leftarrow [\mathfrak E_e/E] \rightarrow [Y_1/E]).
\]
An independently chosen reduced middle stack after quotienting the
object stacks is excluded unless it is identified with
\([\mathfrak E_e/E]\), in which case it is the same
quotient-after-correspondence arrow.

It does not construct \(Q_{E,R}\) on Borel-Moore chains inside this
packet or populate the aggregate hybrid carrier.
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
python3 compute/verify_quotient_after_correspondence_quotient_first_exclusion_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_QUOTIENT_FIRST_EXCLUSION_VERIFIED
```
