#!/usr/bin/env python3
"""Verify row-322 orientation-character Maass-comparison packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_maass_comparison_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_maass_comparison_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_MAASS_COMPARISON_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-character-maass-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_maass_comparison")

DET_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_determinant_comparison")
MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")

DET_STATUS = "RHOMRED_WEYL_ORIENTATION_DETERMINANT_COMPARISON_OBSTRUCTION_VERIFIED"
MAASS_SCHEMA = "delta5_maass_character.v1"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "comparison_rows": 1,
    "row321_epsilon_equals_det_claim": 0,
    "maass_determinant_restriction_rows": 1,
    "maass_orientation_character_claim": 0,
    "epsilon_equals_maass_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_det_comparison",
    "inverse_limit_character",
    "maass_firewall",
    "row323_separation",
}

REQUIRED_FIREWALL = {
    "maass_character_value",
    "maass_determinant_restriction_only",
    "row321_criterion_only",
    "row320_local_formula_only",
    "determinant_character_only",
    "target_coxeter_graph",
    "squared_determinant",
    "scalar_trace",
    "OP_scalar_branch",
    "automorphic_line_only",
    "row323_chamber_comparison",
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
            "source_det_comparison_required",
            "maass_det_restriction_required",
            "transitivity_required",
            "inverse_limit_character_required",
            "maass_as_source_allowed",
            "criterion_recorded",
            "epsilon_equals_maass_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "comparison_rows.csv",
        (
            "comparison_id",
            "subgroup",
            "source_det_equality_required",
            "source_det_equality_supplied",
            "maass_det_equality_required",
            "maass_det_equality_supplied",
            "conclusion_if_supplied",
            "comparison_verified",
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
            "comparison_status",
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


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


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
        "determinant_comparison_imported",
        "maass_character_imported",
        "maass_determinant_restriction_recorded",
        "transitivity_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_character_constructed",
        "epsilon_equals_det_proved",
        "epsilon_equals_maass_proved",
        "inverse_limit_character_supplied",
        "maass_as_source_allowed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(DET_FIXTURE), str(MAASS_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> dict[str, int]:
    det_manifest = read_json(DET_FIXTURE / "manifest.json")
    require_equal(det_manifest.get("status"), DET_STATUS, "determinant comparison status")
    require_equal(det_manifest.get("epsilon_equals_det_proved"), False, "epsilon equals det")

    maass_manifest = read_json(MAASS_FIXTURE / "manifest.json")
    require_equal(maass_manifest.get("schema_version"), MAASS_SCHEMA, "Maass schema")
    require_equal(maass_manifest.get("automorphic_character_certified"), True, "Maass certified")
    require_equal(maass_manifest.get("orientation_character"), False, "Maass orientation firewall")
    require_equal(maass_manifest.get("pfaffian_line"), False, "Maass Pfaffian firewall")

    relations = read_table_path(MAASS_FIXTURE / "character_relations.csv", None)
    det_restrictions = [
        row
        for row in relations
        if row.get("relation_id") == "weyl_restriction_determinant"
        and row.get("relation_kind") == "character_equals_determinant"
        and row.get("computed_value") == "1"
        and row.get("expected_value") == "1"
        and row.get("defect_rank") == "0"
        and row.get("check_status") == "verified"
    ]

    return {
        "row321_epsilon_equals_det_claim": int(bool(det_manifest.get("epsilon_equals_det_proved"))),
        "maass_determinant_restriction_rows": len(det_restrictions),
        "maass_orientation_character_claim": int(bool(maass_manifest.get("orientation_character"))),
    }


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(set(indexed), {"determinant_comparison", "maass_character", "optimization_row"}, "source ids")
    require_equal(indexed["determinant_comparison"]["source_status"], DET_STATUS, "det source")
    require_equal(indexed["maass_character"]["source_status"], MAASS_SCHEMA, "maass source")
    require_equal(indexed["optimization_row"]["source_status"], "row_322", "optimization row")
    for row in rows:
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "maass_character_comparison", "criterion_id")
    for key in (
        "source_det_comparison_required",
        "maass_det_restriction_required",
        "transitivity_required",
        "inverse_limit_character_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in ("maass_as_source_allowed", "epsilon_equals_maass_proved"):
        require_equal(bool_cell(row, key), False, key)
    check_verified(row, "criterion_rows.csv")


def verify_comparison(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "comparison row count")
    row = rows[0]
    require_equal(row["comparison_id"], "w2_maass_comparison", "comparison_id")
    require_equal(row["subgroup"], "W2", "subgroup")
    require_equal(bool_cell(row, "source_det_equality_required"), True, "source required")
    require_equal(bool_cell(row, "source_det_equality_supplied"), False, "source supplied")
    require_equal(bool_cell(row, "maass_det_equality_required"), True, "maass required")
    require_equal(bool_cell(row, "maass_det_equality_supplied"), True, "maass supplied")
    require_equal(bool_cell(row, "conclusion_if_supplied"), True, "conditional conclusion")
    require_equal(bool_cell(row, "comparison_verified"), False, "comparison verified")
    check_verified(row, "comparison_rows.csv")


def verify_coverage(
    rows: list[dict[str, str]],
    import_counts: dict[str, int],
    comparison_count: int,
) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    dynamic = dict(EXPECTED_COVERAGE)
    dynamic.update(import_counts)
    dynamic["comparison_rows"] = comparison_count
    for key, expected in dynamic.items():
        row = indexed[key]
        require_equal(int_cell(row, "computed_value"), expected, f"{key} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{key} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{key} defect")
        check_verified(row, "coverage_rows.csv", proof_required=False)


def verify_obligations(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "obligation_id", "blocked_obligations.csv")
    require_equal(set(indexed), REQUIRED_OBLIGATIONS, "obligation ids")
    for row in indexed.values():
        require_equal(row["comparison_status"], "missing_open_obligation", "comparison status")
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
    import_counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    verify_criterion(tables["criterion_rows.csv"])
    verify_comparison(tables["comparison_rows.csv"])
    verify_coverage(tables["coverage_rows.csv"], import_counts, len(tables["comparison_rows.csv"]))
    verify_obligations(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
