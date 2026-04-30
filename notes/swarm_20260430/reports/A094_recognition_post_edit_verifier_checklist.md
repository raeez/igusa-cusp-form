# A094 recognition post-edit verifier checklist

No files edited. Current tree was already dirty.

Run from `/Users/raeez/igusa-cusp-form` after the recognition-section
patch.

```bash
rg -n -F '\label{thm:primitive-recognition}' main.tex
rg -n -F '\label{prop:first-saturated-primitive-recognition-window}' main.tex
rg -n -F '\label{thm:wlethree-primitive-recognition-certificate}' main.tex
rg -n -F '\label{thm:a071-relation-closed-primitive-certificate}' main.tex
rg -n -F '\label{rem:relation-closed-window-status}' main.tex
rg -n -F '\label{thm:compact-source-provenance-gate}' main.tex
rg -n -F '\label{thm:executable-finite-source-matrix-criterion}' main.tex
rg -n -F '\label{prop:finite-wlethree-no7-source-protocol}' main.tex
rg -n -F '\label{cor:wlethree-no7-subverifier}' main.tex
rg -n -F '\label{subsec:primitive-recognition-proof-ledger}' main.tex
PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py
PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py
make
rg -n 'undefined references|LaTeX Warning: Reference|Citation.*undefined|There were undefined references|multiply defined|Duplicate label|Rerun to get cross-references' .build_logs out/main.log out/main.blg
```

Expected final warning scan: no unresolved references/citations and no
duplicate labels.

Preserve the Gram matrix, the map
\(\alpha(n,l,m)=2nf_2-lf_3+2mf_{-2}
=n\delta_1+m\delta_2+(n+m-l)\delta_3\), the \(W_{\le3}\) target parity
table, \(29-93=-64=f(1,1)\), height-four \(m=90\), signed
multiplicity \(108\), residual \(18\), doubled isotropic \(10|9|1\),
\(m(2\delta_{123})=-540\), \(\smult(2\delta_{123})=4016\), and relation
exponents \(3,5,3\).

Reject any patch that treats signed dimensions as recognition, target
labels as source bases, NO7 as full recognition, \(W_{\le3}\) as
relation-closed, target reference towers as compact source data, or full
parity claims for signed-only rows without target computation/citation.

