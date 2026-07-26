# PBW Pushforward Certificate

This packet records the finite filtered-vector-space statement that
pushforward along the additive normal-ordered Gram grading preserves a
supplied PBW filtration and its finite associated graded.

Run:

```
python3 compute/verify_pbw_pushforward_fixture.py --fixture certificates/charge/pbw_pushforward --check
```

Expected status:

```
PBW_PUSHFORWARD_VERIFIED
```

The packet does not prove the compact-source PBW comparison, target PBW
comparison, no-extra relations, primitive recognition, Pfaffian
orientations, or protected traces.
