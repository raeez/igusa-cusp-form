# Third D0/source attack-heal report

Date: 2026-04-28.
Worktree: `/tmp/igusa-third-d0-source`.
Branch: `agent/igusa-third-d0-source-20260428`.

## Claim attacked

The finite first-order \(D_0\) lane was attacked at the source boundary:
whether \(D_{0,R}\), \(\widehat\Gamma_R\), transition compatibility,
source/observable comparison, and Pfaffian parity conditions were strong
enough to prevent a hidden existence theorem or a missing-factor error.

Status before repair: safe in intention, still under-specified in the
finite Pfaffian test.  The previous residual
\(\mathfrak o^{\mathrm{par}}_{R,\gamma}\) detected extra signed support
inside \(\Gamma_R^\Pi\), but it did not separately detect missing
Borcherds target degrees or invisible even-odd cancelling source pieces in
target-zero degrees.

## Failure/proof and heal

1. \(D_{0,R}\) and \(\widehat\Gamma_R\).
   - Attack: the inverse-limit notation could still be read as producing a
     compact state object before the finite transitions were checked.
   - Heal: `main.tex:880` now says the completed object is part of the
     supplied certificate only after finite stages, transition cocycles, and
     support/parity residuals vanish.  `main.tex:6263` defines all finite
     test data before the inverse limit is named.
   - Proof: finiteness of \(\widehat\Gamma_R\) follows from finite
     \(F_{\sigma,S}(R)\), bounded HN length, and finite possible
     \(\sum_{i<j}B(c_i,c_j)\); see `main.tex:6750`.

2. Target-window coverage.
   - Attack: checking only \(\Gamma_R^\Pi\) can miss a nonzero target factor
     if the compact source has not produced that Gram degree.
   - Heal: `main.tex:6272` introduces the proper height
     \[
     h_\Delta(n,l,m)=|n|+|l|+|m|,
     \quad
     \Gamma_{\Delta,R}
     =\{\gamma\in\Gamma_{\mathrm{eff}}\setminus\{0\}\mid
     h_\Delta(\gamma)\le R\},
     \]
     and the finite test set
     \[
     \Gamma_R^{\mathrm{test}}
     =(\Gamma_R^\Pi\setminus\{0\})\cup\Gamma_{\Delta,R}.
     \]
   - Proof: properness makes \(\Gamma_{\Delta,R}\) finite and the windows
     exhaust \(\Gamma_{\mathrm{eff}}\setminus\{0\}\); see
     `main.tex:6757`.

3. Transition residuals \(\mathfrak o^{\mathrm{tr}}_{R'R}\).
   - Attack: transition maps were named, but the finite truncation target was
     not explicit enough.
   - Heal: `main.tex:6320` now states that the transition maps are
     degree-truncation maps over \(\widehat\Gamma_R\), \(\Gamma_R^\Pi\),
     and \(\Gamma_R^{\mathrm{test}}\), and that the residual lives in
     finite Hom spaces over the test window.
   - Status: conditional finite datum.  Vanishing is not formal from inverse
     limits.

4. Source/observable residual \(\mathfrak o^{obs}_R\).
   - Attack: a comparison with \(\mathsf{Den}_{\Delta_5,E}\) could be
     mistaken for primitive recognition.
   - Heal: `main.tex:6460` restricts the finite residual to product,
     coproduct, bracket, trace, and constant-current primitive comparison
     over \(\Gamma_R^{\mathrm{test}}\), and explicitly excludes
     injectivity, surjectivity, presentation-level isomorphism, and
     no-extra-relations.
   - Status: conditional source-to-target morphism residual, not a full
     recognition theorem.

5. Pfaffian support/parity residuals.
   - Attack: signed superdimension equality can hide actual compact source
     primitives with cancelling parity in target-zero degrees; it also does
     not detect missing target factors outside \(\Gamma_R^\Pi\).
   - Heal: `main.tex:6584` separates
     \[
     \mathfrak o^{\mathrm{supp}}_{R,\gamma}
     =
     \begin{cases}
     P^\Pi_{R,\gamma},&a_\Delta(\gamma)=0,\\
     0,&a_\Delta(\gamma)\ne0,
     \end{cases}
     \]
     from
     \[
     \mathfrak o^{\mathrm{par}}_{R,\gamma}
     =
     \dim P^\Pi_{R,\gamma,\bar0}
     -\dim P^\Pi_{R,\gamma,\bar1}
     -a_\Delta(\gamma),
     \]
     for every \(\gamma\in\Gamma_R^{\mathrm{test}}\), with
     \(P^\Pi_{R,\gamma}=0\) if \(\gamma\notin\Gamma_R^\Pi\).  The leading
     coefficient residual remains
     \[
     \mathfrak o^{\mathrm{lead}}_R
     =\operatorname{lc}_{\mathfrak c_\infty}(\operatorname{pf}_{X,R})-64.
     \]
   - Status: support vanishing is an actual super-vector-space condition in
     target-zero degrees.  For nonzero target multiplicity the Borcherds
     product fixes only signed superdimension, not a canonical even/odd
     split.

6. Exact open construction target.
   - Attack: the open problem did not name target-window coverage and actual
     zero-degree support as separate obligations.
   - Heal: `main.tex:7525` now lists transition cocycles, observable
     residuals on \(\Gamma_R^{\mathrm{test}}\), support residuals,
     signed-parity residuals, target-window coverage, and leading
     coefficient normalization as explicit open \(D_0\)-Pfaffian
     obligations.

## Constants and formulas

- Normal-ordered support:
  \[
  \widehat\Gamma_R
  =\{(c,T)\mid c\in\Gamma_R^{HN},\ T\in\mathcal T_R(c)\},
  \quad
  \Gamma_R^\Pi=\overline\Pi_X(\widehat\Gamma_R).
  \]
- Target exponent:
  \[
  a_\Delta(n,l,m)=
  \begin{cases}
  f(nm,l),&(n,l,m)\in\Gamma_{\mathrm{eff}},\\
  0,&(n,l,m)\notin\Gamma_{\mathrm{eff}}.
  \end{cases}
  \]
- Target/test windows:
  \[
  \Gamma_{\Delta,R}
  =\{\gamma\in\Gamma_{\mathrm{eff}}\setminus\{0\}\mid
  |\gamma_1|+|\gamma_2|+|\gamma_3|\le R\},
  \quad
  \Gamma_R^{\mathrm{test}}
  =(\Gamma_R^\Pi\setminus\{0\})\cup\Gamma_{\Delta,R}.
  \]
- Pfaffian leading constant: \(64\).
- OP scalar square remains imported and orientation-forgetful:
  \(-4096=-(64)^2\).

## Claim-status recommendation

- Proved: finite \(\widehat\Gamma_R\), finite \(\Gamma_R^\Pi\), finite and
  exhausting \(\Gamma_{\Delta,R}\), finite \(\Gamma_R^{\mathrm{test}}\), and
  additivity of \(\overline\Pi_X\).
- Imported: \(\mathsf{Den}_{\Delta_5,E}\),
  \(\mathfrak g_{\Delta_5}\), and the Borcherds--Gritsenko--Nikulin
  product with leading coefficient \(64\).
- Conditional: \(D_{0,R}\), transition maps, \(\mathfrak o^{obs}_R\),
  \(\mathfrak o^{\mathrm{supp}}_{R,\gamma}\),
  \(\mathfrak o^{\mathrm{par}}_{R,\gamma}\), and
  \(\mathfrak o^{\mathrm{lead}}_R\).
- Open: construction of the compact source-side Hall/factorization stages,
  quotient/orientation trivializations, hybrid source object, cyclic
  normal-ordering lift, Pfaffian line, first-order object, and compact
  parity pieces.

## Files changed

- `main.tex`
- `notes/third_d0_source_attack_heal_report.md`

## Checks run

- `git diff --check` - passed.
- `python3 compute/verify_lattice.py` - passed.
- `python3 compute/verify_square_root.py` - passed.
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-third-d0-texcheck main.tex` - passed as a one-pass TeX syntax check after creating the output directory.  Expected undefined reference and citation warnings remain because BibTeX and reruns were not invoked.
- `rg -n "Undefined control sequence|Emergency stop|Fatal error|^!" /tmp/igusa-third-d0-texcheck/main.log` - no hits.

## Remaining open questions

Construct \(D_{0,R}\) for every \(R\).  Prove transition compatibility and
the transition cocycle identity.  Construct the source observable shadow
and prove \(\mathfrak o^{obs}_R=0\).  Construct the Pfaffian line and
compact parity pieces, prove actual support vanishing in target-zero
degrees, prove signed multiplicity equality on
\(\Gamma_R^{\mathrm{test}}\), and normalize the leading coefficient to
\(64\).  Only then can the HN-completed compact first-order object be used
as hypothesis (D0).
