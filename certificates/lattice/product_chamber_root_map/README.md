# Product-Chamber Root-Map Certificate

This packet records the finite arithmetic checks behind the type-II product
chamber and the root map used in the Delta_5 denominator identity.  It is a
target-side certificate: it checks the three Gamma_eff sectors, sector closure,
the map alpha(n,l,m)=2n f_2-l f_3+2m f_-2, the delta-basis formula
alpha=n delta_1+m delta_2+(n+m-l)delta_3, active support, inactive zero
exponents, and the doubled denominator convention Z -> 2Z.

It does not construct compact K3xE source representatives, Pfaffian
orientations, O2 wall charts, mirror-period discriminants, or protected traces.

Run:

```sh
python3 compute/verify_product_chamber_root_map_fixture.py --fixture certificates/lattice/product_chamber_root_map --check
```

Expected status:

```text
PRODUCT_CHAMBER_ROOT_MAP_VERIFIED
```
