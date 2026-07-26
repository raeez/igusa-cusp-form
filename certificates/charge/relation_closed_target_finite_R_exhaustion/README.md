# Relation-Closed Target Finite-R Exhaustion Obstruction

This packet records the missing data required to prove that every
relation-closed target degree appears in a finite test window
\(\Gamma_R^{\mathrm{test}}\).

The target side is not the obstruction: the finite
`wrel_degree_closure` packet records the finite closure cascade through
the 645-row prefix, and the `wrel_tail_staircase` packet proves the
symbolic tail \(A_N\to B_N\to A_{N+2}\) for every even \(N\ge14\).
The missing step is the HN-stage realization.  For each finite target
degree and for each symbolic tail family one must supply a finite
height \(R\), a charge \(c\in\Gamma_R^{HN}\), a translate
\(T\in\mathcal T_R(c)\), and the equality
\[
\Pi_X(c)+T=\gamma .
\]

Run:

```sh
python3 compute/verify_relation_closed_target_finite_R_exhaustion_obstruction.py \
  --fixture certificates/charge/relation_closed_target_finite_R_exhaustion --check
```

Expected status:

```text
RELATION_CLOSED_TARGET_FINITE_R_EXHAUSTION_OBSTRUCTION_VERIFIED
```

This status verifies the obstruction ledger and the imported target
packets.  It does not prove finite-\(R\) exhaustion.
