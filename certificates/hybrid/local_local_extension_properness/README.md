# Local/Local Extension Target Properness

This packet records correction row 221.  It proves the properness
needed for the Hall pushforward in the ordered local/local
correspondence:
\[
q^{\mathrm{LL}}:
\mathfrak E^{\mathrm{LL}}_{\alpha,\beta;\gamma,R,I,J,K}
\longrightarrow
\mathfrak M^{\mathrm{loc,cl}}_{\gamma,R,K}.
\]

For a target object \(B_{\gamma,K}\), the fibre of \(q^{\mathrm{LL}}\)
is the closed locus in the relative Quot scheme parametrising
quotients \(B_{\gamma,K}\twoheadrightarrow A_{\alpha,I}\) whose kernel
has local colour \(\beta\) and closed support over \(E^J\).  Relative
Quot is projective; the local support and retained-colour conditions
are closed.  Hence \(q^{\mathrm{LL}}\) is proper.

The source map
\[
p^{\mathrm{LL}}:
\mathfrak E^{\mathrm{LL}}\to
\mathfrak M^{\mathrm{loc,cl}}_{\alpha,R,I}\times
\mathfrak M^{\mathrm{loc,cl}}_{\beta,R,J}
\]
is not asserted proper.  Its fibre over fixed endpoints contains
extension classes in \(\operatorname{Ext}^1(A_{\alpha,I},A_{\beta,J})\),
and is nonproper in general.

Run:

```sh
python3 compute/verify_local_local_extension_properness_obstruction.py \
  --fixture certificates/hybrid/local_local_extension_properness --check
```

Expected status:

```text
LOCAL_LOCAL_TARGET_PROPERNESS_VERIFIED
```
