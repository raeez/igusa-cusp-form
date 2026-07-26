#!/usr/bin/env python3
"""Verify row-326 imaginary-divisor/Weyl-monodromy firewall packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_imaginary_divisor_firewall.v1"
EXPECTED_KIND = "rhomred_weyl_imaginary_divisor_firewall"
SUCCESS_STATUS = "RHOMRED_WEYL_IMAGINARY_DIVISOR_FIREWALL_VERIFIED"
PROOF_LABEL = "prop:imaginary-divisor-not-weyl-monodromy"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_imaginary_divisor_firewall")

SEMIDIRECT_FIXTURE = Path("certificates/orientation/rhomred_weyl_semidirect_hall_lifts")
SEMIDIRECT_STATUS = "RHOMRED_WEYL_SEMIDIRECT_HALL_LIFTS_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "separation_rows": 4,
    "real_weyl_generator_rows": 2,
    "imaginary_weyl_generator_rows": 0,
    "imaginary_epsilon_argument_rows": 0,
    "local_divisor_monodromy_definition_claim": 0,
    "epsilon_extension_to_imaginary_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "local_divisor_monodromy_definition",
    "local_divisor_monodromy_irrelevance",
    "compact_hall_imaginary_loop",
}

REQUIRED_FIREWALL = {
    "imaginary_root_as_Weyl_generator",
    "imaginary_monodromy_as_epsilon_o_value",
    "denominator_multiplicity_as_monodromy",
    "Borcherds_divisor_component_as_Weyl_reflection",
    "scalar_trace",
    "maass_character_value",
    "OP_scalar_branch",
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
        "separation_rows.csv",
        (
            "separation_id",
            "object_kind",
            "domain_or_source",
            "allowed_as_weyl_generator",
            "allowed_as_epsilon_o_argument",
            "allowed_as_local_divisor_monodromy_source",
            "local_divisor_monodromy_defined",
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
            "firewall_status",
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
        "real_root_definition_imported",
        "imaginary_root_definition_imported",
        "semidirect_hall_lifts_imported",
        "weyl_domain_recorded",
        "imaginary_not_weyl_recorded",
        "local_divisor_monodromy_separated",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "local_divisor_monodromy_defined",
        "imaginary_monodromy_as_weyl_allowed",
        "epsilon_o_extended_to_imaginary_divisors",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(set(manifest.get("imports", [])), {str(SEMIDIRECT_FIXTURE)}, "imports")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> None:
    manifest = read_json(SEMIDIRECT_FIXTURE / "manifest.json")
    require_equal(manifest.get("status"), SEMIDIRECT_STATUS, "semidirect status")
    require_equal(
        manifest.get("semidirect_hall_lifts_supplied"),
        False,
        "semidirect Hall lifts supplied",
    )


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "real_root_definition",
            "real_imaginary_comparison",
            "chapter6_firewall",
            "semidirect_hall_lifts",
            "optimization_row",
        },
        "source ids",
    )
    require_equal(indexed["semidirect_hall_lifts"]["source_status"], SEMIDIRECT_STATUS, "semidirect source")
    require_equal(indexed["optimization_row"]["source_status"], "row_326", "optimization row")
    for row in rows:
        check_verified(row, "source_rows.csv")


def verify_separation(rows: list[dict[str, str]]) -> dict[str, int]:
    indexed = rows_by(rows, "separation_id", "separation_rows.csv")
    require_equal(
        set(indexed),
        {
            "real_simple_reflections",
            "real_root_orbit",
            "imaginary_simple_roots",
            "imaginary_divisor_components",
        },
        "separation ids",
    )
    for key in ("real_simple_reflections", "real_root_orbit"):
        row = indexed[key]
        require_equal(bool_cell(row, "allowed_as_weyl_generator"), True, f"{key} Weyl")
        require_equal(bool_cell(row, "allowed_as_epsilon_o_argument"), True, f"{key} epsilon")
        require_equal(
            bool_cell(row, "allowed_as_local_divisor_monodromy_source"),
            False,
            f"{key} local monodromy",
        )
        require_equal(bool_cell(row, "local_divisor_monodromy_defined"), False, f"{key} defined")
        check_verified(row, "separation_rows.csv")
    for key in ("imaginary_simple_roots", "imaginary_divisor_components"):
        row = indexed[key]
        require_equal(bool_cell(row, "allowed_as_weyl_generator"), False, f"{key} Weyl")
        require_equal(bool_cell(row, "allowed_as_epsilon_o_argument"), False, f"{key} epsilon")
        require_equal(
            bool_cell(row, "allowed_as_local_divisor_monodromy_source"),
            True,
            f"{key} local monodromy",
        )
        require_equal(bool_cell(row, "local_divisor_monodromy_defined"), False, f"{key} defined")
        check_verified(row, "separation_rows.csv")
    return {
        "separation_rows": len(rows),
        "real_weyl_generator_rows": sum(
            1 for row in rows if bool_cell(row, "allowed_as_weyl_generator")
        ),
        "imaginary_weyl_generator_rows": sum(
            1
            for row in rows
            if row["separation_id"].startswith("imaginary")
            and bool_cell(row, "allowed_as_weyl_generator")
        ),
        "imaginary_epsilon_argument_rows": sum(
            1
            for row in rows
            if row["separation_id"].startswith("imaginary")
            and bool_cell(row, "allowed_as_epsilon_o_argument")
        ),
    }


def verify_coverage(
    rows: list[dict[str, str]],
    manifest: dict,
    separation_counts: dict[str, int],
) -> None:
    indexed = rows_by(rows, "coverage_id", "coverage_rows.csv")
    require_equal(set(indexed), set(EXPECTED_COVERAGE), "coverage ids")
    dynamic = dict(EXPECTED_COVERAGE)
    dynamic.update(separation_counts)
    dynamic["local_divisor_monodromy_definition_claim"] = int(
        bool(manifest.get("local_divisor_monodromy_defined"))
    )
    dynamic["epsilon_extension_to_imaginary_claim"] = int(
        bool(manifest.get("epsilon_o_extended_to_imaginary_divisors"))
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
        require_equal(row["firewall_status"], "missing_open_obligation", "firewall status")
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
    verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables["source_rows.csv"])
    separation_counts = verify_separation(tables["separation_rows.csv"])
    verify_coverage(tables["coverage_rows.csv"], manifest, separation_counts)
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
