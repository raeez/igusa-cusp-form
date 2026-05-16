# A138 -- Target Fixture Scaffold Verifier

## Verdict

The A071 fixture is safe to cite in `main.tex` only as a target-only
fixture scaffold. It is not a compact/source verifier, source
PBW/no-extra theorem, finite reducer for blocked rows, or parity split
for blocked rows.

## Checks

- Python compile passed for `compute/build_target_presentation_fixture.py`
  and `compute/verify_square_root.py`.
- Fixture check passed for ten files.
- SHA-256 verification passed for all nine hashed payload files.
- `compute/verify_square_root.py` passed, including \(29|93\),
  \(m(\delta_1+\delta_2+\delta_3)=-93\), height-four gaps \(108|90|18\),
  and doubled isotropic gaps \(10|9|1\).

## Findings

The manifest is `target_only: true`, with compact-source firewall fields
false. The builder imports only stdlib modules and does not import the
source verifier or source packets.

Generated CSV counts:

- `target_degrees`: 16
- active parity rows: 12
- blocked rows: 4
- Hall basis rows: 426
- PBW rows: 16

The blocked set is exactly `2delta123`, `C_1_2`, `C_2_2`, `C_3_2`.
Blocked rows do not occur in `target_hall_lie_basis.csv`; in PBW they
occur only as blocked records with blank basis-vector counts and
`feeds_source_comparison=false`.

## Files Changed By Agent

None.
