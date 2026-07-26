# Geometric Elliptic-Degree Map Obstruction

This packet fixes the definition of the finite-stage geometric
elliptic-degree map.  For a retained HN numerical class \(\gamma\), let
\(\operatorname{cyc}_1(\gamma)\in N_1(K3\times E)\) be the numerical
one-cycle obtained from the codimension-two Chern character component.
Since \(N_1(E)=\mathbb Z[E]\), define
\[
(p_E)_*\operatorname{cyc}_1(\gamma)
=b_R^{\mathrm{geom}}(\gamma)[E],
\qquad
b_R^{\mathrm{geom}}(\gamma)\in\mathbb Z_{\ge0}.
\]

Run:

```sh
python3 compute/verify_geometric_elliptic_degree_map_obstruction.py \
  --fixture certificates/hybrid/geometric_elliptic_degree_map --check
```

Expected status:

```text
GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED
```

This status verifies the definition row and the obstruction ledger.  It
does not supply retained HN class rows, one-cycle rows, pushforward rows,
local/wrapped split rows, transition rows, or row-202 additivity rows.
The row-202 criterion and its fail-closed ledger live in
`certificates/hybrid/geometric_elliptic_degree_additivity`.
The row-203 separation from the Borcherds trace coordinate lives in
`certificates/hybrid/geometric_borcherds_degree_separation`.
The row-204 positive-degree projection theorem lives in
`certificates/hybrid/positive_elliptic_degree_projection`.
