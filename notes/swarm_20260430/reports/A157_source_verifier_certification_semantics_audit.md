# A157 -- Source Verifier Certification Semantics Audit

## Finding

The source verifier's positive status `CERTIFIED` was too strong. A
future all-dummy packet could pass schema, status, payload, and label
checks without exact scalar parsing, matrix identities, radical ranks,
no-extra, PBW, transition, or \(A_\beta\) intertwining verification.

## Recommendation

Use `schema_complete` / `SCHEMA_COMPLETE` for the present verifier's
positive result. Reserve `externally_verified` or `certified` for a
future proof-mode verifier with checked mathematical artifacts, hashes,
and run metadata.

## Manuscript Implication

The manuscript should describe `compute/verify_source_fixture.py` as an
executable schema/status/payload gate, not compact-source
certification. The theorem may still require a certified compact Hall
source; the current script is not that certification.

## Follow-Up

The semantics patch is assigned to A160.

## Files Changed By Agent

None.
