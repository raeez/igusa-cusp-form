#!/usr/bin/env python3
"""AP/Liu heart-compatibility gate.

This verifier checks the packet proving that the retained
Abramovich--Polishchuk/Liu heart is Liu's torsion-pair tilt of the
Abramovich--Polishchuk global heart.  It certifies only the equality
of hearts used by the retained Hall rows.

It does not prove noetherianity, Harder--Narasimhan filtrations,
bounded HN types, finite-type semistable substacks, derived
enhancements, compact Hall stages, Pfaffian orientations, or
protected traces.
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
SUCCESS_STATUS = "AP_LIU_COMPATIBILITY_VERIFIED"
EXPECTED_KIND = "ap_liu_compatibility"
DEFAULT_FIXTURE = Path("certificates/moduli/ap_liu_compatibility")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_IDENTIFICATIONS = frozenset(
    {
        "ap_heart_input",
        "tilt_inside_ap",
        "heart_of_sigma",
        "retained_heart_equals_tilt",
    }
)
REQUIRED_FORMULAS = frozenset(
    {
        "ap_membership_formula",
        "Z_t_formula",
        "nu_t_formula",
        "torsion_pair_formula",
        "tilt_formula",
        "central_charge_formula",
    }
)
REQUIRED_RELATIONS = frozenset(
    {
        "ap_heart_formula_imported",
        "torsion_pair_in_ap_heart",
        "tilt_heart_defined",
        "heart_of_sigma_equals_tilt",
        "retained_heart_equals_liu_tilt",
        "ap_liu_compatibility",
        "noetherianity_not_proved",
        "hn_filtrations_not_proved",
        "bounded_hn_types_not_proved",
        "finite_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "retained_window_noetherianity",
        "retained_hn_filtrations",
        "bounded_hn_types",
        "finite_type_semistable_substacks",
        "quasi_smooth_moduli",
        "universal_complexes",
        "rigidifications",
        "inertia",
        "extension_flags",
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
        "compatibility_datum.csv",
        (
            "compatibility_id",
            "base_heart_symbol",
            "ap_heart_symbol",
            "liu_tilt_heart_symbol",
            "retained_heart_symbol",
            "stability_symbol",
            "compatibility_status",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "heart_identifications.csv",
        (
            "identification_id",
            "left_symbol",
            "right_symbol",
            "identification_kind",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "torsion_pair_rows.csv",
        (
            "torsion_row_id",
            "ambient_heart",
            "torsion_part",
            "free_part",
            "hom_vanishes",
            "short_exact_decomposition",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "formula_trace.csv",
        (
            "formula_id",
            "formula_kind",
            "formula_text",
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
    require_equal(manifest.get("ap_liu_compatibility"), True, "manifest ap_liu_compatibility")
    for key in (
        "noetherianity",
        "hn_filtrations",
        "bounded_hn_types",
        "finite_type_moduli",
        "semistable_substacks",
        "derived_moduli",
        "universal_complexes",
        "rigidifications",
        "inertia",
        "extension_flags",
        "cosection_atlas",
        "transitions",
        "compact_hall_stage",
        "pfaffian_orientation",
        "protected_trace",
    ):
        require_equal(manifest.get(key), False, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_compatibility(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "compatibility row count")
    row = rows[0]
    check_row(row, "compatibility_datum.csv")
    require_equal(row["compatibility_id"], "ap_liu_k3xe", "compatibility_id")
    require_equal(row["base_heart_symbol"], "A_S", "base_heart_symbol")
    require_equal(row["ap_heart_symbol"], "A_E^{AP}", "ap_heart_symbol")
    require_equal(row["liu_tilt_heart_symbol"], "A_E^t", "liu_tilt_heart_symbol")
    require_equal(row["retained_heart_symbol"], "A_X^{AP/Liu}", "retained_heart_symbol")
    require_equal(row["stability_symbol"], "sigma_{s,t}", "stability_symbol")
    require_equal(row["compatibility_status"], "heart_identification_verified", "compatibility_status")
    for key in ("LiuProductStability", "def:liu-product-stability-datum"):
        if key not in row["source_reference"]:
            raise ValueError(f"compatibility_datum.csv: missing source anchor {key}")


def verify_identifications(rows: list[dict[str, str]]) -> None:
    expected = {
        "ap_heart_input": ("A_E^{AP}", "AP global heart", "source_imported_definition"),
        "tilt_inside_ap": ("A_E^t", "<T_t,F_t[1]> in A_E^{AP}", "torsion_pair_tilt"),
        "heart_of_sigma": ("heart(sigma_{s,t})", "A_E^t", "liu_stability_heart"),
        "retained_heart_equals_tilt": ("A_X^{AP/Liu}", "A_E^t", "retained_definition"),
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "heart_identifications.csv")
        identification_id = row["identification_id"]
        if identification_id in seen:
            raise ValueError(f"heart_identifications.csv: duplicate id {identification_id}")
        seen.add(identification_id)
        if identification_id not in expected:
            raise ValueError(f"heart_identifications.csv: unexpected id {identification_id}")
        left, right, kind = expected[identification_id]
        require_equal(row["left_symbol"], left, f"{identification_id} left")
        require_equal(row["right_symbol"], right, f"{identification_id} right")
        require_equal(row["identification_kind"], kind, f"{identification_id} kind")
    require_equal(seen, REQUIRED_IDENTIFICATIONS, "heart identification coverage")


def verify_torsion_pair(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "torsion pair row count")
    row = rows[0]
    check_row(row, "torsion_pair_rows.csv")
    require_equal(row["torsion_row_id"], "liu_torsion_pair", "torsion_row_id")
    require_equal(row["ambient_heart"], "A_E^{AP}", "ambient_heart")
    require_equal(row["torsion_part"], "T_t={nu_t,min>0}", "torsion_part")
    require_equal(row["free_part"], "F_t={nu_t,max<=0}", "free_part")
    require_equal(bool_cell(row, "hom_vanishes"), True, "hom_vanishes")
    require_equal(bool_cell(row, "short_exact_decomposition"), True, "short_exact_decomposition")
    require_zero(int_cell(row, "defect_rank"), "torsion pair defect_rank")


def verify_formulas(rows: list[dict[str, str]]) -> None:
    expected = {
        "ap_membership_formula": "A_E^{AP}={M | p_*(M tensor q^*L_E^n) in A_S for n>>0}",
        "Z_t_formula": "Z_t=a*t-d+i*c*t",
        "nu_t_formula": "nu_t=(-a*t+d)/(c*t); infinity if c=0",
        "torsion_pair_formula": "T_t={nu_t,min>0}; F_t={nu_t,max<=0}",
        "tilt_formula": "A_E^t=<T_t,F_t[1]>",
        "central_charge_formula": "Z_E^{s,t}=c*s+b+i(-a*t+d)",
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formula_trace.csv")
        formula_id = row["formula_id"]
        if formula_id in seen:
            raise ValueError(f"formula_trace.csv: duplicate formula_id {formula_id}")
        seen.add(formula_id)
        if formula_id not in expected:
            raise ValueError(f"formula_trace.csv: unexpected formula_id {formula_id}")
        require_equal(row["formula_text"], expected[formula_id], f"{formula_id} formula")
    require_equal(seen, REQUIRED_FORMULAS, "formula trace coverage")


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


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        verify_compatibility(tables["compatibility_datum.csv"])
        verify_identifications(tables["heart_identifications.csv"])
        verify_torsion_pair(tables["torsion_pair_rows.csv"])
        verify_formulas(tables["formula_trace.csv"])
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"AP_LIU_COMPATIBILITY_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
