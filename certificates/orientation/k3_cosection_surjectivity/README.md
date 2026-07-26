# k3_cosection_surjectivity

This packet is the fail-closed ledger for optimization row 274:
surjectivity of the K3 semiregularity cosection on retained strata.

It records the precise criterion: after a retained stratum has a
nonzero K3-class witness \(\beta_{R,c}\ne0\), an identification with
the reduced DT/PT nonzero-K3-class branch, and a cokernel-rank-zero
row, Maulik--Toda and Oberdieck supply the pointwise surjectivity
input.  Those witness rows are not present in the current retained
finite tables.

Run:

```sh
python3 compute/verify_k3_cosection_surjectivity_obstruction.py \
  --fixture certificates/orientation/k3_cosection_surjectivity --check
```

Expected status:

```text
K3_COSECTION_SURJECTIVITY_OBSTRUCTION_VERIFIED
```

This status is not a proof of surjectivity.  It certifies that the
missing mathematical data are named and that the core surjectivity
tables remain empty.
