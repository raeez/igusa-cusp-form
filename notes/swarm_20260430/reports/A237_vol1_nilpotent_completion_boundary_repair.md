# A237 Vol I nilpotent_completion Boundary Repair

Runtime id: `019ddcc6-26c8-7660-83b3-65a9b02f2460`.

Changed:
- `/Users/raeez/chiral-bar-cobar/chapters/theory/nilpotent_completion.tex`.

Repairs:
- Replaced the uniqueness corollary with a `\ClaimStatusConditional` `\Delta_5` target criterion.
- Made `H^2(\mathfrak g_{\Delta_5})` conditional on Vol III source-recognition gates plus a proved cohomology/Heegner-characteristic comparison.
- Rephrased local `\mathbf H_{\Delta_5}` passages as Vol III target/comparator language, not Vol I construction.
- Removed the local “classification invariant” overclaim in the Fake-Monster comparison.

Checks:
- `git diff --check -- chapters/theory/nilpotent_completion.tex` passed.
- Targeted `rg` for `H^2(\mathfrak g_{\Delta_5})`, `\mathbf H_{\Delta_5}`, `\Delta_5`, `uniqueness`, `classification`, `classified`, and `unique`.
- Remaining `H^2(\mathfrak g_{\Delta_5})` hits are inside the new conditional criterion/proof.
- Remaining `classification` hit states this is not an unconditional classification inside Vol I.
