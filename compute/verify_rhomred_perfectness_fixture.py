#!/usr/bin/env python3
"""Verify perfectness of the cosection-reduced self-Ext cone."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


EXPECTED_SCHEMA = "rhomred_perfectness.v1"
EXPECTED_KIND = "rhomred_perfectness_input"
SUCCESS_STATUS = "RHOMRED_PERFECTNESS_VERIFIED"
PROOF_LABEL = "prop:rhomred-perfectness"
DEFAULT_FIXTURE = Path("certificates/orientation/rhomred_perfectness")
RHOMRED_FIXTURE = Path("certificates/orientation/rhomred_definition")
UNIVERSAL_FIXTURE = Path("certificates/moduli/retained_universal_complexes")
DERIVED_FIXTURE = Path("certificates/moduli/retained_derived_enhancements")
RHOMRED_STATUS = "RHOMRED_DEFINITION_VERIFIED"
UNIVERSAL_STATUS = "RETAINED_UNIVERSAL_COMPLEXES_VERIFIED"
DERIVED_STATUS = "RETAINED_DERIVED_ENHANCEMENTS_VERIFIED"
THEOREM_TAG = "StacksProject_Tag_0685_Lemma_37_61_13"

EXPECTED_ROWS = {
    "perfect_R0_s3": ("rhomred_R0_s3", "Univ_R0_s3", "Mss_R0_s3", "DerStack_R0_s3"),
    "perfect_R0_s2": ("rhomred_R0_s2", "Univ_R0_s2", "Mss_R0_s2", "DerStack_R0_s2"),
    "perfect_R0_s1": ("rhomred_R0_s1", "Univ_R0_s1", "Mss_R0_s1", "DerStack_R0_s1"),
}

EXPECTED_COVERAGE = {
    "perfectness_row_count": 3,
    "input_perfect_count": 3,
    "target_perfect_count": 3,
    "perfectness_defects": 0,
    "surjectivity_claim": 0,
    "determinant_claim": 0,
    "orientation_claim": 0,
    "protected_integration_claim": 0,
}

REQUIRED_OBLIGATIONS = {
    "cosection_surjectivity",
    "det_rhom_red",
    "orientation_square_root",
    "quotient_orientation",
    "transition_compatibility",
    "vanishing_cycle_complex",
    "protected_integration",
}
SUPPLIED_BY_ROW_277 = {"det_rhom_red"}

REQUIRED_FIREWALL = {
    "PTVV_form_only",
    "universal_perfect_complex_only",
    "cone_definition_only",
    "cosection_surjectivity",
    "det_RHomred",
    "orientation_square_root",
    "scalar_trace",
    "protected_integration",
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
        "input_complex_rows.csv",
        (
            "input_id",
            "rhomred_id",
            "universal_id",
            "substack_id",
            "derived_stack_id",
            "perfect_complex_id",
            "universal_tor_amplitude",
            "universal_perfection_defect_rank",
            "proper_smooth_projection",
            "source_perfect",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "target_complex_rows.csv",
        (
            "target_id",
            "rhomred_id",
            "trace_target_id",
            "cosection_target_id",
            "target_complex_id",
            "rgamma_ox_total_rank",
            "h2_s_os_rank",
            "target_perfect",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "perfectness_rows.csv",
        (
            "perfectness_id",
            "rhomred_id",
            "substack_id",
            "derived_stack_id",
            "input_id",
            "target_id",
            "theta_map_id",
            "input_perfect",
            "target_perfect",
            "fibre_closure",
            "theorem_tag",
            "perfectness_defect_rank",
            "cosection_surjectivity_required_for_cone",
            "cosection_surjectivity_supplied",
            "determinant_defined",
            "orientation_constructed",
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
            "perfectness_status",
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

RHOMRED_COLUMNS = (
    "rhomred_id",
    "cosection_id",
    "substack_id",
    "derived_stack_id",
    "input_complex_id",
    "theta_map_id",
    "trace_target_id",
    "cosection_target_id",
    "cone_formula_id",
    "cone_shift",
    "definition_defect_rank",
    "surjectivity_required",
    "surjectivity_supplied",
    "perfectness_proved",
    "determinant_defined",
    "proof_reference",
    "check_status",
    "notes",
)

UNIVERSAL_COLUMNS = (
    "universal_id",
    "substack_id",
    "perfect_complex_id",
    "base_change_id",
    "tor_amplitude",
    "descent_defect_rank",
    "perfection_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)

DERIVED_COLUMNS = (
    "enhancement_id",
    "substack_id",
    "derived_stack_id",
    "shifted_symplectic_form_id",
    "quasi_smooth_status",
    "cotangent_amplitude",
    "tor_amplitude_defect_rank",
    "symplectic_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing json file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_table_path(path: Path, columns: tuple[str, ...]) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != columns:
            raise ValueError(
                f"{path}: expected columns {columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
        raise ValueError(f"{path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{path}: unparsed CSV fields in row {row}")
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
    value = row[key].strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def check_verified(row: dict[str, str], table_name: str, proof_required: bool = True) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if proof_required and PROOF_LABEL not in row.get("proof_reference", ""):
        raise ValueError(f"{table_name}: proof reference does not cite {PROOF_LABEL}: {row}")


def rows_by(rows: list[dict[str, str]], key: str, table_name: str) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in indexed:
            raise ValueError(f"{table_name}: duplicate {key} {value}")
        indexed[value] = row
    return indexed


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), fixture.name, "fixture_name")
    require_equal(manifest.get("orientation_kind"), EXPECTED_KIND, "orientation_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    for key in (
        "rhomred_definition_imported",
        "retained_universal_complexes_imported",
        "retained_derived_enhancements_imported",
        "proper_perfect_pushforward_theorem_imported",
        "perfect_source_complexes",
        "perfect_target_complexes",
        "perfect_cones",
        "three_substacks_verified",
        "perfectness_defect_zero",
    ):
        require_equal(manifest.get(key), True, key)
    for key in (
        "cosection_surjectivity_proved",
        "det_rhom_red",
        "orientation_square_root",
        "quotient_orientation",
        "transition_compatibility",
        "vanishing_cycle_complex",
        "protected_integration",
    ):
        require_equal(manifest.get(key), False, key)
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "tables")
    require_equal(
        set(manifest.get("imports", [])),
        {str(RHOMRED_FIXTURE), str(UNIVERSAL_FIXTURE), str(DERIVED_FIXTURE)},
        "imports",
    )
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError("missing nonempty README")


def verify_imports() -> tuple[
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
    dict[str, dict[str, str]],
]:
    rhomred_manifest = read_json(RHOMRED_FIXTURE / "manifest.json")
    require_equal(rhomred_manifest.get("status"), RHOMRED_STATUS, "rhomred status")
    universal_manifest = read_json(UNIVERSAL_FIXTURE / "manifest.json")
    require_equal(universal_manifest.get("certified"), True, "universal certified")
    require_equal(universal_manifest.get("universal_complexes"), True, "universal complexes")
    require_equal(universal_manifest.get("perfection_defects_zero"), True, "universal perfection defects")
    derived_manifest = read_json(DERIVED_FIXTURE / "manifest.json")
    require_equal(derived_manifest.get("certified"), True, "derived certified")
    require_equal(derived_manifest.get("quasi_smooth_derived_enhancements"), True, "derived enhancements")

    rhomred = rows_by(
        read_table_path(RHOMRED_FIXTURE / "rhomred_rows.csv", RHOMRED_COLUMNS),
        "rhomred_id",
        "imported rhomred rows",
    )
    universal = rows_by(
        read_table_path(UNIVERSAL_FIXTURE / "universal_complexes.csv", UNIVERSAL_COLUMNS),
        "universal_id",
        "imported universal rows",
    )
    derived = rows_by(
        read_table_path(DERIVED_FIXTURE / "derived_enhancements.csv", DERIVED_COLUMNS),
        "substack_id",
        "imported derived rows",
    )
    return rhomred, universal, derived


def verify_sources(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["source_rows.csv"], "source_id", "source rows")
    require_equal(
        set(rows),
        {
            "rhomred_definition",
            "retained_universal_complexes",
            "retained_derived_enhancements",
            "proper_perfect_pushforward",
        },
        "source ids",
    )
    require_equal(rows["rhomred_definition"]["source_status"], RHOMRED_STATUS, "rhomred source status")
    require_equal(rows["retained_universal_complexes"]["source_status"], UNIVERSAL_STATUS, "universal source status")
    require_equal(rows["retained_derived_enhancements"]["source_status"], DERIVED_STATUS, "derived source status")
    require_equal(rows["proper_perfect_pushforward"]["source_path_or_key"], THEOREM_TAG, "perfect pushforward tag")
    for row in rows.values():
        check_verified(row, "source_rows.csv", proof_required=False)


def verify_input_rows(
    tables: dict[str, list[dict[str, str]]],
    rhomred_rows: dict[str, dict[str, str]],
    universal_rows: dict[str, dict[str, str]],
    derived_rows: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    rows = rows_by(tables["input_complex_rows.csv"], "input_id", "input rows")
    require_equal({f"input_R0_{suffix}" for suffix in ("s3", "s2", "s1")}, set(rows), "input ids")
    for perfectness_id, (rhomred_id, universal_id, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        input_id = perfectness_id.replace("perfect", "input")
        row = rows[input_id]
        check_verified(row, "input_complex_rows.csv")
        rhomred = rhomred_rows[rhomred_id]
        universal = universal_rows[universal_id]
        derived = derived_rows[substack_id]
        require_equal(row["rhomred_id"], rhomred_id, f"{input_id} rhomred")
        require_equal(row["universal_id"], universal_id, f"{input_id} universal")
        require_equal(row["substack_id"], substack_id, f"{input_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{input_id} derived stack")
        require_equal(rhomred["substack_id"], substack_id, f"{rhomred_id} substack")
        require_equal(universal["substack_id"], substack_id, f"{universal_id} substack")
        require_equal(derived["derived_stack_id"], derived_stack_id, f"{substack_id} derived")
        require_equal(row["perfect_complex_id"], universal["perfect_complex_id"], f"{input_id} perfect complex")
        require_equal(row["universal_tor_amplitude"], universal["tor_amplitude"], f"{input_id} Tor amplitude")
        require_equal(int_cell(row, "universal_perfection_defect_rank"), 0, f"{input_id} perfection defect")
        require_equal(int_cell(universal, "perfection_defect_rank"), 0, f"{universal_id} perfection defect")
        require_equal(bool_cell(row, "proper_smooth_projection"), True, f"{input_id} proper projection")
        require_equal(bool_cell(row, "source_perfect"), True, f"{input_id} source perfect")
    return rows


def verify_target_rows(tables: dict[str, list[dict[str, str]]]) -> dict[str, dict[str, str]]:
    rows = rows_by(tables["target_complex_rows.csv"], "target_id", "target rows")
    require_equal({f"target_R0_{suffix}" for suffix in ("s3", "s2", "s1")}, set(rows), "target ids")
    for perfectness_id, (rhomred_id, _, _, _) in EXPECTED_ROWS.items():
        target_id = perfectness_id.replace("perfect", "target")
        row = rows[target_id]
        check_verified(row, "target_complex_rows.csv")
        require_equal(row["rhomred_id"], rhomred_id, f"{target_id} rhomred")
        require_equal(row["trace_target_id"], "RGamma_X_OX", f"{target_id} trace target")
        require_equal(row["cosection_target_id"], "H2_S_OS_shift_minus1", f"{target_id} cosection target")
        require_equal(row["target_complex_id"], "RGamma_X_OX_plus_H2_S_OS_shift_minus1", f"{target_id} target")
        require_equal(int_cell(row, "rgamma_ox_total_rank"), 4, f"{target_id} RGamma rank")
        require_equal(int_cell(row, "h2_s_os_rank"), 1, f"{target_id} H2 rank")
        require_equal(bool_cell(row, "target_perfect"), True, f"{target_id} target perfect")
    return rows


def verify_perfectness_rows(
    tables: dict[str, list[dict[str, str]]],
    rhomred_rows: dict[str, dict[str, str]],
    input_rows: dict[str, dict[str, str]],
    target_rows: dict[str, dict[str, str]],
) -> None:
    rows = rows_by(tables["perfectness_rows.csv"], "perfectness_id", "perfectness rows")
    require_equal(set(rows), set(EXPECTED_ROWS), "perfectness ids")
    for perfectness_id, (rhomred_id, _, substack_id, derived_stack_id) in EXPECTED_ROWS.items():
        row = rows[perfectness_id]
        check_verified(row, "perfectness_rows.csv")
        input_id = perfectness_id.replace("perfect", "input")
        target_id = perfectness_id.replace("perfect", "target")
        rhomred = rhomred_rows[rhomred_id]
        require_equal(row["rhomred_id"], rhomred_id, f"{perfectness_id} rhomred")
        require_equal(row["substack_id"], substack_id, f"{perfectness_id} substack")
        require_equal(row["derived_stack_id"], derived_stack_id, f"{perfectness_id} derived")
        require_equal(row["input_id"], input_id, f"{perfectness_id} input id")
        require_equal(row["target_id"], target_id, f"{perfectness_id} target id")
        require_equal(input_rows[input_id]["rhomred_id"], rhomred_id, f"{input_id} rhomred")
        require_equal(target_rows[target_id]["rhomred_id"], rhomred_id, f"{target_id} rhomred")
        require_equal(row["theta_map_id"], rhomred["theta_map_id"], f"{perfectness_id} theta")
        require_equal(bool_cell(row, "input_perfect"), True, f"{perfectness_id} input perfect")
        require_equal(bool_cell(row, "target_perfect"), True, f"{perfectness_id} target perfect")
        require_equal(bool_cell(row, "fibre_closure"), True, f"{perfectness_id} fibre closure")
        require_equal(row["theorem_tag"], THEOREM_TAG, f"{perfectness_id} theorem tag")
        require_equal(int_cell(row, "perfectness_defect_rank"), 0, f"{perfectness_id} defect")
        require_equal(bool_cell(row, "cosection_surjectivity_required_for_cone"), False, f"{perfectness_id} surjectivity required")
        require_equal(bool_cell(row, "cosection_surjectivity_supplied"), False, f"{perfectness_id} surjectivity supplied")
        require_equal(bool_cell(row, "determinant_defined"), False, f"{perfectness_id} determinant")
        require_equal(bool_cell(row, "orientation_constructed"), False, f"{perfectness_id} orientation")


def verify_coverage(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["coverage_rows.csv"], "coverage_id", "coverage rows")
    require_equal(set(rows), set(EXPECTED_COVERAGE), "coverage ids")
    for coverage_id, expected in EXPECTED_COVERAGE.items():
        row = rows[coverage_id]
        check_verified(row, "coverage_rows.csv", proof_required=False)
        require_equal(int_cell(row, "computed_value"), expected, f"{coverage_id} computed")
        require_equal(int_cell(row, "expected_value"), expected, f"{coverage_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{coverage_id} defect")


def verify_obligations(tables: dict[str, list[dict[str, str]]]) -> None:
    rows = rows_by(tables["blocked_obligations.csv"], "obligation_id", "blocked obligations")
    require_equal(set(rows), REQUIRED_OBLIGATIONS, "blocked obligations")
    for row in rows.values():
        check_verified(row, "blocked_obligations.csv", proof_required=False)
        expected_status = (
            "supplied_by_rhomred_determinant"
            if row["obligation_id"] in SUPPLIED_BY_ROW_277
            else "missing_open_obligation"
        )
        require_equal(row["perfectness_status"], expected_status, f"{row['obligation_id']} status")


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
    verify_manifest(fixture)
    rhomred_rows, universal_rows, derived_rows = verify_imports()
    tables = {spec.path: read_table(fixture, spec) for spec in TABLE_SPECS}
    verify_sources(tables)
    input_rows = verify_input_rows(tables, rhomred_rows, universal_rows, derived_rows)
    target_rows = verify_target_rows(tables)
    verify_perfectness_rows(tables, rhomred_rows, input_rows, target_rows)
    verify_coverage(tables)
    verify_obligations(tables)
    verify_firewall(tables)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_fixture(args.fixture)
    except ValueError as exc:
        print(f"RHOMRED_PERFECTNESS_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
