# A126 -- Source Fixture Verifier Scaffold

## Changed Paths

- `compute/verify_source_fixture.py`
- `certificates/sources/k3e_compact_hall/README.md`
- `certificates/sources/k3e_compact_hall/manifest.json`
- `certificates/sources/k3e_compact_hall/degrees.csv`
- `certificates/sources/k3e_compact_hall/parity_blocks.csv`
- `certificates/sources/k3e_compact_hall/basis_provenance.csv`
- `certificates/sources/k3e_compact_hall/M_entries.csv`
- `certificates/sources/k3e_compact_hall/D_entries.csv`
- `certificates/sources/k3e_compact_hall/B_entries.csv`
- `certificates/sources/k3e_compact_hall/G_entries.csv`
- `certificates/sources/k3e_compact_hall/K_entries.csv`
- `certificates/sources/k3e_compact_hall/Q_entries.csv`
- `certificates/sources/k3e_compact_hall/A_entries.csv`
- `certificates/sources/k3e_compact_hall/radical_ideal_coideal.csv`
- `certificates/sources/k3e_compact_hall/relation_rows.csv`
- `certificates/sources/k3e_compact_hall/no_extra.csv`
- `certificates/sources/k3e_compact_hall/pbw.csv`
- `certificates/sources/k3e_compact_hall/transitions.csv`
- `certificates/sources/k3e_compact_hall/a_beta_comparison_maps.csv`

## Commands

```text
python3 -m py_compile compute/verify_source_fixture.py
python3 compute/verify_source_fixture.py --source certificates/sources/k3e_compact_hall --target certificates/targets/delta5_gn_kac/a071_target_presentation --check
git diff --check -- compute/verify_source_fixture.py certificates/sources/k3e_compact_hall
```

The first and third commands passed. The verifier returned exit `1` with
expected fail-closed status `BLOCKED`.

## Fail-Closed Limitations

- `source_kind` is `mock_empty_blocked`, not `compact_source_candidate`.
- `certified` is not true.
- the packet is explicitly empty-blocked.
- the target fixture path did not exist and target truth was not
  generated.
- all required CSV gates are header-only: degrees, parity blocks,
  provenance, \(M,D,B,G,K,Q,A\), radical ideal/coideal, relation rows,
  no-extra, PBW, transitions/ML, and \(A_\beta\) intertwining equations.

The verifier is source-side only. It reads a target path as an external
reference and does not synthesize target parity, PBW ranks, basis labels,
or reducer output.
