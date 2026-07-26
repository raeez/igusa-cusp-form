#!/usr/bin/env python3
"""Verify the downward root-window and Gamma(W_nu) fixture.

This verifier checks the target-side convention used by the finite
primitive-recognition clauses:

* W_nu = { beta in R_+ : ht(beta) <= nu };
* beta = b1 delta_1 + b2 delta_2 + b3 delta_3 has
  gamma_beta = (b1, b1 + b2 - b3, b2);
* alpha(gamma_beta) = beta for
  alpha(n,l,m) = n delta_1 + m delta_2 + (n + m - l) delta_3;
* the preimage gamma_beta lies in the product chamber sectors.

The packet is target-side.  It does not construct compact source
representatives, relation matrices, Hall pairings, PBW data, Pfaffian
orientations, or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from math import comb
from pathlib import Path


SUCCESS_STATUS = "DOWNWARD_ROOT_WINDOWS_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_KIND = "downward_root_windows"
EXPECTED_SCHEMA = "downward_root_windows.v1"
MAX_AUDIT_NU = 7
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source",
        "finite_source_tables",
        "pfaffian_orientation",
        "primitive_recognition",
        "protected_trace",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "root_window_definitions.csv",
        (
            "window_system_id",
            "target_root_set",
            "height_function",
            "window_formula",
            "finite",
            "downward_saturated",
            "cofinal",
            "saturation_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "gamma_window_formula.csv",
        (
            "formula_id",
            "alpha_formula",
            "beta_coordinates",
            "gamma_inverse_formula",
            "inverse_defect_rank",
            "sector_rule",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "finite_height_audit.csv",
        (
            "nu",
            "ambient_positive_degree_count",
            "gamma_preimage_count",
            "m_positive_count",
            "n_positive_boundary_count",
            "negative_l_boundary_count",
            "max_abs_l",
            "downward_saturation_defect_rank",
            "alpha_inverse_defect_rank",
            "sector_defect_rank",
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
        default=Path("certificates/lattice/downward_root_windows"),
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
    raise ValueError(f"{key} is not boolean in row {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def require_zero(value: int, label: str) -> None:
    require_equal(value, 0, label)


def check_verified(row: dict[str, str], table: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table}: row is not verified: {row}")
    if not row.get("source_reference", "source"):
        raise ValueError(f"{table}: row has empty source_reference: {row}")


def beta_triples(nu: int) -> list[tuple[int, int, int]]:
    triples: list[tuple[int, int, int]] = []
    for b1 in range(nu + 1):
        for b2 in range(nu + 1 - b1):
            for b3 in range(nu + 1 - b1 - b2):
                beta = (b1, b2, b3)
                if beta != (0, 0, 0):
                    triples.append(beta)
    return triples


def gamma_from_beta(beta: tuple[int, int, int]) -> tuple[int, int, int]:
    b1, b2, b3 = beta
    return (b1, b1 + b2 - b3, b2)


def alpha(gamma: tuple[int, int, int]) -> tuple[int, int, int]:
    n, ell, m = gamma
    return (n, m, n + m - ell)


def sector(gamma: tuple[int, int, int]) -> str:
    n, ell, m = gamma
    if m > 0 and n >= 0:
        return "m_positive"
    if m == 0 and n > 0:
        return "n_positive_boundary"
    if m == 0 and n == 0 and ell < 0:
        return "negative_l_boundary"
    raise ValueError(f"gamma is outside the product chamber: {gamma}")


def subdegrees(beta: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    b1, b2, b3 = beta
    rows: list[tuple[int, int, int]] = []
    for c1 in range(b1 + 1):
        for c2 in range(b2 + 1):
            for c3 in range(b3 + 1):
                subdegree = (c1, c2, c3)
                if subdegree == (0, 0, 0) or subdegree == beta:
                    continue
                rows.append(subdegree)
    return rows


def expected_counts(nu: int) -> dict[str, int]:
    triples = beta_triples(nu)
    sectors = {"m_positive": 0, "n_positive_boundary": 0, "negative_l_boundary": 0}
    inverse_defect = 0
    saturation_defect = 0
    max_abs_l = 0
    triple_set = set(triples)
    for beta in triples:
        gamma = gamma_from_beta(beta)
        if alpha(gamma) != beta:
            inverse_defect += 1
        sectors[sector(gamma)] += 1
        max_abs_l = max(max_abs_l, abs(gamma[1]))
        for subdegree in subdegrees(beta):
            if subdegree not in triple_set:
                saturation_defect += 1
    return {
        "ambient_positive_degree_count": comb(nu + 3, 3) - 1,
        "gamma_preimage_count": len({gamma_from_beta(beta) for beta in triples}),
        "m_positive_count": sectors["m_positive"],
        "n_positive_boundary_count": sectors["n_positive_boundary"],
        "negative_l_boundary_count": sectors["negative_l_boundary"],
        "max_abs_l": max_abs_l,
        "downward_saturation_defect_rank": saturation_defect,
        "alpha_inverse_defect_rank": inverse_defect,
        "sector_defect_rank": 0,
    }


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), "downward_root_windows", "fixture_name")
    require_equal(manifest.get("window_kind"), EXPECTED_KIND, "window_kind")
    require_equal(manifest.get("certified"), True, "certified")
    require_equal(manifest.get("target_side"), True, "target_side")
    require_equal(manifest.get("compact_source"), False, "compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "primitive_recognition")
    require_equal(manifest.get("pfaffian_orientation"), False, "pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "protected_trace")
    require_equal(manifest.get("max_audit_nu"), MAX_AUDIT_NU, "max_audit_nu")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")


def verify_window_definition(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "root_window_definitions row count")
    row = rows[0]
    check_verified(row, "root_window_definitions.csv")
    require_equal(row["window_system_id"], "height_root_windows", "window_system_id")
    require_equal(row["target_root_set"], "R_plus", "target_root_set")
    require_equal(row["height_function"], "ht(b1,b2,b3)=b1+b2+b3", "height_function")
    require_equal(row["window_formula"], "W_nu={beta in R_plus: ht(beta)<=nu}", "window_formula")
    require_equal(bool_cell(row, "finite"), True, "finite")
    require_equal(bool_cell(row, "downward_saturated"), True, "downward_saturated")
    require_equal(bool_cell(row, "cofinal"), True, "cofinal")
    require_zero(int_cell(row, "saturation_defect_rank"), "saturation_defect_rank")


def verify_gamma_formula(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "gamma_window_formula row count")
    row = rows[0]
    check_verified(row, "gamma_window_formula.csv")
    require_equal(row["formula_id"], "gamma_preimage_of_height_window", "formula_id")
    require_equal(
        row["alpha_formula"],
        "alpha(n,l,m)=n*delta1+m*delta2+(n+m-l)*delta3",
        "alpha_formula",
    )
    require_equal(row["beta_coordinates"], "beta=b1*delta1+b2*delta2+b3*delta3", "beta_coordinates")
    require_equal(row["gamma_inverse_formula"], "gamma_beta=(b1,b1+b2-b3,b2)", "gamma_inverse_formula")
    require_zero(int_cell(row, "inverse_defect_rank"), "inverse_defect_rank")
    require_equal(
        row["sector_rule"],
        "b2>0:m_positive; b2=0,b1>0:n_positive_boundary; b1=b2=0:b3>0:negative_l_boundary",
        "sector_rule",
    )


def verify_height_audit(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), MAX_AUDIT_NU, "finite_height_audit row count")
    seen: set[int] = set()
    for row in rows:
        if row.get("check_status") != "verified":
            raise ValueError(f"finite_height_audit.csv: row is not verified: {row}")
        nu = int_cell(row, "nu")
        seen.add(nu)
        if not (1 <= nu <= MAX_AUDIT_NU):
            raise ValueError(f"finite_height_audit.csv: nu outside audit range: {nu}")
        expected = expected_counts(nu)
        for key, value in expected.items():
            require_equal(int_cell(row, key), value, f"nu={nu} {key}")
    require_equal(seen, set(range(1, MAX_AUDIT_NU + 1)), "audit nu coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_zero(int_cell(row, "defect_rank"), f"{substitute} defect")
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "firewall coverage")


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        verify_window_definition(tables["root_window_definitions.csv"])
        verify_gamma_formula(tables["gamma_window_formula.csv"])
        verify_height_audit(tables["finite_height_audit.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001
        print(f"DOWNWARD_ROOT_WINDOWS_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
