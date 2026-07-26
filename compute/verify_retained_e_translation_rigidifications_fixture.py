#!/usr/bin/env python3
"""Retained E-translation-rigidification gate.

This verifier checks optimization row 176: E-translation rigidification
on the retained finite substacks.  It imports scalar rigidifications
and universal complexes, then checks that every retained finite
substack has an elliptic-translation quotient with the translation
action removed and zero translation-rigidification defect.

It does not construct finite closed inertia stratifications,
extension/flag stacks, cosection atlases, transitions, Pfaffian
orientations, or protected traces.
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
SUCCESS_STATUS = "RETAINED_E_TRANSLATION_RIGIDIFICATIONS_VERIFIED"
EXPECTED_KIND = "retained_e_translation_rigidifications"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_e_translation_rigidifications")
DEFAULT_RIGIDIFICATION_FIXTURE = Path("certificates/moduli/retained_rigidification_inertia")
DEFAULT_UNIVERSAL_FIXTURE = Path("certificates/moduli/retained_universal_complexes")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})

SCALAR_RIGIDIFICATION_COLUMNS = (
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
E_TRANSLATION_COLUMNS = (
    "translation_rigidification_id",
    "substack_id",
    "scalar_rigidification_id",
    "universal_id",
    "elliptic_curve_id",
    "translation_action_id",
    "quotient_stack_id",
    "translation_removed",
    "action_free_on_retained_row",
    "translation_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_RELATIONS = frozenset(
    {
        "scalar_rigidifications_imported",
        "universal_complexes_imported",
        "one_translation_rigidification_per_substack",
        "elliptic_translation_actions_named",
        "translations_removed",
        "free_actions_on_retained_rows",
        "translation_defects_zero",
        "translation_rigidifications_mirrored",
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
    TableSpec("e_translation_rigidifications.csv", E_TRANSLATION_COLUMNS),
    TableSpec(
        "translation_actions.csv",
        (
            "translation_action_id",
            "substack_id",
            "elliptic_curve_id",
            "origin_id",
            "action_defined",
            "action_free_on_retained_row",
            "action_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "quotient_rows.csv",
        (
            "quotient_row_id",
            "translation_rigidification_id",
            "substack_id",
            "quotient_stack_id",
            "translation_removed",
            "quotient_defect_rank",
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
    parser.add_argument("--rigidification-fixture", type=Path, default=DEFAULT_RIGIDIFICATION_FIXTURE)
    parser.add_argument("--universal-fixture", type=Path, default=DEFAULT_UNIVERSAL_FIXTURE)
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


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("moduli_kind"), EXPECTED_KIND, "manifest moduli_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("e_translation_rigidifications"), True, "manifest e_translation_rigidifications")
    require_equal(manifest.get("translations_removed"), True, "manifest translations_removed")
    require_equal(manifest.get("translation_defects_zero"), True, "manifest translation_defects_zero")
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


def load_inputs(args: argparse.Namespace) -> tuple[dict[str, str], dict[str, str]]:
    scalar = rows_by_key(
        args.rigidification_fixture,
        TableSpec("scalar_rigidifications.csv", SCALAR_RIGIDIFICATION_COLUMNS),
        "substack_id",
    )
    universal = rows_by_key(
        args.universal_fixture,
        TableSpec("universal_complexes.csv", UNIVERSAL_COLUMNS),
        "substack_id",
    )
    require_equal(set(scalar), set(universal), "scalar/universal substack coverage")
    scalar_by_substack: dict[str, str] = {}
    universal_by_substack: dict[str, str] = {}
    for substack_id, row in scalar.items():
        require_equal(bool_cell(row, "scalar_gm_removed"), True, f"{substack_id} scalar_gm_removed")
        require_zero(int_cell(row, "rigidification_defect_rank"), f"{substack_id} scalar rigidification defect")
        scalar_by_substack[substack_id] = row["rigidification_id"]
    for substack_id, row in universal.items():
        require_zero(int_cell(row, "descent_defect_rank"), f"{substack_id} descent defect")
        require_zero(int_cell(row, "perfection_defect_rank"), f"{substack_id} perfection defect")
        universal_by_substack[substack_id] = row["universal_id"]
    return scalar_by_substack, universal_by_substack


def verify_translation_rows(
    rows: list[dict[str, str]],
    scalar_by_substack: dict[str, str],
    universal_by_substack: dict[str, str],
) -> dict[str, dict[str, str]]:
    by_translation: dict[str, dict[str, str]] = {}
    seen_substacks: set[str] = set()
    for row in rows:
        check_row(row, "e_translation_rigidifications.csv")
        rid = row["translation_rigidification_id"]
        if rid in by_translation:
            raise ValueError(f"e_translation_rigidifications.csv: duplicate id {rid}")
        substack_id = row["substack_id"]
        if substack_id not in scalar_by_substack:
            raise ValueError(f"e_translation_rigidifications.csv: unknown substack_id {substack_id}")
        if substack_id in seen_substacks:
            raise ValueError(f"e_translation_rigidifications.csv: duplicate substack_id {substack_id}")
        require_equal(row["scalar_rigidification_id"], scalar_by_substack[substack_id], f"{rid} scalar link")
        require_equal(row["universal_id"], universal_by_substack[substack_id], f"{rid} universal link")
        require_equal(row["elliptic_curve_id"], "E", f"{rid} elliptic_curve_id")
        require_equal(bool_cell(row, "translation_removed"), True, f"{rid} translation_removed")
        require_equal(bool_cell(row, "action_free_on_retained_row"), True, f"{rid} free action")
        require_zero(int_cell(row, "translation_defect_rank"), f"{rid} translation defect")
        by_translation[rid] = row
        seen_substacks.add(substack_id)
    require_equal(seen_substacks, set(scalar_by_substack), "translation substack coverage")
    return by_translation


def verify_actions(rows: list[dict[str, str]], by_translation: dict[str, dict[str, str]]) -> None:
    expected_actions = {row["translation_action_id"]: row for row in by_translation.values()}
    seen: set[str] = set()
    for row in rows:
        check_row(row, "translation_actions.csv")
        action_id = row["translation_action_id"]
        if action_id in seen:
            raise ValueError(f"translation_actions.csv: duplicate action_id {action_id}")
        translation = expected_actions.get(action_id)
        if translation is None:
            raise ValueError(f"translation_actions.csv: unknown action_id {action_id}")
        require_equal(row["substack_id"], translation["substack_id"], f"{action_id} substack")
        require_equal(row["elliptic_curve_id"], "E", f"{action_id} elliptic_curve_id")
        require_equal(row["origin_id"], "0_E", f"{action_id} origin")
        require_equal(bool_cell(row, "action_defined"), True, f"{action_id} action_defined")
        require_equal(bool_cell(row, "action_free_on_retained_row"), True, f"{action_id} free")
        require_zero(int_cell(row, "action_defect_rank"), f"{action_id} action defect")
        seen.add(action_id)
    require_equal(seen, set(expected_actions), "translation action coverage")


def verify_quotients(rows: list[dict[str, str]], by_translation: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "quotient_rows.csv")
        rid = row["translation_rigidification_id"]
        if rid in seen:
            raise ValueError(f"quotient_rows.csv: duplicate translation_rigidification_id {rid}")
        translation = by_translation.get(rid)
        if translation is None:
            raise ValueError(f"quotient_rows.csv: unknown translation_rigidification_id {rid}")
        require_equal(row["substack_id"], translation["substack_id"], f"{rid} substack")
        require_equal(row["quotient_stack_id"], translation["quotient_stack_id"], f"{rid} quotient")
        require_equal(bool_cell(row, "translation_removed"), True, f"{rid} translation_removed")
        require_zero(int_cell(row, "quotient_defect_rank"), f"{rid} quotient defect")
        seen.add(rid)
    require_equal(seen, set(by_translation), "translation quotient coverage")


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
            "one_translation_rigidification_per_substack",
            "elliptic_translation_actions_named",
            "translations_removed",
            "free_actions_on_retained_rows",
            "translation_defects_zero",
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
    mirrored = read_table(finite_moduli_fixture, TableSpec("e_translation_rigidifications.csv", E_TRANSLATION_COLUMNS))
    expected = sorted(rows, key=lambda row: row["translation_rigidification_id"])
    actual = sorted(mirrored, key=lambda row: row["translation_rigidification_id"])
    require_equal(actual, expected, "finite-moduli e_translation_rigidifications mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        scalar_by_substack, universal_by_substack = load_inputs(args)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        translations = verify_translation_rows(
            tables["e_translation_rigidifications.csv"],
            scalar_by_substack,
            universal_by_substack,
        )
        verify_actions(tables["translation_actions.csv"], translations)
        verify_quotients(tables["quotient_rows.csv"], translations)
        verify_relations(tables["formal_relations.csv"], len(translations))
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["e_translation_rigidifications.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_E_TRANSLATION_RIGIDIFICATIONS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
