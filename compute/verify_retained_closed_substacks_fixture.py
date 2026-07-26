#!/usr/bin/env python3
"""Retained closed-substack gate.

This verifier checks optimization row 177: the retained finite
substacks are recorded as finite closed substacks with a finite closed
cover and finite residual inertia after scalar rigidification.  It
imports the retained semistable substacks, scalar rigidifications, and
E-translation rigidifications, then checks that the stratification rows
mirrored into the finite-moduli packet have positive finite size, zero
coverage defect, and zero inertia defect.

It does not prove closure under extensions, closure under HN factors,
closure under duals, extension/flag stacks, cosection atlases,
transitions, Pfaffian orientations, or protected traces.
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
SUCCESS_STATUS = "RETAINED_CLOSED_SUBSTACKS_VERIFIED"
EXPECTED_KIND = "retained_closed_substacks"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_closed_substacks")
DEFAULT_SEMISTABLE_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
DEFAULT_RIGIDIFICATION_FIXTURE = Path("certificates/moduli/retained_rigidification_inertia")
DEFAULT_E_TRANSLATION_FIXTURE = Path("certificates/moduli/retained_e_translation_rigidifications")
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
CLOSED_SUBSTACK_COLUMNS = (
    "closed_substack_id",
    "substack_id",
    "translation_rigidification_id",
    "closed_embedding_id",
    "closed_in_ambient",
    "finite_type_status",
    "finite_residual_inertia",
    "closure_defect_rank",
    "inertia_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
CLOSED_COVER_COLUMNS = (
    "closed_cover_id",
    "substack_id",
    "closed_substack_ids",
    "covering_family_finite",
    "cover_is_closed",
    "coverage_defect_rank",
    "source_reference",
    "check_status",
    "notes",
)
STRATIFICATION_COLUMNS = (
    "stratification_id",
    "substack_id",
    "strata_count",
    "closed_cover_id",
    "finite_residual_inertia",
    "coverage_defect_rank",
    "inertia_defect_rank",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_RELATIONS = frozenset(
    {
        "semistable_substacks_imported",
        "scalar_residual_inertia_imported",
        "e_translation_rigidifications_imported",
        "one_closed_substack_per_retained_substack",
        "closed_cover_rows_defined",
        "one_stratum_per_closed_cover",
        "finite_residual_inertia_on_closed_rows",
        "coverage_defects_zero",
        "inertia_defects_zero",
        "stratifications_mirrored",
        "extension_closure_not_proved",
        "hn_factor_closure_not_proved",
        "dual_closure_not_proved",
        "finite_hall_stage_not_proved",
    }
)
COUNT_RELATIONS = frozenset(
    {
        "semistable_substacks_imported",
        "scalar_residual_inertia_imported",
        "e_translation_rigidifications_imported",
        "one_closed_substack_per_retained_substack",
        "closed_cover_rows_defined",
        "one_stratum_per_closed_cover",
        "finite_residual_inertia_on_closed_rows",
        "coverage_defects_zero",
        "inertia_defects_zero",
        "stratifications_mirrored",
    }
)
ZERO_RELATIONS = REQUIRED_RELATIONS - COUNT_RELATIONS
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "extension_closure",
        "hn_factor_closure",
        "dual_closure",
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
    TableSpec("retained_closed_substacks.csv", CLOSED_SUBSTACK_COLUMNS),
    TableSpec("closed_cover_rows.csv", CLOSED_COVER_COLUMNS),
    TableSpec("stratifications.csv", STRATIFICATION_COLUMNS),
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
    parser.add_argument("--rigidification-fixture", type=Path, default=DEFAULT_RIGIDIFICATION_FIXTURE)
    parser.add_argument("--e-translation-fixture", type=Path, default=DEFAULT_E_TRANSLATION_FIXTURE)
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
    require_equal(manifest.get("retained_closed_substacks"), True, "manifest retained_closed_substacks")
    require_equal(manifest.get("finite_closed_cover"), True, "manifest finite_closed_cover")
    require_equal(
        manifest.get("finite_residual_inertia_after_rigidification"),
        True,
        "manifest finite_residual_inertia_after_rigidification",
    )
    require_equal(manifest.get("coverage_defects_zero"), True, "manifest coverage_defects_zero")
    require_equal(manifest.get("inertia_defects_zero"), True, "manifest inertia_defects_zero")
    for key in (
        "extension_closure",
        "hn_factor_closure",
        "dual_closure",
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


def load_inputs(
    semistable_fixture: Path,
    rigidification_fixture: Path,
    e_translation_fixture: Path,
) -> tuple[dict[str, dict[str, str]], dict[str, str], dict[str, str]]:
    semistable = rows_by_key(
        semistable_fixture,
        TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS),
        "substack_id",
    )
    scalar = rows_by_key(
        rigidification_fixture,
        TableSpec("scalar_rigidifications.csv", SCALAR_RIGIDIFICATION_COLUMNS),
        "substack_id",
    )
    e_translation = rows_by_key(
        e_translation_fixture,
        TableSpec("e_translation_rigidifications.csv", E_TRANSLATION_COLUMNS),
        "substack_id",
    )
    require_equal(set(semistable), set(scalar), "semistable/scalar substack coverage")
    require_equal(set(semistable), set(e_translation), "semistable/E-translation substack coverage")

    scalar_by_substack: dict[str, str] = {}
    e_translation_by_substack: dict[str, str] = {}
    for substack_id, row in semistable.items():
        require_equal(row["finite_type_status"], "finite_type_verified", f"{substack_id} finite_type")
        require_equal(bool_cell(row, "specialization_closed"), True, f"{substack_id} specialization_closed")
        require_zero(int_cell(row, "semistability_defect_rank"), f"{substack_id} semistability defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{substack_id} boundedness defect")
    for substack_id, row in scalar.items():
        require_equal(bool_cell(row, "scalar_gm_removed"), True, f"{substack_id} scalar_gm_removed")
        require_equal(bool_cell(row, "residual_inertia_finite"), True, f"{substack_id} residual inertia")
        require_zero(int_cell(row, "rigidification_defect_rank"), f"{substack_id} rigidification defect")
        scalar_by_substack[substack_id] = row["rigidification_id"]
    for substack_id, row in e_translation.items():
        require_equal(bool_cell(row, "translation_removed"), True, f"{substack_id} translation_removed")
        require_equal(bool_cell(row, "action_free_on_retained_row"), True, f"{substack_id} free E-action")
        require_zero(int_cell(row, "translation_defect_rank"), f"{substack_id} translation defect")
        e_translation_by_substack[substack_id] = row["translation_rigidification_id"]
    return semistable, scalar_by_substack, e_translation_by_substack


def verify_closed_substacks(
    rows: list[dict[str, str]],
    semistable_by_substack: dict[str, dict[str, str]],
    e_translation_by_substack: dict[str, str],
) -> dict[str, dict[str, str]]:
    by_substack: dict[str, dict[str, str]] = {}
    seen_closed_ids: set[str] = set()
    for row in rows:
        check_row(row, "retained_closed_substacks.csv")
        closed_id = row["closed_substack_id"]
        if closed_id in seen_closed_ids:
            raise ValueError(f"retained_closed_substacks.csv: duplicate closed_substack_id {closed_id}")
        seen_closed_ids.add(closed_id)
        substack_id = row["substack_id"]
        if substack_id not in semistable_by_substack:
            raise ValueError(f"retained_closed_substacks.csv: unknown substack_id {substack_id}")
        if substack_id in by_substack:
            raise ValueError(f"retained_closed_substacks.csv: duplicate substack_id {substack_id}")
        require_equal(
            row["translation_rigidification_id"],
            e_translation_by_substack[substack_id],
            f"{closed_id} E-translation link",
        )
        require_equal(bool_cell(row, "closed_in_ambient"), True, f"{closed_id} closed_in_ambient")
        if row["finite_type_status"] not in {"finite_type_verified", "verified"}:
            raise ValueError(f"{closed_id}: finite_type_status is not verified")
        require_equal(bool_cell(row, "finite_residual_inertia"), True, f"{closed_id} finite residual inertia")
        require_zero(int_cell(row, "closure_defect_rank"), f"{closed_id} closure defect")
        require_zero(int_cell(row, "inertia_defect_rank"), f"{closed_id} inertia defect")
        by_substack[substack_id] = row
    require_equal(set(by_substack), set(semistable_by_substack), "closed-substack coverage")
    return by_substack


def verify_covers(
    rows: list[dict[str, str]],
    closed_by_substack: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_substack: dict[str, dict[str, str]] = {}
    seen_cover_ids: set[str] = set()
    for row in rows:
        check_row(row, "closed_cover_rows.csv")
        cover_id = row["closed_cover_id"]
        if cover_id in seen_cover_ids:
            raise ValueError(f"closed_cover_rows.csv: duplicate closed_cover_id {cover_id}")
        seen_cover_ids.add(cover_id)
        substack_id = row["substack_id"]
        closed = closed_by_substack.get(substack_id)
        if closed is None:
            raise ValueError(f"closed_cover_rows.csv: unknown substack_id {substack_id}")
        if substack_id in by_substack:
            raise ValueError(f"closed_cover_rows.csv: duplicate substack_id {substack_id}")
        require_equal(row["closed_substack_ids"], closed["closed_substack_id"], f"{cover_id} closed_substack_ids")
        require_equal(bool_cell(row, "covering_family_finite"), True, f"{cover_id} finite cover")
        require_equal(bool_cell(row, "cover_is_closed"), True, f"{cover_id} closed cover")
        require_zero(int_cell(row, "coverage_defect_rank"), f"{cover_id} coverage defect")
        by_substack[substack_id] = row
    require_equal(set(by_substack), set(closed_by_substack), "closed-cover coverage")
    return by_substack


def verify_stratifications(
    rows: list[dict[str, str]],
    covers_by_substack: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_substack: dict[str, dict[str, str]] = {}
    seen_stratification_ids: set[str] = set()
    for row in rows:
        check_row(row, "stratifications.csv")
        stratification_id = row["stratification_id"]
        if stratification_id in seen_stratification_ids:
            raise ValueError(f"stratifications.csv: duplicate stratification_id {stratification_id}")
        seen_stratification_ids.add(stratification_id)
        substack_id = row["substack_id"]
        cover = covers_by_substack.get(substack_id)
        if cover is None:
            raise ValueError(f"stratifications.csv: unknown substack_id {substack_id}")
        if substack_id in by_substack:
            raise ValueError(f"stratifications.csv: duplicate substack_id {substack_id}")
        require_equal(row["closed_cover_id"], cover["closed_cover_id"], f"{stratification_id} closed cover")
        require_equal(int_cell(row, "strata_count"), 1, f"{stratification_id} strata_count")
        require_equal(bool_cell(row, "finite_residual_inertia"), True, f"{stratification_id} finite residual inertia")
        require_zero(int_cell(row, "coverage_defect_rank"), f"{stratification_id} coverage defect")
        require_zero(int_cell(row, "inertia_defect_rank"), f"{stratification_id} inertia defect")
        by_substack[substack_id] = row
    require_equal(set(by_substack), set(covers_by_substack), "stratification coverage")
    return by_substack


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
        if relation_id in COUNT_RELATIONS:
            require_equal(computed, row_count, f"{relation_id} count")
        elif relation_id in ZERO_RELATIONS:
            require_zero(computed, f"{relation_id} computed")
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
    mirrored = read_table(finite_moduli_fixture, TableSpec("stratifications.csv", STRATIFICATION_COLUMNS))
    expected = sorted(rows, key=lambda row: row["stratification_id"])
    actual = sorted(mirrored, key=lambda row: row["stratification_id"])
    require_equal(actual, expected, "finite-moduli stratifications mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        semistable, _scalar_by_substack, e_translation_by_substack = load_inputs(
            args.semistable_fixture,
            args.rigidification_fixture,
            args.e_translation_fixture,
        )
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        closed = verify_closed_substacks(
            tables["retained_closed_substacks.csv"],
            semistable,
            e_translation_by_substack,
        )
        covers = verify_covers(tables["closed_cover_rows.csv"], closed)
        stratifications = verify_stratifications(tables["stratifications.csv"], covers)
        verify_relations(tables["formal_relations.csv"], len(stratifications))
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["stratifications.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_CLOSED_SUBSTACKS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
