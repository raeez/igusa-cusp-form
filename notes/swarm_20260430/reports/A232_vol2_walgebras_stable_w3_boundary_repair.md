# A232 -- Vol II stable/W3 W-algebra boundary repair

## Claim attacked

`w-algebras-stable.tex` and `w-algebras-w3.tex` treated stable-W,
Schur, module, D-module, and coproduct data as if they constructed
\(\mathbf H_{\Delta_5}\).

## Repairs

- `w-algebras-stable.tex`: the K3 stable-W passage now gives protected
  Schur/stable-W comparison data. The notation
  \(\mathbf H_{\Delta_5}\) is available only after Vol III finite
  Hall--Borcherds source recognition.
- `w-algebras-w3.tex`: module structure, higher-spin generators,
  Humbert D-module monodromy, and coproduct are conditional target
  recognition statements after finite Hall--Borcherds/source gates.

## Verification

`git diff --check -- chapters/examples/w-algebras-stable.tex chapters/examples/w-algebras-w3.tex`
passed. Remaining targeted hits are negative or gated statements.

## Residual obligation

Compact source provenance, orientation/parity/root fixtures,
product/coproduct matrices, radical/no-extra/PBW checks, D-module/source
block identification, and compatible completions remain open recognition
data.
