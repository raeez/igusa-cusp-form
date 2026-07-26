# rhomred_finite_stabilizer_beta_nulltrivialization

This packet verifies the row-287 obstruction ledger for constructing
null-trivializations of finite-stabilizer Borel classes compatible
under subgroup restriction.

After rows 285 and 286 supply a representative
\[
a^H_{\mathcal C,S}\in Z^2(BH;\mathbb F_2)
\]
and verify that its class vanishes, row 287 requires a chosen primitive
\[
h^H_{\mathcal C,S}\in C^1(BH;\mathbb F_2),
\qquad \delta h^H_{\mathcal C,S}=a^H_{\mathcal C,S}.
\]
For each retained subgroup inclusion \(K\hookrightarrow H\), the row
also requires a comparison zero-cochain \(q\) whose coboundary is the
difference between the restricted primitive on \(H\) and the primitive
on \(K\), with zero defect on two-step subgroup chains.

This packet imports the row-286 finite-stabilizer beta-vanishing packet
and records that the current tables supply no beta cocycle, no zero
row, no one-cochain, no subgroup-inclusion table, no comparison
zero-cochain, and no chain-coherence row.  It does not construct
row-288 linearization characters, row-289 linearization vanishing,
quotient orientation, transition compatibility, vanishing cycles, or
protected integration.

Verify with:

```sh
python3 compute/verify_rhomred_finite_stabilizer_beta_nulltrivialization_obstruction.py \
  --fixture certificates/orientation/rhomred_finite_stabilizer_beta_nulltrivialization --check
```
