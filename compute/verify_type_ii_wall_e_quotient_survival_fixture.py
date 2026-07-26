#!/usr/bin/env python3
"""Verify type-II wall profile survival under quotient-after-correspondence."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "TYPE_II_WALL_E_QUOTIENT_SURVIVAL_VERIFIED"
EXPECTED_SCHEMA = "type_ii_wall_e_quotient_survival.v1"
EXPECTED_KIND = "type_ii_wall_e_quotient_profile_survival"
DEFAULT_FIXTURE = Path("certificates/hybrid/type_ii_wall_e_quotient_survival")
PROOF_LABEL = "prop:type-ii-walls-survive-e-quotient"
IMPORT_STATUSES = {
    "certificates/hybrid/type_ii_wall_hybrid_operation_recovery": "TYPE_II_WALL_HYBRID_OPERATION_RECOVERY_VERIFIED",
    "certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition": "QUOTIENT_AFTER_CORRESPONDENCE_PSEUDOFUNCTOR_DEFINED",
    "certificates/hybrid/quotient_after_correspondence_quotient_first_exclusion": "QUOTIENT_AFTER_CORRESPONDENCE_QUOTIENT_FIRST_EXCLUSION_VERIFIED",
    "certificates/hybrid/quotient_after_correspondence_hn_transition_compatibility": "QUOTIENT_AFTER_CORRESPONDENCE_HN_TRANSITION_COMPATIBILITY_VERIFIED",
}
EXPECTED_WALLS = {
    "survive_delta1": ("profile_delta1", "delta_1", "delta1_image"),
    "survive_delta2": ("profile_delta2", "delta_2", "delta2_image"),
    "survive_delta3": ("profile_delta3", "delta_3", "delta3_image"),
}
EXPECTED_OPERATIONS = {
    f"survive_op_delta{i}_{op}": (f"op_delta{i}_{op}", f"profile_delta{i}", f"delta_{i}", op)
    for i in (1, 2, 3)
    for op in ("LW", "WL", "LWL")
}
REQUIRED_COVERAGE = {
    "three_wall_profile_survival": 3,
    "nine_operation_profile_survival": 9,
    "quotient_after_not_first": 9,
    "profile_survival_defects": 0,
    "object_nonzero_claim": 0,
    "o2_atlas_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "retained_wall_object_rows",
    "object_level_nonzero_survival",
    "coefficient_descent_nonzero",
    "orientation_descent",
    "o2_wall_atlas_rows",
    "protected_integration",
    "aggregate_hybrid_population",
    "transition_to_o2",
}
REQUIRED_FIREWALL_ROWS = {
    "quotient_first",
    "object_quotient_only",
    "target_wall_labels_only",
    "object_nonzero_survival",
    "coefficient_descent_nonzero",
    "o2_wall_atlas",
    "pfaffian_sign",
    "protected_integration",
    "scalar_trace",
    "populated_hybrid_carrier",
    "compact_hall_source_basis",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "wall_survival_rows.csv",
        (
            "survival_id",
            "profile_id",
            "delta_id",
            "wall_image_row_id",
            "unreduced_carrier",
            "quotient_carrier",
            "quotient_map_id",
            "e_action_preserves_profile",
            "quotient_after_correspondence",
            "survival_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "operation_survival_rows.csv",
        (
            "survival_id",
            "operation_id",
            "profile_id",
            "delta_id",
            "operation_profile",
            "unreduced_correspondence",
            "reduced_correspondence",
            "quotient_after_not_first",
            "wall_profile_preserved",
            "survival_defect_rank",
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
            "survival_status",
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
            "source_reference",
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


def read_json(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"missing JSON file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root is not an object: {path}")
    return value


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    path = fixture / spec.path
    if not path.is_file():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != spec.columns:
            raise ValueError(f"{spec.path}: expected columns {spec.columns}, got {actual}")
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one data row")
    return rows


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


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def check_verified(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if table_name not in {"blocked_obligations.csv"} and PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "type_ii_wall_e_quotient_survival",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "coefficient_ring": "ZZ",
        "profile_survival_certified": True,
        "three_wall_survival_certified": True,
        "operation_profile_survival_certified": True,
        "quotient_after_correspondence_imported": True,
        "quotient_first_excluded": True,
        "hn_transition_compatibility_imported": True,
        "type_ii_operation_recovery_imported": True,
        "object_level_nonzero_survival": False,
        "coefficient_descent_nonzero": False,
        "orientation_descent": False,
        "o2_wall_atlas": False,
        "protected_integration": False,
        "aggregate_hybrid_population": False,
    }
    for key, value in expected.items():
        require_equal(manifest.get(key), value, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")
    require_equal(set(manifest.get("imports", [])), set(IMPORT_STATUSES), "manifest imports")
    if not isinstance(manifest.get("limitations"), list) or not manifest["limitations"]:
        raise ValueError("manifest limitations must be a nonempty list")


def verify_imports() -> None:
    for directory, expected_status in IMPORT_STATUSES.items():
        manifest = read_json(Path(directory) / "manifest.json")
        require_equal(manifest.get("status"), expected_status, f"{directory} status")
    q_manifest = read_json(Path("certificates/hybrid/quotient_after_correspondence_pseudofunctor_definition/manifest.json"))
    require_equal(q_manifest.get("object_assignment_defined"), True, "quotient object assignment")
    require_equal(q_manifest.get("arrow_assignment_defined"), True, "quotient arrow assignment")
    require_equal(q_manifest.get("quotient_first"), False, "quotient first excluded")
    carrier = read_json(Path("certificates/hybrid/k3e_hybrid_carrier/manifest.json"))
    require_equal(carrier.get("hybrid_kind"), "mock_empty_blocked", "aggregate hybrid carrier remains blocked")


def verify_wall_survival(rows: list[dict[str, str]]) -> None:
    by_id = {row["survival_id"]: row for row in rows}
    require_equal(set(by_id), set(EXPECTED_WALLS), "wall survival coverage")
    for survival_id, (profile_id, delta_id, wall_image_row_id) in EXPECTED_WALLS.items():
        row = by_id[survival_id]
        check_verified(row, "wall_survival_rows.csv")
        require_equal(row["profile_id"], profile_id, f"{survival_id} profile")
        require_equal(row["delta_id"], delta_id, f"{survival_id} delta")
        require_equal(row["wall_image_row_id"], wall_image_row_id, f"{survival_id} wall image")
        require_equal(row["unreduced_carrier"], f"M_eta_{delta_id.replace('_', '')}_R_wr_rig", f"{survival_id} unreduced")
        require_equal(row["quotient_carrier"], f"M_eta_{delta_id.replace('_', '')}_R_wr_rig_slash_E", f"{survival_id} quotient")
        require_equal(bool_cell(row, "e_action_preserves_profile"), True, f"{survival_id} E action")
        require_equal(bool_cell(row, "quotient_after_correspondence"), True, f"{survival_id} quotient after")
        require_equal(int_cell(row, "survival_defect_rank"), 0, f"{survival_id} defect")


def verify_operation_survival(rows: list[dict[str, str]]) -> None:
    by_id = {row["survival_id"]: row for row in rows}
    require_equal(set(by_id), set(EXPECTED_OPERATIONS), "operation survival coverage")
    for survival_id, (operation_id, profile_id, delta_id, operation_profile) in EXPECTED_OPERATIONS.items():
        row = by_id[survival_id]
        check_verified(row, "operation_survival_rows.csv")
        require_equal(row["operation_id"], operation_id, f"{survival_id} operation_id")
        require_equal(row["profile_id"], profile_id, f"{survival_id} profile")
        require_equal(row["delta_id"], delta_id, f"{survival_id} delta")
        require_equal(row["operation_profile"], operation_profile, f"{survival_id} operation profile")
        suffix = f"{operation_profile}_delta{delta_id[-1]}"
        require_equal(row["unreduced_correspondence"], f"E_{suffix}", f"{survival_id} unreduced")
        require_equal(row["reduced_correspondence"], f"E_{suffix}_slash_E", f"{survival_id} reduced")
        require_equal(bool_cell(row, "quotient_after_not_first"), True, f"{survival_id} quotient after")
        require_equal(bool_cell(row, "wall_profile_preserved"), True, f"{survival_id} profile preserved")
        require_equal(int_cell(row, "survival_defect_rank"), 0, f"{survival_id} defect")


def verify_coverage(rows: list[dict[str, str]]) -> None:
    seen = {row["coverage_id"] for row in rows}
    require_equal(seen, set(REQUIRED_COVERAGE), "coverage rows")
    for row in rows:
        check_verified(row, "coverage_rows.csv")
        expected = REQUIRED_COVERAGE[row["coverage_id"]]
        require_equal(int_cell(row, "computed_value"), expected, f"{row['coverage_id']} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{row['coverage_id']} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['coverage_id']} defect")


def verify_obligations(rows: list[dict[str, str]]) -> None:
    seen = {row["obligation_id"] for row in rows}
    require_equal(seen, REQUIRED_OBLIGATIONS, "blocked obligation coverage")
    for row in rows:
        if row["survival_status"] != "missing_open_obligation":
            raise ValueError(f"blocked obligation is not missing: {row}")
        if row["check_status"] != "verified":
            raise ValueError(f"blocked obligation is not verified: {row}")
        if not row["mathematical_payload"]:
            raise ValueError(f"blocked obligation lacks mathematical payload: {row}")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen = {row["forbidden_substitute"] for row in rows}
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "scalar firewall coverage")
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        if not (args.fixture / "README.md").is_file():
            raise ValueError(f"missing README: {args.fixture / 'README.md'}")
        verify_manifest(args.fixture)
        verify_imports()
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        verify_wall_survival(tables["wall_survival_rows.csv"])
        verify_operation_survival(tables["operation_survival_rows.csv"])
        verify_coverage(tables["coverage_rows.csv"])
        verify_obligations(tables["blocked_obligations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TYPE_II_WALL_E_QUOTIENT_SURVIVAL_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
