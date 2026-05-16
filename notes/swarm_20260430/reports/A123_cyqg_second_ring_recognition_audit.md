# A123 -- CYQG Second-Ring Recognition Audit

## Claim Attacked

After the first Vol III patch cluster, stale target/source collapses
might remain outside the directly patched files.

## Findings

Critical:

- `chapters/examples/k3_chiral_algebra.tex` asserted
  \(\sum|\operatorname{mult}(\alpha)|=24\) at every level and identified
  level multiplicities with \(|c(D)|\). This collapses signed BKM
  supermultiplicity into ordinary dimension.
- `notes/gluing_ch_part_7_lattice_automorphic.tex` repeatedly said
  Fourier coefficients produce CoHA structure constants directly.
- `working_notes.tex` marked a direct chiral-bialgebra equivalence to
  \(\mathcal H_{\Delta_5}\) and \(U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})\),
  while later text correctly guarded against CoHA equality.

Major:

- `chapters/connections/modular_koszul_bridge.tex` and
  `chapters/theory/cy_to_chiral.tex` say \(c(D)\) simultaneously counts
  BPS states, walls, Stokes lines, and Stokes constants.
- `main.tex`, `chapters/theory/introduction.tex`, and
  `chapters/theory/e1_chiral_algebras.tex` repeat direct
  \(U_{\mathrm{ch}}(\mathfrak g_{\Delta_5})\) specialisations without the
  finite Hall--Borcherds recognition gate.
- `chapters/theory/quantum_groups_foundations.tex` states
  \(\CoHA(X)\simeq U(Y^+(\mathfrak g_{\Delta_5}))\) and
  \(\operatorname{Lie}\CoHA(X)=Y^+(\mathfrak g_{\Delta_5})\) without the
  finite recognition datum.
- `notes/wave15_a9_G_of_X_generic_bezrukavnikov.tex`,
  `notes/wave15_b2_sigma2_moduli_K3xE.tex`, and
  `notes/wave_cfg2026/agent_3_e1_ran_specialization.tex` contain direct
  CoHA / positive-half / \(U_{\mathrm{ch}}\) identifications not gated by
  source fixtures.

## Repair Principle

Use the healed language already established in the first patch cluster:
Borcherds/Jacobi coefficients are target arithmetic and
Euler/superdimension tests; ordinary target parity requires a parity
fixture or target presentation computation; compact Hall/CoHA source
identification requires the finite Hall--Borcherds recognition gate.

## Files Changed By Agent

None.
