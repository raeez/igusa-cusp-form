# Gram-Fibre Kernel Certificate

This packet records formal arithmetic for the Mukai--Gram map
`Pi_X(Q,P)=(Q^2/2,Q.P,P^2/2)`.

It checks that rows with the same Gram label are grouped before parity
is evaluated, that even and odd dimensions are recorded separately, and
that the zero Gram fibre is not an additive subgroup of the formal
charge lattice.

Run:

```
python3 compute/verify_gram_fibre_kernel_fixture.py --fixture certificates/charge/gram_fibre_kernel --check
```

Expected status:

```
GRAM_FIBRE_KERNEL_VERIFIED
```

The packet is formal lattice and bookkeeping arithmetic only.  It does
not prove finite HN boundedness, compact Hall support, source Hall
brackets, source parity certification, Hopf radical ideal/coideal
properties, exactness of a pushforward, Pfaffian orientations, or
protected traces.
