# Agents 103--204 Synthesis

Date: 2026-04-29.

This ledger integrates the second attack-heal continuation over
`notes/ingest/attack_whitepaper_analysis_20260429.txt`, agents 103--204.
The agents attacked the late whitepaper's universal-source language against
the current manuscript.

## Required manuscript patches

1. **Separate geometric elliptic degree from the Igusa trace exponent.**
   Residual prose still identifies geometric wrapped degree with the
   `s`-exponent.  The manuscript must use
   `b_R^{\mathrm{geom}}` only for local/wrapped support and
   `m_R=\operatorname{pr}_3\overline\Pi_X` for the Borcherds/Igusa
   trace exponent.  In the rank-one D6--D2--D0 branch, `m=d-1`.

2. **Tighten finite target-window/PBW language.**
   A finite window in the full enveloping algebra is not finite if Cartan
   powers or positive-negative cancellations are allowed.  The target tower
   must be phrased as a finite positive/root-window and bounded PBW
   filtration piece, with multiplication landing in a larger window.

3. **Clarify the formal `V_\gamma` blocks.**
   The chosen blocks in the algebraic target tower record only the signed
   exponent `f(nm,l)` unless additional target root-space data are supplied.
   They are not compact primitive spaces, parity data, or source Pfaffian
   lines.

4. **Remove undefined `Z^2_{\mathrm{sym}}` cohomology notation.**
   The text already says no ordinary cohomology class is asserted.  The
   sentence should instead say that `B` is a normalized symmetric bilinear
   additive 2-cocycle.

5. **Replace remaining source-overclaim language.**
   The abstract's compact statement should be the compact realization
   problem/criterion, and the late protected one-particle sentence must be
   replaced by the virtual determinant and protected K3-index statement plus
   the compact one-particle construction problem.

6. **Pfaffian square wording.**
   Where the source text says "Pfaffian square", it should say
   "Pfaffian square-root datum" or "Pfaffian line datum" unless the line
   is explicitly being squared.  This prevents confusion with the
   orientation-forgetful OP scalar square.

## Already safe

- The universal `UDI` / compact-source construction is absent from
  `main.tex`.  The finite Dirac--Igusa tower is target-reference data only.
- The target current envelope and target bar-cobar counit are not used to
  construct `C_X`, `b_X`, or `\Theta_{\mathrm{Kos}}`.
- The OP scalar square is quarantined as the primitive-class OP chamber
  scalar branch; it does not determine orientation monodromy.
- The Borcherds--Gritsenko--Nikulin constants survived attack:
  `D_5=64^{-1}\Delta_5`,
  `\operatorname{den}(\mathfrak g_{\Delta_5})=64^{-1}\Delta_5(2Z)`,
  `\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}`, and the type-II Cartan matrix.
- Primitive recognition uses source representatives,
  full parity dimensions, Hopf radical/coideal stability, no-extra-relations,
  completed PBW, and exact completion.

## Open obligations

The compact Hall--Dirac source, finite Hall atlases, hybrid wrapped
source, quotient orientation system, type-II Pfaffian wall charts,
  source Koszul datum, and compact primitive recognition are still
open source-side obligations.  No agent report supplies them.
