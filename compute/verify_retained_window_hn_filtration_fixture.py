#!/usr/bin/env python3
"""Finite retained-window Harder--Narasimhan filtration gate.

This verifier checks the finite HN-filtration statement used for
retained windows in the Abramovich--Polishchuk/Liu heart.  It certifies
that a supplied finite exact window carries explicit filtration chains
whose quotients are semistable and whose phases strictly decrease.

It does not prove the global AP/Liu heart has HN filtrations, does not
prove bounded HN types, and does not construct finite-type moduli.
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
SUCCESS_STATUS = "RETAINED_WINDOW_HN_FILTRATION_VERIFIED"
EXPECTED_KIND = "retained_window_hn_filtration_finite_exact_category"
DEFAULT_FIXTURE = Path("certificates/moduli/retained_window_hn_filtration")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "finite_object_set",
        "finite_phase_set",
        "semistable_factor_rows",
        "exact_quotient_steps",
        "all_objects_hn_filtration",
        "all_nonzero_objects_hn_filtration",
        "strict_phase_descent",
        "length_additivity",
        "retained_window_hn_filtration",
        "global_hn_not_proved",
        "bounded_hn_types_not_proved",
        "finite_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "global_ap_liu_noetherianity",
        "global_ap_liu_hn_filtrations",
        "bounded_hn_types",
        "finite_type_semistable_substacks",
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
class ObjectDatum:
    length: int
    is_zero: bool
    semistable: bool
    phase: Fraction | None


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "window_hn_datum.csv",
        (
            "window_id",
            "heart_id",
            "noetherian_window_id",
            "object_count",
            "phase_count",
            "finite_phase_set",
            "subobject_closed",
            "quotient_closed",
            "retained_window_noetherian",
            "global_hn_claim",
            "bounded_hn_type_claim",
            "finite_moduli_claim",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "object_stability.csv",
        (
            "object_id",
            "window_id",
            "class_id",
            "length_rank",
            "is_zero_object",
            "semistable",
            "phase_num",
            "phase_den",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "exact_quotient_steps.csv",
        (
            "step_id",
            "window_id",
            "object_id",
            "filtration_id",
            "step_order",
            "previous_object_id",
            "current_object_id",
            "quotient_object_id",
            "strict",
            "quotient_semistable",
            "quotient_phase_num",
            "quotient_phase_den",
            "length_defect_rank",
            "closure_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "hn_filtration_summary.csv",
        (
            "object_id",
            "window_id",
            "filtration_id",
            "factor_count",
            "expected_length_rank",
            "summed_factor_lengths",
            "phase_sequence",
            "strictly_descending",
            "hn_exists",
            "length_defect_rank",
            "phase_order_defect_rank",
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


def fraction_cell(row: dict[str, str], num_key: str, den_key: str) -> Fraction | None:
    num_text = row[num_key].strip()
    den_text = row[den_key].strip()
    if not num_text and not den_text:
        return None
    if not num_text or not den_text:
        raise ValueError(f"incomplete fraction in row {row}")
    num = int_cell(row, num_key)
    den = int_cell(row, den_key)
    if den <= 0:
        raise ValueError(f"{den_key} must be positive in row {row}")
    return Fraction(num, den)


def phase_text(phase: Fraction) -> str:
    return f"{phase.numerator}/{phase.denominator}"


def parse_phase_set(text: str) -> set[Fraction]:
    phases: set[Fraction] = set()
    for part in text.split(";"):
        token = part.strip()
        if not token:
            continue
        try:
            num_text, den_text = token.split("/", 1)
        except ValueError as exc:
            raise ValueError(f"bad phase token {token!r}") from exc
        num = int(num_text)
        den = int(den_text)
        if den <= 0:
            raise ValueError(f"bad phase denominator in token {token!r}")
        phases.add(Fraction(num, den))
    return phases


def check_row(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    if not row.get("source_reference", "").strip():
        raise ValueError(f"{table_name}: missing source_reference: {row}")
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
    require_equal(manifest.get("retained_window_noetherianity_required"), True, "manifest retained_window_noetherianity_required")
    require_equal(manifest.get("retained_window_hn_filtration"), True, "manifest retained_window_hn_filtration")
    require_equal(manifest.get("global_ap_liu_hn_filtrations"), False, "manifest global_ap_liu_hn_filtrations")
    require_equal(manifest.get("bounded_hn_types"), False, "manifest bounded_hn_types")
    require_equal(manifest.get("finite_type_moduli"), False, "manifest finite_type_moduli")
    require_equal(manifest.get("derived_moduli"), False, "manifest derived_moduli")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_window(rows: list[dict[str, str]]) -> tuple[str, int, set[Fraction]]:
    require_equal(len(rows), 1, "window row count")
    row = rows[0]
    check_row(row, "window_hn_datum.csv")
    window_id = row["window_id"]
    object_count = int_cell(row, "object_count")
    phase_count = int_cell(row, "phase_count")
    if object_count <= 0:
        raise ValueError("window object_count must be positive")
    phases = parse_phase_set(row["finite_phase_set"])
    require_equal(len(phases), phase_count, "window phase_count")
    require_equal(bool_cell(row, "subobject_closed"), True, "window subobject_closed")
    require_equal(bool_cell(row, "quotient_closed"), True, "window quotient_closed")
    require_equal(bool_cell(row, "retained_window_noetherian"), True, "window retained_window_noetherian")
    require_equal(bool_cell(row, "global_hn_claim"), False, "window global_hn_claim")
    require_equal(bool_cell(row, "bounded_hn_type_claim"), False, "window bounded_hn_type_claim")
    require_equal(bool_cell(row, "finite_moduli_claim"), False, "window finite_moduli_claim")
    return window_id, object_count, phases


def verify_objects(
    rows: list[dict[str, str]],
    window_id: str,
    object_count: int,
    declared_phases: set[Fraction],
) -> dict[str, ObjectDatum]:
    objects: dict[str, ObjectDatum] = {}
    zero_count = 0
    semistable_phases: set[Fraction] = set()
    for row in rows:
        check_row(row, "object_stability.csv")
        require_equal(row["window_id"], window_id, f"{row['object_id']} window")
        object_id = row["object_id"]
        if object_id in objects:
            raise ValueError(f"object_stability.csv: duplicate object_id {object_id}")
        length = int_cell(row, "length_rank")
        if length < 0:
            raise ValueError(f"object_stability.csv: negative length in {row}")
        is_zero = bool_cell(row, "is_zero_object")
        semistable = bool_cell(row, "semistable")
        phase = fraction_cell(row, "phase_num", "phase_den")
        if is_zero:
            zero_count += 1
            require_equal(length, 0, f"{object_id} zero length")
            if phase is not None:
                raise ValueError(f"object_stability.csv: zero object has a phase in {row}")
        elif length == 0:
            raise ValueError(f"object_stability.csv: nonzero object has length 0 in {row}")
        elif phase is None:
            raise ValueError(f"object_stability.csv: nonzero object lacks phase in {row}")
        if semistable:
            if is_zero:
                raise ValueError(f"object_stability.csv: zero object marked semistable in {row}")
            if phase is None:
                raise ValueError(f"object_stability.csv: semistable object lacks phase in {row}")
            semistable_phases.add(phase)
        objects[object_id] = ObjectDatum(
            length=length,
            is_zero=is_zero,
            semistable=semistable,
            phase=phase,
        )
    require_equal(len(objects), object_count, "object_count")
    require_equal(zero_count, 1, "zero object count")
    require_equal(semistable_phases, declared_phases, "finite semistable phase set")
    return objects


def verify_steps(
    rows: list[dict[str, str]],
    window_id: str,
    objects: dict[str, ObjectDatum],
) -> dict[str, list[dict[str, str]]]:
    grouped: dict[str, list[dict[str, str]]] = {}
    seen_steps: set[str] = set()
    for row in rows:
        check_row(row, "exact_quotient_steps.csv")
        step_id = row["step_id"]
        if step_id in seen_steps:
            raise ValueError(f"exact_quotient_steps.csv: duplicate step_id {step_id}")
        seen_steps.add(step_id)
        require_equal(row["window_id"], window_id, f"{step_id} window")
        for key in ("object_id", "previous_object_id", "current_object_id", "quotient_object_id"):
            if row[key] not in objects:
                raise ValueError(f"exact_quotient_steps.csv: unknown {key}={row[key]}")
        require_equal(bool_cell(row, "strict"), True, f"{step_id} strict")
        quotient = objects[row["quotient_object_id"]]
        require_equal(bool_cell(row, "quotient_semistable"), True, f"{step_id} quotient_semistable flag")
        require_equal(quotient.semistable, True, f"{step_id} quotient object semistable")
        quotient_phase = fraction_cell(row, "quotient_phase_num", "quotient_phase_den")
        require_equal(quotient_phase, quotient.phase, f"{step_id} quotient phase")
        previous = objects[row["previous_object_id"]]
        current = objects[row["current_object_id"]]
        if not previous.length < current.length:
            raise ValueError(f"{step_id}: filtration step is not strict in length")
        expected_current_length = previous.length + quotient.length
        require_equal(current.length, expected_current_length, f"{step_id} exact length")
        require_zero(int_cell(row, "length_defect_rank"), f"{step_id} length_defect")
        require_zero(int_cell(row, "closure_defect_rank"), f"{step_id} closure_defect")
        grouped.setdefault(row["object_id"], []).append(row)
    return grouped


def verify_summaries(
    rows: list[dict[str, str]],
    window_id: str,
    objects: dict[str, ObjectDatum],
    grouped_steps: dict[str, list[dict[str, str]]],
) -> tuple[int, int, int]:
    seen: set[str] = set()
    nonzero_hn_count = 0
    strict_descent_count = 0
    total_steps = 0
    for row in rows:
        check_row(row, "hn_filtration_summary.csv")
        object_id = row["object_id"]
        if object_id in seen:
            raise ValueError(f"hn_filtration_summary.csv: duplicate object_id {object_id}")
        seen.add(object_id)
        if object_id not in objects:
            raise ValueError(f"hn_filtration_summary.csv: unknown object_id {object_id}")
        require_equal(row["window_id"], window_id, f"{object_id} summary window")
        obj = objects[object_id]
        factor_count = int_cell(row, "factor_count")
        expected_length = int_cell(row, "expected_length_rank")
        summed_length = int_cell(row, "summed_factor_lengths")
        require_equal(expected_length, obj.length, f"{object_id} expected_length")
        require_equal(summed_length, obj.length, f"{object_id} summed length")
        require_equal(bool_cell(row, "hn_exists"), True, f"{object_id} hn_exists")
        require_zero(int_cell(row, "length_defect_rank"), f"{object_id} summary length_defect")
        require_zero(int_cell(row, "phase_order_defect_rank"), f"{object_id} summary phase_order_defect")
        steps = sorted(grouped_steps.get(object_id, []), key=lambda item: int_cell(item, "step_order"))
        require_equal(factor_count, len(steps), f"{object_id} factor_count")
        if obj.is_zero:
            require_equal(factor_count, 0, f"{object_id} zero factor_count")
            require_equal(row["phase_sequence"], "empty", f"{object_id} phase_sequence")
            require_equal(bool_cell(row, "strictly_descending"), True, f"{object_id} strictly_descending")
            continue
        if factor_count == 0:
            raise ValueError(f"{object_id}: nonzero object has no HN factors")
        nonzero_hn_count += 1
        require_equal(row["filtration_id"], steps[0]["filtration_id"], f"{object_id} filtration_id")
        require_equal(steps[0]["previous_object_id"], "zero", f"{object_id} first previous")
        require_equal(steps[-1]["current_object_id"], object_id, f"{object_id} last current")
        factor_lengths = 0
        phases: list[Fraction] = []
        for index, step in enumerate(steps, start=1):
            require_equal(int_cell(step, "step_order"), index, f"{object_id} step order")
            if index > 1:
                previous_current = steps[index - 2]["current_object_id"]
                require_equal(step["previous_object_id"], previous_current, f"{object_id} step continuity")
            quotient = objects[step["quotient_object_id"]]
            factor_lengths += quotient.length
            if quotient.phase is None:
                raise ValueError(f"{object_id}: quotient has no phase in step {step['step_id']}")
            phases.append(quotient.phase)
        require_equal(factor_lengths, obj.length, f"{object_id} factor length sum")
        phase_sequence = ">".join(phase_text(phase) for phase in phases)
        require_equal(row["phase_sequence"], phase_sequence, f"{object_id} phase_sequence")
        strictly_descending = all(left > right for left, right in zip(phases, phases[1:]))
        require_equal(bool_cell(row, "strictly_descending"), strictly_descending, f"{object_id} strict descent flag")
        if not strictly_descending:
            raise ValueError(f"{object_id}: HN phases are not strictly descending")
        strict_descent_count += 1
        total_steps += len(steps)
    require_equal(seen, set(objects), "HN summary coverage")
    return len(seen), nonzero_hn_count, strict_descent_count


def verify_relations(
    rows: list[dict[str, str]],
    object_count: int,
    phase_count: int,
    semistable_count: int,
    step_count: int,
    summary_count: int,
    nonzero_hn_count: int,
    strict_descent_count: int,
) -> None:
    relation_values = {
        "finite_object_set": object_count,
        "finite_phase_set": phase_count,
        "semistable_factor_rows": semistable_count,
        "exact_quotient_steps": step_count,
        "all_objects_hn_filtration": summary_count,
        "all_nonzero_objects_hn_filtration": nonzero_hn_count,
        "strict_phase_descent": strict_descent_count,
        "length_additivity": step_count,
        "retained_window_hn_filtration": 1,
        "global_hn_not_proved": 1,
        "bounded_hn_types_not_proved": 1,
        "finite_moduli_not_proved": 1,
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
        window_id, object_count, phases = verify_window(tables["window_hn_datum.csv"])
        objects = verify_objects(tables["object_stability.csv"], window_id, object_count, phases)
        grouped_steps = verify_steps(tables["exact_quotient_steps.csv"], window_id, objects)
        summary_count, nonzero_hn_count, strict_descent_count = verify_summaries(
            tables["hn_filtration_summary.csv"],
            window_id,
            objects,
            grouped_steps,
        )
        semistable_count = sum(1 for datum in objects.values() if datum.semistable)
        verify_relations(
            tables["formal_relations.csv"],
            object_count,
            len(phases),
            semistable_count,
            len(tables["exact_quotient_steps.csv"]),
            summary_count,
            nonzero_hn_count,
            strict_descent_count,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"RETAINED_WINDOW_HN_FILTRATION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
