# Protected integration primitive compatibility

This packet records correction row 260: prove that
\(I_R^{\mathrm{prot}}\) respects the supplied finite primitive
projection.

The certified square is
\[
I_R^{\mathrm{prot}}\overline\pi_R^{\mathrm{Prim}}
=
\pi_{\mathsf T_R}^{\mathrm{Prim}}I_R^{\mathrm{prot}}.
\]
The target primitive projector is an abstract projector on
\(\mathbb C[\mathsf T_R]_{\le R}\).  Gram degree is supplied separately
by `certificates/hybrid/protected_integration_gram_degree`; the proof
that the labels come from \(\overline\Pi_X\) rather than
\(b_R^{\mathrm{geom}}\) is supplied separately by
`certificates/hybrid/protected_integration_pi_x_separation`.

Product and coproduct compatibility are imported from the row-258 and
row-259 packets.  This packet does not prove HN-transition
compatibility, and it does not construct the level-Z protected trace or
the Pfaffian line.

Run:

```sh
python3 compute/verify_protected_integration_primitive_compatibility_obstruction.py \
  --fixture certificates/hybrid/protected_integration_primitive_compatibility --check
```

Expected status:

```text
PROTECTED_INTEGRATION_PRIMITIVE_COMPATIBILITY_VERIFIED
```
