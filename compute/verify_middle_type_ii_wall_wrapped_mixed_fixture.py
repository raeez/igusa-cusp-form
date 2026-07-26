#!/usr/bin/env python3
"""Verify wrapped/mixed routing for the middle type-II wall."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "MIDDLE_TYPE_II_WALL_WRAPPED_MIXED_ROUTING_VERIFIED"
EXPECTED_SCHEMA = "middle_type_ii_wall_wrapped_mixed.v1"
EXPECTED_KIND = "middle_type_ii_wall_wrapped_mixed_routing"
DEFAULT_FIXTURE = Path("certificates/hybrid/middle_type_ii_wall_wrapped_mixed")
PROOF_LABEL = "prop:middle-type-ii-wall-wrapped-mixed"
IMPORT_STATUSES = {
    "certificates/lattice/type_ii_wall_images": "TYPE_II_WALL_IMAGES_VERIFIED",
    "certificates/hybrid/geometric_elliptic_degree_map": "GEOMETRIC_ELLIPTIC_DEGREE_MAP_OBSTRUCTION_VERIFIED",
    "certificates/hybrid/geometric_borcherds_degree_separation": "GEOMETRIC_BORCHERDS_DEGREE_SEPARATION_OBSTRUCTION_VERIFIED",
    "certificates/hybrid/positive_elliptic_degree_projection": "POSITIVE_ELLIPTIC_DEGREE_PROJECTION_VERIFIED",
    "certificates/hybrid/wrapped_stratum_bpositive_prestack_definition": "WRAPPED_STRATUM_BPOSITIVE_PRESTACK_DEFINITION_VERIFIED",
    "certificates/hybrid/equivariant_wrapped_prequotient_definition": "E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_VERIFIED",
    "certificates/hybrid/mixed_local_wrapped_correspondence_definition": "MIXED_LOCAL_WRAPPED_CORRESPONDENCE_DEFINITION_VERIFIED",
    "certificates/hybrid/two_sided_mixed_correspondence_definition": "TWO_SIDED_MIXED_CORRESPONDENCE_DEFINITION_VERIFIED",
}
REQUIRED_OBLIGATIONS = {
    "retained_branch_comparison_rows",
    "retained_wall_object_row",
    "effective_support_realization",
    "anchor_population",
    "mixed_extension_stack_rows",
    "o2_wall_atlas_rows",
    "quotient_descent",
    "protected_integration",
    "hybrid_carrier_population",
    "transition_compatibility",
}
REQUIRED_FIREWALL_ROWS = {
    "borcherds_s_degree_only",
    "type_ii_target_label_only",
    "compact_mukai_representative_only",
    "local_ran_point",
    "compact_hall_source_basis",
    "o2_wall_object",
    "quotient_first_product",
    "scalar_trace",
    "pfaffian_sign",
    "protected_integration",
    "populated_hybrid_carrier",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "wall_degree_rows.csv",
        (
            "wall_id",
            "delta_id",
            "n",
            "l",
            "m",
            "elliptic_degree_formula",
            "elliptic_degree_value",
            "positive_degree",
            "wall_image_row_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "wrapped_routing_rows.csv",
        (
            "routing_id",
            "wall_id",
            "degree_value",
            "local_condition",
            "wrapped_condition",
            "local_membership",
            "wrapped_membership",
            "carrier_symbol",
            "prequotient_symbol",
            "projection_conclusion",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "mixed_operation_rows.csv",
        (
            "operation_id",
            "wall_id",
            "operation_profile",
            "source_carrier",
            "target_carrier",
            "correspondence_definition",
            "quotient_timing",
            "mixed_required",
            "proof_reference",
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
            "routing_status",
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
        "fixture_name": "middle_type_ii_wall_wrapped_mixed",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "coefficient_ring": "ZZ",
        "routing_certified": True,
        "middle_wall_image_imported": True,
        "type_ii_wall_branch_formula_checked": True,
        "positive_elliptic_degree_checked": True,
        "wrapped_stratum_definition_imported": True,
        "mixed_correspondence_definition_imported": True,
        "two_sided_mixed_definition_imported": True,
        "wrapped_prequotient_definition_imported": True,
        "retained_branch_comparison_rows": False,
        "retained_wall_object_certification": False,
        "effective_support_realization": False,
        "anchor_population": False,
        "o2_wall_atlas": False,
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


def verify_imports() -> None:
    for directory, expected_status in IMPORT_STATUSES.items():
        manifest = read_json(Path(directory) / "manifest.json")
        require_equal(manifest.get("status"), expected_status, f"{directory} status")
    separation = read_json(Path("certificates/hybrid/geometric_borcherds_degree_separation/manifest.json"))
    require_equal(separation.get("equality_certification"), False, "degree equality remains uncertified")
    carrier = read_json(Path("certificates/hybrid/k3e_hybrid_carrier/manifest.json"))
    require_equal(carrier.get("hybrid_kind"), "mock_empty_blocked", "aggregate hybrid carrier remains blocked")


def imported_wall_image() -> tuple[int, int, int]:
    path = Path("certificates/lattice/type_ii_wall_images/wall_image_rows.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if row.get("wall_id") == "delta2_image":
            return (int(row["n"]), int(row["l"]), int(row["m"]))
    raise ValueError("missing imported delta2_image row")


def verify_wall_degree(rows: list[dict[str, str]]) -> dict[str, int]:
    if len(rows) != 1:
        raise ValueError("wall_degree_rows.csv must contain exactly one row")
    row = rows[0]
    check_verified(row, "wall_degree_rows.csv")
    require_equal(row["wall_id"], "middle_type_ii_wall", "wall_id")
    require_equal(row["delta_id"], "delta_2", "delta_id")
    triple = (int_cell(row, "n"), int_cell(row, "l"), int_cell(row, "m"))
    require_equal(triple, (0, 1, 1), "middle wall triple")
    require_equal(triple, imported_wall_image(), "imported delta2 wall image")
    require_equal(row["elliptic_degree_formula"], "d_equals_m_plus_1", "degree formula")
    d_value = int_cell(row, "elliptic_degree_value")
    require_equal(d_value, triple[2] + 1, "d=m+1")
    require_equal(d_value, 2, "middle wall elliptic degree")
    require_equal(bool_cell(row, "positive_degree"), True, "positive degree")
    require_equal(row["wall_image_row_id"], "delta2_image", "wall image row")
    return {"degree": d_value}


def verify_wrapped_routing(rows: list[dict[str, str]], degree: int) -> None:
    if len(rows) != 1:
        raise ValueError("wrapped_routing_rows.csv must contain exactly one row")
    row = rows[0]
    check_verified(row, "wrapped_routing_rows.csv")
    require_equal(row["routing_id"], "middle_wall_wrapped_route", "routing_id")
    require_equal(row["wall_id"], "middle_type_ii_wall", "routing wall_id")
    require_equal(int_cell(row, "degree_value"), degree, "routing degree")
    require_equal(row["local_condition"], "b_R_geom_equals_0", "local condition")
    require_equal(row["wrapped_condition"], "b_R_geom_positive", "wrapped condition")
    require_equal(bool_cell(row, "local_membership"), False, "local membership")
    require_equal(bool_cell(row, "wrapped_membership"), degree > 0, "wrapped membership")
    require_equal(row["carrier_symbol"], "Ran_wr_R_pre_E", "wrapped carrier")
    require_equal(row["prequotient_symbol"], "M_eta_R_wr_rig", "wrapped prequotient")
    require_equal(
        row["projection_conclusion"],
        "p_E_support_equals_E_if_effective_support_row_supplied",
        "projection conclusion",
    )


def verify_mixed_operations(rows: list[dict[str, str]]) -> None:
    expected = {
        "middle_wall_LW": (
            "local_then_middle_wrapped",
            "Ran_loc_R_pre_E_times_Ran_wr_R_pre_E",
            "Ran_wr_R_pre_E",
            "mixed_LW_R_correspondence",
        ),
        "middle_wall_WL": (
            "middle_wrapped_then_local",
            "Ran_wr_R_pre_E_times_Ran_loc_R_pre_E",
            "Ran_wr_R_pre_E",
            "mixed_WL_R_correspondence",
        ),
        "middle_wall_LWL": (
            "local_middle_wrapped_local",
            "Ran_loc_R_pre_E_times_Ran_wr_R_pre_E_times_Ran_loc_R_pre_E",
            "Ran_wr_R_pre_E",
            "two_sided_mixed_R_correspondence",
        ),
    }
    by_id = {row["operation_id"]: row for row in rows}
    require_equal(set(by_id), set(expected), "mixed operation coverage")
    for operation_id, (profile, source, target, definition) in expected.items():
        row = by_id[operation_id]
        check_verified(row, "mixed_operation_rows.csv")
        require_equal(row["wall_id"], "middle_type_ii_wall", f"{operation_id} wall")
        require_equal(row["operation_profile"], profile, f"{operation_id} profile")
        require_equal(row["source_carrier"], source, f"{operation_id} source")
        require_equal(row["target_carrier"], target, f"{operation_id} target")
        require_equal(row["correspondence_definition"], definition, f"{operation_id} definition")
        require_equal(row["quotient_timing"], "before_E_quotient", f"{operation_id} quotient")
        require_equal(bool_cell(row, "mixed_required"), True, f"{operation_id} mixed_required")


def verify_obligations(rows: list[dict[str, str]]) -> None:
    seen = {row["obligation_id"] for row in rows}
    require_equal(seen, REQUIRED_OBLIGATIONS, "blocked obligation coverage")
    for row in rows:
        if row["routing_status"] != "missing_open_obligation":
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
        wall_data = verify_wall_degree(tables["wall_degree_rows.csv"])
        verify_wrapped_routing(tables["wrapped_routing_rows.csv"], wall_data["degree"])
        verify_mixed_operations(tables["mixed_operation_rows.csv"])
        verify_obligations(tables["blocked_obligations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"MIDDLE_TYPE_II_WALL_WRAPPED_MIXED_ROUTING_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
