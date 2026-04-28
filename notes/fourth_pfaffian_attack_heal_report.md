# Fourth Pfaffian Attack-Heal Report

Date: 2026-04-28.

Worktree: `/tmp/igusa-fourth-pfaffian`.
Branch: `agent/igusa-fourth-pfaffian-20260428`.
Owned paths: `main.tex`, `notes/fourth_pfaffian_attack_heal_report.md`.

## Stable Core

The O2/type-II Pfaffian lane is stable only as a conditional local
Dirac model.

The supplied finite wall certificate consists of three type-II wall
charts, one for each simple root
`\delta_1=2f_2-f_3`, `\delta_2=2f_{-2}-f_3`, `\delta_3=f_3`, with:

```tex
s_{\delta_i}(u_i)=-u_i,\qquad
K^{\mathrm{nor}}_{\delta_i}\simeq
[\mathbb R\xrightarrow{u_i}\mathbb R],
\qquad
N_{\delta_i}^{\mathrm{Pf}}=1.
```

This gives the Hall-side conditional local sign

```tex
\varepsilon_o(s_{\delta_i})
=(-1)^{N_{\delta_i}^{\mathrm{Pf}}}
=-1,\qquad i=1,2,3.
```

Independently, the automorphic target has

```tex
D_5=64^{-1}\Delta_5
=q^{1/2}r^{1/2}s^{1/2}
\prod(1-q^nr^ls^m)^{f(nm,l)},
```

so the type-II divisor orders are

```tex
d_{\delta_1}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_2}^{\mathrm{aut}}=f(0,1)=1,\quad
d_{\delta_3}^{\mathrm{aut}}=f(0,-1)=1.
```

Maass/Gritsenko--Nikulin then gives

```tex
\nu_{\Delta_5}(s_{\delta_i})=-1,\qquad
\nu_{\Delta_5}(s_{f_{-2}-f_2})
=\nu_{\Delta_5}(s_{f_2-f_3})
=\nu_{\Delta_5}(s_{f_2+f_3})=+1.
```

The equality `\varepsilon_o=\nu_{\Delta_5}` on
`W^{(2)}(\Lambda^{2,1}_{II})` is conditional on `(O1)`, `(O1)+`, and
`(O2)`.  The OP scalar square remains separate:

```tex
Z^X_{\mathrm{OP}}=Z^X_{\mathrm{DT}}
=-4096\,\Delta_5^{-2},\qquad
-4096=-(64)^2.
```

The constants `64`, `4096`, and the OP minus sign do not determine a
Hall orientation character.

## Valid Attacks

`A4-H03-01`: The same symbol `N_{\delta_i}` was used close to both the
Pfaffian normal-mode rank and the automorphic product exponent.  This
made it too easy to read the local Hall sign from the Borcherds divisor
order.  Status: healed by replacing the local rank with
`N_{\delta_i}^{\mathrm{Pf}}` and the automorphic divisor order with
`d_{\delta_i}^{\mathrm{aut}}`.

`A4-H03-02`: The local-sign lemma opened with lattice and automorphic
target data before the local Pfaffian calculation.  This presented the
right result in a logically dangerous order.  Status: healed by putting
the O2 rank-one Pfaffian crossing first and moving the automorphic
labels to an independent target paragraph.

`A4-H03-03`: The automorphic target check stated the monic Borcherds
product as a formula for `\Delta_5`, omitting the theta normalization.
Status: healed by writing `D_5=64^{-1}\Delta_5` in the product display.

`A4-H03-04`: The Maass/divisor paragraph could be read as deriving the
Maass sign solely from divisor order and anti-invariance of a local
equation.  Status: healed by using Lemma `maass-multiplier-restriction`
for character values and using divisor orders only as an independent
target check.

`A4-H03-05`: The pure group-theoretic Weyl-sign extension still referred
to `N_{\delta_i}`.  Status: healed by making the input signs
`\epsilon_i=(-1)^{N_{\delta_i}^{\mathrm{Pf}}}`.

## Repairs

- `main.tex`: O2 now names three supplied odd Pfaffian normal ranks
  `N_{\delta_i}^{\mathrm{Pf}}=1`.
- `main.tex`: The theorem statement says the first `-1` is the
  Hall/Pfaffian output of O2 and the second `-1` is the independent
  Maass value.
- `main.tex`: The conditional sign lemma computes the Pfaffian sign from
  the rank-one model before mentioning automorphic labels.
- `main.tex`: The automorphic target check uses `D_5=64^{-1}\Delta_5`
  and separates `d_{\delta}^{\mathrm{aut}}` from
  `N_{\delta}^{\mathrm{Pf}}`.
- `main.tex`: The comparison remark now says the Borcherds product and
  Maass character supply the target character, not the Hall orientation
  character.

## Residual Obligations

O2 remains a real residual.  The manuscript still needs the three
geometric local calculations:

```tex
(x_i,U_i,u_i),\qquad s_{\delta_i}(u_i)=-u_i,\qquad
K^{\mathrm{red}}|_{U_i}\simeq K_i^{\mathrm{tan}}\oplus K_i^{\mathrm{nor}},
```

with an oriented quasi-isomorphism

```tex
K_i^{\mathrm{nor}}\simeq[\mathbb R\xrightarrow{u_i}\mathbb R]
```

at each simple type-II wall.  The global orientation line `(O1)` and
the quotient-compatible Weyl transport `(O1)+` also remain open.

## Commands

- `rg -n "Pfaffian|pfaffian|Dirac|type-II|type II|Type-II|Weyl character|Maass|OP scalar|O2|odd normal|normal mode|automorphic|boundary|diagonal" main.tex`
- `rg -n "Pfaffian|pfaffian|Dirac|type-II|type II|Type-II|Weyl character|Maass|OP scalar|O2|odd normal|normal mode|automorphic|boundary|diagonal" proj.bib notes -g '*.md' -g '*.bib'`
- `git diff --check` passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=out main.tex` passed as a one-pass TeX syntax check.  It produced expected undefined-reference and undefined-citation warnings because BibTeX and later LaTeX passes were not run.
- `git show HEAD:out/main.pdf > out/main.pdf` restored the generated PDF after the syntax check, because `out/main.pdf` is outside this agent's owned write paths.
- `git add -- main.tex notes/fourth_pfaffian_attack_heal_report.md`
- `git diff --cached --check` passed.

## Files Changed

- `main.tex`
- `notes/fourth_pfaffian_attack_heal_report.md`

Staged paths: `main.tex`, `notes/fourth_pfaffian_attack_heal_report.md`.
