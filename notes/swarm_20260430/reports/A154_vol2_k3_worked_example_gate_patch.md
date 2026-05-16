# A154 -- Vol II K3 Worked-Example Gate Patch

## Claim Attacked

The Vol II K3 worked example directly defined a Hall--Drinfeld double /
Siegel--Borcherds associator / Miki-generator model from
\(\CoHA_{K3\times E}\) and Igusa data.

## Patch

The file now adds the positive-half/full-double distinction, rewrites the
K3 construction as a recognition target, scopes the central-charge
paragraph to recognition data, makes the Hall--Drinfeld formula
conditional, and treats Miki coordinates as a fixture rather than
explicit constructed generators.

## Verification

```text
git diff --check -- chapters/examples/examples-worked.tex
```

passed. Targeted search for \(H_{\Delta_5}\), \(\CoHA_{K3}\), Miki,
recognition, and positive-half found only guarded/conditional hits.

## Changed Paths

- `/Users/raeez/chiral-bar-cobar-vol2/chapters/examples/examples-worked.tex`
