#!/usr/bin/env python3
"""Verify active target root-window exhaustion.

This verifier checks Optimization row 183 at the target-window level:
the active height windows exhaust the positive root set.  It imports the
downward root-window packet and verifies the formal witness

    beta in R_+  ->  beta in W_{ht(beta)}.

It does not construct compact source support, moduli transitions,
orientations, vanishing cycles, Hall operations, radicals, PBW
filtrations, or protected traces.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "ACTIVE_ROOT_WINDOW_EXHAUSTION_VERIFIED"
DOWNWARD_STATUS = "DOWNWARD_ROOT_WINDOWS_VERIFIED"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
EXPECTED_SCHEMA = "active_root_window_exhaustion.v1"
EXPECTED_KIND = "active_root_window_exhaustion"
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_support",
        "moduli_transitions",
        "orientation_transport",
        "vanishing_cycles",
        "hall_operations",
        "radicals_pbw",
    }
)
EXPECTED_SAMPLE_BETAS = {
    "delta_1": (1, 0, 0),
    "delta_2": (0, 1, 0),
    "delta_3": (0, 0, 1),
    "a_12": (1, 1, 0),
    "a_13": (1, 0, 1),
    "a_23": (0, 1, 1),
    "delta123": (1, 1, 1),
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "active_exhaustion.csv",
        (
            "exhaustion_id",
            "target_root_set",
            "active_window_system",
            "union_formula",
            "height_witness_formula",
            "exhaustive",
            "defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "sample_membership.csv",
        (
            "sample_id",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "height",
            "minimal_window",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "sector_id",
            "alpha_inverse_defect_rank",
            "window_membership_defect_rank",
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
        default=Path("certificates/lattice/active_root_window_exhaustion"),
    )
    parser.add_argument(
        "--downward-fixture",
        type=Path,
        default=Path("certificates/lattice/downward_root_windows"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def read_json(path: Path) -> dict:
    if not path.exists():
        raise ValueError(f"missing JSON file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_manifest(fixture: Path) -> dict:
    manifest_path = fixture / MANIFEST_NAME
    readme_path = fixture / README_NAME
    if not readme_path.exists() or not readme_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme_path}")
    return read_json(manifest_path)


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
    if not row.get("source_reference"):
        raise ValueError(f"{table}: row has empty source_reference: {row}")


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
    raise ValueError(f"gamma is outside the type-II product chamber: {gamma}")


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("schema_version"), EXPECTED_SCHEMA, "schema_version")
    require_equal(manifest.get("fixture_name"), "active_root_window_exhaustion", "fixture_name")
    require_equal(manifest.get("window_kind"), EXPECTED_KIND, "window_kind")
    require_equal(manifest.get("status"), SUCCESS_STATUS, "status")
    require_equal(manifest.get("active_exhaustion"), True, "active_exhaustion")
    require_equal(manifest.get("target_side"), True, "target_side")
    require_equal(manifest.get("compact_support"), False, "compact_support")
    require_equal(manifest.get("moduli_transitions"), False, "moduli_transitions")
    require_equal(manifest.get("orientation_transport"), False, "orientation_transport")
    require_equal(manifest.get("vanishing_cycles"), False, "vanishing_cycles")
    require_equal(set(manifest.get("tables", [])), {spec.path for spec in TABLE_SPECS}, "manifest tables")


def verify_downward_fixture(downward_fixture: Path) -> None:
    manifest = read_json(downward_fixture / MANIFEST_NAME)
    require_equal(manifest.get("status"), DOWNWARD_STATUS, "downward fixture status")
    require_equal(manifest.get("certified"), True, "downward fixture certified")
    require_equal(manifest.get("target_side"), True, "downward fixture target_side")


def verify_exhaustion(rows: list[dict[str, str]]) -> None:
    require_equal(len(rows), 1, "active_exhaustion row count")
    row = rows[0]
    check_verified(row, "active_exhaustion.csv")
    require_equal(row["exhaustion_id"], "active_height_windows_exhaust_R_plus", "exhaustion_id")
    require_equal(row["target_root_set"], "R_plus", "target_root_set")
    require_equal(row["active_window_system"], "W_nu_active=W_nu", "active_window_system")
    require_equal(row["union_formula"], "union_nu W_nu_active=R_plus", "union_formula")
    require_equal(row["height_witness_formula"], "beta in R_plus -> beta in W_ht(beta)", "height_witness_formula")
    require_equal(bool_cell(row, "exhaustive"), True, "exhaustive")
    require_zero(int_cell(row, "defect_rank"), "exhaustion defect")


def verify_sample_membership(rows: list[dict[str, str]]) -> None:
    require_equal({row["sample_id"] for row in rows}, set(EXPECTED_SAMPLE_BETAS), "sample coverage")
    for row in rows:
        check_verified(row, "sample_membership.csv")
        sample_id = row["sample_id"]
        beta = (
            int_cell(row, "beta_c1"),
            int_cell(row, "beta_c2"),
            int_cell(row, "beta_c3"),
        )
        require_equal(beta, EXPECTED_SAMPLE_BETAS[sample_id], f"{sample_id} beta")
        height = sum(beta)
        require_equal(int_cell(row, "height"), height, f"{sample_id} height")
        require_equal(int_cell(row, "minimal_window"), height, f"{sample_id} minimal window")
        gamma = gamma_from_beta(beta)
        require_equal(
            (int_cell(row, "gamma_n"), int_cell(row, "gamma_l"), int_cell(row, "gamma_m")),
            gamma,
            f"{sample_id} gamma",
        )
        require_equal(alpha(gamma), beta, f"{sample_id} alpha inverse")
        require_equal(row["sector_id"], sector(gamma), f"{sample_id} sector")
        require_zero(int_cell(row, "alpha_inverse_defect_rank"), f"{sample_id} alpha defect")
        require_zero(int_cell(row, "window_membership_defect_rank"), f"{sample_id} window defect")


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
        verify_downward_fixture(args.downward_fixture)
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        verify_exhaustion(tables["active_exhaustion.csv"])
        verify_sample_membership(tables["sample_membership.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001
        print(f"ACTIVE_ROOT_WINDOW_EXHAUSTION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
