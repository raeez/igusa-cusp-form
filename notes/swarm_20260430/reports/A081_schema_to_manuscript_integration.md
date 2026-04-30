# A081 - Schema-to-Manuscript Integration

Used `chriss-ginzburg-rectify`; no edits, no reverts by the agent.

## Decision

A067/A072 as CSV/verifier schema belongs in a standalone
`certificates/README.md` plus `certificates/schemas/`, not in `main.tex`
and not in a manuscript appendix.

`main.tex` should contain the mathematical certificate interface: finite
window `W`, source spaces `P^X_{R,\beta,\bar p}`, source provenance,
matrices `M,D,B,G,K,Q`, maps `A_{\beta,\bar p}`, relation rows, NO7
radical descent, no-extra kernel equality, PBW associated-graded
comparison, and strict transition/ML conditions. It should not contain
file names, CSV headers, JSON outputs, failure codes, or directory
layout.

## Manuscript Plan

Keep the standalone logic in these existing anchors:

- Primitive recognition theorem: `main.tex` near line 12491.
- Cofinal finite-window datum: `main.tex` near line 12853.
- Source matrices: `main.tex` near line 13841.
- Comparison maps `A_{\gamma,\bar p}`: `main.tex` near line 14017.
- `W_{\le3}` first-window criterion: `main.tex` near line 15011.
- Finite source matrix criterion: `main.tex` near line 15275.
- NO7 protocol: `main.tex` near line 15380.

Add only a short mathematical statement when integrating: "A populated
finite source certificate for `W` is a finite exact model of
Definition/Theorem X satisfying clauses ...". No CSV vocabulary.

Appendix, if used, should be a one-page mathematical checklist, not the
schema: "Certificate clauses and proof role." It may tabulate radical
descent, relation containment, no-extra, PBW, transition/ML, each as a
mathematical assertion. It should not list `manifest.yaml`, `degrees.csv`,
or column names.

`certificates/README.md` should receive the A067/A072 implementation
layer: directory layout, schemas, exact scalar encoding, source-target
firewall, verifier gates, expected failures, hashes, and `verifier.json`
/ `verifier-summary.tex` conventions.

## Status

There is currently no `certificates/` directory and no populated source
fixture. Target arithmetic scripts pass: lattice checks, `29|93`,
height-four `108|90|18`, doubled isotropic `10|9|1`, Serre exponents
`3,5`. That verifies target arithmetic only; it does not supply compact
source matrices or a recognition proof.

