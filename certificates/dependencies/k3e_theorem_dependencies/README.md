# k3e_theorem_dependencies fixture

This directory is the finite theorem-dependency ledger for the
Dirac--Igusa construction and the cross-level claims around
\(\Delta_5\).  It is schema-complete and fail-closed; it is not a proof
of any theorem.

The packet supplies the thirteen tables required by the verifier:

- `beilinson_levels.csv` records the five finite sites
  \(\mathsf P,\mathsf C,\mathsf S,\mathsf Z,\mathsf A\), their ambient
  categories, primitive objects, allowed equality kinds, and forbidden
  scalar promotions;
- `objects.csv` records typed objects at Beilinson levels \(P,C,S,Z,A\);
- `morphisms.csv` records level-preserving comparison and construction
  morphisms with zero functoriality and level defect ranks;
- `theorem_dependencies.csv` records the seven theorem rows:
  construction, Pfaffian--Dirac, orientation character, primitive
  recognition, scalar trace, mirror discriminant, and gravity-line
  residual;
- `dependency_edges.csv` records the proof edges allowed for each
  theorem row;
- `forbidden_edges.csv` records the proof edges excluded from the
  stronger theorem lanes;
- `status_separation.csv` records non-collapse of proved, relative,
  conditional, conjectural, and open statuses;
- `level_equalities.csv` records the ambient category and Beilinson
  level of each load-bearing equality: pro-object, automorphic
  section, BKM denominator, Pfaffian section, orientation character,
  primitive recognition, Koszul comparison, scalar trace, mirror
  discriminant, and gravity-line residual;
- `equality_sites.csv` records where equality statements live:
  pro-categories, \(K_0\)-groups, Picard groupoids, derived
  categories, completed Lie superalgebras, automorphic line bundles,
  and scalar traces;
- `definition_separation.csv` records non-circular definition order:
  the Pfaffian is not defined from \(\mathcal D_X=\Delta_5\) or its
  desired value, \(P_X\) is not defined from target multiplicities,
  orientation is not defined from scalar signs, the Koszul source is
  not defined from the target counit, and the pro-object is not defined
  from a scalar shadow;
- `obstruction_independence.csv` records finite-row witnesses that no
  named obstruction datum is inferred from another named datum; these
  are theorem-dependency witnesses, not constructed geometric
  counterexamples on \(K3\times E\);
- `transitions.csv` records strict transition of the dependency graph
  along the finite HN and cofinal recognition systems;
- `scalar_firewall.csv` records the substitutions excluded from the
  ledger: automorphic-only, target-only, scalar trace, OP branch,
  mirror conjecture, gravity-line residual, and status collapse.

The required forbidden rows include:

- the automorphic section cannot define the Pfaffian line;
- the denominator product cannot prove primitive recognition;
- the mirror conjecture and gravity-line residual do not enter
  Pfaffian or recognition proofs;
- the scalar trace does not recover orientation or primitive brackets;
- the target counit is not a source Koszul datum;
- target labels are not compact source representatives;
- the Wrel infinite target-tail audit is not a compact-source theorem;
- signed target rows are not parity, pairing, radical, or PBW data.

Run

```sh
python3 compute/verify_dependency_fixture.py \
  --fixture certificates/dependencies/k3e_theorem_dependencies \
  --check --schema-only-ok
```

A positive result is `SCHEMA_COMPLETE_SCHEMA_ONLY` with
`dependency_certification: false` and `mathematical_certification:
false`.  The verifier checks schema, status, payload, required
Beilinson-level rows, required theorem types, required forbidden-edge
types, required scalar-firewall types, required equality-scope types,
required equality-site types, required definition-separation types,
required obstruction-independence rows, zero defect ranks, and row
provenance.
It does not prove the Pfaffian
identity, orientation character, primitive recognition, mirror
discriminant conjecture, scalar trace interpretation, or gravity-line
operator algebra.
