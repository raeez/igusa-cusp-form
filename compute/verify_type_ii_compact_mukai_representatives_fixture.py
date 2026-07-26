#!/usr/bin/env python3
"""Verify compact Mukai representatives for the three type-II wall charges."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


SUCCESS_STATUS = "TYPE_II_COMPACT_MUKAI_REPRESENTATIVES_VERIFIED"
EXPECTED_SCHEMA = "type_ii_compact_mukai_representatives.v1"
EXPECTED_KIND = "type_ii_compact_mukai_representatives"
DEFAULT_FIXTURE = Path("certificates/charge/type_ii_compact_mukai_representatives")
PROOF_LABEL = "prop:type-ii-compact-mukai-representatives"
IMPORTS = {
    "certificates/charge/mukai_gram_cocycle",
    "certificates/lattice/type_ii_wall_images",
}
EXPECTED_OBJECTS = {
    "I_Z2": ("ideal_sheaf_length_2", 2, (1, 0, -1)),
    "I_p": ("ideal_sheaf_point", 1, (1, 0, 0)),
    "O_p": ("skyscraper_point", 1, (0, 0, 1)),
}
EXPECTED_REPRESENTATIVES = {
    "x_delta1": ("delta_1", "I_Z2", "I_p", (1, 1, 0), "delta1_image"),
    "x_delta2": ("delta_2", "I_p", "I_Z2", (0, 1, 1), "delta2_image"),
    "x_delta3": ("delta_3", "I_p", "O_p", (0, -1, 0), "delta3_image"),
}
REQUIRED_FIREWALL_ROWS = {
    "compact_hall_source_basis",
    "o2_wall_object",
    "hn_semistability",
    "orientation_data",
    "vanishing_cycle_summand",
    "e_quotient",
    "wall_chart",
    "pfaffian_sign",
    "protected_integration",
    "target_label_only",
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS = (
    TableSpec(
        "mukai_object_rows.csv",
        (
            "object_id",
            "object_model",
            "length",
            "r",
            "d",
            "s",
            "mukai_vector_defect_rank",
            "compact_support",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "representative_rows.csv",
        (
            "representative_id",
            "delta_id",
            "Q_object_id",
            "P_object_id",
            "Q_vector",
            "P_vector",
            "compact_mukai_pair",
            "compact_pair_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "gram_image_rows.csv",
        (
            "image_id",
            "representative_id",
            "delta_id",
            "pi_n",
            "pi_l",
            "pi_m",
            "expected_n",
            "expected_l",
            "expected_m",
            "gram_defect_rank",
            "type_ii_wall_image_row_id",
            "proof_reference",
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


Vector = tuple[int, int, int]
Triple = tuple[int, int, int]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def read_json(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"missing JSON file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root is not an object: {path}")
    return value


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    path = fixture / spec.path
    if not path.is_file():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        actual = tuple(reader.fieldnames or ())
        if actual != spec.columns:
            raise ValueError(f"{spec.path}: expected columns {spec.columns}, got {actual}")
        rows = [
            {key: (value or "").strip() for key, value in row.items() if key is not None}
            for row in reader
        ]
    rows = [row for row in rows if any(row.values())]
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one data row")
    return rows


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key} is not an integer in row {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key} is not a boolean in row {row}")


def vector_from_row(row: dict[str, str]) -> Vector:
    return (int_cell(row, "r"), int_cell(row, "d"), int_cell(row, "s"))


def vector_from_literal(value: str) -> Vector:
    stripped = value.strip()
    if not stripped.startswith("(") or not stripped.endswith(")"):
        raise ValueError(f"vector literal must be parenthesized: {value}")
    parts = [part.strip() for part in stripped[1:-1].split(",")]
    if len(parts) != 3:
        raise ValueError(f"vector literal must have three components: {value}")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def triple_from_columns(row: dict[str, str], prefix: str) -> Triple:
    return (int_cell(row, f"{prefix}_n"), int_cell(row, f"{prefix}_l"), int_cell(row, f"{prefix}_m"))


def pair(left: Vector, right: Vector) -> int:
    r, d, s = left
    rp, dp, sp = right
    return 2 * d * dp - r * sp - rp * s


def pi(q: Vector, p: Vector) -> Triple:
    q_square = pair(q, q)
    p_square = pair(p, p)
    if q_square % 2 != 0 or p_square % 2 != 0:
        raise ValueError(f"non-even Mukai square for pair {q}, {p}")
    return (q_square // 2, pair(q, p), p_square // 2)


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def check_verified(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")
    reference = row.get("proof_reference") or row.get("source_reference") or ""
    if PROOF_LABEL not in reference:
        raise ValueError(f"{table_name}: missing proof label in row {row}")


def verify_manifest(fixture: Path) -> None:
    manifest = read_json(fixture / "manifest.json")
    expected = {
        "schema_version": EXPECTED_SCHEMA,
        "fixture_name": "type_ii_compact_mukai_representatives",
        "charge_kind": EXPECTED_KIND,
        "status": SUCCESS_STATUS,
        "coefficient_ring": "ZZ",
        "certified": True,
        "compact_mukai_representatives_certified": True,
        "delta1_representative_certified": True,
        "delta2_representative_certified": True,
        "delta3_representative_certified": True,
        "mukai_gram_cocycle_imported": True,
        "type_ii_wall_images_imported": True,
        "compact_hall_source_basis": False,
        "o2_wall_atlas": False,
        "hn_semistability": False,
        "orientation_data": False,
        "vanishing_cycles": False,
        "protected_integration": False,
        "e_quotient": False,
    }
    for key, value in expected.items():
        require_equal(manifest.get(key), value, f"manifest {key}")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")
    require_equal(set(manifest.get("imports", [])), IMPORTS, "manifest imports")
    if not isinstance(manifest.get("limitations"), list) or not manifest["limitations"]:
        raise ValueError("manifest limitations must be a nonempty list")


def verify_readme(fixture: Path) -> None:
    readme = fixture / "README.md"
    if not readme.is_file() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme}")


def verify_imports() -> None:
    mukai_manifest = read_json(Path("certificates/charge/mukai_gram_cocycle/manifest.json"))
    wall_manifest = read_json(Path("certificates/lattice/type_ii_wall_images/manifest.json"))
    require_equal(mukai_manifest.get("formal_cocycle_certified"), True, "mukai_gram_cocycle import")
    require_equal(wall_manifest.get("status"), "TYPE_II_WALL_IMAGES_VERIFIED", "type_ii_wall_images import")


def verify_objects(rows: list[dict[str, str]]) -> dict[str, Vector]:
    objects: dict[str, Vector] = {}
    for row in rows:
        check_verified(row, "mukai_object_rows.csv")
        object_id = row["object_id"]
        if object_id in objects:
            raise ValueError(f"mukai_object_rows.csv: duplicate object_id {object_id}")
        if object_id not in EXPECTED_OBJECTS:
            raise ValueError(f"mukai_object_rows.csv: unexpected object_id {object_id}")
        model, length, expected_vector = EXPECTED_OBJECTS[object_id]
        require_equal(row["object_model"], model, f"{object_id} object_model")
        require_equal(int_cell(row, "length"), length, f"{object_id} length")
        vector = vector_from_row(row)
        require_equal(vector, expected_vector, f"{object_id} Mukai vector")
        require_equal(int_cell(row, "mukai_vector_defect_rank"), 0, f"{object_id} defect")
        require_equal(bool_cell(row, "compact_support"), True, f"{object_id} compact_support")
        objects[object_id] = vector
    require_equal(set(objects), set(EXPECTED_OBJECTS), "Mukai object coverage")
    return objects


def verify_representatives(rows: list[dict[str, str]], objects: dict[str, Vector]) -> dict[str, tuple[str, Vector, Vector]]:
    representatives: dict[str, tuple[str, Vector, Vector]] = {}
    for row in rows:
        check_verified(row, "representative_rows.csv")
        representative_id = row["representative_id"]
        if representative_id in representatives:
            raise ValueError(f"representative_rows.csv: duplicate representative_id {representative_id}")
        if representative_id not in EXPECTED_REPRESENTATIVES:
            raise ValueError(f"representative_rows.csv: unexpected representative_id {representative_id}")
        expected_delta, expected_q_id, expected_p_id, _, _ = EXPECTED_REPRESENTATIVES[representative_id]
        require_equal(row["delta_id"], expected_delta, f"{representative_id} delta_id")
        require_equal(row["Q_object_id"], expected_q_id, f"{representative_id} Q_object_id")
        require_equal(row["P_object_id"], expected_p_id, f"{representative_id} P_object_id")
        q = objects[row["Q_object_id"]]
        p = objects[row["P_object_id"]]
        require_equal(vector_from_literal(row["Q_vector"]), q, f"{representative_id} Q_vector")
        require_equal(vector_from_literal(row["P_vector"]), p, f"{representative_id} P_vector")
        require_equal(bool_cell(row, "compact_mukai_pair"), True, f"{representative_id} compact_mukai_pair")
        require_equal(int_cell(row, "compact_pair_defect_rank"), 0, f"{representative_id} compact_pair_defect")
        representatives[representative_id] = (row["delta_id"], q, p)
    require_equal(set(representatives), set(EXPECTED_REPRESENTATIVES), "representative coverage")
    return representatives


def verify_wall_image_imports() -> dict[str, Triple]:
    path = Path("certificates/lattice/type_ii_wall_images/wall_image_rows.csv")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    wall_images: dict[str, Triple] = {}
    for row in rows:
        wall_images[row["wall_id"]] = (int(row["n"]), int(row["l"]), int(row["m"]))
    return wall_images


def verify_gram_images(rows: list[dict[str, str]], representatives: dict[str, tuple[str, Vector, Vector]]) -> None:
    wall_images = verify_wall_image_imports()
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "gram_image_rows.csv")
        image_id = row["image_id"]
        if image_id in seen:
            raise ValueError(f"gram_image_rows.csv: duplicate image_id {image_id}")
        seen.add(image_id)
        representative_id = row["representative_id"]
        if representative_id not in EXPECTED_REPRESENTATIVES:
            raise ValueError(f"gram_image_rows.csv: unexpected representative_id {representative_id}")
        expected_delta, _, _, expected_pi, expected_wall_row = EXPECTED_REPRESENTATIVES[representative_id]
        delta_id, q, p = representatives[representative_id]
        computed_pi = pi(q, p)
        require_equal(delta_id, expected_delta, f"{image_id} representative delta")
        require_equal(row["delta_id"], expected_delta, f"{image_id} delta_id")
        require_equal(triple_from_columns(row, "pi"), computed_pi, f"{image_id} computed Pi")
        require_equal(triple_from_columns(row, "expected"), expected_pi, f"{image_id} expected Pi")
        require_equal(computed_pi, expected_pi, f"{image_id} Pi target")
        require_equal(int_cell(row, "gram_defect_rank"), 0, f"{image_id} gram_defect")
        require_equal(row["type_ii_wall_image_row_id"], expected_wall_row, f"{image_id} wall row")
        require_equal(wall_images.get(expected_wall_row), expected_pi, f"{image_id} imported wall image")
    require_equal(seen, {"image_delta1", "image_delta2", "image_delta3"}, "gram image coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"scalar_firewall.csv: duplicate substitute {substitute}")
        if substitute not in REQUIRED_FIREWALL_ROWS:
            raise ValueError(f"scalar_firewall.csv: unexpected substitute {substitute}")
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect_rank")
        seen.add(substitute)
    require_equal(seen, REQUIRED_FIREWALL_ROWS, "firewall coverage")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        verify_manifest(args.fixture)
        verify_readme(args.fixture)
        verify_imports()
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        objects = verify_objects(tables["mukai_object_rows.csv"])
        representatives = verify_representatives(tables["representative_rows.csv"], objects)
        verify_gram_images(tables["gram_image_rows.csv"], representatives)
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TYPE_II_COMPACT_MUKAI_REPRESENTATIVES_BLOCKED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
