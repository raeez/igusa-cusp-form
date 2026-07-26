#!/usr/bin/env python3
"""Retained rigidification and residual-inertia gate.

This verifier checks the item-169 packet: each retained derived
enhancement has a scalar rigidification, the scalar G_m is removed,
and the residual inertia is finite with zero rigidification defect.

It does not construct universal complexes, finite inertia
stratifications, extension/flag stacks, cosection atlases, transitions,
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
SUCCESS_STATUS = "RETAINED_RIGIDIFICATION_INERTIA_VERIFIED"
EXPECTED_KIND = "retained_rigidification_inertia"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_rigidification_inertia")
DEFAULT_DERIVED_FIXTURE = Path("certificates/moduli/retained_derived_enhancements")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
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
REQUIRED_RELATIONS = frozenset(
    {
        "derived_enhancements_imported",
        "one_rigidification_per_substack",
        "automorphism_groups_named",
        "scalar_gm_removed",
        "residual_inertia_finite",
        "rigidification_defects_zero",
        "rigidifications_mirrored",
        "universal_complexes_not_proved",
        "stratifications_not_proved",
        "finite_hall_stage_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "universal_complexes",
        "finite_inertia_stratifications",
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
        "group_exact_sequences.csv",
        (
            "sequence_id",
            "rigidification_id",
            "substack_id",
            "automorphism_group_id",
            "scalar_group_id",
            "residual_group_id",
            "residual_group_order",
            "exactness_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec("scalar_rigidifications.csv", RIGIDIFICATION_COLUMNS),
    TableSpec(
        "residual_inertia.csv",
        (
            "inertia_id",
            "rigidification_id",
            "substack_id",
            "residual_group_id",
            "residual_group_order",
            "residual_inertia_finite",
            "inertia_defect_rank",
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
    parser.add_argument("--derived-fixture", type=Path, default=DEFAULT_DERIVED_FIXTURE)
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


def read_derived_enhancements(fixture: Path) -> list[dict[str, str]]:
    return read_table(fixture, TableSpec("derived_enhancements.csv", DERIVED_COLUMNS))


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
        manifest.get("quasi_smooth_derived_enhancements_required"),
        True,
        "manifest quasi_smooth_derived_enhancements_required",
    )
    require_equal(manifest.get("scalar_rigidifications"), True, "manifest scalar_rigidifications")
    require_equal(
        manifest.get("finite_residual_inertia_after_rigidification"),
        True,
        "manifest finite_residual_inertia_after_rigidification",
    )
    for key in (
        "complete_finite_moduli",
        "universal_complexes",
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


def verify_derived_inputs(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    by_substack: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "derived_enhancements.csv")
        substack_id = row["substack_id"]
        if substack_id in by_substack:
            raise ValueError(f"derived_enhancements.csv: duplicate substack_id {substack_id}")
        require_equal(row["quasi_smooth_status"], "quasi_smooth_verified", f"{substack_id} quasi_smooth")
        require_zero(int_cell(row, "tor_amplitude_defect_rank"), f"{substack_id} tor_amplitude_defect")
        require_zero(int_cell(row, "symplectic_defect_rank"), f"{substack_id} symplectic_defect")
        by_substack[substack_id] = row
    return by_substack


def verify_sequences(
    rows: list[dict[str, str]],
    derived_by_substack: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_rigidification: dict[str, dict[str, str]] = {}
    seen_substacks: set[str] = set()
    for row in rows:
        check_row(row, "group_exact_sequences.csv")
        rigidification_id = row["rigidification_id"]
        if rigidification_id in by_rigidification:
            raise ValueError(f"group_exact_sequences.csv: duplicate rigidification_id {rigidification_id}")
        substack_id = row["substack_id"]
        if substack_id in seen_substacks:
            raise ValueError(f"group_exact_sequences.csv: duplicate substack_id {substack_id}")
        if substack_id not in derived_by_substack:
            raise ValueError(f"group_exact_sequences.csv: unknown substack_id {substack_id}")
        seen_substacks.add(substack_id)
        require_equal(row["scalar_group_id"], "G_m", f"{rigidification_id} scalar_group_id")
        if int_cell(row, "residual_group_order") <= 0:
            raise ValueError(f"group_exact_sequences.csv: residual_group_order must be positive in {row}")
        require_zero(int_cell(row, "exactness_defect_rank"), f"{rigidification_id} exactness_defect")
        by_rigidification[rigidification_id] = row
    require_equal(seen_substacks, set(derived_by_substack), "exact-sequence substack coverage")
    return by_rigidification


def verify_rigidifications(
    rows: list[dict[str, str]],
    sequences_by_rigidification: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_rigidification: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "scalar_rigidifications.csv")
        rigidification_id = row["rigidification_id"]
        if rigidification_id in by_rigidification:
            raise ValueError(f"scalar_rigidifications.csv: duplicate rigidification_id {rigidification_id}")
        sequence = sequences_by_rigidification.get(rigidification_id)
        if sequence is None:
            raise ValueError(f"scalar_rigidifications.csv: unknown rigidification_id {rigidification_id}")
        require_equal(row["substack_id"], sequence["substack_id"], f"{rigidification_id} substack_id")
        require_equal(row["automorphism_group_id"], sequence["automorphism_group_id"], f"{rigidification_id} automorphism_group")
        require_equal(bool_cell(row, "scalar_gm_removed"), True, f"{rigidification_id} scalar_gm_removed")
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{rigidification_id} residual_inertia_finite")
        require_zero(int_cell(row, "rigidification_defect_rank"), f"{rigidification_id} rigidification_defect")
        by_rigidification[rigidification_id] = row
    require_equal(set(by_rigidification), set(sequences_by_rigidification), "rigidification coverage")
    return by_rigidification


def verify_residual_inertia(
    rows: list[dict[str, str]],
    sequences_by_rigidification: dict[str, dict[str, str]],
) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "residual_inertia.csv")
        rigidification_id = row["rigidification_id"]
        if rigidification_id in seen:
            raise ValueError(f"residual_inertia.csv: duplicate rigidification_id {rigidification_id}")
        seen.add(rigidification_id)
        sequence = sequences_by_rigidification.get(rigidification_id)
        if sequence is None:
            raise ValueError(f"residual_inertia.csv: unknown rigidification_id {rigidification_id}")
        require_equal(row["substack_id"], sequence["substack_id"], f"{rigidification_id} substack_id")
        require_equal(row["residual_group_id"], sequence["residual_group_id"], f"{rigidification_id} residual_group")
        require_equal(int_cell(row, "residual_group_order"), int_cell(sequence, "residual_group_order"), f"{rigidification_id} residual_group_order")
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{rigidification_id} residual_inertia_finite")
        require_zero(int_cell(row, "inertia_defect_rank"), f"{rigidification_id} inertia_defect")
    require_equal(seen, set(sequences_by_rigidification), "residual inertia coverage")


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


def verify_finite_moduli_mirror(finite_moduli_fixture: Path, rows: list[dict[str, str]]) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("scalar_rigidifications.csv", RIGIDIFICATION_COLUMNS))
    expected = sorted(rows, key=lambda row: row["rigidification_id"])
    actual = sorted(mirrored, key=lambda row: row["rigidification_id"])
    require_equal(actual, expected, "finite-moduli scalar_rigidifications mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        derived_by_substack = verify_derived_inputs(read_derived_enhancements(args.derived_fixture))
        sequences = verify_sequences(tables["group_exact_sequences.csv"], derived_by_substack)
        verify_rigidifications(tables["scalar_rigidifications.csv"], sequences)
        verify_residual_inertia(tables["residual_inertia.csv"], sequences)
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["scalar_rigidifications.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_RIGIDIFICATION_INERTIA_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
