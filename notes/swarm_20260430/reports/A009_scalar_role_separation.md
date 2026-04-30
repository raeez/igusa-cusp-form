# A009 report: \(\Delta_5/D_5/\Phi_{10}\) and OP scalar role separation

Runtime id: `019ddbcc-3917-7292-8813-ae3a775a3ebd`.
Nickname: Parfit.
Status: completed.
Files changed by agent: none.

## Verdict

The normalization chain is correct. The scalar firewall is mostly in
place. Remaining risks are wording risks, not formula errors.

## Verified Chain

\[
\Delta_5=64q^{1/2}r^{1/2}s^{1/2}
\prod(1-q^nr^ls^m)^{f(nm,l)}
\]
with \([q^{1/2}r^{1/2}s^{1/2}]\Delta_5=64\). Therefore
\[
D_5=64^{-1}\Delta_5.
\]

OP uses the monic square:
\[
\chi_{10}^{\mathrm{OP}}=D_5^2=(64^{-1}\Delta_5)^2
=4096^{-1}\Delta_5^2.
\]
Hence
\[
Z^X_{\mathrm{OP/DT}}
=-(\chi_{10}^{\mathrm{OP}})^{-1}
=-D_5^{-2}
=-4096\Delta_5^{-2}.
\]

Theta convention:
\[
\Phi_{10}^{\theta}=\Delta_{10}^{\theta}=\Delta_5^2.
\]

OP convention:
\[
\Phi_{10}^{\mathrm{OP}}=\chi_{10}^{\mathrm{OP}}
=D_5^2=4096^{-1}\Delta_5^2.
\]

Thus bare \(-\Delta_5^{-2}\) is not the OP/DT scalar. It is only an
unnormalised shorthand if the missing factor \(4096\) is restored.

## Firewalls

| Risk | Correct firewall |
|---|---|
| \(-\Delta_5^{-2}\) as OP/DT scalar | Wrong unless explicitly unnormalised. OP/DT is \(-4096\Delta_5^{-2}\). |
| \(D_5=\Delta_5\) | Wrong in this manuscript. \(D_5=64^{-1}\Delta_5\). |
| \(\Phi_{10}^{-1}\) unqualified | Ambiguous. \(\Phi_{10}^{\theta}=\Delta_5^2\), but OP uses \(\Phi_{10}^{\mathrm{OP}}=D_5^2\). |
| OP scalar square implies square root | False. OP proves the reciprocal scalar square, not the first-order Pfaffian object. |
| OP minus sign as orientation sign | False. \(-1\) is OP scalar convention; \(\epsilon_o\) is orientation-line monodromy. |
| \(4096\) as degeneracy/anomaly/orientation | False. \(4096=64^2\) is theta-to-monic conversion squared. |
| Scalar equality as orientation evidence | False. Squaring kills \(\Delta_5\mapsto-\Delta_5\) and any sign character. |

## Overclaim Risks

`main.tex:106`: abstract says the missing \(\mathfrak D_X\) has scalar
trace \(-4096\Delta_5^{-2}\). It is fenced by "missing compact object",
but should stay conditional: "if supplied, its scalar shadow must
match...".

`main.tex:785`: "Dirac/Pfaffian recognition target" is framed as a
proposition while existence is open at `main.tex:811`. Safer as
definition/open target.

`main.tex:4259`: "OP scalar sign absorbed into the fermionic shift" is
acceptable only as scalar chamber bookkeeping. It should not be used as
evidence for orientation.

`main.tex:16055`: title "Square-root consequence" can mislead. Content
is safe; title should be "Orientation-forgetting scalar consequence."

## Anchors

Core manuscript anchors:
`main.tex:73`, `main.tex:90`, `main.tex:15922`, `main.tex:15976`,
`main.tex:16094`, `main.tex:16281`, `main.tex:16739`.

Attack/guide anchors:
`notes/attack_whitepaper_analysis_20260430_guide.md:53`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:353`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:5405`,
`materials/processed/2026-04-30-attack-whitepaper-analysis.txt:5971`.

CYQG anchors:
`AP-CY357`, `AP-CY365`.

## Residual Obligations

Primary-source audit remains: OP theorem/product equation/chamber,
Oberdieck--Pandharipande comparison citation, Oberdieck reduced DT/PT
theorem, Bryan variable interchange, GN \(D_5=64^{-1}\Delta_5\), and
\(2Z\) denominator convention. No orientation claim should be
strengthened until O1/O1+/O2 compute \(\epsilon_o\) from type-II wall
monodromy.

Commands run by agent: read-only `sed`, `nl`, `rg`;
`python3 compute/verify_square_root.py`;
`python3 compute/verify_lattice.py`; arithmetic checks; `git status
--short`.
