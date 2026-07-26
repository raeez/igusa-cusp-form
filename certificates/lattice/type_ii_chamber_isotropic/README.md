# Type-II Chamber Isotropic Certificate

This packet records finite target-side arithmetic for the type-II chamber of
the Delta_5 BKM denominator.  It checks the type-I/type-II divisibility split,
the three type-II Coxeter generators, the absence of finite braid relations
among distinct type-II simple generators, the S3 chamber automorphisms, the
three primitive isotropic rays a_ij=delta_i+delta_j, the multiplicity
10=1+9, and the nine Gritsenko--Nikulin isotropic directions on each ray.

It is not a compact K3xE source construction and does not supply Pfaffian
orientations, O2 wall charts, mirror discriminants, protected traces, or
target parity decompositions.

Run:

```sh
python3 compute/verify_type_ii_chamber_isotropic_fixture.py --fixture certificates/lattice/type_ii_chamber_isotropic --check
```

Expected status:

```text
TYPE_II_CHAMBER_ISOTROPIC_VERIFIED
```
