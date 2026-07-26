# Local/Local Correspondence Definition

This packet records correction row 210. At finite HN height \(R\), the
local/local correspondence is the ordered projection-finite extension
diagram
\[
\mathfrak E^{\mathrm{LL}}_{\alpha,\beta;\gamma,R,I,J,K}
\xrightarrow{p^{\mathrm{LL}}}
\mathfrak M^{\mathrm{loc,cl}}_{\alpha,R,I}
\times
\mathfrak M^{\mathrm{loc,cl}}_{\beta,R,J},
\qquad
\mathfrak E^{\mathrm{LL}}_{\alpha,\beta;\gamma,R,I,J,K}
\xrightarrow{q^{\mathrm{LL}}}
\mathfrak M^{\mathrm{loc,cl}}_{\gamma,R,K},
\]
where \(\alpha:I\to\Gamma_R^{\mathrm{loc}}\),
\(\beta:J\to\Gamma_R^{\mathrm{loc}}\),
\(\gamma=|\alpha|+|\beta|\in\Gamma_R^{\mathrm{loc}}\), and
\(K=I\sqcup J\) modulo the ordinary Ran collision maps. It classifies
extensions
\[
0\to A_{\beta,J}\to B_{\gamma,K}\to A_{\alpha,I}\to0.
\]

This packet only defines the local/local correspondence type. It is not
the mixed correspondence, not the wrapped/wrapped correspondence, not
the two-sided mixed correspondence, not a wrapped carrier, not a
properness theorem, and not a scalar trace substitute.

Run:

```sh
python3 compute/verify_local_local_correspondence_definition_obstruction.py \
  --fixture certificates/hybrid/local_local_correspondence_definition --check
```

Expected status:

```text
LOCAL_LOCAL_CORRESPONDENCE_DEFINITION_VERIFIED
```

This status verifies the typed definition row and records the missing
extension-stack, source/target-map, descent, properness,
Thom--Sebastiani, collision-compatibility, and transition rows
fail-closed.  Target-properness of the \(LL\) Hall map is separated in
`certificates/hybrid/local_local_extension_properness`; source
properness is not asserted there.
