#!/usr/bin/env python3
"""Chosen stability-heart datum gate.

This verifier checks the finite definition packet for the retained
Abramovich--Polishchuk/Liu heart used in the K3xE Hall construction.
It certifies only that the heart has been specified as a datum with its
inputs, references, and scalar firewalls.  It does not prove
noetherianity, Harder--Narasimhan filtrations, bounded HN types,
finite-type semistable substacks, or derived moduli.
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
SUCCESS_STATUS = "STABILITY_HEART_DATUM_VERIFIED"
EXPECTED_KIND = "chosen_stability_heart_datum"
DEFAULT_FIXTURE = Path("certificates/moduli/stability_heart")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_INPUTS = frozenset(
    {
        "polarized_k3_surface",
        "elliptic_curve_with_origin",
        "rational_k3_stability_condition",
        "degree_one_elliptic_line_bundle",
        "ap_product_t_structure",
        "liu_product_parameters",
        "liu_product_stability",
        "retained_hn_index_system",
    }
)
REQUIRED_RELATIONS = frozenset(
    {
        "heart_defined",
        "derived_category_named",
        "base_stability_named",
        "product_t_structure_named",
        "liu_product_stability_defined",
        "retained_sector_named",
        "noetherianity_not_proved",
        "hn_filtration_not_proved",
        "finite_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "noetherian_heart",
        "harder_narasimhan_filtrations",
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


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "heart_datum.csv",
        (
            "heart_id",
            "variety",
            "derived_category",
            "base_surface_stability",
            "product_t_structure",
            "product_stability",
            "heart_symbol",
            "definition_status",
            "noetherian_claim",
            "hn_filtration_claim",
            "finite_moduli_claim",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "heart_inputs.csv",
        (
            "input_id",
            "input_kind",
            "input_symbol",
            "required",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "retained_sector.csv",
        (
            "sector_id",
            "heart_id",
            "effective_semigroup_symbol",
            "object_condition",
            "hn_index_symbol",
            "finite_window_claim",
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
    require_equal(manifest.get("heart_defined"), True, "manifest heart_defined")
    require_equal(manifest.get("noetherianity"), False, "manifest noetherianity")
    require_equal(manifest.get("hn_filtrations"), False, "manifest hn_filtrations")
    require_equal(manifest.get("bounded_hn_types"), False, "manifest bounded_hn_types")
    require_equal(manifest.get("finite_type_moduli"), False, "manifest finite_type_moduli")
    require_equal(manifest.get("derived_moduli"), False, "manifest derived_moduli")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_heart(rows: list[dict[str, str]]) -> str:
    require_equal(len(rows), 1, "heart row count")
    row = rows[0]
    check_row(row, "heart_datum.csv")
    require_equal(row["variety"], "X=SxE", "heart variety")
    require_equal(row["derived_category"], "DbCoh(X)", "heart derived category")
    require_equal(row["definition_status"], "chosen_retained_heart", "heart definition_status")
    require_equal(bool_cell(row, "noetherian_claim"), False, "heart noetherian_claim")
    require_equal(bool_cell(row, "hn_filtration_claim"), False, "heart hn_filtration_claim")
    require_equal(bool_cell(row, "finite_moduli_claim"), False, "heart finite_moduli_claim")
    for key in ("AbramovichPolishchukTStructures", "LiuProductStability"):
        if key not in row["source_reference"]:
            raise ValueError(f"heart_datum.csv: missing citation key {key}")
    return row["heart_id"]


def verify_inputs(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "heart_inputs.csv")
        input_id = row["input_id"]
        if input_id in seen:
            raise ValueError(f"heart_inputs.csv: duplicate input_id {input_id}")
        seen.add(input_id)
        if input_id not in REQUIRED_INPUTS:
            raise ValueError(f"heart_inputs.csv: unexpected input_id {input_id}")
        require_equal(bool_cell(row, "required"), True, f"{input_id} required")
    require_equal(seen, REQUIRED_INPUTS, "heart input coverage")


def verify_retained_sector(rows: list[dict[str, str]], heart_id: str) -> None:
    require_equal(len(rows), 1, "retained sector row count")
    row = rows[0]
    check_row(row, "retained_sector.csv")
    require_equal(row["heart_id"], heart_id, "retained sector heart_id")
    require_equal(row["effective_semigroup_symbol"], "Gamma_X_sigma_eff", "effective semigroup")
    require_equal(row["hn_index_symbol"], "R_HN", "HN index symbol")
    require_equal(bool_cell(row, "finite_window_claim"), False, "retained sector finite_window_claim")


def verify_relations(rows: list[dict[str, str]]) -> None:
    relation_values = {
        "heart_defined": 1,
        "derived_category_named": 1,
        "base_stability_named": 1,
        "product_t_structure_named": 1,
        "liu_product_stability_defined": 1,
        "retained_sector_named": 1,
        "noetherianity_not_proved": 1,
        "hn_filtration_not_proved": 1,
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
        heart_id = verify_heart(tables["heart_datum.csv"])
        verify_inputs(tables["heart_inputs.csv"])
        verify_retained_sector(tables["retained_sector.csv"], heart_id)
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"STABILITY_HEART_DATUM_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
