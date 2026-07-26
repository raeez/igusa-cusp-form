# Wrapped/Wrapped Extension Admissibility

This packet records correction row 223.  It proves the target
admissibility needed for the Hall pushforward in the ordered
wrapped/wrapped correspondence:
\[
q^{WW}:
\mathfrak E^{WW}_{\eta_1,\eta_2;\zeta,R}
\longrightarrow
\mathcal M_{\zeta,R}^{\mathrm{wr,rig}}.
\]

For a target object \(B_\zeta\), the fibre of \(q^{WW}\) is the closed
relative Quot locus parametrising quotients
\(B_\zeta\twoheadrightarrow W_{\eta_1}\) whose kernel is
\(W_{\eta_2}\).  Relative Quot is projective over the wrapped target,
and the retained wrapped endpoint, colour, and finite-window
conditions are closed row conditions.  Hence \(q^{WW}\) is proper.

The source map is not asserted proper.  Over fixed endpoints its fibre
contains extension classes in
\(\operatorname{Ext}^1(W_{\eta_1},W_{\eta_2})\), modulo
automorphisms, and this fibre is nonproper in general.

This packet does not construct the compact-support exceptional
pushforward model, populated anchor memory, symmetric descent,
Thom--Sebastiani transport, quotient descent, transition
compatibility, or aggregate hybrid-carrier population.

Run:

```sh
python3 compute/verify_wrapped_wrapped_extension_admissibility_obstruction.py \
  --fixture certificates/hybrid/wrapped_wrapped_extension_admissibility --check
```

Expected status:

```text
WRAPPED_WRAPPED_ADMISSIBILITY_VERIFIED
```
