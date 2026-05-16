# A276 -- Vol II HT boundary-line HDelta scout

Status: completed; repairs integrated by master thread.

Claim attacked: the HT bulk-boundary-line cluster was asserting K3
boundary structures, Wilson pairings, Schwinger transport, and all-loop
partition identities on `\mathbf H_{\Delta_5}` without explicit
Hall--Borcherds gates.

Findings integrated:
- `ht_bulk_boundary_line.tex` K3 three-loop, 4d CS, Wilson-line,
  Heegner, Schwinger, nonperturbative, and all-loop statements were
  retagged or rewritten as conditional comparison targets.
- `sc_chtop_heptagon.tex` was changed from a hard
  `H^2(\mathfrak g_{\Delta_5}) \cong \mathbb C\cdot\Delta_5`
  reading to a conditional scalar target.
- `six_d_hcs_e3_chiral_avatar_platonic.tex` now marks the K3 row as a
  conditional boundary-to-Borcherds comparator.

Post-integration checks:
- `git diff --check` passed for the touched Vol II files.
- Targeted fixed-string searches found no remaining old exact phrases
  `c_n^{\mathrm{triangle}}`, bare Schwinger `H_{\Delta_5}` module
  assertions, or direct `H_{\Delta_5}` Fock-module phrasing in the
  repaired HT anchors.

Remaining obligation: A279 was launched for an independent postpatch
verification pass.
