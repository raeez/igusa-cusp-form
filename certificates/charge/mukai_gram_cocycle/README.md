# Mukai-Gram Cocycle Certificate

This packet records formal chart arithmetic for the Mukai-Gram map

```text
Pi_X(Q,P)=((Q,Q)/2, (Q,P), (P,P)/2)
```

and the symmetric bilinear polarization cocycle

```text
B(c,c')=((Q,Q'), (Q,P')+(Q',P), (P,P')).
```

The verifier uses the manuscript's Mukai sign convention on a rank-one
algebraic slice with pairing

```text
<(r,d,s),(r',d',s')> = 2dd' - rs' - r's.
```

It proves formal chart identities only.  It is not a finite HN charge
window and does not construct compact source representatives, source
Hall brackets, Pfaffian orientations, O2 wall atlases, mirror
discriminants, or protected traces.

Run:

```sh
python3 compute/verify_mukai_gram_cocycle_fixture.py \
  --fixture certificates/charge/mukai_gram_cocycle \
  --check
```

A positive result is `MUKAI_GRAM_COCYCLE_VERIFIED`.
