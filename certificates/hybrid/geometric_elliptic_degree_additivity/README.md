# Geometric Elliptic-Degree Additivity Obstruction

This packet records correction row 202.  The finite-stage assertion
\[
b_R^{\mathrm{geom}}(\gamma)
=b_R^{\mathrm{geom}}(\gamma')
+b_R^{\mathrm{geom}}(\gamma'')
\]
for a retained extension row
\[
0\to A_{\gamma'}\to A_\gamma\to A_{\gamma''}\to0
\]
is not a consequence of retained-extension closure alone.  It requires
rows identifying the retained extension pair, the three retained
one-cycle classes, additivity of those classes in \(N_1(K3\times E)\),
additivity after proper pushforward to \(N_1(E)\), equality of the
integer coefficients of \([E]\), and compatibility with finite-stage
transitions.

Run:

```sh
python3 compute/verify_geometric_elliptic_degree_additivity_obstruction.py \
  --fixture certificates/hybrid/geometric_elliptic_degree_additivity --check
```

Expected status:

```text
GEOMETRIC_ELLIPTIC_DEGREE_ADDITIVITY_OBSTRUCTION_VERIFIED
```

This status verifies the criterion row, imports the row-201 degree-map
definition packet and the retained-extension-closure packet, and records
the missing additivity rows fail-closed.  It is not a proof that the
current hybrid carrier has a populated additive degree map.
