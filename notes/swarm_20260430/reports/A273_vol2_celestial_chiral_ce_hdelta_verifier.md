# A273 -- Vol II celestial/chiral-CE HDelta verifier

Status: completed; evidence integrated.

Claim attacked: Vol II celestial and chiral-CE passages were using
`\mathbf H_{\Delta_5}` as a constructed Vol II object rather than a
gated K3 target package.

Findings:
- `chiral_ce_factalg_gen_rel.tex` had already been repaired:
  `thm:ch-ce-k3-avatar-24-punctures` is conditional and names finite
  Hall--Borcherds recognition gates.
- `celestial_holography.tex` needed conditional gates in the Costello
  5-brane item, the CE theorem for `\mathfrak g_{\Delta_5}`, the
  bulk-boundary conjecture, and the `M_{24}`/Serre-cocycle theorem.

Integration:
- The master thread patched `celestial_holography.tex` so the K3
  package is `\mathbf H_{\Delta_5}^{\mathrm{tgt}}` or
  `\mathbf H_{\Delta_5}^{\mathrm{rec}}` as appropriate.
- The CE construction is now conditional on finite Hall--Borcherds
  recognition and the comparison map, not on Costello alone.
- The `M_{24}` action is projective through a chosen
  `\widetilde M_{24}` lift; the twined trace is conditional/expected.

Checks:
- `git diff --check` passed on the touched Vol II files.

Remaining obligation: A279 was launched to re-verify the patched
celestial/chiral-CE/HT/six-d cluster.
