# A097 target-presentation computation spec

No files edited. `python3 compute/verify_square_root.py` passed.

## Computation target

Add a target-only reducer, separate from source verification:

```text
compute/build_target_presentation_fixture.py
```

It should consume arithmetic helpers from `compute/verify_square_root.py`
but not live inside the coefficient script. Output should live under:

```text
certificates/targets/delta5_gn_kac/a071_target_presentation/
```

with `manifest.yaml`, `target_degrees.csv`,
`target_simple_generators.csv`, `target_hall_lie_basis.csv`,
`target_relation_rows.csv`, `target_pairing_blocks.csv`,
`target_radicals.csv`, `target_dimensions.csv`, `target_pbw.csv`, and
hashes.

## Inputs

Use the imported GN/Kac target presentation:

- real even simples \(\delta_1,\delta_2,\delta_3\) with the manuscript
  Gram matrix;
- isotropic simples \(u_{ij,t,r}\) in degree \(t a_{ij}\), \(r=1,\ldots,9\),
  even, from the GN \(\tau(t a)=9\) row;
- timelike simples from \(m(\beta)\), even when \(m(\beta)>0\), odd when
  \(m(\beta)<0\);
- full target algebra as the BK free Lie quotient by
  \(J_{\mathrm{BK}}+\operatorname{Rad}_{\mathrm{GN}}\).

For \(C_{k,2}\), use the full downward closure of \(a_{ij}+2\delta_k\).
For \(2\delta_{123}\), use all \(0<\beta\le(2,2,2)\), not merely the
relation-minimal A071 packet.

## Expected invariants

| row | invariant |
|---|---|
| \(2a_{ij}\) | \(\smult=10\), isotropic simple \(9|0\), affine residual \(1|0\), hence \(10|0\). |
| \(C_{k,2}\) | \(\|\beta\|^2=-8\), \(\smult=108\), simple block \(90|0\); expected \(201|93\) only after the reducer proves the 93 odd string survives the radical quotient. |
| \(2\delta_{123}\) | \(\|\beta\|^2=-24\), \(\smult=4016\), simple block \(0|540\); output exact \(E|O\) with \(E-O=4016\), \(O\ge540\), and all auxiliary rows present. |

The manuscript proof should be a short target-presentation proposition,
with implementation/schema in `certificates/README.md`, not `main.tex`.

