# Retained Window Harder--Narasimhan Filtration Certificate

This packet records the finite HN-filtration statement used for
retained windows inside the Abramovich--Polishchuk/Liu heart.  A
supplied finite exact window is noetherian, carries a finite phase set,
and has explicit exact quotient chains for every object.  The verifier
checks that the quotient factors are semistable, that the phases
strictly decrease, and that lengths add along the chains.

Run:

```
python3 compute/verify_retained_window_hn_filtration_fixture.py --fixture certificates/moduli/retained_window_hn_filtration --check
```

Expected status:

```
RETAINED_WINDOW_HN_FILTRATION_VERIFIED
```

The packet does not prove global HN filtrations in the AP/Liu heart,
bounded HN types, finite-type moduli, Pfaffian orientations, or
protected traces.
