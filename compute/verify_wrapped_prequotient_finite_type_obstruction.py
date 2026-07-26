#!/usr/bin/env python3
"""Verify the wrapped prequotient finite-type packet."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


SUCCESS_STATUS = "WRAPPED_PREQUOTIENT_FINITE_TYPE_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "wrapped_prequotient_finite_type.v1"
EXPECTED_KIND = "wrapped_prequotient_finite_type"
FINITE_TYPE_COLUMNS = (
    "finite_type_id",
    "R_id",
    "wrapped_colour_id",
    "prequotient_stack_id",
    "class_index_set",
    "semistable_source",
    "rigidification_source",
    "wrapped_locus_kind",
    "finite_type_status",
    "finite_type_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_FINITE_TYPE = {
    "finite_type_id": "wrapped_prequotient_ft_eta_R",
    "R_id": "R",
    "wrapped_colour_id": "eta_in_Gamma_R_wr",
    "prequotient_stack_id": "M_eta_R_wr_rig",
    "class_index_set": "C_R_eta_finite",
    "semistable_source": "retained_finite_type_semistable_substacks",
    "rigidification_source": "scalar_Gm_rigidification",
    "wrapped_locus_kind": "finite_union_of_retained_class_pieces",
    "finite_type_status": "finite_type_verified",
    "finite_type_defect_rank": "0",
    "check_status": "verified",
}
INPUT_COLUMNS = (
    "input_id",
    "class_fixture",
    "class_row_count",
    "semistable_fixture",
    "semistable_row_count",
    "rigidification_fixture",
    "rigidification_row_count",
    "all_classes_finite",
    "all_semistable_finite_type",
    "all_scalar_rigidifications_supplied",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_INPUT = {
    "input_id": "retained_finite_type_inputs",
    "class_fixture": "certificates/moduli/retained_class_bounds",
    "class_row_count": "3",
    "semistable_fixture": "certificates/moduli/retained_semistable_substacks",
    "semistable_row_count": "3",
    "rigidification_fixture": "certificates/moduli/retained_rigidification_inertia",
    "rigidification_row_count": "3",
    "all_classes_finite": "true",
    "all_semistable_finite_type": "true",
    "all_scalar_rigidifications_supplied": "true",
    "defect_rank": "0",
    "check_status": "verified",
}
RIGIDIFICATION_DESCENT_COLUMNS = (
    "descent_id",
    "source_stack",
    "group_scheme",
    "rigidified_stack",
    "descent_principle",
    "finite_type_preserved",
    "descent_defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
EXPECTED_RIGIDIFICATION_DESCENT = {
    "descent_id": "scalar_gm_rigidification_ft_descent",
    "source_stack": "Mss_R_c",
    "group_scheme": "G_m",
    "rigidified_stack": "M_R_c_rig",
    "descent_principle": "fppf_rigidification_descent",
    "finite_type_preserved": "true",
    "descent_defect_rank": "0",
    "check_status": "verified",
}
EMPTY_TABLES = {
    "properness_rows.csv": (
        "properness_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "properness_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_population_rows.csv": (
        "population_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "anchor_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "anchor_losslessness_rows.csv": (
        "losslessness_id",
        "R_id",
        "wrapped_colour_id",
        "prequotient_stack_id",
        "anchor_id",
        "anchor_loss_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "quotient_descent_rows.csv": (
        "descent_id",
        "R_id",
        "prequotient_stack_id",
        "quotient_stack_id",
        "descent_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "transition_rows.csv": (
        "transition_id",
        "from_R",
        "to_R",
        "prequotient_stack_id",
        "finite_type_compatibility_defect_rank",
        "descent_compatibility_defect_rank",
        "proof_reference",
        "check_status",
        "notes",
    ),
    "aggregate_population_rows.csv": (
        "population_id",
        "aggregate_fixture",
        "aggregate_table",
        "wrapped_row_id",
        "population_status",
        "proof_reference",
        "check_status",
        "notes",
    ),
}
OBLIGATION_COLUMNS = (
    "obligation_id",
    "lane",
    "required_artifact",
    "required_table",
    "required_row_type",
    "mathematical_payload",
    "why_required",
    "finite_type_status",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_OBLIGATIONS = frozenset(
    {
        "properness_rows",
        "anchor_population_rows",
        "anchor_losslessness_rows",
        "quotient_descent_rows",
        "transition_rows",
        "aggregate_population_rows",
    }
)
SCALAR_FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "prequotient_definition_only",
        "retained_class_set_only",
        "semistable_substack_only",
        "quotient_first",
        "properness_claim",
        "anchor_population",
        "anchor_losslessness",
        "scalar_trace",
        "Borcherds_s_degree",
        "empty_hybrid_carrier",
    }
)
CLASS_COLUMNS = (
    "class_id",
    "window_id",
    "type_id",
    "charge_id",
    "substack_id",
    "hilbert_polynomial_id",
    "amplitude_bounds",
    "regularity_bound",
    "retained_class",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
SEMISTABLE_COLUMNS = (
    "substack_id",
    "type_id",
    "stability_id",
    "ambient_stack_id",
    "quot_postnikov_chart_id",
    "finite_type_status",
    "specialization_closed",
    "semistability_defect_rank",
    "boundedness_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
RIGIDIFICATION_COLUMNS = (
    "rigidification_id",
    "substack_id",
    "automorphism_group_id",
    "scalar_gm_removed",
    "residual_inertia_finite",
    "rigidification_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)


@dataclass
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check wrapped prequotient finite-type packet."
    )
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/hybrid/wrapped_prequotient_finite_type"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def nonempty_rows(reader: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for row in reader:
        normalized = {
            key: (value or "").strip()
            for key, value in row.items()
            if key is not None
        }
        if any(normalized.values()):
            rows.append(normalized)
    return rows


def load_csv(path: Path, columns: tuple[str, ...], issues: list[str]) -> CsvTable:
    if not path.is_file():
        issues.append(f"missing table: {path}")
        return CsvTable(path, [])
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            issues.append(f"header mismatch in {path}; expected {','.join(columns)}")
        rows = nonempty_rows(reader)
    return CsvTable(path, rows)


def load_json(path: Path, issues: list[str]) -> dict[str, object]:
    if not path.is_file():
        issues.append(f"missing JSON file: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {path}")
        return {}
    return value


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "wrapped_prequotient_finite_type",
        "hybrid_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "finite_type_wrapped_prequotients": True,
        "prequotient_definition_imported": True,
        "finite_class_bounds_imported": True,
        "finite_type_semistable_substacks_imported": True,
        "scalar_rigidification_imported": True,
        "rigidification_finite_type_descent_used": True,
        "properness_certification": False,
        "anchor_population_certification": False,
        "anchor_losslessness_certification": False,
        "quotient_descent_certification": False,
        "transition_certification": False,
        "aggregate_hybrid_population": False,
        "quotient_first": False,
        "scalar_only": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    expected_tables = set(EMPTY_TABLES) | {
        "finite_type_rows.csv",
        "finite_type_input_rows.csv",
        "rigidification_descent_rows.csv",
        "blocked_obligations.csv",
        "scalar_firewall.csv",
    }
    if set(manifest.get("tables", [])) != expected_tables:
        issues.append("manifest tables do not match expected finite-type tables")
    expected_imports = {
        "certificates/hybrid/equivariant_wrapped_prequotient_definition",
        "certificates/moduli/retained_class_bounds",
        "certificates/moduli/retained_semistable_substacks",
        "certificates/moduli/retained_rigidification_inertia",
    }
    if set(manifest.get("imports", [])) != expected_imports:
        issues.append("manifest imports do not match expected finite-type imports")


def check_single_row(
    fixture: Path,
    table_name: str,
    columns: tuple[str, ...],
    expected: dict[str, str],
    issues: list[str],
) -> None:
    table = load_csv(fixture / table_name, columns, issues)
    if len(table.rows) != 1:
        issues.append(f"{table_name} must contain exactly one row")
        return
    row = table.rows[0]
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"{table_name} {key}: expected {value!r}, got {row.get(key)!r}")


def check_empty_tables(fixture: Path, issues: list[str]) -> None:
    for table_name, columns in EMPTY_TABLES.items():
        table = load_csv(fixture / table_name, columns, issues)
        if table.rows:
            issues.append(f"{table_name} must remain empty until later rows are supplied")


def check_obligations(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "blocked_obligations.csv", OBLIGATION_COLUMNS, issues)
    ids = {row.get("obligation_id", "") for row in table.rows}
    missing = sorted(REQUIRED_OBLIGATIONS - ids)
    extra = sorted(ids - REQUIRED_OBLIGATIONS)
    if missing:
        issues.append("missing obligation rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected obligation rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("finite_type_status") != "missing_open_obligation":
            issues.append(f"blocked_obligations.csv:{index} has non-missing status")
        if row.get("check_status") != "verified":
            issues.append(f"blocked_obligations.csv:{index} is not verified")
        if not row.get("mathematical_payload"):
            issues.append(f"blocked_obligations.csv:{index} lacks mathematical payload")


def check_firewall(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "scalar_firewall.csv", SCALAR_FIREWALL_COLUMNS, issues)
    substitutes = {row.get("forbidden_substitute", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_ROWS - substitutes)
    extra = sorted(substitutes - REQUIRED_FIREWALL_ROWS)
    if missing:
        issues.append("missing firewall rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected firewall rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("excluded") != "true":
            issues.append(f"scalar_firewall.csv:{index} excluded is not true")
        if row.get("defect_rank") != "0":
            issues.append(f"scalar_firewall.csv:{index} defect_rank is not zero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_firewall.csv:{index} is not verified")


def check_imports(fixture: Path, issues: list[str]) -> None:
    root = fixture.parent.parent
    prequotient = load_json(
        fixture.parent / "equivariant_wrapped_prequotient_definition" / MANIFEST_NAME,
        issues,
    )
    if prequotient and prequotient.get("status") != "E_EQUIVARIANT_WRAPPED_PREQUOTIENT_DEFINITION_VERIFIED":
        issues.append("prequotient definition manifest status is not verified")

    class_fixture = root / "moduli" / "retained_class_bounds"
    semistable_fixture = root / "moduli" / "retained_semistable_substacks"
    rigidification_fixture = root / "moduli" / "retained_rigidification_inertia"
    class_manifest = load_json(class_fixture / MANIFEST_NAME, issues)
    if class_manifest:
        if class_manifest.get("certified") is not True:
            issues.append("retained class bounds manifest is not certified")
        if class_manifest.get("finite_class_set") is not True:
            issues.append("retained class bounds manifest lacks finite_class_set")
    semistable_manifest = load_json(semistable_fixture / MANIFEST_NAME, issues)
    if semistable_manifest:
        if semistable_manifest.get("certified") is not True:
            issues.append("retained semistable manifest is not certified")
        if semistable_manifest.get("finite_type_semistable_substacks") is not True:
            issues.append("retained semistable manifest lacks finite type")
    rigidification_manifest = load_json(rigidification_fixture / MANIFEST_NAME, issues)
    if rigidification_manifest:
        if rigidification_manifest.get("certified") is not True:
            issues.append("retained rigidification manifest is not certified")
        if rigidification_manifest.get("scalar_rigidifications") is not True:
            issues.append("retained rigidification manifest lacks scalar rigidifications")

    class_rows = load_csv(class_fixture / "class_set.csv", CLASS_COLUMNS, issues).rows
    semistable_rows = load_csv(
        semistable_fixture / "semistable_substacks.csv",
        SEMISTABLE_COLUMNS,
        issues,
    ).rows
    rigidification_rows = load_csv(
        rigidification_fixture / "scalar_rigidifications.csv",
        RIGIDIFICATION_COLUMNS,
        issues,
    ).rows
    if len(class_rows) != 3:
        issues.append("retained class row count must be 3")
    if len(semistable_rows) != 3:
        issues.append("retained semistable row count must be 3")
    if len(rigidification_rows) != 3:
        issues.append("retained rigidification row count must be 3")
    for index, row in enumerate(class_rows, start=2):
        if row.get("retained_class") != "true":
            issues.append(f"class_set.csv:{index} retained_class is not true")
        if row.get("check_status") != "verified":
            issues.append(f"class_set.csv:{index} is not verified")
    for index, row in enumerate(semistable_rows, start=2):
        if row.get("finite_type_status") != "finite_type_verified":
            issues.append(f"semistable_substacks.csv:{index} finite type not verified")
        if row.get("semistability_defect_rank") != "0":
            issues.append(f"semistable_substacks.csv:{index} semistability defect nonzero")
        if row.get("boundedness_defect_rank") != "0":
            issues.append(f"semistable_substacks.csv:{index} boundedness defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"semistable_substacks.csv:{index} is not verified")
    for index, row in enumerate(rigidification_rows, start=2):
        if row.get("scalar_gm_removed") != "true":
            issues.append(f"scalar_rigidifications.csv:{index} scalar Gm not removed")
        if row.get("rigidification_defect_rank") != "0":
            issues.append(f"scalar_rigidifications.csv:{index} rigidification defect nonzero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_rigidifications.csv:{index} is not verified")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    fixture = args.fixture
    issues: list[str] = []
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_manifest(fixture, issues)
    check_single_row(fixture, "finite_type_rows.csv", FINITE_TYPE_COLUMNS, EXPECTED_FINITE_TYPE, issues)
    check_single_row(fixture, "finite_type_input_rows.csv", INPUT_COLUMNS, EXPECTED_INPUT, issues)
    check_single_row(
        fixture,
        "rigidification_descent_rows.csv",
        RIGIDIFICATION_DESCENT_COLUMNS,
        EXPECTED_RIGIDIFICATION_DESCENT,
        issues,
    )
    check_empty_tables(fixture, issues)
    check_obligations(fixture, issues)
    check_firewall(fixture, issues)
    check_imports(fixture, issues)
    if issues:
        print("WRAPPED_PREQUOTIENT_FINITE_TYPE_FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
