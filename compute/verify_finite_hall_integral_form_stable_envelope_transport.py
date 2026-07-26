#!/usr/bin/env python3
"""Verify the row-368 finite Hall integral-form/stable-envelope packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_integral_form_stable_envelope_transport.v1"
EXPECTED_KIND = "finite_hall_integral_form_stable_envelope_transport_obstruction"
SUCCESS_STATUS = "FINITE_HALL_INTEGRAL_FORM_STABLE_ENVELOPE_TRANSPORT_OBSTRUCTION_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_integral_form_stable_envelope_transport")

ROW367_FIXTURE = Path("certificates/hall/finite_hall_hopf_radical_ideal_coideal")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")
D0_FIXTURE = Path("certificates/d0/k3e_d0_hn")
O2_FIXTURE = Path("certificates/wall_atlas/k3e_o2_atlas")

ROW367_STATUS = "FINITE_HALL_HOPF_RADICAL_IDEAL_COIDEAL_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
D0_STATUS = "D0_OBSTRUCTION_LEDGER_VERIFIED"
O2_STATUS = "O2_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row367_hopf_radical": ROW367_STATUS,
    "compact_hall_source": COMPACT_SOURCE_STATUS,
    "d0_hn": D0_STATUS,
    "o2_atlas": O2_STATUS,
    "maulik_okounkov_scope": "QUIVER_VARIETY_STABLE_ENVELOPE_SCOPE_RECORDED",
    "schiffmann_vasserot_scope": "AFFINE_A0_TORIC_SCOPE_RECORDED",
    "ks_coha_scope": "COHA_DRINFELD_DOUBLE_SCOPE_RECORDED",
}

EXPECTED_SCOPE = {
    "maulik_okounkov_quiver_variety": ("not_proved_for_compact_k3e", "true"),
    "schiffmann_vasserot_affine_a0": ("not_proved_for_compact_k3e", "true"),
    "kontsevich_soibelman_coha": ("not_proved_for_compact_k3e", "true"),
    "compact_k3e_non_toric": ("open_conditional", "false"),
}

EXPECTED_COVERAGE = {
    "datum_count": 1,
    "scope_rows": 4,
    "integral_form_rows": 0,
    "completion_rows": 0,
    "drinfeld_double_rows": 0,
    "stable_envelope_rows": 0,
    "cartan_rows": 0,
    "compact_source_A_entries": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "compact_source_radical_ideal_coideal_rows": 0,
    "compact_source_transition_rows": 0,
    "d0_retained_rows": 0,
    "o2_wall_chart_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "integral_form_definition",
    "integral_form_product_stability",
    "integral_form_coproduct_stability",
    "integral_form_pairing_stability",
    "completion_separated",
    "completion_complete",
    "drinfeld_double_definition",
    "drinfeld_cross_relations",
    "stable_envelope_transport",
    "compact_non_toric_replacement",
    "cyqg_comparison_constants",
    "cartan_part_definition",
    "cartan_lattice_identification",
    "primitive_cartan_survival",
    "toric_theorem_replacement",
}

REQUIRED_FIREWALL = {
    "maulik_okounkov_quiver_theorem",
    "schiffmann_vasserot_toric_theorem",
    "coha_framework_statement",
    "w_1_infty_fock_evaluation",
    "drinfeld_double_not_input",
    "target_bkm_denominator",
    "compact_source_empty",
    "physical_duality",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]
    allow_empty: bool = False


TABLE_SPECS = (
    TableSpec(
        "source_rows.csv",
        (
            "source_id",
            "source_kind",
            "source_path_or_key",
            "source_status",
            "input_payload",
            "output_payload",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "datum_rows.csv",
        (
            "datum_id",
            "integral_form_required",
            "product_stability_required",
            "coproduct_stability_required",
            "pairing_stability_required",
            "completion_separated_required",
            "completion_complete_required",
            "drinfeld_double_required",
            "cross_relations_required",
            "cartan_identification_required",
            "primitive_cartan_survival_required",
            "stable_envelope_transport_required",
            "compact_non_toric_replacement_required",
            "cyqg_comparison_required",
            "datum_recorded",
            "current_source_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scope_rows.csv",
        (
            "scope_id",
            "source_label",
            "proved_context",
            "compact_k3e_applicability",
            "transport_claim_status",
            "forbidden_import",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "integral_form_rows.csv",
        (
            "row_id",
            "R_id",
            "lattice_id",
            "degree_id",
            "product_stable",
            "coproduct_stable",
            "pairing_stable",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "completion_rows.csv",
        (
            "row_id",
            "R_id",
            "completion_id",
            "separated",
            "complete",
            "topology_id",
            "ml_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "drinfeld_double_rows.csv",
        (
            "row_id",
            "R_id",
            "double_id",
            "positive_half_id",
            "negative_half_id",
            "cartan_id",
            "cross_relation_id",
            "hall_pairing_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "stable_envelope_rows.csv",
        (
            "row_id",
            "R_id",
            "moduli_id",
            "chamber_id",
            "fixed_locus_id",
            "support_axiom",
            "normalization_axiom",
            "degree_axiom",
            "transport_matrix_id",
            "compact_non_toric_proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "cartan_rows.csv",
        (
            "row_id",
            "R_id",
            "cartan_id",
            "lattice_id",
            "primitive_survival_status",
            "bracket_row_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "coverage_rows.csv",
        (
            "coverage_id",
            "claim_kind",
            "computed_value",
            "expected_value",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "blocked_obligations.csv",
        (
            "obligation_id",
            "lane",
            "required_artifact",
            "required_table",
            "required_row_type",
            "mathematical_payload",
            "why_required",
            "compatibility_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_firewall.csv",
        (
            "firewall_id",
            "forbidden_substitute",
            "excluded",
            "defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "text_requirements.csv",
        (
            "requirement_id",
            "file_path",
            "required_fragment",
            "fragment_present",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"json root is not an object: {path}")
    return value


def read_table_path(
    path: Path,
    columns: tuple[str, ...] | None = None,
    *,
    allow_empty: bool = False,
) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if columns is not None and tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
    if not rows and not allow_empty:
        raise ValueError(f"{path}: expected at least one row")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns, allow_empty=spec.allow_empty)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_true(value: object, label: str) -> None:
    require_equal(value, True, label)


def require_false(value: object, label: str) -> None:
    require_equal(value, False, label)


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"{key}: expected integer cell, got {row.get(key)!r}") from exc


def require_table_empty(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    if rows:
        raise ValueError(f"{path}: expected no rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("row_number"), 368, "row_number")

    for key in (
        "comparison_datum_recorded",
        "row367_hopf_radical_packet_imported",
        "compact_hall_source_ledger_imported",
        "d0_obstruction_ledger_imported",
        "o2_obstruction_ledger_imported",
        "maulik_okounkov_quiver_scope_recorded",
        "schiffmann_vasserot_scope_recorded",
        "ks_coha_scope_recorded",
        "non_toric_firewall_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "integral_form_rows_supplied",
        "product_stability_rows_supplied",
        "coproduct_stability_rows_supplied",
        "pairing_stability_rows_supplied",
        "completion_separated_rows_supplied",
        "completion_complete_rows_supplied",
        "drinfeld_double_rows_supplied",
        "cross_relation_rows_supplied",
        "cartan_identification_rows_supplied",
        "primitive_cartan_survival_rows_supplied",
        "stable_envelope_rows_supplied",
        "compact_non_toric_replacement_theorem_supplied",
        "cyqg_comparison_rows_supplied",
        "compact_drinfeld_double_constructed",
        "toric_theorem_imported_as_compact_proof",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW367_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
            str(D0_FIXTURE),
            str(O2_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    sources = {row["source_id"]: row for row in tables["source_rows.csv"]}
    require_equal(set(sources), set(EXPECTED_SOURCE_ROWS), "source row ids")
    for source_id, status in EXPECTED_SOURCE_ROWS.items():
        row = sources[source_id]
        require_equal(row.get("source_status"), status, f"{source_id} status")
        require_equal(row.get("check_status"), "verified", f"{source_id} check")

    datum = tables["datum_rows.csv"]
    require_equal(len(datum), 1, "datum row count")
    datum_row = datum[0]
    required_keys = (
        "integral_form_required",
        "product_stability_required",
        "coproduct_stability_required",
        "pairing_stability_required",
        "completion_separated_required",
        "completion_complete_required",
        "drinfeld_double_required",
        "cross_relations_required",
        "cartan_identification_required",
        "primitive_cartan_survival_required",
        "stable_envelope_transport_required",
        "compact_non_toric_replacement_required",
        "cyqg_comparison_required",
        "datum_recorded",
    )
    for key in required_keys:
        require_equal(datum_row.get(key), "true", f"datum {key}")
    require_equal(datum_row.get("current_source_supplied"), "false", "datum current source")

    scope = {row["scope_id"]: row for row in tables["scope_rows.csv"]}
    require_equal(set(scope), set(EXPECTED_SCOPE), "scope ids")
    for scope_id, (applicability, forbidden_import) in EXPECTED_SCOPE.items():
        row = scope[scope_id]
        require_equal(row.get("compact_k3e_applicability"), applicability, f"{scope_id} applicability")
        require_equal(row.get("forbidden_import"), forbidden_import, f"{scope_id} forbidden import")
        require_equal(row.get("check_status"), "verified", f"{scope_id} status")

    for empty_table in (
        "integral_form_rows.csv",
        "completion_rows.csv",
        "drinfeld_double_rows.csv",
        "stable_envelope_rows.csv",
        "cartan_rows.csv",
    ):
        require_equal(len(tables[empty_table]), 0, f"{empty_table} row count")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = coverage[coverage_id]
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(row.get("check_status"), "verified", f"{coverage_id} status")

    obligations = {row["obligation_id"]: row for row in tables["blocked_obligations.csv"]}
    require_equal(set(obligations), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, row in obligations.items():
        require_equal(row.get("compatibility_status"), "missing_open_obligation", obligation_id)
        require_equal(row.get("check_status"), "verified", f"{obligation_id} status")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, row in firewall.items():
        require_equal(row.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect")
        require_equal(row.get("check_status"), "verified", f"{substitute} status")

    for req in tables["text_requirements.csv"]:
        require_equal(req.get("fragment_present"), "true", f"{req['requirement_id']} fragment flag")
        require_equal(req.get("check_status"), "verified", f"{req['requirement_id']} status")


def check_imports() -> None:
    row367 = read_json(ROW367_FIXTURE / "manifest.json")
    require_equal(row367.get("status"), ROW367_STATUS, "row367 status")
    require_false(row367.get("hopf_radical_descent_proved_for_current_source"), "row367 current descent")

    compact = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact.get("compact_source_recognition"), "compact source recognition")
    require_false(compact.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "A_entries.csv",
        "G_entries.csv",
        "hopf_pairing_identities.csv",
        "radical_ideal_coideal.csv",
        "transitions.csv",
        "pbw.csv",
    ):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)

    d0 = read_json(D0_FIXTURE / "manifest.json")
    require_equal(d0.get("obstruction_ledger_status"), D0_STATUS, "D0 status")
    require_false(d0.get("d0_certification"), "D0 certification")
    require_false(d0.get("mathematical_certification"), "D0 mathematical certification")
    for table_name in (
        "retained_substacks.csv",
        "hn_transitions.csv",
        "vanishing_cycles.csv",
        "orientation_specializations.csv",
        "ml_exactness.csv",
    ):
        require_table_empty(D0_FIXTURE / table_name)

    o2 = read_json(O2_FIXTURE / "manifest.json")
    require_equal(o2.get("obstruction_ledger_status"), O2_STATUS, "O2 status")
    require_false(o2.get("o2_certification"), "O2 certification")
    require_false(o2.get("mathematical_certification"), "O2 mathematical certification")
    for table_name in (
        "wall_objects.csv",
        "wall_charts.csv",
        "overlaps.csv",
        "orbit_transport.csv",
        "half_hilbert_orbit.csv",
    ):
        require_table_empty(O2_FIXTURE / table_name)


def check_text_requirements(fixture: Path) -> None:
    rows = read_table_path(
        fixture / "text_requirements.csv",
        next(spec.columns for spec in TABLE_SPECS if spec.path == "text_requirements.csv"),
    )
    for row in rows:
        path = Path(row["file_path"])
        if not path.exists():
            raise ValueError(f"{row['requirement_id']}: missing text file {path}")
        text = path.read_text(encoding="utf-8")
        if row["required_fragment"] not in text:
            raise ValueError(f"{row['requirement_id']}: required fragment not found")


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
    check_text_requirements(fixture)
    return SUCCESS_STATUS


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        status = verify(args.fixture)
    except Exception as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
