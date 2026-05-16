# A201 Vol II BV/BRST Local-Summand Gate Patch

## Claim Attacked

`~/chiral-bar-cobar-vol2/chapters/connections/bv_brst.tex` asserted
that the 24 local BV/HCS obstruction summands are BKM root-space
multiplicities `c(n,\ell)` and the BV origin of
`\mathbf H_{\Delta_5}`.

## Patch

The remark at `bv_brst.tex` around 5381 now states only a scalar or
supertrace obstruction target. It explicitly denies that the local
summands are identified with root spaces of
`\mathfrak g_{\Delta_5}` or that they construct
`\mathbf H_{\Delta_5}` without further data.

The upgrade criterion now lists the required source BV/HCS chain map,
parity/superdimension convention, root labels, denominator-identity
comparison, and normalization.

## Checks

- Targeted `rg` over BKM/root-space/supertrace/upgrade/normalisation
  terms.
- `git diff --check -- chapters/connections/bv_brst.tex`.

## Status

Accepted as a conditional comparison target. Follow-up Vol II static
verification delegated to A205.

