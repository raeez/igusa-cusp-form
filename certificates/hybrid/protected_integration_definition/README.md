# Protected integration definition

This packet records correction row 257: define
\(I_R^{\mathrm{prot}}\).

The certified datum is the finite chargewise direct sum
\[
I_R^{\mathrm{prot}}
=\bigoplus_{\gamma\in\Gamma_R}
\int^{\mathrm{prot}}_{\gamma,R}:
Q_{E,R}\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}
\to \mathbb C[\mathsf T_R]_{\le R}.
\]
Each chargewise summand is a supplied degree-zero chain map to the
abstract line \(\mathbb C e_{\omega_R(\gamma)}\).  Gram degree is
supplied separately by
`certificates/hybrid/protected_integration_gram_degree`.  This packet
leaves the normal-ordered label comparison to
`certificates/hybrid/protected_integration_pi_x_separation`.

Product compatibility is supplied separately by
`certificates/hybrid/protected_integration_product_compatibility`.
Coproduct compatibility is supplied separately by
`certificates/hybrid/protected_integration_coproduct_compatibility`.
Primitive-projection compatibility is supplied separately by
`certificates/hybrid/protected_integration_primitive_compatibility`.
This packet does not prove HN-transition compatibility, and it does not
construct the level-Z protected trace or the Pfaffian line.

Run:

```sh
python3 compute/verify_protected_integration_definition_obstruction.py \
  --fixture certificates/hybrid/protected_integration_definition --check
```

Expected status:

```text
PROTECTED_INTEGRATION_DEFINITION_VERIFIED
```
