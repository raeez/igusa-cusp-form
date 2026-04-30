# A076 - Certificate Repository Integration Plan

## Observed

A067 proposes `certificates/wle3/<certificate_id>/` as the source fixture
packet. A071/A072 were only live when A076 ran, so A076 did not treat
them as archived evidence.

## Proposed Layout

```text
certificates/
  INDEX.md
  schemas/
    source_fixture.schema.yaml
    verifier_run.schema.yaml
  targets/delta5_gn_kac/<target_fixture_id>/
    manifest.yaml
    target_basis.csv
    target_dimensions.csv
    target_relations.csv
  wle3/<certificate_id>/
    manifest.yaml
    degrees.csv
    basis_provenance.csv
    pairs.csv
    decompositions.csv
    matrix_index.csv
    matrices/{M,D,B,G,K,Q,A}_entries.csv
    relation_rows.csv
    pbw.csv
    no_extra.csv
    transitions.csv
    ml_stable_images.csv
    orientation_protected.csv
    verification/<run_id>/
      run_manifest.yaml
      summary.json
      residuals.csv
      relation_failures.csv
      hashes.txt
      stdout.txt
  wle7/<certificate_id>/
    same schema, with relation_rows closing height-four/six/seven terminal rows
```

Use ASCII ids: `wle3-R<stage_slug>-<yyyymmdd>-<hash12>` and
`wle7-R<stage_slug>-<yyyymmdd>-<hash12>`. `manifest.yaml` must carry
`window`, `stage_R`, `degree_set`, `target_fixture_id`,
`source_target_firewall: true`, full table hashes, and status. Target
labels stay only in `certificates/targets/...` and `A_entries.csv`,
matching A067.

## Directory Roles

`certificates/`: canonical populated fixture packets and committed
verifier outputs. These are evidence artifacts, not notes.

`compute/`: verifier and generator code only. Existing target-side
scripts stay there; future additions should be things like
`verify_source_fixture.py`, `build_target_fixture.py`, and schema
validators. Do not store populated source CSVs in `compute/`.

`notes/`: proposal reports, attack-heal traces, synthesis ledgers.
A067/A069/A070 live here as design evidence only. Future A071/A072
reports should be archived here, then distilled into schemas/verifiers.

`materials/`: raw and processed external inputs: critique PDFs,
extracted text, raw source dumps before normalization. Normalized fixture
tables move to `certificates/`; `basis_provenance.csv` can point back to
material ids.

## Manuscript Integration

`main.tex` should cite mathematical criteria, not notes. Anchors already
exist: source matrices near `main.tex` line 13836, comparison maps near
line 14012, `W<=3` window near line 15004, finite source criterion near
line 15268, NO7 protocol near line 15373.

When populated, add only a short artifact sentence or proposition: "The
hypotheses of Theorem X on `W_{\le3}` are verified by certificate
`<certificate_id>` and verifier run `<run_id>` under `certificates/...`."
Do not `\input` generated `.tex`; do not cite `notes/swarm...`. If
formal bibliography is desired, add a `proj.bib` dataset-style entry
pointing to the certificate path and hashes.

Supremum rule: `W_{\le3}` is a finite source certificate, not relation
closure. `W_{\le7}` must be a separate populated packet closing the
A065/A066 terminal rows; it must not be inferred from target arithmetic
or from the `W<=3` packet.

No files edited by the agent.

