# A066 - Height-Six and Height-Seven Complementary String Rows

## Status

`BLOCKED AS SOURCE THEOREM`. Target relation is imported/proved inside
the GN/Kac Borcherds-Kac presentation; compact Hall source verification
is not proved.

## Complementary String

For `a_{ij}=\delta_i+\delta_j`, `{i,j,k}={1,2,3}`:

```tex
(\delta_k,a_{ij})=-4,\qquad
1-2(\delta_k,a_{ij})/(\delta_k,\delta_k)=5.
```

Thus

```tex
(\operatorname{ad}e_k)^5u_{ij,r}=0
```

is the terminal target Serre row. Anchors: `main.tex` near lines 12666,
14783, and 14856.

Let

```tex
v_s=(\operatorname{ad}e_k)^s u_{ij,r},\qquad
\beta_s=a_{ij}+s\delta_k.
```

| `s` | degree | height | target/source obligation |
|---|---:|---:|---|
| 1 | `\delta_1+\delta_2+\delta_3` | 3 | `v_1=[e_k,u_{ij,r}]`. This is the only complementary string row visible in `W_{\le3}`. Target block `29|93`, with 27 mixed even words. |
| 2 | `a_{ij}+2\delta_k` | 4 | Need `B_{\delta_k,\beta_1}`. Manuscript has signed target `\smult=108`, chamber additive coefficient `m=90`, residual `18`. Source row absent. |
| 3 | `a_{ij}+3\delta_k` | 5 | Need `B_{\delta_k,\beta_2}`, full parity target fixture, source bases, pairing/radical/PBW. Current product arithmetic gives signed `\smult=-64`; source row absent. |
| 4 | `a_{ij}+4\delta_k=s_{\delta_k}(a_{ij})` | 6 | Last nonzero target string row. Need height-six root-space fixture and source row `B_{\delta_k,\beta_3}`. Product arithmetic gives signed `\smult=10`; source decomposition not certified. |
| 5 | `a_{ij}+5\delta_k` | 7 | Terminal zero row: `Q_{\beta_5}B_{\delta_k,\beta_4}(e_k\otimes v_4)=0`. Product arithmetic gives `\smult=0`, but determinant data cannot prove source vanishing. |

Degree triples:

```tex
a_{12}+s\delta_3=(1,1,s),\quad
a_{13}+s\delta_2=(1,s,1),\quad
a_{23}+s\delta_1=(s,1,1).
```

## Failure

The manuscript's `W_{\le3}` criterion cannot prove terminal vanishing. It
only covers rows with `\alpha,\beta,\alpha+\beta\in W_{\le3}`; the rows
`s=2,3,4,5` land in heights `4,5,6,7`. Anchors: `main.tex` near lines
15004, 15096, 15268, and 15339. A058 states the same obstruction.

Guide section 12 agrees that `W_{\le3}` is a source-matrix certificate,
not a consequence of target arithmetic. A051/A052 give the same
firewall.

## Residual Obligation

Introduce an enlarged downward-saturated string window through height 7,
with negatives and `0`, and supply source bases plus `M,D,B,G,K,Q,A_\beta`,
kernel equality, radical ideal/coideal checks, PBW associated-graded
comparison, and transition compatibility. Without that, `W_{\le3}` proves
no height-six row and no height-seven terminal vanishing.

## Commands

Read-only `rg`, `find`, `sed`, `nl -ba`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_lattice.py`;
`PYTHONDONTWRITEBYTECODE=1 python3 compute/verify_square_root.py`; one
read-only Python coefficient table.

## Files Changed

None by the agent.

