# Fifth Hybrid Real Attack-Heal Report

Date: 2026-04-28.
Role: H04.
Worktree: `/tmp/igusa-fifth-hybrid`.
Branch: `agent/igusa-fifth-hybrid-real-20260428`.

## Claim Attacked

Obligation (5): construct the real hybrid source
\[
\mathcal F_X^{\mathrm{hyb}}
\]
from finite-stage data: `Ran^{hyb}(E)`, local/wrapped strata, anchored
prequotients, ordered mixed and wrapped correspondences, eight-word flags,
`Q_{E,R}`, `theta^Q`, protected integration, and the residual tuple
`\mathfrak O_{\mathrm{hyb},R}`.

Status: conditional certificate only.  No real finite-stage source was
constructed.  The manuscript now records a stricter obstruction package:
the quotient transition residual and protected-integration transition
residual are explicit, and quotient-first or determinant-only universal
categories are ruled out as source certificates.

## Attacks

1. Support-locality attack.  Positive elliptic degree still dominates
   \(E\) by `lem:projection-e-support-locality-obstruction`; ordinary
   `Ran(E)` locality only sees `b_R=0`.
2. Projection-to-\(E\) obstruction.  A positive-degree wrapped object
   cannot be inserted at a finite Ran point without false support data.
3. Anchor dependence.  The anchor
   `lambda_{\eta,R}: M_{\eta,R}^{wr,rig}->E` is noncanonical but
   necessary; quotienting first erases the relative \(E\)-position used
   by mixed convolution.
4. Ordered mixed correspondence attack.  The current certificate contains
   two-sided ordered mixed maps and the eight triple words, but a universal
   finite correspondence category cannot be declared after quotienting.
5. Quotient-before-correspondence attack.  `Q_{E,R}` must be a functor on
   the finite unreduced correspondence category.  A quotient of object
   stacks followed by a new Hall product loses source stacks, anchors, and
   flag 2-morphisms.
6. Non-proper pushforward and vanishing-cycle admissibility attack.
   Proper-support/admissibility witnesses remain part of the certificate;
   no moduli theorem in the manuscript supplies them for wrapped sectors.
7. Eight-word and four-input attack.  Eight-word associativity and the
   four-input pentagon are required finite flag data.  No associativity is
   imported from the inverse limit.
8. Protected integration attack.  Product, coproduct, primitive, and now
   transition compatibility are residuals.  A trace degree `s^{b_R}` is
   not a source construction.
9. Fake Fock/Hecke repair attack.  A determinant/Fock factor can reproduce
   coefficients after decategorification.  It does not supply source
   correspondences or primitive brackets unless represented by wrapped
   prequotients and mixed Hall actions before the reduced quotient.

## Repairs Inscribed

- `main.tex:5627` adds the protected-integration transition defect
  \[
  \mathfrak o^{I,\mathrm{tr}}_{R'R}
  =
  I_R^{\mathrm{prot}}Q_{E,R}\tau^{\mathrm{hyb}}_{R'R}
  -\pi^\Gamma_{R'R}I_{R'}^{\mathrm{prot}}Q_{E,R'}.
  \]
- `main.tex:5656` inserts `\mathfrak o^{Q,\mathrm{tr}}_{R'R}` and
  `\mathfrak o^{I,\mathrm{tr}}_{R'R}` into the finite hybrid residual
  tuple, and changes the final transition residual to
  `\mathfrak o^{\mathrm{tr}}_{\mathrm{hyb},R'R}`.
- `main.tex:5737` threads `\mathfrak o^{I,\mathrm{tr}}_{R'R}=0` into the
  finite consequences of the certificate.
- `main.tex:5783` adds `cor:no-quotient-first-hybrid-repair`: a
  quotient-first finite category or determinant/Fock category does not
  define the hybrid source.
- `main.tex:5844` strengthens the open problem so protected integration
  must also kill `\mathfrak o^{I,\mathrm{tr}}_{R'R}` for all `R' >= R`,
  and `main.tex:5851` states that the transition components are included
  in the required trivialization of `\mathfrak O_{\mathrm{hyb},R}`.

## Exact Residual Tuple

At finite height \(R\), with transition components read for every
\(R'\ge R\), the hybrid obstruction package is
\[
\mathfrak O_{\mathrm{hyb},R}
=
\left(
\mathfrak o^{\mathrm{stage}}_R,
\mathfrak o^{\lambda}_R,
\mathfrak o^{\mathrm{corr},\mathrm{LL}}_R,
\mathfrak o^{\mathrm{corr},\mathrm{mix}}_R,
\mathfrak o^{\mathrm{corr},\mathrm{WW}}_R,
\{\mathfrak o^{\mathrm{assoc}}_{w,R}\}_{w\in\{\mathrm L,\mathrm W\}^3},
\mathfrak o^{Q,\mathrm{form}}_R,
\mathfrak o^{Q,\mathrm{adm}}_R,
\mathfrak o^{Q,\mathrm{flag}}_R,
\mathfrak o^{Q,\mathrm{tr}}_{R'R},
\mathfrak o^{I,\mathrm{ch}}_R,
\{\mathfrak o^{I,\mathrm{prod}}_{w,R}\}_{w},
\mathfrak o^{I,\mathrm{co}}_R,
\mathfrak o^{I,\Prim}_R,
\mathfrak o^{I,\mathrm{tr}}_{R'R},
\mathfrak o^{\mathrm{tr}}_{\mathrm{hyb},R'R}
\right).
\]

Vanishing of this tuple means: finite HN stage existence, anchor
rigidification, local-local correspondences, all ordered mixed
correspondences, wrapped-wrapped correspondences, eight-word flag
coherence and four-input pentagon, quotient formation/admissibility/flag
and transition descent, protected chain/product/coproduct/primitive and
transition integration, and HN transition compatibility.

## Minimal Obstruction

The minimal unresolved package is:

1. construct the compact extension-closed Hall category and finite HN
   quotients with finite-type local and wrapped moduli;
2. construct rigidified wrapped prequotients and anchors without forcing
   wrapped support into a finite Ran point;
3. construct all ordered local-local, local-wrapped, and wrapped-wrapped
   extension stacks with vanishing-cycle admissibility and proper-support
   witnesses;
4. prove the eight-word flag coherences and four-input pentagon in finite
   quotients;
5. construct `Q_{E,R}` as quotient-after-correspondence functor with all
   quotient residuals zero, including `\mathfrak o^{Q,\mathrm{tr}}_{R'R}`;
6. construct protected integration as a chain-level character with
   product, coproduct, primitive, and transition residuals zero;
7. pass these data compatibly through the HN inverse system.

No external theorem was invoked to fill these hypotheses.  Existing
Borcherds, Gritsenko--Nikulin, Beilinson--Drinfeld, and OP/Oberdieck
sources support the target determinant, denominator, chiral formalism,
and scalar square lanes; they do not construct this compact wrapped
source.

## Commands Run

- `pwd`
- `git status --short --branch`
- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`,
  `/Users/raeez/ecosystem/INVARIANTS.md`,
  `/Users/raeez/ecosystem/AGENTS-HARNESS.md`, and
  `/Users/raeez/igusa-cusp-form/.agents/skills/chriss-ginzburg-rectify/SKILL.md`.
- `rg -n` searches for hybrid, wrapped, `Ran`, `Q_{E,R}`, `theta^Q`,
  `I_R^{prot}`, eight-word flags, quotient, and Koszul anchors in
  `main.tex` and `notes/`.
- `nl -ba main.tex | sed -n ...` reads of the compact/hybrid
  factorization, projection-locality obstruction,
  `def:hybrid-wrapped-factorization-certificate`, `(H_X)`, and the open
  certificate list.
- `sed -n` reads of prior hybrid/Koszul reports:
  `notes/worktree_hybrid_report.md`,
  `notes/next_hybrid_attack_heal_report.md`,
  `notes/third_hybrid_attack_heal_report.md`,
  `notes/fourth_hybrid_koszul_attack_heal_report.md`,
  `notes/next_koszul_attack_heal_report.md`, and
  `notes/third_koszul_attack_heal_report.md`.
- `perl -0pi -e 's/^\t//mg' main.tex` to remove accidental leading-tab
  indentation introduced in the edited TeX block; no mathematical content
  changed by this mechanical cleanup.
- `git add -N notes/fifth_hybrid_real_attack_heal_report.md` so the
  required diff check includes this new report without staging content.
- `git diff --check -- main.tex notes/fifth_hybrid_real_attack_heal_report.md`:
  passed.
- `mkdir -p /tmp/igusa-fifth-hybrid-texcheck`.
- `pdflatex -halt-on-error -interaction=nonstopmode
  -output-directory=/tmp/igusa-fifth-hybrid-texcheck main.tex`: passed.
  The one-pass syntax run reported expected first-pass unresolved
  references/citations and layout warnings, and wrote only to `/tmp`.

## Files Changed

- `main.tex`
- `notes/fifth_hybrid_real_attack_heal_report.md`
