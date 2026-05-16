# A228 -- Topological anchor postrepair verifier

## Findings

Two non-theorem-status issues remained:

- The quintic BCOV table anchor `244-256` included current \(n_{10}\)
  while claiming degree `1,...,9` only.
- A residual old range `762--769` remained in the MNOP/PT-DT anchor file.

## Integration

The main thread changed:

- `244-256` to `244-254` for the degree `1,...,9` BCOV-supported entries;
- `762--769` to `759--769`.

## Verification

`git diff --check` passed and stale-anchor `rg` returned no hits.
