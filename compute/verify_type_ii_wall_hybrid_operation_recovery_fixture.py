#!/usr/bin/env python3
"""Verify hybrid operation-profile recovery of the three type-II walls."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "TYPE_II_WALL_HYBRID_OPERATION_RECOVERY_VERIFIED"
EXPECTED_SCHEMA = "type_ii_wall_hybrid_operation_recovery.v1"
EXPECTED_KIND = "type_ii_wall_hybrid_operation_profile_recovery"
DEFAULT_FIXTURE = Path("certificates/hybrid/type_ii_wall_hybrid_operation_recovery")
PROOF_LABEL = "prop:type-ii-walls-hybrid-operation-recovery"
IMPORT_STATUSES = {
    "certificates/lattice/type_ii_wall_images": "TYPE_II_WALL_IMAGES_VERIFIED",
    "certificates/hybrid/geometric_borcherds_degree_separation": "GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED",
    "certificates/hybrid/positive_elliptic_degree_projection": "POSITIVE_ELLIPTIC_DEGREE_PROJECTION_VERIFIED",
    "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition": "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED",
    "certificates/hybrid/mixed_local_wrapped_correspondence_definition": "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
    "certificates/hybrid/two_sided_mixed_correspondence_definition": "TWO_SIDED_MIXED_CORRESPONDENCE_DEFINITION_VERIFIED",
    "certificates/hybrid/middle_type_ii_wall_wrapped_mixed": "MIDDLE_TYPE_II_WALL_WRAPPED_MIXED_ROUTING_VERIFIED",
}
EXPECTED_WALLS = {
    "profile_delta1": ("delta_1", "delta1_image", (1, 1, 0), 1),
    "profile_delta2": ("delta_2", "delta2_image", (0, 1, 1), 2),
    "profile_delta3": ("delta_3", "delta3_image", (0, -1, 0), 1),
}
EXPECTED_OPERATION_PROFILES = {
    "LW": ("Ran_loc_R_pre_E_times_Ran_wr_R_pre_E", "mixed_LW_R_correspondence"),
    "WL": ("Ran_wr_R_pre_E_times_Ran_loc_R_pre_E", "mixed_WL_R_correspondence"),
    "LWL": (
        "Ran_loc_R_pre_E_times_Ran_wr_R_pre_E_times_Ran_loc_R_pre_E",
        "two_sided_mixed_R_correspondence",
    ),
}
REQUIRED_COVERAGE = {
    "three_wall_coverage": 3,
    "distinct_wall_images": 3,
    "positive_wrapped_profiles": 3,
    "mixed_operation_profiles": 9,
    "local_only_profiles": 0,
    "quotient_losslessness_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "retained_branch_comparison_rows",
    "retained_wall_object_rows",
    "effective_support_realization",
    "anchor_population",
    "mixed_extension_stack_rows",
    "o2_wall_atlas_rows",
    "e_quotient_losslessness",
    "quotient_descent",
    "protected_integration",
    "hybrid_carrier_population",
    "transition_compatibility",
}
REQUIRED_FIREWALL_ROWS = {
    "target_wall_labels_only",
    "borcherds_s_degree_only",
    "compact_mukai_representatives",
    "local_LL_operation",
    "quotient_first_product",
    "o2_wall_objects",
    "e_quotient_losslessness",
    "scalar_trace",
    "pfaffian_sign",
    "protected_integration",
    "populated_hybrid_carrier",
    "compact_hall_source_basis",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "wall_profile_rows.csv",
        (
            "profile_id",
            "delta_id",
            "wall_image_row_id",
            "n",
            "l",
            "m",
            "elliptic_degree_formula",
            "elliptic_degree_value",
            "positive_degree",
            "wall_profile",
            "carrier_symbol",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "operation_profile_rows.csv",
        (
            "operation_id",
            "profile_id",
            "delta_id",
            "operation_profile",
            "source_carrier",
            "target_carrier",
            "correspondence_definition",
            "quotient_timing",
            "recovery_role",
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
            "recovery_status",
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


Triple = tuple[int, int, int]


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
        "fixture_name": "type_ii_wall_hybrid_operation_recovery",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "coefficient_ring": "ZZ",
        "operation_profile_recovery_certified": True,
        "three_wall_coverage_certified": True,
        "wall_image_imported": True,
        "wall_branch_degree_checked": True,
        "wrapped_profile_recovery_checked": True,
        "mixed_profiles_checked": True,
        "middle_wall_routing_imported": True,
        "retained_branch_comparison_rows": False,
        "retained_wall_object_certification": False,
        "effective_support_realization": False,
        "anchor_population": False,
        "mixed_extension_stack_population": False,
        "o2_wall_atlas": False,
        "e_quotient_losslessness": False,
        "quotient_descent": False,
        "protected_integration": False,
        "hybrid_carrier_population": False,
    }
    for key, value in expected.items():
        require_equal(manifest.get(key), value, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")
    require_equal(set(manifest.get("imports", [])), set(IMPORT_STATUSES), "manifest imports")
    if not isinstance(manifest.get("limitations"), list) or not manifest["limitations"]:
        raise ValueError("manifest limitations must be a nonempty list")


def verify_imports() -> dict[str, Triple]:
    for directory, expected_status in IMPORT_STATUSES.items():
        manifest = read_json(Path(directory) / "manifest.json")
        require_equal(manifest.get("status"), expected_status, f"{directory} status")
    carrier = read_json(Path("certificates/hybrid/k3e_hybrid_carrier/manifest.json"))
    require_equal(carrier.get("hybrid_kind"), "mock_empty_blocked", "aggregate hybrid carrier remains blocked")
    wall_path = Path("certificates/lattice/type_ii_wall_images/wall_image_rows.csv")
    with wall_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    imported: dict[str, Triple] = {}
    for row in rows:
        imported[row["wall_id"]] = (int(row["n"]), int(row["l"]), int(row["m"]))
    return imported


def verify_wall_profiles(rows: list[dict[str, str]], imported: dict[str, Triple]) -> dict[str, tuple[str, Triple, int]]:
    profiles: dict[str, tuple[str, Triple, int]] = {}
    by_id = {row["profile_id"]: row for row in rows}
    require_equal(set(by_id), set(EXPECTED_WALLS), "wall profile coverage")
    for profile_id, (delta_id, wall_row_id, triple, degree) in EXPECTED_WALLS.items():
        row = by_id[profile_id]
        check_verified(row, "wall_profile_rows.csv")
        require_equal(row["delta_id"], delta_id, f"{profile_id} delta")
        require_equal(row["wall_image_row_id"], wall_row_id, f"{profile_id} wall image row")
        computed_triple = (int_cell(row, "n"), int_cell(row, "l"), int_cell(row, "m"))
        require_equal(computed_triple, triple, f"{profile_id} triple")
        require_equal(imported.get(wall_row_id), triple, f"{profile_id} imported wall image")
        require_equal(row["elliptic_degree_formula"], "d_equals_m_plus_1", f"{profile_id} degree formula")
        require_equal(int_cell(row, "elliptic_degree_value"), computed_triple[2] + 1, f"{profile_id} d=m+1")
        require_equal(int_cell(row, "elliptic_degree_value"), degree, f"{profile_id} degree")
        require_equal(bool_cell(row, "positive_degree"), True, f"{profile_id} positive")
        require_equal(row["wall_profile"], "singleton_wrapped_colour", f"{profile_id} profile")
        require_equal(row["carrier_symbol"], "Ran_wr_R_pre_E", f"{profile_id} carrier")
        profiles[profile_id] = (delta_id, computed_triple, degree)
    return profiles


def verify_operation_profiles(
    rows: list[dict[str, str]], profiles: dict[str, tuple[str, Triple, int]]
) -> None:
    expected_ids = {
        f"op_{delta.replace('_', '')}_{operation}"
        for _, (delta, _, _) in profiles.items()
        for operation in EXPECTED_OPERATION_PROFILES
    }
    actual_ids = {row["operation_id"] for row in rows}
    require_equal(actual_ids, expected_ids, "operation profile coverage")
    for row in rows:
        check_verified(row, "operation_profile_rows.csv")
        profile_id = row["profile_id"]
        if profile_id not in profiles:
            raise ValueError(f"operation row has unknown profile_id: {row}")
        delta_id, _, _ = profiles[profile_id]
        require_equal(row["delta_id"], delta_id, f"{row['operation_id']} delta")
        operation = row["operation_profile"]
        if operation not in EXPECTED_OPERATION_PROFILES:
            raise ValueError(f"unexpected operation profile: {operation}")
        source, definition = EXPECTED_OPERATION_PROFILES[operation]
        require_equal(row["source_carrier"], source, f"{row['operation_id']} source")
        require_equal(row["target_carrier"], "Ran_wr_R_pre_E", f"{row['operation_id']} target")
        require_equal(row["correspondence_definition"], definition, f"{row['operation_id']} definition")
        require_equal(row["quotient_timing"], "before_E_quotient", f"{row['operation_id']} quotient")
        if operation == "LWL":
            require_equal(
                row["recovery_role"],
                "two_sided_local_action_on_wrapped_wall",
                f"{row['operation_id']} role",
            )
        else:
            require_equal(
                row["recovery_role"],
                "local_action_on_wrapped_wall",
                f"{row['operation_id']} role",
            )


def verify_coverage(rows: list[dict[str, str]]) -> None:
    seen = {row["coverage_id"] for row in rows}
    require_equal(seen, set(REQUIRED_COVERAGE), "coverage row ids")
    for row in rows:
        if row["coverage_id"] not in REQUIRED_COVERAGE:
            raise ValueError(f"unexpected coverage row: {row}")
        check_verified(row, "coverage_rows.csv")
        expected = REQUIRED_COVERAGE[row["coverage_id"]]
        require_equal(int_cell(row, "computed_value"), expected, f"{row['coverage_id']} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{row['coverage_id']} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['coverage_id']} defect")


def verify_obligations(rows: list[dict[str, str]]) -> None:
    seen = {row["obligation_id"] for row in rows}
    require_equal(seen, REQUIRED_OBLIGATIONS, "blocked obligation coverage")
    for row in rows:
        if row["recovery_status"] != "missing_open_obligation":
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
        imported = verify_imports()
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        profiles = verify_wall_profiles(tables["wall_profile_rows.csv"], imported)
        verify_operation_profiles(tables["operation_profile_rows.csv"], profiles)
        verify_coverage(tables["coverage_rows.csv"])
        verify_obligations(tables["blocked_obligations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TYPE_II_WALL_HYBRID_OPERATION_RECOVERY_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
