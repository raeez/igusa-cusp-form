#!/usr/bin/env python3
"""Verify row-334 orientation Chevalley anti-involution packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_chevalley_antiinvolution_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_chevalley_antiinvolution_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_CHEVALLEY_ANTIINVOLUTION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-chevalley-antiinvolution"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_chevalley_antiinvolution")

ROW333_FIXTURE = Path("certificates/orientation/rhomred_negative_root_orientation_compatibility")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
TARGET_FIXTURE = Path("certificates/targets/delta5_gn_kac/a071_target_presentation")
DUAL_FIXTURE = Path("certificates/moduli/retained_dual_closure")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

ROW333_STATUS = "RHOMRED_NEGATIVE_ROOT_ORIENTATION_COMPATIBILITY_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
DUAL_SCHEMA = "retained_dual_closure.v1"
PAIRING_PUSHFORWARD_SCHEMA = "hall_pairing_pushforward_compatibility.v1"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "target_relation_rows": 19,
    "target_negative_dual_formal_blocks": 12,
    "target_source_pairing_true_rows": 0,
    "retained_dual_hn_rows": 7,
    "source_simple_representative_rows": 0,
    "source_bracket_rows": 0,
    "source_chevalley_relation_rows": 0,
    "source_pairing_rows": 0,
    "source_radical_rows": 0,
    "source_parity_rows": 0,
    "orientation_transition_rows": 0,
    "chevalley_antiinvolution_rows": 0,
    "row335_frobenius_claim": 0,
    "row336_trace_degree_claim": 0,
    "row337_serre_sign_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_simple_representatives",
    "positive_negative_source_charts",
    "source_bracket_matrix",
    "source_chevalley_relation_rows",
    "cartan_orientation_rows",
    "source_pairing_matrix",
    "radical_quotient",
    "parity_preservation",
    "orientation_square_roots",
    "determinant_duality_square",
    "serre_sign_line",
    "quotient_orientation_transport",
    "transition_compatibility",
    "involutivity_identity",
    "anti_multiplicativity_identity",
    "row335_frobenius_pairing",
    "row336_trace_degree",
    "row337_serre_signs",
}

REQUIRED_FIREWALL = {
    "target_Chevalley_language",
    "target_presentation",
    "retained_dual_closure",
    "formal_pairing_pushforward",
    "row333_negative_root_criterion",
    "compact_Hall_empty_ledger",
    "empty_simple_representatives",
    "empty_relation_rows",
    "empty_B_entries",
    "empty_G_entries",
    "determinant_line_only",
    "square_root_obstruction_ledger",
    "scalar_trace",
    "protected_trace",
    "pfaffian_product",
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
            "negative_root_compatibility_required",
            "source_simple_representatives_required",
            "source_positive_negative_charts_required",
            "source_bracket_required",
            "source_chevalley_relations_required",
            "source_pairing_required",
            "radical_quotient_required",
            "source_parity_blocks_required",
            "orientation_square_roots_required",
            "determinant_duality_square_required",
            "serre_sign_line_required",
            "quotient_orientation_required",
            "transition_compatibility_required",
            "target_chevalley_as_source_allowed",
            "retained_dual_closure_as_source_allowed",
            "formal_pairing_pushforward_as_source_allowed",
            "criterion_recorded",
            "antiinvolution_constructed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "chevalley_antiinvolution_rows.csv",
        (
            "antiinvolution_row_id",
            "R_id",
            "stratum_id",
            "positive_degree_id",
            "negative_degree_id",
            "source_positive_chart_id",
            "source_negative_chart_id",
            "simple_representative_row_id",
            "cartan_row_id",
            "source_bracket_matrix_id",
            "chevalley_relation_row_id",
            "pairing_matrix_id",
            "radical_quotient_id",
            "positive_orientation_line_id",
            "negative_orientation_line_id",
            "determinant_duality_square_id",
            "serre_sign_line_id",
            "quotient_orientation_transport_id",
            "transition_row_id",
            "involutive_defect_rank",
            "anti_multiplicative_defect_rank",
            "orientation_square_defect_rank",
            "antiinvolution_verified",
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


def require_empty_csv(path: Path) -> None:
    rows = read_table_path(path, allow_empty=True)
    require_equal(rows, [], str(path))


def check_verified(row: dict[str, str], table_name: str, *, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "negative_root_compatibility_imported",
        "compact_hall_ledger_imported",
        "target_presentation_imported",
        "retained_dual_closure_imported",
        "hall_pairing_pushforward_imported",
        "transition_orientation_ledger_imported",
        "chevalley_antiinvolution_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_simple_representative_rows_supplied",
        "source_positive_negative_chart_rows_supplied",
        "source_bracket_rows_supplied",
        "source_chevalley_relation_rows_supplied",
        "source_pairing_rows_supplied",
        "source_radical_rows_supplied",
        "source_parity_blocks_supplied",
        "orientation_square_root_rows_supplied",
        "determinant_duality_square_rows_supplied",
        "serre_sign_line_rows_supplied",
        "quotient_orientation_rows_supplied",
        "transition_rows_supplied",
        "chevalley_antiinvolution_constructed",
        "row335_frobenius_claimed",
        "row336_trace_degree_claimed",
        "row337_serre_sign_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW333_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(TARGET_FIXTURE),
            str(DUAL_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    row333 = read_json(ROW333_FIXTURE / "manifest.json")
    require_equal(row333.get("status"), ROW333_STATUS, "row333 status")
    require_equal(
        row333.get("negative_root_orientation_compatibility_proved"),
        False,
        "row333 compatibility proved",
    )
    require_equal(row333.get("row334_chevalley_claimed"), False, "row333 Chevalley flag")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty")
    require_empty_csv(COMPACT_HALL_FIXTURE / "simple_representatives.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "B_entries.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "relation_rows.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "G_entries.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "K_entries.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "parity_blocks.csv")

    target_relations = read_table_path(TARGET_FIXTURE / "target_relation_rows.csv")
    require_equal(len(target_relations), 19, "target relation rows")
    target_pairs = read_table_path(TARGET_FIXTURE / "target_pairing_blocks.csv")
    formal_blocks = [
        row for row in target_pairs if row["pairing_block_status"] == "target_negative_dual_formal_block"
    ]
    require_equal(len(formal_blocks), 12, "target formal negative-dual blocks")
    require_equal(sum(1 for row in target_pairs if bool_cell(row, "source_pairing")), 0, "source pairing target rows")

    dual = read_json(DUAL_FIXTURE / "manifest.json")
    require_equal(dual.get("schema_version"), DUAL_SCHEMA, "dual schema")
    require_equal(dual.get("certified"), True, "dual certified")
    require_equal(dual.get("dual_closure"), True, "dual closure")
    require_equal(dual.get("compact_hall_stage"), False, "dual compact Hall stage")
    require_equal(dual.get("pfaffian_orientation"), False, "dual Pfaffian orientation")
    require_equal(len(read_table_path(DUAL_FIXTURE / "dual_closure.csv")), 7, "HN dual rows")

    pairing_pushforward = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pairing_pushforward.get("schema_version"), PAIRING_PUSHFORWARD_SCHEMA, "pairing pushforward schema")
    require_equal(pairing_pushforward.get("certified"), True, "pairing pushforward certified")
    require_equal(pairing_pushforward.get("compact_hall_correspondence"), False, "pairing compact Hall")
    require_equal(pairing_pushforward.get("hopf_adjointness"), False, "pairing Hopf adjointness")
    require_equal(pairing_pushforward.get("frobenius_cyclic_identity"), False, "pairing Frobenius")
    require_equal(pairing_pushforward.get("pfaffian_orientation"), False, "pairing Pfaffian orientation")

    transition_orientation = read_json(TRANSITION_ORIENTATION_FIXTURE / "manifest.json")
    require_equal(transition_orientation.get("status"), TRANSITION_ORIENTATION_STATUS, "transition orientation status")
    require_equal(transition_orientation.get("orientation_transition_certification"), False, "transition orientation certification")
    require_empty_csv(TRANSITION_ORIENTATION_FIXTURE / "orientation_transition_maps.csv")


def verify_sources(rows: list[dict[str, str]]) -> None:
    indexed = rows_by(rows, "source_id", "source_rows.csv")
    require_equal(
        set(indexed),
        {
            "optimization_row",
            "negative_root_orientation_compatibility",
            "compact_hall_source",
            "a071_target_presentation",
            "retained_dual_closure",
            "hall_pairing_pushforward",
            "transition_orientation",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "orientation_chevalley_antiinvolution", "criterion id")
    for key in (
        "negative_root_compatibility_required",
        "source_simple_representatives_required",
        "source_positive_negative_charts_required",
        "source_bracket_required",
        "source_chevalley_relations_required",
        "source_pairing_required",
        "radical_quotient_required",
        "source_parity_blocks_required",
        "orientation_square_roots_required",
        "determinant_duality_square_required",
        "serre_sign_line_required",
        "quotient_orientation_required",
        "transition_compatibility_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in (
        "target_chevalley_as_source_allowed",
        "retained_dual_closure_as_source_allowed",
        "formal_pairing_pushforward_as_source_allowed",
        "antiinvolution_constructed",
    ):
        require_equal(bool_cell(row, key), False, key)
    check_verified(row, "criterion_rows.csv")


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
        require_equal(row["compatibility_status"], "missing_open_obligation", "obligation status")
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
    verify_criterion(tables["criterion_rows.csv"])
    require_equal(tables["chevalley_antiinvolution_rows.csv"], [], "Chevalley antiinvolution rows")
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
