# Fifth O2 Walls Attack-Heal Report

Date: 2026-04-28.

Worktree: `/tmp/igusa-fifth-o2`.
Branch: `agent/igusa-fifth-o2-walls-20260428`.
Owned paths: `main.tex`, `notes/fifth_o2_walls_attack_heal_report.md`.

## Stable Core

O2 is not proved geometrically in the current manuscript.  The stable
statement is a conditional finite local certificate on the three type-II
walls
```tex
\delta_1=2f_2-f_3,\qquad
\delta_2=2f_{-2}-f_3,\qquad
\delta_3=f_3.
```

Under a supplied reduced Hall wall chart, a supplied equivariant splitting
of the reduced self-Ext determinant complex, and a supplied rank-one
normal Pfaffian block, the local sign is
```tex
\varepsilon_o(s_\delta)
=(-1)^{N_\delta^{\mathrm{Pf}}}.
```
For the O2 certificate the required ranks are
```tex
N_{\delta_1}^{\mathrm{Pf}}
=N_{\delta_2}^{\mathrm{Pf}}
=N_{\delta_3}^{\mathrm{Pf}}=1.
```

The automorphic target check remains separate:
```tex
d_{\delta_1}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_2}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_3}^{\mathrm{aut}}=f(0,-1)=1,
```
and Maass/Gritsenko--Nikulin gives
```tex
\nu_{\Delta_5}(s_{\delta_i})=-1.
```
These facts check the target.  They do not compute the Hall normal-mode
rank.

## Attacks

`A5-H03-01` deformation-obstruction chart attack.  The previous O2 text
named a local normal form but did not state the actual chart-level input:
a generic wall object, an equivariant real analytic d-critical/Kuranishi
chart, the reduced self-Ext complex in that chart, and the equality of
the fixed tangent with the wall tangent.

`A5-H03-02` local wall coordinate attack.  The lattice reflection supplies
the target hyperplane and the formal rule `s_delta(u_delta)=-u_delta`.
It does not prove that the Hall chart has such an anti-invariant real
coordinate or that the fixed locus is exactly the type-II wall.

`A5-H03-03` Ext-splitting attack.  The tangent determinant and normal
determinant may be coupled.  The local model requires the vanishing of an
equivariant extension class
```tex
\eta_\delta\in
\operatorname{Ext}^1_{D^{s_\delta}(U_\delta)}
(K^{\mathrm{nor}}_\delta,K^{\mathrm{tan}}_\delta).
```
If this class does not vanish, no independent normal Pfaffian sign has
been computed.

`A5-H03-04` unit and orientation attack.  Even after splitting, the
normal Pfaffian has the local form
```tex
\operatorname{Pf}(K_\delta^{\mathrm{nor}})
=\upsilon_\delta u_\delta^{N_\delta^{\mathrm{Pf}}}.
```
The sign is `(-1)^N` only if the unit is reflection-invariant after the
chosen quotient orientation trivializations:
```tex
s_\delta(\upsilon_\delta)=\upsilon_\delta.
```
A nontrivial unit character belongs to `(O1)+` and multiplies the local
sign.

`A5-H03-05` rank-one failure attack.  The local Hall normal model could
have `N_delta^{Pf}=0`, `2k`, `1+2k`, higher-order vanishing, or a
non-split family.  `1+2k` gives the same parity but not the rank-one
certificate.  `2k` gives the wrong sign.  Thus the exact O2 assertion is
the rank computation `N_delta^{Pf}=1`, not only odd parity.

`A5-H03-06` divisor-order conflation attack.  The equality
`d_delta^{aut}=1` is target-side Borcherds data.  It is not evidence for
`N_delta^{Pf}=1` unless a compact Hall/Pfaffian object has already been
constructed and identified with the automorphic determinant section.

## Repairs Inscribed

`main.tex` now contains Proposition
`prop:o2-local-obstruction-certificate`.  It states the exact local
calculation needed to remove the O2 hypothesis:
```tex
(U_\delta,x_\delta,u_\delta,K_\delta^{\mathrm{red}})
\to \mathfrak M_{\mathcal C_\delta}^{\mathrm{red}},
```
with `x_delta=[C_delta]`, the reduced self-Ext complex
```tex
\operatorname{RHom}_{\mathrm{red}}(\mathcal C_\delta,\mathcal C_\delta),
```
an equivariant tangent/normal splitting, invariant unit, and
rank-one normal model
```tex
K_\delta^{\mathrm{nor}}\simeq
\bigoplus_{j=1}^{N_\delta^{\mathrm{Pf}}}
[\mathbb R\xrightarrow{u_\delta}\mathbb R],
\qquad
N_\delta^{\mathrm{Pf}}=1.
```

The O2 theorem clause now points to that proposition as the local
obstruction test.  The honest-status remark and orientation open problem
also point to it, so future readers see that O2 is a geometric local
model obligation, not a corollary of Maass signs or the OP scalar square.

## Exact Residual Inputs

For each `i=1,2,3` one must still construct:

```tex
x_i=[\mathcal C_{\delta_i}],\qquad
(U_i,u_i,K_i^{\mathrm{red}}),
\qquad s_{\delta_i}(u_i)=-u_i,
```
the reduced self-Ext complex on the chart, the equivariant splitting
```tex
K_i^{\mathrm{red}}\simeq K_i^{\mathrm{tan}}\oplus K_i^{\mathrm{nor}},
```
the vanishing of the splitting obstruction `eta_delta_i`, the invariant
normal Pfaffian unit, and the rank computation
```tex
N_{\delta_i}^{\mathrm{Pf}}=1.
```

The global orientation line `(O1)`, quotient-compatible Weyl transport
`(O1)+`, and finite-stabilizer linearization data remain separate
obligations.

## Commands

- `sed`/`nl` reads of `CLAUDE.md`, ecosystem invariants/harness, the
  `chriss-ginzburg-rectify` skill, `main.tex` O2/Pfaffian regions,
  type-II root lattice regions, `compute/verify_lattice.py`,
  `appendices/boundary_compatibility_conditions.tex`, and
  `notes/fourth_pfaffian_attack_heal_report.md`.
- `rg -n "O2|Pfaff|pfaff|type-II|Type-II|wall|walls|N_\\delta|u_\\delta|normal|Ext|reflection|anti-invariant|Hall|d_\\delta" main.tex notes/fourth_pfaffian_attack_heal_report.md compute/verify_lattice.py proj.bib`
- `python3 compute/verify_lattice.py` passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-fifth-o2-texcheck main.tex` passed.  It produced the expected one-pass undefined-reference and undefined-citation warnings because BibTeX and later LaTeX passes were not run.
- `git diff --check -- main.tex notes/fifth_o2_walls_attack_heal_report.md` passed.
- `git diff --no-index --check -- /dev/null notes/fifth_o2_walls_attack_heal_report.md` emitted no whitespace diagnostics; exit code was `1` because the report is a new untracked file.

## Files Changed

- `main.tex`
- `notes/fifth_o2_walls_attack_heal_report.md`
