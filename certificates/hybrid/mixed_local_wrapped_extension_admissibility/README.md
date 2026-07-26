# Mixed Local/Wrapped Extension Admissibility

This packet records correction row 222.  It proves the target
admissibility needed for the Hall pushforward in the one-sided mixed
correspondences:
\[
q^{LW}:
\mathfrak E^{LW}_{\alpha,\eta;\zeta,R,I}
\longrightarrow
\mathcal M_{\zeta,R}^{\mathrm{wr,rig}},
\qquad
q^{WL}:
\mathfrak E^{WL}_{\eta,\alpha;\zeta,R,I}
\longrightarrow
\mathcal M_{\zeta,R}^{\mathrm{wr,rig}}.
\]

For \(LW\), the fibre over a target object \(B_\zeta\) is the closed
relative Quot locus parametrising quotients
\(B_\zeta\twoheadrightarrow A_{\alpha,I}\) whose kernel is
\(W_\eta\).  For \(WL\), the quotient is
\(B_\zeta\twoheadrightarrow W_\eta\) and the kernel is
\(A_{\alpha,I}\).  Relative Quot is projective over the wrapped target,
and the retained local, wrapped, colour, and finite-window conditions
are closed row conditions.  Hence \(q^{LW}\) and \(q^{WL}\) are proper.

The source maps are not asserted proper.  Over fixed endpoints their
fibres contain extension classes in
\(\operatorname{Ext}^1(A_{\alpha,I},W_\eta)\) or
\(\operatorname{Ext}^1(W_\eta,A_{\alpha,I})\), modulo automorphisms,
and these fibres are nonproper in general.

This packet does not construct the compact-support exceptional
pushforward model, populated anchor memory, base change, the projection
formula, Thom--Sebastiani transport, quotient descent, transition
compatibility, or aggregate hybrid-carrier population.

Run:

```sh
python3 compute/verify_mixed_local_wrapped_extension_admissibility_obstruction.py \
  --fixture certificates/hybrid/mixed_local_wrapped_extension_admissibility --check
```

Expected status:

```text
MIXED_LOCAL_WRAPPED_ADMISSIBILITY_VERIFIED
```
