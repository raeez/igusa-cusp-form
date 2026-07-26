# Geometric/Borcherds Degree Separation Obstruction

This packet records correction row 203.  The finite-stage geometric
elliptic-degree map
\[
b_R^{\mathrm{geom}}(\gamma)
=\operatorname{coeff}_{[E]}(p_E)_*\operatorname{cyc}_1(\gamma)
\]
is not the Borcherds trace coordinate
\[
m_R^{\mathrm{Bch}}(\widehat\gamma)
=\operatorname{pr}_3\overline\Pi_X(\widehat\gamma).
\]
The first map is a support degree in \(N_1(E)=\mathbb Z[E]\) and is
used before forming the local/wrapped hybrid carrier.  The second is
the third normal-ordered Gram coordinate and grades protected
integration after \(\overline\Pi_X\)-descent.  A formula relating them,
for example on a rank-one Oberdieck--Pandharipande branch, is allowed
only after a branch-comparison datum has been supplied.

Run:

```sh
python3 compute/verify_geometric_borcherds_degree_separation_obstruction.py \
  --fixture certificates/hybrid/geometric_borcherds_degree_separation --check
```

Expected status:

```text
GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED
```

This status verifies the separation ledger and firewall.  It does not
populate a branch comparison between \(b_R^{\mathrm{geom}}\) and
\(m_R^{\mathrm{Bch}}\).
