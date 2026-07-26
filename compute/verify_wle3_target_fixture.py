#!/usr/bin/env python3
"""Exact target-parity gate for the first arithmetic window W<=3.

This verifier checks only the imported GN/Kac target table in the first
arithmetic window:

* delta_i: 1|0;
* a_ij: 10|0;
* 2 delta_i + delta_j: 1|0;
* delta_123: 29|93.

It recomputes the signed Jacobi coefficients and the first timelike
presentation split from ``verify_square_root.py``.  It does not
construct compact source representatives, Hall brackets, pairing
kernels, PBW data, or primitive recognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from pathlib import Path


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from verify_square_root import (
    delta_basis_to_gamma,
    delta_pair,
    first_timelike_presentation_split,
    free_lie_multidegree_dimension,
    monic_delta_qrs_coefficient,
    phi_01_coefficients,
    real_string_exponent,
    signed_root_supermultiplicity,
)


SUCCESS_STATUS = "WLE3_TARGET_PARITY_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/targets/delta5_gn_kac/wle3_target_parity")
EXPECTED_KIND = "wle3_target_parity_candidate"
REAL_SIMPLE = frozenset({"delta_1", "delta_2", "delta_3"})
ISOTROPIC = frozenset({"a_12", "a_13", "a_23"})
REAL_STRING = frozenset(
    {"2delta_1_delta_2", "2delta_1_delta_3", "2delta_2_delta_1",
     "2delta_2_delta_3", "2delta_3_delta_1", "2delta_3_delta_2"}
)
TIMELIKE = frozenset({"delta123"})
EXPECTED_DEGREES = REAL_SIMPLE | ISOTROPIC | REAL_STRING | TIMELIKE
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source_representatives",
        "source_parity",
        "hall_bracket",
        "pairing_radical",
        "pbw_comparison",
        "primitive_recognition",
    }
)


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "target_degrees.csv",
        (
            "degree_id",
            "tex_label",
            "family",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "full_even",
            "full_odd",
            "parity_status",
            "parity_source",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "decomposition.csv",
        (
            "degree_id",
            "real_simple_even",
            "real_bracket_even",
            "isotropic_simple_even",
            "real_string_even",
            "real_real_real_even",
            "mixed_real_isotropic_even",
            "odd_imaginary_simple",
            "total_even",
            "total_odd",
            "decomposition_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "coefficient_comparison.csv",
        (
            "degree_id",
            "phi_n",
            "phi_l",
            "computed_coefficient",
            "full_even",
            "full_odd",
            "parity_difference",
            "comparison_residual",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "real_string_checks.csv",
        (
            "check_id",
            "real_root_id",
            "other_root_id",
            "pairing",
            "serre_exponent",
            "expected_exponent",
            "exponent_residual",
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
            "proof_reference",
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
    path = fixture / "manifest.json"
    if not path.exists():
        raise ValueError(f"missing manifest: {path}")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme}")
    return json.loads(path.read_text(encoding="utf-8"))


def read_table(fixture: Path, spec: TableSpec) -> list[dict[str, str]]:
    path = fixture / spec.path
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != spec.columns:
            raise ValueError(
                f"{spec.path}: expected {spec.columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if not rows:
        raise ValueError(f"{spec.path}: expected at least one row")
    for row in rows:
        if None in row:
            raise ValueError(f"{spec.path}: unparsed CSV fields in row {row}")
    return rows


def rows_by_id(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        row_id = row[key]
        if row_id in out:
            raise ValueError(f"duplicate {key}: {row_id}")
        out[row_id] = row
    return out


def int_cell(row: dict[str, str], key: str) -> int:
    try:
        return int(row[key])
    except ValueError as exc:
        raise ValueError(f"{key}: noninteger value {row.get(key)!r} in {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row[key].strip().lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key}: nonboolean value {row.get(key)!r} in {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def beta(row: dict[str, str]) -> tuple[int, int, int]:
    return int_cell(row, "beta_c1"), int_cell(row, "beta_c2"), int_cell(row, "beta_c3")


def check_verified(row: dict[str, str], table_name: str) -> None:
    require_equal(row.get("check_status"), "verified", f"{table_name} check_status")
    if not row.get("proof_reference", "").strip():
        raise ValueError(f"{table_name}: missing proof_reference in {row}")


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("target_kind"), EXPECTED_KIND, "manifest target_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("target_only"), True, "manifest target_only")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")


def verify_degrees(rows: dict[str, dict[str, str]]) -> None:
    require_equal(set(rows), EXPECTED_DEGREES, "W<=3 degree set")
    phi = phi_01_coefficients()
    even_delta123, odd_delta123 = first_timelike_presentation_split(phi)
    require_equal((even_delta123, odd_delta123), (29, 93), "delta123 split")

    for degree_id, row in rows.items():
        check_verified(row, "target_degrees.csv")
        gamma = delta_basis_to_gamma(beta(row))
        require_equal(gamma[0], int_cell(row, "gamma_n"), f"{degree_id} gamma_n")
        require_equal(gamma[1], int_cell(row, "gamma_l"), f"{degree_id} gamma_l")
        require_equal(gamma[2], int_cell(row, "gamma_m"), f"{degree_id} gamma_m")
        require_equal(sum(beta(row)), int_cell(row, "height"), f"{degree_id} height")
        require_equal(delta_pair(beta(row), beta(row)), int_cell(row, "norm"), f"{degree_id} norm")
        signed = signed_root_supermultiplicity(phi, beta(row))
        require_equal(signed, int_cell(row, "signed_dimension"), f"{degree_id} signed")
        even = int_cell(row, "full_even")
        odd = int_cell(row, "full_odd")
        require_equal(even - odd, signed, f"{degree_id} parity difference")
        require_equal(row["parity_status"], "target_parity_verified", f"{degree_id} parity_status")
        if degree_id in REAL_SIMPLE:
            require_equal((even, odd), (1, 0), f"{degree_id} parity")
            require_equal(row["family"], "real_simple", f"{degree_id} family")
        elif degree_id in ISOTROPIC:
            require_equal((even, odd), (10, 0), f"{degree_id} parity")
            require_equal(row["family"], "isotropic_with_bracket", f"{degree_id} family")
        elif degree_id in REAL_STRING:
            require_equal((even, odd), (1, 0), f"{degree_id} parity")
            require_equal(row["family"], "height_three_real_string", f"{degree_id} family")
        elif degree_id == "delta123":
            require_equal((even, odd), (29, 93), "delta123 parity")
            require_equal(row["family"], "first_timelike", "delta123 family")


def verify_decomposition(rows: dict[str, dict[str, str]]) -> None:
    require_equal(set(rows), EXPECTED_DEGREES, "decomposition degree set")
    real_real_real = free_lie_multidegree_dimension((1, 1, 1))
    require_equal(real_real_real, 2, "free real-real-real dimension")
    odd_simple = monic_delta_qrs_coefficient(phi_01_coefficients())
    require_equal(odd_simple, 93, "delta123 odd imaginary simple")

    for degree_id, row in rows.items():
        check_verified(row, "decomposition.csv")
        require_equal(int_cell(row, "decomposition_defect_rank"), 0, f"{degree_id} decomposition defect")
        entries = {
            "real_simple_even": int_cell(row, "real_simple_even"),
            "real_bracket_even": int_cell(row, "real_bracket_even"),
            "isotropic_simple_even": int_cell(row, "isotropic_simple_even"),
            "real_string_even": int_cell(row, "real_string_even"),
            "real_real_real_even": int_cell(row, "real_real_real_even"),
            "mixed_real_isotropic_even": int_cell(row, "mixed_real_isotropic_even"),
            "odd_imaginary_simple": int_cell(row, "odd_imaginary_simple"),
        }
        total_even = sum(value for key, value in entries.items() if key != "odd_imaginary_simple")
        total_odd = entries["odd_imaginary_simple"]
        require_equal(total_even, int_cell(row, "total_even"), f"{degree_id} total_even")
        require_equal(total_odd, int_cell(row, "total_odd"), f"{degree_id} total_odd")
        if degree_id in REAL_SIMPLE:
            require_equal(entries, {
                "real_simple_even": 1,
                "real_bracket_even": 0,
                "isotropic_simple_even": 0,
                "real_string_even": 0,
                "real_real_real_even": 0,
                "mixed_real_isotropic_even": 0,
                "odd_imaginary_simple": 0,
            }, f"{degree_id} decomposition")
        elif degree_id in ISOTROPIC:
            require_equal(entries["real_bracket_even"], 1, f"{degree_id} real bracket")
            require_equal(entries["isotropic_simple_even"], 9, f"{degree_id} isotropic simple")
        elif degree_id in REAL_STRING:
            require_equal(entries["real_string_even"], 1, f"{degree_id} real string")
        elif degree_id == "delta123":
            require_equal(entries["real_real_real_even"], real_real_real, "delta123 real-real-real")
            require_equal(entries["mixed_real_isotropic_even"], 27, "delta123 mixed real-isotropic")
            require_equal(entries["odd_imaginary_simple"], odd_simple, "delta123 odd simple")


def verify_coefficients(
    rows: dict[str, dict[str, str]],
    degree_rows: dict[str, dict[str, str]],
) -> None:
    require_equal(set(rows), EXPECTED_DEGREES, "coefficient comparison degree set")
    phi = phi_01_coefficients()
    for degree_id, row in rows.items():
        check_verified(row, "coefficient_comparison.csv")
        degree = degree_rows[degree_id]
        gamma = delta_basis_to_gamma(beta(degree))
        require_equal(int_cell(row, "phi_n"), gamma[0] * gamma[2], f"{degree_id} phi_n")
        require_equal(int_cell(row, "phi_l"), gamma[1], f"{degree_id} phi_l")
        signed = int(phi.get((gamma[0] * gamma[2], gamma[1]), 0))
        require_equal(int_cell(row, "computed_coefficient"), signed, f"{degree_id} coefficient")
        even = int_cell(row, "full_even")
        odd = int_cell(row, "full_odd")
        require_equal(even - odd, int_cell(row, "parity_difference"), f"{degree_id} parity_difference")
        require_equal(signed - (even - odd), int_cell(row, "comparison_residual"), f"{degree_id} residual")


def verify_real_strings(rows: list[dict[str, str]]) -> None:
    by_name = {
        "delta_1": (1, 0, 0),
        "delta_2": (0, 1, 0),
        "delta_3": (0, 0, 1),
    }
    expected_pairs = {
        ("delta_1", "delta_2"),
        ("delta_1", "delta_3"),
        ("delta_2", "delta_1"),
        ("delta_2", "delta_3"),
        ("delta_3", "delta_1"),
        ("delta_3", "delta_2"),
    }
    seen: set[tuple[str, str]] = set()
    for row in rows:
        check_verified(row, "real_string_checks.csv")
        pair = (row["real_root_id"], row["other_root_id"])
        seen.add(pair)
        pairing = delta_pair(by_name[pair[0]], by_name[pair[1]])
        exponent = real_string_exponent(by_name[pair[0]], by_name[pair[1]])
        require_equal(pairing, int_cell(row, "pairing"), f"{row['check_id']} pairing")
        require_equal(exponent, int_cell(row, "serre_exponent"), f"{row['check_id']} exponent")
        require_equal(int_cell(row, "expected_exponent"), 3, f"{row['check_id']} expected exponent")
        require_equal(int_cell(row, "exponent_residual"), exponent - 3, f"{row['check_id']} residual")
    require_equal(seen, expected_pairs, "real string pair coverage")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "scalar_firewall.csv")
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
        degree_rows = rows_by_id(tables["target_degrees.csv"], "degree_id")
        verify_degrees(degree_rows)
        verify_decomposition(rows_by_id(tables["decomposition.csv"], "degree_id"))
        verify_coefficients(rows_by_id(tables["coefficient_comparison.csv"], "degree_id"), degree_rows)
        verify_real_strings(tables["real_string_checks.csv"])
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"WLE3_TARGET_FIXTURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
