# A008 report: \(\phi_{0,1}\), coefficients, and half-index fencing

Runtime id: `019ddbcc-302f-7bb0-bf9b-cec6ba11d7e1`.
Nickname: Pasteur.
Status: completed.
Files changed by agent: none.

## Claim Attacked

\(\phi_{0,1}\), coefficient convention \(f(n,l)\),
\(Z_{\mathrm{K3}}=2\phi_{0,1}\), and "half-index" fencing.

## Status

No fatal convention error found in `main.tex`.

The manuscript's convention is consistent:
\[
\phi_{0,1}(\tau,z)=\sum_{n\ge0,l\in\mathbb Z} f(n,l)q^nr^l,
\qquad Z_{\mathrm{K3}}=2\phi_{0,1}.
\]

Local anchors:
`main.tex:625`, `main.tex:16130`.

Direct computation in `compute/verify_square_root.py` confirms:
\[
f(0,\pm1)=1,\quad f(0,0)=10,\quad f(1,\pm2)=10,\quad
f(1,\pm1)=-64,\quad f(1,0)=108.
\]
The same script confirms the displayed \(q^2\)-row in the coefficient
dictionary.

## Primary-Source Status

Gritsenko 1999 Example 1.3 gives the displayed \(\phi_{0,1}\) expansion
and states \(\chi(K3;\tau,z)=2\phi_{0,1}\). Source checked by A008:
`https://arxiv.org/pdf/math/9906190`, lines 385-405.

GNII gives the Borcherds product with exponents \(f_1(nm,l)\). Source
checked by A008: `https://arxiv.org/pdf/alg-geom/9611028`, lines
3450-3462.

GN gives the product split into \(m=0\) and \(m>0\) sectors and records
\(f(0,0)=10\), \(f(0,-1)=1\). Source checked by A008:
`https://arxiv.org/pdf/alg-geom/9504006`, lines 1282-1295.

Bibliography anchors:
`proj.bib:87`, `proj.bib:100`, `proj.bib:124`, `proj.bib:136`.

## Half-Index Fencing

Mostly correct. Strong local safeguards already present:

- abstract denial of microscopic Hilbert-space meaning: `main.tex:64`;
- Grothendieck representative definition: `main.tex:625`;
- noncanonical parity warning: `main.tex:638`;
- bulk/cusp non-Hilbert warning: `main.tex:674`;
- virtuality proposition: `main.tex:756`;
- coefficient dictionary firewall: `main.tex:16168`.

## Residual Wording Risks

`main.tex:68`: replace "For virtual super vector spaces" with "For
arbitrary Grothendieck representatives".

`main.tex:5801`: replace "K3 half-index coefficients" with
"coefficients \(f(nm,l)\) of the arithmetic Borcherds half
\(\phi_{0,1}\)".

`main.tex:18267`: replace "active half-coefficients" with "active
coefficients \(f(nm,l)\) of \(\phi_{0,1}\), not half-Hilbert-space
dimensions".

Commands run by agent:
`sed`, `nl -ba`, `rg`, `python3 compute/verify_square_root.py`,
`python3 compute/verify_lattice.py`, `git status --short`, plus arXiv
primary PDF checks. No writes.
