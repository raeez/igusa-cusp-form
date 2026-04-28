# Sixth Koszul/Cobar Attack-Heal Report

Date: 2026-04-28.
Role: S05 Koszul/Cobar.
Worktree: `/tmp/igusa-sixth-koszul-cobar`.
Branch: `agent/igusa-sixth-koszul-cobar-20260428`.

## Claim Attacked

Obligation (7) asks for the Koszul source coalgebra, finite filtration,
collision coproduct, and source-to-target cobar comparison.  The
dangerous shortcut is:
\[
\bar B_E^{\mathrm{ch}}(\mathsf{Den}_{\Delta_5,E,\le R})
\quad\text{or}\quad
\Omega_E^{\mathrm{ch}}\bar B_E^{\mathrm{ch}}
(\mathsf{Den}_{\Delta_5,E,\le R})\to
\mathsf{Den}_{\Delta_5,E,\le R}
\]
constructs \(C_{X,R}\), \(F^{\mathrm{co}}_{R,\bullet}\),
\(\Delta_R^{\mathrm{ch}}\), \(b_{X,R}\), or source primitives.

Status: false.  The target current envelope cannot define the source
coalgebra.  The stable repair is source-side and conditional on the
finite hybrid source.

## Stable Repair

`main.tex` now contains two new source-side statements.

- `main.tex:5356`: `prop:canonical-source-bar-coalgebra`.
  If the finite hybrid residual \(\mathfrak O_{\mathrm{hyb},R}=0\), set
  \[
  C^{\mathrm{bar}}_{X,R}:=
  \bar B_E^{\mathrm{ch}}
  (\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}).
  \]
  This is the reduced chiral bar coalgebra of the supplied hybrid source,
  not the target bar coalgebra.
- `main.tex:5449`: `cor:source-bar-remaining-cobar-obstruction`.
  With this source-bar choice, the coalgebra, filtration, collision
  coproduct, conilpotence, and bar comparison are constructed; the
  remaining obstruction is the source-to-target cobar quasi-isomorphism.

The finite filtration is bar length:
\[
F^{\mathrm{co}}_{R,p}C^{\mathrm{bar}}_{X,R}
=
k\mathbf 1\oplus
\bigoplus_{1\le j\le p}
\bar B_E^{\mathrm{ch},j}
(\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}).
\]
The counit is projection to \(k\mathbf1\), and the coaugmentation is the
inclusion of \(k\mathbf1\).

For \(x=[x_1|\cdots|x_p]\), the source collision coproduct is the
finite collision-flag cut:
\[
\Delta_R^{\mathrm{bar}}(x)
=\mathbf1\otimes x+x\otimes\mathbf1
+\sum_{i=1}^{p-1}
[x_1|\cdots|x_i]\otimes[x_{i+1}|\cdots|x_p].
\]
The cut maps are realized by the finite collision and flag pull-push
maps in \(\mathsf{Corr}^{E,\mathrm{hyb}}_R\).  The eight-word flag
coherences and four-input pentagon give coassociativity.  Vacuum flags
give the counit identities.  The reduced coproduct lowers bar length, so
\[
(\overline\Delta_R^{\mathrm{bar}})^{N_R+1}=0.
\]

Thus the repair kills, after the hybrid source is supplied,
\[
\mathfrak o^C_R,\quad
\mathfrak o^{\mathrm{fil}}_R,\quad
\mathfrak o^{\mathrm{conil}}_R,\quad
\mathfrak o^{\Delta,\mathrm{ch}}_R,
\]
and takes \(b_{X,R}\) to be the identity of the source bar coalgebra.
The transition residual \(\mathfrak o^{C,\mathrm{tr}}_{R'R}\) vanishes
only if the finite hybrid transition functors preserve ordered collision
flags, quotient compatibilities, and the bar-length filtration.

## Remaining Cobar Obstruction

The source bar-cobar counit gives only a source-internal map:
\[
\varepsilon^{\mathrm{src}}_{\mathrm{bar},R}:
\Omega_E^{\mathrm{ch}}C^{\mathrm{bar}}_{X,R}
\longrightarrow
\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}.
\]
It is not the target comparison.  A source-to-target comparison in this
model is supplied by a chiral algebra quasi-isomorphism
\[
\vartheta_R:
\mathcal F_{X,\sigma,S,\le R}^{\mathrm{hyb}}
\xrightarrow{\simeq}
\mathsf{Den}_{\Delta_5,E,\le R}
\]
with
\[
\Theta_{\mathrm{Kos},R}
=
\vartheta_R\circ
\varepsilon^{\mathrm{src}}_{\mathrm{bar},R}
\]
in the finite homotopy category.

The exact residual is
\[
\mathfrak o^\Omega_R
=
\left(
d_{\Delta}\vartheta_R-\vartheta_Rd_{\mathrm{hyb}},
\vartheta_R\mu_R^{\mathrm{hyb}}
-\mu_{\Delta,R}(\vartheta_R\otimes\vartheta_R),
\vartheta_R\eta_R^{\mathrm{hyb}}-\eta_{\Delta,R},
\vartheta_R\tau^{\mathrm{hyb}}_{R'R}
-\pi^\Delta_{R'R}\vartheta_{R'},
\vartheta_R|_{\Prim}-\iota_R^{\Prim}
\right).
\]

This is the surviving obstruction.  It is source-to-target.  It is not
the target-internal bar-cobar counit.

## Attacks Run

1. Target-internal counit.
   Rejected by `lem:source-target-koszul-separation`.  The domain of the
   target counit contains only target augmentation, target filtration,
   and target operations.  It contains no compact objects, anchors,
   mixed correspondences, quotient functor, protected integration, or
   primitive representatives.

2. Correspondence-only coalgebra.
   A bare finite correspondence category does not determine a coalgebra
   unless the hybrid residual has vanished: proper/admissible pull-push,
   Thom-Sebastiani transport, orientations, quotient-after-correspondence
   data, and flag coherences are needed before the bar cuts are maps.

3. Quotient-first construction.
   Rejected by `cor:no-quotient-first-hybrid-repair`.  Quotienting object
   stacks before forming the mixed and wrapped correspondences erases the
   anchors needed for source collision flags.

4. Nonproper collision pushforward.
   Still a live obstruction inside \(\mathfrak O_{\mathrm{hyb},R}\):
   the \(q\)-maps in local-local, ordered local-wrapped, and
   wrapped-wrapped extension stacks must have proper-support witnesses.

5. Conilpotence failure.
   Healed for the source-bar model by finite HN height and reduced
   bar-length filtration.  If a non-vacuum zero-height summand survived
   the finite quotient, \(N_R\) would not bound bar length; that case is
   outside the repaired statement and must be excluded by the finite HN
   stage.

6. Transition noncontinuity.
   Not killed automatically.  The exact residual is
   \(\mathfrak o^{C,\mathrm{tr}}_{R'R}\), now sharpened to preservation
   of ordered collision flags, quotient compatibilities, and bar length.

7. Primitive mismatch.
   Not killed.  The finite defect
   \(\vartheta_R|_{\Prim}-\iota_R^{\Prim}\) remains part of
   \(\mathfrak o^\Omega_R\), and primitive recognition remains downstream.

## Claim Status

Conditional repair achieved.  If the finite hybrid source is supplied
with \(\mathfrak O_{\mathrm{hyb},R}=0\), the source coalgebra can be
chosen canonically as the reduced source chiral bar coalgebra, with
finite filtration, coaugmentation, counit, collision coproduct,
coassociativity, counit, conilpotence, and identity bar comparison.

Open: construct the hybrid source itself, prove transition continuity,
and construct the source-to-target quasi-isomorphism
\(\vartheta_R\) or \(\Theta_{\mathrm{Kos},R}\).  The target current
envelope still cannot define any of these source data.

## Commands Run

- `git status --short --branch`
- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`, and
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`.
- `sed -n` read of the `chriss-ginzburg-rectify` skill.
- `sed -n` read of
  `/Users/raeez/igusa-cusp-form/notes/sixth_attack_heal_swarm_20260428.md`
  because the sixth ledger was not present in the isolated worktree.
- `rg` scans for `Koszul`, `cobar`, `coalgebra`, `coaug`, `collision`,
  `source-target`, `D_X`, and `hybrid`.
- `nl -ba main.tex | sed -n ...` reads of the source-target separation
  lemma, chiral Koszul source certificate, hybrid section, `(D_X)`, and
  open full-certificate obligation.
- Reads of prior Koszul and hybrid/Koszul reports in `notes/notes/`.
- Cross-repo spot checks in `~/chiral-bar-cobar` and
  `~/chiral-bar-cobar-vol2` for the bar-cobar inversion warning:
  \(\Omega B(A)=A\) is inversion, not source construction.
- `git diff --check -- main.tex`: passed.
- `pdflatex -halt-on-error -interaction=nonstopmode -output-directory=/tmp/igusa-sixth-koszul-cobar-texcheck main.tex`:
  passed as a one-pass syntax check.  It reported expected first-pass
  unresolved references/citations and layout warnings; no fatal TeX
  error occurred.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-sixth-koszul-cobar-texcheck/main.log`:
  no hits.
- `git diff --check -- main.tex notes/sixth_koszul_cobar_attack_heal_report.md`:
  passed.

## Files Changed

- `main.tex`
- `notes/sixth_koszul_cobar_attack_heal_report.md`

Pre-existing dirty and untracked files were observed and not reverted.
