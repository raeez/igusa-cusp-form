#!/usr/bin/env python3
"""Quasi-smooth retained derived-enhancement gate.

This verifier checks the item-168 packet: each finite-type retained
semistable substack carries a quasi-smooth derived Artin enhancement,
with PTVV (-1)-shifted symplectic form, cotangent amplitude [-1,0],
and zero Tor-amplitude and symplectic defects.

It does not construct universal complexes, rigidifications, inertia
strata, extension/flag stacks, cosection atlases, transitions,
Pfaffian orientations, or protected traces.
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
SUCCESS_STATUS = "RETAINED_DERIVED_ENHANCEMENTS_VERIFIED"
EXPECTED_KIND = "retained_derived_enhancements"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_derived_enhancements")
DEFAULT_SEMISTABLE_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
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
REQUIRED_RELATIONS = frozenset(
    {
        "semistable_substacks_imported",
        "ptvv_shifted_symplectic_imported",
        "one_enhancement_per_substack",
        "cotangent_amplitude_minus_one_zero",
        "quasi_smooth_rows_verified",
        "tor_amplitude_defects_zero",
        "symplectic_defects_zero",
        "derived_enhancements_mirrored",
        "universal_complexes_not_proved",
        "rigidification_not_proved",
        "finite_hall_stage_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "universal_complexes",
        "scalar_rigidification",
        "finite_residual_inertia",
        "extension_flag_stacks",
        "cosection_atlas",
        "transitions",
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
    TableSpec(
        "source_theorem.csv",
        (
            "source_id",
            "citation_key",
            "source_theorem",
            "shifted_degree",
            "calabi_yau_dimension",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec("derived_enhancements.csv", DERIVED_COLUMNS),
    TableSpec(
        "amplitude_rows.csv",
        (
            "amplitude_id",
            "enhancement_id",
            "derived_stack_id",
            "cotangent_amplitude",
            "quasi_smooth_status",
            "tor_amplitude_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "symplectic_rows.csv",
        (
            "symplectic_id",
            "enhancement_id",
            "shifted_symplectic_form_id",
            "shifted_degree",
            "restriction_status",
            "symplectic_defect_rank",
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


def read_semistable_substacks(fixture: Path) -> list[dict[str, str]]:
    return read_table(fixture, TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS))


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


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("moduli_kind"), EXPECTED_KIND, "manifest moduli_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(
        manifest.get("finite_type_semistable_substacks_required"),
        True,
        "manifest finite_type_semistable_substacks_required",
    )
    require_equal(
        manifest.get("quasi_smooth_derived_enhancements"),
        True,
        "manifest quasi_smooth_derived_enhancements",
    )
    for key in (
        "complete_finite_moduli",
        "universal_complexes",
        "scalar_rigidification",
        "finite_residual_inertia",
        "extension_flag_stacks",
        "cosection_atlas",
        "transitions",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_equal(manifest.get(key), False, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_semistable_inputs(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    by_substack: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "semistable_substacks.csv")
        substack_id = row["substack_id"]
        if substack_id in by_substack:
            raise ValueError(f"semistable_substacks.csv: duplicate substack_id {substack_id}")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{substack_id} finite_type_status")
        require_equal(bool_cell(row, "specialization_closed"), True, f"{substack_id} specialization_closed")
        require_zero(int_cell(row, "semistability_defect_rank"), f"{substack_id} semistability_defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{substack_id} boundedness_defect")
        by_substack[substack_id] = row
    return by_substack


def verify_source(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "source row count")
    row = rows[0]
    check_row(row, "source_theorem.csv")
    require_equal(row["citation_key"], "PTVV2013", "citation_key")
    require_equal(row["source_theorem"], "Theorem 0.3", "source_theorem")
    require_equal(row["shifted_degree"], "-1", "shifted_degree")
    require_equal(row["calabi_yau_dimension"], "3", "calabi_yau_dimension")


def verify_derived_rows(
    rows: list[dict[str, str]],
    semistable_by_substack: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_enhancement: dict[str, dict[str, str]] = {}
    seen_substacks: set[str] = set()
    for row in rows:
        check_row(row, "derived_enhancements.csv")
        enhancement_id = row["enhancement_id"]
        if enhancement_id in by_enhancement:
            raise ValueError(f"derived_enhancements.csv: duplicate enhancement_id {enhancement_id}")
        substack_id = row["substack_id"]
        if substack_id in seen_substacks:
            raise ValueError(f"derived_enhancements.csv: duplicate substack_id {substack_id}")
        if substack_id not in semistable_by_substack:
            raise ValueError(f"derived_enhancements.csv: unknown substack_id {substack_id}")
        seen_substacks.add(substack_id)
        require_equal(row["quasi_smooth_status"], "quasi_smooth_verified", f"{enhancement_id} quasi_smooth_status")
        require_equal(row["cotangent_amplitude"], "[-1,0]", f"{enhancement_id} cotangent_amplitude")
        require_zero(int_cell(row, "tor_amplitude_defect_rank"), f"{enhancement_id} tor_amplitude_defect")
        require_zero(int_cell(row, "symplectic_defect_rank"), f"{enhancement_id} symplectic_defect")
        if "PTVV2013" not in row["proof_reference"]:
            raise ValueError(f"derived_enhancements.csv: PTVV2013 missing in {enhancement_id}")
        by_enhancement[enhancement_id] = row
    require_equal(seen_substacks, set(semistable_by_substack), "derived enhancement substack coverage")
    return by_enhancement


def verify_amplitudes(rows: list[dict[str, str]], derived_by_id: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "amplitude_rows.csv")
        enhancement_id = row["enhancement_id"]
        if enhancement_id in seen:
            raise ValueError(f"amplitude_rows.csv: duplicate enhancement_id {enhancement_id}")
        seen.add(enhancement_id)
        derived = derived_by_id.get(enhancement_id)
        if derived is None:
            raise ValueError(f"amplitude_rows.csv: unknown enhancement_id {enhancement_id}")
        require_equal(row["derived_stack_id"], derived["derived_stack_id"], f"{enhancement_id} derived_stack_id")
        require_equal(row["cotangent_amplitude"], "[-1,0]", f"{enhancement_id} cotangent_amplitude")
        require_equal(row["quasi_smooth_status"], "quasi_smooth_verified", f"{enhancement_id} quasi_smooth_status")
        require_zero(int_cell(row, "tor_amplitude_defect_rank"), f"{enhancement_id} tor_amplitude_defect")
    require_equal(seen, set(derived_by_id), "amplitude coverage")


def verify_symplectic(rows: list[dict[str, str]], derived_by_id: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "symplectic_rows.csv")
        enhancement_id = row["enhancement_id"]
        if enhancement_id in seen:
            raise ValueError(f"symplectic_rows.csv: duplicate enhancement_id {enhancement_id}")
        seen.add(enhancement_id)
        derived = derived_by_id.get(enhancement_id)
        if derived is None:
            raise ValueError(f"symplectic_rows.csv: unknown enhancement_id {enhancement_id}")
        require_equal(
            row["shifted_symplectic_form_id"],
            derived["shifted_symplectic_form_id"],
            f"{enhancement_id} shifted_symplectic_form_id",
        )
        require_equal(row["shifted_degree"], "-1", f"{enhancement_id} shifted_degree")
        require_equal(row["restriction_status"], "restricted_verified", f"{enhancement_id} restriction_status")
        require_zero(int_cell(row, "symplectic_defect_rank"), f"{enhancement_id} symplectic_defect")
    require_equal(seen, set(derived_by_id), "symplectic coverage")


def verify_relations(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), int_cell(row, "expected_value"), f"{relation_id} expected")
        require_zero(int_cell(row, "defect_rank"), f"{relation_id} defect")
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
        require_zero(int_cell(row, "defect_rank"), f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"scalar_firewall.csv missing rows: {sorted(missing)}")


def verify_finite_moduli_mirror(finite_moduli_fixture: Path, derived_rows: list[dict[str, str]]) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("derived_enhancements.csv", DERIVED_COLUMNS))
    expected = sorted(derived_rows, key=lambda row: row["enhancement_id"])
    actual = sorted(mirrored, key=lambda row: row["enhancement_id"])
    require_equal(actual, expected, "finite-moduli derived_enhancements mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        semistable_by_substack = verify_semistable_inputs(read_semistable_substacks(args.semistable_fixture))
        verify_source(tables["source_theorem.csv"])
        derived_by_id = verify_derived_rows(tables["derived_enhancements.csv"], semistable_by_substack)
        verify_amplitudes(tables["amplitude_rows.csv"], derived_by_id)
        verify_symplectic(tables["symplectic_rows.csv"], derived_by_id)
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["derived_enhancements.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_DERIVED_ENHANCEMENTS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
