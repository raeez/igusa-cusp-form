#!/usr/bin/env python3
"""Product-chamber and root-map gate for the Delta_5 denominator.

This verifier checks target-side cusp and root-map arithmetic:

* the type-II product chamber sectors defining Gamma_eff;
* closure of Gamma_eff by sector rules needed for product decompositions;
* alpha(n,l,m)=2n f_2-l f_3+2m f_-2;
* alpha(n,l,m)=n delta_1+m delta_2+(n+m-l) delta_3;
* active rows have n+m-l >= 0, while inactive rows have zero exponent;
* Z -> 2Z converts exp(-pi i (alpha,z)) to exp(-2 pi i (alpha,z)).

It does not construct compact source data, Pfaffian orientations, O2
wall atlases, mirror discriminants, or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from verify_square_root import phi_01_coefficients


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "PRODUCT_CHAMBER_ROOT_MAP_VERIFIED"
EXPECTED_KIND = "product_chamber_root_map_lattice"
SECTORS = {
    "m_positive": "m>0,n>=0",
    "n_positive_boundary": "m=0,n>0",
    "negative_l_boundary": "m=0,n=0,l<0",
}
REQUIRED_CLOSURE_RULES = {
    ("m_positive", "m_positive"): "m_positive",
    ("m_positive", "n_positive_boundary"): "m_positive",
    ("m_positive", "negative_l_boundary"): "m_positive",
    ("n_positive_boundary", "n_positive_boundary"): "n_positive_boundary",
    ("n_positive_boundary", "negative_l_boundary"): "n_positive_boundary",
    ("negative_l_boundary", "negative_l_boundary"): "negative_l_boundary",
}
REQUIRED_ROOT_ROWS = frozenset(
    {
        "delta1",
        "delta2",
        "delta3",
        "delta1_plus_delta3",
        "delta2_plus_delta3",
        "timelike_first",
        "inactive_negative_delta_coeff",
        "inactive_boundary_zero",
    }
)
REQUIRED_RELATIONS = frozenset(
    {
        "alpha_formula",
        "delta_basis_formula",
        "active_nonnegative_delta3",
        "inactive_zero_exponent",
        "gamma_eff_sector_closure",
    }
)
REQUIRED_DENOMINATOR_CONVENTIONS = frozenset({"z_to_2z"})
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source",
        "pfaffian_orientation",
        "o2_wall_atlas",
        "mirror_discriminant",
        "protected_trace",
    }
)
FORBIDDEN_TOKENS = frozenset(
    {
        "mock",
        "placeholder",
        "todo",
        "unsupplied",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "chamber_sectors.csv",
        (
            "sector_id",
            "n_condition",
            "m_condition",
            "l_condition",
            "included",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "closure_rules.csv",
        (
            "rule_id",
            "left_sector",
            "right_sector",
            "sum_sector",
            "closed",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "root_map_rows.csv",
        (
            "row_id",
            "n",
            "l",
            "m",
            "sector_id",
            "gamma_eff_member",
            "phi_index_n",
            "phi_l",
            "coefficient",
            "active",
            "alpha_f2",
            "alpha_f3",
            "alpha_fm2",
            "delta1_coeff",
            "delta2_coeff",
            "delta3_coeff",
            "delta_coeff_nonnegative",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "root_map_relations.csv",
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
        "denominator_conventions.csv",
        (
            "convention_id",
            "cusp_character",
            "denominator_character",
            "z_scale",
            "computed_scale",
            "expected_scale",
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
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/lattice/product_chamber_root_map"),
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


def coefficient(phi: dict[tuple[int, int], Fraction], n: int, l: int) -> int:
    value = phi.get((n, l), Fraction(0))
    if value.denominator != 1:
        raise ValueError(f"nonintegral phi_01 coefficient f({n},{l})={value}")
    return int(value)


def gamma_eff_sector(n: int, l: int, m: int) -> str | None:
    if m > 0 and n >= 0:
        return "m_positive"
    if m == 0 and n > 0:
        return "n_positive_boundary"
    if n == 0 and m == 0 and l < 0:
        return "negative_l_boundary"
    return None


def alpha(n: int, l: int, m: int) -> tuple[int, int, int]:
    return (2 * n, -l, 2 * m)


def delta_coeffs(n: int, l: int, m: int) -> tuple[int, int, int]:
    return (n, m, n + m - l)


def alpha_from_delta_coeffs(c1: int, c2: int, c3: int) -> tuple[int, int, int]:
    # delta_1=(2,-1,0), delta_2=(0,-1,2), delta_3=(0,1,0).
    return (2 * c1, -c1 - c2 + c3, 2 * c2)


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("chamber_kind"), EXPECTED_KIND, "manifest chamber_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("root_map_certified"), True, "manifest root_map_certified")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("o2_wall_atlas"), False, "manifest o2_wall_atlas")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_chamber_sectors(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "chamber_sectors.csv")
        sector_id = row["sector_id"]
        if sector_id in seen:
            raise ValueError(f"chamber_sectors.csv: duplicate sector_id {sector_id}")
        seen.add(sector_id)
        if sector_id not in SECTORS:
            raise ValueError(f"chamber_sectors.csv: unexpected sector_id {sector_id}")
        require_equal(bool_cell(row, "included"), True, f"{sector_id} included")
    require_equal(seen, set(SECTORS), "sector coverage")


def canonical_pair(left: str, right: str) -> tuple[str, str]:
    order = ("m_positive", "n_positive_boundary", "negative_l_boundary")
    return tuple(sorted((left, right), key=order.index))  # type: ignore[return-value]


def verify_closure_rules(rows: list[dict[str, str]]) -> None:
    seen: set[tuple[str, str]] = set()
    for row in rows:
        check_row(row, "closure_rules.csv")
        left = row["left_sector"]
        right = row["right_sector"]
        if left not in SECTORS or right not in SECTORS:
            raise ValueError(f"closure_rules.csv: unknown sector in row {row}")
        key = canonical_pair(left, right)
        if key in seen:
            raise ValueError(f"closure_rules.csv: duplicate sector pair {key}")
        seen.add(key)
        expected = REQUIRED_CLOSURE_RULES[key]
        require_equal(row["sum_sector"], expected, f"{row['rule_id']} sum_sector")
        require_equal(bool_cell(row, "closed"), True, f"{row['rule_id']} closed")
        require_equal(int_cell(row, "defect_rank"), 0, f"{row['rule_id']} defect_rank")
    require_equal(seen, set(REQUIRED_CLOSURE_RULES), "closure rule coverage")


def verify_root_map_rows(rows: list[dict[str, str]]) -> dict[str, dict[str, int | bool]]:
    phi = phi_01_coefficients()
    seen: set[str] = set()
    row_data: dict[str, dict[str, int | bool]] = {}
    for row in rows:
        check_row(row, "root_map_rows.csv")
        row_id = row["row_id"]
        if row_id in seen:
            raise ValueError(f"root_map_rows.csv: duplicate row_id {row_id}")
        seen.add(row_id)
        if row_id not in REQUIRED_ROOT_ROWS:
            raise ValueError(f"root_map_rows.csv: unexpected row_id {row_id}")
        n = int_cell(row, "n")
        l = int_cell(row, "l")
        m = int_cell(row, "m")
        sector = gamma_eff_sector(n, l, m)
        require_equal(row["sector_id"], sector, f"{row_id} sector_id")
        require_equal(bool_cell(row, "gamma_eff_member"), sector is not None, f"{row_id} gamma_eff_member")
        phi_n = n * m
        coeff = coefficient(phi, phi_n, l)
        require_equal(int_cell(row, "phi_index_n"), phi_n, f"{row_id} phi_index_n")
        require_equal(int_cell(row, "phi_l"), l, f"{row_id} phi_l")
        require_equal(int_cell(row, "coefficient"), coeff, f"{row_id} coefficient")
        active = sector is not None and coeff != 0
        require_equal(bool_cell(row, "active"), active, f"{row_id} active")
        alpha_vector = alpha(n, l, m)
        require_equal((int_cell(row, "alpha_f2"), int_cell(row, "alpha_f3"), int_cell(row, "alpha_fm2")), alpha_vector, f"{row_id} alpha")
        coeff_vector = delta_coeffs(n, l, m)
        require_equal(
            (int_cell(row, "delta1_coeff"), int_cell(row, "delta2_coeff"), int_cell(row, "delta3_coeff")),
            coeff_vector,
            f"{row_id} delta coeffs",
        )
        require_equal(alpha_from_delta_coeffs(*coeff_vector), alpha_vector, f"{row_id} delta formula")
        nonnegative = all(value >= 0 for value in coeff_vector)
        require_equal(bool_cell(row, "delta_coeff_nonnegative"), nonnegative, f"{row_id} delta_coeff_nonnegative")
        if active and not nonnegative:
            raise ValueError(f"{row_id}: active row has negative delta coefficient")
        if not active:
            require_equal(coeff, 0, f"{row_id} inactive coefficient")
        row_data[row_id] = {
            "active": active,
            "coefficient": coeff,
            "delta_nonnegative": nonnegative,
        }
    require_equal(seen, REQUIRED_ROOT_ROWS, "root row coverage")
    return row_data


def verify_root_map_relations(rows: list[dict[str, str]], row_data: dict[str, dict[str, int | bool]]) -> None:
    seen: set[str] = set()
    relation_values = {
        "alpha_formula": 1,
        "delta_basis_formula": 1,
        "active_nonnegative_delta3": 1 if all(bool(data["delta_nonnegative"]) for data in row_data.values() if data["active"]) else 0,
        "inactive_zero_exponent": 1 if all(int(data["coefficient"]) == 0 for data in row_data.values() if not data["active"]) else 0,
        "gamma_eff_sector_closure": 1,
    }
    for row in rows:
        check_row(row, "root_map_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"root_map_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"root_map_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed_value")
        require_equal(int_cell(row, "computed_value"), int_cell(row, "expected_value"), f"{relation_id} expected_value")
        require_equal(int_cell(row, "defect_rank"), 0, f"{relation_id} defect_rank")
    require_equal(seen, REQUIRED_RELATIONS, "root relation coverage")


def verify_denominator_conventions(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "denominator_conventions.csv")
        convention_id = row["convention_id"]
        if convention_id in seen:
            raise ValueError(f"denominator_conventions.csv: duplicate convention_id {convention_id}")
        seen.add(convention_id)
        if convention_id not in REQUIRED_DENOMINATOR_CONVENTIONS:
            raise ValueError(f"denominator_conventions.csv: unexpected convention_id {convention_id}")
        require_equal(row["cusp_character"], "exp_minus_pi_i_alpha_z", f"{convention_id} cusp_character")
        require_equal(row["denominator_character"], "exp_minus_2pi_i_alpha_z", f"{convention_id} denominator_character")
        z_scale = int_cell(row, "z_scale")
        require_equal(z_scale, 2, f"{convention_id} z_scale")
        require_equal(int_cell(row, "computed_scale"), z_scale, f"{convention_id} computed_scale")
        require_equal(int_cell(row, "expected_scale"), 2, f"{convention_id} expected_scale")
        require_equal(int_cell(row, "defect_rank"), 0, f"{convention_id} defect_rank")
    require_equal(seen, REQUIRED_DENOMINATOR_CONVENTIONS, "denominator convention coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"scalar_firewall.csv: duplicate substitute {substitute}")
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
        verify_chamber_sectors(tables["chamber_sectors.csv"])
        verify_closure_rules(tables["closure_rules.csv"])
        row_data = verify_root_map_rows(tables["root_map_rows.csv"])
        verify_root_map_relations(tables["root_map_relations.csv"], row_data)
        verify_denominator_conventions(tables["denominator_conventions.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"PRODUCT_CHAMBER_ROOT_MAP_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
