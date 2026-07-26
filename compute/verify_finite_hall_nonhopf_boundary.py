#!/usr/bin/env python3
"""Verify the row-352 finite Hall non-Hopf boundary packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_nonhopf_boundary.v1"
EXPECTED_KIND = "finite_hall_nonhopf_boundary"
SUCCESS_STATUS = "FINITE_HALL_NONHOPF_BOUNDARY_VERIFIED"
PROOF_LABEL = "prop:finite-hall-nonhopf-boundary"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_nonhopf_boundary")

ANTIPODE_FIXTURE = Path("certificates/hall/finite_hall_antipode_datum")
BIALGEBRA_FIXTURE = Path("certificates/hall/finite_hall_bialgebra_compatibility")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

ANTIPODE_STATUS = "FINITE_HALL_ANTIPODE_DATUM_OBSTRUCTION_VERIFIED"
BIALGEBRA_STATUS = "FINITE_HALL_BIALGEBRA_COMPATIBILITY_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "boundary_count": 1,
    "row351_antipode_rows": 0,
    "row351_convolution_identity_rows": 0,
    "row351_hopf_claims": 0,
    "source_antipode_rows": 0,
    "source_unit_counit_rows": 0,
    "source_bialgebra_rows": 0,
    "row350_compatibility_rows": 0,
}

REQUIRED_PROMOTIONS = {
    "bialgebra_to_hopf_without_antipode",
    "row350_bialgebra_compatibility_to_hopf",
    "hopf_pairing_to_antipode",
    "drinfeld_double_to_source_antipode",
    "bar_coalgebra_to_hopf",
    "primitive_closure_to_hopf",
    "target_hopf_to_source_hopf",
    "scalar_trace_to_hopf",
    "nonexistence_theorem_without_search",
}

FORBIDDEN_CHAPTER_FRAGMENTS = (
    "these form a graded Hopf datum on the protected primitive layer",
    "for the primitive layer of the protected Hall Hopf object",
)


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
        "boundary_rows.csv",
        (
            "boundary_id",
            "bialgebra_without_antipode_hopf_name_allowed",
            "row351_antipode_datum_required",
            "current_hopf_claim_present",
            "nonexistence_of_antipode_claimed",
            "bialgebra_level_name_required",
            "conditional_hopf_statement_required",
            "boundary_recorded",
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
        "forbidden_promotions.csv",
        (
            "promotion_id",
            "forbidden_promotion",
            "excluded",
            "defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "text_requirements.csv",
        (
            "requirement_id",
            "file_path",
            "required_fragment",
            "fragment_present",
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


def read_optional_table(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    return read_table_path(path, allow_empty=True)


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    return read_table_path(fixture / spec.path, spec.columns, allow_empty=spec.allow_empty)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_true(value: object, label: str) -> None:
    require_equal(value, True, label)


def require_false(value: object, label: str) -> None:
    require_equal(value, False, label)


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"{key}: expected integer cell, got {row.get(key)!r}") from exc


def require_table_empty(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    if rows:
        raise ValueError(f"{path}: expected no rows, got {len(rows)}")


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("row_number"), 352, "row_number")

    for key in (
        "boundary_recorded",
        "antipode_packet_imported",
        "bialgebra_compatibility_packet_imported",
        "compact_hall_source_ledger_imported",
        "future_antipode_allowed_as_open_obligation",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "bialgebra_without_antipode_hopf_name_allowed",
        "current_finite_hall_hopf_algebra_claimed",
        "nonexistence_of_antipode_claimed",
        "mathematical_certification",
    ):
        require_false(manifest.get(key), key)

    require_equal(
        set(manifest.get("tables", [])),
        {spec.path for spec in TABLE_SPECS},
        "manifest tables",
    )
    require_equal(
        set(manifest.get("imports", [])),
        {str(ANTIPODE_FIXTURE), str(BIALGEBRA_FIXTURE), str(COMPACT_SOURCE_FIXTURE)},
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    boundary = tables["boundary_rows.csv"]
    require_equal(len(boundary), 1, "boundary row count")
    row = boundary[0]
    require_equal(row.get("bialgebra_without_antipode_hopf_name_allowed"), "false", "boundary hopf allowed")
    require_equal(row.get("row351_antipode_datum_required"), "true", "boundary row351 required")
    require_equal(row.get("current_hopf_claim_present"), "false", "boundary current hopf claim")
    require_equal(row.get("nonexistence_of_antipode_claimed"), "false", "boundary nonexistence claim")
    require_equal(row.get("bialgebra_level_name_required"), "true", "boundary bialgebra level")
    require_equal(row.get("conditional_hopf_statement_required"), "true", "boundary conditional hopf")
    require_equal(row.get("boundary_recorded"), "true", "boundary recorded")
    require_equal(row.get("check_status"), "verified", "boundary status")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("boundary proof reference does not point to row-352 proposition")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        crow = coverage[coverage_id]
        require_equal(int_cell(crow, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(crow, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(crow, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(crow.get("check_status"), "verified", f"{coverage_id} status")

    promotions = {row["forbidden_promotion"]: row for row in tables["forbidden_promotions.csv"]}
    require_equal(set(promotions), REQUIRED_PROMOTIONS, "forbidden promotions")
    for promotion, prow in promotions.items():
        require_equal(prow.get("excluded"), "true", f"{promotion} excluded")
        require_equal(int_cell(prow, "defect_rank"), 0, f"{promotion} defect")
        require_equal(prow.get("check_status"), "verified", f"{promotion} status")
        if PROOF_LABEL not in prow.get("proof_reference", ""):
            raise ValueError(f"{promotion}: proof reference does not point to proposition")

    for req in tables["text_requirements.csv"]:
        require_equal(req.get("fragment_present"), "true", f"{req['requirement_id']} fragment flag")
        require_equal(req.get("check_status"), "verified", f"{req['requirement_id']} status")


def check_imports() -> None:
    antipode = read_json(ANTIPODE_FIXTURE / "manifest.json")
    require_equal(antipode.get("status"), ANTIPODE_STATUS, "antipode packet status")
    require_false(antipode.get("actual_antipode_proved"), "row351 actual antipode")
    require_false(antipode.get("finite_hall_hopf_algebra_claimed"), "row351 hopf claim")
    require_table_empty(ANTIPODE_FIXTURE / "antipode_rows.csv")
    require_table_empty(ANTIPODE_FIXTURE / "convolution_identity_rows.csv")

    bialgebra = read_json(BIALGEBRA_FIXTURE / "manifest.json")
    require_equal(bialgebra.get("status"), BIALGEBRA_STATUS, "bialgebra packet status")
    require_false(bialgebra.get("actual_bialgebra_compatibility_proved"), "row350 actual bialgebra")
    require_false(bialgebra.get("finite_hall_bialgebra_populated"), "row350 populated bialgebra")
    require_table_empty(BIALGEBRA_FIXTURE / "compatibility_rows.csv")

    compact_source = read_json(COMPACT_SOURCE_FIXTURE / "manifest.json")
    require_equal(
        compact_source.get("obstruction_ledger_status"),
        COMPACT_SOURCE_STATUS,
        "compact source status",
    )
    require_false(compact_source.get("compact_source_recognition"), "compact source recognition")
    require_false(
        compact_source.get("mathematical_certification"),
        "compact source mathematical certification",
    )
    for table_name in ("unit_counit.csv", "hall_bialgebra_identities.csv"):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)
    require_equal(
        len(read_optional_table(COMPACT_SOURCE_FIXTURE / "S_entries.csv")),
        0,
        "source antipode rows",
    )


def check_text_requirements(fixture: Path) -> None:
    rows = read_table_path(
        fixture / "text_requirements.csv",
        next(spec.columns for spec in TABLE_SPECS if spec.path == "text_requirements.csv"),
    )
    for row in rows:
        path = Path(row["file_path"])
        if not path.exists():
            raise ValueError(f"{row['requirement_id']}: missing text file {path}")
        text = path.read_text(encoding="utf-8")
        fragment = row["required_fragment"]
        if fragment not in text:
            raise ValueError(f"{row['requirement_id']}: required fragment not found")

    chapter = Path("chapters/05_subsections/05_3_hall.tex").read_text(encoding="utf-8")
    for fragment in FORBIDDEN_CHAPTER_FRAGMENTS:
        if fragment in chapter:
            raise ValueError(f"forbidden unconditional Hopf fragment remains: {fragment}")


def verify(fixture: Path) -> str:
    check_manifest(fixture)
    check_local_tables(fixture)
    check_imports()
    check_text_requirements(fixture)
    return SUCCESS_STATUS


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        status = verify(args.fixture)
    except Exception as exc:
        print(f"verification failed: {exc}", file=sys.stderr)
        return 1
    print(status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
