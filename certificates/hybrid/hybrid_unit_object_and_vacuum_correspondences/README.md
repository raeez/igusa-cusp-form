# hybrid_unit_object_and_vacuum_correspondences

This packet records row 241: the definition of units in the hybrid
local/wrapped factorization structure.

It supplies the local zero unit object and four split vacuum
correspondence types:

- `LL` left unit for local inputs;
- `LL` right unit for local inputs;
- `LW` left unit for wrapped inputs;
- `WL` right unit for wrapped inputs.

The packet is definition-only.  It does not prove the induced
compact-support pull-push maps are identity maps.  The local identity
law is recorded separately in
`certificates/hybrid/local_unit_compatibility`; the wrapped identity
law is recorded separately in
`certificates/hybrid/wrapped_unit_compatibility`.

Run:

```sh
python3 compute/verify_hybrid_unit_object_and_vacuum_correspondences_obstruction.py \
  --fixture certificates/hybrid/hybrid_unit_object_and_vacuum_correspondences --check
```
