# Agent55 Notation Collision Latest Report

Date: 2026-04-29.

Scope: proposal-only notation/firewall review.  No source files edited.
Inspected `main.tex`, latest typeset manuscript PDF `out/main.pdf` (created
2026-04-29 19:21 SAST), and the latest attack PDF extraction
`materials/processed/2026-04-29-attack-whitepaper-analysis-revision-1923.txt`
from `materials/raw/2026-04-29-attack-whitepaper-analysis-revision-1923.pdf`.

Protocol read: `AGENTS.md`, `CLAUDE.md`, and
`notes/attack_whitepaper_analysis_20260428_090346_guide.md`.  The controlling
attack-heal rule here is evidence-first notation separation: source grading,
Gram/Fourier grading, target reference algebra, and compact geometric source
must not share symbols.

## Verdict

The latest PDF introduces a real notation collision cluster:

1. `UDI_R` is named as a "constructed finite compact source object", but its
   displayed components include target-derived data such as
   `H_R=U(g_{\Delta_5})_{\le R}` and "the BKM bracket"
   (`...revision-1923.txt:29517-29732`).  This can be a target-derived
   algebraic reference model only.  It is not compact `K3 x E` geometry.
2. `R_X:H_X^{geom}->UDI` conflicts with the live manuscript's
   `R_X` primitive-recognition slot (`main.tex:11853`, `main.tex:12203`) and
   with finite height `R`.
3. `H_X^{geom}` conflicts with the live `H_X` certificate slot and nearby
   `\mathcal H_X` Hall object (`main.tex:11853`, `main.tex:11896`,
   `main.tex:11962`).
4. Bare `D_X` is already overloaded by `\mathcal D_X` (virtual determinant),
   `\mathfrak D_X` (conditional first-order operator/algebra), and the
   five-part certificate slot `(D_X)` (`main.tex:73`, `main.tex:104`,
   `main.tex:11853`, `main.tex:12087`).
5. `D_R` in the latest PDF's `UDI_R` tuple collides with the existing finite
   `D_{0,R}` certificate family and with `\mathfrak D_{X,R}`
   (`main.tex:10346-10359`, `main.tex:10708`).
6. `b_R` is currently used both as geometric wrapped degree and as an
   `s`-exponent proxy; the manuscript itself has the attempted repair
   `b_R^{geom}` / `m_R=pr_3 \overline\Pi_X` in summary prose
   (`main.tex:250-256`, `main.tex:14255-14263`) but many body occurrences
   still use `s^{b_R}` or `b_R(...)=1` (`main.tex:7767-7781`,
   `main.tex:7790-7792`, `main.tex:8275-8278`).
7. Bare `\Gamma_X` must remain banned for the normal-ordered extension.  The
   live manuscript mostly uses `\widehat\Gamma_X`; the latest PDF prose and
   reports still describe "Gamma_X" as if it were the corrected extension.

## Safe Notation Table

| Safe symbol | Meaning | Status / firewall |
|---|---|---|
| `\Gamma_X^{\mathrm{form}}` | Formal full-Mukai dyonic lattice `\Lambda_S\oplus\Lambda_S` | Source bookkeeping lattice only. |
| `\Gamma_{X,\sigma}^{\mathrm{eff}}\subset\Gamma_X^{\mathrm{alg}}\subset\Gamma_X^{\mathrm{form}}` | Actual supplied Hall support | Use for compact source support; never replace by `\Gamma_{\mathrm{gram}}`. |
| `\Gamma_{\mathrm{gram}}=\mathbb Z^3` | Gram/Fourier index lattice `(n,l,m)` | Target/Fourier grading after descent; not Hall charge support. |
| `\Pi_X:\Gamma_X^{\mathrm{form}}\to\Gamma_{\mathrm{gram}}` | Raw quadratic Gram map | Non-additive.  Never use for corrected descent. |
| `\widehat\Gamma_X=\Gamma_X^{\mathrm{form}}\oplus_B\Gamma_{\mathrm{gram}}` | Normal-ordered charge extension | Corrected source grading after counterterm. |
| `\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}` | Additive normal-ordered Gram map | The only lattice-level map to use for descended Igusa degrees. |
| `\overline\Pi_{X,*}^{\Theta}` | Chain-level corrected descent | Never abbreviate to raw `\Pi_{X,*}`. |
| `\mathcal D_X` | Virtual `K_0` Borcherds determinant, `\mathcal D_X=\Delta_5` | Imported/computed determinant.  Not an operator. |
| `\mathfrak D_X`, `\mathfrak D_{X,R}` | Conditional first-order protected operator/algebra | Source-side datum, not constructed by `\mathcal D_X`. |
| `\mathsf K_X^{\mathrm{loc}}`, `\mathsf K_X^{\mathrm{hyb}}`, `\mathsf K_X^{\mathrm{or}}`, `\mathsf K_X^{\mathrm{desc}}`, `\mathsf K_X^{\mathrm{rec}}` | Proposed explicit replacements for `(L_X,H_X,O_X,D_X,R_X)` | Avoids `H_X/D_X/R_X` collisions. |
| `\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L;R}` | Target-derived algebraic finite Dirac-Igusa reference model, if added | Replacement for bare `UDI_R` when built from GN/BKM target data. |
| `\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L}` | Pro algebraic reference model | May satisfy `Pf=\Delta_5` by imported Borcherds/GN input; not compact geometry. |
| `\mathsf{DI}^{\mathrm{src}}_{X,R}` | Genuine finite compact source datum, only if independently constructed | Requires finite stacks/correspondences/orientations/hybrid source/coalgebra/Pfaffian data. |
| `\mathfrak H^{\mathrm{geom}}_{X,R}` | Conditional geometric Hall-domain candidate | Replacement for `H_X^{geom}`.  Must say "if constructed." |
| `\mathsf{Real}_{X,R}` | Geometric realization functor | Replacement for `R_{X,R}` / `R_X`. |
| `\mathcal H^{\mathrm{tw}}_{X,R}` | Orientation-gerbe-twisted geometric state object | Replacement for `Htw`, `H_R^tw` in source geometry. |
| `\mathsf H^{\mathrm{tw,alg}}_{\Delta_5,E,L;R}` | Optional twisted component of algebraic reference model | Use only if the universal/reference model really has a separate twisted-state component. |
| `b_R^{\mathrm{geom}}` | Geometric wrapped/support degree over `E` | Controls local/wrapped color and positivity of wrapped support. |
| `m_R=\operatorname{pr}_3\overline\Pi_X` | Borcherds/Gram trace exponent | Controls the `s`-power.  Use `s^{m_R}`, not `s^{b_R}`. |

## Forbidden / Replacement Names

| Forbidden manuscript form | Replacement | Reason |
|---|---|---|
| `UDI_R` as a compact finite Hall-Dirac source | `\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L;R}` if target-derived; `\mathsf{DI}^{\mathrm{src}}_{X,R}` only after real source construction | Prevents target model from masquerading as compact geometry. |
| `UDI_{\Delta_5,E,L}` without qualifier | `\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L}` or explicitly `\mathsf{UDI}^{\mathrm{alg}}_{\Delta_5,E,L}` | Bare UDI hides whether the object is target-reference or source-geometric. |
| "constructed finite compact source object" for a model with `H_R=U(g_{\Delta_5})_{\le R}` | "target-derived algebraic reference model" | PBW/BKM/radical data are imported from target algebra. |
| `R_X:H_X^{\mathrm{geom}}\to UDI` | `\mathsf{Real}_X:\mathfrak H_X^{\mathrm{geom}}\to\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L}` | Avoids collision with certificate `(R_X)` and finite height `R`. |
| `R_{X,R}` for finite realization | `\mathsf{Real}_{X,R}` | Same collision; finite height already uses `R`. |
| `H_X^{\mathrm{geom}}` | `\mathfrak H_X^{\mathrm{geom}}` or finite `\mathfrak H^{\mathrm{geom}}_{X,R}` | Avoids live `H_X` certificate slot and `\mathcal H_X`. |
| `H_R=U(g_{\Delta_5})_{\le R}` in a source tuple | `\mathsf U^{\mathrm{PBW}}_{\Delta_5,R}:=U(\mathfrak g_{\Delta_5})_{\le R}` | Names it as PBW target/reference tower. |
| `H_R^{tw}`, `Htw`, `H_tw` | `\mathcal H^{\mathrm{tw}}_{X,R}` for geometry; `\mathsf H^{\mathrm{tw,alg}}_{\Delta_5,E,L;R}` for algebraic reference | Avoids undefined shorthand and TeX `\H` accent hazard. |
| Bare `D_X` for determinant | `\mathcal D_X` | Determinant is calligraphic. |
| Bare `D_X` for first-order operator | `\mathfrak D_X` | Operator/algebra is fraktur. |
| Bare `(D_X)` certificate component in running prose | `\mathsf K_X^{\mathrm{desc}}` | Avoids determinant/operator collision. |
| `D_R` for finite Dirac block | `\mathfrak D^{\mathrm{alg}}_{\Delta_5,E,L;R}` or `\mathfrak D^{\mathrm{src}}_{X,R}` | Avoids `D_{0,R}` and `\mathfrak D_{X,R}` collisions. |
| `Pf_R` in the universal tuple | `\operatorname{pf}^{\mathrm{alg}}_{\Delta_5,E,L;R}` or `\operatorname{pf}^{\mathrm{src}}_{X,R}` | Must say whether the Pfaffian is target-reference or source-geometric. |
| `b_R` for `s`-degree | `m_R` | `s`-exponent is the third Gram coordinate. |
| `s^{b_R}` | `s^{m_R}` | Prevents geometric-degree / trace-exponent shift error. |
| `b_R(\eta)=1` for the `(0,1,1)` test | `m_R(\eta)=1` and `b_R^{\mathrm{geom}}(\eta)>0` | The test needs positive wrapped support and trace exponent one. |
| `b_R^{\mathrm{geom}}=m_R` | ban unless explicitly redefined in a special branch | On the rank-one D6-D2-D0 branch, the live dictionary has the shift `m=d-1`. |
| Bare `\Gamma_X` | `\Gamma_X^{\mathrm{form}}`, actual support, or `\widehat\Gamma_X` as appropriate | Bare `\Gamma_X` loses the source/raw/corrected split. |
| `\Gamma_{\mathrm{gram}}` as Hall charge support | `\Gamma_{X,\sigma}^{\mathrm{eff}}` upstairs, then `\overline\Pi_X` descent | Gram lattice is not additive Hall support. |
| `\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}` | `\overline\Pi_X:\widehat\Gamma_X\to\Gamma_{\mathrm{gram}}` | Raw `\Pi_X` is quadratic and has domain `\Gamma_X^{form}`. |
| `\Pi_{X,*}` for source descent | `\overline\Pi_{X,*}^{\Theta}` | Raw pushforward is exactly the no-go object. |

## Manuscript Firewall

Add or enforce this firewall before importing any latest-PDF prose:

```tex
\[
\Gamma_X^{\mathrm{form}}\neq\widehat\Gamma_X\neq\Gamma_{\mathrm{gram}},
\qquad
\Pi_X\neq\overline\Pi_X,
\qquad
\mathcal D_X\neq\mathfrak D_X\neq\mathsf K_X^{\mathrm{desc}}.
\]
\[
b_R^{\mathrm{geom}}\ \text{records wrapped geometric support},\qquad
m_R=\operatorname{pr}_3\overline\Pi_X\ \text{records the }s\text{-exponent}.
\]
```

If the universal finite construction is integrated, the first line should
not say "we construct the compact source."  Safe statement:

```tex
We construct a target-derived algebraic reference model
\(\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L;R}\) at finite height \(R\).
A compact \(K3\times E\) realization is a separate conditional functor
\[
\mathsf{Real}_{X,R}:\mathfrak H^{\mathrm{geom}}_{X,R}
\longrightarrow
\mathsf{DI}^{\mathrm{alg}}_{\Delta_5,E,L;R},
\]
defined only after the finite geometric Hall domain
\(\mathfrak H^{\mathrm{geom}}_{X,R}\) has been supplied.
```

## Grep Gates After Any Patch

```bash
rg -n -F -e 'UDI_R' -e 'UDI_{\\Delta_5,E,L}' main.tex
rg -n -F -e 'R_X:H_X' -e 'R_{X,R}' -e 'H_X^{\\mathrm{geom}}' main.tex
rg -n -F -e 'D_R' -e 'Htw' -e 'H_tw' -e 'H_R^{tw}' main.tex
rg -n -F -e 's^{b_R}' -e 's^{\\,b_R' -e 'b_R(\\eta)=1' -e 'b_R(\\eta_2)=1' main.tex
rg -n -P '\\\\Gamma_X(?!\\s*\\^)' main.tex
rg -n -F -e '\\Pi_X:\\widehat\\Gamma_X' -e '\\Pi_{X,*}' main.tex
rg -n -F -e '\\mathcal D_X' -e '\\mathfrak D_X' -e 'D_X' -e 'D_5' main.tex
```

Passing rule: no bare latest-PDF abbreviations survive.  Every surviving hit
must choose one layer explicitly: formal source lattice, normal-ordered
extension, Gram/Fourier target, algebraic reference model, or genuine compact
geometric source.

