# Fibre Pushforward Exactness Certificate

This packet records the finite linear algebra behind the formal
fibre-summed Gram pushforward.  It checks exact sequences of finite
vector spaces in each displayed Gram/parity block, verifies that finite
direct sums preserve exactness, and defines the zero-fibre radical as
the kernel of a finite pairing matrix.

Run:

```
python3 compute/verify_fibre_pushforward_exactness_fixture.py --fixture certificates/charge/fibre_pushforward_exactness --check
```

Expected status:

```
FIBRE_PUSHFORWARD_EXACTNESS_VERIFIED
```

The packet is finite linear algebra only.  It does not prove finite HN
boundedness, compact Hall support, source Hall brackets, Hopf
ideal/coideal closure of the radical, exact Hall pushforward,
bar-construction commutation, Pfaffian orientations, or protected
traces.
