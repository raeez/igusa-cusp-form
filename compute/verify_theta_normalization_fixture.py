#!/usr/bin/env python3
"""Exact scalar-normalization gate for Delta_5 leading constants.

This verifier checks only scalar arithmetic:

* the theta-leading coefficient 64 of Delta_5;
* the monic normalization D_5 = 64^{-1} Delta_5;
* the squared normalization 64^2 = 4096;
* the OP branch sign separated from the orientation character.

It does not construct a Pfaffian line, an O2 wall atlas, compact source
data, or a primitive-recognition theorem.
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
SUCCESS_STATUS = "SCALAR_NORMALIZATION_VERIFIED"
EXPECTED_KIND = "delta5_theta_leading_scalar_normalization"
FORBIDDEN_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "source_representative",
        "status_only",
        "todo",
        "unsupplied",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "pfaffian_line",
        "orientation_character",
        "o2_wall_atlas",
        "compact_source_trace",
        "primitive_recognition",
    }
)
BASE_DELTA5_LEADING = Fraction(64, 1)
REQUIRED_FORM_CONVENTIONS = {
    "Delta5": (Fraction(1, 1), 1, Fraction(64, 1), False),
    "D5": (Fraction(1, 64), 1, Fraction(1, 1), False),
    "Delta10_theta": (Fraction(1, 1), 2, Fraction(4096, 1), False),
    "chi10": (Fraction(1, 1), 2, Fraction(4096, 1), False),
    "Phi10_un": (Fraction(1, 1), 2, Fraction(4096, 1), False),
    "chi10_OP": (Fraction(1, 4096), 2, Fraction(1, 1), False),
    "Phi10_un_inverse": (Fraction(1, 1), -2, Fraction(1, 4096), True),
    "chi10_OP_inverse": (Fraction(4096, 1), -2, Fraction(1, 1), True),
    "Z_OP_scalar_branch": (Fraction(-4096, 1), -2, Fraction(-1, 1), True),
}
REQUIRED_FORM_RELATIONS = frozenset(
    {
        "delta10_is_delta5_square",
        "chi10_is_delta10",
        "phi10un_is_chi10",
        "chi10op_is_d5_square",
        "chi10op_is_scaled_delta10",
        "zbps_is_phi10un_inverse",
        "op_inverse_is_chi10op_inverse",
        "op_branch_is_negative_chi10op_inverse",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "normalizations.csv",
        (
            "normalization_id",
            "form_id",
            "leading_monomial",
            "scale_numerator",
            "scale_denominator",
            "base_leading",
            "normalized_leading",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "scalar_relations.csv",
        (
            "relation_id",
            "relation_kind",
            "input_a",
            "input_b",
            "computed_value",
            "expected_value",
            "residual",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "form_conventions.csv",
        (
            "form_id",
            "tex_name",
            "role",
            "base_form",
            "scale_numerator",
            "scale_denominator",
            "power",
            "leading_monomial",
            "leading_numerator",
            "leading_denominator",
            "is_partition_function",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "form_relations.csv",
        (
            "relation_id",
            "relation_kind",
            "left_form",
            "right_form",
            "scale_numerator",
            "scale_denominator",
            "computed_left_numerator",
            "computed_left_denominator",
            "computed_right_numerator",
            "computed_right_denominator",
            "residual_numerator",
            "residual_denominator",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "branch_separation.csv",
        (
            "branch_id",
            "scalar_branch",
            "sign_value",
            "orientation_character_value",
            "identified_with_orientation",
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
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/normalizations/delta5_theta_leading"),
    )
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


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("normalization_kind"), EXPECTED_KIND, "manifest normalization_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("scalar_arithmetic_certified"), True, "manifest scalar_arithmetic_certified")
    require_equal(manifest.get("form_conventions_certified"), True, "manifest form_conventions_certified")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("pfaffian_line"), False, "manifest pfaffian_line")
    require_equal(manifest.get("orientation_character"), False, "manifest orientation_character")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_normalizations(rows: list[dict[str, str]]) -> dict[str, int]:
    normalized: dict[str, int] = {}
    for row in rows:
        check_row(row, "normalizations.csv")
        scale = Fraction(int_cell(row, "scale_numerator"), int_cell(row, "scale_denominator"))
        base = int_cell(row, "base_leading")
        value = scale * base
        if value.denominator != 1:
            raise ValueError(f"{row['normalization_id']}: nonintegral normalized leading {value}")
        require_equal(int(value), int_cell(row, "normalized_leading"), f"{row['normalization_id']} normalized_leading")
        normalized[row["normalization_id"]] = int(value)

    required = {
        "Delta5_theta_leading": 64,
        "D5_monic_leading": 1,
        "Delta10_theta_square": 4096,
        "chi10_OP_monic": 1,
    }
    for key, value in required.items():
        require_equal(normalized.get(key), value, key)
    return normalized


def verify_relations(rows: list[dict[str, str]]) -> None:
    for row in rows:
        check_row(row, "scalar_relations.csv")
        kind = row["relation_kind"]
        input_a = int_cell(row, "input_a")
        input_b = int_cell(row, "input_b")
        if kind == "multiply":
            computed = input_a * input_b
        elif kind == "divide":
            if input_b == 0:
                raise ValueError(f"{row['relation_id']}: division by zero")
            quotient = Fraction(input_a, input_b)
            if quotient.denominator != 1:
                raise ValueError(f"{row['relation_id']}: nonintegral quotient {quotient}")
            computed = int(quotient)
        else:
            raise ValueError(f"{row['relation_id']}: unknown relation_kind {kind!r}")
        expected = int_cell(row, "expected_value")
        require_equal(int_cell(row, "computed_value"), computed, f"{row['relation_id']} computed_value")
        require_equal(computed, expected, f"{row['relation_id']} expected_value")
        require_equal(int_cell(row, "residual"), computed - expected, f"{row['relation_id']} residual")


def fraction_cell(row: dict[str, str], numerator_key: str, denominator_key: str) -> Fraction:
    denominator = int_cell(row, denominator_key)
    if denominator == 0:
        raise ValueError(f"{denominator_key} is zero in row {row}")
    return Fraction(int_cell(row, numerator_key), denominator)


def delta5_scaled_leading(scale: Fraction, power: int) -> Fraction:
    if power >= 0:
        return scale * (BASE_DELTA5_LEADING ** power)
    return scale / (BASE_DELTA5_LEADING ** (-power))


def verify_form_conventions(rows: list[dict[str, str]]) -> dict[str, Fraction]:
    leading: dict[str, Fraction] = {}
    roles: set[str] = set()
    for row in rows:
        check_row(row, "form_conventions.csv")
        form_id = row["form_id"]
        if form_id in leading:
            raise ValueError(f"form_conventions.csv: duplicate form_id {form_id}")
        if form_id not in REQUIRED_FORM_CONVENTIONS:
            raise ValueError(f"form_conventions.csv: unexpected form_id {form_id}")
        if row["role"] in roles:
            raise ValueError(f"form_conventions.csv: duplicate role {row['role']}")
        roles.add(row["role"])
        require_equal(row["base_form"], "Delta5", f"{form_id} base_form")

        scale = fraction_cell(row, "scale_numerator", "scale_denominator")
        power = int_cell(row, "power")
        computed = delta5_scaled_leading(scale, power)
        displayed = fraction_cell(row, "leading_numerator", "leading_denominator")
        required_scale, required_power, required_leading, required_partition = REQUIRED_FORM_CONVENTIONS[form_id]
        require_equal(scale, required_scale, f"{form_id} scale")
        require_equal(power, required_power, f"{form_id} power")
        require_equal(displayed, computed, f"{form_id} displayed leading")
        require_equal(computed, required_leading, f"{form_id} required leading")
        require_equal(bool_cell(row, "is_partition_function"), required_partition, f"{form_id} is_partition_function")
        leading[form_id] = computed

    require_equal(set(leading), set(REQUIRED_FORM_CONVENTIONS), "form convention coverage")
    return leading


def verify_form_relations(rows: list[dict[str, str]], leading: dict[str, Fraction]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "form_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"form_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_FORM_RELATIONS:
            raise ValueError(f"form_relations.csv: unexpected relation_id {relation_id}")
        left_form = row["left_form"]
        right_form = row["right_form"]
        if left_form not in leading or right_form not in leading:
            raise ValueError(f"{relation_id}: unknown form in relation")

        scale = fraction_cell(row, "scale_numerator", "scale_denominator")
        relation_kind = row["relation_kind"]
        if relation_kind == "same":
            right = scale * leading[right_form]
        elif relation_kind == "square":
            right = scale * leading[right_form] * leading[right_form]
        elif relation_kind == "inverse":
            if leading[right_form] == 0:
                raise ValueError(f"{relation_id}: inverse of zero leading term")
            right = scale / leading[right_form]
        else:
            raise ValueError(f"{relation_id}: unknown relation_kind {relation_kind!r}")
        left = leading[left_form]
        residual = left - right

        require_equal(fraction_cell(row, "computed_left_numerator", "computed_left_denominator"), left, f"{relation_id} left")
        require_equal(fraction_cell(row, "computed_right_numerator", "computed_right_denominator"), right, f"{relation_id} right")
        require_equal(fraction_cell(row, "residual_numerator", "residual_denominator"), residual, f"{relation_id} residual")
        require_equal(residual, Fraction(0, 1), f"{relation_id} residual zero")
    require_equal(seen, REQUIRED_FORM_RELATIONS, "form relation coverage")


def verify_branch_separation(rows: list[dict[str, str]]) -> None:
    for row in rows:
        check_row(row, "branch_separation.csv")
        require_equal(row["scalar_branch"], "OP_DT", f"{row['branch_id']} scalar_branch")
        require_equal(int_cell(row, "sign_value"), -1, f"{row['branch_id']} sign_value")
        require_equal(row["orientation_character_value"], "not_identified", f"{row['branch_id']} orientation_character_value")
        require_equal(bool_cell(row, "identified_with_orientation"), False, f"{row['branch_id']} identified_with_orientation")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"scalar_firewall.csv missing rows: {sorted(missing)}")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        verify_normalizations(tables["normalizations.csv"])
        verify_relations(tables["scalar_relations.csv"])
        leading = verify_form_conventions(tables["form_conventions.csv"])
        verify_form_relations(tables["form_relations.csv"], leading)
        verify_branch_separation(tables["branch_separation.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"THETA_NORMALIZATION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
