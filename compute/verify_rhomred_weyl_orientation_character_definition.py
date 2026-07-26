#!/usr/bin/env python3
"""Verify row-319 orientation character definition packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_weyl_orientation_character_definition_obstruction.v1"
EXPECTED_KIND = "rhomred_weyl_orientation_character_definition_obstruction"
SUCCESS_STATUS = "RHOMRED_WEYL_ORIENTATION_CHARACTER_DEFINITION_OBSTRUCTION_VERIFIED"
PROOF_LABEL = "def:orientation-character-epsilon-o"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_weyl_orientation_character_definition")

COCHAIN_TRANSITION_FIXTURE = Path(
    "certificates/orientation/rhomred_weyl_orientation_cocycle_cochain_transition"
)
TORSOR_VANISHING_FIXTURE = Path(
    "certificates/orientation/rhomred_weyl_orientation_torsor_defect_vanishing"
)
ALPHA_RED_FIXTURE = Path("certificates/orientation/rhomred_weyl_alpha_red_preservation")
ALPHA_E_FIXTURE = Path("certificates/orientation/rhomred_weyl_alpha_e_free_preservation")
BETA_FIXTURE = Path("certificates/orientation/rhomred_weyl_finite_stabilizer_beta_preservation")
LAMBDA_FIXTURE = Path(
    "certificates/orientation/rhomred_weyl_finite_stabilizer_lambda_zero_preservation"
)
MAASS_FIXTURE = Path("certificates/automorphic/delta5_maass_character")

COCHAIN_TRANSITION_STATUS = "RHOMRED_WEYL_ORIENTATION_COCYCLE_COCHAIN_TRANSITION_OBSTRUCTION_VERIFIED"
TORSOR_VANISHING_STATUS = "RHOMRED_WEYL_ORIENTATION_TORSOR_DEFECT_VANISHING_OBSTRUCTION_VERIFIED"
ALPHA_RED_STATUS = "RHOMRED_WEYL_ALPHA_RED_PRESERVATION_OBSTRUCTION_VERIFIED"
ALPHA_E_STATUS = "RHOMRED_WEYL_ALPHA_E_FREE_PRESERVATION_OBSTRUCTION_VERIFIED"
BETA_STATUS = "RHOMRED_WEYL_FINITE_STABILIZER_BETA_PRESERVATION_OBSTRUCTION_VERIFIED"
LAMBDA_STATUS = "RHOMRED_WEYL_FINITE_STABILIZER_LAMBDA_ZERO_PRESERVATION_OBSTRUCTION_VERIFIED"
MAASS_SCHEMA = "delta5_maass_character.v1"

EXPECTED_COVERAGE = {
    "definition_count": 1,
    "row312_cochain_transition_claim": 0,
    "row314_torsor_vanishing_claim": 0,
    "row315_alpha_red_preservation_claim": 0,
    "row316_alpha_e_free_preservation_claim": 0,
    "row317_beta_preservation_claim": 0,
    "row318_lambda_zero_preservation_claim": 0,
    "maass_orientation_character_claim": 0,
    "generator_sign_rows": 0,
    "character_rows": 0,
    "orientation_character_constructed_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "strict_weyl_action_rows",
    "cochain_transition_compatibility",
    "torsor_defect_vanishing",
    "alpha_red_preservation",
    "alpha_e_free_preservation",
    "beta_preservation",
    "lambda_zero_preservation",
    "generator_sign_rows",
    "stratum_independence",
    "transition_compatibility",
    "inverse_limit_character",
    "row320_sign_computation",
    "maass_comparison_separation",
}

REQUIRED_FIREWALL = {
    "maass_character_value",
    "automorphic_character_certified",
    "determinant_character",
    "target_coxeter_graph",
    "target_no_braid_presentation",
    "tau_square_relation",
    "local_pfaffian_sign_without_transport",
    "OP_scalar_branch",
    "scalar_trace",
    "squared_determinant",
    "row320_sign_value",
    "row321_det_comparison",
    "row322_maass_comparison",
    "empty_generator_sign_table",
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
            "strict_weyl_action_required",
            "cochain_transition_required",
            "torsor_defect_vanishing_required",
            "component_preservation_required",
            "generator_sign_rows_required",
            "stratum_independence_required",
            "transition_compatibility_required",
            "coxeter_presentation_required",
            "maass_character_source_allowed",
            "definition_recorded",
            "orientation_character_constructed",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "generator_sign_rows.csv",
        (
            "sign_id",
            "R_id",
            "stratum_id",
            "delta_id",
            "w_label",
            "tau_row_id",
            "orientation_line_row_id",
            "normal_pfaffian_unit_id",
            "sign_value",
            "stratum_independence_row_id",
            "transition_compatibility_row_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
        allow_empty=True,
    ),
    TableSpec(
        "character_rows.csv",
        (
            "character_id",
            "R_id",
            "group_id",
            "coxeter_presentation_id",
            "generator_sign_ids",
            "word_evaluation_rule",
            "homomorphism_verified",
            "transition_compatible",
            "inverse_limit_compatible",
            "epsilon_o_defined",
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


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
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
        "cochain_transition_imported",
        "torsor_defect_vanishing_imported",
        "alpha_red_preservation_imported",
        "alpha_e_free_preservation_imported",
        "beta_preservation_imported",
        "lambda_zero_preservation_imported",
        "maass_character_firewall_imported",
        "definition_criterion_recorded",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "strict_weyl_action_rows_supplied",
        "orientation_line_automorphism_rows_supplied",
        "generator_sign_rows_supplied",
        "stratum_independence_rows_supplied",
        "transition_compatibility_rows_supplied",
        "finite_stage_character_rows_supplied",
        "inverse_limit_character_rows_supplied",
        "orientation_character_constructed",
        "mathematical_certification",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {
            str(COCHAIN_TRANSITION_FIXTURE),
            str(TORSOR_VANISHING_FIXTURE),
            str(ALPHA_RED_FIXTURE),
            str(ALPHA_E_FIXTURE),
            str(BETA_FIXTURE),
            str(LAMBDA_FIXTURE),
            str(MAASS_FIXTURE),
        },
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")
    return manifest


def verify_imports() -> dict[str, int]:
    cochain_manifest = read_json(COCHAIN_TRANSITION_FIXTURE / "manifest.json")
    require_equal(cochain_manifest.get("status"), COCHAIN_TRANSITION_STATUS, "cochain status")
    require_equal(
        cochain_manifest.get("cochain_transition_compatibility_proved"),
        False,
        "cochain transition compatibility",
    )

    torsor_manifest = read_json(TORSOR_VANISHING_FIXTURE / "manifest.json")
    require_equal(torsor_manifest.get("status"), TORSOR_VANISHING_STATUS, "torsor status")
    require_equal(
        torsor_manifest.get("all_torsor_defects_vanishing_proved"),
        False,
        "torsor defect vanishing",
    )

    alpha_red_manifest = read_json(ALPHA_RED_FIXTURE / "manifest.json")
    require_equal(alpha_red_manifest.get("status"), ALPHA_RED_STATUS, "alpha red status")
    require_equal(
        alpha_red_manifest.get("alpha_red_preservation_proved"),
        False,
        "alpha red preservation",
    )

    alpha_e_manifest = read_json(ALPHA_E_FIXTURE / "manifest.json")
    require_equal(alpha_e_manifest.get("status"), ALPHA_E_STATUS, "alpha E status")
    require_equal(
        alpha_e_manifest.get("alpha_e_free_preservation_proved"),
        False,
        "alpha E preservation",
    )

    beta_manifest = read_json(BETA_FIXTURE / "manifest.json")
    require_equal(beta_manifest.get("status"), BETA_STATUS, "beta status")
    require_equal(
        beta_manifest.get("finite_stabilizer_beta_preservation_proved"),
        False,
        "beta preservation",
    )

    lambda_manifest = read_json(LAMBDA_FIXTURE / "manifest.json")
    require_equal(lambda_manifest.get("status"), LAMBDA_STATUS, "lambda status")
    require_equal(
        lambda_manifest.get("lambda_zero_preservation_proved"),
        False,
        "lambda zero preservation",
    )

    maass_manifest = read_json(MAASS_FIXTURE / "manifest.json")
    require_equal(maass_manifest.get("schema_version"), MAASS_SCHEMA, "Maass schema")
    require_equal(maass_manifest.get("automorphic_character_certified"), True, "Maass certified")
    require_equal(maass_manifest.get("orientation_character"), False, "Maass orientation firewall")
    require_equal(maass_manifest.get("pfaffian_line"), False, "Maass Pfaffian firewall")
    require_equal(maass_manifest.get("compact_source"), False, "Maass compact source firewall")

    return {
        "row312_cochain_transition_claim": int(
            bool(cochain_manifest.get("cochain_transition_compatibility_proved"))
        ),
        "row314_torsor_vanishing_claim": int(
            bool(torsor_manifest.get("all_torsor_defects_vanishing_proved"))
        ),
        "row315_alpha_red_preservation_claim": int(
            bool(alpha_red_manifest.get("alpha_red_preservation_proved"))
        ),
        "row316_alpha_e_free_preservation_claim": int(
            bool(alpha_e_manifest.get("alpha_e_free_preservation_proved"))
        ),
        "row317_beta_preservation_claim": int(
            bool(beta_manifest.get("finite_stabilizer_beta_preservation_proved"))
        ),
        "row318_lambda_zero_preservation_claim": int(
            bool(lambda_manifest.get("lambda_zero_preservation_proved"))
        ),
        "maass_orientation_character_claim": int(bool(maass_manifest.get("orientation_character"))),
    }


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    expected = {
        "cochain_transition": COCHAIN_TRANSITION_STATUS,
        "torsor_defect_vanishing": TORSOR_VANISHING_STATUS,
        "alpha_red_preservation": ALPHA_RED_STATUS,
        "alpha_e_free_preservation": ALPHA_E_STATUS,
        "beta_preservation": BETA_STATUS,
        "lambda_zero_preservation": LAMBDA_STATUS,
        "maass_character_firewall": MAASS_SCHEMA,
        "optimization_row": "row_319",
    }
    require_equal(set(rows), set(expected), "source ids")
    for source_id, status in expected.items():
        require_equal(rows[source_id]["source_status"], status, f"{source_id} status")
    for row in rows.values():
        check_verified(row, "source_rows.csv")


def verify_definition(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["definition_rows.csv"], "definition_id", "definition rows")
    expected_id = "orientation_character_word_evaluation"
    require_equal(set(rows), {expected_id}, "definition ids")
    row = rows[expected_id]
    check_verified(row, "definition_rows.csv")
    for key in (
        "strict_weyl_action_required",
        "cochain_transition_required",
        "torsor_defect_vanishing_required",
        "component_preservation_required",
        "generator_sign_rows_required",
        "stratum_independence_required",
        "transition_compatibility_required",
        "coxeter_presentation_required",
        "definition_recorded",
    ):
        require_equal(bool_cell(row, key), True, key)
    require_equal(bool_cell(row, "maass_character_source_allowed"), False, "Maass as source")
    require_equal(
        bool_cell(row, "orientation_character_constructed"),
        False,
        "orientation character constructed",
    )


def verify_empty_tables(tables: dict[str, list[dict[str, str]]]) -> None:
    for table_name in ("generator_sign_rows.csv", "character_rows.csv"):
        if tables[table_name]:
            raise ValueError(f"{table_name} must remain empty in obstruction packet")


def verify_coverage(
    manifest: dict,
    tables: dict[str, list[dict[str, str]]],
    counts: dict[str, int],
) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    computed = dict(EXPECTED_COVERAGE)
    computed.update(counts)
    computed["generator_sign_rows"] = len(tables["generator_sign_rows.csv"])
    computed["character_rows"] = len(tables["character_rows.csv"])
    computed["orientation_character_constructed_claim"] = int(
        bool(manifest.get("orientation_character_constructed"))
    )
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        require_equal(row["check_status"], "verified", f"{coverage_id} check")
        require_equal(
            int_cell(row, "computed_value"),
            computed[coverage_id],
            f"{coverage_id} computed",
        )
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        require_equal(
            row["definition_status"],
            "missing_open_obligation",
            f"{row['obligation_id']} status",
        )
        require_equal(row["check_status"], "verified", f"{row['obligation_id']} check")
        if not row["mathematical_payload"] or not row["why_required"]:
            raise ValueError(f"{row['obligation_id']}: missing payload or reason")


def verify_firewall(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["scalar_firewall.csv"], "forbidden_substitute", "scalar firewall")
    require_equal(set(rows), REQUIRED_FIREWALL, "scalar firewall")
    for row in rows.values():
        check_verified(row, "scalar_firewall.csv")
        require_equal(bool_cell(row, "excluded"), True, f"{row['forbidden_substitute']} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['forbidden_substitute']} defect")


def verify_fixture(fixture: Path) -> None:
    if not fixture.is_dir():
        raise ValueError(f"fixture is not a directory: {fixture}")
    manifest = verify_manifest(fixture)
    counts = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    verify_definition(tables)
    verify_empty_tables(tables)
    verify_coverage(manifest, tables, counts)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_WEYL_ORIENTATION_CHARACTER_DEFINITION_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
