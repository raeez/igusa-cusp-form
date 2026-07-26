#!/usr/bin/env python3
"""Verify row-327 local divisor monodromy definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_local_divisor_monodromy_definition_obstruction.v1"
EXPECTED_KIND = "rhomred_local_divisor_monodromy_definition_obstruction"
SUCCESS_STATUS = "RHOMRED_LOCAL_DIVISOR_MONODROMY_DEFINITION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "def:local-divisor-monodromy-datum"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_local_divisor_monodromy_definition")

FIREWALL_FIXTURE = Path("certificates/orientation/rhomred_weyl_imaginary_divisor_firewall")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
ORIENTATION_FIXTURE = Path("certificates/orientation/k3e_reduced_orientation")
VANISHING_FIXTURE = Path("certificates/vanishing_cycles/transition_vanishing_cycle_preservation")
PFAFFIAN_FIXTURE = Path("certificates/pfaffian/k3e_finite_pfaffian")

FIREWALL_STATUS = "RHOMRED_WEYL_IMAGINARY_DIVISOR_FIREWALL_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
ORIENTATION_STATUS = "ORIENTATION_OBSTRUCTION_LEDGER_VERIFIED"
VANISHING_STATUS = "TRANSITION_VANISHING_CYCLE_PRESERVATION_OBSTRUCTION_VERIFIED"
PFAFFIAN_STATUS = "PFAFFIAN_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "definition_count": 1,
    "local_divisor_rows": 0,
    "normal_tube_rows": 0,
    "meridian_rows": 0,
    "coefficient_system_rows": 0,
    "pfaffian_line_rows": 0,
    "monodromy_operator_rows": 0,
    "epsilon_extension_claim": 0,
    "row328_irrelevance_claim": 0,
    "local_monodromy_constructed_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "compact_hall_divisor_component",
    "normal_tube_and_meridian",
    "reduced_coefficient_local_system",
    "pfaffian_line_summand",
    "monodromy_operator",
    "transition_compatibility",
    "row328_irrelevance_to_maass",
}

REQUIRED_FIREWALL = {
    "Weyl_generator",
    "epsilon_o_value",
    "maass_character_value",
    "automorphic_Humbert_divisor",
    "Borcherds_multiplicity",
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
        "definition_rows.csv",
        (
            "definition_id",
            "finite_stage_required",
            "divisor_component_required",
            "normal_tube_required",
            "meridian_required",
            "coefficient_system_required",
            "pfaffian_line_optional",
            "monodromy_operator_rule",
            "transition_compatibility_required",
            "weyl_character_domain_allowed",
            "definition_recorded",
            "local_monodromy_constructed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "local_divisor_rows.csv",
        (
            "divisor_id",
            "R_id",
            "stratum_id",
            "label_id",
            "label_kind",
            "source_divisor_row",
            "normal_tube_row",
            "component_supplied",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "local_monodromy_rows.csv",
        (
            "monodromy_id",
            "divisor_id",
            "basepoint_id",
            "meridian_id",
            "coefficient_system_id",
            "pfaffian_line_id",
            "operator_label",
            "operator_matrix",
            "rank_one_sign",
            "transition_row",
            "monodromy_supplied",
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
            "definition_status",
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
        "imaginary_divisor_firewall_imported",
        "compact_hall_ledger_imported",
        "reduced_orientation_ledger_imported",
        "vanishing_cycle_transition_imported",
        "finite_pfaffian_ledger_imported",
        "definition_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "local_divisor_rows_supplied",
        "normal_tube_rows_supplied",
        "meridian_rows_supplied",
        "coefficient_local_system_rows_supplied",
        "pfaffian_line_rows_supplied",
        "monodromy_operator_rows_supplied",
        "transition_compatibility_rows_supplied",
        "local_divisor_monodromy_constructed",
        "epsilon_o_extended_to_local_divisors",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(FIREWALL_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(ORIENTATION_FIXTURE),
            str(VANISHING_FIXTURE),
            str(PFAFFIAN_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> None:
    firewall = read_json(FIREWALL_FIXTURE / "manifest.json")
    require_equal(firewall.get("status"), FIREWALL_STATUS, "firewall status")
    require_equal(firewall.get("local_divisor_monodromy_defined"), False, "row326 definition flag")
    require_equal(
        firewall.get("epsilon_o_extended_to_imaginary_divisors"),
        False,
        "row326 epsilon extension flag",
    )

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty blocked")

    orientation = read_json(ORIENTATION_FIXTURE / "manifest.json")
    require_equal(
        orientation.get("obstruction_ledger_status"),
        ORIENTATION_STATUS,
        "orientation ledger status",
    )
    require_equal(
        orientation.get("orientation_certification"),
        False,
        "orientation certification",
    )

    vanishing = read_json(VANISHING_FIXTURE / "manifest.json")
    require_equal(vanishing.get("status"), VANISHING_STATUS, "vanishing-cycle status")
    require_equal(
        vanishing.get("vanishing_cycle_transition_certification"),
        False,
        "vanishing-cycle transition certification",
    )

    pfaffian = read_json(PFAFFIAN_FIXTURE / "manifest.json")
    require_equal(pfaffian.get("obstruction_ledger_status"), PFAFFIAN_STATUS, "Pfaffian status")
    require_equal(pfaffian.get("pfaffian_certification"), False, "Pfaffian certification")


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "imaginary_divisor_firewall",
            "compact_hall_source",
            "reduced_orientation",
            "vanishing_cycle_transition",
            "finite_pfaffian",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_definition(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "definition row count")
    row = rows[0]
    require_equal(row["definition_id"], "local_divisor_monodromy_definition", "definition id")
    for key in (
        "finite_stage_required",
        "divisor_component_required",
        "normal_tube_required",
        "meridian_required",
        "coefficient_system_required",
        "pfaffian_line_optional",
        "transition_compatibility_required",
        "definition_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in ("weyl_character_domain_allowed", "local_monodromy_constructed"):
        require_equal(bool_cell(row, key), False, key)
    if row["monodromy_operator_rule"] != "meridian_action_on_KR_or_supplied_pfaffian_line":
        raise ValueError(f"unexpected monodromy rule: {row}")
    check_verified(row, "definition_rows.csv")


def verify_empty_local_tables(
    local_divisors: list[dict[str, str]],
    local_monodromy: list[dict[str, str]],
) -> None:
    require_equal(local_divisors, [], "local divisor rows")
    require_equal(local_monodromy, [], "local monodromy rows")


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
        require_equal(row["definition_status"], "missing_open_obligation", "obligation status")
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
    verify_definition(tables["definition_rows.csv"])
    verify_empty_local_tables(tables["local_divisor_rows.csv"], tables["local_monodromy_rows.csv"])
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
