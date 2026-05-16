# A247 Vol II thqg_perturbative_finiteness Repair

Runtime id: `019ddcd6-a10f-7172-9274-2907de18b43d`.

Changed:
- `/Users/raeez/chiral-bar-cobar-vol2/chapters/connections/thqg_perturbative_finiteness.tex`.

Repairs:
- Replaced “trace delivers `\Phi_{10}`” with scalar target/source-package language.
- Changed BV/Jacobi equality into a `BV,target` package gated by Vol III Hall-Borcherds plus Bruinier comparison.
- Changed “BV effective action exponentiates to” into a gated scalar target identity.
- Removed direct derivation language; BV graph side now supplies coefficient source only.
- Replaced “derivations/produce same Fourier” with conditional comparison-package language.
- Changed the `constant\cdot\Phi_{10}`-style identity into target-normalised `C_{\mathrm{M5}}\,\Phi_{10}^{\mathrm{un}}`.

Checks:
- `git diff --check -- chapters/connections/thqg_perturbative_finiteness.tex` passed.
- Targeted `rg` for `delivers the Siegel`, `exponentiates to the bimodular`, `derivation of the Borcherds`, `produce the same Fourier`, and `constant\cdot \Phi_{10}` found no matches.

Residual risk:
- No full LaTeX build was run.
