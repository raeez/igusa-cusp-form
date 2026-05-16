# A275 -- Vol II THQG bootstrap/nonperturbative HDelta scout

Status: completed; repair assigned to A282.

Claim attacked: THQG passages conflated scalar Igusa/Borcherds
identities with module, MTC, state-sum, and transport constructions on
`\mathbf H_{\Delta_5}`.

Scalar facts to preserve:
- `\Phi_{10}^{\mathrm{un}}=\Delta_5^2`.
- `D_5=64^{-1}\Delta_5`.
- `\Phi_{10}^{\mathrm{OP}}=D_5^2`.
- `Z_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}`.

Findings:
- Delta5 denominator lanes in `thqg_nonperturbative.tex` must use
  `\phi_{0,1}` coefficients, not `\phi_{-2,1}`.
- `thqg_modular_bootstrap.tex` needs scalar Fourier lemmas split from
  conditional TQFT/Hall corollaries.
- The displayed `z=0` specialization of `\phi_{-2,1}` is suspect
  because `\phi_{-2,1}(\tau,0)=0`; it requires a residue or
  renormalized Humbert restriction.
- Every module/MTC/state-sum/conformal-block use of
  `\mathbf H_{\Delta_5}` needs the finite Hall--Borcherds recognition
  datum.

Integration:
- A282 owns `thqg_nonperturbative.tex` and
  `thqg_modular_bootstrap.tex` for direct repair.
