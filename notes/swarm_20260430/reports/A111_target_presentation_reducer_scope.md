# A111 -- Target Presentation Reducer Scope

## Claim Attacked

The A071 target parity rows need an implementation path that does not
collapse coefficient extraction, target presentation reduction, and
compact source verification.

## Worker Package

Recommended ownership:

- `compute/build_target_presentation_fixture.py`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/manifest.yaml`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/hashes.sha256`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_degrees.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_simple_generators.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_hall_lie_basis.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_relation_rows.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_pairing_blocks.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_radicals.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_dimensions.csv`
- `certificates/targets/delta5_gn_kac/a071_target_presentation/target_pbw.csv`

Not owned by this worker package: `main.tex`, `proj.bib`, `notes/**`,
`certificates/README.md`, or any compact source fixture.

## CLI Contract

```text
python3 compute/build_target_presentation_fixture.py --out certificates/targets/delta5_gn_kac/a071_target_presentation --force
python3 compute/build_target_presentation_fixture.py --out certificates/targets/delta5_gn_kac/a071_target_presentation --check
```

## Verification Contract

- `python3 compute/verify_square_root.py`
- Python byte-compilation of the reducer
- fixture build and fixture check
- `shasum` comparison against `hashes.sha256`
- `git diff --check`
- firewall grep proving the reducer does not import compact source
  packets or source verifier truth.

## Files Changed By Agent

None.
