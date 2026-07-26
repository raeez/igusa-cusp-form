#!/usr/bin/env python3
"""Verify row-333 negative-root orientation-compatibility packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_negative_root_orientation_compatibility_obstruction.v1"
EXPECTED_KIND = "rhomred_negative_root_orientation_compatibility_obstruction"
SUCCESS_STATUS = "RHOMRED_NEGATIVE_ROOT_ORIENTATION_COMPATIBILITY_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-line-negative-root-compatibility"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_negative_root_orientation_compatibility")

DUAL_FIXTURE = Path("certificates/moduli/retained_dual_closure")
TARGET_FIXTURE = Path("certificates/targets/delta5_gn_kac/a071_target_presentation")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
ROW332_FIXTURE = Path("certificates/orientation/rhomred_delta123_parity_compatibility")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

DUAL_SCHEMA = "retained_dual_closure.v1"
PAIRING_PUSHFORWARD_SCHEMA = "hall_pairing_pushforward_compatibility.v1"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
ROW332_STATUS = "RHOMRED_DELTA123_PARITY_COMPATIBILITY_OBSTRUCTION_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "retained_dual_type_rows": 3,
    "retained_dual_hn_rows": 7,
    "target_negative_dual_formal_blocks": 12,
    "target_source_pairing_true_rows": 0,
    "source_pairing_rows": 0,
    "source_hopf_pairing_identity_rows": 0,
    "source_radical_rows": 0,
    "source_negative_parity_rows": 0,
    "orientation_square_root_rows": 0,
    "orientation_transition_rows": 0,
    "negative_root_compatibility_rows": 0,
    "row334_chevalley_claim": 0,
    "row335_frobenius_claim": 0,
    "row336_trace_degree_claim": 0,
    "row337_serre_sign_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_negative_root_charts",
    "source_duality_lift",
    "source_positive_negative_pairing",
    "source_pairing_off_parity_zero",
    "hopf_pairing_identities",
    "source_radical_quotient",
    "source_negative_parity_blocks",
    "orientation_square_roots",
    "serre_sign_line",
    "determinant_duality_square",
    "quotient_orientation_transport",
    "orientation_transition_transport",
    "row334_chevalley_antiinvolution",
    "row335_frobenius_pairing",
    "row336_trace_degree",
    "row337_serre_signs",
}

REQUIRED_FIREWALL = {
    "retained_dual_closure",
    "target_negative_dual_formal_block",
    "source_pairing_false_target_rows",
    "formal_pairing_pushforward",
    "compact_Hall_empty_ledger",
    "empty_G_entries",
    "row332_delta123_parity_compatibility",
    "determinant_line_only",
    "square_root_obstruction_ledger",
    "Chevalley_word_only",
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
            "retained_dual_closure_required",
            "source_negative_chart_required",
            "source_duality_lift_required",
            "target_negative_block_required",
            "source_parity_blocks_required",
            "source_pairing_required",
            "hopf_pairing_identity_required",
            "radical_quotient_required",
            "orientation_square_roots_required",
            "serre_sign_line_required",
            "quotient_orientation_required",
            "orientation_transition_required",
            "retained_dual_closure_as_source_allowed",
            "target_negative_block_as_source_allowed",
            "formal_pairing_pushforward_as_source_allowed",
            "criterion_recorded",
            "compatibility_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "negative_root_compatibility_rows.csv",
        (
            "compatibility_row_id",
            "R_id",
            "stratum_id",
            "positive_degree_id",
            "negative_degree_id",
            "positive_chart_id",
            "negative_chart_id",
            "source_duality_lift_id",
            "source_pairing_matrix_id",
            "source_radical_id",
            "positive_parity_block_id",
            "negative_parity_block_id",
            "positive_orientation_line_id",
            "negative_orientation_line_id",
            "serre_sign_line_id",
            "determinant_duality_square_id",
            "quotient_orientation_transport_id",
            "orientation_transition_id",
            "compatibility_verified",
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
        "retained_dual_closure_imported",
        "target_presentation_imported",
        "hall_pairing_pushforward_imported",
        "compact_hall_ledger_imported",
        "delta123_parity_compatibility_imported",
        "transition_orientation_ledger_imported",
        "negative_root_orientation_criterion_recorded",
        "target_negative_dual_blocks_certified",
        "retained_dual_closure_certified",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_negative_root_chart_rows_supplied",
        "source_duality_lift_rows_supplied",
        "source_pairing_rows_supplied",
        "source_hopf_pairing_identity_rows_supplied",
        "source_radical_rows_supplied",
        "source_negative_parity_rows_supplied",
        "orientation_square_root_rows_supplied",
        "serre_sign_line_rows_supplied",
        "quotient_orientation_rows_supplied",
        "orientation_transition_rows_supplied",
        "negative_root_orientation_compatibility_proved",
        "row334_chevalley_claimed",
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
            str(DUAL_FIXTURE),
            str(TARGET_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(ROW332_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    dual = read_json(DUAL_FIXTURE / "manifest.json")
    require_equal(dual.get("schema_version"), DUAL_SCHEMA, "dual schema")
    require_equal(dual.get("certified"), True, "dual certified")
    require_equal(dual.get("dual_closure"), True, "dual closure")
    require_equal(dual.get("compact_hall_stage"), False, "dual compact Hall stage")
    require_equal(dual.get("pfaffian_orientation"), False, "dual Pfaffian orientation")
    require_equal(len(read_table_path(DUAL_FIXTURE / "type_duals.csv")), 3, "type dual rows")
    require_equal(len(read_table_path(DUAL_FIXTURE / "dual_closure.csv")), 7, "HN dual rows")

    target_pairs = read_table_path(TARGET_FIXTURE / "target_pairing_blocks.csv")
    formal_blocks = [
        row for row in target_pairs if row["pairing_block_status"] == "target_negative_dual_formal_block"
    ]
    require_equal(len(formal_blocks), 12, "target formal negative-dual blocks")
    require_equal(sum(1 for row in target_pairs if bool_cell(row, "source_pairing")), 0, "source pairing target rows")

    pairing_pushforward = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pairing_pushforward.get("schema_version"), PAIRING_PUSHFORWARD_SCHEMA, "pairing pushforward schema")
    require_equal(pairing_pushforward.get("certified"), True, "pairing pushforward certified")
    require_equal(pairing_pushforward.get("compact_hall_correspondence"), False, "pairing compact Hall")
    require_equal(pairing_pushforward.get("pfaffian_orientation"), False, "pairing Pfaffian orientation")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty")
    require_empty_csv(COMPACT_HALL_FIXTURE / "G_entries.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "hopf_pairing_identities.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "K_entries.csv")
    require_empty_csv(COMPACT_HALL_FIXTURE / "parity_blocks.csv")

    row332 = read_json(ROW332_FIXTURE / "manifest.json")
    require_equal(row332.get("status"), ROW332_STATUS, "row332 status")
    require_equal(row332.get("delta123_parity_compatibility_proved"), False, "row332 compatibility proved")
    require_equal(row332.get("row334_chevalley_claimed"), False, "row332 Chevalley flag")

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
            "retained_dual_closure",
            "a071_target_presentation",
            "hall_pairing_pushforward",
            "compact_hall_source",
            "delta123_parity_compatibility",
            "transition_orientation",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "negative_root_orientation_compatibility", "criterion id")
    for key in (
        "retained_dual_closure_required",
        "source_negative_chart_required",
        "source_duality_lift_required",
        "target_negative_block_required",
        "source_parity_blocks_required",
        "source_pairing_required",
        "hopf_pairing_identity_required",
        "radical_quotient_required",
        "orientation_square_roots_required",
        "serre_sign_line_required",
        "quotient_orientation_required",
        "orientation_transition_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in (
        "retained_dual_closure_as_source_allowed",
        "target_negative_block_as_source_allowed",
        "formal_pairing_pushforward_as_source_allowed",
        "compatibility_proved",
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
    require_equal(tables["negative_root_compatibility_rows.csv"], [], "negative root compatibility rows")
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
