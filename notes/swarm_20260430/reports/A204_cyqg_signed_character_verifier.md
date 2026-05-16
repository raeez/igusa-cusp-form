# A204 CYQG Signed-Character/Test Verifier

## Claim Attacked

The recent CYQG signed-character patches might still conflate
`\Delta_5` exponents with the doubled K3 elliptic genus /
`\Phi_{10}^{\mathrm{un}}=\Delta_5^2` lane, or let ordinary multiplicity
language survive inside protected-index formulas.

## Findings

### High

- `~/calabi-yau-quantum-groups/chapters/examples/k3e_cy3_programme.tex`
  still mixed `g_{\Delta_5}` with `Z_{K3}=2\phi_{0,1}` in several
  sentences. The corrected lane is:
  `sdim g_{\Delta_5,\alpha}=c_0(D)`, while
  `Z_{K3}=2\phi_{0,1}` gives doubled
  `\Phi_{10}^{\mathrm{un}}=\Delta_5^2` exponents.
- `~/calabi-yau-quantum-groups/notes/physics_bps_root_multiplicities.tex`
  still called `\phi_{0,1}` the K3 elliptic genus, used the doubled
  expansion `2y+20+2y^{-1}`, set `sdim g_\alpha=f(nm,\ell)`, and used
  `f(1,1)=-128` where the `g_{\Delta_5}` coefficient is `-64`.

### Medium

- The same note kept boxed/general formulas of the form
  `mult = \Omega` where the intended invariant is a protected
  index/supertrace.
- `compute/lib/k3e_coha_structure.py` still had a nominal
  "three independent paths" check whose third path was assigned from
  the first; the test reflected that dependence.

## Checks

- `git diff --check -- <4 scoped files>` clean.
- `PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider compute/tests/test_k3e_coha_structure.py`
  reported `93 passed`.
- Targeted `rg` over the four scoped files for `K3 elliptic genus`,
  `Z_{K3}`, `root multiplicity`, `ordinary`, `generator count`,
  `c_0(D)`, `-128`, and `c(3) = -64`.

## Status

No fatal findings, but the high normalization defects are real. Patch
delegated to A207 with disjoint CYQG ownership.

