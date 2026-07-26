#!/usr/bin/env python3
"""Verify row-328 local-divisor-monodromy/Maass irrelevance packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_local_divisor_monodromy_maass_irrelevance.v1"
EXPECTED_KIND = "rhomred_local_divisor_monodromy_maass_irrelevance"
SUCCESS_STATUS = "RHOMRED_LOCAL_DIVISOR_MONODROMY_MAASS_IRRELEVANCE_VERIFIED"
PROOF_LABEL = "prop:local-divisor-monodromy-maass-irrelevance"
DEFAULT_FIXTURE = Path(
    "certificates/orientation/rhomred_local_divisor_monodromy_maass_irrelevance"
)

LOCAL_DEFINITION_FIXTURE = Path(
    "certificates/orientation/rhomred_local_divisor_monodromy_definition"
)
MAASS_COMPARISON_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_maass_comparison")
AUTOMORPHIC_MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")

LOCAL_DEFINITION_STATUS = "RHOMRED_LOCAL_DIVISOR_MONODROMY_DEFINITION_OBSTRUCTION_VERIFIED"
MAASS_COMPARISON_STATUS = "RHOMRED_WEYL_ORIENTATION_MAASS_COMPARISON_OBSTRUCTION_VERIFIED"
AUTOMORPHIC_MAASS_SCHEMA = "delta5_maass_character.v1"

EXPECTED_COVERAGE = {
    "irrelevance_rows": 1,
    "comparison_map_rows": 0,
    "local_monodromy_rows": 0,
    "nu_on_meridian_values": 0,
    "maass_local_dependency_claim": 0,
    "epsilon_extension_claim": 0,
    "row329_simple_wall_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "local_monodromy_operator_rows",
    "meridian_to_automorphic_map",
    "source_epsilon_maass_comparison",
    "row329_simple_wall_orientations",
}

REQUIRED_FIREWALL = {
    "local_meridian_as_maass_argument",
    "local_monodromy_value_as_maass_value",
    "Borcherds_multiplicity",
    "automorphic_Humbert_divisor",
    "epsilon_o_value",
    "OP_scalar_branch",
    "scalar_trace",
    "empty_local_monodromy_table",
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
        "irrelevance_rows.csv",
        (
            "irrelevance_id",
            "maass_domain",
            "local_monodromy_domain",
            "comparison_map_required",
            "comparison_map_supplied",
            "maass_values_depend_on_local_monodromy",
            "irrelevance_recorded",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "comparison_map_rows.csv",
        (
            "map_id",
            "source_domain",
            "target_domain",
            "map_rule",
            "compatible_with_meridians",
            "compatible_with_maass",
            "comparison_map_supplied",
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
            "irrelevance_status",
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


def verify_manifest(fixture: Path) -> dict:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "local_divisor_monodromy_definition_imported",
        "orientation_maass_comparison_imported",
        "automorphic_maass_character_imported",
        "domain_separation_recorded",
        "no_meridian_to_automorphic_map_recorded",
        "irrelevance_theorem_recorded",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "local_divisor_monodromy_rows_supplied",
        "meridian_to_automorphic_comparison_supplied",
        "nu_delta5_depends_on_local_monodromy",
        "nu_delta5_evaluated_on_meridians",
        "epsilon_o_extended_to_local_divisors",
        "row329_simple_wall_orientation_computed",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(LOCAL_DEFINITION_FIXTURE),
            str(MAASS_COMPARISON_FIXTURE),
            str(AUTOMORPHIC_MAASS_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> None:
    local_definition = read_json(LOCAL_DEFINITION_FIXTURE / "manifest.json")
    require_equal(local_definition.get("status"), LOCAL_DEFINITION_STATUS, "local definition status")
    require_equal(
        local_definition.get("local_divisor_monodromy_constructed"),
        False,
        "local monodromy constructed",
    )
    require_equal(
        local_definition.get("epsilon_o_extended_to_local_divisors"),
        False,
        "local definition epsilon extension",
    )

    maass_comparison = read_json(MAASS_COMPARISON_FIXTURE / "manifest.json")
    require_equal(maass_comparison.get("status"), MAASS_COMPARISON_STATUS, "Maass comparison status")
    require_equal(maass_comparison.get("epsilon_equals_maass_proved"), False, "epsilon equals Maass")
    require_equal(maass_comparison.get("maass_as_source_allowed"), False, "Maass as source")

    automorphic = read_json(AUTOMORPHIC_MAASS_FIXTURE / "manifest.json")
    require_equal(automorphic.get("schema_version"), AUTOMORPHIC_MAASS_SCHEMA, "Maass schema")
    require_equal(automorphic.get("automorphic_character_certified"), True, "automorphic certified")
    require_equal(automorphic.get("compact_source"), False, "Maass compact source flag")


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "local_definition",
            "orientation_maass_comparison",
            "automorphic_maass",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_irrelevance(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "irrelevance row count")
    row = rows[0]
    require_equal(row["irrelevance_id"], "local_monodromy_maass_irrelevance", "irrelevance id")
    require_equal(row["maass_domain"], "W2_and_AutPolyII", "Maass domain")
    require_equal(row["local_monodromy_domain"], "compact_Hall_meridian_groupoids", "local domain")
    require_equal(bool_cell(row, "comparison_map_required"), True, "comparison map required")
    require_equal(bool_cell(row, "comparison_map_supplied"), False, "comparison map supplied")
    require_equal(
        bool_cell(row, "maass_values_depend_on_local_monodromy"),
        False,
        "Maass local dependency",
    )
    require_equal(bool_cell(row, "irrelevance_recorded"), True, "irrelevance recorded")
    check_verified(row, "irrelevance_rows.csv")


def verify_comparison_maps(rows: list[dict[str, str]]) -> None:
    require_equal(rows, [], "comparison map rows")


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
        require_equal(row["irrelevance_status"], "missing_open_obligation", "obligation status")
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
    verify_irrelevance(tables["irrelevance_rows.csv"])
    verify_comparison_maps(tables["comparison_map_rows.csv"])
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
