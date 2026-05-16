# A133 -- Source Fixture Scaffold Verifier

## Result

The scaffold is safe to cite as a blocked source verifier scaffold, not
as a compact Hall source certificate.

## Findings

The verifier is fail-closed: any issue returns `BLOCKED` and exit code
`1`. The current fixture is intentionally blocked by
`source_kind: mock_empty_blocked`, `certified: false`,
`empty_blocked: true`, and header-only CSVs.

Schema coverage is complete for the scaffold: sixteen CSV gates exist
with matching headers for degrees, parity, provenance, \(M,D,B,G,K,Q,A\),
radical, relation rows, no-extra, PBW, transitions, and \(A_\beta\).
No subdirectories or unexpected files were present inside the source
fixture directory.

The target/source firewall is present at scaffold level: target labels
are rejected outside allowed target columns, and the verifier does not
read or derive target truth.

## Hardening Caveats

Future certifying use should harden target validation because the
initial scaffold did not type-check the target fixture or forbid
`--target == --source`. The `--check` flag was parsed but did not have a
distinct role beyond the verifier's fail-closed default.

These hardening items are assigned to A140.

## Files Changed By Agent

None.
