#!/usr/bin/env python3
"""Finite retained-window Harder--Narasimhan type-bound gate.

This verifier checks the bounded HN-type row for a retained active
window.  It certifies that the supplied finite HN factor set and the
bounded HN length give a finite set of HN type words, with Liu-Hilbert
labels recorded for the semistable factor types.

It does not construct finite-type semistable substacks, derived
enhancements, universal complexes, compact Hall stages, Pfaffian
orientations, or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "RETAINED_HN_TYPE_BOUNDS_VERIFIED"
EXPECTED_KIND = "retained_hn_type_bounds_finite_active_window"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_hn_type_bounds")
DEFAULT_FINITE_MODULI_FIXTURE = Path("certificates/moduli/k3e_finite_moduli")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
FINITE_MODULI_HN_COLUMNS = (
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
        "finite_hn_factor_type_set",
        "finite_hn_type_word_set",
        "bounded_hn_height",
        "bounded_factor_count",
        "bounded_length_rank",
        "all_retained_objects_bounded",
        "active_window_hn_type_bounded",
        "finite_moduli_not_proved",
        "semistable_substacks_not_proved",
        "derived_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "global_ap_liu_hn_type_boundedness",
        "finite_type_semistable_substacks",
        "hilbert_polynomial_formulas",
        "regularity_theorem",
        "quasi_smooth_moduli",
        "universal_complexes",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


@dataclass(frozen=True)
class FactorDatum:
    phase: Fraction
    length: int


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "active_window_bounds.csv",
        (
            "window_id",
            "hn_filtration_window_id",
            "noetherian_window_id",
            "max_hn_height",
            "max_factor_count",
            "max_length_rank",
            "factor_type_count",
            "hn_type_count",
            "finite_hn_type_set",
            "bounded_hn_type_claim",
            "global_boundedness_claim",
            "finite_moduli_claim",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hn_factor_types.csv",
        (
            "type_id",
            "factor_object_id",
            "phase_num",
            "phase_den",
            "length_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec("hn_type_bounds.csv", FINITE_MODULI_HN_COLUMNS),
    TableSpec(
        "object_hn_type_bounds.csv",
        (
            "object_id",
            "window_id",
            "hn_type_id",
            "type_sequence",
            "factor_count",
            "hn_height",
            "length_sum",
            "phase_sequence",
            "within_factor_bound",
            "within_height_bound",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "closure_bounds.csv",
        (
            "closure_id",
            "window_id",
            "closure_kind",
            "source_type_ids",
            "target_hn_type_id",
            "closure_defect_rank",
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
    parser.add_argument(
        "--finite-moduli-fixture",
        type=Path,
        default=DEFAULT_FINITE_MODULI_FIXTURE,
        help="fixture whose hn_type_bounds.csv must mirror the bounded HN row",
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
                f"{spec.path}: expected columns {spec.columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{spec.path}: unparsed CSV fields in row {row}")
    return rows


def read_finite_moduli_hn_bounds(fixture: Path) -> list[dict[str, str]]:
    spec = TableSpec("hn_type_bounds.csv", FINITE_MODULI_HN_COLUMNS)
    return read_table(fixture, spec)


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


def fraction_cell(row: dict[str, str], num_key: str, den_key: str) -> Fraction:
    num = int_cell(row, num_key)
    den = int_cell(row, den_key)
    if den <= 0:
        raise ValueError(f"{den_key} must be positive in row {row}")
    return Fraction(num, den)


def phase_text(phase: Fraction) -> str:
    return f"{phase.numerator}/{phase.denominator}"


def split_semicolon(text: str) -> list[str]:
    if text == "empty":
        return []
    return [part.strip() for part in text.split(";") if part.strip()]


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
    require_equal(manifest.get("retained_window_hn_filtration_required"), True, "manifest retained_window_hn_filtration_required")
    require_equal(manifest.get("bounded_hn_types"), True, "manifest bounded_hn_types")
    require_equal(manifest.get("global_ap_liu_bounded_hn_types"), False, "manifest global_ap_liu_bounded_hn_types")
    require_equal(manifest.get("finite_type_moduli"), False, "manifest finite_type_moduli")
    require_equal(manifest.get("derived_moduli"), False, "manifest derived_moduli")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_window(rows: list[dict[str, str]]) -> tuple[str, dict[str, int], set[str]]:
    require_equal(len(rows), 1, "active window row count")
    row = rows[0]
    check_row(row, "active_window_bounds.csv")
    window_id = row["window_id"]
    bounds = {
        "max_hn_height": int_cell(row, "max_hn_height"),
        "max_factor_count": int_cell(row, "max_factor_count"),
        "max_length_rank": int_cell(row, "max_length_rank"),
        "factor_type_count": int_cell(row, "factor_type_count"),
        "hn_type_count": int_cell(row, "hn_type_count"),
    }
    for key, value in bounds.items():
        if value < 0:
            raise ValueError(f"{key} must be nonnegative")
    finite_hn_types = set(split_semicolon(row["finite_hn_type_set"]))
    require_equal(len(finite_hn_types), bounds["hn_type_count"], "finite_hn_type_set size")
    require_equal(bool_cell(row, "bounded_hn_type_claim"), True, "bounded_hn_type_claim")
    require_equal(bool_cell(row, "global_boundedness_claim"), False, "global_boundedness_claim")
    require_equal(bool_cell(row, "finite_moduli_claim"), False, "finite_moduli_claim")
    return window_id, bounds, finite_hn_types


def verify_factor_types(rows: list[dict[str, str]], expected_count: int) -> dict[str, FactorDatum]:
    factors: dict[str, FactorDatum] = {}
    for row in rows:
        check_row(row, "hn_factor_types.csv")
        type_id = row["type_id"]
        if type_id in factors:
            raise ValueError(f"hn_factor_types.csv: duplicate type_id {type_id}")
        phase = fraction_cell(row, "phase_num", "phase_den")
        length = int_cell(row, "length_rank")
        if length <= 0:
            raise ValueError(f"hn_factor_types.csv: length_rank must be positive in {row}")
        factors[type_id] = FactorDatum(phase=phase, length=length)
    require_equal(len(factors), expected_count, "factor_type_count")
    return factors


def verify_hn_type_bounds(rows: list[dict[str, str]], factors: dict[str, FactorDatum]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "hn_type_bounds.csv")
        type_id = row["type_id"]
        if type_id in seen:
            raise ValueError(f"hn_type_bounds.csv: duplicate type_id {type_id}")
        seen.add(type_id)
        if type_id not in factors:
            raise ValueError(f"hn_type_bounds.csv: unknown factor type {type_id}")
        if int_cell(row, "hn_height") <= 0:
            raise ValueError(f"hn_type_bounds.csv: hn_height must be positive in {row}")
        if int_cell(row, "regularity_bound") < 0:
            raise ValueError(f"hn_type_bounds.csv: regularity_bound must be nonnegative in {row}")
        require_zero(int_cell(row, "extension_closure_defect_rank"), f"{type_id} extension_closure_defect")
        require_equal(row["finite_type_status"], "finite_type_verified", f"{type_id} finite_type_status")


def verify_object_bounds(
    rows: list[dict[str, str]],
    window_id: str,
    bounds: dict[str, int],
    finite_hn_types: set[str],
    factors: dict[str, FactorDatum],
) -> tuple[int, set[str]]:
    seen_objects: set[str] = set()
    seen_hn_types: set[str] = set()
    for row in rows:
        check_row(row, "object_hn_type_bounds.csv")
        object_id = row["object_id"]
        if object_id in seen_objects:
            raise ValueError(f"object_hn_type_bounds.csv: duplicate object_id {object_id}")
        seen_objects.add(object_id)
        require_equal(row["window_id"], window_id, f"{object_id} window")
        hn_type_id = row["hn_type_id"]
        if hn_type_id not in finite_hn_types:
            raise ValueError(f"object_hn_type_bounds.csv: unknown hn_type_id {hn_type_id}")
        seen_hn_types.add(hn_type_id)
        sequence = split_semicolon(row["type_sequence"])
        for type_id in sequence:
            if type_id not in factors:
                raise ValueError(f"object_hn_type_bounds.csv: unknown factor type {type_id}")
        factor_count = int_cell(row, "factor_count")
        hn_height = int_cell(row, "hn_height")
        length_sum = int_cell(row, "length_sum")
        require_equal(factor_count, len(sequence), f"{object_id} factor_count")
        require_equal(hn_height, factor_count, f"{object_id} hn_height")
        computed_length = sum(factors[type_id].length for type_id in sequence)
        require_equal(length_sum, computed_length, f"{object_id} length_sum")
        phases = [factors[type_id].phase for type_id in sequence]
        expected_phase_sequence = "empty" if not phases else ">".join(phase_text(phase) for phase in phases)
        require_equal(row["phase_sequence"], expected_phase_sequence, f"{object_id} phase_sequence")
        if any(left <= right for left, right in zip(phases, phases[1:])):
            raise ValueError(f"{object_id}: phases do not strictly descend")
        require_equal(bool_cell(row, "within_factor_bound"), True, f"{object_id} within_factor_bound")
        require_equal(bool_cell(row, "within_height_bound"), True, f"{object_id} within_height_bound")
        if factor_count > bounds["max_factor_count"]:
            raise ValueError(f"{object_id}: factor_count exceeds max_factor_count")
        if hn_height > bounds["max_hn_height"]:
            raise ValueError(f"{object_id}: hn_height exceeds max_hn_height")
        if length_sum > bounds["max_length_rank"]:
            raise ValueError(f"{object_id}: length_sum exceeds max_length_rank")
    require_equal(seen_hn_types, finite_hn_types, "HN type word coverage")
    return len(seen_objects), seen_hn_types


def verify_closure(rows: list[dict[str, str]], window_id: str, finite_hn_types: set[str], factors: dict[str, FactorDatum]) -> None:
    for row in rows:
        check_row(row, "closure_bounds.csv")
        require_equal(row["window_id"], window_id, f"{row['closure_id']} window")
        for type_id in split_semicolon(row["source_type_ids"]):
            if type_id not in factors and type_id not in finite_hn_types:
                raise ValueError(f"closure_bounds.csv: unknown source type {type_id}")
        if row["target_hn_type_id"] not in finite_hn_types:
            raise ValueError(f"closure_bounds.csv: unknown target_hn_type_id {row['target_hn_type_id']}")
        require_zero(int_cell(row, "closure_defect_rank"), f"{row['closure_id']} closure_defect")


def verify_relations(
    rows: list[dict[str, str]],
    factor_count: int,
    hn_type_count: int,
    bounds: dict[str, int],
    object_count: int,
) -> None:
    relation_values = {
        "finite_hn_factor_type_set": factor_count,
        "finite_hn_type_word_set": hn_type_count,
        "bounded_hn_height": bounds["max_hn_height"],
        "bounded_factor_count": bounds["max_factor_count"],
        "bounded_length_rank": bounds["max_length_rank"],
        "all_retained_objects_bounded": object_count,
        "active_window_hn_type_bounded": 1,
        "finite_moduli_not_proved": 1,
        "semistable_substacks_not_proved": 1,
        "derived_moduli_not_proved": 1,
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed")
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


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        finite_moduli_hn_rows = read_finite_moduli_hn_bounds(args.finite_moduli_fixture)
        require_equal(
            tables["hn_type_bounds.csv"],
            finite_moduli_hn_rows,
            "finite-moduli hn_type_bounds mirror",
        )
        window_id, bounds, finite_hn_types = verify_window(tables["active_window_bounds.csv"])
        factors = verify_factor_types(tables["hn_factor_types.csv"], bounds["factor_type_count"])
        verify_hn_type_bounds(tables["hn_type_bounds.csv"], factors)
        object_count, seen_hn_types = verify_object_bounds(
            tables["object_hn_type_bounds.csv"],
            window_id,
            bounds,
            finite_hn_types,
            factors,
        )
        verify_closure(tables["closure_bounds.csv"], window_id, seen_hn_types, factors)
        verify_relations(
            tables["formal_relations.csv"],
            len(factors),
            len(seen_hn_types),
            bounds,
            object_count,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_HN_TYPE_BOUNDS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
