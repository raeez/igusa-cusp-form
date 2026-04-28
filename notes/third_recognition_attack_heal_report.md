# Third primitive recognition/PBW attack-heal report

Date: 2026-04-28.

## Claim attacked

The attacked shortcut was:
\[
\smult(\delta_1+\delta_2+\delta_3)=-64
\quad\Longrightarrow\quad
\text{primitive recognition in the first timelike channel}.
\]

This shortcut is false.  The signed exponent is only the difference of
two parity dimensions.  It does not give compact generators, Hall
constants, the Hopf pairing, the closed radical quotient,
no-extra-relations, generation, or completed PBW.

## Manuscript heal

- Strengthened Theorem `thm:primitive-recognition` so the compact
  Borcherds--Kac relation check explicitly includes the primitive
  isotropic roots
  \[
  a_{ij}=\delta_i+\delta_j,\qquad u^{\pm,X}_{ij,r},\quad 1\le r\le9,
  \]
  their adjacent real-root zero relations, and the complementary
  real-string relations
  \[
  (\operatorname{ad}e_k^X)^5u^{+,X}_{ij,r}=0,\qquad
  (\operatorname{ad}f_k^X)^5u^{-,X}_{ij,r}=0.
  \]
- Made the Hopf-radical clause matrix-level: finite-height
  positive-negative pairing matrices must have the same parity-block
  ranks as the Gritsenko--Nikulin/Kac invariant pairing.  Radical rank is
  computed from pairing matrices, not from the signed determinant.
- Added Proposition `prop:delta123-presentation-count`.  It computes the
  first timelike target parity dimensions:
  \[
  [qrs]\left(D_5/(qrs)^{1/2}\right)=93,\qquad
  m(\delta_{123})=-93,
  \]
  hence
  \[
  \rootmult_{\overline0}(\delta_{123})=29,\qquad
  \rootmult_{\overline1}(\delta_{123})=93.
  \]
- Updated the low-degree compact test: the source must now produce
  \(29\) even and \(93\) odd compact primitives in degree \((1,1,1)\),
  compute the even Hall constants
  \[
  [e_k^X,u^X_{ij,r}]
  =\sum_{a=1}^{29}C^{\overline0}_{k;ijr,a}v^{\overline0}_a,
  \]
  verify \(T_1^X+T_2^X+T_3^X=0\), the real-string relations, the
  \(29|93\) Hopf-pairing block ranks, and the closed radical quotient.

## Target-side count

The count is not inferred from \(-64\).  It uses three inputs:

- Weyl-sum coefficient:
  \[
  c_\Delta(3,3,3)=64\cdot93,\qquad m(\delta_{123})=-93.
  \]
- Lower even presentation words:
  \[
  2\quad\text{real-real-real Jacobi words}
  \]
  and
  \[
  3\cdot9=27\quad\text{mixed real-isotropic words}.
  \]
- GN/Kac parity convention: the negative \(m(\delta_{123})\) gives
  \(93\) odd imaginary simple generators.

Thus the target presentation gives \(29-93=-64=f(1,1)\).  The equality
with the product exponent is a check, not the source of the parity
dimensions.

## Remaining obstruction

Construct the compact finite-first Hall/factorization source and compute
the recognition data.  The first finite obstruction is now sharper:
produce the actual \(29|93\) compact basis in the
\(\delta_1+\delta_2+\delta_3\) channel, compute the Hall constants and
pairing matrices, prove the closed Hopf-radical quotient, and then prove
no-extra-relations, generation, and completed PBW in the finite-height
inverse system.

## Files changed

- `main.tex`
- `compute/verify_square_root.py`
- `notes/third_recognition_attack_heal_report.md`

## Commands run

- `sed -n` reads of `CLAUDE.md`, `AGENTS.md`,
  `.agents/skills/chriss-ginzburg-rectify/SKILL.md`,
  `notes/worktree_semantic_merge_audit_20260428.md`, and
  `notes/next_recognition_attack_heal_report.md`.
- `rg` and `nl -ba` reads of the primitive recognition theorem,
  low-degree denominator-bracket proposition, denominator algebra, and
  coefficient definitions in `main.tex`.
- `python3 compute/verify_square_root.py`: confirmed
  \(f(1,1)=-64\), \([qrs]D_5/(qrs)^{1/2}=93\), and
  \(m(\delta_{123})=-93\).
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/igusa-third-recognition-texcheck main.tex`:
  passed.  The single pass reports expected unresolved references and
  citations because it was not a full `make` build.
- `git diff --check`: passed.
- `git add main.tex compute/verify_square_root.py notes/third_recognition_attack_heal_report.md`.
- `git diff --cached --check`: passed.
