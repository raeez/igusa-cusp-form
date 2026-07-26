#!/usr/bin/env python3
"""Verify the row-305 orientation/primitive-projection descent packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_primitive_projection_descent_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_primitive_projection_descent_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_PRIMITIVE_PROJECTION_DESCENT_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-descent-primitive-projection"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_primitive_projection_descent")

E_QUOTIENT_FIXTURE = Path("certificates/orientation/rhomred_orientation_e_quotient_descent")
COPRODUCT_DESCENT_FIXTURE = Path("certificates/orientation/rhomred_orientation_hall_coproduct_descent")
THETA_PRIMITIVES_FIXTURE = Path("certificates/hybrid/quotient_after_correspondence_theta_mu_primitives")
TRANSITION_PRIMITIVE_FIXTURE = Path("certificates/hall/transition_primitive_subspace_preservation")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

E_QUOTIENT_STATUS = "RHOMRED_ORIENTATION_E_QUOTIENT_DESCENT_OBSTRUCTION_VERIFIED"
COPRODUCT_DESCENT_STATUS = "RHOMRED_ORIENTATION_HALL_COPRODUCT_DESCENT_OBSTRUCTION_VERIFIED"
THETA_PRIMITIVES_STATUS = "QUOTIENT_AFTER_CORRESPONDENCE_THETA_MU_PRIMITIVES_VERIFIED"
TRANSITION_PRIMITIVE_STATUS = "TRANSITION_PRIMITIVE_SUBSPACE_PRESERVATION_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "theta_primitive_rows_available": 1,
    "theta_projection_rows_available": 1,
    "theta_kernel_intertwining_rows_available": 1,
    "source_hall_coproduct_matrix_rows_supplied": 0,
    "source_counit_rows_supplied": 0,
    "source_primitive_kernel_rows_supplied": 0,
    "source_primitive_projection_rows_supplied": 0,
    "primitive_projection_descent_claim": 0,
    "transition_primitive_rows_supplied": 0,
}

REQUIRED_OBLIGATIONS = {
    "quotient_orientation_rows",
    "hall_coproduct_orientation_descent",
    "unit_counit_orientation_descent",
    "source_hall_coproduct_row",
    "source_counit_row",
    "source_reduced_coproduct_matrix",
    "source_primitive_kernel",
    "primitive_projection_matrix",
    "kernel_intertwining_identity",
    "projection_commutator_identity",
    "transition_primitive_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}

REQUIRED_FIREWALL = {
    "theta_primitive_only",
    "hall_coproduct_descent_criterion_only",
    "transition_primitive_ledger_only",
    "empty_coproduct_matrix",
    "empty_counit",
    "primitive_rank_only",
    "scalar_trace",
    "denominator_product",
    "target_bkm_root_space",
    "bar_coalgebra_primitives",
    "protected_integration",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


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
            "quotient_orientation_required",
            "hall_coproduct_descent_required",
            "unit_counit_descent_required",
            "source_coproduct_row_required",
            "counit_row_required",
            "primitive_kernel_required",
            "primitive_projection_required",
            "theta_primitive_required",
            "kernel_intertwining_required",
            "projection_commutator_required",
            "transition_compatibility_required",
            "criterion_recorded",
            "primitive_projection_descent_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "imported_status_rows.csv",
        (
            "import_id",
            "import_path",
            "import_status",
            "positive_input",
            "missing_input",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "primitive_projection_descent_obstruction_rows.csv",
        (
            "obstruction_id",
            "quotient_orientation_status",
            "hall_coproduct_descent_status",
            "unit_counit_orientation_descent_status",
            "theta_primitive_status",
            "source_coproduct_matrix_status",
            "counit_status",
            "source_primitive_kernel_status",
            "primitive_projection_matrix_status",
            "kernel_intertwining_status",
            "projection_commutator_status",
            "transition_compatibility_status",
            "primitive_projection_descent_proved",
            "mathematical_certification",
            "proof_reference",
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
            "primitive_projection_descent_status",
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
    return read_table_path(fixture / spec.path, spec.columns)


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
        "e_quotient_descent_imported",
        "hall_coproduct_descent_imported",
        "theta_mu_primitives_imported",
        "transition_primitive_subspace_imported",
        "compact_hall_source_imported",
        "primitive_projection_descent_criterion_recorded",
        "theta_primitive_available_for_supplied_rows",
        "theta_projection_available_for_supplied_rows",
        "theta_kernel_intertwining_available_for_supplied_rows",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "quotient_orientation_rows_supplied",
        "hall_coproduct_orientation_descent_supplied",
        "source_hall_coproduct_rows_supplied",
        "source_counit_rows_supplied",
        "source_primitive_kernel_rows_supplied",
        "source_primitive_projection_rows_supplied",
        "primitive_projection_descent",
        "transition_compatibility",
        "protected_integration",
        "aggregate_hybrid_population",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(E_QUOTIENT_FIXTURE),
            str(COPRODUCT_DESCENT_FIXTURE),
            str(THETA_PRIMITIVES_FIXTURE),
            str(TRANSITION_PRIMITIVE_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    e_manifest = read_json(E_QUOTIENT_FIXTURE / "manifest.json")
    require_equal(e_manifest.get("status"), E_QUOTIENT_STATUS, "E quotient status")
    require_equal(e_manifest.get("quotient_orientation"), False, "E quotient orientation")
    require_equal(e_manifest.get("quotient_borel_rows_supplied"), False, "quotient Borel rows")

    coproduct_manifest = read_json(COPRODUCT_DESCENT_FIXTURE / "manifest.json")
    require_equal(coproduct_manifest.get("status"), COPRODUCT_DESCENT_STATUS, "coproduct descent status")
    require_equal(coproduct_manifest.get("hall_coproduct_descent"), False, "coproduct descent")
    require_equal(
        coproduct_manifest.get("source_hall_coproduct_rows_supplied"),
        False,
        "source coproduct rows",
    )
    require_equal(coproduct_manifest.get("source_counit_rows_supplied"), False, "source counit rows")

    primitive_manifest = read_json(THETA_PRIMITIVES_FIXTURE / "manifest.json")
    require_equal(primitive_manifest.get("status"), THETA_PRIMITIVES_STATUS, "theta primitive status")
    require_equal(primitive_manifest.get("theta_mu_primitive_compatible"), True, "theta primitive compatible")
    require_equal(primitive_manifest.get("primitive_certification"), True, "primitive certification")
    require_equal(primitive_manifest.get("primitive_defect_rank"), 0, "primitive defect")
    require_equal(
        primitive_manifest.get("primitive_projection_defect_rank"),
        0,
        "primitive projection defect",
    )
    require_equal(
        primitive_manifest.get("primitive_kernel_intertwining_defect_rank"),
        0,
        "primitive kernel intertwining defect",
    )
    require_equal(
        primitive_manifest.get("protected_integration_certification"),
        False,
        "theta primitive integration",
    )
    require_equal(primitive_manifest.get("aggregate_hybrid_population"), False, "theta primitive aggregate")

    transition_manifest = read_json(TRANSITION_PRIMITIVE_FIXTURE / "manifest.json")
    require_equal(
        transition_manifest.get("status"),
        TRANSITION_PRIMITIVE_STATUS,
        "transition primitive status",
    )
    require_equal(
        transition_manifest.get("primitive_transition_certification"),
        False,
        "primitive transition certification",
    )
    require_equal(transition_manifest.get("mathematical_certification"), False, "transition primitive math")

    compact_manifest = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(compact_manifest.get("obstruction_ledger_status"), COMPACT_SOURCE_STATUS, "compact source status")
    require_equal(compact_manifest.get("empty_blocked"), True, "compact source empty")
    require_equal(compact_manifest.get("compact_source_recognition"), False, "compact source recognition")
    require_equal(compact_manifest.get("mathematical_certification"), False, "compact source math")

    compact_blocked = rows_by(
        read_table_path(COMPACT_SOURCE_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "compact source obligations",
    )
    for obligation_id in (
        "hall_coproduct_D",
        "hall_counit",
        "identity_primitive_closure",
    ):
        if obligation_id not in compact_blocked:
            raise ValueError(f"compact source ledger missing {obligation_id}")
        require_equal(
            compact_blocked[obligation_id]["source_status"],
            "missing_open_obligation",
            f"{obligation_id} source_status",
        )
        require_equal(compact_blocked[obligation_id]["check_status"], "verified", f"{obligation_id} check")

    transition_blocked = rows_by(
        read_table_path(TRANSITION_PRIMITIVE_FIXTURE / "blocked_obligations.csv", None),
        "obligation_id",
        "transition primitive obligations",
    )
    for obligation_id in (
        "source_hall_coproduct_matrix",
        "source_counit_map",
        "source_primitive_kernel",
        "primitive_projection_matrix",
        "primitive_restricted_transition_matrix",
    ):
        if obligation_id not in transition_blocked:
            raise ValueError(f"transition primitive ledger missing {obligation_id}")
        require_equal(
            transition_blocked[obligation_id]["primitive_transition_status"],
            "missing_open_obligation",
            f"{obligation_id} primitive_transition_status",
        )
        require_equal(
            transition_blocked[obligation_id]["check_status"],
            "verified",
            f"{obligation_id} check",
        )

    return {
        "theta_primitive_rows": count_data_rows(THETA_PRIMITIVES_FIXTURE / "primitive_rows.csv"),
        "theta_projection_rows": count_data_rows(THETA_PRIMITIVES_FIXTURE / "primitive_projection_rows.csv"),
        "theta_kernel_rows": count_data_rows(THETA_PRIMITIVES_FIXTURE / "kernel_intertwining_rows.csv"),
        "d_entries": count_data_rows(COMPACT_SOURCE_FIXTURE / "D_entries.csv"),
        "unit_counit": count_data_rows(COMPACT_SOURCE_FIXTURE / "unit_counit.csv"),
        "primitive_kernel_rows": count_data_rows(TRANSITION_PRIMITIVE_FIXTURE / "primitive_kernel_rows.csv"),
        "primitive_transition_rows": count_data_rows(TRANSITION_PRIMITIVE_FIXTURE / "primitive_transition_matrices.csv"),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "e_quotient_descent": E_QUOTIENT_STATUS,
        "hall_coproduct_descent": COPRODUCT_DESCENT_STATUS,
        "theta_mu_primitives": THETA_PRIMITIVES_STATUS,
        "transition_primitive_subspace": TRANSITION_PRIMITIVE_STATUS,
        "compact_hall_source": COMPACT_SOURCE_STATUS,
        "primitive_projection_descent_criterion": "proved_criterion",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"orientation_primitive_projection_descent"}, "criterion ids")
    row = rows["orientation_primitive_projection_descent"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "quotient_orientation_required",
        "hall_coproduct_descent_required",
        "unit_counit_descent_required",
        "source_coproduct_row_required",
        "counit_row_required",
        "primitive_kernel_required",
        "primitive_projection_required",
        "theta_primitive_required",
        "kernel_intertwining_required",
        "projection_commutator_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(
        bool_cell(row, "primitive_projection_descent_proved"),
        False,
        "primitive projection descent proved",
    )


def verify_imported_status_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["imported_status_rows.csv"], "import_id", "imported rows")
    expected = {
        "row302_quotient_orientation": E_QUOTIENT_STATUS,
        "row304_hall_coproduct_descent": COPRODUCT_DESCENT_STATUS,
        "theta_mu_primitives": THETA_PRIMITIVES_STATUS,
        "transition_primitive_subspace": TRANSITION_PRIMITIVE_STATUS,
        "compact_source": COMPACT_SOURCE_STATUS,
    }
    require_equal(set(rows), set(expected), "import ids")
    for import_id, status in expected.items():
        row = rows[import_id]
        require_equal(row["import_status"], status, f"{import_id} status")
        check_verified(row, "imported_status_rows.csv")
        if not row["positive_input"] or not row["missing_input"]:
            raise ValueError(f"{import_id}: missing positive or missing input description")


def verify_obstruction_rows(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(
        tables["primitive_projection_descent_obstruction_rows.csv"],
        "obstruction_id",
        "obstruction rows",
    )
    require_equal(set(rows), {"orientation_primitive_projection_descent"}, "obstruction ids")
    row = rows["orientation_primitive_projection_descent"]
    check_verified(row, "primitive_projection_descent_obstruction_rows.csv")
    for key in (
        "quotient_orientation_status",
        "hall_coproduct_descent_status",
        "unit_counit_orientation_descent_status",
        "source_coproduct_matrix_status",
        "counit_status",
        "source_primitive_kernel_status",
        "primitive_projection_matrix_status",
        "transition_compatibility_status",
    ):
        require_equal(row[key], "missing_open_obligation", key)
    for key in (
        "theta_primitive_status",
        "kernel_intertwining_status",
        "projection_commutator_status",
    ):
        require_equal(row[key], "available_for_supplied_primitive_rows", key)
    require_equal(bool_cell(row, "primitive_projection_descent_proved"), False, "descent proved")
    require_equal(bool_cell(row, "mathematical_certification"), False, "math certification")


def verify_coverage(tables: dict[str, list[dict[str, str]]], counts: dict[str, int]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed["theta_primitive_rows_available"] = counts["theta_primitive_rows"]
    computed["theta_projection_rows_available"] = counts["theta_projection_rows"]
    computed["theta_kernel_intertwining_rows_available"] = counts["theta_kernel_rows"]
    computed["source_hall_coproduct_matrix_rows_supplied"] = counts["d_entries"]
    computed["source_counit_rows_supplied"] = counts["unit_counit"]
    computed["source_primitive_kernel_rows_supplied"] = counts["primitive_kernel_rows"]
    computed["source_primitive_projection_rows_supplied"] = counts["primitive_transition_rows"]
    computed["transition_primitive_rows_supplied"] = counts["primitive_transition_rows"]
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
        require_equal(
            row["primitive_projection_descent_status"],
            "missing_open_obligation",
            f"{row['obligation_id']} status",
        )
        require_equal(row["check_status"], "verified", f"{row['obligation_id']} check")
        if not row["mathematical_payload"] or not row["why_required"]:
            raise ValueError(f"{row['obligation_id']}: missing payload or reason")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        require_equal(row["check_status"], "verified", f"{row['forbidden_substitute']} check")
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
    verify_imported_status_rows(tables)
    verify_obstruction_rows(tables)
    verify_coverage(tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_ORIENTATION_PRIMITIVE_PROJECTION_DESCENT_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
