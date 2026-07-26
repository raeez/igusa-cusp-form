#!/usr/bin/env python3
"""Verify the target-side images of the three simple type-II walls."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "TYPE_II_WALL_IMAGES_VERIFIED"
EXPECTED_SCHEMA = "type_ii_wall_images.v1"
EXPECTED_KIND = "type_ii_target_lattice_images"
MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
PROOF_LABEL = "prop:type-ii-wall-images"
EXPECTED_WALLS = {
    "delta1_image": {
        "delta_id": "delta_1",
        "triple": (1, 1, 0),
        "sector_id": "n_positive_boundary",
        "alpha": (2, -1, 0),
        "delta_coeffs": (1, 0, 0),
        "product_chamber_row_id": "delta1",
    },
    "delta2_image": {
        "delta_id": "delta_2",
        "triple": (0, 1, 1),
        "sector_id": "m_positive",
        "alpha": (0, -1, 2),
        "delta_coeffs": (0, 1, 0),
        "product_chamber_row_id": "delta2",
    },
    "delta3_image": {
        "delta_id": "delta_3",
        "triple": (0, -1, 0),
        "sector_id": "negative_l_boundary",
        "alpha": (0, 1, 0),
        "delta_coeffs": (0, 0, 1),
        "product_chamber_row_id": "delta3",
    },
}
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source",
        "o2_wall_atlas",
        "pfaffian_orientation",
        "protected_trace",
        "hall_carrier",
    }
)

WALL_COLUMNS = (
    "wall_id",
    "delta_id",
    "n",
    "l",
    "m",
    "sector_id",
    "alpha_f2",
    "alpha_f3",
    "alpha_fm2",
    "delta1_coeff",
    "delta2_coeff",
    "delta3_coeff",
    "root_map_defect_rank",
    "product_chamber_row_id",
    "proof_reference",
    "check_status",
    "notes",
)
FORMULA_COLUMNS = (
    "formula_id",
    "root_map_formula",
    "inverse_condition",
    "delta1_image",
    "delta2_image",
    "delta3_image",
    "defect_rank",
    "proof_reference",
    "check_status",
    "notes",
)
FIREWALL_COLUMNS = (
    "firewall_id",
    "forbidden_substitute",
    "excluded",
    "defect_rank",
    "source_reference",
    "check_status",
    "notes",
)


@dataclass(frozen=True)
class CsvTable:
    path: Path
    rows: list[dict[str, str]]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/lattice/type_ii_wall_images"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def load_json(path: Path, issues: list[str]) -> dict[str, object]:
    if not path.is_file():
        issues.append(f"missing JSON file: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        issues.append(f"invalid JSON {path}: {exc}")
        return {}
    if not isinstance(value, dict):
        issues.append(f"JSON root is not an object: {path}")
        return {}
    return value


def load_csv(path: Path, columns: tuple[str, ...], issues: list[str]) -> CsvTable:
    if not path.is_file():
        issues.append(f"missing table: {path}")
        return CsvTable(path, [])
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != columns:
            issues.append(f"header mismatch in {path}; expected {','.join(columns)}")
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    return CsvTable(path, [row for row in rows if any(row.values())])


def int_cell(row: dict[str, str], key: str, issues: list[str]) -> int:
    try:
        return int(row.get(key, ""))
    except ValueError:
        issues.append(f"{key} is not an integer in row {row}")
        return 0


def check_manifest(fixture: Path, issues: list[str]) -> None:
    manifest = load_json(fixture / MANIFEST_NAME, issues)
    if not manifest:
        return
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "type_ii_wall_images",
        "wall_image_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "coefficient_ring": "ZZ",
        "wall_images_certified": True,
        "delta1_image_certified": True,
        "delta2_image_certified": True,
        "delta3_image_certified": True,
        "product_chamber_root_map_imported": True,
        "compact_source": False,
        "o2_wall_atlas": False,
        "pfaffian_orientation": False,
        "protected_trace": False,
        "hall_carrier": False,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            issues.append(f"manifest {key}: expected {value!r}, got {manifest.get(key)!r}")
    if set(manifest.get("tables", [])) != {
        "wall_image_rows.csv",
        "inverse_formula_rows.csv",
        "scalar_firewall.csv",
    }:
        issues.append("manifest tables do not match expected type-II wall image tables")
    if set(manifest.get("imports", [])) != {
        "certificates/lattice/product_chamber_root_map"
    }:
        issues.append("manifest imports do not match expected product-chamber import")


def check_product_import(fixture: Path, issues: list[str]) -> None:
    imported = (fixture / "../product_chamber_root_map/manifest.json").resolve()
    if not imported.is_file():
        issues.append("missing imported product_chamber_root_map manifest")
        return
    manifest = load_json(imported, issues)
    if manifest.get("certified") is not True:
        issues.append("imported product_chamber_root_map is not certified")


def check_wall_rows(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "wall_image_rows.csv", WALL_COLUMNS, issues)
    rows_by_id = {row.get("wall_id", ""): row for row in table.rows}
    missing = sorted(set(EXPECTED_WALLS) - set(rows_by_id))
    extra = sorted(set(rows_by_id) - set(EXPECTED_WALLS))
    if missing:
        issues.append("missing wall image rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected wall image rows: " + ", ".join(extra))
    for wall_id, expected in EXPECTED_WALLS.items():
        row = rows_by_id.get(wall_id)
        if not row:
            continue
        n = int_cell(row, "n", issues)
        l = int_cell(row, "l", issues)
        m = int_cell(row, "m", issues)
        if (n, l, m) != expected["triple"]:
            issues.append(f"{wall_id} triple mismatch")
        alpha = (2 * n, -l, 2 * m)
        delta_coeffs = (n, m, n + m - l)
        if alpha != expected["alpha"]:
            issues.append(f"{wall_id} computed alpha mismatch: {alpha}")
        if delta_coeffs != expected["delta_coeffs"]:
            issues.append(f"{wall_id} computed delta coefficients mismatch: {delta_coeffs}")
        csv_alpha = tuple(int_cell(row, key, issues) for key in ("alpha_f2", "alpha_f3", "alpha_fm2"))
        csv_delta = tuple(
            int_cell(row, key, issues)
            for key in ("delta1_coeff", "delta2_coeff", "delta3_coeff")
        )
        if csv_alpha != alpha:
            issues.append(f"{wall_id} alpha CSV mismatch")
        if csv_delta != delta_coeffs:
            issues.append(f"{wall_id} delta coefficient CSV mismatch")
        if row.get("delta_id") != expected["delta_id"]:
            issues.append(f"{wall_id} delta_id mismatch")
        if row.get("sector_id") != expected["sector_id"]:
            issues.append(f"{wall_id} sector_id mismatch")
        if row.get("product_chamber_row_id") != expected["product_chamber_row_id"]:
            issues.append(f"{wall_id} product chamber row mismatch")
        if row.get("root_map_defect_rank") != "0":
            issues.append(f"{wall_id} root_map_defect_rank must be zero")
        if PROOF_LABEL not in row.get("proof_reference", ""):
            issues.append(f"{wall_id} missing proof label")
        if row.get("check_status") != "verified":
            issues.append(f"{wall_id} not verified")


def check_formula_row(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "inverse_formula_rows.csv", FORMULA_COLUMNS, issues)
    if len(table.rows) != 1:
        issues.append("inverse_formula_rows.csv must contain exactly one row")
        return
    row = table.rows[0]
    expected = {
        "formula_id": "type_ii_inverse_images",
        "root_map_formula": "alpha_equals_n_delta1_plus_m_delta2_plus_n_plus_m_minus_l_delta3",
        "inverse_condition": "solve_standard_basis_coefficients",
        "delta1_image": "(1,1,0)",
        "delta2_image": "(0,1,1)",
        "delta3_image": "(0,-1,0)",
        "defect_rank": "0",
        "check_status": "verified",
    }
    for key, value in expected.items():
        if row.get(key) != value:
            issues.append(f"inverse formula {key}: expected {value!r}, got {row.get(key)!r}")
    if PROOF_LABEL not in row.get("proof_reference", ""):
        issues.append("inverse formula row missing proof label")


def check_firewall(fixture: Path, issues: list[str]) -> None:
    table = load_csv(fixture / "scalar_firewall.csv", FIREWALL_COLUMNS, issues)
    substitutes = {row.get("forbidden_substitute", "") for row in table.rows}
    missing = sorted(REQUIRED_FIREWALL_ROWS - substitutes)
    extra = sorted(substitutes - REQUIRED_FIREWALL_ROWS)
    if missing:
        issues.append("missing firewall rows: " + ", ".join(missing))
    if extra:
        issues.append("unexpected firewall rows: " + ", ".join(extra))
    for index, row in enumerate(table.rows, start=2):
        if row.get("excluded") != "true":
            issues.append(f"scalar_firewall.csv:{index} excluded must be true")
        if row.get("defect_rank") != "0":
            issues.append(f"scalar_firewall.csv:{index} defect_rank must be zero")
        if row.get("check_status") != "verified":
            issues.append(f"scalar_firewall.csv:{index} not verified")


def run(fixture: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []
    check_manifest(fixture, issues)
    if not (fixture / README_NAME).is_file():
        issues.append(f"missing README: {fixture / README_NAME}")
    check_product_import(fixture, issues)
    check_wall_rows(fixture, issues)
    check_formula_row(fixture, issues)
    check_firewall(fixture, issues)
    return not issues, issues


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    ok, issues = run(args.fixture)
    if ok:
        print(SUCCESS_STATUS)
        return 0
    print("TYPE_II_WALL_IMAGES_BLOCKED")
    for issue in issues:
        print(f"- {issue}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
