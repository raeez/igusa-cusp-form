# A220 -- Igusa post-gamma-source verifier

## Claim attacked

The post-A214 Igusa patch still risked using the BKM root \(\beta\) as a
compact Hall source coordinate.

## Findings

High:

- A proof sentence still used \(P^X_{R,\beta,\bar p}\).
- The adjacent finite source matrix criterion used beta-indexed source
  blocks.

Pass:

- Finite colored normal form and central-label atlas used
  \(\gamma_\beta\in\Gamma_{\mathrm{gram}}\) with
  \(\alpha(\gamma_\beta)=\beta\).
- `compute/verify_source_fixture.py` checks secondary statuses and fails
  closed on the header-only mock source packet.

## Integration

The main thread rewrote the provenance-gate proof and matrix criterion
so source domains, kernels, quotients, pairings, and transitions use
\(\gamma_\beta\), while root-indexed matrix names remain root labels.

## Verification

After integration: fixed-string Igusa leak scan returned no hits;
`git diff --check -- main.tex` passed; source verifier returned
`BLOCKED`.
