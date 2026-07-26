#!/usr/bin/env python3
"""Verify row-325 semidirect Hall-lift obstruction packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_semidirect_hall_lifts_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_semidirect_hall_lifts_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_SEMIDIRECT_HALL_LIFTS_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:semidirect-hall-lift-construction-criterion"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_semidirect_hall_lifts")

S3_EXTENSION_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_s3_extension_decision")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
PARTIAL_GROUPOID_FIXTURE = Path("certificates/orientation/rhomred_weyl_partial_action_groupoid")
TAU_FIXTURE = Path("certificates/orientation/rhomred_weyl_wall_transport_tau")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

S3_EXTENSION_STATUS = "RHOMRED_WEYL_ORIENTATION_S3_EXTENSION_DECISION_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
PARTIAL_GROUPOID_STATUS = "RHOMRED_WEYL_PARTIAL_ACTION_GROUPOID_OBSTRUCTION_VERIFIED"
TAU_STATUS = "RHOMRED_WEYL_WALL_TRANSPORT_TAU_OBSTRUCTION_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "semidirect_lift_rows": 0,
    "semidirect_relation_rows": 0,
    "row324_source_extension_claim": 0,
    "compact_hall_certification_claim": 0,
    "compact_hall_product_rows": 0,
    "compact_hall_coproduct_rows": 0,
    "partial_action_groupoid_claim": 0,
    "partial_groupoid_arrow_rows": 0,
    "tau_transport_claim": 0,
    "transition_orientation_certification_claim": 0,
    "semidirect_hall_lift_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "compact_hall_source",
    "hall_product_compatibility",
    "hall_coproduct_compatibility",
    "partial_action_groupoid_objects",
    "partial_action_groupoid_arrows",
    "type_i_chamber_source_lifts",
    "orientation_line_transport",
    "determinant_square_compatibility",
    "quotient_orientation_transport",
    "s3_relations",
    "semidirect_conjugation_relations",
    "transition_compatibility",
    "inverse_limit_exactness",
    "row326_separation",
}

REQUIRED_FIREWALL = {
    "abstract_character_extension_only",
    "maass_s3_triviality_only",
    "target_chamber_action",
    "typeII_tau_criterion_only",
    "partial_action_groupoid_criterion_only",
    "compact_Hall_obstruction_ledger_only",
    "scalar_trace",
    "OP_scalar_branch",
    "empty_semidirect_lift_table",
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
            "row324_extension_decision_required",
            "compact_hall_source_required",
            "partial_action_groupoid_required",
            "type_i_chamber_lifts_required",
            "hall_product_required",
            "hall_coproduct_required",
            "orientation_line_transport_required",
            "determinant_square_required",
            "quotient_orientation_transport_required",
            "semidirect_relations_required",
            "transition_compatibility_required",
            "inverse_limit_required",
            "criterion_recorded",
            "semidirect_hall_lifts_constructed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "semidirect_lift_rows.csv",
        (
            "lift_id",
            "s3_generator",
            "source_stratum_id",
            "target_stratum_id",
            "hall_correspondence_id",
            "product_compatibility_row",
            "coproduct_compatibility_row",
            "orientation_transport_row",
            "determinant_square_row",
            "quotient_transport_row",
            "transition_row",
            "lift_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "semidirect_relation_rows.csv",
        (
            "relation_id",
            "relation_kind",
            "left_word",
            "right_word",
            "hall_relation_row",
            "orientation_relation_row",
            "semidirect_defect_rank",
            "relation_supplied",
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
            "lift_status",
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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
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
        "s3_extension_decision_imported",
        "compact_hall_ledger_imported",
        "partial_action_groupoid_imported",
        "tau_transport_imported",
        "transition_orientation_imported",
        "semidirect_hall_lift_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "compact_hall_source_supplied",
        "partial_action_groupoid_defined",
        "tau_transport_constructed",
        "transition_orientation_certified",
        "semidirect_hall_lifts_supplied",
        "orientation_transport_rows_supplied",
        "semidirect_relation_rows_supplied",
        "source_orientation_extension_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(S3_EXTENSION_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(PARTIAL_GROUPOID_FIXTURE),
            str(TAU_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    extension_manifest = read_json(S3_EXTENSION_FIXTURE / "manifest.json")
    require_equal(extension_manifest.get("status"), S3_EXTENSION_STATUS, "row324 status")
    require_equal(
        extension_manifest.get("source_orientation_extension_claimed"),
        False,
        "row324 source extension",
    )

    hall_manifest = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(
        hall_manifest.get("obstruction_ledger_status"),
        COMPACT_HALL_STATUS,
        "compact Hall status",
    )
    require_equal(hall_manifest.get("certified"), False, "compact Hall certified")
    require_equal(hall_manifest.get("empty_blocked"), True, "compact Hall empty blocked")

    groupoid_manifest = read_json(PARTIAL_GROUPOID_FIXTURE / "manifest.json")
    require_equal(groupoid_manifest.get("status"), PARTIAL_GROUPOID_STATUS, "groupoid status")
    require_equal(
        groupoid_manifest.get("partial_action_groupoid_defined"),
        False,
        "partial groupoid defined",
    )

    tau_manifest = read_json(TAU_FIXTURE / "manifest.json")
    require_equal(tau_manifest.get("status"), TAU_STATUS, "tau status")
    require_equal(tau_manifest.get("tau_transport_constructed"), False, "tau constructed")

    transition_manifest = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        transition_manifest.get("status"),
        TRANSITION_ORIENTATION_STATUS,
        "transition orientation status",
    )
    require_equal(
        transition_manifest.get("orientation_transition_certification"),
        False,
        "transition orientation certification",
    )

    return {
        "row324_source_extension_claim": int(
            bool(extension_manifest.get("source_orientation_extension_claimed"))
        ),
        "compact_hall_certification_claim": int(bool(hall_manifest.get("certified"))),
        "compact_hall_product_rows": count_data_rows(COMPACT_HALL_FIXTURE / "M_entries.csv"),
        "compact_hall_coproduct_rows": count_data_rows(COMPACT_HALL_FIXTURE / "D_entries.csv"),
        "partial_action_groupoid_claim": int(
            bool(groupoid_manifest.get("partial_action_groupoid_defined"))
        ),
        "partial_groupoid_arrow_rows": count_data_rows(
            PARTIAL_GROUPOID_FIXTURE / "groupoid_arrow_rows.csv"
        ),
        "tau_transport_claim": int(bool(tau_manifest.get("tau_transport_constructed"))),
        "transition_orientation_certification_claim": int(
            bool(transition_manifest.get("orientation_transition_certification"))
        ),
    }


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "s3_extension_decision",
            "compact_hall_source",
            "partial_action_groupoid",
            "tau_transport",
            "transition_orientation",
            "optimization_row",
        },
        "source ids",
    )
    require_equal(indexed["s3_extension_decision"]["source_status"], S3_EXTENSION_STATUS, "row324 source")
    require_equal(indexed["compact_hall_source"]["source_status"], COMPACT_HALL_STATUS, "Hall source")
    require_equal(indexed["partial_action_groupoid"]["source_status"], PARTIAL_GROUPOID_STATUS, "groupoid source")
    require_equal(indexed["tau_transport"]["source_status"], TAU_STATUS, "tau source")
    require_equal(indexed["transition_orientation"]["source_status"], TRANSITION_ORIENTATION_STATUS, "transition source")
    require_equal(indexed["optimization_row"]["source_status"], "row_325", "optimization row")
    for row in rows:
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "semidirect_hall_lift_construction", "criterion_id")
    for key in (
        "row324_extension_decision_required",
        "compact_hall_source_required",
        "partial_action_groupoid_required",
        "type_i_chamber_lifts_required",
        "hall_product_required",
        "hall_coproduct_required",
        "orientation_line_transport_required",
        "determinant_square_required",
        "quotient_orientation_transport_required",
        "semidirect_relations_required",
        "transition_compatibility_required",
        "inverse_limit_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "semidirect_hall_lifts_constructed"), False, "lift constructed")
    check_verified(row, "criterion_rows.csv")


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    require_equal(len(tables["semidirect_lift_rows.csv"]), 0, "semidirect lift rows")
    require_equal(len(tables["semidirect_relation_rows.csv"]), 0, "semidirect relation rows")


def verify_coverage(
    rows: list[dict[str, str]],
    manifest: dict,
    import_counts: dict[str, int],
    tables: dict[str, list[dict[str, str]]],
) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    dynamic = dict(EXPECTED_COVERAGE)
    dynamic.update(import_counts)
    dynamic["criterion_count"] = len(tables["criterion_rows.csv"])
    dynamic["semidirect_lift_rows"] = len(tables["semidirect_lift_rows.csv"])
    dynamic["semidirect_relation_rows"] = len(tables["semidirect_relation_rows.csv"])
    dynamic["semidirect_hall_lift_claim"] = int(
        bool(manifest.get("semidirect_hall_lifts_supplied"))
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
        require_equal(row["lift_status"], "missing_open_obligation", "lift status")
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
    verify_empty_tables(tables)
    verify_coverage(tables["coverage_rows.csv"], manifest, import_counts, tables)
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
