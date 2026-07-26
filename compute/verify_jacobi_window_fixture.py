#!/usr/bin/env python3
"""Exact Jacobi-coefficient gate for the first relation window.

This verifier checks a target-arithmetic certificate only.  It
recomputes the coefficients of phi_{0,1}, compares f(nm,l) with the
A071 target signed dimensions, and verifies that the table does not
claim compact-source representatives, parity splits, Hall brackets, PBW
data, or primitive recognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from verify_square_root import delta_basis_to_gamma, phi_01_coefficients


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "COEFFICIENT_TABLE_VERIFIED"
EXPECTED_KIND = "finite_jacobi_window_candidate"
TARGET_FIXTURE_NAME = "a071_target_presentation"
FORBIDDEN_PROVENANCE_TOKENS = frozenset(
    {
        "arbitrary_matrices",
        "denominator_only",
        "mock",
        "pfaffian_only",
        "placeholder",
        "scalar_only",
        "signed_only_source",
        "status_only",
        "todo",
        "unsupplied",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "parity_split",
        "source_representatives",
        "hall_bracket",
        "pfaffian_line",
        "pbw_graded",
        "primitive_recognition",
        "compact_source_theorem",
    }
)
REQUIRED_NORMALIZATION_KINDS = frozenset(
    {
        "leading_q0",
        "evenness",
        "discriminant_dependence",
    }
)
REQUIRED_LEADING_Q0 = {
    -1: 1,
    0: 10,
    1: 1,
}


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]
    require_rows: bool = True


@dataclass
class CsvTable:
    spec: TableSpec
    rows: list[dict[str, str]]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "window_degrees.csv",
        (
            "degree_id",
            "tex_label",
            "beta_delta1",
            "beta_delta2",
            "beta_delta3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "nm",
            "relation_window_member",
            "target_signed_dimension",
            "target_dimension_status",
            "source_target_status",
            "source_formula_id",
            "target_fixture_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "normalization_laws.csv",
        (
            "law_id",
            "law_kind",
            "n",
            "l",
            "n_prime",
            "l_prime",
            "discriminant",
            "l_mod_2",
            "expected_left",
            "expected_right",
            "law_residual",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "jacobi_coefficients.csv",
        (
            "degree_id",
            "phi_n",
            "phi_l",
            "computed_coefficient",
            "target_signed_dimension",
            "coefficient_residual",
            "coefficient_status",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "discriminant_orbits.csv",
        (
            "orbit_id",
            "degree_ids",
            "discriminant",
            "l_mod_2",
            "orbit_coefficient",
            "orbit_size",
            "orbit_defect_rank",
            "source_formula_id",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "target_comparisons.csv",
        (
            "degree_id",
            "target_fixture_id",
            "target_signed_dimension",
            "computed_coefficient",
            "comparison_residual",
            "target_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "transitions.csv",
        (
            "transition_id",
            "from_window",
            "to_window",
            "strict_status",
            "coefficient_transition_defect_rank",
            "source_formula_id",
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
    parser.add_argument(
        "--fixture",
        type=Path,
        default=Path("certificates/jacobi/k3e_first_relation_window_coefficients"),
    )
    parser.add_argument(
        "--target-fixture",
        type=Path,
        default=Path("certificates/targets/delta5_gn_kac/a071_target_presentation"),
    )
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def read_csv_table(path: Path, spec: TableSpec) -> CsvTable:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != spec.columns:
            raise ValueError(
                f"{path.name}: expected columns {spec.columns}, got {tuple(reader.fieldnames or ())}"
            )
        rows = list(reader)
    if spec.require_rows and not rows:
        raise ValueError(f"{path.name}: expected at least one data row")
    return CsvTable(spec=spec, rows=rows)


def read_fixture(fixture: Path) -> tuple[dict, dict[str, CsvTable]]:
    manifest_path = fixture / MANIFEST_NAME
    readme_path = fixture / README_NAME
    if not manifest_path.exists():
        raise ValueError(f"missing manifest: {manifest_path}")
    if not readme_path.exists() or not readme_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    tables = {
        spec.path: read_csv_table(fixture / spec.path, spec) for spec in TABLE_SPECS
    }
    return manifest, tables


def read_target_fixture(target_fixture: Path) -> tuple[dict[str, dict[str, str]], dict[str, int], dict[str, str]]:
    degrees_path = target_fixture / "target_degrees.csv"
    dims_path = target_fixture / "target_dimensions.csv"
    if not degrees_path.exists() or not dims_path.exists():
        raise ValueError(f"target fixture lacks target_degrees.csv or target_dimensions.csv: {target_fixture}")

    with degrees_path.open(newline="", encoding="utf-8") as handle:
        degree_rows = {row["degree_id"]: row for row in csv.DictReader(handle)}
    with dims_path.open(newline="", encoding="utf-8") as handle:
        dimension_rows = {row["degree_id"]: row for row in csv.DictReader(handle)}

    signed_dimensions = {
        degree_id: int(row["signed_dimension"]) for degree_id, row in dimension_rows.items()
    }
    dimension_statuses = {
        degree_id: row["dimension_status"] for degree_id, row in dimension_rows.items()
    }
    return degree_rows, signed_dimensions, dimension_statuses


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


def coefficient(phi: dict[tuple[int, int], Fraction], n: int, l: int) -> int:
    value = phi.get((n, l), Fraction(0))
    if value.denominator != 1:
        raise ValueError(f"nonintegral phi_01 coefficient f({n},{l})={value}")
    return int(value)


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def check_status(row: dict[str, str], table_name: str) -> None:
    if row.get("check_status") != "verified":
        raise ValueError(f"{table_name}: row is not verified: {row}")


def check_provenance(row: dict[str, str], table_name: str) -> None:
    haystack = " ".join(row.values()).lower()
    for token in FORBIDDEN_PROVENANCE_TOKENS:
        if token in haystack:
            raise ValueError(f"{table_name}: forbidden provenance token {token!r} in {row}")
    if not row.get("proof_reference", "").strip():
        raise ValueError(f"{table_name}: missing proof_reference in {row}")


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("jacobi_kind"), EXPECTED_KIND, "manifest jacobi_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("coefficient_certified"), True, "manifest coefficient_certified")
    require_equal(manifest.get("normalization_laws_certified"), True, "manifest normalization_laws_certified")
    require_equal(manifest.get("target_only"), True, "manifest target_only")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("first_window_theorem"), False, "manifest first_window_theorem")
    require_equal(manifest.get("target_fixture_id"), TARGET_FIXTURE_NAME, "manifest target_fixture_id")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_normalization_laws(
    table: CsvTable,
    phi: dict[tuple[int, int], Fraction],
) -> None:
    seen_ids: set[str] = set()
    seen_kinds: set[str] = set()
    leading_values: dict[int, int] = {}
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        law_id = row["law_id"]
        if law_id in seen_ids:
            raise ValueError(f"duplicate normalization law: {law_id}")
        seen_ids.add(law_id)

        law_kind = row["law_kind"]
        if law_kind not in REQUIRED_NORMALIZATION_KINDS:
            raise ValueError(f"{law_id}: unknown law_kind {law_kind!r}")
        seen_kinds.add(law_kind)

        n = int_cell(row, "n")
        l = int_cell(row, "l")
        n_prime = int_cell(row, "n_prime")
        l_prime = int_cell(row, "l_prime")
        left_discriminant = 4 * n - l * l
        right_discriminant = 4 * n_prime - l_prime * l_prime
        left = coefficient(phi, n, l)
        right = coefficient(phi, n_prime, l_prime)

        require_equal(int_cell(row, "discriminant"), left_discriminant, f"{law_id} discriminant")
        require_equal(int_cell(row, "l_mod_2"), l % 2, f"{law_id} l_mod_2")
        require_equal(int_cell(row, "expected_left"), left, f"{law_id} expected_left")
        require_equal(int_cell(row, "expected_right"), right, f"{law_id} expected_right")
        require_equal(int_cell(row, "law_residual"), left - right, f"{law_id} law_residual")
        require_equal(row["source_formula_id"], "theta_series_phi_01_exact", f"{law_id} source_formula_id")

        if law_kind == "leading_q0":
            require_equal(n, 0, f"{law_id} leading n")
            require_equal(n_prime, 0, f"{law_id} leading n_prime")
            require_equal(l_prime, l, f"{law_id} leading l_prime")
            if l not in REQUIRED_LEADING_Q0:
                raise ValueError(f"{law_id}: unexpected leading q0 exponent l={l}")
            require_equal(left, REQUIRED_LEADING_Q0[l], f"{law_id} leading coefficient")
            leading_values[l] = left
        elif law_kind == "evenness":
            require_equal(n_prime, n, f"{law_id} evenness n_prime")
            require_equal(l_prime, -l, f"{law_id} evenness l_prime")
            require_equal(right_discriminant, left_discriminant, f"{law_id} evenness discriminant")
        elif law_kind == "discriminant_dependence":
            if (n, l) == (n_prime, l_prime):
                raise ValueError(f"{law_id}: discriminant-dependence row is vacuous")
            require_equal(right_discriminant, left_discriminant, f"{law_id} right discriminant")
            require_equal((l - l_prime) % 2, 0, f"{law_id} l parity")

    missing_kinds = REQUIRED_NORMALIZATION_KINDS - seen_kinds
    if missing_kinds:
        raise ValueError(f"normalization_laws.csv missing law kinds: {sorted(missing_kinds)}")
    require_equal(leading_values, REQUIRED_LEADING_Q0, "leading q0 normalization")


def verify_window_degrees(
    table: CsvTable,
    target_degrees: dict[str, dict[str, str]],
    target_dimensions: dict[str, int],
    target_statuses: dict[str, str],
) -> dict[str, dict[str, int | str]]:
    degree_data: dict[str, dict[str, int | str]] = {}
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        degree_id = row["degree_id"]
        if degree_id in degree_data:
            raise ValueError(f"duplicate degree_id: {degree_id}")
        if degree_id not in target_degrees:
            raise ValueError(f"{degree_id}: absent from target_degrees.csv")

        beta = (
            int_cell(row, "beta_delta1"),
            int_cell(row, "beta_delta2"),
            int_cell(row, "beta_delta3"),
        )
        gamma = delta_basis_to_gamma(beta)
        require_equal(gamma[0], int_cell(row, "gamma_n"), f"{degree_id} gamma_n")
        require_equal(gamma[1], int_cell(row, "gamma_l"), f"{degree_id} gamma_l")
        require_equal(gamma[2], int_cell(row, "gamma_m"), f"{degree_id} gamma_m")
        require_equal(gamma[0] * gamma[2], int_cell(row, "nm"), f"{degree_id} nm")
        require_equal(bool_cell(row, "relation_window_member"), True, f"{degree_id} relation_window_member")
        require_equal(row["source_target_status"], "target_arithmetic_only", f"{degree_id} source_target_status")
        require_equal(row["target_fixture_id"], TARGET_FIXTURE_NAME, f"{degree_id} target_fixture_id")
        require_equal(int_cell(row, "target_signed_dimension"), target_dimensions[degree_id], f"{degree_id} target signed dimension")
        require_equal(row["target_dimension_status"], target_statuses[degree_id], f"{degree_id} target dimension status")

        target_row = target_degrees[degree_id]
        for key, target_key in (
            ("beta_delta1", "beta_c1"),
            ("beta_delta2", "beta_c2"),
            ("beta_delta3", "beta_c3"),
            ("gamma_n", "gamma_n"),
            ("gamma_l", "gamma_l"),
            ("gamma_m", "gamma_m"),
        ):
            require_equal(row[key], target_row[target_key], f"{degree_id} {key} target comparison")

        degree_data[degree_id] = {
            "phi_n": int_cell(row, "nm"),
            "phi_l": gamma[1],
            "target_signed_dimension": target_dimensions[degree_id],
        }
    return degree_data


def verify_jacobi_coefficients(
    table: CsvTable,
    degree_data: dict[str, dict[str, int | str]],
    phi: dict[tuple[int, int], Fraction],
) -> dict[str, int]:
    values: dict[str, int] = {}
    seen: set[str] = set()
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        degree_id = row["degree_id"]
        if degree_id in seen:
            raise ValueError(f"duplicate coefficient row: {degree_id}")
        seen.add(degree_id)
        if degree_id not in degree_data:
            raise ValueError(f"coefficient row not in window_degrees: {degree_id}")
        data = degree_data[degree_id]
        phi_n = int_cell(row, "phi_n")
        phi_l = int_cell(row, "phi_l")
        require_equal(phi_n, data["phi_n"], f"{degree_id} phi_n")
        require_equal(phi_l, data["phi_l"], f"{degree_id} phi_l")
        computed = coefficient(phi, phi_n, phi_l)
        require_equal(int_cell(row, "computed_coefficient"), computed, f"{degree_id} coefficient")
        require_equal(
            int_cell(row, "target_signed_dimension"),
            data["target_signed_dimension"],
            f"{degree_id} target_signed_dimension",
        )
        require_equal(
            int_cell(row, "coefficient_residual"),
            computed - int(data["target_signed_dimension"]),
            f"{degree_id} coefficient_residual",
        )
        if computed == 0:
            require_equal(row["coefficient_status"], "terminal_zero_matches_target", f"{degree_id} coefficient_status")
        else:
            require_equal(row["coefficient_status"], "coefficient_matches_target", f"{degree_id} coefficient_status")
        values[degree_id] = computed
    require_equal(seen, set(degree_data), "coefficient degree coverage")
    return values


def verify_discriminant_orbits(
    table: CsvTable,
    degree_data: dict[str, dict[str, int | str]],
    coefficients: dict[str, int],
) -> None:
    covered: set[str] = set()
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        degree_ids = split_ids(row["degree_ids"])
        if not degree_ids:
            raise ValueError(f"{table.spec.path}: empty degree_ids in {row}")
        require_equal(int_cell(row, "orbit_size"), len(degree_ids), f"{row['orbit_id']} orbit_size")
        require_equal(int_cell(row, "orbit_defect_rank"), 0, f"{row['orbit_id']} orbit_defect_rank")
        orbit_coefficient = int_cell(row, "orbit_coefficient")
        for degree_id in degree_ids:
            if degree_id in covered:
                raise ValueError(f"{degree_id}: repeated in discriminant orbits")
            if degree_id not in degree_data:
                raise ValueError(f"{degree_id}: orbit degree absent from window_degrees")
            data = degree_data[degree_id]
            n = int(data["phi_n"])
            l = int(data["phi_l"])
            require_equal(4 * n - l * l, int_cell(row, "discriminant"), f"{degree_id} discriminant")
            require_equal(l % 2, int_cell(row, "l_mod_2"), f"{degree_id} l_mod_2")
            require_equal(coefficients[degree_id], orbit_coefficient, f"{degree_id} orbit coefficient")
            covered.add(degree_id)
    require_equal(covered, set(degree_data), "discriminant orbit coverage")


def verify_target_comparisons(
    table: CsvTable,
    degree_data: dict[str, dict[str, int | str]],
    coefficients: dict[str, int],
) -> None:
    seen: set[str] = set()
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        degree_id = row["degree_id"]
        if degree_id in seen:
            raise ValueError(f"duplicate target comparison row: {degree_id}")
        seen.add(degree_id)
        if degree_id not in degree_data:
            raise ValueError(f"target comparison degree absent from window_degrees: {degree_id}")
        require_equal(row["target_fixture_id"], TARGET_FIXTURE_NAME, f"{degree_id} target_fixture_id")
        target = int(degree_data[degree_id]["target_signed_dimension"])
        computed = coefficients[degree_id]
        require_equal(int_cell(row, "target_signed_dimension"), target, f"{degree_id} target")
        require_equal(int_cell(row, "computed_coefficient"), computed, f"{degree_id} computed")
        require_equal(int_cell(row, "comparison_residual"), computed - target, f"{degree_id} residual")
        expected_status = "terminal_zero_matched" if computed == 0 else "matched"
        require_equal(row["target_status"], expected_status, f"{degree_id} target_status")
    require_equal(seen, set(degree_data), "target comparison coverage")


def verify_transitions(table: CsvTable) -> None:
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        require_equal(row["strict_status"], "strict_verified", f"{row['transition_id']} strict_status")
        require_equal(
            int_cell(row, "coefficient_transition_defect_rank"),
            0,
            f"{row['transition_id']} coefficient_transition_defect_rank",
        )


def verify_scalar_firewall(table: CsvTable) -> None:
    seen: set[str] = set()
    for row in table.rows:
        check_status(row, table.spec.path)
        check_provenance(row, table.spec.path)
        substitute = row["forbidden_substitute"]
        if substitute in seen:
            raise ValueError(f"duplicate firewall substitute: {substitute}")
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"scalar_firewall.csv missing rows: {sorted(missing)}")


def verify_tables(
    tables: dict[str, CsvTable],
    target_fixture: Path,
) -> None:
    target_degrees, target_dimensions, target_statuses = read_target_fixture(target_fixture)
    phi = phi_01_coefficients()
    verify_normalization_laws(tables["normalization_laws.csv"], phi)
    degree_data = verify_window_degrees(
        tables["window_degrees.csv"],
        target_degrees,
        target_dimensions,
        target_statuses,
    )
    coefficients = verify_jacobi_coefficients(
        tables["jacobi_coefficients.csv"],
        degree_data,
        phi,
    )
    verify_discriminant_orbits(
        tables["discriminant_orbits.csv"],
        degree_data,
        coefficients,
    )
    verify_target_comparisons(
        tables["target_comparisons.csv"],
        degree_data,
        coefficients,
    )
    verify_transitions(tables["transitions.csv"])
    verify_scalar_firewall(tables["scalar_firewall.csv"])


def main() -> int:
    args = parse_args()
    try:
        manifest, tables = read_fixture(args.fixture)
        verify_manifest(manifest)
        verify_tables(tables, args.target_fixture)
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"JACOBI_WINDOW_FIXTURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
