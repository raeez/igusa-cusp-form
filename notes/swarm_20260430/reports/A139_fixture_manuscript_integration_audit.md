# A139 -- Fixture Manuscript Integration Audit

## Result

Minimal integration requires four short insertions in `main.tex`, with
no theorem statement changes.

## Proposed Insertions

- Primitive-recognition proof ledger: state that the target packet is
  checked by `compute/build_target_presentation_fixture.py --check` and
  records target rows only; the source packet is fail-closed and in its
  current `mock_empty_blocked` state certifies no compact Hall stage.
- A071 target rows: cite the target-only certificate and record that
  \(2a_{ij}:10|0\), \(C_{k,3}:29|93\), \(C_{k,4}:10|0\), and
  \(C_{k,5}:0|0\) are active target parity rows, while \(C_{k,2}\) and
  \(2\tau_{123}\) are `signed_only_blocked`.
- Finite compact-source provenance gate: state that the fail-closed
  source verifier is the executable form of the gate and accepts only
  certified compact-source candidates with populated verified source
  tables.
- Source matrix criterion: state that `compute/verify_source_fixture.py`
  checks whether a supplied packet contains the source-side data named in
  the theorem and that the current packet is a negative fixture, not
  evidence for primitive recognition.

## Files Changed By Agent

None.
