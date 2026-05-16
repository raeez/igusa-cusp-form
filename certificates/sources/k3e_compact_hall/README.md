# k3e_compact_hall source fixture

This directory is a compact-source fixture scaffold. It is not a compact
Hall source certificate.

The packet is intentionally `mock_empty_blocked`. Its CSV files contain
headers only. The verifier must return `BLOCKED` until a compact source
stage supplies provenance for every source basis vector, parity blocks,
the source matrices `M,D,B,G,K,Q,A`, radical ideal/coideal checks,
relation rows, no-extra kernel equality, PBW associated-graded checks,
strict transitions/Mittag-Leffler data, and the `A_beta` comparison
identities.

Target labels such as `e_i,E_ij,u_ij_r,T_i,M_ij_r,w_s` are forbidden in
source rows. They may occur only in target reference fixtures or in the
codomain coordinates of `A_entries.csv` and target-matrix references used
by `a_beta_comparison_maps.csv`.

The source verifier may consume a target fixture path. It must not
generate target truth, target parity tables, target PBW ranks, or target
basis templates. The verifier is check-only; `--check` is an explicit
spelling of its default mode and does not permit writes or generated truth.
The target path must be a separate existing target reference directory,
not the source packet itself and not any path inside this source packet.

Future populated packets must supply mathematical payload fields in every
CSV row. Status/comment-only rows do not supply a gate, and `degrees.csv`
passes only rows whose `source_block_status` is `source_verified` or
`source_admissible`.

A positive verifier result is `SCHEMA_COMPLETE`: schema, status, payload,
target-reference separation, target-label firewall, and source-degree
firewall checks passed. It is not compact-source certification. The
manifest `certified` field is not proof status for this checker;
certification/external verification belongs to future proof-mode artifacts.
