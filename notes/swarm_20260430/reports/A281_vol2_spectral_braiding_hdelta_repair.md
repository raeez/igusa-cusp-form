# A281 -- Vol II spectral-braiding HDelta repair

Status: completed; isolated patch integrated by master thread.

Isolated worktree: `/tmp/a281-spectral-braiding-hdelta-6e74667`.

Files integrated:
- `chapters/connections/spectral-braiding.tex`
- `chapters/connections/spectral-braiding-core.tex`
- `chapters/connections/spectral-braiding-frontier.tex`

Repairs:
- Added Hall--Borcherds recognition gates and target-package notation.
- Recast `R_{\mathrm{Sieg,dyn}}` as a datum of
  `\mathbf H_{\Delta_5}^{\mathrm{tgt}}`.
- Made Lusztig/order-8 braid closure conditional on integral braid
  comparison and compact source recognition.
- Restricted rational-times-theta QYBE and RTT/qdet claims to the
  rank-24 Mukai-Heisenberg/Miki evaluation block.
- Treated full centre/global braid statements as recognition problems,
  not formal RTT consequences.

Checks:
- Worker `git diff --check` passed in the isolated worktree.
- Master `git apply --check` passed before integration.
- Master `git diff --check` passed on the three integrated files.

Remaining obligations:
- Construct the finite Hall--Borcherds recognition datum.
- Prove the integral braid comparison lifting target monodromy to
  compact source modules.
- Prove any global DYBE beyond the paramodular evaluation block.
