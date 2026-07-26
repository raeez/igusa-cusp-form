# Target/Source Window Compatibility Obstruction

This packet records the missing compatibility data between target root
windows and compact source windows.

The target side supplies `W_nu` and `Gamma(W_nu)`.  The source side does
not yet supply compact-support source windows.  Compatibility requires a
row-level map from each compact source support row to a Gram degree
lying in `Gamma(W_nu)`, together with a zero compatibility defect and
transition compatibility.

Run:

```sh
python3 compute/verify_target_source_window_compatibility_obstruction.py \
  --fixture certificates/sources/target_source_window_compatibility --check
```

Expected status:

```text
TARGET_SOURCE_WINDOW_COMPATIBILITY_OBSTRUCTION_VERIFIED
```
