# A080 - A071 Target Fixture Arithmetic Design

No files edited or reverted by the agent.

## Verdict

A071 target fixture generation must separate three layers:

1. `smult(beta)=f(nm,l)` from the Borcherds product.
2. GN simple-root data: `m(a)` for timelike chamber roots, `tau(ta)=9`
   on isotropic rays.
3. Full GN/Kac root-space parity `d_0|d_1`, obtained only from the
   Borcherds-Kac presentation, Weyl transport, PBW/radical quotient, or
   an explicit finite target computation.

`f(nm,l)` never determines `d_0|d_1`.

## A071 Target Rows

Use `gamma(c1,c2,c3)=(c1,c1+c2-c3,c2)`.

| Degree | Current arithmetic | Fixture status |
|---|---:|---|
| `delta_i` | `f=1` | known GN/Kac: `1|0` |
| `a_ij` | `f=10`, `tau=9` | known GN/Kac: `10|0 = E_ij + 9u_ij,r` |
| `2delta_i+delta_j` | `f=1` | known Kac real-string: `1|0` |
| `tau` | `f=-64`, `m=-93` | known presentation count: `29|93` |
| `3delta_i+delta_j` | `f=0` | known real-Serre terminal: `0|0` |
| `2a_ij` | `f=10`, `tau(2a)=9`, residual `1` | should be target-computed or cited as rank-two Kac affine residual; do not infer from `f` |
| `C_{k,2}` | `f=108`, `m=90`, residual `18` | full parity not currently known from product; needs finite GN/Kac target computation |
| `C_{k,3}` | `f=-64` | known if Weyl transport is admitted: `C_{k,3}=s_k(tau)`, hence `29|93`; not from product |
| `C_{k,4}` | `f=10` | known if Weyl transport is admitted: `C_{k,4}=s_k(a_ij)`, hence `10|0`; also receives the zero row for the `tau`-string terminal relation |
| `C_{k,5}` | `f=0` | terminal complementary-string row; record zero relation, and separately justify `0|0` by GN/Kac root support, not by product alone |
| `2tau` | `f(4,2)=4016`, `m(2tau)=-540` | full parity unknown; `m=-540` gives 540 odd simple generators, not the full root space |

The correction to A071 is mainly `C_{k,3}` and `C_{k,4}`: they are not
signed-only once the fixture imports the real Weyl action. They should be
populated by Weyl transport from `tau` and `a_ij`, with
parity-preserving real reflections. `2tau` remains genuinely
presentation-required.

## Required Fixture Design

Add target-side fields:

```text
beta, gamma, height, norm, smult, chamber_rep, weyl_word,
simple_even, simple_odd, full_even, full_odd, parity_source,
citation, computation_hash
```

Allowed `parity_source` values:

```text
gn_kac_base
weyl_transport
serre_zero
target_presentation_computed
signed_only_blocked
```

Rows marked `signed_only_blocked` cannot feed `target_basis.csv`,
`target_pbw.csv`, or source comparison maps.

## Required Computations

- Existing arithmetic: `compute/verify_square_root.py` verifies `29|93`,
  height-four `108|90|18`, doubled isotropic `10|9|1`,
  `m(2tau)=-540`.
- Add a Weyl reducer: prove `s_k(tau)=C_{k,3}` and `s_k(a_ij)=C_{k,4}`
  using the Gram matrix.
- Add a finite GN/Kac presentation reducer for `C_{k,2}`, `2a_ij` if not
  cited, and `2tau`: free Lie superalgebra, BK relations, GN radical,
  PBW associated graded, exact parity dimensions.
- Keep relation rows separate from dimension rows. `C_{k,4}` is nonzero
  `10|0` even though the `tau`-string terminal map into it is zero.

## Primary Citations and Anchors

Primary citations: GN correction algebra and imaginary data; GNII
product/coefficient machinery; Borcherds 1988 GKM presentation; Kac
real-root/Weyl/PBW conventions.

Local anchors: `main.tex` near lines 5818, 14917, 15170, and 15305.

