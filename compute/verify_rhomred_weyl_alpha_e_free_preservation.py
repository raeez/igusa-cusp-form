#!/usr/bin/env python3
"""Verify row-316 Weyl preservation of alpha_E_free packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_alpha_e_free_preservation_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_alpha_e_free_preservation_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ALPHA_E_FREE_PRESERVATION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:weyl-alpha-e-free-preservation-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_alpha_e_free_preservation")

FREE_E_FIXTURE = Path("certificates/orientation/rhomred_free_e_borel")
FREE_E_VANISHING_FIXTURE = Path("certificates/orientation/rhomred_free_e_vanishing")
FREE_E_NULL_FIXTURE = Path("certificates/orientation/rhomred_free_e_nulltrivialization")
TAU_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")
ALPHA_RED_PRES_FIXTURE = Path("certificates/orientation/rhomred_weyl_alpha_red_preservation")

FREE_E_STATUS = "RHOMRED_FREE_E_BOREL_OBSTRUCTION_VERIFIED"
FREE_E_VANISHING_STATUS = "RHOMRED_FREE_E_VANISHING_OBSTRUCTION_VERIFIED"
FREE_E_NULL_STATUS = "RHOMRED_FREE_E_NULLTRIVIALIZATION_OBSTRUCTION_VERIFIED"
TAU_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
ALPHA_RED_PRES_STATUS = "RHOMRED_WEYL_ALPHA_RED_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "row282_free_e_rows": 3,
    "row282_free_e_values_computed_claim": 0,
    "row282_free_e_vanishing_claim": 0,
    "row283_free_e_vanishing_rows": 3,
    "row283_free_e_vanishing_claim": 0,
    "row284_nulltrivialization_rows": 3,
    "row284_nulltrivialization_claim": 0,
    "row306_tau_transport_claim": 0,
    "row315_alpha_red_preservation_claim": 0,
    "preservation_rows": 0,
    "alpha_e_free_preservation_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_target_coefficients",
    "h2_be_transport_matrix",
    "cochain_transport_defect",
    "coordinate_defect_vector",
    "zero_vector_certificate",
    "all_retained_wall_coverage",
    "row282_completion",
    "row283_vanishing",
    "row284_nulltrivialization",
    "row306_tau_transport",
    "row315_alpha_red_preservation",
    "row317_separation",
}

REQUIRED_FIREWALL = {
    "H1_BE_zero",
    "free_E_action_only",
    "quotient_stack_only",
    "missing_coefficients",
    "row284_nulltrivialization_only",
    "row306_tau_criterion",
    "row315_alpha_red_preservation",
    "target_coxeter_graph",
    "maass_character_value",
    "pfaffian_wall_sign",
    "scalar_trace",
    "finite_stabilizer_bits",
    "empty_preservation_table",
    "row317_finite_beta_preservation",
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
            "source_target_coefficients_required",
            "h2_be_transport_matrix_required",
            "coordinate_defect_required",
            "zero_vector_required",
            "cochain_transport_defect_required",
            "all_retained_coverage_required",
            "free_e_nulltrivialization_dependency_required",
            "alpha_red_preservation_dependency_required",
            "criterion_recorded",
            "alpha_e_free_preservation_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "preservation_rows.csv",
        (
            "preservation_id",
            "R_id",
            "source_stratum_id",
            "target_stratum_id",
            "delta_id",
            "source_free_e_id",
            "target_free_e_id",
            "h2_be_matrix_id",
            "source_a1",
            "source_a2",
            "target_a1",
            "target_a2",
            "coordinate_defect_vector_id",
            "coordinate_defect_rank",
            "cochain_transport_defect_rank",
            "alpha_e_free_preserved",
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
            "preservation_status",
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


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "free_e_borel_imported",
        "free_e_vanishing_imported",
        "free_e_nulltrivialization_imported",
        "weyl_wall_transport_imported",
        "alpha_red_preservation_imported",
        "preservation_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_target_coefficient_rows_supplied",
        "h2_be_transport_matrices_supplied",
        "coordinate_defect_rows_supplied",
        "zero_vector_rows_supplied",
        "cochain_transport_defect_rows_supplied",
        "retained_coverage_rows_supplied",
        "alpha_e_free_preservation_proved",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(FREE_E_FIXTURE),
            str(FREE_E_VANISHING_FIXTURE),
            str(FREE_E_NULL_FIXTURE),
            str(TAU_FIXTURE),
            str(ALPHA_RED_PRES_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    free_e_manifest = read_json(FREE_E_FIXTURE / "manifest.json")
    require_equal(free_e_manifest.get("status"), FREE_E_STATUS, "free-E status")
    require_equal(free_e_manifest.get("free_e_class_values_computed"), False, "free-E computed")
    require_equal(free_e_manifest.get("free_e_vanishing_verified"), False, "free-E vanishing")

    vanishing_manifest = read_json(FREE_E_VANISHING_FIXTURE / "manifest.json")
    require_equal(
        vanishing_manifest.get("status"),
        FREE_E_VANISHING_STATUS,
        "free-E vanishing status",
    )
    require_equal(
        vanishing_manifest.get("free_e_vanishing_verified"),
        False,
        "free-E vanishing proved",
    )

    null_manifest = read_json(FREE_E_NULL_FIXTURE / "manifest.json")
    require_equal(null_manifest.get("status"), FREE_E_NULL_STATUS, "free-E null status")
    require_equal(
        null_manifest.get("nulltrivializations_supplied"),
        False,
        "free-E nulltrivializations",
    )

    tau_manifest = read_json(TAU_FIXTURE / "manifest.json")
    require_equal(tau_manifest.get("status"), TAU_STATUS, "tau status")
    require_equal(tau_manifest.get("tau_transport_constructed"), False, "tau constructed")
    require_equal(tau_manifest.get("weyl_lift_rows_supplied"), False, "tau Weyl lift rows")

    alpha_red_manifest = read_json(ALPHA_RED_PRES_FIXTURE / "manifest.json")
    require_equal(
        alpha_red_manifest.get("status"),
        ALPHA_RED_PRES_STATUS,
        "alpha-red preservation status",
    )
    require_equal(
        alpha_red_manifest.get("alpha_red_preservation_proved"),
        False,
        "alpha-red preservation proved",
    )

    return {
        "row282_free_e_rows": count_data_rows(FREE_E_FIXTURE / "free_e_obstruction_rows.csv"),
        "row282_free_e_values_computed_claim": int(
            bool(free_e_manifest.get("free_e_class_values_computed"))
        ),
        "row282_free_e_vanishing_claim": int(
            bool(free_e_manifest.get("free_e_vanishing_verified"))
        ),
        "row283_free_e_vanishing_rows": count_data_rows(
            FREE_E_VANISHING_FIXTURE / "free_e_vanishing_obstruction_rows.csv"
        ),
        "row283_free_e_vanishing_claim": int(
            bool(vanishing_manifest.get("free_e_vanishing_verified"))
        ),
        "row284_nulltrivialization_rows": count_data_rows(
            FREE_E_NULL_FIXTURE / "nulltrivialization_obstruction_rows.csv"
        ),
        "row284_nulltrivialization_claim": int(
            bool(null_manifest.get("nulltrivializations_supplied"))
        ),
        "row306_tau_transport_claim": int(bool(tau_manifest.get("tau_transport_constructed"))),
        "row315_alpha_red_preservation_claim": int(
            bool(alpha_red_manifest.get("alpha_red_preservation_proved"))
        ),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "free_e_borel": FREE_E_STATUS,
        "free_e_vanishing": FREE_E_VANISHING_STATUS,
        "free_e_nulltrivialization": FREE_E_NULL_STATUS,
        "weyl_wall_transport": TAU_STATUS,
        "alpha_red_preservation": ALPHA_RED_PRES_STATUS,
        "optimization_row": "row_316",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    require_equal(set(rows), {"weyl_alpha_e_free_preservation"}, "criterion ids")
    row = rows["weyl_alpha_e_free_preservation"]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "source_target_coefficients_required",
        "h2_be_transport_matrix_required",
        "coordinate_defect_required",
        "zero_vector_required",
        "cochain_transport_defect_required",
        "all_retained_coverage_required",
        "free_e_nulltrivialization_dependency_required",
        "alpha_red_preservation_dependency_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(
        bool_cell(row, "alpha_e_free_preservation_proved"),
        False,
        "alpha-E-free preservation proved",
    )


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    if tables["preservation_rows.csv"]:
        raise ValueError("preservation_rows.csv must remain empty in obstruction packet")


def verify_coverage(
    manifest: dict,
    tables: dict[str, list[dict[str, str]]],
    counts: dict[str, int],
) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed.update(counts)
    computed["preservation_rows"] = len(tables["preservation_rows.csv"])
    computed["alpha_e_free_preservation_claim"] = int(
        bool(manifest.get("alpha_e_free_preservation_proved"))
    )
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
        require_equal(row["preservation_status"], "missing_open_obligation", f"{row['obligation_id']} status")
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
    manifest = verify_manifest(fixture)
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_criterion(tables)
    verify_empty_tables(tables)
    verify_coverage(manifest, tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_WEYL_ALPHA_E_FREE_PRESERVATION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
