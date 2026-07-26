# Bar Pushforward Commutation Certificate

This packet records the finite tensor-coalgebra statement

```
phi_* T^c(Abar) = T^c(phi_* Abar)
```

for the additive normal-ordered Gram grading.  It checks finite word
degrees, deconcatenation, and displayed bar-differential degree
bookkeeping.

Run:

```
python3 compute/verify_bar_pushforward_commutation_fixture.py --fixture certificates/charge/bar_pushforward_commutation --check
```

Expected status:

```
BAR_PUSHFORWARD_COMMUTATION_VERIFIED
```

The packet is finite tensor-coalgebra arithmetic only.  It does not
certify the raw quadratic `Pi_X` pushforward, chiral Koszul
quasi-isomorphism, Hall bracket compatibility, Hopf pairing
compatibility, Pfaffian orientations, or protected traces.
