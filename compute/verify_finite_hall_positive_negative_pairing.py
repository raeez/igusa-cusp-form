#!/usr/bin/env python3
"""Verify the row-358 finite Hall positive-negative pairing packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_positive_negative_pairing.v1"
EXPECTED_KIND = "finite_hall_positive_negative_pairing_obstruction"
SUCCESS_STATUS = "FINITE_HALL_POSITIVE_NEGATIVE_PAIRING_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "def:finite-hall-positive-negative-pairing"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_positive_negative_pairing")

GRAM_DEGREE_FIXTURE = Path("certificates/hall/finite_hall_normal_ordered_gram_degree")
BRACKET_PARITY_FIXTURE = Path("certificates/hall/finite_hall_bracket_parity")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

GRAM_DEGREE_STATUS = "FINITE_HALL_NORMAL_ORDERED_GRAM_DEGREE_OBSTRUCTION_VERIFIED"
BRACKET_PARITY_STATUS = "FINITE_HALL_BRACKET_PARITY_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "formal_pairing_rows": 3,
    "formal_pairing_degree_defect_total": 0,
    "local_pairing_rows": 0,
    "compact_source_G_entries": 0,
    "compact_source_hopf_pairing_identity_rows": 0,
    "source_trace_functional_rows": 0,
    "source_pairing_correspondence_rows": 0,
    "source_orientation_transport_rows": 0,
}

EXPECTED_FORMAL_IMPORTS = {
    "formal_pairing_rows": ("pairing_rows.csv", 3, 3, 0),
    "formal_pairing_relations": ("formal_relations.csv", 6, 6, 0),
}

REQUIRED_OBLIGATIONS = {
    "source_G_entries",
    "degree_zero_trace",
    "positive_negative_correspondence",
    "orientation_transport",
    "positive_negative_primitive_bases",
    "hopf_pairing_identity_rows",
    "formal_pairing_firewall",
    "source_vs_target_firewall",
}

REQUIRED_FIREWALL = {
    "formal_pairing_rows",
    "target_pairing_blocks",
    "scalar_trace",
    "denominator_product",
    "signed_dimension",
    "row359_homogeneity",
    "row360_supersymmetry",
    "row361_invariance",
    "row362_coproduct",
    "empty_G_entries",
    "empty_hopf_pairing_identities",
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
        "criterion_rows.csv",
        (
            "criterion_id",
            "primitive_stage_required",
            "normal_ordered_grading_required",
            "degree_zero_trace_required",
            "positive_negative_correspondence_required",
            "orientation_transport_required",
            "homogeneous_bases_required",
            "G_matrix_definition_recorded",
            "formal_pairing_rows_imported",
            "current_source_pairing_defined",
            "homogeneity_claimed",
            "supersymmetry_claimed",
            "invariance_claimed",
            "coproduct_compatibility_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pairing_rows.csv",
        (
            "pairing_row_id",
            "R_id",
            "degree_id",
            "parity",
            "positive_basis_id",
            "negative_basis_id",
            "value",
            "coefficient_ring",
            "trace_row_id",
            "pairing_correspondence_id",
            "orientation_transport_id",
            "geometric_source_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "formal_import_rows.csv",
        (
            "import_id",
            "source_fixture",
            "imported_table",
            "imported_row_count",
            "zero_defect_rows",
            "positive_defect_rows",
            "source_reference",
            "check_status",
            "notes",
        ),
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
        rows = []
        for row in reader:
            normalized = {
                key: (value or "").strip()
                for key, value in row.items()
                if key is not None
            }
            if any(normalized.values()):
                rows.append(normalized)
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
    require_equal(manifest.get("row_number"), 358, "row_number")

    for key in (
        "definition_recorded",
        "normal_ordered_gram_degree_packet_imported",
        "bracket_parity_packet_imported",
        "formal_pairing_pushforward_imported",
        "compact_hall_source_ledger_imported",
        "positive_negative_formula_recorded",
        "formal_degree_zero_pairing_rows_verified",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_G_entries_supplied",
        "source_trace_functional_supplied",
        "source_pairing_correspondences_supplied",
        "source_orientation_transport_rows_supplied",
        "source_hopf_pairing_identity_rows_supplied",
        "homogeneity_proved",
        "supersymmetry_proved",
        "invariance_proved",
        "coproduct_compatibility_proved",
        "quotient_nondegeneracy_proved",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(
        set(manifest.get("tables", [])),
        {spec.path for spec in TABLE_SPECS},
        "manifest tables",
    )
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(GRAM_DEGREE_FIXTURE),
            str(BRACKET_PARITY_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "primitive_stage_required",
        "normal_ordered_grading_required",
        "degree_zero_trace_required",
        "positive_negative_correspondence_required",
        "orientation_transport_required",
        "homogeneous_bases_required",
        "G_matrix_definition_recorded",
        "formal_pairing_rows_imported",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_pairing_defined",
        "homogeneity_claimed",
        "supersymmetry_claimed",
        "invariance_claimed",
        "coproduct_compatibility_claimed",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-358 definition")

    require_equal(len(tables["pairing_rows.csv"]), 0, "local pairing row count")

    formal_imports = {row["import_id"]: row for row in tables["formal_import_rows.csv"]}
    require_equal(set(formal_imports), set(EXPECTED_FORMAL_IMPORTS), "formal import ids")
    for import_id, (table_name, row_count, zero_count, positive_count) in EXPECTED_FORMAL_IMPORTS.items():
        irow = formal_imports[import_id]
        require_equal(irow.get("imported_table"), table_name, f"{import_id} table")
        require_equal(int_cell(irow, "imported_row_count"), row_count, f"{import_id} count")
        require_equal(int_cell(irow, "zero_defect_rows"), zero_count, f"{import_id} zero")
        require_equal(int_cell(irow, "positive_defect_rows"), positive_count, f"{import_id} positive")
        require_equal(irow.get("check_status"), "verified", f"{import_id} status")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        crow = coverage[coverage_id]
        require_equal(int_cell(crow, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(crow, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(crow, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(crow.get("check_status"), "verified", f"{coverage_id} status")

    obligations = {row["obligation_id"]: row for row in tables["blocked_obligations.csv"]}
    require_equal(set(obligations), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, orow in obligations.items():
        require_equal(orow.get("compatibility_status"), "missing_open_obligation", obligation_id)
        require_equal(orow.get("check_status"), "verified", f"{obligation_id} status")
        if PROOF_LABEL not in orow.get("proof_reference", ""):
            raise ValueError(f"{obligation_id}: proof reference does not point to definition")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, frow in firewall.items():
        require_equal(frow.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(frow, "defect_rank"), 0, f"{substitute} defect")
        require_equal(frow.get("check_status"), "verified", f"{substitute} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{substitute}: proof reference does not point to definition")

    for req in tables["text_requirements.csv"]:
        require_equal(req.get("fragment_present"), "true", f"{req['requirement_id']} fragment flag")
        require_equal(req.get("check_status"), "verified", f"{req['requirement_id']} status")


def check_pairing_pushforward_import() -> None:
    manifest = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(
        manifest.get("schema_version"),
        "hall_pairing_pushforward_compatibility.v1",
        "pairing pushforward schema",
    )
    require_true(manifest.get("certified"), "pairing pushforward certified")
    require_true(manifest.get("normal_ordered_pairing_degree"), "normal ordered pairing degree")
    for key in (
        "compact_hall_correspondence",
        "primitive_closure",
        "hopf_adjointness",
        "frobenius_cyclic_identity",
        "quotient_nondegeneracy",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_false(manifest.get(key), f"pairing pushforward {key}")

    pairing_rows = read_table_path(PAIRING_PUSHFORWARD_FIXTURE / "pairing_rows.csv")
    require_equal(len(pairing_rows), 3, "formal pairing row count")
    for row in pairing_rows:
        for axis in ("n", "l", "m"):
            require_equal(int_cell(row, f"total_degree_{axis}"), 0, f"{row['pairing_id']} total {axis}")
        require_equal(row.get("homogeneous_degree_zero"), "true", f"{row['pairing_id']} homogeneous")
        require_equal(int_cell(row, "degree_defect_rank"), 0, f"{row['pairing_id']} defect")
        require_equal(row.get("check_status"), "verified", f"{row['pairing_id']} status")

    formal_relations = read_table_path(PAIRING_PUSHFORWARD_FIXTURE / "formal_relations.csv")
    require_equal(len(formal_relations), 6, "formal relation row count")
    relation_ids = {row["relation_id"] for row in formal_relations}
    if {"pairing_degree_compatible", "pushforward_pairing_graded", "hopf_adjointness_not_proved"} - relation_ids:
        raise ValueError("formal relations omit pairing-degree firewall rows")
    for row in formal_relations:
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['relation_id']} defect")
        require_equal(row.get("check_status"), "verified", f"{row['relation_id']} status")


def check_imports() -> None:
    gram_degree = read_json(GRAM_DEGREE_FIXTURE / "manifest.json")
    require_equal(gram_degree.get("status"), GRAM_DEGREE_STATUS, "row356 Gram-degree packet status")
    require_false(gram_degree.get("normal_ordered_gram_degree_proved_for_current_source"), "row356 current source")

    bracket_parity = read_json(BRACKET_PARITY_FIXTURE / "manifest.json")
    require_equal(bracket_parity.get("status"), BRACKET_PARITY_STATUS, "row357 bracket-parity packet status")
    require_false(bracket_parity.get("bracket_parity_proved_for_current_source"), "row357 current source")

    check_pairing_pushforward_import()

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(
        compact_source.get("obstruction_ledger_status"),
        COMPACT_SOURCE_STATUS,
        "compact source status",
    )
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(compact_source.get("mathematical_certification"), "compact source certification")
    for table_name in (
        "G_entries.csv",
        "hopf_pairing_identities.csv",
        "K_entries.csv",
        "Q_entries.csv",
    ):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)


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
