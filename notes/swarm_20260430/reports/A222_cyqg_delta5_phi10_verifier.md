# A222 -- CYQG Delta5/Phi10 verifier

## Claim attacked

The Vol III executable normalization repair might still conflate the
\(\Delta_5\) signed-character lane \(c(D)\) with the doubled
DMVV/\(\Phi_{10}\) lane \(2c(D)\).

## Findings

High:

- `compute/lib/k3e_coha_structure.py` still described the \(c(D)\) product
  as "full DMVV".

Medium:

- The three-path verifier skipped checks when path 1 returned zero, so a
  deleted known discriminant could pass.
- A local manuscript passage still used root multiplicity notation for
  signed data.

## Integration

The main thread:

- rewrote API prose to call the \(c(D)\) product the \(\Delta_5\)
  Borcherds signed-character lane and reserved DMVV/\(\Phi_{10}\) for the
  doubled lane;
- removed the `path1 != 0` skip;
- added a missing-discriminant regression test;
- changed the local constancy passage to signed root-character
  \(\operatorname{sch}=\operatorname{sdim}=c_0(D)\).

## Verification

`pytest -q -p no:cacheprovider compute/tests/test_k3e_coha_structure.py`
passed with `99` tests after integration.
