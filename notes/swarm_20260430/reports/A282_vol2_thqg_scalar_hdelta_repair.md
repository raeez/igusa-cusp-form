# A282 -- Vol II THQG scalar/HDelta repair

Status: completed; isolated patch integrated by master thread.

Isolated worktree: `/tmp/a282-thqg-work`.

Files integrated:
- `chapters/connections/thqg_nonperturbative.tex`
- `chapters/connections/thqg_modular_bootstrap.tex`

Repairs:
- Replaced erroneous `\phi_{-2,1}` Delta5 denominator exponents with
  `\phi_{0,1}` coefficients `f(mn,r)`.
- Preserved scalar normalizations:
  `\Phi_{10}^{\mathrm{un}}=\Delta_5^2`,
  `D_5=64^{-1}\Delta_5`,
  `\Phi_{10}^{\mathrm{OP}}=D_5^2`, and
  `Z_{\mathrm{OP/DT}}=-4096\Delta_5^{-2}`.
- Split scalar Fourier/product identities from conditional
  D3/BPS/TQFT/Hall readings.
- Gated `\mathbf H_{\Delta_5}` module, MTC, state-space, state-sum,
  transport, and conformal-block claims on the Vol III finite
  Hall--Borcherds recognition datum.
- Replaced raw nonzero use of `\phi_{-2,1}(\tau,0)` by a renormalized
  Humbert residue `\mathcal R_{-2,1}` and explicitly recorded that the
  unrenormalized value is zero.

Checks:
- Worker `git diff --check` passed in the isolated worktree.
- Master `git apply --check` passed before integration.
- Master `git diff --check` passed on both integrated files.
- Targeted master grep found no `c_{\phi_{-2,1}}` denominator exponents.

Remaining obligations:
- Prove/import the finite Hall--Borcherds recognition datum.
- Prove the Gevrey/Borel/resurgent hypotheses behind D3 and Schwinger
  physical interpretations.
- Construct and verify the Humbert residue functional
  `\mathcal R_{-2,1}` and resulting block `q`-expansions.
