#!/usr/bin/env python3
"""Delta_123 presentation-split gate for the Delta_5 BKM target.

This verifier checks the first timelike target presentation split:

* delta_123 has beta=(1,1,1), gamma=(1,1,1), norm -6;
* smult(delta_123)=f(1,1)=-64;
* the monic qrs coefficient of D_5/(qrs)^(1/2) is 93, hence
  m(delta_123)=-93 in the GN additive correction convention;
* the even presentation count is 29=2+27;
* the two real-real-real directions come from the three Jacobi words
  T_1,T_2,T_3 modulo T_1+T_2+T_3=0;
* the 27 mixed real-isotropic directions are the brackets [e_k,u_{ij,r}];
* the 93 odd directions are the negative-norm imaginary simple fibre.

It is a target-presentation certificate only.  It does not construct
compact source representatives, source Hall brackets, pairings,
radicals, PBW data, Pfaffian orientations, O2 wall atlases, mirror
discriminants, or protected traces.
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
    additive_m_coefficient,
    delta_basis_to_gamma,
    delta_pair,
    first_timelike_presentation_split,
    free_lie_multidegree_dimension,
    monic_delta_qrs_coefficient,
    phi_01_coefficients,
    signed_root_supermultiplicity,
)


MANIFEST_NAME = "manifest.json"
README_NAME = "README.md"
SUCCESS_STATUS = "DELTA123_PRESENTATION_SPLIT_VERIFIED"
EXPECTED_KIND = "delta123_presentation_split_target"
DEFAULT_FIXTURE = Path("certificates/targets/delta5_gn_kac/delta123_presentation_split")
DEFAULT_WLE3_FIXTURE = Path("certificates/targets/delta5_gn_kac/wle3_target_parity")
DEFAULT_CHAMBER_FIXTURE = Path("certificates/lattice/type_ii_chamber_isotropic")
DELTA123 = (1, 1, 1)
EXPECTED_GAMMA = (1, 1, 1)
REAL_ROOTS = {"delta_1": (1, 0, 0), "delta_2": (0, 1, 0), "delta_3": (0, 0, 1)}
RAY_DEGREES = {"a_12": (1, 1, 0), "a_13": (1, 0, 1), "a_23": (0, 1, 1)}
RAY_COMPLEMENTS = {"a_12": "delta_3", "a_13": "delta_2", "a_23": "delta_1"}
REAL_REAL_WORDS = {
    "T_1": ("[e_1,[e_2,e_3]]", 1, True),
    "T_2": ("[e_2,[e_3,e_1]]", 1, True),
    "T_3": ("[e_3,[e_1,e_2]]", 1, False),
}
REQUIRED_RELATIONS = frozenset(
    {
        "delta123_norm",
        "delta123_signed_dimension",
        "monic_qrs_coefficient",
        "additive_m_delta123",
        "real_real_real_dimension",
        "mixed_real_isotropic_count",
        "odd_imaginary_count",
        "even_presentation_count",
        "parity_difference",
        "wle3_crosscheck",
        "chamber_isotropic_crosscheck",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source_representatives",
        "source_hall_bracket",
        "source_parity",
        "pairing_radical",
        "pbw_comparison",
        "pfaffian_orientation",
        "o2_wall_atlas",
        "mirror_discriminant",
        "protected_trace",
    }
)
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "delta123_degree.csv",
        (
            "degree_id",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "phi_index_n",
            "phi_l",
            "signed_dimension",
            "monic_qrs_coefficient",
            "additive_m",
            "full_even",
            "full_odd",
            "parity_difference",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "real_real_real_words.csv",
        (
            "word_id",
            "word",
            "degree_id",
            "relation_id",
            "relation_coefficient",
            "basis_representative",
            "real_real_real_dimension",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "mixed_real_isotropic_words.csv",
        (
            "word_id",
            "ray_id",
            "real_root_id",
            "direction_index",
            "source_direction_id",
            "degree_id",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "mixed_even",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "odd_imaginary_generators.csv",
        (
            "generator_id",
            "degree_id",
            "generator_index",
            "parity",
            "signed_contribution",
            "fibre_size",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "split_relations.csv",
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
    parser.add_argument("--wle3-fixture", type=Path, default=DEFAULT_WLE3_FIXTURE)
    parser.add_argument("--chamber-fixture", type=Path, default=DEFAULT_CHAMBER_FIXTURE)
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


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise ValueError(f"missing dependency table: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


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


def vector_sum(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[i] + right[i] for i in range(3))


def read_wle3_delta123(wle3_fixture: Path) -> tuple[int, int, int]:
    rows = read_csv(wle3_fixture / "target_degrees.csv")
    for row in rows:
        if row.get("degree_id") == "delta123":
            return int(row["full_even"]), int(row["full_odd"]), int(row["signed_dimension"])
    raise ValueError("wle3 target_degrees.csv has no delta123 row")


def read_wle3_decomposition(wle3_fixture: Path) -> tuple[int, int, int]:
    rows = read_csv(wle3_fixture / "decomposition.csv")
    for row in rows:
        if row.get("degree_id") == "delta123":
            return (
                int(row["real_real_real_even"]),
                int(row["mixed_real_isotropic_even"]),
                int(row["odd_imaginary_simple"]),
            )
    raise ValueError("wle3 decomposition.csv has no delta123 row")


def read_chamber_direction_ids(chamber_fixture: Path) -> set[str]:
    rows = read_csv(chamber_fixture / "gn_isotropic_directions.csv")
    return {row["direction_id"] for row in rows}


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("target_kind"), EXPECTED_KIND, "manifest target_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("target_only"), True, "manifest target_only")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("source_hall_bracket"), False, "manifest source_hall_bracket")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("o2_wall_atlas"), False, "manifest o2_wall_atlas")
    require_equal(manifest.get("mirror_discriminant"), False, "manifest mirror_discriminant")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_delta123_degree(rows: list[dict[str, str]], wle3_delta123: tuple[int, int, int]) -> dict[str, int]:
    if len(rows) != 1:
        raise ValueError("delta123_degree.csv: expected exactly one row")
    row = rows[0]
    check_row(row, "delta123_degree.csv")
    phi = phi_01_coefficients()
    require_equal(row["degree_id"], "delta123", "degree_id")
    beta = (int_cell(row, "beta_c1"), int_cell(row, "beta_c2"), int_cell(row, "beta_c3"))
    require_equal(beta, DELTA123, "delta123 beta")
    gamma = delta_basis_to_gamma(beta)
    require_equal(gamma, EXPECTED_GAMMA, "delta123 gamma")
    require_equal((int_cell(row, "gamma_n"), int_cell(row, "gamma_l"), int_cell(row, "gamma_m")), gamma, "displayed gamma")
    require_equal(int_cell(row, "height"), sum(beta), "height")
    require_equal(int_cell(row, "norm"), delta_pair(beta, beta), "norm")
    require_equal(int_cell(row, "norm"), -6, "norm expected")
    require_equal(int_cell(row, "phi_index_n"), gamma[0] * gamma[2], "phi_index_n")
    require_equal(int_cell(row, "phi_l"), gamma[1], "phi_l")
    signed = signed_root_supermultiplicity(phi, beta)
    monic = monic_delta_qrs_coefficient(phi)
    additive = additive_m_coefficient(phi, beta)
    require_equal(int_cell(row, "signed_dimension"), signed, "signed_dimension")
    require_equal(signed, -64, "signed_dimension expected")
    require_equal(int_cell(row, "monic_qrs_coefficient"), monic, "monic qrs coefficient")
    require_equal(monic, 93, "monic qrs expected")
    require_equal(int_cell(row, "additive_m"), additive, "additive m")
    require_equal(additive, -93, "additive m expected")
    even = int_cell(row, "full_even")
    odd = int_cell(row, "full_odd")
    require_equal((even, odd, signed), wle3_delta123, "wle3 delta123 crosscheck")
    require_equal(even - odd, int_cell(row, "parity_difference"), "parity_difference")
    require_equal(even - odd, signed, "parity difference signed")
    return {
        "signed": signed,
        "monic": monic,
        "additive": additive,
        "even": even,
        "odd": odd,
    }


def verify_real_real_real_words(rows: list[dict[str, str]]) -> int:
    seen: set[str] = set()
    basis_count = 0
    relation_sum = 0
    for row in rows:
        check_row(row, "real_real_real_words.csv")
        word_id = row["word_id"]
        if word_id in seen:
            raise ValueError(f"real_real_real_words.csv: duplicate word_id {word_id}")
        seen.add(word_id)
        if word_id not in REAL_REAL_WORDS:
            raise ValueError(f"real_real_real_words.csv: unexpected word_id {word_id}")
        word, relation_coefficient, basis_representative = REAL_REAL_WORDS[word_id]
        require_equal(row["word"], word, f"{word_id} word")
        require_equal(row["degree_id"], "delta123", f"{word_id} degree_id")
        require_equal(row["relation_id"], "jacobi_T1_plus_T2_plus_T3", f"{word_id} relation_id")
        require_equal(int_cell(row, "relation_coefficient"), relation_coefficient, f"{word_id} relation_coefficient")
        require_equal(bool_cell(row, "basis_representative"), basis_representative, f"{word_id} basis_representative")
        require_equal(int_cell(row, "real_real_real_dimension"), 2, f"{word_id} dimension")
        basis_count += 1 if basis_representative else 0
        relation_sum += relation_coefficient
    require_equal(seen, set(REAL_REAL_WORDS), "real-real-real word coverage")
    require_equal(basis_count, free_lie_multidegree_dimension((1, 1, 1)), "real-real-real basis count")
    require_equal(relation_sum, 3, "Jacobi relation support count")
    return basis_count


def verify_mixed_words(rows: list[dict[str, str]], chamber_direction_ids: set[str]) -> int:
    seen: set[str] = set()
    for row in rows:
        check_row(row, "mixed_real_isotropic_words.csv")
        word_id = row["word_id"]
        if word_id in seen:
            raise ValueError(f"mixed_real_isotropic_words.csv: duplicate word_id {word_id}")
        seen.add(word_id)
        ray_id = row["ray_id"]
        if ray_id not in RAY_DEGREES:
            raise ValueError(f"mixed_real_isotropic_words.csv: unexpected ray_id {ray_id}")
        real_root_id = row["real_root_id"]
        require_equal(real_root_id, RAY_COMPLEMENTS[ray_id], f"{word_id} real_root_id")
        index = int_cell(row, "direction_index")
        if index < 1 or index > 9:
            raise ValueError(f"{word_id}: direction_index outside 1..9")
        suffix = ray_id[2:]
        source_direction_id = f"u_{suffix}_{index}"
        expected_word_id = f"mix_{suffix}_{index}"
        require_equal(word_id, expected_word_id, f"{word_id} expected id")
        require_equal(row["source_direction_id"], source_direction_id, f"{word_id} source_direction_id")
        if source_direction_id not in chamber_direction_ids:
            raise ValueError(f"{word_id}: source direction {source_direction_id} absent from chamber packet")
        require_equal(row["degree_id"], "delta123", f"{word_id} degree_id")
        degree = vector_sum(RAY_DEGREES[ray_id], REAL_ROOTS[real_root_id])
        require_equal((int_cell(row, "beta_c1"), int_cell(row, "beta_c2"), int_cell(row, "beta_c3")), degree, f"{word_id} degree")
        require_equal(degree, DELTA123, f"{word_id} delta123 degree")
        require_equal(int_cell(row, "mixed_even"), 1, f"{word_id} mixed_even")
    require_equal(len(seen), 27, "mixed word count")
    return len(seen)


def verify_odd_generators(rows: list[dict[str, str]]) -> int:
    seen: set[str] = set()
    indices: set[int] = set()
    for row in rows:
        check_row(row, "odd_imaginary_generators.csv")
        generator_id = row["generator_id"]
        if generator_id in seen:
            raise ValueError(f"odd_imaginary_generators.csv: duplicate generator_id {generator_id}")
        seen.add(generator_id)
        index = int_cell(row, "generator_index")
        require_equal(generator_id, f"xi_delta123_{index:03d}", f"{generator_id} label")
        require_equal(row["degree_id"], "delta123", f"{generator_id} degree_id")
        require_equal(row["parity"], "odd", f"{generator_id} parity")
        require_equal(int_cell(row, "signed_contribution"), -1, f"{generator_id} signed_contribution")
        require_equal(int_cell(row, "fibre_size"), 93, f"{generator_id} fibre_size")
        indices.add(index)
    require_equal(indices, set(range(1, 94)), "odd generator indices")
    return len(seen)


def verify_split_relations(
    rows: list[dict[str, str]],
    degree_data: dict[str, int],
    real_real_count: int,
    mixed_count: int,
    odd_count: int,
    wle3_decomposition: tuple[int, int, int],
    chamber_direction_ids: set[str],
) -> None:
    relation_values = {
        "delta123_norm": -6,
        "delta123_signed_dimension": degree_data["signed"],
        "monic_qrs_coefficient": degree_data["monic"],
        "additive_m_delta123": degree_data["additive"],
        "real_real_real_dimension": real_real_count,
        "mixed_real_isotropic_count": mixed_count,
        "odd_imaginary_count": odd_count,
        "even_presentation_count": real_real_count + mixed_count,
        "parity_difference": degree_data["even"] - degree_data["odd"],
        "wle3_crosscheck": 1 if wle3_decomposition == (real_real_count, mixed_count, odd_count) else 0,
        "chamber_isotropic_crosscheck": 1 if len(chamber_direction_ids) == 27 else 0,
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "split_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"split_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"split_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed")
        require_equal(int_cell(row, "computed_value"), int_cell(row, "expected_value"), f"{relation_id} expected")
        require_equal(int_cell(row, "defect_rank"), 0, f"{relation_id} defect")
    require_equal(seen, REQUIRED_RELATIONS, "split relation coverage")


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
        wle3_delta123 = read_wle3_delta123(args.wle3_fixture)
        wle3_decomposition = read_wle3_decomposition(args.wle3_fixture)
        chamber_direction_ids = read_chamber_direction_ids(args.chamber_fixture)
        degree_data = verify_delta123_degree(tables["delta123_degree.csv"], wle3_delta123)
        real_real_count = verify_real_real_real_words(tables["real_real_real_words.csv"])
        mixed_count = verify_mixed_words(tables["mixed_real_isotropic_words.csv"], chamber_direction_ids)
        odd_count = verify_odd_generators(tables["odd_imaginary_generators.csv"])
        verify_split_relations(
            tables["split_relations.csv"],
            degree_data,
            real_real_count,
            mixed_count,
            odd_count,
            wle3_decomposition,
            chamber_direction_ids,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"DELTA123_PRESENTATION_SPLIT_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
