#!/usr/bin/env python3
"""Verify the row-369 finite Hall conilpotent source-coalgebra packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_conilpotent_source_coalgebra.v1"
EXPECTED_KIND = "finite_hall_conilpotent_source_coalgebra_obstruction"
SUCCESS_STATUS = "FINITE_HALL_CONILPOTENT_SOURCE_COALGEBRA_OBSTRUCTION_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_conilpotent_source_coalgebra")

ROW368_FIXTURE = Path("certificates/hall/finite_hall_integral_form_stable_envelope_transport")
HYBRID_FIXTURE = Path("certificates/hybrid/k3e_hybrid_carrier")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")
D0_FIXTURE = Path("certificates/d0/k3e_d0_hn")
TRANS_PRODUCT_FIXTURE = Path("certificates/hall/transition_hall_product_preservation")
TRANS_COPRODUCT_FIXTURE = Path("certificates/hall/transition_hall_coproduct_preservation")
PRIMITIVE_LIM1_FIXTURE = Path("certificates/hall/primitive_space_lim1_vanishing")
PAIRING_LIM1_FIXTURE = Path("certificates/hall/pairing_kernel_lim1_vanishing")

ROW368_STATUS = "FINITE_HALL_INTEGRAL_FORM_STABLE_ENVELOPE_TRANSPORT_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
D0_STATUS = "D0_OBSTRUCTION_LEDGER_VERIFIED"
TRANS_PRODUCT_STATUS = "TRANSITION_HALL_PRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"
TRANS_COPRODUCT_STATUS = "TRANSITION_HALL_COPRODUCT_PRESERVATION_OBSTRUCTION_VERIFIED"
PRIMITIVE_LIM1_STATUS = "PRIMITIVE_SPACE_LIM1_VANISHING_OBSTRUCTION_VERIFIED"
PAIRING_LIM1_STATUS = "PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED"

EXPECTED_SOURCE_ROWS = {
    "row368_transport_firewall": ROW368_STATUS,
    "hybrid_carrier": "HYBRID_CARRIER_EMPTY_BLOCKED",
    "compact_hall_source": COMPACT_SOURCE_STATUS,
    "d0_hn": D0_STATUS,
    "transition_hall_product": TRANS_PRODUCT_STATUS,
    "transition_hall_coproduct": TRANS_COPRODUCT_STATUS,
    "primitive_lim1": PRIMITIVE_LIM1_STATUS,
    "pairing_kernel_lim1": PAIRING_LIM1_STATUS,
}

EXPECTED_COVERAGE = {
    "datum_count": 1,
    "coalgebra_rows": 0,
    "filtration_rows": 0,
    "conilpotence_rows": 0,
    "coproduct_transition_rows": 0,
    "inverse_limit_rows": 0,
    "hybrid_higher_coloured_rows": 0,
    "hybrid_transition_rows": 0,
    "compact_source_D_entries": 0,
    "compact_source_unit_counit_rows": 0,
    "compact_source_bialgebra_rows": 0,
    "d0_retained_rows": 0,
    "transition_coproduct_defect_rows": 0,
    "primitive_lim1_rows": 0,
    "pairing_kernel_lim1_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_chiral_object",
    "source_counit",
    "finite_charge_filtration",
    "bar_length_bound",
    "normal_ordered_gram_grading",
    "collision_coproduct_rows",
    "coalgebra_coassociativity",
    "coalgebra_counit_identities",
    "quotient_after_correspondence",
    "conilpotence_nilpotence",
    "transition_coalgebra_maps",
    "transition_coproduct_intertwining",
    "strict_mittag_leffler",
    "inverse_limit_construction",
    "bar_koszul_comparison",
    "source_target_separation",
}

REQUIRED_FIREWALL = {
    "notation_C_XR",
    "formal_bar_coalgebra_language",
    "target_bkm_denominator",
    "stable_envelope_transport",
    "drinfeld_double",
    "primitive_space_lim1",
    "pairing_kernel_lim1",
    "ordinary_ran_only",
    "compact_source_empty",
    "finite_type_boundedness",
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
            "coalgebra_required",
            "coaugmentation_required",
            "counit_required",
            "filtration_required",
            "collision_coproduct_required",
            "coalgebra_identities_required",
            "conilpotence_required",
            "quotient_identities_required",
            "transition_required",
            "inverse_limit_required",
            "bar_koszul_comparison_required",
            "datum_recorded",
            "current_source_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coalgebra_rows.csv",
        (
            "row_id",
            "R_id",
            "coalgebra_id",
            "coaugmentation_id",
            "counit_id",
            "collision_coproduct_id",
            "coalgebra_identity_id",
            "quotient_identity_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "filtration_rows.csv",
        (
            "row_id",
            "R_id",
            "coalgebra_id",
            "filtration_id",
            "degree_id",
            "bar_length_bound",
            "N_R",
            "finite_graded_piece_status",
            "normal_ordered_gram_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "conilpotence_rows.csv",
        (
            "row_id",
            "R_id",
            "coalgebra_id",
            "reduced_coproduct_id",
            "N_R",
            "iterated_power",
            "computed_defect_rank",
            "expected_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "coproduct_transition_rows.csv",
        (
            "row_id",
            "from_stage",
            "to_stage",
            "coalgebra_id",
            "transition_map_id",
            "coproduct_intertwining_id",
            "counit_intertwining_id",
            "filtration_intertwining_id",
            "computed_defect_rank",
            "expected_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "inverse_limit_rows.csv",
        (
            "row_id",
            "tower_id",
            "object_type",
            "transition_maps_id",
            "strict_ml_status",
            "r1lim_rank",
            "limit_object_id",
            "bar_cobar_completion_status",
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
    require_equal(manifest.get("row_number"), 369, "row_number")

    for key in (
        "conilpotent_source_datum_recorded",
        "row368_transport_firewall_imported",
        "hybrid_carrier_ledger_imported",
        "compact_hall_source_ledger_imported",
        "d0_obstruction_ledger_imported",
        "transition_product_ledger_imported",
        "transition_coproduct_ledger_imported",
        "primitive_lim1_ledger_imported",
        "pairing_kernel_lim1_ledger_imported",
        "source_target_firewall_recorded",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "coalgebra_rows_supplied",
        "coaugmentation_rows_supplied",
        "counit_rows_supplied",
        "filtration_rows_supplied",
        "collision_coproduct_rows_supplied",
        "coalgebra_identity_rows_supplied",
        "conilpotence_rows_supplied",
        "quotient_coalgebra_identity_rows_supplied",
        "transition_coalgebra_rows_supplied",
        "inverse_limit_ml_rows_supplied",
        "bar_koszul_comparison_rows_supplied",
        "current_source_coalgebra_constructed",
        "inverse_limit_coalgebra_constructed",
        "stable_envelope_substitutes_for_source_coalgebra",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW368_FIXTURE),
            str(HYBRID_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
            str(D0_FIXTURE),
            str(TRANS_PRODUCT_FIXTURE),
            str(TRANS_COPRODUCT_FIXTURE),
            str(PRIMITIVE_LIM1_FIXTURE),
            str(PAIRING_LIM1_FIXTURE),
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
    for key in (
        "coalgebra_required",
        "coaugmentation_required",
        "counit_required",
        "filtration_required",
        "collision_coproduct_required",
        "coalgebra_identities_required",
        "conilpotence_required",
        "quotient_identities_required",
        "transition_required",
        "inverse_limit_required",
        "bar_koszul_comparison_required",
        "datum_recorded",
    ):
        require_equal(datum_row.get(key), "true", f"datum {key}")
    require_equal(datum_row.get("current_source_supplied"), "false", "datum current source")

    for empty_table in (
        "coalgebra_rows.csv",
        "filtration_rows.csv",
        "conilpotence_rows.csv",
        "coproduct_transition_rows.csv",
        "inverse_limit_rows.csv",
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
    row368 = read_json(ROW368_FIXTURE / "manifest.json")
    require_equal(row368.get("status"), ROW368_STATUS, "row368 status")
    require_false(row368.get("stable_envelope_rows_supplied"), "row368 stable-envelope rows")
    require_false(row368.get("compact_drinfeld_double_constructed"), "row368 compact double")

    hybrid = read_json(HYBRID_FIXTURE / "manifest.json")
    require_equal(hybrid.get("hybrid_kind"), "mock_empty_blocked", "hybrid kind")
    require_false(hybrid.get("certified"), "hybrid certified")
    require_true(hybrid.get("empty_blocked"), "hybrid empty blocked")
    for table_name in (
        "hybrid_base.csv",
        "correspondences.csv",
        "flag_atlas.csv",
        "higher_coloured.csv",
        "quotient_pseudofunctor.csv",
        "transitions.csv",
    ):
        require_table_empty(HYBRID_FIXTURE / table_name)

    compact = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_false(compact.get("compact_source_recognition"), "compact source recognition")
    require_false(compact.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "D_entries.csv",
        "M_entries.csv",
        "unit_counit.csv",
        "hall_bialgebra_identities.csv",
        "transitions.csv",
    ):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)

    d0 = read_json(D0_FIXTURE / "manifest.json")
    require_equal(d0.get("obstruction_ledger_status"), D0_STATUS, "D0 status")
    require_false(d0.get("d0_certification"), "D0 certification")
    require_table_empty(D0_FIXTURE / "retained_substacks.csv")
    require_table_empty(D0_FIXTURE / "hn_transitions.csv")

    product = read_json(TRANS_PRODUCT_FIXTURE / "manifest.json")
    require_equal(product.get("status"), TRANS_PRODUCT_STATUS, "transition product status")
    require_false(product.get("hall_product_transition_certification"), "transition product certification")
    for table_name in (
        "extension_correspondence_transitions.csv",
        "coefficient_transport.csv",
        "product_matrix_transport.csv",
        "base_change_projection.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANS_PRODUCT_FIXTURE / table_name)

    coproduct = read_json(TRANS_COPRODUCT_FIXTURE / "manifest.json")
    require_equal(coproduct.get("status"), TRANS_COPRODUCT_STATUS, "transition coproduct status")
    require_false(coproduct.get("hall_coproduct_transition_certification"), "transition coproduct certification")
    for table_name in (
        "splitting_correspondence_transitions.csv",
        "coefficient_transport.csv",
        "coproduct_matrix_transport.csv",
        "base_change_projection.csv",
        "transition_defects.csv",
    ):
        require_table_empty(TRANS_COPRODUCT_FIXTURE / table_name)

    primitive = read_json(PRIMITIVE_LIM1_FIXTURE / "manifest.json")
    require_equal(primitive.get("status"), PRIMITIVE_LIM1_STATUS, "primitive lim1 status")
    require_false(primitive.get("lim1_vanishing_certification"), "primitive lim1 certification")
    require_table_empty(PRIMITIVE_LIM1_FIXTURE / "primitive_ml_r1lim_defects.csv")

    pairing = read_json(PAIRING_LIM1_FIXTURE / "manifest.json")
    require_equal(pairing.get("status"), PAIRING_LIM1_STATUS, "pairing lim1 status")
    require_false(pairing.get("lim1_vanishing_certification"), "pairing lim1 certification")
    require_table_empty(PAIRING_LIM1_FIXTURE / "pairing_kernel_ml_r1lim_defects.csv")


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
