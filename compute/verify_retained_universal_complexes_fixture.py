#!/usr/bin/env python3
"""Retained universal-perfect-complex gate.

This verifier checks optimization row 174: universal perfect complexes
on the retained finite substacks.  It imports the retained semistable
substack, class-bound, derived-enhancement, and scalar-rigidification
packets, then checks that every retained finite substack has a
universal perfect complex with base-change datum, finite Tor amplitude,
zero descent defect, and zero perfection defect.

It does not construct finite inertia stratifications, extension/flag
stacks, cosection atlases, transitions, Pfaffian orientations, or
protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "RETAINED_UNIVERSAL_COMPLEXES_VERIFIED"
EXPECTED_KIND = "retained_universal_complexes"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_universal_complexes")
DEFAULT_SEMISTABLE_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
DEFAULT_CLASS_FIXTURE = Path("certificates/moduli/retained_class_bounds")
DEFAULT_DERIVED_FIXTURE = Path("certificates/moduli/retained_derived_enhancements")
DEFAULT_RIGIDIFICATION_FIXTURE = Path("certificates/moduli/retained_rigidification_inertia")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})

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
REQUIRED_RELATIONS = frozenset(
    {
        "semistable_substacks_imported",
        "class_bounds_imported",
        "derived_enhancements_imported",
        "scalar_rigidifications_imported",
        "one_universal_complex_per_substack",
        "base_change_rows_defined",
        "tor_amplitudes_finite",
        "descent_defects_zero",
        "perfection_defects_zero",
        "universal_complexes_mirrored",
        "finite_inertia_stratifications_not_proved",
        "finite_hall_stage_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "finite_inertia_stratifications",
        "extension_flag_stacks",
        "cosection_atlas",
        "transitions",
        "scalar_firewall",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec("universal_complexes.csv", UNIVERSAL_COLUMNS),
    TableSpec(
        "base_change_rows.csv",
        (
            "base_change_id",
            "universal_id",
            "substack_id",
            "base_change_status",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "tor_amplitude_rows.csv",
        (
            "tor_id",
            "universal_id",
            "substack_id",
            "tor_amplitude",
            "lower_tor",
            "upper_tor",
            "tor_amplitude_finite",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "descent_rows.csv",
        (
            "descent_id",
            "universal_id",
            "substack_id",
            "rigidification_id",
            "descent_defect_rank",
            "perfection_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "formal_relations.csv",
        (
            "relation_id",
            "relation_kind",
            "computed_value",
            "expected_value",
            "defect_rank",
            "source_reference",
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
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--semistable-fixture", type=Path, default=DEFAULT_SEMISTABLE_FIXTURE)
    parser.add_argument("--class-fixture", type=Path, default=DEFAULT_CLASS_FIXTURE)
    parser.add_argument("--derived-fixture", type=Path, default=DEFAULT_DERIVED_FIXTURE)
    parser.add_argument("--rigidification-fixture", type=Path, default=DEFAULT_RIGIDIFICATION_FIXTURE)
    parser.add_argument("--finite-moduli-fixture", type=Path, default=DEFAULT_FINITE_MODULI_FIXTURE)
    return parser.parse_args()


def read_manifest(fixture: Path) -> dict:
    manifest_path = fixture / MANIFEST_NAME
    readme_path = fixture / README_NAME
    if not manifest_path.exists():
        raise ValueError(f"missing manifest: {manifest_path}")
    if not readme_path.exists() or not readme_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme_path}")
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    path = fixture / spec.path
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != spec.columns:
            raise ValueError(
                f"{spec.path}: expected columns {spec.columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{spec.path}: unparsed CSV fields in row {row}")
    return rows


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


def check_row(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    if not row.get("source_reference", row.get("proof_reference", "")).strip():
        raise ValueError(f"{table_name}: missing source reference: {row}")
    haystack = " ".join(row.values()).lower()
    for token in FORBIDDEN_TOKENS:
        if token in haystack:
            raise ValueError(f"{table_name}: forbidden token {token!r} in {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_zero(value: int, label: str) -> None:
    if value != 0:
        raise ValueError(f"{label}: expected 0, got {value}")


def parse_amplitude(text: str) -> tuple[int, int]:
    parts = text.split(":")
    if len(parts) != 2:
        raise ValueError(f"tor_amplitude must have form lower:upper, got {text!r}")
    lower = int(parts[0])
    upper = int(parts[1])
    if lower > upper:
        raise ValueError(f"tor_amplitude lower bound exceeds upper bound: {text!r}")
    return lower, upper


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("moduli_kind"), EXPECTED_KIND, "manifest moduli_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("universal_complexes"), True, "manifest universal_complexes")
    require_equal(manifest.get("base_change_compatible"), True, "manifest base_change_compatible")
    require_equal(manifest.get("tor_amplitude_bounded"), True, "manifest tor_amplitude_bounded")
    require_equal(manifest.get("descent_defects_zero"), True, "manifest descent_defects_zero")
    require_equal(manifest.get("perfection_defects_zero"), True, "manifest perfection_defects_zero")
    for key in (
        "finite_inertia_stratifications",
        "extension_flag_stacks",
        "cosection_atlas",
        "transitions",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_equal(manifest.get(key), False, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def rows_by_key(fixture: Path, spec: TableSpec, key: str) -> dict[str, dict[str, str]]:
    rows = read_table(fixture, spec)
    by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, spec.path)
        value = row[key]
        if value in by_key:
            raise ValueError(f"{spec.path}: duplicate {key} {value}")
        by_key[value] = row
    return by_key


def load_inputs(args: argparse.Namespace) -> tuple[set[str], dict[str, str]]:
    semistable = rows_by_key(args.semistable_fixture, TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS), "substack_id")
    class_rows = rows_by_key(args.class_fixture, TableSpec("class_set.csv", CLASS_COLUMNS), "substack_id")
    derived = rows_by_key(args.derived_fixture, TableSpec("derived_enhancements.csv", DERIVED_COLUMNS), "substack_id")
    rigid = rows_by_key(args.rigidification_fixture, TableSpec("scalar_rigidifications.csv", RIGIDIFICATION_COLUMNS), "substack_id")
    substacks = set(semistable)
    require_equal(set(class_rows), substacks, "class-bound substack coverage")
    require_equal(set(derived), substacks, "derived-enhancement substack coverage")
    require_equal(set(rigid), substacks, "rigidification substack coverage")
    rigidification_by_substack = {}
    for substack_id, row in rigid.items():
        require_equal(bool_cell(row, "scalar_gm_removed"), True, f"{substack_id} scalar_gm_removed")
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{substack_id} residual_inertia_finite")
        require_zero(int_cell(row, "rigidification_defect_rank"), f"{substack_id} rigidification_defect")
        rigidification_by_substack[substack_id] = row["rigidification_id"]
    return substacks, rigidification_by_substack


def verify_universal_rows(rows: list[dict[str, str]], substacks: set[str]) -> dict[str, dict[str, str]]:
    by_universal: dict[str, dict[str, str]] = {}
    seen_substacks: set[str] = set()
    for row in rows:
        check_row(row, "universal_complexes.csv")
        universal_id = row["universal_id"]
        if universal_id in by_universal:
            raise ValueError(f"universal_complexes.csv: duplicate universal_id {universal_id}")
        substack_id = row["substack_id"]
        if substack_id not in substacks:
            raise ValueError(f"universal_complexes.csv: unknown substack_id {substack_id}")
        if substack_id in seen_substacks:
            raise ValueError(f"universal_complexes.csv: duplicate substack_id {substack_id}")
        parse_amplitude(row["tor_amplitude"])
        require_zero(int_cell(row, "descent_defect_rank"), f"{universal_id} descent_defect")
        require_zero(int_cell(row, "perfection_defect_rank"), f"{universal_id} perfection_defect")
        by_universal[universal_id] = row
        seen_substacks.add(substack_id)
    require_equal(seen_substacks, substacks, "universal-complex substack coverage")
    return by_universal


def verify_base_change(rows: list[dict[str, str]], by_universal: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "base_change_rows.csv")
        universal_id = row["universal_id"]
        if universal_id in seen:
            raise ValueError(f"base_change_rows.csv: duplicate universal_id {universal_id}")
        universal = by_universal.get(universal_id)
        if universal is None:
            raise ValueError(f"base_change_rows.csv: unknown universal_id {universal_id}")
        require_equal(row["substack_id"], universal["substack_id"], f"{universal_id} substack")
        require_equal(row["base_change_id"], universal["base_change_id"], f"{universal_id} base_change_id")
        require_equal(row["base_change_status"], "base_change_verified", f"{universal_id} base_change_status")
        require_zero(int_cell(row, "defect_rank"), f"{universal_id} base_change defect")
        seen.add(universal_id)
    require_equal(seen, set(by_universal), "base-change universal coverage")


def verify_tor(rows: list[dict[str, str]], by_universal: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "tor_amplitude_rows.csv")
        universal_id = row["universal_id"]
        if universal_id in seen:
            raise ValueError(f"tor_amplitude_rows.csv: duplicate universal_id {universal_id}")
        universal = by_universal.get(universal_id)
        if universal is None:
            raise ValueError(f"tor_amplitude_rows.csv: unknown universal_id {universal_id}")
        lower, upper = parse_amplitude(row["tor_amplitude"])
        require_equal(row["substack_id"], universal["substack_id"], f"{universal_id} substack")
        require_equal(row["tor_amplitude"], universal["tor_amplitude"], f"{universal_id} tor_amplitude")
        require_equal(int_cell(row, "lower_tor"), lower, f"{universal_id} lower_tor")
        require_equal(int_cell(row, "upper_tor"), upper, f"{universal_id} upper_tor")
        require_equal(bool_cell(row, "tor_amplitude_finite"), True, f"{universal_id} tor finite")
        require_zero(int_cell(row, "defect_rank"), f"{universal_id} tor defect")
        seen.add(universal_id)
    require_equal(seen, set(by_universal), "Tor universal coverage")


def verify_descent(
    rows: list[dict[str, str]],
    by_universal: dict[str, dict[str, str]],
    rigidification_by_substack: dict[str, str],
) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "descent_rows.csv")
        universal_id = row["universal_id"]
        if universal_id in seen:
            raise ValueError(f"descent_rows.csv: duplicate universal_id {universal_id}")
        universal = by_universal.get(universal_id)
        if universal is None:
            raise ValueError(f"descent_rows.csv: unknown universal_id {universal_id}")
        substack_id = universal["substack_id"]
        require_equal(row["substack_id"], substack_id, f"{universal_id} substack")
        require_equal(row["rigidification_id"], rigidification_by_substack[substack_id], f"{universal_id} rigidification")
        require_equal(int_cell(row, "descent_defect_rank"), int_cell(universal, "descent_defect_rank"), f"{universal_id} descent")
        require_equal(int_cell(row, "perfection_defect_rank"), int_cell(universal, "perfection_defect_rank"), f"{universal_id} perfection")
        require_zero(int_cell(row, "descent_defect_rank"), f"{universal_id} descent defect")
        require_zero(int_cell(row, "perfection_defect_rank"), f"{universal_id} perfection defect")
        seen.add(universal_id)
    require_equal(seen, set(by_universal), "descent universal coverage")


def verify_relations(rows: list[dict[str, str]], row_count: int) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        computed = int_cell(row, "computed_value")
        expected = int_cell(row, "expected_value")
        require_equal(computed, expected, f"{relation_id} expected")
        if relation_id in {
            "one_universal_complex_per_substack",
            "base_change_rows_defined",
            "tor_amplitudes_finite",
            "descent_defects_zero",
            "perfection_defects_zero",
        }:
            require_equal(computed, row_count, f"{relation_id} count")
        require_zero(int_cell(row, "defect_rank"), f"{relation_id} defect")
        seen.add(relation_id)
    require_equal(seen, REQUIRED_RELATIONS, "formal relation coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"scalar_firewall.csv: duplicate substitute {substitute}")
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_zero(int_cell(row, "defect_rank"), f"{substitute} defect")
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "firewall coverage")


def verify_finite_moduli_mirror(finite_moduli_fixture: Path, rows: list[dict[str, str]]) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("universal_complexes.csv", UNIVERSAL_COLUMNS))
    expected = sorted(rows, key=lambda row: row["universal_id"])
    actual = sorted(mirrored, key=lambda row: row["universal_id"])
    require_equal(actual, expected, "finite-moduli universal_complexes mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        substacks, rigidification_by_substack = load_inputs(args)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        universal = verify_universal_rows(tables["universal_complexes.csv"], substacks)
        verify_base_change(tables["base_change_rows.csv"], universal)
        verify_tor(tables["tor_amplitude_rows.csv"], universal)
        verify_descent(tables["descent_rows.csv"], universal, rigidification_by_substack)
        verify_relations(tables["formal_relations.csv"], len(universal))
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["universal_complexes.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_UNIVERSAL_COMPLEXES_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
