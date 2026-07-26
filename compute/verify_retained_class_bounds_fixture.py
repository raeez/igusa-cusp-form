#!/usr/bin/env python3
"""Retained finite class-bound gate.

This verifier checks rows 170--173 of the optimization ledger: the
retained finite class set C_R, Hilbert-polynomial labels P_{c,i},
cohomological amplitude bounds [a_c,b_c], and finite regularity bounds
N_c.  It imports the retained HN type-bound rows and the retained
semistable-substack rows.

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
SUCCESS_STATUS = "RETAINED_CLASS_BOUNDS_VERIFIED"
EXPECTED_KIND = "retained_class_bounds"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_class_bounds")
DEFAULT_HN_TYPE_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
DEFAULT_SEMISTABLE_FIXTURE = Path("certificates/moduli/retained_semistable_substacks")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})

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
REQUIRED_RELATIONS = frozenset(
    {
        "finite_class_set",
        "one_class_per_retained_type",
        "semistable_substacks_imported",
        "hilbert_polynomial_bounds_defined",
        "cohomological_amplitude_bounds_defined",
        "finite_regularity_bounds",
        "finite_moduli_rows_mirrored",
        "universal_complexes_not_proved",
        "finite_hall_stage_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "global_classification",
        "finite_type_moduli",
        "universal_complexes",
        "finite_inertia_stratifications",
        "extension_flag_stacks",
        "cosection_atlas",
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
    TableSpec("class_set.csv", CLASS_COLUMNS),
    TableSpec(
        "hilbert_polynomial_bounds.csv",
        (
            "bound_id",
            "class_id",
            "hilbert_polynomial_id",
            "hp_index_count",
            "finite_hilbert_bound",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "amplitude_bounds.csv",
        (
            "bound_id",
            "class_id",
            "amplitude_bounds",
            "lower_amplitude",
            "upper_amplitude",
            "finite_amplitude_bound",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "regularity_bounds.csv",
        (
            "bound_id",
            "class_id",
            "regularity_bound",
            "finite_regularity_bound",
            "defect_rank",
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
    parser.add_argument("--semistable-fixture", type=Path, default=DEFAULT_SEMISTABLE_FIXTURE)
    parser.add_argument(
        "--finite-moduli-fixture",
        type=Path,
        default=DEFAULT_FINITE_MODULI_FIXTURE,
    )
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
                f"{spec.path}: expected columns {spec.columns}, "
                f"got {tuple(reader.fieldnames or ())}"
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
    require_equal(manifest.get("finite_class_set"), True, "manifest finite_class_set")
    require_equal(
        manifest.get("hilbert_polynomial_bounds"),
        True,
        "manifest hilbert_polynomial_bounds",
    )
    require_equal(
        manifest.get("cohomological_amplitude_bounds"),
        True,
        "manifest cohomological_amplitude_bounds",
    )
    require_equal(manifest.get("finite_regularity_bounds"), True, "manifest finite_regularity_bounds")
    require_equal(
        manifest.get("finite_type_semistable_substacks_required"),
        True,
        "manifest finite_type_semistable_substacks_required",
    )
    for key in (
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


def read_hn_type_bounds(fixture: Path) -> dict[str, dict[str, str]]:
    rows = read_table(fixture, TableSpec("hn_type_bounds.csv", HN_TYPE_COLUMNS))
    by_type: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "hn_type_bounds.csv")
        type_id = row["type_id"]
        if type_id in by_type:
            raise ValueError(f"hn_type_bounds.csv: duplicate type_id {type_id}")
        if int_cell(row, "regularity_bound") < 0:
            raise ValueError(f"hn_type_bounds.csv: negative regularity bound in {row}")
        require_zero(int_cell(row, "extension_closure_defect_rank"), f"{type_id} closure defect")
        by_type[type_id] = row
    return by_type


def read_semistable_substacks(fixture: Path) -> dict[str, dict[str, str]]:
    rows = read_table(fixture, TableSpec("semistable_substacks.csv", SEMISTABLE_COLUMNS))
    by_type: dict[str, dict[str, str]] = {}
    for row in rows:
        check_row(row, "semistable_substacks.csv")
        type_id = row["type_id"]
        if type_id in by_type:
            raise ValueError(f"semistable_substacks.csv: duplicate type_id {type_id}")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite_type")
        require_equal(bool_cell(row, "specialization_closed"), True, f"{type_id} specialization_closed")
        require_zero(int_cell(row, "semistability_defect_rank"), f"{type_id} semistability defect")
        require_zero(int_cell(row, "boundedness_defect_rank"), f"{type_id} boundedness defect")
        by_type[type_id] = row
    return by_type


def verify_class_set(
    rows: list[dict[str, str]],
    hn_by_type: dict[str, dict[str, str]],
    semistable_by_type: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    classes: dict[str, dict[str, str]] = {}
    seen_types: set[str] = set()
    for row in rows:
        check_row(row, "class_set.csv")
        class_id = row["class_id"]
        if class_id in classes:
            raise ValueError(f"class_set.csv: duplicate class_id {class_id}")
        type_id = row["type_id"]
        if type_id in seen_types:
            raise ValueError(f"class_set.csv: duplicate type_id {type_id}")
        if type_id not in hn_by_type:
            raise ValueError(f"class_set.csv: unknown type_id {type_id}")
        if type_id not in semistable_by_type:
            raise ValueError(f"class_set.csv: missing semistable substack for {type_id}")
        hn_row = hn_by_type[type_id]
        substack = semistable_by_type[type_id]
        require_equal(row["charge_id"], hn_row["charge_id"], f"{class_id} charge")
        require_equal(
            row["hilbert_polynomial_id"],
            hn_row["hilbert_polynomial_id"],
            f"{class_id} Hilbert label",
        )
        require_equal(row["amplitude_bounds"], hn_row["amplitude_bounds"], f"{class_id} amplitude")
        require_equal(
            int_cell(row, "regularity_bound"),
            int_cell(hn_row, "regularity_bound"),
            f"{class_id} regularity",
        )
        require_equal(row["substack_id"], substack["substack_id"], f"{class_id} substack")
        require_equal(bool_cell(row, "retained_class"), True, f"{class_id} retained_class")
        classes[class_id] = row
        seen_types.add(type_id)
    require_equal(seen_types, set(hn_by_type), "retained class type coverage")
    return classes


def verify_hilbert_bounds(rows: list[dict[str, str]], classes: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "hilbert_polynomial_bounds.csv")
        class_id = row["class_id"]
        if class_id in seen:
            raise ValueError(f"hilbert_polynomial_bounds.csv: duplicate class_id {class_id}")
        if class_id not in classes:
            raise ValueError(f"hilbert_polynomial_bounds.csv: unknown class_id {class_id}")
        require_equal(
            row["hilbert_polynomial_id"],
            classes[class_id]["hilbert_polynomial_id"],
            f"{class_id} Hilbert label",
        )
        if int_cell(row, "hp_index_count") <= 0:
            raise ValueError(f"hilbert_polynomial_bounds.csv: hp_index_count must be positive in {row}")
        require_equal(bool_cell(row, "finite_hilbert_bound"), True, f"{class_id} finite Hilbert")
        require_zero(int_cell(row, "defect_rank"), f"{class_id} Hilbert defect")
        seen.add(class_id)
    require_equal(seen, set(classes), "Hilbert-bound class coverage")


def verify_amplitude_bounds(rows: list[dict[str, str]], classes: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "amplitude_bounds.csv")
        class_id = row["class_id"]
        if class_id in seen:
            raise ValueError(f"amplitude_bounds.csv: duplicate class_id {class_id}")
        if class_id not in classes:
            raise ValueError(f"amplitude_bounds.csv: unknown class_id {class_id}")
        require_equal(row["amplitude_bounds"], classes[class_id]["amplitude_bounds"], f"{class_id} amplitude")
        lower = int_cell(row, "lower_amplitude")
        upper = int_cell(row, "upper_amplitude")
        if lower > upper:
            raise ValueError(f"amplitude_bounds.csv: lower_amplitude exceeds upper_amplitude in {row}")
        require_equal(bool_cell(row, "finite_amplitude_bound"), True, f"{class_id} finite amplitude")
        require_zero(int_cell(row, "defect_rank"), f"{class_id} amplitude defect")
        seen.add(class_id)
    require_equal(seen, set(classes), "amplitude-bound class coverage")


def verify_regularity_bounds(rows: list[dict[str, str]], classes: dict[str, dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "regularity_bounds.csv")
        class_id = row["class_id"]
        if class_id in seen:
            raise ValueError(f"regularity_bounds.csv: duplicate class_id {class_id}")
        if class_id not in classes:
            raise ValueError(f"regularity_bounds.csv: unknown class_id {class_id}")
        bound = int_cell(row, "regularity_bound")
        if bound < 0:
            raise ValueError(f"regularity_bounds.csv: regularity_bound must be nonnegative in {row}")
        require_equal(bound, int_cell(classes[class_id], "regularity_bound"), f"{class_id} regularity")
        require_equal(bool_cell(row, "finite_regularity_bound"), True, f"{class_id} finite regularity")
        require_zero(int_cell(row, "defect_rank"), f"{class_id} regularity defect")
        seen.add(class_id)
    require_equal(seen, set(classes), "regularity-bound class coverage")


def verify_relations(rows: list[dict[str, str]], class_count: int) -> None:
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
            "finite_class_set",
            "one_class_per_retained_type",
            "hilbert_polynomial_bounds_defined",
            "cohomological_amplitude_bounds_defined",
            "finite_regularity_bounds",
        }:
            require_equal(computed, class_count, f"{relation_id} count")
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


def verify_finite_moduli_mirror(
    finite_moduli_fixture: Path,
    hn_by_type: dict[str, dict[str, str]],
) -> None:
    mirrored = read_table(finite_moduli_fixture, TableSpec("hn_type_bounds.csv", HN_TYPE_COLUMNS))
    actual = {row["type_id"]: row for row in mirrored}
    require_equal(set(actual), set(hn_by_type), "finite-moduli HN-bound type coverage")
    for type_id, row in hn_by_type.items():
        require_equal(actual[type_id], row, f"{type_id} finite-moduli HN-bound mirror")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        hn_by_type = read_hn_type_bounds(args.hn_type_fixture)
        semistable_by_type = read_semistable_substacks(args.semistable_fixture)
        classes = verify_class_set(tables["class_set.csv"], hn_by_type, semistable_by_type)
        verify_hilbert_bounds(tables["hilbert_polynomial_bounds.csv"], classes)
        verify_amplitude_bounds(tables["amplitude_bounds.csv"], classes)
        verify_regularity_bounds(tables["regularity_bounds.csv"], classes)
        verify_relations(tables["formal_relations.csv"], len(classes))
        verify_firewall(tables["scalar_firewall.csv"])
        verify_finite_moduli_mirror(args.finite_moduli_fixture, hn_by_type)
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_CLASS_BOUNDS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
