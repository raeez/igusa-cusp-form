# type_ii_weyl_vector

This fixture records the target-side type-II BKM lattice arithmetic used
by the \(\Delta_5\) denominator:

- simple roots
  \(\delta_1=2f_2-f_3\), \(\delta_2=2f_{-2}-f_3\),
  \(\delta_3=f_3\);
- Cartan matrix \(4I_3-2J_3\);
- discriminant \(-32\);
- explicit isometry
  \(\Lambda_{II}^{2,1}\simeq U(4)\oplus\langle2\rangle\) via
  \(\delta_1+\delta_3,\delta_2+\delta_3,\delta_3\);
- Weyl vector
  \(\rho=\frac12(\delta_1+\delta_2+\delta_3)
  =f_2-\frac12f_3+f_{-2}\);
- \((\rho,\delta_i)=-1\), \((\rho,\rho)=-3/2\), and
  \(\rho\in(\Lambda_{II}^{2,1})^\vee\).

The packet is lattice arithmetic only.  It does not construct compact
source representatives, Pfaffian orientations, O2 wall atlases, mirror
discriminants, or protected traces.

Run:

```sh
python3 compute/verify_type_ii_weyl_vector_fixture.py \
  --fixture certificates/lattice/type_ii_weyl_vector \
  --check
```

A positive result is `TYPE_II_WEYL_VECTOR_VERIFIED`.
