# local_configuration_symmetric_descent

This packet records correction row 244: finite symmetric-group descent
for projection-finite local configuration charts.

It proves that relabelling a finite local colour profile preserves the
incidence locus `Z_I`, induces an isomorphism of closed local
configuration charts, transports the reduced local coefficient, and
descends the coefficient to the finite stabilizer quotient stack.  The
proof is before the reduced `E`-quotient and at fixed HN height.

It does not prove collision compatibility, closed-chart refinement,
ordered-chart descent to the symmetric finite-colour colimit, quotient
descent, transition compatibility, or aggregate hybrid-carrier
population.

Run:

```sh
python3 compute/verify_local_configuration_symmetric_descent_obstruction.py \
  --fixture certificates/hybrid/local_configuration_symmetric_descent --check
```

Expected status:

```text
LOCAL_CONFIGURATION_SYMMETRIC_DESCENT_VERIFIED
```
