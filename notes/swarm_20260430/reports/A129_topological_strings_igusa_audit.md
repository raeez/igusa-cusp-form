# A129 -- Topological-Strings Igusa Recognition Audit

## Verdict

No active `topological-strings` manuscript theorem currently proves an
Igusa/Borcherds/CoHA/Hall recognition statement from local Hamiltonian
BF/Moyal data. The active firewall is mostly clean.

Risk remains in a standalone frontier note and archival reconstitution
reports that could later be mined as theorem-grade.

## Findings

- `frontier_mnop_framing_volume.tex` used theorem/proof-sketch language
  saying DT/PT/GW modules are canonically attached and KS wall-crossing
  lifts scalar equality to a motivic identity on the underlying
  factorisation algebra. This risks promoting scalar DT/PT equality into
  chain-level \(E_2\)/factorization recognition.
- an archival cross-volume report wrote
  \(Z^{DT,red}=-1/\Phi_{10}=-1/\Delta_5^2\), while the current Igusa OP
  normalization is \(-4096\Delta_5^{-2}\).
- `tate-P5-cross-volume.tex` is mostly safe but should explicitly use
  the finite-stage recognition-gate vocabulary.
- archival heuristic / Polyakov firewall notes contain speculative
  \(\mathfrak g_{\Delta_5}\) routes that should be labelled not compact
  Hall recognition routes.

## Repair Principle

Scalar DT/PT/GW identities are scalar target information. Any
factorization, \(E_2\)-center, Hall, or compact-source recognition lift
requires explicit moduli/source data, orientation, support/properness,
Hall integration, trace map, and recognition automorphism.

## Files Changed By Agent

None.
