# type_i_false_wall_exclusion

This packet records correction row 270: no false type-I wall enters the
type-II hybrid wall-profile inlet.

The proof is at profile level.  It imports the lattice packet where
`eta_12`, `eta_13`, and `eta_23` are the type-I chamber-automorphism
roots: ambient divisibility one, zero Delta5 divisor support, and zero
Delta5 divisor order.  It imports the hybrid operation-recovery packet
where only `delta_1`, `delta_2`, and `delta_3` enter as type-II wall
profiles, and the E-quotient survival packet where exactly those wall
profiles survive quotient-after-correspondence.

The packet does not populate the aggregate hybrid carrier, prove global
colour exhaustion, construct retained wall objects, supply nonzero
quotient cycles or coefficient descent, or insert rows into the O2 wall
atlas.

Verify with:

```bash
python3 compute/verify_type_i_false_wall_exclusion_fixture.py \
  --fixture certificates/hybrid/type_i_false_wall_exclusion --check
```
