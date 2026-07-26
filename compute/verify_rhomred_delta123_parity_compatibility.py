#!/usr/bin/env python3
"""Verify row-332 delta123 orientation-line parity-compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_delta123_parity_compatibility_obstruction.v1"
EXPECTED_KIND = "rhomred_delta123_parity_compatibility_obstruction"
SUCCESS_STATUS = "RHOMRED_DELTA123_PARITY_COMPATIBILITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-line-delta123-parity-compatibility"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_delta123_parity_compatibility")

DELTA123_FIXTURE = Path("certificates/targets/delta5_gn_kac/delta123_presentation_split")
ROW331_FIXTURE = Path("certificates/orientation/rhomred_delta123_chart_orientation")
DETERMINANT_FIXTURE = Path("certificates/orientation/rhomred_determinant")
SQUARE_ROOT_FIXTURE = Path("certificates/orientation/rhomred_square_root")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
TRANSITION_PARITY_FIXTURE = Path("certificates/hall/transition_parity_decomposition_preservation")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

DELTA123_SCHEMA = "delta123_presentation_split.v1"
ROW331_STATUS = "RHOMRED_DELTA123_CHART_ORIENTATION_OBSTRUCTION_VERIFIED"
DETERMINANT_STATUS = "RHOMRED_DETERMINANT_VERIFIED"
SQUARE_ROOT_STATUS = "RHOMRED_SQUARE_ROOT_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
TRANSITION_PARITY_STATUS = "TRANSITION_PARITY_DECOMPOSITION_PRESERVATION_OBSTRUCTION_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "target_delta123_even_rank": 29,
    "target_delta123_odd_rank": 93,
    "target_delta123_signed_dimension": -64,
    "expected_chart_sign": -1,
    "determinant_line_input": 1,
    "orientation_square_root_rows": 0,
    "source_parity_block_rows": 0,
    "source_parity_involution_rows": 0,
    "parity_transition_rows": 0,
    "orientation_transition_rows": 0,
    "compatibility_rows": 0,
    "unconditional_compatibility_claim": 0,
    "row333_negative_root_claim": 0,
    "row334_chevalley_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_parity_block",
    "source_parity_involution",
    "source_target_comparison",
    "orientation_square_root",
    "ber_factorization",
    "determinant_square",
    "quotient_orientation",
    "parity_commutator_transition",
    "off_diagonal_zero_transition",
    "orientation_line_pullback",
    "orientation_mittag_leffler",
    "row333_negative_root_compatibility",
    "row334_chevalley_antiinvolution",
}

REQUIRED_FIREWALL = {
    "target_parity_29_93",
    "signed_superdimension_minus64",
    "row331_chart_sign_minus_one",
    "determinant_line_only",
    "square_root_obstruction_ledger",
    "compact_Hall_empty_ledger",
    "transition_parity_obstruction_ledger",
    "transition_orientation_obstruction_ledger",
    "formal_parity_pushforward",
    "scalar_trace",
    "protected_trace",
    "pfaffian_product",
    "maass_character_value",
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
            "target_delta123_split_required",
            "source_parity_block_required",
            "source_parity_involution_required",
            "source_target_comparison_required",
            "determinant_line_required",
            "orientation_square_root_required",
            "ber_factorization_required",
            "determinant_square_required",
            "quotient_orientation_required",
            "parity_transition_required",
            "orientation_transition_required",
            "target_split_as_source_allowed",
            "row331_chart_sign_as_line_compatibility_allowed",
            "criterion_recorded",
            "compatibility_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "compatibility_rows.csv",
        (
            "compatibility_row_id",
            "R_id",
            "stratum_id",
            "degree_id",
            "orientation_line_id",
            "det_complex_id",
            "square_root_id",
            "source_parity_block_id",
            "source_parity_involution_id",
            "source_target_comparison_id",
            "ber_factorization_id",
            "determinant_square_id",
            "quotient_orientation_id",
            "parity_transition_id",
            "orientation_transition_id",
            "odd_rank",
            "orientation_sign",
            "compatibility_verified",
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


def require_empty_csv(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    require_equal(rows, [], str(path))


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "delta123_presentation_split_imported",
        "delta123_chart_orientation_imported",
        "rhomred_determinant_imported",
        "rhomred_square_root_imported",
        "compact_hall_ledger_imported",
        "transition_parity_ledger_imported",
        "transition_orientation_ledger_imported",
        "line_level_parity_compatibility_criterion_recorded",
        "target_delta123_parity_certified",
        "determinant_line_defined",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_parity_block_rows_supplied",
        "source_parity_involution_supplied",
        "source_target_comparison_rows_supplied",
        "orientation_square_root_rows_supplied",
        "quotient_orientation_rows_supplied",
        "determinant_square_rows_supplied",
        "parity_transition_rows_supplied",
        "orientation_transition_rows_supplied",
        "delta123_parity_compatibility_proved",
        "orientation_sign_claimed_unconditionally",
        "row333_negative_root_claimed",
        "row334_chevalley_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(DELTA123_FIXTURE),
            str(ROW331_FIXTURE),
            str(DETERMINANT_FIXTURE),
            str(SQUARE_ROOT_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(TRANSITION_PARITY_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    delta123 = read_json(DELTA123_FIXTURE / "manifest.json")
    require_equal(delta123.get("schema_version"), DELTA123_SCHEMA, "delta123 schema")
    require_equal(delta123.get("certified"), True, "delta123 certified")
    require_equal(delta123.get("target_only"), True, "delta123 target only")
    degree = read_table_path(DELTA123_FIXTURE / "delta123_degree.csv")[0]
    require_equal(degree["degree_id"], "delta123", "delta123 degree id")
    require_equal(int_cell(degree, "full_even"), 29, "delta123 even")
    require_equal(int_cell(degree, "full_odd"), 93, "delta123 odd")
    require_equal(int_cell(degree, "signed_dimension"), -64, "delta123 signed")

    row331 = read_json(ROW331_FIXTURE / "manifest.json")
    require_equal(row331.get("status"), ROW331_STATUS, "row331 status")
    require_equal(row331.get("delta123_orientation_computed"), False, "row331 computed flag")
    require_equal(row331.get("row332_parity_compatibility_claimed"), False, "row331 row332 flag")

    determinant = read_json(DETERMINANT_FIXTURE / "manifest.json")
    require_equal(determinant.get("status"), DETERMINANT_STATUS, "determinant status")
    require_equal(determinant.get("determinant_lines_defined"), True, "determinant lines")
    require_equal(determinant.get("orientation_square_root"), False, "determinant orientation square root")

    square_root = read_json(SQUARE_ROOT_FIXTURE / "manifest.json")
    require_equal(square_root.get("status"), SQUARE_ROOT_STATUS, "square-root status")
    require_equal(square_root.get("square_root_rows_supplied"), False, "square-root rows")
    require_equal(square_root.get("mathematical_certification"), False, "square-root certification")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty")
    require_empty_csv(COMPACT_HALL_FIXTURE / "parity_blocks.csv")

    transition_parity = read_json(TRANSITION_PARITY_FIXTURE / "manifest.json")
    require_equal(transition_parity.get("status"), TRANSITION_PARITY_STATUS, "transition parity status")
    require_equal(transition_parity.get("parity_transition_certification"), False, "transition parity certification")
    for table_name in (
        "parity_decomposition_rows.csv",
        "parity_involutions.csv",
        "parity_transition_matrices.csv",
        "parity_comparison_squares.csv",
        "transition_defects.csv",
    ):
        require_empty_csv(TRANSITION_PARITY_FIXTURE / table_name)

    transition_orientation = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(transition_orientation.get("status"), TRANSITION_ORIENTATION_STATUS, "transition orientation status")
    require_equal(transition_orientation.get("orientation_transition_certification"), False, "transition orientation certification")
    for table_name in (
        "orientation_transition_maps.csv",
        "null_trivialization_transport.csv",
        "multiplicative_weyl_transport.csv",
        "transition_defects.csv",
    ):
        require_empty_csv(TRANSITION_ORIENTATION_FIXTURE / table_name)


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "delta123_presentation_split",
            "delta123_chart_orientation",
            "rhomred_determinant",
            "rhomred_square_root",
            "compact_hall_source",
            "transition_parity",
            "transition_orientation",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "delta123_line_parity_compatibility", "criterion id")
    for key in (
        "target_delta123_split_required",
        "source_parity_block_required",
        "source_parity_involution_required",
        "source_target_comparison_required",
        "determinant_line_required",
        "orientation_square_root_required",
        "ber_factorization_required",
        "determinant_square_required",
        "quotient_orientation_required",
        "parity_transition_required",
        "orientation_transition_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in (
        "target_split_as_source_allowed",
        "row331_chart_sign_as_line_compatibility_allowed",
        "compatibility_proved",
    ):
        require_equal(bool_cell(row, key), False, key)
    check_verified(row, "criterion_rows.csv")


def verify_coverage(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    for key, expected in EXPECTED_COVERAGE.items():
        row = indexed[key]
        require_equal(int_cell(row, "computed_value"), expected, f"{key} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{key} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{key} defect")
        require_equal(row.get("check_status"), "verified", f"{key} status")


def verify_obligations(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "obligation_id", "blocked_obligations.csv")
    require_equal(set(indexed), REQUIRED_OBLIGATIONS, "obligation ids")
    for row in indexed.values():
        require_equal(row["compatibility_status"], "missing_open_obligation", "obligation status")
        check_verified(row, "blocked_obligations.csv")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "forbidden_substitute", "scalar_firewall.csv")
    require_equal(set(indexed), REQUIRED_FIREWALL, "firewall substitutes")
    for row in indexed.values():
        require_equal(bool_cell(row, "excluded"), True, "firewall excluded")
        require_equal(int_cell(row, "defect_rank"), 0, "firewall defect")
        check_verified(row, "scalar_firewall.csv")


def verify_fixture(fixture: Path) -> None:
    verify_manifest(fixture)
    verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    verify_criterion(tables["criterion_rows.csv"])
    require_equal(tables["compatibility_rows.csv"], [], "compatibility rows")
    verify_coverage(tables["coverage_rows.csv"])
    verify_obligations(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
