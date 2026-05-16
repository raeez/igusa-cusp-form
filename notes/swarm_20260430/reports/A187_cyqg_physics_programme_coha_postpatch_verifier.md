# A187 -- CYQG Physics / Programme / CoHA Postpatch Verifier

## Result

Read-only verification found the A183 patch mostly clean, with one older
programme proposition still using bare \(\mathrm{mult}=c_0(D)\) language.

## Findings

- Residual: `k3e_cy3_programme.tex:2071` and `2107` still had older bare
  \(\mathrm{mult}(\alpha)=c_0(D_\alpha)\) language.
- Clean: `k3e_cy3_programme.tex:4837` identifies `mult alpha` as signed
  root character, and `4862` gates actual generators/relations behind
  parity/Hall--Borcherds recognition.
- Clean: `physics_bps_root_multiplicities.tex:425`, `434` say signed
  index/superdimension and require parity recognition; no \(f(0,0)\) /
  \(f(1,1)\) ordinary generator-count leak remains.
- Clean: `k3e_coha_structure.py:820` says the PL value is a
  protected-character fixture, not an unsourced ordinary generator count.
- Clean: `root_multiplicity` is visibly trap-fenced as a deprecated legacy
  alias at `k3e_coha_structure.py:220`, with no-dimension warning at
  `223`.

## Checks

- `git diff --check -- <four scoped files>` passed.
- `pytest compute/tests/test_k3e_coha_structure.py` returned
  `92 passed in 4.36s`.
- Targeted `rg` found only the older programme `mult=c_0(D)` prose.

## Main-Thread Follow-Up

The main thread patched the older programme proposition to signed
root-character / target superdimension language and renamed the remaining
CoHA test method away from “means free.”

