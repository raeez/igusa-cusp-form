# rhomred_weyl_wall_transport_tau

This packet verifies row 306 as a criterion and obstruction ledger:
constructing Weyl wall transports
\(\tau_{i,R,S}:o_{R,S}\to s_{\delta_i}^*o_{R,s_{\delta_i}S}\)
requires source and target orientation lines, retained type-II wall
objects, determinant-square compatibility, and transport of the full
quotient-orientation cocycle.  The condition \(\tau_i^2=1\) is row 307
and is not certified here.

The type-II target generators and quotient wall profiles are available.
The source orientation-line, wall-object, and Weyl-lift tables remain
empty.

Run:

```sh
python3 compute/verify_rhomred_weyl_wall_transport_tau.py \
  --fixture certificates/orientation/rhomred_weyl_wall_transport_tau --check
```
