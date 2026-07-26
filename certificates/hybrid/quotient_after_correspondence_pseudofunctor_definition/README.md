# quotient_after_correspondence_pseudofunctor_definition

This packet records correction row 246: the quotient-after-
correspondence pseudofunctor.

It defines the object assignment \(Y \mapsto [Y/E]\), the generating
arrow assignment
\[
(Y_0 \leftarrow \mathfrak E_e \rightarrow Y_1)
\mapsto
([Y_0/E] \leftarrow [\mathfrak E_e/E] \rightarrow [Y_1/E]),
\]
and the coefficient-descent interface \(q_Y^*\overline K_Y\simeq K_Y\).
The correspondence stack is formed before taking the diagonal
\(E\)-quotient.

The composition component is supplied separately by
`certificates/hybrid/quotient_after_correspondence_composition`; the
base-change square component is supplied separately by
`certificates/hybrid/quotient_after_correspondence_base_change`.
The Thom-Sebastiani descent component is supplied separately by
`certificates/hybrid/quotient_after_correspondence_thom_sebastiani`.
The quotient-first exclusion theorem is supplied separately by
`certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion`.
The Borel-Moore chain functor is supplied separately by
`certificates/hybrid/quotient_after_correspondence_bm_chain_functor`.
The operation-comparison maps \(\theta^Q_{\mu,R}\) are supplied
separately by
`certificates/hybrid/quotient_after_correspondence_theta_mu_comparison`.
The HN transition compatibility of \(Q_{E,R}\) is supplied separately by
`certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility`.
The remaining compact-support pushforward base-change, protected
integration, and aggregate components are still absent.

Run:

```sh
python3 compute/verify_quotient_after_correspondence_pseudofunctor_definition_obstruction.py \
  --fixture certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition --check
```

Expected status:

```text
QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED
```
