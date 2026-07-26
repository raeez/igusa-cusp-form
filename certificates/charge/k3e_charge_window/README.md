# k3e_charge_window fixture

This directory is a finite charge-window scaffold. It is not a
construction of the active Igusa support, the Liu HN window, or the
normal-ordered Gram lift.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until finite HN-window
rows supply mathematical payload and geometric provenance for:

- active support rows from the Fourier coefficients of `phi_{0,1}`;
- downward saturation of the finite target window;
- Liu charge-height bounds and retained HN types;
- the Mukai-Gram map, including integrality and formula checks;
- the symmetric bilinear Gram cocycle, including delta, polarization,
  and bilinearity defects;
- normal-ordered lift orbits in the central extension;
- target test-window images under the normal-ordered Gram map, with the
  definition separated in `certificates/charge/finite_test_window`;
- formal primitive lifts of retained Gram triples;
- strict transition and Mittag-Leffler rows with `R^1 lim` rank zero;
- scalar-firewall checks excluding target presentations, signed
  exponents, scalar Pfaffian products, Hilbert-scheme scalar shadows,
  and source-rank-only substitutes as charge-window data.

Every populated row must carry `geometric_source_id` or
`source_formula_id` where appropriate, together with `proof_reference`.
Placeholder, mock, target-only, signed-only, Pfaffian-only,
scalar-only, status-only, Hilbert-scheme-only, rank-only, todo, or
unsupplied provenance is rejected.

A positive verifier result is `SCHEMA_COMPLETE_SCHEMA_ONLY`: schema,
status, payload, defect, transition, active-support, cocycle, lift, and
scalar-firewall checks passed. It is not a proof of the charge window.
