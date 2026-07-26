#!/usr/bin/env python3
"""Verify the row-357 finite Hall bracket-parity packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "finite_hall_bracket_parity.v1"
EXPECTED_KIND = "finite_hall_bracket_parity_obstruction"
SUCCESS_STATUS = "FINITE_HALL_BRACKET_PARITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:finite-hall-bracket-parity"
DEFAULT_FIXTURE = Path("certificates/hall/finite_hall_bracket_parity")

JACOBI_FIXTURE = Path("certificates/hall/finite_hall_graded_jacobi")
GRAM_DEGREE_FIXTURE = Path("certificates/hall/finite_hall_normal_ordered_gram_degree")
BRACKET_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
PARITY_PUSHFORWARD_FIXTURE = Path("certificates/charge/parity_pushforward")
COMPACT_SOURCE_FIXTURE = Path("certificates/sources/k3e_compact_hall")

JACOBI_STATUS = "FINITE_HALL_GRADED_JACOBI_OBSTRUCTION_VERIFIED"
GRAM_DEGREE_STATUS = "FINITE_HALL_NORMAL_ORDERED_GRAM_DEGREE_OBSTRUCTION_VERIFIED"
COMPACT_SOURCE_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "formal_bracket_rows": 3,
    "formal_bracket_parity_defect_total": 0,
    "formal_basis_parity_rows": 10,
    "parity_pushforward_source_rows": 6,
    "parity_pushforward_sum_rows": 3,
    "compact_source_parity_rows": 0,
    "source_product_matrix_rows": 0,
    "source_primitive_bracket_rows": 0,
    "source_bracket_parity_rows": 0,
}

EXPECTED_FORMAL_IMPORTS = {
    "formal_bracket_parity_rows": ("bracket_rows.csv", 3, 3, 0),
    "formal_bracket_basis_rows": ("basis_degrees.csv", 10, 10, 0),
    "formal_parity_source_rows": ("source_parity_rows.csv", 6, 6, 0),
    "formal_parity_pushforward_rows": ("pushforward_parity_sums.csv", 3, 3, 0),
    "formal_parity_relations": ("formal_relations.csv", 7, 7, 0),
}

REQUIRED_OBLIGATIONS = {
    "source_parity_blocks",
    "homogeneous_product_rows",
    "primitive_bracket_matrix",
    "bracket_parity_defect_rows",
    "parity_pushforward_as_source",
    "gn_kac_parity_equality",
    "signed_dimension_firewall",
    "source_vs_target_firewall",
}

REQUIRED_FIREWALL = {
    "target_parity_table",
    "signed_dimension",
    "scalar_trace",
    "formal_bracket_rows_only",
    "parity_pushforward_only",
    "row356_degree_only",
    "row355_jacobi_only",
    "product_without_parity",
    "bracket_without_parity",
    "gn_kac_parity_equality",
    "orientation_parity",
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
            "even_product_required",
            "homogeneous_parity_required",
            "supercommutator_formula_required",
            "parity_sum_required",
            "normal_ordered_degree_context_required",
            "formal_bracket_packet_imported",
            "parity_pushforward_packet_imported",
            "relative_theorem_recorded",
            "current_source_parity_proved",
            "gn_kac_parity_claimed",
            "primitive_lie_algebra_populated",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "parity_rows.csv",
        (
            "parity_row_id",
            "R_id",
            "left_primitive_basis_id",
            "right_primitive_basis_id",
            "target_primitive_basis_id",
            "left_parity",
            "right_parity",
            "target_parity",
            "sum_parity",
            "bracket_matrix_id",
            "parity_defect_rank",
            "parity_verified",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "formal_import_rows.csv",
        (
            "import_id",
            "source_fixture",
            "imported_table",
            "imported_row_count",
            "zero_defect_rows",
            "positive_defect_rows",
            "source_reference",
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
            "compatibility_status",
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


def parity_sum(left: str, right: str) -> str:
    if left not in {"even", "odd"} or right not in {"even", "odd"}:
        raise ValueError(f"bad parity values: {left!r}, {right!r}")
    return "even" if left == right else "odd"


def check_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("hall_kind"), EXPECTED_KIND, "hall_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("row_number"), 357, "row_number")

    for key in (
        "relative_theorem_recorded",
        "graded_jacobi_packet_imported",
        "normal_ordered_gram_degree_packet_imported",
        "bracket_pushforward_packet_imported",
        "parity_pushforward_packet_imported",
        "compact_hall_source_ledger_imported",
        "parity_formula_recorded",
        "formal_supplied_rows_verified",
    ):
        require_true(manifest.get(key), key)

    for key in (
        "source_parity_blocks_supplied",
        "source_product_matrix_rows_supplied",
        "source_primitive_bracket_rows_supplied",
        "source_bracket_parity_defect_rows_supplied",
        "bracket_parity_proved_for_current_source",
        "full_source_parity_certified",
        "gn_kac_parity_equality",
        "primitive_lie_algebra_populated",
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
        {
            str(JACOBI_FIXTURE),
            str(GRAM_DEGREE_FIXTURE),
            str(BRACKET_PUSHFORWARD_FIXTURE),
            str(PARITY_PUSHFORWARD_FIXTURE),
            str(COMPACT_SOURCE_FIXTURE),
        },
        "manifest imports",
    )


def check_local_tables(fixture: Path) -> None:
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}

    criterion = tables["criterion_rows.csv"]
    require_equal(len(criterion), 1, "criterion row count")
    row = criterion[0]
    for key in (
        "even_product_required",
        "homogeneous_parity_required",
        "supercommutator_formula_required",
        "parity_sum_required",
        "normal_ordered_degree_context_required",
        "formal_bracket_packet_imported",
        "parity_pushforward_packet_imported",
        "relative_theorem_recorded",
    ):
        require_equal(row.get(key), "true", f"criterion {key}")
    for key in (
        "current_source_parity_proved",
        "gn_kac_parity_claimed",
        "primitive_lie_algebra_populated",
    ):
        require_equal(row.get(key), "false", f"criterion {key}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError("criterion proof reference does not point to row-357 proposition")

    require_equal(len(tables["parity_rows.csv"]), 0, "parity row count")

    formal_imports = {row["import_id"]: row for row in tables["formal_import_rows.csv"]}
    require_equal(set(formal_imports), set(EXPECTED_FORMAL_IMPORTS), "formal import ids")
    for import_id, (table_name, row_count, zero_count, positive_count) in EXPECTED_FORMAL_IMPORTS.items():
        irow = formal_imports[import_id]
        require_equal(irow.get("imported_table"), table_name, f"{import_id} table")
        require_equal(int_cell(irow, "imported_row_count"), row_count, f"{import_id} count")
        require_equal(int_cell(irow, "zero_defect_rows"), zero_count, f"{import_id} zero")
        require_equal(int_cell(irow, "positive_defect_rows"), positive_count, f"{import_id} positive")
        require_equal(irow.get("check_status"), "verified", f"{import_id} status")

    coverage = {row["coverage_id"]: row for row in tables["coverage_rows.csv"]}
    require_equal(set(coverage), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        crow = coverage[coverage_id]
        require_equal(int_cell(crow, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(crow, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(crow, "defect_rank"), 0, f"{coverage_id} defect")
        require_equal(crow.get("check_status"), "verified", f"{coverage_id} status")

    obligations = {row["obligation_id"]: row for row in tables["blocked_obligations.csv"]}
    require_equal(set(obligations), REQUIRED_OBLIGATIONS, "blocked obligation ids")
    for obligation_id, orow in obligations.items():
        require_equal(orow.get("compatibility_status"), "missing_open_obligation", obligation_id)
        require_equal(orow.get("check_status"), "verified", f"{obligation_id} status")
        if PROOF_LABEL not in orow.get("proof_reference", ""):
            raise ValueError(f"{obligation_id}: proof reference does not point to proposition")

    firewall = {row["forbidden_substitute"]: row for row in tables["scalar_firewall.csv"]}
    require_equal(set(firewall), REQUIRED_FIREWALL, "firewall substitutes")
    for substitute, frow in firewall.items():
        require_equal(frow.get("excluded"), "true", f"{substitute} excluded")
        require_equal(int_cell(frow, "defect_rank"), 0, f"{substitute} defect")
        require_equal(frow.get("check_status"), "verified", f"{substitute} status")
        if PROOF_LABEL not in frow.get("proof_reference", ""):
            raise ValueError(f"{substitute}: proof reference does not point to proposition")

    for req in tables["text_requirements.csv"]:
        require_equal(req.get("fragment_present"), "true", f"{req['requirement_id']} fragment flag")
        require_equal(req.get("check_status"), "verified", f"{req['requirement_id']} status")


def check_bracket_pushforward_import() -> None:
    manifest = read_json(BRACKET_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(
        manifest.get("schema_version"),
        "hall_pairing_pushforward_compatibility.v1",
        "bracket pushforward schema",
    )
    require_true(manifest.get("certified"), "bracket pushforward certified")
    require_true(manifest.get("normal_ordered_bracket_degree"), "normal ordered bracket degree")
    require_false(manifest.get("compact_hall_correspondence"), "compact Hall correspondence")
    require_false(manifest.get("primitive_closure"), "primitive closure")

    basis_rows = read_table_path(BRACKET_PUSHFORWARD_FIXTURE / "basis_degrees.csv")
    require_equal(len(basis_rows), 10, "formal basis row count")
    parities: dict[str, str] = {}
    for row in basis_rows:
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"{row['basis_id']}: bad parity {parity!r}")
        parities[row["basis_id"]] = parity

    bracket_rows = read_table_path(BRACKET_PUSHFORWARD_FIXTURE / "bracket_rows.csv")
    require_equal(len(bracket_rows), 3, "formal bracket row count")
    for row in bracket_rows:
        bracket_id = row["bracket_id"]
        left = row["left_basis_id"]
        right = row["right_basis_id"]
        target = row["target_basis_id"]
        for basis_id in (left, right, target):
            if basis_id not in parities:
                raise ValueError(f"{bracket_id}: unknown basis id {basis_id}")
        expected_sum = parity_sum(parities[left], parities[right])
        require_equal(row.get("sum_parity"), expected_sum, f"{bracket_id} sum parity")
        require_equal(row.get("target_parity"), parities[target], f"{bracket_id} target parity")
        require_equal(row.get("target_parity"), row.get("sum_parity"), f"{bracket_id} parity")
        require_equal(row.get("check_status"), "verified", f"{bracket_id} status")


def check_parity_pushforward_import() -> None:
    manifest = read_json(PARITY_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(manifest.get("schema_version"), "parity_pushforward.v1", "parity pushforward schema")
    require_true(manifest.get("certified"), "parity pushforward certified")
    require_true(manifest.get("normal_ordered_parity_pushforward"), "normal ordered parity pushforward")
    for key in (
        "source_parity_certification",
        "gn_kac_parity_equality",
        "compact_source",
        "primitive_recognition",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_false(manifest.get(key), f"parity pushforward {key}")

    source_rows = read_table_path(PARITY_PUSHFORWARD_FIXTURE / "source_parity_rows.csv")
    require_equal(len(source_rows), 6, "parity pushforward source row count")
    for row in source_rows:
        if row["parity"] not in {"even", "odd"}:
            raise ValueError(f"{row['source_id']}: bad source parity")
        if int_cell(row, "dimension") <= 0:
            raise ValueError(f"{row['source_id']}: nonpositive dimension")
        require_equal(row.get("check_status"), "verified", f"{row['source_id']} status")

    pushforward_rows = read_table_path(PARITY_PUSHFORWARD_FIXTURE / "pushforward_parity_sums.csv")
    require_equal(len(pushforward_rows), 3, "parity pushforward sum row count")
    for row in pushforward_rows:
        require_equal(
            int_cell(row, "total_dimension"),
            int_cell(row, "even_dimension") + int_cell(row, "odd_dimension"),
            f"{row['pushforward_id']} total",
        )
        require_equal(int_cell(row, "parity_defect_rank"), 0, f"{row['pushforward_id']} defect")
        require_equal(row.get("check_status"), "verified", f"{row['pushforward_id']} status")

    relation_rows = read_table_path(PARITY_PUSHFORWARD_FIXTURE / "formal_relations.csv")
    require_equal(len(relation_rows), 7, "parity relation row count")
    relation_ids = {row["relation_id"] for row in relation_rows}
    if "parity_pushforward_preserves_blocks" not in relation_ids:
        raise ValueError("parity pushforward relation is missing")
    for row in relation_rows:
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['relation_id']} defect")
        require_equal(row.get("check_status"), "verified", f"{row['relation_id']} status")


def check_imports() -> None:
    jacobi = read_json(JACOBI_FIXTURE / "manifest.json")
    require_equal(jacobi.get("status"), JACOBI_STATUS, "row355 Jacobi packet status")
    require_false(jacobi.get("parity_rows_supplied"), "row355 parity rows")
    require_false(jacobi.get("primitive_lie_algebra_populated"), "row355 primitive Lie algebra")

    gram_degree = read_json(GRAM_DEGREE_FIXTURE / "manifest.json")
    require_equal(gram_degree.get("status"), GRAM_DEGREE_STATUS, "row356 Gram-degree packet status")
    require_false(gram_degree.get("parity_proved"), "row356 parity proved")
    require_false(
        gram_degree.get("normal_ordered_gram_degree_proved_for_current_source"),
        "row356 current-source degree",
    )

    check_bracket_pushforward_import()
    check_parity_pushforward_import()

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
    for table_name in (
        "degrees.csv",
        "M_entries.csv",
        "B_entries.csv",
        "hall_bialgebra_identities.csv",
        "parity_blocks.csv",
    ):
        require_table_empty(COMPACT_SOURCE_FIXTURE / table_name)


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
        if row["required_fragment"] not in text:
            raise ValueError(f"{row['requirement_id']}: required fragment not found")


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
