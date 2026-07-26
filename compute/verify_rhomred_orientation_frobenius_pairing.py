#!/usr/bin/env python3
"""Verify row-335 orientation Frobenius pairing packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_orientation_frobenius_pairing_obstruction.v1"
EXPECTED_KIND = "rhomred_orientation_frobenius_pairing_obstruction"
SUCCESS_STATUS = "RHOMRED_ORIENTATION_FROBENIUS_PAIRING_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "prop:orientation-frobenius-pairing"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_orientation_frobenius_pairing")

ROW334_FIXTURE = Path("certificates/orientation/rhomred_orientation_chevalley_antiinvolution")
COMPACT_HALL_FIXTURE = Path("certificates/sources/k3e_compact_hall")
PAIRING_PUSHFORWARD_FIXTURE = Path("certificates/charge/hall_pairing_pushforward_compatibility")
TRANSITION_RADICAL_FIXTURE = Path("certificates/hall/transition_radical_preservation")
PAIRING_KERNEL_LIM1_FIXTURE = Path("certificates/hall/pairing_kernel_lim1_vanishing")
TRANSITION_ORIENTATION_FIXTURE = Path("certificates/orientation/transition_orientation_preservation")

ROW334_STATUS = "RHOMRED_ORIENTATION_CHEVALLEY_ANTIINVOLUTION_OBSTRUCTION_VERIFIED"
COMPACT_HALL_STATUS = "COMPACT_HALL_OBSTRUCTION_LEDGER_VERIFIED"
PAIRING_PUSHFORWARD_SCHEMA = "hall_pairing_pushforward_compatibility.v1"
TRANSITION_RADICAL_STATUS = "TRANSITION_RADICAL_PRESERVATION_OBSTRUCTION_VERIFIED"
PAIRING_KERNEL_LIM1_STATUS = "PAIRING_KERNEL_LIM1_VANISHING_OBSTRUCTION_VERIFIED"
TRANSITION_ORIENTATION_STATUS = "TRANSITION_ORIENTATION_PRESERVATION_OBSTRUCTION_VERIFIED"

EXPECTED_COVERAGE = {
    "criterion_count": 1,
    "source_product_rows": 0,
    "source_coproduct_rows": 0,
    "source_bracket_rows": 0,
    "source_bialgebra_identity_rows": 0,
    "source_pairing_rows": 0,
    "source_hopf_pairing_identity_rows": 0,
    "source_radical_rows": 0,
    "source_quotient_splitting_rows": 0,
    "radical_ideal_coideal_rows": 0,
    "chevalley_antiinvolution_rows": 0,
    "transition_radical_pairing_rows": 0,
    "pairing_kernel_ml_rows": 0,
    "orientation_transition_rows": 0,
    "frobenius_pairing_rows": 0,
    "row336_trace_degree_claim": 0,
    "row337_serre_sign_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "source_hall_product",
    "source_hall_coproduct",
    "source_bialgebra_identities",
    "source_hopf_pairing_matrix",
    "hopf_adjointness_identity",
    "frobenius_cyclic_identity",
    "quotient_nondegeneracy_identity",
    "radical_kernel_rows",
    "quotient_splitting_rows",
    "radical_ideal_coideal",
    "chevalley_antiinvolution_source_map",
    "orientation_pairing_line",
    "thom_sebastiani_cyclic_signs",
    "serre_sign_line",
    "transition_radical_preservation",
    "pairing_kernel_lim1_vanishing",
    "orientation_transition_compatibility",
    "source_trace_functional",
    "row336_trace_degree",
    "row337_serre_signs",
}

REQUIRED_FIREWALL = {
    "formal_pairing_pushforward",
    "target_negative_dual_formal_block",
    "row334_Chevalley_criterion",
    "compact_Hall_empty_ledger",
    "empty_M_entries",
    "empty_D_entries",
    "empty_B_entries",
    "empty_G_entries",
    "empty_hopf_pairing_identities",
    "empty_K_entries",
    "determinant_line_only",
    "square_root_obstruction_ledger",
    "transition_radical_obstruction_only",
    "pairing_kernel_lim1_obstruction_only",
    "scalar_trace",
    "protected_trace",
    "pfaffian_product",
    "denominator_product",
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
            "chevalley_antiinvolution_required",
            "source_product_required",
            "source_coproduct_required",
            "source_bialgebra_identities_required",
            "source_hopf_pairing_required",
            "hopf_adjointness_required",
            "frobenius_cyclic_required",
            "quotient_nondegeneracy_required",
            "radical_quotient_required",
            "orientation_line_pairing_required",
            "orientation_cyclic_signs_required",
            "transition_compatibility_required",
            "pairing_kernel_lim1_required",
            "formal_pairing_pushforward_as_frobenius_allowed",
            "target_pairing_as_frobenius_allowed",
            "scalar_trace_as_frobenius_allowed",
            "criterion_recorded",
            "frobenius_pairing_proved",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "frobenius_pairing_rows.csv",
        (
            "frobenius_row_id",
            "R_id",
            "stratum_id",
            "degree_tuple_id",
            "left_degree_id",
            "right_degree_id",
            "product_matrix_id",
            "coproduct_matrix_id",
            "bracket_matrix_id",
            "pairing_matrix_id",
            "hopf_adjointness_check_id",
            "frobenius_cyclic_check_id",
            "quotient_nondegeneracy_check_id",
            "radical_quotient_id",
            "orientation_pairing_line_id",
            "orientation_cyclic_square_id",
            "chevalley_antiinvolution_row_id",
            "transition_row_id",
            "pairing_kernel_ml_row_id",
            "hopf_adjointness_defect_rank",
            "frobenius_cyclic_defect_rank",
            "quotient_nondegeneracy_defect_rank",
            "orientation_cyclic_defect_rank",
            "frobenius_verified",
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
        "chevalley_antiinvolution_imported",
        "compact_hall_ledger_imported",
        "hall_pairing_pushforward_imported",
        "transition_radical_ledger_imported",
        "pairing_kernel_lim1_ledger_imported",
        "transition_orientation_ledger_imported",
        "frobenius_pairing_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "source_product_rows_supplied",
        "source_coproduct_rows_supplied",
        "source_bialgebra_identity_rows_supplied",
        "source_pairing_rows_supplied",
        "hopf_adjointness_rows_supplied",
        "frobenius_cyclic_rows_supplied",
        "quotient_nondegeneracy_rows_supplied",
        "source_radical_rows_supplied",
        "quotient_splitting_rows_supplied",
        "radical_ideal_coideal_rows_supplied",
        "orientation_pairing_rows_supplied",
        "orientation_cyclic_sign_rows_supplied",
        "serre_sign_line_rows_supplied",
        "transition_radical_rows_supplied",
        "pairing_kernel_lim1_rows_supplied",
        "orientation_transition_rows_supplied",
        "frobenius_pairing_proved",
        "row336_trace_degree_claimed",
        "row337_serre_sign_claimed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(ROW334_FIXTURE),
            str(COMPACT_HALL_FIXTURE),
            str(PAIRING_PUSHFORWARD_FIXTURE),
            str(TRANSITION_RADICAL_FIXTURE),
            str(PAIRING_KERNEL_LIM1_FIXTURE),
            str(TRANSITION_ORIENTATION_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> None:
    row334 = read_json(ROW334_FIXTURE / "manifest.json")
    require_equal(row334.get("status"), ROW334_STATUS, "row334 status")
    require_equal(row334.get("chevalley_antiinvolution_constructed"), False, "row334 constructed")
    require_equal(row334.get("row335_frobenius_claimed"), False, "row334 Frobenius flag")
    require_empty_csv(ROW334_FIXTURE / "chevalley_antiinvolution_rows.csv")

    compact = read_json(COMPACT_HALL_FIXTURE / "manifest.json")
    require_equal(compact.get("obstruction_ledger_status"), COMPACT_HALL_STATUS, "compact Hall status")
    require_equal(compact.get("empty_blocked"), True, "compact Hall empty")
    for table in (
        "M_entries.csv",
        "D_entries.csv",
        "B_entries.csv",
        "G_entries.csv",
        "K_entries.csv",
        "Q_entries.csv",
        "hall_bialgebra_identities.csv",
        "hopf_pairing_identities.csv",
        "radical_ideal_coideal.csv",
        "unit_counit.csv",
    ):
        require_empty_csv(COMPACT_HALL_FIXTURE / table)

    pairing_pushforward = read_json(PAIRING_PUSHFORWARD_FIXTURE / "manifest.json")
    require_equal(pairing_pushforward.get("schema_version"), PAIRING_PUSHFORWARD_SCHEMA, "pairing pushforward schema")
    require_equal(pairing_pushforward.get("certified"), True, "pairing pushforward certified")
    require_equal(pairing_pushforward.get("compact_hall_correspondence"), False, "pairing compact Hall")
    require_equal(pairing_pushforward.get("hopf_adjointness"), False, "pairing Hopf adjointness")
    require_equal(pairing_pushforward.get("frobenius_cyclic_identity"), False, "pairing Frobenius")
    require_equal(pairing_pushforward.get("quotient_nondegeneracy"), False, "pairing quotient nondegeneracy")

    transition_radical = read_json(TRANSITION_RADICAL_FIXTURE / "manifest.json")
    require_equal(transition_radical.get("status"), TRANSITION_RADICAL_STATUS, "transition radical status")
    require_equal(transition_radical.get("radical_transition_certification"), False, "transition radical certification")
    for table in (
        "pairing_transition.csv",
        "radical_kernel_rows.csv",
        "radical_transition_matrices.csv",
        "quotient_transition_matrices.csv",
        "transition_defects.csv",
    ):
        require_empty_csv(TRANSITION_RADICAL_FIXTURE / table)

    pairing_kernel = read_json(PAIRING_KERNEL_LIM1_FIXTURE / "manifest.json")
    require_equal(pairing_kernel.get("status"), PAIRING_KERNEL_LIM1_STATUS, "pairing kernel status")
    require_equal(pairing_kernel.get("lim1_vanishing_certification"), False, "pairing kernel lim1 certification")
    for table in (
        "pairing_maps.csv",
        "pairing_kernel_spaces.csv",
        "pairing_kernel_transition_maps.csv",
        "pairing_kernel_image_stabilization.csv",
        "pairing_kernel_ml_r1lim_defects.csv",
        "pairing_kernel_coverage.csv",
    ):
        require_empty_csv(PAIRING_KERNEL_LIM1_FIXTURE / table)

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
            "chevalley_antiinvolution",
            "compact_hall_source",
            "hall_pairing_pushforward",
            "transition_radical",
            "pairing_kernel_lim1",
            "transition_orientation",
        },
        "source ids",
    )
    for row in indexed.values():
        check_verified(row, "source_rows.csv")


def verify_criterion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "criterion row count")
    row = rows[0]
    require_equal(row["criterion_id"], "orientation_frobenius_pairing", "criterion id")
    for key in (
        "chevalley_antiinvolution_required",
        "source_product_required",
        "source_coproduct_required",
        "source_bialgebra_identities_required",
        "source_hopf_pairing_required",
        "hopf_adjointness_required",
        "frobenius_cyclic_required",
        "quotient_nondegeneracy_required",
        "radical_quotient_required",
        "orientation_line_pairing_required",
        "orientation_cyclic_signs_required",
        "transition_compatibility_required",
        "pairing_kernel_lim1_required",
        "criterion_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    for key in (
        "formal_pairing_pushforward_as_frobenius_allowed",
        "target_pairing_as_frobenius_allowed",
        "scalar_trace_as_frobenius_allowed",
        "frobenius_pairing_proved",
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
    require_equal(tables["frobenius_pairing_rows.csv"], [], "Frobenius pairing rows")
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
