# A219 -- Topological source-anchor repair follow-up

## Claim attacked

Stale `frontier_mnop_framing_volume.tex` line anchors survived in the
topological-strings source-anchor fixtures.

## Result

The worker repaired the two owned anchor files:

- `/Users/raeez/topological-strings/references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
- `/Users/raeez/topological-strings/references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`

Exact repairs reported:

- Quintic table anchor: `233-256` to `244-256`.
- MNOP status anchors: `762--769` and `761--769` to `759--769`.

## Verification

`git diff --check` and stale-anchor `rg` scans were clean in the owned
paths. A228 later narrowed the quintic degree `1,...,9` range to
`244-254` and normalized a remaining `762--769` occurrence.

## Residual obligation

No theorem status changed. The fixture still records missing HKQ/CDGP/GV
source obligations.
