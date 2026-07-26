# Pairing Kernel lim1 Vanishing Obstruction

This packet records the missing data required to prove that
\(R^1\varprojlim\) vanishes on the kernels of the finite
positive-negative Hopf-pairing maps used in primitive recognition.

For each cofinal finite root window, each retained Gram degree, and each
parity, one must construct the finite Hopf-pairing matrix, the left and
right kernel spaces, bases for those kernels, restricted transition
maps between the kernels, identity and composition rows, and an explicit
Mittag-Leffler image-stabilization witness.  A pairing matrix, a rank
equality, primitive-space Mittag-Leffler exactness, radical-transition
preservation, or non-degeneracy after quotient does not by itself prove
that the pairing-kernel tower has \(R^1\varprojlim=0\).

Run:

```sh
python3 compute/verify_pairing_kernel_lim1_vanishing_obstruction.py \
  --fixture certificates/hall/pairing_kernel_lim1_vanishing --check
```

Expected status:

```text
PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED
```

This status is not a proof that \(R^1\varprojlim\) vanishes on pairing
kernels.  It only certifies that the obstruction ledger is complete
while the core pairing-kernel and Mittag-Leffler tables remain empty.
