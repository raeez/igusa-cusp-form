# rhomred_finite_stabilizer_linearization_vanishing

This packet verifies the row-289 obstruction ledger for proving
\[
\lambda^H_{\mathcal C,S}=0
\]
for every retained finite stabilizer \(H\).

After row 288 computes \(\lambda^H\), row 289 requires the zero
condition in the relevant \(H^1(BH;\mathbb F_2)\)-basis: trivial or
odd stabilizers have zero target after the actual retained action row
is supplied, \(E[2]\) requires \(\lambda_1=\lambda_2=0\), and
two-primary rank two stabilizers require
\(\lambda^{(H)}_1=\lambda^{(H)}_2=0\).

This packet imports the row-288 finite-stabilizer linearization
character packet and records that the current tables supply no
\(\lambda^H\)-values and no zero-coordinate rows.  It does not infer
zero linearization from \(\beta^H=0\), from a row-287
null-trivialization, from determinant-anchor translation weight, from
class invariance, from transition compatibility, from vanishing cycles,
or from protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_linearization_vanishing_obstruction.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_linearization_vanishing --check
```
