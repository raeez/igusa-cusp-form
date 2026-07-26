# Protected integration coproduct compatibility

This packet records correction row 259: prove that
\(I_R^{\mathrm{prot}}\) respects the supplied finite binary Hall
coproducts.

For each binary local/wrapped output word
\(w\in\{LL,LW,WL,WW\}\), the packet records the zero-defect square
\[
(\int^{\mathrm{prot}}_{\gamma_1,R}\otimes
\int^{\mathrm{prot}}_{\gamma_2,R})\overline\Delta_{w,R}
=
\Delta_{\mathsf T_R,w}
\int^{\mathrm{prot}}_{\gamma_1+\gamma_2,R}.
\]
The target labels remain abstract monoid-coalgebra labels in this
packet.  Gram degree is supplied separately by
`certificates/hybrid/protected_integration_gram_degree`; the proof that
the labels come from \(\overline\Pi_X\) rather than
\(b_R^{\mathrm{geom}}\) is supplied separately by
`certificates/hybrid/protected_integration_pi_x_separation`.

Product compatibility is imported from
`certificates/hybrid/protected_integration_product_compatibility`.
Primitive-projection compatibility is supplied separately by
`certificates/hybrid/protected_integration_primitive_compatibility`.
This packet does not prove HN-transition compatibility, and it does not
construct the level-Z protected trace or the Pfaffian line.

Run:

```sh
python3 compute/verify_protected_integration_coproduct_compatibility_obstruction.py \
  --fixture certificates/hybrid/protected_integration_coproduct_compatibility --check
```

Expected status:

```text
PROTECTED_INTEGRATION_COPRODUCT_COMPATIBILITY_VERIFIED
```
