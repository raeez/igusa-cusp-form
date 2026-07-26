# rhomred_finite_stabilizer_beta

This packet verifies the row-285 obstruction ledger for computing the
finite-stabilizer Borel class
\[
\beta^H_{\mathcal C,S}\in H^2(BH;\mathbb F_2).
\]

The computation requires a finite-stabilizer Cech--Borel representative
\(\widetilde\beta^H\), a Borel spectral-sequence edge reduction, and
coordinates in the relevant group-cohomology basis: odd/trivial,
Klein-four, or full two-primary.  The rank-two coefficient \(A_{12}\)
is not detected by cyclic order-two restrictions.

This packet imports residual finite group input, but records that the
current tables supply no finite-stabilizer orientation row, no
\(\widetilde\beta^H\) representative, no edge-reduction row, and no
\(\beta^H\) coefficient row.  It does not prove row 286 vanishing,
construct row 287 null-trivializations, compute row 288 linearization
characters, construct quotient orientation, prove transition
compatibility, construct vanishing cycles, or define protected
integration.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_beta_obstruction.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_beta --check
```
