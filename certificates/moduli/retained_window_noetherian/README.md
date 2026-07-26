# Retained Window Noetherianity Certificate

This packet records the finite ACC statement used for retained windows
inside the Abramovich--Polishchuk/Liu heart.  A supplied finite exact
window is subobject-closed, quotient-closed, and equipped with a length
rank that strictly increases along strict subobject inclusions.  The
verifier computes acyclicity and longest-chain bounds.

Run:

```
python3 compute/verify_retained_window_noetherian_fixture.py --fixture certificates/moduli/retained_window_noetherian --check
```

Expected status:

```
RETAINED_WINDOW_NOETHERIAN_VERIFIED
```

The packet does not prove global noetherianity of the AP/Liu heart,
Harder--Narasimhan filtrations, bounded HN types, finite-type moduli,
Pfaffian orientations, or protected traces.
