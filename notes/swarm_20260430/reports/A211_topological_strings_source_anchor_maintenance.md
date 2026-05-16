# A211 Topological Strings Source-Anchor Maintenance

## Claim Attacked

A206 found line-stale source-gate anchors in topological-strings after
`frontier_mnop_framing_volume.tex` moved.

## Patch

- `~/topological-strings/references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  now has current anchors for the `N=10` table, `a_N` values, tail fit,
  raw period formula/arithmetic, BCOV/GV rows, and claim-to-source map.
- `~/topological-strings/references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  now has current MNOP/PT/DT anchors and preserves the missing
  CoHA/centre source status.
- `frontier_mnop_framing_volume.tex` was not edited by A211.

## Checks

- Targeted `rg` for old stale ranges: no matches.
- `git diff --check` on owned files passed.
- `git diff --cached --check` on owned files passed.

## Open Obligations

HKQ `N=10`, CDGP period convention, OSV rate, GV/conifold-resurgence
sources, Abel-Jacobi normalization, and compact chain-level
`C_tar`/CoHA/centre data remain missing-source obligations. Finite
quintic evidence remains conditional/proposition-level, not theorem
import.

