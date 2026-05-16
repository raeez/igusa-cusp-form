# A120 -- Unifying Recognition-Gate Patch

## Claim Attacked

`chapters/theory/gluing/sec_10_unifying.tex` mapped a quotient to the
Borcherds positive half from primitive seed and Fourier data alone.

## Patch

The direct numerical Hall--BKM comparison was replaced by a finite-window
recognition-gated map \(\Psi^+_{\Hall\to\BKM,W}\). Primitive seed and
Fourier multiplicities are now necessary arithmetic tests, not sufficient
data for the quotient-to-Borcherds map. The layer table and proof now
require the finite Hall--Borcherds recognition datum plus completion
compatibility.

## Verification

```text
git diff --check -- chapters/theory/gluing/sec_10_unifying.tex
```

passed. Targeted search found no remaining stale "so the quotient maps"
or "The numerical Hall--BKM comparison" phrasing in the file.

## Changed Paths

- `/Users/raeez/calabi-yau-quantum-groups/chapters/theory/gluing/sec_10_unifying.tex`
