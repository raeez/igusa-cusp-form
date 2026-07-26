# Source-Window Compact-Support Obstruction

This packet records the missing source-side data required for source
windows to exhaust compact support.

The target root-window packets prove the target statements

```text
union_nu W_nu = R_plus
Gamma(W_nu) = alpha^{-1}(W_nu)
```

but they do not supply compact K3xE source support.  This packet is
fail-closed: the core source tables remain empty, and the obstruction
ledger lists the rows required before compact-source support exhaustion
can be proved.

Run:

```sh
python3 compute/verify_source_window_compact_support_obstruction.py \
  --fixture certificates/sources/source_window_compact_support --check
```

Expected status:

```text
SOURCE_WINDOW_COMPACT_SUPPORT_OBSTRUCTION_VERIFIED
```
