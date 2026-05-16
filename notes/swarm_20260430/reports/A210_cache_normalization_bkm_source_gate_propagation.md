# A210 Cache Normalization/BKM-Source Gate Propagation

## Work Completed

Propagated the newest attack-heal lessons into
`~/calabi-yau-quantum-groups` cache files:

- AP-CY444: `\Delta_5` denominator exponents are not doubled K3
  elliptic-genus or `\Phi_{10}` square exponents.
- AP-CY445: scalar Schur/Humbert/BV/HCS characteristic data is not
  `H^2(\mathfrak g_{\Delta_5})`, BKM root-space recognition, or
  `\mathbf H_{\Delta_5}` recognition without source algebra, chain map,
  parity/supertrace, root labels, denominator comparison, and
  normalization.
- AP-CY446: a three-path verification cannot count a duplicate path.
- IC-86--IC-88 added to the first-principles cache and comprehensive
  cache with the same lessons.
- Canonical registry rows added in the anti-pattern catalogue.

## Anchors

- `~/calabi-yau-quantum-groups/notes/antipatterns_catalogue.md` around
  5695.
- `~/calabi-yau-quantum-groups/appendices/first_principles_cache.md`
  around 750.
- `~/calabi-yau-quantum-groups/notes/first_principles_cache_comprehensive.md`
  around 5355.

## Checks

- `git diff --check -- <three files>` clean.
- `git diff --cached --check -- <three files>` clean after staging.
- A210 staged only its three owned files.

## Status

Accepted as cache propagation. The staged CYQG cache files remain staged
as produced by the worker.

