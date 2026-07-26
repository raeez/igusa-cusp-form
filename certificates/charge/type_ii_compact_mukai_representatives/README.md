# Type-II compact Mukai representatives

This packet verifies row 266 of the optimization ledger: compact
representatives for the three target wall charges in the K3 Mukai chart.
It uses the convention

```text
v(E)=ch(E) sqrt(td(S)),  sqrt(td(S))=(1,0,1)
<(r,d,s),(r',d',s')> = 2dd' - rs' - r's.
```

For a point `p` on a smooth projective K3 surface and a length-two
zero-dimensional subscheme `Z`, the representative pairs are

```text
x_delta1 = (I_Z, I_p),  Pi_X=(1,1,0)
x_delta2 = (I_p, I_Z),  Pi_X=(0,1,1)
x_delta3 = (I_p, O_p),  Pi_X=(0,-1,0)
```

The packet imports the formal Mukai--Gram cocycle packet and the
type-II target wall-image packet.  It does not supply retained HN
semistability, a compact Hall source basis, reduced orientations,
vanishing-cycle summands, E-quotient data, O2 wall charts, Pfaffian
signs, or protected integration.
