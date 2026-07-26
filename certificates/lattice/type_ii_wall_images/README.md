# Type-II wall images

This packet records correction rows 263--265.  It computes the inverse
image of the three simple type-II roots under the product-chamber root
map
\[
\alpha(n,l,m)=n\delta_1+m\delta_2+(n+m-l)\delta_3.
\]

The certified images are
\[
\gamma_{\mathrm{wall}}(\delta_1)=(1,1,0),\qquad
\gamma_{\mathrm{wall}}(\delta_2)=(0,1,1),\qquad
\gamma_{\mathrm{wall}}(\delta_3)=(0,-1,0).
\]

This is target-side lattice arithmetic.  It does not construct compact
\(K3\times E\) representatives, retained wall objects, O2 wall charts,
Pfaffian orientations, protected traces, or Hall carrier data.

Run:

```sh
python3 compute/verify_type_ii_wall_images_fixture.py \
  --fixture certificates/lattice/type_ii_wall_images --check
```

Expected status:

```text
TYPE_II_WALL_IMAGES_VERIFIED
```
