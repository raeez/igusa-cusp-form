#!/usr/bin/env python3
"""Verify row-312 transition compatibility for Coxeter cochains."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_cocycle_cochain_transition_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_cocycle_cochain_transition_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_COCHAIN_TRANSITION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-cocycle-cochain-transition-compatibility"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_cocycle_cochain_transition")

COCHAIN_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_cocycle_cochain_trivialization")
TRANSITION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")

COCHAIN_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_COCHAIN_TRIVIALIZATION_OBSTRUCTION_VERIFIED"
TRANSITION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "row311_witness_rows": 0,
    "row311_defect_rows": 0,
    "transition_orientation_multiplicative_rows": 0,
    "transition_orientation_defect_rows": 0,
    "orientation_transition_rows": 0,
    "orientation_coxeter_rows": 0,
    "transition_cochain_map_rows": 0,
    "cochain_transition_defect_rows": 0,
    "cochain_transition_claim": 0,
    "torsor_defect_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "row311_cochain_vectors",
    "row311_coboundary_defects",
    "transition_orientation_input",
    "cochain_map_rows",
    "chain_map_defect",
    "cocycle_pullback_defect",
    "b_transition_defect",
    "gauge_compatibility",
    "two_step_coherence",
    "transition_orientation_ledger_row",
    "torsor_defects_later",
    "no_transition_geometry_only_substitution",
    "no_row311_only_substitution",
    "no_maass_character_substitution",
}

REQUIRED_FIREWALL = {
    "row311_local_choice",
    "transition_geometry_only",
    "orientation_transition_ledger_only",
    "maass_character_value",
    "target_coxeter_graph",
    "torsor_defects",
    "scalar_trace",
}

REQUIRED_TRANSITION_OBLIGATIONS = {
    "transition_geometry_input",
    "weyl_lift_transition_compatibility",
    "coxeter_cochain_transition",
    "strict_picard_groupoid_transition",
    "orientation_mittag_leffler",
}

REQUIRED_ORIENTATION_OBLIGATIONS = {
    "coxeter_cochain_trivialization",
    "coxeter_coherence",
    "transition_strict",
    "transition_ml",
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
            "b_R_rows_required",
            "b_Rprime_rows_required",
            "transition_cochain_maps_required",
            "chain_map_required",
            "cocycle_pullback_required",
            "b_transition_defect_required",
            "gauge_compatibility_required",
            "two_step_coherence_required",
            "torsor_defects_out_of_scope",
            "criterion_recorded",
            "cochain_transition_compatibility_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transition_cochain_map_rows.csv",
        (
            "transition_map_id",
            "from_stage",
            "to_stage",
            "transition_id",
            "rho1_matrix_id",
            "rho2_matrix_id",
            "source_C1_basis_id",
            "target_C1_basis_id",
            "source_C2_basis_id",
            "target_C2_basis_id",
            "chain_map_defect_rank",
            "cocycle_pullback_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "cochain_transition_defect_rows.csv",
        (
            "defect_id",
            "transition_map_id",
            "source_witness_id",
            "target_witness_id",
            "rho1_matrix_id",
            "b_transition_defect_rank",
            "gauge_compatibility_id",
            "two_step_chain_id",
            "two_step_coherence_defect_rank",
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
            "transition_status",
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


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def count_data_rows(path: Path) -> int:
    return len(read_table_path(path, None, allow_empty=True))


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "cochain_trivialization_imported",
        "transition_orientation_imported",
        "orientation_obstruction_imported",
        "transition_compatibility_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "cochain_vector_rows_supplied",
        "transition_cochain_map_rows_supplied",
        "cocycle_pullback_rows_supplied",
        "cochain_transition_defect_rows_supplied",
        "gauge_compatibility_rows_supplied",
        "two_step_coherence_rows_supplied",
        "cochain_transition_compatibility_proved",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(COCHAIN_FIXTURE), str(TRANSITION_FIXTURE), str(ORIENTATION_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    cochain_manifest = read_json(COCHAIN_FIXTURE / "manifest.json")
    require_equal(cochain_manifest.get("status"), COCHAIN_STATUS, "row-311 status")
    require_equal(cochain_manifest.get("cochain_trivialization_constructed"), False, "row-311 constructed")
    require_equal(cochain_manifest.get("transition_compatibility_rows_supplied"), False, "row-311 transition")

    transition_manifest = read_json(TRANSITION_FIXTURE / "manifest.json")
    require_equal(transition_manifest.get("status"), TRANSITION_STATUS, "transition status")
    require_equal(
        transition_manifest.get("orientation_transition_certification"),
        False,
        "orientation transition certification",
    )

    transition_blocked = rows_by(
        read_table_path(TRANSITION_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "transition blocked obligations",
    )
    if not REQUIRED_TRANSITION_OBLIGATIONS.issubset(transition_blocked):
        missing = sorted(REQUIRED_TRANSITION_OBLIGATIONS - set(transition_blocked))
        raise ValueError(f"transition ledger missing obligations: {missing}")

    orientation_manifest = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation_manifest.get("obstruction_ledger_status"),
        ORIENTATION_STATUS,
        "orientation obstruction status",
    )
    require_equal(orientation_manifest.get("empty_blocked"), True, "orientation empty")

    orientation_blocked = rows_by(
        read_table_path(ORIENTATION_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "orientation blocked obligations",
    )
    if not REQUIRED_ORIENTATION_OBLIGATIONS.issubset(orientation_blocked):
        missing = sorted(REQUIRED_ORIENTATION_OBLIGATIONS - set(orientation_blocked))
        raise ValueError(f"orientation ledger missing transition obligations: {missing}")

    return {
        "row311_witness_rows": count_data_rows(COCHAIN_FIXTURE / "cochain_witness_rows.csv"),
        "row311_defect_rows": count_data_rows(COCHAIN_FIXTURE / "cochain_defect_rows.csv"),
        "transition_orientation_multiplicative_rows": count_data_rows(
            TRANSITION_FIXTURE / "multiplicative_weyl_transport.csv"
        ),
        "transition_orientation_defect_rows": count_data_rows(
            TRANSITION_FIXTURE / "transition_defects.csv"
        ),
        "orientation_transition_rows": count_data_rows(ORIENTATION_FIXTURE / "transitions.csv"),
        "orientation_coxeter_rows": count_data_rows(ORIENTATION_FIXTURE / "coxeter_cocycles.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "cochain_trivialization": COCHAIN_STATUS,
        "transition_orientation": TRANSITION_STATUS,
        "orientation_obstruction": ORIENTATION_STATUS,
        "optimization_row": "row_312",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"cochain_transition_compatibility"}, "criterion ids")
    row = rows["cochain_transition_compatibility"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "b_R_rows_required",
        "b_Rprime_rows_required",
        "transition_cochain_maps_required",
        "chain_map_required",
        "cocycle_pullback_required",
        "b_transition_defect_required",
        "gauge_compatibility_required",
        "two_step_coherence_required",
        "torsor_defects_out_of_scope",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(
        bool_cell(row, "cochain_transition_compatibility_proved"),
        False,
        "cochain transition compatibility proved",
    )


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    for table_name in ("transition_cochain_map_rows.csv", "cochain_transition_defect_rows.csv"):
        if tables[table_name]:
            raise ValueError(f"{table_name} must remain empty in obstruction packet")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed.update(counts)
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(int_cell(row, "computed_value"), computed[coverage_id], f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(row["transition_status"], "missing_open_obligation", f"{row['obligation_id']} status")
        require_equal(row["check_status"], "verified", f"{row['obligation_id']} check")
        if not row["mathematical_payload"] or not row["why_required"]:
            raise ValueError(f"{row['obligation_id']}: missing payload or reason")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        check_verified(row, "scalar_firewall.csv")
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def verify_fixture(fixture: Path) -> None:
    if not fixture.is_dir():
        raise ValueError(f"fixture is not a directory: {fixture}")
    verify_manifest(fixture)
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_empty_tables(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(
            f"RHOMRED_WEYL_ORIENTATION_COCYCLE_COCHAIN_TRANSITION_BLOCKED: {exc}",
            file=sys.stderr,
        )
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
