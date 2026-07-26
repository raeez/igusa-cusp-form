#!/usr/bin/env python3
"""Verify exclusion of false type-I wall profiles from the hybrid wall inlet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "TYPE_I_FALSE_WALL_EXCLUSION_VERIFIED"
EXPECTED_SCHEMA = "type_i_false_wall_exclusion.v1"
EXPECTED_KIND = "type_i_false_wall_profile_exclusion"
DEFAULT_FIXTURE = Path("certificates/hybrid/type_i_false_wall_exclusion")
PROOF_LABEL = "prop:no-type-i-wall-enters-hybrid-carrier"
TYPE_II_CHAMBER_FIXTURE = Path("certificates/lattice/type_ii_chamber_isotropic")
TYPE_II_RECOVERY_FIXTURE = Path("certificates/hybrid/type_ii_wall_hybrid_operation_recovery")
E_QUOTIENT_SURVIVAL_FIXTURE = Path("certificates/hybrid/type_ii_wall_e_quotient_survival")
EXPECTED_TYPE_II = {
    "profile_delta1": ("delta_1", "delta1_image", 1),
    "profile_delta2": ("delta_2", "delta2_image", 2),
    "profile_delta3": ("delta_3", "delta3_image", 1),
}
EXPECTED_TYPE_I = {
    "exclude_eta12": ("eta_12", "sigma_12"),
    "exclude_eta13": ("eta_13", "sigma_13"),
    "exclude_eta23": ("eta_23", "sigma_23"),
}
REQUIRED_COVERAGE = {
    "admitted_type_ii_wall_profiles": 3,
    "excluded_type_i_chamber_roots": 3,
    "false_type_i_admitted": 0,
    "quotient_resurrection_defect": 0,
    "divisor_support_defect": 0,
    "type_i_chamber_action_defect": 0,
    "aggregate_carrier_population_claim": 0,
    "o2_wall_atlas_claim": 0,
}
REQUIRED_OBLIGATIONS = {
    "aggregate_hybrid_population",
    "global_colour_exhaustion",
    "retained_wall_object_rows",
    "object_level_nonzero_survival",
    "coefficient_descent_nonzero",
    "o2_wall_atlas",
    "protected_integration",
    "transition_to_o2",
}
REQUIRED_FIREWALL_ROWS = {
    "type_i_divisor_wall",
    "type_i_chamber_symmetry_as_wall",
    "quotient_resurrection",
    "global_hybrid_carrier_exhaustion",
    "o2_wall_atlas",
    "compact_source",
    "pfaffian_sign",
    "protected_integration",
    "scalar_trace",
    "quotient_first",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "admitted_type_ii_wall_rows.csv",
        (
            "profile_id",
            "root_id",
            "root_kind",
            "divisor_support",
            "delta5_order",
            "wall_image_row_id",
            "branch_degree",
            "hybrid_wall_profile_admitted",
            "quotient_profile_survives",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "type_i_exclusion_rows.csv",
        (
            "exclusion_id",
            "root_id",
            "chamber_automorphism_id",
            "ambient_divisibility",
            "divisor_support",
            "delta5_order",
            "chamber_action",
            "permutes_type_ii_profiles",
            "hybrid_wall_profile_admitted",
            "quotient_resurrection",
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
            "exclusion_status",
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

ROOT_DIVISIBILITY_COLUMNS = (
    "root_id",
    "root_kind",
    "f2",
    "f3",
    "fm2",
    "square",
    "ambient_divisibility",
    "primitive_ambient",
    "divisor_support",
    "delta5_order",
    "source_reference",
    "check_status",
    "notes",
)
CHAMBER_AUTOMORPHISM_COLUMNS = (
    "automorphism_id",
    "root_id",
    "root_square",
    "ambient_divisibility",
    "delta1_image",
    "delta2_image",
    "delta3_image",
    "permutation",
    "rho_fixed",
    "source_reference",
    "check_status",
    "notes",
)
RECOVERY_PROFILE_COLUMNS = (
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
)
SURVIVAL_WALL_COLUMNS = (
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


def read_table_path(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            raise ValueError(f"{path}: expected columns {columns}, got {actual}")
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
    if not rows:
        raise ValueError(f"{path}: expected at least one data row")
    return rows


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns)


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


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if proof_required and PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key}={value}")
        indexed[value] = row
    return indexed


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hybrid_kind"), EXPECTED_KIND, "hybrid_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "profile_exclusion_certified",
        "type_i_chamber_roots_excluded",
        "type_ii_wall_profiles_imported",
        "quotient_survival_imported",
        "quotient_resurrection_excluded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "aggregate_hybrid_population",
        "global_colour_exhaustion",
        "retained_wall_object_certification",
        "object_level_nonzero_survival",
        "coefficient_descent_nonzero",
        "orientation_descent",
        "o2_wall_atlas",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    expected_tables = [spec.path for spec in TABLE_SPECS]
    require_equal(manifest.get("tables"), expected_tables, "tables")
    require_equal(
        manifest.get("imports"),
        [
            str(TYPE_II_CHAMBER_FIXTURE),
            str(TYPE_II_RECOVERY_FIXTURE),
            str(E_QUOTIENT_SURVIVAL_FIXTURE),
        ],
        "imports",
    )


def verify_import_manifests() -> None:
    chamber_manifest = read_json(TYPE_II_CHAMBER_FIXTURE / "manifest.json")
    require_equal(chamber_manifest.get("certified"), True, "type-II chamber certified")
    require_equal(
        chamber_manifest.get("chamber_isotropic_certified"),
        True,
        "type-II chamber isotropic certified",
    )
    recovery_manifest = read_json(TYPE_II_RECOVERY_FIXTURE / "manifest.json")
    require_equal(
        recovery_manifest.get("status"),
        "TYPE_II_WALL_HYBRID_OPERATION_RECOVERY_VERIFIED",
        "operation recovery status",
    )
    survival_manifest = read_json(E_QUOTIENT_SURVIVAL_FIXTURE / "manifest.json")
    require_equal(
        survival_manifest.get("status"),
        "TYPE_II_WALL_E_QUOTIENT_SURVIVAL_VERIFIED",
        "E quotient survival status",
    )


def verify_admitted_rows(
    rows: list[dict[str, str]],
    root_rows: dict[str, dict[str, str]],
    recovery_rows: dict[str, dict[str, str]],
    survival_rows: dict[str, dict[str, str]],
) -> None:
    indexed = rows_by(rows, "profile_id", "admitted_type_ii_wall_rows.csv")
    require_equal(set(indexed), set(EXPECTED_TYPE_II), "admitted type-II profile coverage")
    for profile_id, (root_id, wall_image_id, branch_degree) in EXPECTED_TYPE_II.items():
        row = indexed[profile_id]
        check_verified(row, "admitted_type_ii_wall_rows.csv")
        require_equal(row["root_id"], root_id, f"{profile_id} root")
        require_equal(row["root_kind"], "type_II", f"{profile_id} kind")
        require_equal(bool_cell(row, "divisor_support"), True, f"{profile_id} divisor support")
        require_equal(int_cell(row, "delta5_order"), 1, f"{profile_id} Delta5 order")
        require_equal(row["wall_image_row_id"], wall_image_id, f"{profile_id} wall image")
        require_equal(int_cell(row, "branch_degree"), branch_degree, f"{profile_id} branch degree")
        require_equal(bool_cell(row, "hybrid_wall_profile_admitted"), True, f"{profile_id} admitted")
        require_equal(bool_cell(row, "quotient_profile_survives"), True, f"{profile_id} quotient survives")

        root_row = root_rows[root_id]
        require_equal(root_row["root_kind"], "type_II", f"{root_id} imported kind")
        require_equal(bool_cell(root_row, "divisor_support"), True, f"{root_id} imported divisor support")
        require_equal(int_cell(root_row, "delta5_order"), 1, f"{root_id} imported Delta5 order")
        recovery_row = recovery_rows[profile_id]
        require_equal(recovery_row["delta_id"], root_id, f"{profile_id} recovery root")
        require_equal(recovery_row["wall_image_row_id"], wall_image_id, f"{profile_id} recovery wall image")
        require_equal(int_cell(recovery_row, "elliptic_degree_value"), branch_degree, f"{profile_id} recovery degree")
        require_equal(bool_cell(recovery_row, "positive_degree"), True, f"{profile_id} positive degree")
        survival_row = survival_rows[profile_id]
        require_equal(survival_row["delta_id"], root_id, f"{profile_id} survival root")
        require_equal(bool_cell(survival_row, "e_action_preserves_profile"), True, f"{profile_id} E action")
        require_equal(bool_cell(survival_row, "quotient_after_correspondence"), True, f"{profile_id} quotient timing")
        require_equal(int_cell(survival_row, "survival_defect_rank"), 0, f"{profile_id} survival defect")


def verify_type_i_exclusions(
    rows: list[dict[str, str]],
    root_rows: dict[str, dict[str, str]],
    automorphism_rows: dict[str, dict[str, str]],
) -> None:
    indexed = rows_by(rows, "exclusion_id", "type_i_exclusion_rows.csv")
    require_equal(set(indexed), set(EXPECTED_TYPE_I), "type-I exclusion coverage")
    for exclusion_id, (root_id, automorphism_id) in EXPECTED_TYPE_I.items():
        row = indexed[exclusion_id]
        check_verified(row, "type_i_exclusion_rows.csv")
        require_equal(row["root_id"], root_id, f"{exclusion_id} root")
        require_equal(row["chamber_automorphism_id"], automorphism_id, f"{exclusion_id} automorphism")
        require_equal(int_cell(row, "ambient_divisibility"), 1, f"{exclusion_id} divisibility")
        require_equal(bool_cell(row, "divisor_support"), False, f"{exclusion_id} divisor support")
        require_equal(int_cell(row, "delta5_order"), 0, f"{exclusion_id} Delta5 order")
        require_equal(bool_cell(row, "permutes_type_ii_profiles"), True, f"{exclusion_id} permutes")
        require_equal(bool_cell(row, "hybrid_wall_profile_admitted"), False, f"{exclusion_id} admitted")
        require_equal(bool_cell(row, "quotient_resurrection"), False, f"{exclusion_id} quotient resurrection")

        root_row = root_rows[root_id]
        require_equal(root_row["root_kind"], "type_I", f"{root_id} imported kind")
        require_equal(int_cell(root_row, "ambient_divisibility"), 1, f"{root_id} imported divisibility")
        require_equal(bool_cell(root_row, "divisor_support"), False, f"{root_id} imported divisor support")
        require_equal(int_cell(root_row, "delta5_order"), 0, f"{root_id} imported Delta5 order")
        automorphism_row = automorphism_rows[automorphism_id]
        require_equal(automorphism_row["root_id"], root_id, f"{automorphism_id} imported root")
        require_equal(int_cell(automorphism_row, "ambient_divisibility"), 1, f"{automorphism_id} imported divisibility")
        require_equal(bool_cell(automorphism_row, "rho_fixed"), True, f"{automorphism_id} rho fixed")


def verify_coverage(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(REQUIRED_COVERAGE), "coverage row ids")
    for coverage_id, expected in REQUIRED_COVERAGE.items():
        row = indexed[coverage_id]
        check_verified(row, "coverage_rows.csv")
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_blocked(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "obligation_id", "blocked_obligations.csv")
    require_equal(set(indexed), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, row in indexed.items():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        require_equal(row["exclusion_status"], "missing_open_obligation", f"{obligation_id} status")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect")
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "firewall substitutes")


def verify_fixture(fixture: Path) -> None:
    verify_manifest(fixture)
    verify_import_manifests()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    root_rows = rows_by(
        read_table_path(TYPE_II_CHAMBER_FIXTURE / "root_divisibility.csv", ROOT_DIVISIBILITY_COLUMNS),
        "root_id",
        "root_divisibility.csv",
    )
    automorphism_rows = rows_by(
        read_table_path(TYPE_II_CHAMBER_FIXTURE / "chamber_automorphisms.csv", CHAMBER_AUTOMORPHISM_COLUMNS),
        "automorphism_id",
        "chamber_automorphisms.csv",
    )
    recovery_rows = rows_by(
        read_table_path(TYPE_II_RECOVERY_FIXTURE / "wall_profile_rows.csv", RECOVERY_PROFILE_COLUMNS),
        "profile_id",
        "wall_profile_rows.csv",
    )
    survival_rows = rows_by(
        read_table_path(E_QUOTIENT_SURVIVAL_FIXTURE / "wall_survival_rows.csv", SURVIVAL_WALL_COLUMNS),
        "profile_id",
        "wall_survival_rows.csv",
    )

    verify_admitted_rows(
        tables["admitted_type_ii_wall_rows.csv"],
        root_rows,
        recovery_rows,
        survival_rows,
    )
    verify_type_i_exclusions(
        tables["type_i_exclusion_rows.csv"],
        root_rows,
        automorphism_rows,
    )
    verify_coverage(tables["coverage_rows.csv"])
    verify_blocked(tables["blocked_obligations.csv"])
    verify_firewall(tables["scalar_firewall.csv"])


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"TYPE_I_FALSE_WALL_EXCLUSION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
