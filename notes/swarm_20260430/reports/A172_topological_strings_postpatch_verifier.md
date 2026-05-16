# A172 -- Topological-Strings Postpatch Verifier

## Result

Read-only verification found no high or medium issues after A165.

## Findings

- Low: `tate-P5-cross-volume.tex:963` names
  \(\tau_{\mathrm{DT/PT/OP}}\) while the firewall language includes
  DT/PT/GW/OP at `38` and `235`. If a GW scalar normalization is intended
  in the Igusa/BKM template, it remains an explicit target-normalization
  obligation.
- Low: `971-980` preserve the \(\Delta_5\)/OP scalar equalities as
  target-side constants. A172 did not rederive those constants; their
  proof/source anchors remain external obligations.

## Separation Check

- Scalar equalities are firewalled as target evidence only at `38-44`,
  `235-240`, and `981-988`.
- Compact/global/Hall/CoHA/\(E_2\)/Borcherds/source recognition is
  finite-gate conditional through \(\Gamma_{\mathrm{src}}\) and
  \(\operatorname{ob}_{\mathrm{src/rec}}=0\) at `189-240`, `492-496`,
  and `849-853`.
- Product-disk factorization is separated from arbitrary Weiss/Ran/global
  descent at `615-623` and `691-745`.
- BF/Moyal is restricted to formal-stalk input under
  \(\operatorname{Ob}_{\mathrm{UKD}}(C_{\mathrm{tar}})=0\) at `834-853`
  and `868-893`.

## Checks

- Targeted `rg` for DT/PT/GW/OP, \(\Delta_5\), \(\Phi_{10}\), Borcherds,
  BF/Moyal, factorization, product-disk, Hall/CoHA, \(E_2\),
  compact/source/global/finite-gate language.
- `rg` for stale old obstruction notation: no hits.
- `git diff --check -- tate-P5-cross-volume.tex` passed.

