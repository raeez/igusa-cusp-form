#!/usr/bin/env python3
"""Finite-type retained semistable-substack gate.

This verifier checks the item-167 packet: for each retained semistable
HN factor type in the active window, a finite-type semistable substack
is cut inside a bounded Quot/Postnikov ambient chart.

It does not construct derived enhancements, universal complexes,
rigidifications, inertia strata, extension/flag stacks, cosection
atlases, transitions, Pfaffian orientations, or protected traces.
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
SUCCESS_STATUS = "RETAINED_SEMISTABLE_SUBSTACKS_VERIFIED"
EXPECTED_KIND = "retained_semistable_substacks"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
DEFAULT_HN_TYPE_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
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
HN_TYPE_COLUMNS = (
    "type_id",
    "hn_height",
    "charge_id",
    "amplitude_bounds",
    "hilbert_polynomial_id",
    "regularity_bound",
    "closure_family_id",
    "extension_closure_defect_rank",
    "finite_type_status",
    "geometric_source_id",
    "proof_reference",
    "check_status",
    "notes",
)
REQUIRED_RELATIONS = frozenset(
    {
        "bounded_hn_types_imported",
        "ambient_quot_postnikov_charts_finite_type",
        "one_substack_per_retained_class",
        "semistability_defects_zero",
        "boundedness_defects_zero",
        "specialization_closed",
        "finite_type_semistable_substacks",
        "derived_moduli_not_proved",
        "universal_complexes_not_proved",
        "rigidification_not_proved",
        "finite_hall_stage_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "quasi_smooth_moduli",
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
        "ambient_charts.csv",
        (
            "chart_id",
            "type_id",
            "ambient_stack_id",
            "chart_kind",
            "finite_type_status",
            "postnikov_bound",
            "regularity_bound",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS),
    TableSpec(
        "class_coverage.csv",
        (
            "coverage_id",
            "window_id",
            "type_id",
            "substack_id",
            "charge_id",
            "hilbert_polynomial_id",
            "coverage_defect_rank",
            "boundedness_defect_rank",
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
    parser.add_argument("--hn-type-fixture", type=Path, default=DEFAULT_HN_TYPE_FIXTURE)
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


def read_hn_types(fixture: Path) -> list[dict[str, str]]:
    return read_table(fixture, TableSpec("hn_type_bounds.csv", HN_TYPE_COLUMNS))


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
    require_equal(manifest.get("bounded_hn_types_required"), True, "manifest bounded_hn_types_required")
    require_equal(
        manifest.get("finite_type_semistable_substacks"),
        True,
        "manifest finite_type_semistable_substacks",
    )
    for key in (
        "complete_finite_moduli",
        "derived_moduli",
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


def verify_hn_type_inputs(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    by_type: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "hn_type_bounds.csv")
        type_id = row["type_id"]
        if type_id in by_type:
            raise ValueError(f"hn_type_bounds.csv: duplicate type_id {type_id}")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite_type_status")
        require_zero(int_cell(row, "extension_closure_defect_rank"), f"{type_id} extension_closure_defect")
        by_type[type_id] = row
    return by_type


def verify_ambient(rows: list[dict[str, str]], retained_types: set[str]) -> dict[str, dict[str, str]]:
    by_type: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "ambient_charts.csv")
        type_id = row["type_id"]
        if type_id in by_type:
            raise ValueError(f"ambient_charts.csv: duplicate type_id {type_id}")
        if type_id not in retained_types:
            raise ValueError(f"ambient_charts.csv: unexpected type_id {type_id}")
        require_equal(row["chart_kind"], "bounded_quot_postnikov", f"{type_id} chart_kind")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite_type_status")
        if int_cell(row, "postnikov_bound") < 0:
            raise ValueError(f"ambient_charts.csv: postnikov_bound must be nonnegative in {row}")
        if int_cell(row, "regularity_bound") < 0:
            raise ValueError(f"ambient_charts.csv: regularity_bound must be nonnegative in {row}")
        by_type[type_id] = row
    require_equal(set(by_type), retained_types, "ambient chart coverage")
    return by_type


def verify_semistable_rows(
    rows: list[dict[str, str]],
    retained_types: set[str],
    ambient_by_type: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    by_type: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "semistable_substacks.csv")
        type_id = row["type_id"]
        if type_id in by_type:
            raise ValueError(f"semistable_substacks.csv: duplicate type_id {type_id}")
        if type_id not in retained_types:
            raise ValueError(f"semistable_substacks.csv: unexpected type_id {type_id}")
        ambient = ambient_by_type[type_id]
        require_equal(row["ambient_stack_id"], ambient["ambient_stack_id"], f"{type_id} ambient")
        require_equal(row["quot_postnikov_chart_id"], ambient["chart_id"], f"{type_id} chart")
        require_equal(row["stability_id"], "sigma_st", f"{type_id} stability_id")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite_type_status")
        require_equal(bool_cell(row, "specialization_closed"), True, f"{type_id} specialization_closed")
        require_zero(int_cell(row, "semistability_defect_rank"), f"{type_id} semistability_defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{type_id} boundedness_defect")
        by_type[type_id] = row
    require_equal(set(by_type), retained_types, "semistable substack coverage")
    return by_type


def verify_coverage(
    rows: list[dict[str, str]],
    retained_types: dict[str, dict[str, str]],
    substacks_by_type: dict[str, dict[str, str]],
) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "class_coverage.csv")
        type_id = row["type_id"]
        if type_id in seen:
            raise ValueError(f"class_coverage.csv: duplicate type_id {type_id}")
        seen.add(type_id)
        if type_id not in retained_types:
            raise ValueError(f"class_coverage.csv: unexpected type_id {type_id}")
        hn_row = retained_types[type_id]
        require_equal(row["substack_id"], substacks_by_type[type_id]["substack_id"], f"{type_id} substack_id")
        require_equal(row["charge_id"], hn_row["charge_id"], f"{type_id} charge_id")
        require_equal(
            row["hilbert_polynomial_id"],
            hn_row["hilbert_polynomial_id"],
            f"{type_id} hilbert_polynomial_id",
        )
        require_zero(int_cell(row, "coverage_defect_rank"), f"{type_id} coverage_defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{type_id} boundedness_defect")
    require_equal(seen, set(retained_types), "class coverage")


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


def verify_finite_moduli_mirror(
    finite_moduli_fixture: Path,
    semistable_rows: list[dict[str, str]],
) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS))
    expected = sorted(semistable_rows, key=lambda row: row["substack_id"])
    actual = sorted(mirrored, key=lambda row: row["substack_id"])
    require_equal(actual, expected, "finite-moduli semistable_substacks mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        retained_types = verify_hn_type_inputs(read_hn_types(args.hn_type_fixture))
        ambient_by_type = verify_ambient(tables["ambient_charts.csv"], set(retained_types))
        substacks_by_type = verify_semistable_rows(
            tables["semistable_substacks.csv"],
            set(retained_types),
            ambient_by_type,
        )
        verify_coverage(tables["class_coverage.csv"], retained_types, substacks_by_type)
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, tables["semistable_substacks.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_SEMISTABLE_SUBSTACKS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
