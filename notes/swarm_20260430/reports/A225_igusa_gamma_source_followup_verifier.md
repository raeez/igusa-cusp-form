# A225 -- Igusa gamma-source follow-up verifier

## Result

Initial result: repair incomplete. The verifier found source-coordinate
leaks in NO7 and finite matrix text:

- \(P^X_{R,\beta,\bar p}\), \(K_\beta\), \(Q_\beta\);
- source pairing blocks \(G_\alpha,G_\beta,G_{\alpha+\beta}\);
- \(k\in K_\rho\) and \(Q_\mu\otimes Q_\nu\) in the coideal failure
  example.

## Integration

The main thread rewrote the global NO7 text and the finite source matrix
criterion so source blocks use Gram labels. It also clarified that a
separate geometric proposition uses Greek letters as Gram degrees, not
BKM root labels.

## Verification

After integration:

```bash
rg -F 'P^X_{R,\beta' 'P^\Pi_{R,\beta' 'K_\beta' 'Q_\beta' 'G_\beta' main.tex
git diff --check -- main.tex
```

The leak scan returned no hits and diff check passed.
