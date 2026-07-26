#!/usr/bin/env python3
"""Verify row-318 Weyl preservation of lambda^H=0 packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_finite_stabilizer_lambda_zero_preservation_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_finite_stabilizer_lambda_zero_preservation_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_FINITE_STABILIZER_LAMBDA_ZERO_PRESERVATION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:weyl-finite-stabilizer-lambda-zero-preservation-criterion"
DEFAULT_FIXTURE = Path(
    "certificates/orientation/rhomred_weyl_finite_stabilizer_lambda_zero_preservation"
)

CHARACTER_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_linearization_character")
VANISHING_FIXTURE = Path("certificates/orientation/rhomred_finite_stabilizer_linearization_vanishing")
TAU_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")
BETA_PRES_FIXTURE = Path("certificates/orientation/rhomred_weyl_finite_stabilizer_beta_preservation")

CHARACTER_STATUS = "RHOMRED_FINITE_STABILIZER_LINEARIZATION_CHARACTER_OBSTRUCTION_VERIFIED"
VANISHING_STATUS = "RHOMRED_FINITE_STABILIZER_LINEARIZATION_VANISHING_OBSTRUCTION_VERIFIED"
TAU_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
BETA_PRES_STATUS = "RHOMRED_WEYL_FINITE_STABILIZER_BETA_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "row288_lambda_rows": 3,
    "row288_lambda_computed_claim": 0,
    "row288_lambda_vanishing_claim": 0,
    "row289_lambda_vanishing_rows": 3,
    "row289_lambda_vanishing_claim": 0,
    "row306_tau_transport_claim": 0,
    "row317_beta_preservation_claim": 0,
    "preservation_rows": 0,
    "lambda_zero_preservation_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_target_lambda_coordinates",
    "stabilizer_isomorphism",
    "h1_bh_transport_matrix",
    "orientation_line_action_transport",
    "coordinate_defect_vector",
    "zero_vector_row",
    "all_retained_wall_coverage",
    "row288_completion",
    "row289_vanishing",
    "row306_tau_transport",
    "row317_beta_preservation",
    "row319_separation",
}

REQUIRED_FIREWALL = {
    "residual_group_order_one",
    "H1_B1_zero_template",
    "missing_lambda_value",
    "lambda_character_not_computed",
    "beta_zero_claim",
    "beta_nulltrivialization",
    "row317_beta_preservation",
    "row306_tau_criterion",
    "determinant_anchor_translation_weight",
    "target_coxeter_graph",
    "maass_character_value",
    "pfaffian_wall_sign",
    "scalar_trace",
    "empty_preservation_table",
    "row319_orientation_character",
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
            "stabilizer_isomorphism_required",
            "source_target_lambda_required",
            "h1_bh_transport_matrix_required",
            "orientation_line_action_transport_required",
            "coordinate_defect_required",
            "zero_vector_required",
            "all_retained_coverage_required",
            "lambda_zero_dependency_required",
            "beta_preservation_dependency_required",
            "criterion_recorded",
            "lambda_zero_preservation_proved",
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
            "source_lambda_row_id",
            "target_lambda_row_id",
            "source_residual_group_id",
            "target_residual_group_id",
            "stabilizer_isomorphism_id",
            "h1_bh_matrix_id",
            "source_lambda_vector_id",
            "target_lambda_vector_id",
            "coordinate_defect_vector_id",
            "coordinate_defect_rank",
            "action_transport_defect_rank",
            "lambda_zero_preserved",
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
        "linearization_character_imported",
        "linearization_vanishing_imported",
        "weyl_wall_transport_imported",
        "beta_preservation_imported",
        "preservation_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "stabilizer_isomorphism_rows_supplied",
        "source_target_lambda_rows_supplied",
        "h1_bh_transport_matrices_supplied",
        "orientation_line_action_transport_rows_supplied",
        "coordinate_defect_rows_supplied",
        "zero_vector_rows_supplied",
        "retained_coverage_rows_supplied",
        "lambda_zero_preservation_proved",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(CHARACTER_FIXTURE),
            str(VANISHING_FIXTURE),
            str(TAU_FIXTURE),
            str(BETA_PRES_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    character_manifest = read_json(CHARACTER_FIXTURE / "manifest.json")
    require_equal(character_manifest.get("status"), CHARACTER_STATUS, "character status")
    require_equal(character_manifest.get("h1_coordinates_computed"), False, "H1 coordinates")
    require_equal(
        character_manifest.get("all_retained_lambda_computed"),
        False,
        "all lambda computed",
    )
    require_equal(
        character_manifest.get("lambda_vanishing_verified"),
        False,
        "lambda vanishing in character packet",
    )

    vanishing_manifest = read_json(VANISHING_FIXTURE / "manifest.json")
    require_equal(vanishing_manifest.get("status"), VANISHING_STATUS, "vanishing status")
    require_equal(
        vanishing_manifest.get("all_retained_lambda_vanishing_verified"),
        False,
        "all lambda vanishing",
    )
    require_equal(
        vanishing_manifest.get("lambda_character_computed"),
        False,
        "lambda character computed in vanishing packet",
    )

    tau_manifest = read_json(TAU_FIXTURE / "manifest.json")
    require_equal(tau_manifest.get("status"), TAU_STATUS, "tau status")
    require_equal(tau_manifest.get("tau_transport_constructed"), False, "tau constructed")
    require_equal(tau_manifest.get("weyl_lift_rows_supplied"), False, "tau Weyl lift rows")

    beta_pres_manifest = read_json(BETA_PRES_FIXTURE / "manifest.json")
    require_equal(beta_pres_manifest.get("status"), BETA_PRES_STATUS, "beta preservation status")
    require_equal(
        beta_pres_manifest.get("finite_stabilizer_beta_preservation_proved"),
        False,
        "finite-stabilizer beta preservation proved",
    )

    return {
        "row288_lambda_rows": count_data_rows(
            CHARACTER_FIXTURE / "linearization_character_obstruction_rows.csv"
        ),
        "row288_lambda_computed_claim": int(
            bool(character_manifest.get("all_retained_lambda_computed"))
        ),
        "row288_lambda_vanishing_claim": int(
            bool(character_manifest.get("lambda_vanishing_verified"))
        ),
        "row289_lambda_vanishing_rows": count_data_rows(
            VANISHING_FIXTURE / "linearization_vanishing_obstruction_rows.csv"
        ),
        "row289_lambda_vanishing_claim": int(
            bool(vanishing_manifest.get("all_retained_lambda_vanishing_verified"))
        ),
        "row306_tau_transport_claim": int(bool(tau_manifest.get("tau_transport_constructed"))),
        "row317_beta_preservation_claim": int(
            bool(beta_pres_manifest.get("finite_stabilizer_beta_preservation_proved"))
        ),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "linearization_character": CHARACTER_STATUS,
        "linearization_vanishing": VANISHING_STATUS,
        "weyl_wall_transport": TAU_STATUS,
        "beta_preservation": BETA_PRES_STATUS,
        "optimization_row": "row_318",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["criterion_rows.csv"], "criterion_id", "criterion rows")
    expected_id = "weyl_finite_stabilizer_lambda_zero_preservation"
    require_equal(set(rows), {expected_id}, "criterion ids")
    row = rows[expected_id]
    check_verified(row, "criterion_rows.csv")
    for key in (
        "stabilizer_isomorphism_required",
        "source_target_lambda_required",
        "h1_bh_transport_matrix_required",
        "orientation_line_action_transport_required",
        "coordinate_defect_required",
        "zero_vector_required",
        "all_retained_coverage_required",
        "lambda_zero_dependency_required",
        "beta_preservation_dependency_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(
        bool_cell(row, "lambda_zero_preservation_proved"),
        False,
        "lambda zero preservation proved",
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
    computed["lambda_zero_preservation_claim"] = int(
        bool(manifest.get("lambda_zero_preservation_proved"))
    )
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(
            int_cell(row, "computed_value"),
            computed[coverage_id],
            f"{coverage_id} computed",
        )
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(
            row["preservation_status"],
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
        print(
            f"RHOMRED_WEYL_FINITE_STABILIZER_LAMBDA_ZERO_PRESERVATION_BLOCKED: {exc}",
            file=sys.stderr,
        )
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
