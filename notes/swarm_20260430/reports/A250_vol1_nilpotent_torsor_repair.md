# A250 Vol I nilpotent_completion Torsor Repair

Runtime id: `019ddcd6-bc8a-7971-9192-77717f803212`.

Changed:
- `/Users/raeez/chiral-bar-cobar/chapters/theory/nilpotent_completion.tex`.

Repairs:
- Rewrote the K3-BKM transitivity remark as target-side and conditional.
- Retitled the super-EK/GRT torsor theorem and changed it to `\ClaimStatusConditional`.
- Separated affine/EK/motivic mechanisms from the K3 imaginary-cone hypothesis.
- Preserved the conditional `\Delta_5` criterion under Vol III source gates plus cohomology/Heegner comparison.
- Retargeted the Full BKM locus theorem to conditional target loci.
- Rewrote the landscape-row remark so the K3 row is not unconditionally classified through weight 12.

Checks:
- `git diff --check -- chapters/theory/nilpotent_completion.tex` passed.
- No hits for `ClaimStatusProvedHere` in the checked `\mathfrak g_{\Delta_5}` window.
- No hits for exact `unconditional through motivic weight~$12$`.
- No hits for `obstruction.*vanishes for $\mathfrak g_{\Delta_5}$`.
- Torsor/principal-homogeneous hits remain only in conditional target or affine contexts.

Residual risk:
- No TeX build was run; cross-volume Vol III labels were not build-graph verified.
