#!/usr/bin/env python3
"""Verify row-324 S3 semidirect orientation-character extension packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_s3_extension_decision_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_s3_extension_decision_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_S3_EXTENSION_DECISION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-character-s3-extension-decision"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_s3_extension_decision")

DET_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_determinant_comparison")
S3_FIXTURE = Path("certificates/automorphic/delta5_s3_chamber_maass_triviality")

DET_STATUS = "RHOMRED_WEYL_ORIENTATION_DETERMINANT_COMPARISON_OBSTRUCTION_VERIFIED"
S3_STATUS = "DELTA5_S3_CHAMBER_MAASS_TRIVIALITY_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "abstract_extension_rows": 2,
    "maass_compatible_extension_rows": 1,
    "row321_epsilon_equals_det_claim": 0,
    "row323_s3_maass_triviality_claim": 1,
    "source_semidirect_hall_lift_claim": 0,
    "source_orientation_extension_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_character_constructed",
    "source_generator_values",
    "source_det_comparison",
    "semidirect_hall_lifts",
    "orientation_line_transport",
    "square_root_compatibility",
    "quotient_orientation_transport",
    "semidirect_relations",
    "row325_separation",
}

REQUIRED_FIREWALL = {
    "maass_s3_triviality_only",
    "abstract_character_extension_only",
    "row321_criterion_only",
    "row320_local_formula_only",
    "target_chamber_action",
    "pfaffian_orientation",
    "scalar_trace",
    "OP_scalar_branch",
    "empty_semidirect_lift_table",
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
            "source_character_required",
            "source_equal_generator_values_required",
            "s3_permutation_action_required",
            "s3_invariance_required",
            "abstract_extension_classification_required",
            "maass_triviality_required",
            "source_semidirect_lifts_required_for_geometric_extension",
            "criterion_recorded",
            "geometric_extension_claimed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "extension_rows.csv",
        (
            "extension_id",
            "s3_character",
            "formula",
            "restricts_to_epsilon_o_on_W2",
            "restricts_to_maass_on_S3",
            "abstract_extension_available",
            "source_hall_lift_required",
            "source_hall_lift_supplied",
            "geometric_extension_claimed",
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
            "extension_status",
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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "determinant_comparison_imported",
        "s3_maass_triviality_imported",
        "s3_generator_permutation_recorded",
        "abstract_invariance_criterion_recorded",
        "abstract_extensions_classified",
        "maass_compatible_extension_identified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "orientation_character_constructed",
        "epsilon_equals_det_proved",
        "source_generator_signs_supplied",
        "source_semidirect_hall_lifts_supplied",
        "source_orientation_extension_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(DET_FIXTURE), str(S3_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    det_manifest = read_json(DET_FIXTURE / "manifest.json")
    require_equal(det_manifest.get("status"), DET_STATUS, "determinant comparison status")
    require_equal(det_manifest.get("epsilon_equals_det_proved"), False, "epsilon equals det")

    s3_manifest = read_json(S3_FIXTURE / "manifest.json")
    require_equal(s3_manifest.get("status"), S3_STATUS, "S3 Maass status")
    require_equal(s3_manifest.get("triviality_on_s3_proved"), True, "S3 Maass triviality")
    require_equal(s3_manifest.get("epsilon_o_extension_claimed"), False, "S3 source extension")

    return {
        "row321_epsilon_equals_det_claim": int(bool(det_manifest.get("epsilon_equals_det_proved"))),
        "row323_s3_maass_triviality_claim": int(bool(s3_manifest.get("triviality_on_s3_proved"))),
    }


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {"determinant_comparison", "s3_maass_triviality", "s3_chamber_action", "optimization_row"},
        "source ids",
    )
    require_equal(indexed["determinant_comparison"]["source_status"], DET_STATUS, "det source")
    require_equal(indexed["s3_maass_triviality"]["source_status"], S3_STATUS, "S3 source")
    require_equal(indexed["s3_chamber_action"]["source_status"], "S3_chamber_action", "S3 action")
    require_equal(indexed["optimization_row"]["source_status"], "row_324", "optimization row")
    for row in rows:
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "s3_extension_decision", "criterion_id")
    for key in (
        "source_character_required",
        "source_equal_generator_values_required",
        "s3_permutation_action_required",
        "s3_invariance_required",
        "abstract_extension_classification_required",
        "maass_triviality_required",
        "source_semidirect_lifts_required_for_geometric_extension",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "geometric_extension_claimed"), False, "geometric extension")
    check_verified(row, "criterion_rows.csv")


def verify_extensions(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "extension_id", "extension_rows.csv")
    require_equal(set(indexed), {"trivial_s3_extension", "sign_s3_extension"}, "extension ids")
    trivial = indexed["trivial_s3_extension"]
    sign = indexed["sign_s3_extension"]
    require_equal(trivial["s3_character"], "trivial", "trivial character")
    require_equal(sign["s3_character"], "sign", "sign character")
    for row in (trivial, sign):
        require_equal(bool_cell(row, "restricts_to_epsilon_o_on_W2"), True, "restricts to W2")
        require_equal(bool_cell(row, "abstract_extension_available"), True, "abstract available")
        require_equal(bool_cell(row, "source_hall_lift_required"), True, "source lift required")
        require_equal(bool_cell(row, "source_hall_lift_supplied"), False, "source lift supplied")
        require_equal(bool_cell(row, "geometric_extension_claimed"), False, "geometric claimed")
        check_verified(row, "extension_rows.csv")
    require_equal(bool_cell(trivial, "restricts_to_maass_on_S3"), True, "trivial Maass-compatible")
    require_equal(bool_cell(sign, "restricts_to_maass_on_S3"), False, "sign not Maass-compatible")


def verify_coverage(
    rows: list[dict[str, str]],
    manifest: dict,
    import_counts: dict[str, int],
    extension_rows: list[dict[str, str]],
) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    maass_compatible = sum(
        1 for row in extension_rows if bool_cell(row, "restricts_to_maass_on_S3")
    )
    dynamic = dict(EXPECTED_COVERAGE)
    dynamic.update(import_counts)
    dynamic["abstract_extension_rows"] = len(extension_rows)
    dynamic["maass_compatible_extension_rows"] = maass_compatible
    dynamic["source_semidirect_hall_lift_claim"] = int(
        bool(manifest.get("source_semidirect_hall_lifts_supplied"))
    )
    dynamic["source_orientation_extension_claim"] = int(
        bool(manifest.get("source_orientation_extension_claimed"))
    )
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
        require_equal(row["extension_status"], "missing_open_obligation", "extension status")
        check_verified(row, "blocked_obligations.csv")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "forbidden_substitute", "scalar_firewall.csv")
    require_equal(set(indexed), REQUIRED_FIREWALL, "firewall substitutes")
    for row in indexed.values():
        require_equal(bool_cell(row, "excluded"), True, "firewall excluded")
        require_equal(int_cell(row, "defect_rank"), 0, "firewall defect")
        check_verified(row, "scalar_firewall.csv")


def verify_fixture(fixture: Path) -> None:
    manifest = verify_manifest(fixture)
    import_counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    verify_criterion(tables["criterion_rows.csv"])
    verify_extensions(tables["extension_rows.csv"])
    verify_coverage(
        tables["coverage_rows.csv"],
        manifest,
        import_counts,
        tables["extension_rows.csv"],
    )
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
