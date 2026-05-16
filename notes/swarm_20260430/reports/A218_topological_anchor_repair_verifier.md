# A218 -- Topological strings anchor repair verifier

## Claim attacked

Topological-strings source-anchor documents needed verification after
recent frontier edits.

## Findings

Fatal: none.

High:

- `/Users/raeez/topological-strings/references/primary-sources/quintic-bcov-gv-source-anchors-2026-04-30.md`
  contains stale internal line anchors. Examples reported:
  `frontier:524-533` for a BCOV framework now beginning around
  `frontier_mnop_framing_volume.tex:542`; table ranges beginning around
  `227` where the current finite table starts around `244`; a range
  ending at `253` omitting current \(n_9,n_{10}\) data around `254`.
- `/Users/raeez/topological-strings/references/primary-sources/mnop-pt-dt-source-anchors-2026-04-30.md`
  contains stale line anchors. Examples reported: `68--70` now points
  into theorem-grade non-import prose; `743--748` misses the current
  status summary around `759`; `787--801` misses current restrictions
  around `809`.

Medium:

- The firewall anchor range should include the current guardrail line
  around `68`.

## Files changed by agent

None. A219 was launched as the bounded follow-up repair worker for the
two anchor markdown files.

## Verification

A218 performed line-anchor inspection against the current frontier file.

## Residual obligation

Repair only the stale internal anchors. Do not change theorem strength
or conditional/proved status in the topological-strings manuscript.
