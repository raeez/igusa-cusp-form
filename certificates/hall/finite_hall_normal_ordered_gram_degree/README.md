# finite_hall_normal_ordered_gram_degree

This packet records correction row 356.

It proves the relative normal-ordered Gram-degree statement for supplied
homogeneous Hall bracket rows: if the source bracket has degree
`chat + chat'` and `overlinePi_X` is additive, then the descended
fibre-summed bracket has degree `gamma + gamma'`.

The packet imports the existing finite
`hall_pairing_pushforward_compatibility` rows as formal supplied data.
Those rows are not compact `K3xE` source rows.  The current compact
source still has no degree rows, normal-ordered lift rows, product
matrix rows, primitive bracket rows, or row-356 degree-defect rows.

Run:

```sh
python3 compute/verify_finite_hall_normal_ordered_gram_degree.py \
  --fixture certificates/hall/finite_hall_normal_ordered_gram_degree --check
```

Expected status:

```text
FINITE_HALL_NORMAL_ORDERED_GRAM_DEGREE_OBSTRUCTION_VERIFIED
```
