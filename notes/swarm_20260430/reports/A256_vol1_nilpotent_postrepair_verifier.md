# A256 Vol I nilpotent_completion Post-Repair Verifier

Runtime id: `019ddcde-875a-7542-a309-088550904ddb`.

Verdict:
- Pass. No edits made.

Checks:
- `git diff --check -- chapters/theory/nilpotent_completion.tex` passed.
- No exact match for `unconditional through motivic weight~$12$`.
- No `\ClaimStatusProvedHere` attached to the `\mathfrak g_{\Delta_5}` / `\mathbf H_{\Delta_5}` torsor or source-recognition material.
- Obstruction-vanishing language for `\mathfrak g_{\Delta_5}` is marked as a hypothesis, not proved.
- Principal homogeneous / torsor claims are qualified by `\ClaimStatusConditional`, “under these hypotheses,” “under obstruction-vanishing hypothesis,” or target language.

Key anchors:
- `nilpotent_completion.tex:1990`: Vol I does not prove `ob^{GN}` vanishing or Hall-source classification.
- `nilpotent_completion.tex:2020`: K3-BKM torsor theorem is `\ClaimStatusConditional`.
- `nilpotent_completion.tex:2114`: proof denies compact Hall-source classification.
- `nilpotent_completion.tex:2189`: `\mathbf H_{\Delta_5}` criterion remains conditional on Vol III gates plus Heegner comparison.
- `nilpotent_completion.tex:2767`: full BKM transitivity theorem is conjectural; K3 case is conditional.
- `nilpotent_completion.tex:2838`: row `\mathsf B` has only motivic-coordinate window unconditional; target torsor and source recognition remain conditional.
