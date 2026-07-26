# Stability Heart Datum Certificate

This packet records the chosen Abramovich--Polishchuk/Liu heart used by
the retained K3xE Hall construction. It certifies the definition of the
heart and its inputs, not noetherianity, Harder--Narasimhan
filtrations, bounded HN types, finite-type semistable substacks, or
derived moduli.

Run:

```
python3 compute/verify_stability_heart_fixture.py --fixture certificates/moduli/stability_heart --check
```

Expected status:

```
STABILITY_HEART_DATUM_VERIFIED
```

The finite moduli packet remains separate and fail-closed until the HN
and finite-type rows are supplied.
