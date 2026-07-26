#!/usr/bin/env python3
"""Mathematical consistency gate for the A071 target presentation.

This verifier checks the target-only Gritsenko--Nikulin/Kac packet
against the deterministic builder and the independent arithmetic in
``verify_square_root.py``.  It verifies the supplied target parity rows,
the signed-only blocked rows, basis counts, formal pairing/radical/PBW
summaries, and the firewall excluding compact-source use.

It does not construct compact K3xE representatives, source pairings,
source radicals, source PBW data, or primitive recognition.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from build_target_presentation_fixture import build_fixture_contents
from verify_square_root import (
    additive_m_coefficient,
    doubled_isotropic_gap_checks,
    first_timelike_presentation_split,
    height_four_timelike_gap_checks,
    phi_01_coefficients,
    real_string_relation_checks,
    signed_root_supermultiplicity,
)


SUCCESS_STATUS = "TARGET_PRESENTATION_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/targets/delta5_gn_kac/a071_target_presentation")
ACTIVE_PARITY_ROWS = frozenset(
    {
        "2a_12",
        "2a_13",
        "2a_23",
        "C_1_3",
        "C_2_3",
        "C_3_3",
        "C_1_4",
        "C_2_4",
        "C_3_4",
        "C_1_5",
        "C_2_5",
        "C_3_5",
    }
)
BLOCKED_ROWS = frozenset(
    {"C_1_2", "C_2_2", "C_3_2", "D_1", "D_2", "D_3", "2delta123"}
)
EXPECTED_FILES = tuple(build_fixture_contents())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise ValueError(f"empty table: {path}")
    for row in rows:
        if None in row:
            raise ValueError(f"{path.name}: unparsed CSV fields in row {row}")
    return rows


def require_equal(actual: object, expected: object, label: str) -> None:
    if actual != expected:
        raise ValueError(f"{label}: expected {expected!r}, got {actual!r}")


def int_cell(row: dict[str, str], key: str) -> int:
    value = row.get(key, "")
    if value == "":
        raise ValueError(f"{key}: blank integer cell in {row}")
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{key}: noninteger value {value!r} in {row}") from exc


def optional_int_cell(row: dict[str, str], key: str) -> int | None:
    value = row.get(key, "")
    if value == "":
        return None
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{key}: noninteger value {value!r} in {row}") from exc


def bool_cell(row: dict[str, str], key: str) -> bool:
    value = row.get(key, "").lower()
    if value == "true":
        return True
    if value == "false":
        return False
    raise ValueError(f"{key}: nonboolean value {row.get(key)!r} in {row}")


def beta(row: dict[str, str]) -> tuple[int, int, int]:
    return int_cell(row, "beta_c1"), int_cell(row, "beta_c2"), int_cell(row, "beta_c3")


def rows_by_id(rows: Iterable[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for row in rows:
        row_id = row[key]
        if row_id in out:
            raise ValueError(f"duplicate {key}: {row_id}")
        out[row_id] = row
    return out


def verify_generated_content(fixture: Path) -> None:
    expected = build_fixture_contents()
    for filename, expected_text in expected.items():
        path = fixture / filename
        if not path.exists():
            raise ValueError(f"missing generated file: {filename}")
        actual = path.read_text(encoding="utf-8")
        require_equal(actual, expected_text, f"generated content {filename}")


def verify_degree_and_dimension_tables(
    degree_rows: dict[str, dict[str, str]],
    dimension_rows: dict[str, dict[str, str]],
) -> None:
    require_equal(set(degree_rows), ACTIVE_PARITY_ROWS | BLOCKED_ROWS, "target degree ids")
    require_equal(set(dimension_rows), set(degree_rows), "dimension degree ids")

    phi = phi_01_coefficients()
    first_even, first_odd = first_timelike_presentation_split(phi)
    require_equal((first_even, first_odd), (29, 93), "first timelike target split")

    height_four_gaps = height_four_timelike_gap_checks(phi)
    doubled_gaps = doubled_isotropic_gap_checks(phi)
    require_equal(
        real_string_relation_checks()["complement_isotropic_exponent"],
        5,
        "complement isotropic real-string exponent",
    )

    expected_full: dict[str, tuple[int | None, int | None]] = {}
    expected_simple: dict[str, tuple[int | None, int | None, int | None]] = {}
    for degree_id in ("2a_12", "2a_13", "2a_23"):
        expected_full[degree_id] = (10, 0)
        signed, tau, gap = doubled_gaps[beta(degree_rows[degree_id])]
        require_equal((signed, tau, gap), (10, 9, 1), f"{degree_id} doubled isotropic gap")
        expected_simple[degree_id] = (9, 0, 1)
    for degree_id in ("C_1_3", "C_2_3", "C_3_3"):
        expected_full[degree_id] = (29, 93)
        expected_simple[degree_id] = (None, None, None)
    for degree_id in ("C_1_4", "C_2_4", "C_3_4"):
        expected_full[degree_id] = (10, 0)
        expected_simple[degree_id] = (None, None, None)
    for degree_id in ("C_1_5", "C_2_5", "C_3_5"):
        expected_full[degree_id] = (0, 0)
        expected_simple[degree_id] = (0, 0, 0)

    for degree_id in ("C_1_2", "C_2_2", "C_3_2"):
        signed, simple, residual = height_four_gaps[beta(degree_rows[degree_id])]
        require_equal((signed, simple, residual), (108, 90, 18), f"{degree_id} height-four gap")
        expected_simple[degree_id] = (90, 0, 18)
    for degree_id in ("D_1", "D_2", "D_3"):
        beta_value = beta(degree_rows[degree_id])
        signed = signed_root_supermultiplicity(phi, beta_value)
        simple = additive_m_coefficient(phi, beta_value)
        require_equal((signed, simple), (-513, 54), f"{degree_id} saturation-defect arithmetic")
        expected_simple[degree_id] = (54, 0, signed - simple)
    expected_simple["2delta123"] = (0, 540, None)

    for degree_id, row in degree_rows.items():
        dim = dimension_rows[degree_id]
        require_equal(row["computation_hash"], dim["computation_hash"], f"{degree_id} hash bridge")
        signed = signed_root_supermultiplicity(phi, beta(row))
        require_equal(int_cell(row, "smult"), signed, f"{degree_id} degree signed multiplicity")
        require_equal(int_cell(dim, "signed_dimension"), signed, f"{degree_id} dimension signed multiplicity")
        require_equal(bool_cell(row, "is_parity_fixture"), degree_id in ACTIVE_PARITY_ROWS, f"{degree_id} active status")
        require_equal(bool_cell(dim, "is_parity_fixture"), degree_id in ACTIVE_PARITY_ROWS, f"{degree_id} dimension active status")

        if degree_id in ACTIVE_PARITY_ROWS:
            require_equal(row["fixture_status"], "target_parity_fixture", f"{degree_id} fixture_status")
            require_equal(dim["dimension_status"], "target_parity_dimension", f"{degree_id} dimension_status")
            even, odd = expected_full[degree_id]
            require_equal(optional_int_cell(dim, "full_even"), even, f"{degree_id} full_even")
            require_equal(optional_int_cell(dim, "full_odd"), odd, f"{degree_id} full_odd")
            assert even is not None and odd is not None
            require_equal(even - odd, signed, f"{degree_id} parity signed difference")
        else:
            require_equal(row["fixture_status"], "signed_only_blocked", f"{degree_id} fixture_status")
            require_equal(dim["dimension_status"], "signed_only_no_parity_split", f"{degree_id} dimension_status")
            require_equal(optional_int_cell(dim, "full_even"), None, f"{degree_id} full_even blocked")
            require_equal(optional_int_cell(dim, "full_odd"), None, f"{degree_id} full_odd blocked")

        simple_even, simple_odd, residual = expected_simple[degree_id]
        require_equal(optional_int_cell(dim, "simple_even"), simple_even, f"{degree_id} simple_even")
        require_equal(optional_int_cell(dim, "simple_odd"), simple_odd, f"{degree_id} simple_odd")
        require_equal(optional_int_cell(dim, "signed_residual"), residual, f"{degree_id} signed_residual")


def verify_basis_counts(
    basis_rows: list[dict[str, str]],
    dimension_rows: dict[str, dict[str, str]],
) -> None:
    counts: Counter[tuple[str, str]] = Counter()
    indices: defaultdict[tuple[str, str], list[int]] = defaultdict(list)
    for row in basis_rows:
        degree_id = row["degree_id"]
        if degree_id in BLOCKED_ROWS:
            raise ValueError(f"blocked row has target basis vector: {degree_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"bad basis parity {parity!r} in {row}")
        counts[(degree_id, parity)] += 1
        indices[(degree_id, parity)].append(int_cell(row, "index_in_parity"))
        require_equal(row["basis_status"], "target_reference_basis", f"{row['basis_id']} basis_status")

    for degree_id in ACTIVE_PARITY_ROWS:
        dim = dimension_rows[degree_id]
        for parity, field in (("even", "full_even"), ("odd", "full_odd")):
            expected = optional_int_cell(dim, field)
            assert expected is not None
            require_equal(counts[(degree_id, parity)], expected, f"{degree_id} {parity} basis count")
            expected_indices = list(range(1, expected + 1))
            require_equal(sorted(indices[(degree_id, parity)]), expected_indices, f"{degree_id} {parity} basis indices")


def verify_simple_generators(rows: list[dict[str, str]]) -> None:
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(
        set(by_degree),
        {
            "2a_12",
            "2a_13",
            "2a_23",
            "C_1_2",
            "C_2_2",
            "C_3_2",
            "D_1",
            "D_2",
            "D_3",
            "2delta123",
        },
        "simple generator rows",
    )
    for degree_id in ("2a_12", "2a_13", "2a_23"):
        row = by_degree[degree_id]
        require_equal(row["generator_block"], "gn_isotropic_simple_t2", f"{degree_id} generator block")
        require_equal(row["parity"], "even", f"{degree_id} generator parity")
        require_equal(int_cell(row, "count"), 9, f"{degree_id} generator count")
        require_equal(bool_cell(row, "feeds_basis"), True, f"{degree_id} feeds_basis")
    for degree_id in ("C_1_2", "C_2_2", "C_3_2"):
        row = by_degree[degree_id]
        require_equal(row["generator_block"], "gn_timelike_simple_m_positive", f"{degree_id} generator block")
        require_equal(row["parity"], "even", f"{degree_id} generator parity")
        require_equal(int_cell(row, "count"), 90, f"{degree_id} generator count")
        require_equal(row["fixture_status"], "signed_only_blocked", f"{degree_id} fixture_status")
        require_equal(bool_cell(row, "feeds_basis"), False, f"{degree_id} feeds_basis")
    for degree_id in ("D_1", "D_2", "D_3"):
        row = by_degree[degree_id]
        require_equal(row["generator_block"], "gn_timelike_simple_m_positive", f"{degree_id} generator block")
        require_equal(row["parity"], "even", f"{degree_id} generator parity")
        require_equal(int_cell(row, "count"), 54, f"{degree_id} generator count")
        require_equal(row["fixture_status"], "signed_only_blocked", f"{degree_id} fixture_status")
        require_equal(bool_cell(row, "feeds_basis"), False, f"{degree_id} feeds_basis")
    row = by_degree["2delta123"]
    require_equal(row["generator_block"], "gn_timelike_simple_m_negative", "2delta123 generator block")
    require_equal(row["parity"], "odd", "2delta123 generator parity")
    require_equal(int_cell(row, "count"), 540, "2delta123 generator count")
    require_equal(bool_cell(row, "feeds_basis"), False, "2delta123 feeds_basis")


def verify_relation_pairing_radical_pbw(
    relation_rows: dict[str, dict[str, str]],
    pairing_rows: dict[str, dict[str, str]],
    radical_rows: dict[str, dict[str, str]],
    pbw_rows: dict[str, dict[str, str]],
    dimension_rows: dict[str, dict[str, str]],
) -> None:
    expected_ids = ACTIVE_PARITY_ROWS | BLOCKED_ROWS
    require_equal(set(relation_rows), {f"rel.{degree_id}" for degree_id in expected_ids}, "relation ids")
    require_equal(set(pairing_rows), expected_ids, "pairing ids")
    require_equal(set(radical_rows), expected_ids, "radical ids")
    require_equal(set(pbw_rows), expected_ids, "pbw ids")

    for degree_id in expected_ids:
        relation = relation_rows[f"rel.{degree_id}"]
        pairing = pairing_rows[degree_id]
        radical = radical_rows[degree_id]
        pbw = pbw_rows[degree_id]
        dim = dimension_rows[degree_id]
        require_equal(bool_cell(pairing, "source_pairing"), False, f"{degree_id} source_pairing")
        require_equal(bool_cell(radical, "source_radical"), False, f"{degree_id} source_radical")
        require_equal(bool_cell(pbw, "feeds_source_comparison"), False, f"{degree_id} feeds_source_comparison")

        if degree_id in ACTIVE_PARITY_ROWS:
            require_equal(relation["relation_status"], "recorded_target_relation", f"{degree_id} relation_status")
            require_equal(pairing["pairing_block_status"], "target_negative_dual_formal_block", f"{degree_id} pairing status")
            require_equal(radical["radical_status"], "target_quotient_radical_zero", f"{degree_id} radical status")
            require_equal(pbw["pbw_status"], "target_reference_summary_no_source_pbw", f"{degree_id} pbw status")
            even = optional_int_cell(dim, "full_even")
            odd = optional_int_cell(dim, "full_odd")
            assert even is not None and odd is not None
            for field in ("positive_even", "negative_even"):
                require_equal(optional_int_cell(pairing, field), even, f"{degree_id} {field}")
            for field in ("positive_odd", "negative_odd"):
                require_equal(optional_int_cell(pairing, field), odd, f"{degree_id} {field}")
            require_equal(optional_int_cell(radical, "radical_even"), 0, f"{degree_id} radical_even")
            require_equal(optional_int_cell(radical, "radical_odd"), 0, f"{degree_id} radical_odd")
            require_equal(optional_int_cell(pbw, "basis_vectors_even"), even, f"{degree_id} pbw even")
            require_equal(optional_int_cell(pbw, "basis_vectors_odd"), odd, f"{degree_id} pbw odd")
        else:
            require_equal(relation["relation_status"], "blocked_no_relation_fixture", f"{degree_id} relation_status")
            require_equal(pairing["pairing_block_status"], "blocked_no_pairing_block", f"{degree_id} pairing status")
            require_equal(radical["radical_status"], "blocked_no_radical_fixture", f"{degree_id} radical status")
            require_equal(pbw["pbw_status"], "blocked_signed_only_no_pbw", f"{degree_id} pbw status")
            for field in ("positive_even", "positive_odd", "negative_even", "negative_odd"):
                require_equal(optional_int_cell(pairing, field), None, f"{degree_id} {field}")
            require_equal(optional_int_cell(radical, "radical_even"), None, f"{degree_id} radical_even")
            require_equal(optional_int_cell(radical, "radical_odd"), None, f"{degree_id} radical_odd")
            require_equal(optional_int_cell(pbw, "basis_vectors_even"), None, f"{degree_id} pbw even")
            require_equal(optional_int_cell(pbw, "basis_vectors_odd"), None, f"{degree_id} pbw odd")


def verify_fixture(fixture: Path) -> None:
    verify_generated_content(fixture)
    degree_rows = rows_by_id(read_csv(fixture / "target_degrees.csv"), "degree_id")
    dimension_rows = rows_by_id(read_csv(fixture / "target_dimensions.csv"), "degree_id")
    verify_degree_and_dimension_tables(degree_rows, dimension_rows)
    verify_basis_counts(read_csv(fixture / "target_hall_lie_basis.csv"), dimension_rows)
    verify_simple_generators(read_csv(fixture / "target_simple_generators.csv"))
    verify_relation_pairing_radical_pbw(
        rows_by_id(read_csv(fixture / "target_relation_rows.csv"), "relation_id"),
        rows_by_id(read_csv(fixture / "target_pairing_blocks.csv"), "degree_id"),
        rows_by_id(read_csv(fixture / "target_radicals.csv"), "degree_id"),
        rows_by_id(read_csv(fixture / "target_pbw.csv"), "degree_id"),
        dimension_rows,
    )


def main() -> int:
    args = parse_args()
    try:
        verify_fixture(args.fixture)
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"TARGET_PRESENTATION_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
