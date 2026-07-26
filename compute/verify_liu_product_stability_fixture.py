#!/usr/bin/env python3
"""Liu product-stability definition gate.

This verifier checks the retained definition packet for Liu's product
stability condition on S x E.  It records the Abramovich--Polishchuk
global heart, the linear polynomial attached to the elliptic factor,
the weak charge Z_t, the torsion-pair tilt, and the final central
charge Z_E^{s,t}.

It does not prove finite-type semistable substacks, derived
enhancements, compact Hall stages, Pfaffian orientations, or protected
traces.
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
SUCCESS_STATUS = "LIU_PRODUCT_STABILITY_DEFINED"
EXPECTED_KIND = "liu_product_stability_definition"
DEFAULT_FIXTURE = Path("certificates/moduli/liu_product_stability")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_INPUTS = frozenset(
    {
        "base_smooth_projective_variety",
        "base_rational_stability",
        "central_charge_discrete_image",
        "product_smooth_projective_curve",
        "degree_one_elliptic_line_bundle",
        "positive_parameters",
    }
)
REQUIRED_RELATIONS = frozenset(
    {
        "base_rational_stability_named",
        "ap_heart_membership_formula",
        "polynomial_linear_on_curve",
        "coefficient_functionals_named",
        "weak_charge_zt_named",
        "nu_t_slope_named",
        "torsion_pair_named",
        "tilted_heart_named",
        "product_central_charge_named",
        "sigma_st_defined",
        "ap_compatibility_not_proved",
        "finite_moduli_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "ap_compatibility_theorem",
        "retained_window_noetherianity",
        "retained_hn_filtrations",
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
        "source_theorem.csv",
        (
            "source_id",
            "citation_key",
            "arxiv_id",
            "source_section",
            "source_theorem",
            "ap_heart_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "base_inputs.csv",
        (
            "input_id",
            "role",
            "symbol",
            "condition",
            "required",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "ap_heart_formula.csv",
        (
            "formula_id",
            "product_variety",
            "curve_line_bundle",
            "projection_p",
            "projection_q",
            "heart_symbol",
            "heart_membership_test",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "polynomial_coefficients.csv",
        (
            "coefficient_id",
            "object_symbol",
            "polynomial_symbol",
            "polynomial_formula",
            "coefficient_symbols",
            "curve_degree",
            "coefficient_group",
            "target_group",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "weak_charge_tilt.csv",
        (
            "tilt_id",
            "t_parameter",
            "weak_charge_formula",
            "slope_formula",
            "torsion_part",
            "free_part",
            "tilted_heart",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "product_charge.csv",
        (
            "product_id",
            "s_parameter",
            "t_parameter",
            "heart_symbol",
            "central_charge_formula",
            "stability_symbol",
            "parameter_domain",
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
    reference = row.get("source_reference", row.get("citation_key", ""))
    if not reference.strip():
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
    require_equal(manifest.get("liu_product_stability_defined"), True, "manifest liu_product_stability_defined")
    require_equal(manifest.get("ap_compatibility_proved"), False, "manifest ap_compatibility_proved")
    require_equal(manifest.get("finite_type_moduli"), False, "manifest finite_type_moduli")
    require_equal(manifest.get("derived_moduli"), False, "manifest derived_moduli")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_source(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "source row count")
    row = rows[0]
    check_row(row, "source_theorem.csv")
    require_equal(row["citation_key"], "LiuProductStability", "citation_key")
    require_equal(row["arxiv_id"], "1907.09326", "arxiv_id")
    require_equal(row["source_section"], "Section 4", "source_section")
    require_equal(row["source_theorem"], "Theorem 4.7", "source_theorem")
    if "AbramovichPolishchukTStructures" not in row["ap_heart_reference"]:
        raise ValueError("source_theorem.csv: AP reference missing")


def verify_inputs(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "base_inputs.csv")
        input_id = row["input_id"]
        if input_id in seen:
            raise ValueError(f"base_inputs.csv: duplicate input_id {input_id}")
        seen.add(input_id)
        if input_id not in REQUIRED_INPUTS:
            raise ValueError(f"base_inputs.csv: unexpected input_id {input_id}")
        require_equal(bool_cell(row, "required"), True, f"{input_id} required")
    require_equal(seen, REQUIRED_INPUTS, "base input coverage")


def verify_ap_heart(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "AP heart formula row count")
    row = rows[0]
    check_row(row, "ap_heart_formula.csv")
    require_equal(row["product_variety"], "SxE", "product_variety")
    require_equal(row["curve_line_bundle"], "L_E", "curve_line_bundle")
    require_equal(row["projection_p"], "p:SxE->S", "projection_p")
    require_equal(row["projection_q"], "q:SxE->E", "projection_q")
    require_equal(row["heart_symbol"], "A_E^{AP}", "heart_symbol")
    expected = "p_*(M tensor q^*L_E^n) in A_S for n>>0"
    require_equal(row["heart_membership_test"], expected, "heart_membership_test")


def verify_polynomial(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "polynomial row count")
    row = rows[0]
    check_row(row, "polynomial_coefficients.csv")
    require_equal(row["object_symbol"], "M", "object_symbol")
    require_equal(row["polynomial_symbol"], "L_M(n)", "polynomial_symbol")
    require_equal(row["polynomial_formula"], "a(M)n+b(M)+i(c(M)n+d(M))", "polynomial_formula")
    require_equal(row["coefficient_symbols"], "a,b,c,d", "coefficient_symbols")
    require_equal(int_cell(row, "curve_degree"), 1, "curve_degree")
    require_equal(row["coefficient_group"], "K(A_E^{AP})", "coefficient_group")
    require_equal(row["target_group"], "Q", "target_group")


def verify_tilt(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "tilt row count")
    row = rows[0]
    check_row(row, "weak_charge_tilt.csv")
    require_equal(row["t_parameter"], "t>0", "t_parameter")
    require_equal(row["weak_charge_formula"], "Z_t=a*t-d+i*c*t", "weak_charge_formula")
    require_equal(row["slope_formula"], "nu_t=(-a*t+d)/(c*t); infinity if c=0", "slope_formula")
    require_equal(row["torsion_part"], "T_t={nu_t,min>0}", "torsion_part")
    require_equal(row["free_part"], "F_t={nu_t,max<=0}", "free_part")
    require_equal(row["tilted_heart"], "A_E^t=<T_t,F_t[1]>", "tilted_heart")


def verify_product_charge(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "product charge row count")
    row = rows[0]
    check_row(row, "product_charge.csv")
    require_equal(row["s_parameter"], "s>0", "s_parameter")
    require_equal(row["t_parameter"], "t>0", "t_parameter")
    require_equal(row["heart_symbol"], "A_E^t", "heart_symbol")
    require_equal(row["central_charge_formula"], "Z_E^{s,t}=c*s+b+i(-a*t+d)", "central_charge_formula")
    require_equal(row["stability_symbol"], "sigma_{s,t}=(A_E^t,Z_E^{s,t})", "stability_symbol")
    require_equal(row["parameter_domain"], "Q_{>0}^2; continuous extension to R_{>0}^2", "parameter_domain")


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
        verify_source(tables["source_theorem.csv"])
        verify_inputs(tables["base_inputs.csv"])
        verify_ap_heart(tables["ap_heart_formula.csv"])
        verify_polynomial(tables["polynomial_coefficients.csv"])
        verify_tilt(tables["weak_charge_tilt.csv"])
        verify_product_charge(tables["product_charge.csv"])
        verify_relations(tables["formal_relations.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"LIU_PRODUCT_STABILITY_DEFINITION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
