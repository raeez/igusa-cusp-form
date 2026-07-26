# Formal Primitive Lift Certificate

This packet records the formal lattice formula

```
Q = e1 + n f1
P = l f1 + e2 + m f2
```

inside two orthogonal hyperbolic planes with `(e_i,f_i)=1`.  It verifies
`Pi_X(Q,P)=(n,l,m)`, the primitive `e1,e2` minor, wedge torsion one, and
the target grading `alpha(Pi_X(Q,P))=(2n,-l,2m)` on the listed rows.

Run:

```
python3 compute/verify_formal_primitive_lift_fixture.py --fixture certificates/charge/formal_primitive_lift --check
```

Expected status:

```
FORMAL_PRIMITIVE_LIFT_VERIFIED
```

The packet is formal lattice arithmetic only.  It does not prove algebraic
effectivity, finite HN boundedness, compact Hall support, source Hall brackets,
Pfaffian orientations, O2 wall atlases, mirror discriminants, or protected
traces.
