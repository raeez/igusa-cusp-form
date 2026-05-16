# Third Koszul Attack-Heal Report

Date: 2026-04-28.
Worktree: `/tmp/igusa-third-koszul`.
Branch: `agent/igusa-third-koszul-20260428`.

## Claim Attacked

The attacked shortcut was:
\[
\Omega_E^{\mathrm{ch}}\bar B_E^{\mathrm{ch}}
(\mathsf{Den}_{\Delta_5,E})
\to
\mathsf{Den}_{\Delta_5,E}
\]
constructs the compact source coalgebra \(C_{X,R}\), the source
filtration \(F^{\mathrm{co}}_{R,\bullet}\), the collision coproduct
\(\Delta_R^{\mathrm{ch}}\), the source bar comparison \(b_{X,R}\), the
cobar comparison \(\Theta_{\mathrm{Kos},R}\), or the primitive
restriction.

Status: false.  The target counit reconstructs only the already imported
current envelope from its target bar coalgebra.  The compact source data
must be supplied independently or remain open.

## Manuscript Changes

- `main.tex:4284`: the compact realization section now states that the
  target-side bar-cobar counit remains internal to the target observable
  algebra.
- `main.tex:4565`: the former target-internal inversion statement is now
  a target-internal counit statement for a chosen augmented filtered
  target model.  Its filtration is explicitly separated from
  \(F^{\mathrm{co}}_{R,\bullet}\), and its bar coalgebra is explicitly not
  \(C_{X,R}\).
- `main.tex:4613`: the finite chiral Koszul certificate now forbids
  defining \(C_{X,R}\), \(F^{\mathrm{co}}_{R,\bullet}\), or
  \(\Delta_R^{\mathrm{ch}}\) from
  \(\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E,\le R})\) or from a
  homotopy inverse to the target counit.
- `main.tex:4654`: conilpotence and the collision coproduct are named as
  source finite-stage data, not structures transported from the target
  bar construction.
- `main.tex:4684`: \(\Theta_{\mathrm{Kos},R}\) is fixed as a
  source-to-target comparison; a target-side inverse cannot define source
  primitives.
- `main.tex:4713`: the Koszul residual tuple now includes
  \(\mathfrak o^{\mathrm{sep}}_R\), recording source/target separation.
- `main.tex:4744`: the inverse-limit consequence is weakened to a
  completed pro-conilpotent source coalgebra, conilpotent on finite HN
  quotients.
- `main.tex:6782`, `main.tex:6984`, and `main.tex:7517`: the full
  Dirac-Igusa certificate and open full-certificate list now require
  \(F^{\mathrm{co}}_{R,\bullet}\), \(\Delta_R^{\mathrm{ch}}\), and
  \(\mathfrak o^{\mathrm{sep}}_R=0\) along with \(C_{X,R}\),
  \(b_{X,R}\), and \(\Theta_{\mathrm{Kos},R}\).

## Exact Residual

At height \(R\), the residual is now
\[
\mathfrak O_{\mathrm{Kos},R}
=
(\mathfrak o^C_R,\mathfrak o^{\mathrm{conil}}_R,
\mathfrak o^b_R,\mathfrak o^\Omega_R,
\mathfrak o^{\mathrm{hyb}}_R,\mathfrak o^\Pi_R,
\mathfrak o^{\mathrm{sep}}_R,\mathfrak o^{\Prim}_R).
\]

The new entry \(\mathfrak o^{\mathrm{sep}}_R\) vanishes only when the
source coalgebra, filtration, collision coproduct, bar comparison, and
primitive restriction are supplied before the target comparison and are
not reconstructed from the target counit.

## Remaining Open Obligations

1. Construct \(C_{X,R}\), \(F^{\mathrm{co}}_{R,\bullet}\), and
   \(\Delta_R^{\mathrm{ch}}\) from compact finite Hall/factorization
   correspondences, including local-local, local-wrapped, and
   wrapped-wrapped flags.
2. Prove the bar comparison
   \(b_{X,R}:C_{X,R}\simeq
   \bar B_E^{\mathrm{ch}}(\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}})\)
   independently of the target bar coalgebra.
3. Prove the cobar comparison
   \(\Theta_{\mathrm{Kos},R}:\Omega_E^{\mathrm{ch}}C_{X,R}\simeq
   \mathsf{Den}_{\Delta_5,E,\le R}\) as a source-to-target theorem.
4. Prove primitive restriction after the closed Hopf-radical quotient
   from source primitive representatives, not by pulling back target root
   spaces.

## Verification

- `git diff --check` passed before and after writing this report.
- `pdflatex -halt-on-error -interaction=nonstopmode
  -output-directory=/tmp/igusa-third-koszul-texcheck main.tex` passed.
  The run was intentionally one pass into `/tmp`; it reported expected
  first-pass unresolved references and citations and did not touch
  `out/main.pdf`.
