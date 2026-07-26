# finite_hall_compact_geometric_hopf_pairing_datum

This packet records correction row 364.

It records the compact geometric Hopf-pairing datum as a source-level
datum: source degree-zero trace, positive-negative pairing
correspondences, orientation and Thom-Sebastiani transport, `G`
matrices, `K` radical matrices, `Q` quotient splittings, cyclic
three-point correspondences, Hopf-adjointness witnesses, Frobenius
cyclic witnesses, and quotient non-degeneracy witnesses.

The packet imports row 363, row 362, row 361, the Calabi-Yau threefold
Serre-sign criterion, the level-Z protected-trace obstruction ledger
as a firewall, and the compact Hall source obstruction ledger.  The
current compact source supplies none of the datum rows.

Run:

```sh
python3 compute/verify_finite_hall_compact_geometric_hopf_pairing_datum.py \
  --fixture certificates/hall/finite_hall_compact_geometric_hopf_pairing_datum --check
```

Expected status:

```text
FINITE_HALL_COMPACT_GEOMETRIC_HOPF_PAIRING_DATUM_OBSTRUCTION_VERIFIED
```
