# Liu Product-Stability Definition Certificate

This packet records the Liu product-stability datum used on
`S x E`.  Starting from a rational stability condition
`sigma_S=(A_S,Z_S)` on `D^b Coh(S)`, it defines the
Abramovich--Polishchuk global heart `A_E^{AP}`, the polynomial
`L_M(n)=a(M)n+b(M)+i(c(M)n+d(M))`, the weak charge
`Z_t=a*t-d+i*c*t`, the torsion-pair tilt
`A_E^t=<T_t,F_t[1]>`, and the product central charge
`Z_E^{s,t}=c*s+b+i(-a*t+d)`.

Run:

```
python3 compute/verify_liu_product_stability_fixture.py --fixture certificates/moduli/liu_product_stability --check
```

Expected status:

```
LIU_PRODUCT_STABILITY_DEFINED
```

This is a definition/source-import packet.  It is not the separate
AP-compatibility theorem and not a finite-moduli construction.
