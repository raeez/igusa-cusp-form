# A012 report: OP scalar square and citation-role audit

Runtime id: `019ddbcc-5496-7b32-adbf-385bf9377a24`.
Nickname: Huygens.
Status: completed.
Files changed by agent: none.

## Citation-Role Audit

Survives.

Oberdieck--Pixton is correctly used for the primitive reduced GW Igusa
theorem and product normalization:
\[
Z_{\mathrm{OP}}=-1/\chi_{10},
\]
with \(p=e^{iu}\) and the product defining \(\chi_{10}\).

Oberdieck--Pandharipande is correctly used for the primitive GW/PT bridge
with \(y=-e^{iu}\); the arXiv source counter makes this Proposition 5.

Oberdieck 2018 is correctly used for quotient/incidence PT equality and
reduced DT/PT, Theorem 1 and Theorem 3(i).

Bryan is only safe as reduced Hilbert-scheme DT definition, variable
convention, and conjectural background, not as the proof of full
DT = Igusa.

## Formula Normalization

Correct:
\[
\chi_{10}^{\mathrm{OP}}
=D_5^2
=(64^{-1}\Delta_5)^2
=4096^{-1}\Delta_5^2,
\]
hence
\[
Z_{\mathrm{OP}}
=-(\chi_{10}^{\mathrm{OP}})^{-1}
=-4096\Delta_5^{-2}.
\]

Local anchors:
`main.tex:15894`, `main.tex:15976`, `main.tex:16094`.

CYQG anchor:
`AP-CY357`.

## Quarantine Audit

Mostly healed. The manuscript repeatedly states that \(64\), \(4096\),
and the OP minus are scalar normalization data, not orientation monodromy.

Anchors:
`main.tex:106`, `main.tex:312`, `main.tex:2841`, `main.tex:3168`,
`main.tex:3257`, `main.tex:16094`, `main.tex:16281`.

CYQG anchors:
`AP-CY350`, `AP-CY357`, `AP-CY365`.

## Overclaim Risks

Minor naming risk:
"OP's normalization" at `main.tex:124` and `main.tex:324` should say
"Oberdieck--Pixton's" to avoid AP-CY350 ambiguity with
Oberdieck--Pandharipande.

Minor credit risk:
`main.tex:18270` credits the primitive reduced scalar branch only to
Oberdieck--Pixton. If that sentence includes DT/PT equality, it should
name Oberdieck and Oberdieck--Pandharipande too.

Wording risk:
`main.tex:4253` says the OP scalar sign is "absorbed into" the fermionic
shift. It then says "not into the orientation line," so the claim is
quarantined, but "recorded by" would be cleaner.

## Primary Sources Checked

arXiv source streams:

- Oberdieck--Pixton 1706.10100: `https://arxiv.org/abs/1706.10100`
- Oberdieck--Pandharipande 1411.1514: `https://arxiv.org/abs/1411.1514`
- Oberdieck 1605.04631: `https://arxiv.org/abs/1605.04631`
- Bryan 1504.02920: `https://arxiv.org/abs/1504.02920`

## Residual Obligation

Confirm final journal PDF theorem/equation numbering if the manuscript
wants DOI-publication numbering rather than arXiv-source numbering.

Commands run by agent:
read-only `sed`, `nl -ba`, `rg`, `find`, `ls`; arXiv source inspection
via `curl | gunzip -c` and `curl | tar -xzOf`. No git commands. No
build.
