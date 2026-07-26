#!/usr/bin/env python3
"""Verify the row-341 finite geometric Hall object definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_geometric_hall_object_definition.v1"
EXPECTED_KIND = "finite_geometric_hall_object_definition"
SUCCESS_STATUS = "FINITE_GEOMETRIC_HALL_OBJECT_DEFINITION_VERIFIED"
PROOF_LABEL = "def:finite-geometric-hall-object"
DEFAULT_FIXTURE = Path("certificates/hall/finite_geometric_hall_object")

FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
VANISHING_CYCLE_FIXTURE = Path(
    "certificates/vanishing_cycles/transition_vanishing_cycle_preservation"
)
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")

FINITE_MODULI_STATUS = "MODULI_OBSTRUCTION_LEDGER_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
VANISHING_CYCLE_STATUS = "TRANSITION_VANISHING_CYCLE_PRESERVATION_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "definition_count": 1,
    "object_component_rows": 0,
    "source_degree_rows": 0,
    "basis_provenance_rows": 0,
    "orientation_line_rows": 0,
    "vanishing_cycle_transport_rows": 0,
    "hall_product_rows": 0,
    "hall_coproduct_rows": 0,
    "unit_counit_rows": 0,
}

REQUIRED_OBLIGATIONS = {
    "reduced_vanishing_cycle_coefficients",
    "orientation_lines",
    "compact_support_bm_model",
    "object_component_rows",
    "finite_rank_rows",
    "source_degree_rows",
    "homogeneous_basis_provenance",
    "transition_compatibility",
    "compact_hall_source_population",
}

REQUIRED_FIREWALL = {
    "finite_moduli_only",
    "orientation_ledger_only",
    "vanishing_cycle_transition_only",
    "compact_Hall_empty_ledger",
    "product_matrix",
    "coproduct_matrix",
    "scalar_trace",
    "euler_characteristic",
    "signed_multiplicity",
    "pfaffian_product",
    "target_root_window",
    "denominator_product",
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
        "definition_rows.csv",
        (
            "definition_id",
            "finite_charge_set_required",
            "retained_substacks_required",
            "finite_residual_inertia_required",
            "reduced_vanishing_cycles_required",
            "orientation_lines_required",
            "compact_support_bm_required",
            "homogeneous_basis_required",
            "object_definition_recorded",
            "object_populated",
            "product_claimed",
            "coproduct_claimed",
            "pairing_claimed",
            "primitive_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "object_components.csv",
        (
            "component_id",
            "degree_id",
            "parity",
            "stack_id",
            "coefficient_system_id",
            "bm_group_id",
            "finite_rank",
            "basis_provenance_id",
            "component_verified",
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
        raise ValueError(f"{path}: expected no source rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")

    for key in (
        "definition_recorded",
        "finite_moduli_packet_imported",
        "reduced_orientation_ledger_imported",
        "transition_vanishing_cycle_ledger_imported",
        "compact_hall_source_ledger_imported",
        "finite_charge_set_available",
        "retained_substacks_available",
        "finite_residual_inertia_available",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "orientation_lines_supplied",
        "vanishing_cycle_coefficients_supplied",
        "compact_support_bm_model_supplied",
        "object_component_rows_supplied",
        "source_degree_rows_supplied",
        "basis_provenance_rows_supplied",
        "finite_rank_rows_supplied",
        "finite_hall_object_populated",
        "product_claimed",
        "coproduct_claimed",
        "pairing_claimed",
        "primitive_claimed",
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
            str(FINITE_MODULI_FIXTURE),
            str(ORIENTATION_FIXTURE),
            str(VANISHING_CYCLE_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    definition = tables["definition_rows.csv"]
    require_equal(len(definition), 1, "definition row count")
    row = definition[0]
    for key in (
        "finite_charge_set_required",
        "retained_substacks_required",
        "finite_residual_inertia_required",
        "reduced_vanishing_cycles_required",
        "orientation_lines_required",
        "compact_support_bm_required",
        "homogeneous_basis_required",
        "object_definition_recorded",
    ):
        require_equal(row.get(key), "true", f"definition {key}")
    for key in (
        "object_populated",
        "product_claimed",
        "coproduct_claimed",
        "pairing_claimed",
        "primitive_claimed",
    ):
        require_equal(row.get(key), "false", f"definition {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("definition proof reference does not point to row-341 definition")

    require_equal(len(tables["object_components.csv"]), 0, "object components count")

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


def check_imports() -> None:
    moduli = read_json(FINITE_MODULI_FIXTURE / "manifest.json")
    require_equal(moduli.get("obstruction_ledger_status"), FINITE_MODULI_STATUS, "moduli status")
    require_true(moduli.get("finite_class_set"), "finite class set")
    require_true(moduli.get("retained_closed_substacks"), "retained substacks")
    require_true(
        moduli.get("finite_residual_inertia_after_rigidification"),
        "finite residual inertia",
    )
    if moduli.get("compact_hall_stage") is True:
        raise ValueError("moduli compact hall stage: unexpected positive compact Hall claim")
    require_false(moduli.get("moduli_certification"), "moduli certification")
    require_false(moduli.get("mathematical_certification"), "moduli mathematical certification")

    orientation = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation.get("obstruction_ledger_status"),
        ORIENTATION_STATUS,
        "orientation status",
    )
    require_false(orientation.get("orientation_certification"), "orientation certification")
    require_false(
        orientation.get("mathematical_certification"),
        "orientation mathematical certification",
    )
    require_table_empty(ORIENTATION_FIXTURE / "orientation_lines.csv")

    vcycles = read_json(VANISHING_CYCLE_FIXTURE / "manifest.json")
    require_equal(vcycles.get("status"), VANISHING_CYCLE_STATUS, "vanishing-cycle status")
    require_false(
        vcycles.get("vanishing_cycle_transition_certification"),
        "vanishing-cycle transition certification",
    )
    require_false(
        vcycles.get("mathematical_certification"),
        "vanishing-cycle mathematical certification",
    )
    for rel_path in (
        "dcritical_chart_transitions.csv",
        "vanishing_cycle_transport.csv",
        "transition_defects.csv",
    ):
        require_table_empty(VANISHING_CYCLE_FIXTURE / rel_path)

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(
        compact.get("obstruction_ledger_status"),
        COMPACT_HALL_STATUS,
        "compact hall status",
    )
    require_equal(compact.get("source_kind"), "mock_empty_blocked", "compact source kind")
    require_true(compact.get("empty_blocked"), "compact source empty blocked")
    require_false(compact.get("compact_source_recognition"), "compact source recognition")
    require_false(compact.get("mathematical_certification"), "compact mathematical certification")
    for rel_path in (
        "degrees.csv",
        "basis_provenance.csv",
        "M_entries.csv",
        "D_entries.csv",
        "unit_counit.csv",
    ):
        require_table_empty(COMPACT_HALL_FIXTURE / rel_path)


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
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
