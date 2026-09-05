---
name: chriss-ginzburg-rectify
description: Restructure an Igusa Square Root proof region or introduction when its mathematical argument requires structural repair. Use local edits for isolated corrections.
---

# Structural mathematical repair

Identify the requested region, its intended result, and the defect in its argument.
Read that region with its definitions, hypotheses, cited results, and affected dependents.
Read relevant sections of `docs/igusa-research-reference.md`, resolved from the repository root.
Consult appendix sources, investigation notes, and companion volumes only when the claim depends on them.

For a Borcherds determinant, BKM denominator, K3×E realization comparison, or Igusa square root,
make the lattice, Weyl vector, multiplier, and retained data explicit before use.
A worked Fourier coefficient or exponent computation can expose the obstruction before the general result.
Use `compute/verify_lattice.py` or `compute/verify_square_root.py` when the changed claim concerns their fixtures.
Inspect other local verifiers when the claim requires a different arithmetic check.

Choose structural changes that resolve the demonstrated defect. Preserve substantive mathematical content.
Organize around the governing identity, comparison, or obstruction.
Use decomposition tables or precise cases when they clarify the argument.
Rewrite a region when local patches leave dependencies unclear. Do not require fixed rewriting passes.
Test the repaired argument against plausible failures: signs, characters, Weyl vectors, divisors, multipliers, exponents, or categorical levels.

Preserve the theorem target and repair the proof or construction. State discovered gaps honestly.
Do not present unsupported sentences as theorems or treat demotion as completion of theorem repair.
Conclude when the requested result has checkable evidence, or report the exact unresolved obligation,
failed routes, and next discriminating step. An unresolved investigation is not a proved obstruction.

Keep workflow, agents, and repair history outside manuscript sources, including metadata.
Use literal mathematical prose. No mannered prose.
Verify coherent TeX changes through an isolated local build under the root contract.
Report proof evidence separately from compilation and finite arithmetic checks.
