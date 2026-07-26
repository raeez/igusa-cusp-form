#!/usr/bin/env python3
"""Finite parity-pushforward gate for the normal-ordered Gram grading.

This verifier checks the finite super-vector-space statement that
pushforward along the additive normal-ordered Gram grading preserves the
even/odd direct-sum decomposition:

    (phi_* V)_{gamma,p} = direct sum_{phi(c)=gamma} V_{c,p}.

It also checks that signed superdimension is derived from the two
parity ranks, not used as a substitute for them.  The packet does not
certify source parity, the GN/Kac parity split, compact source
representatives, primitive recognition, Pfaffian orientations, or
protected traces.
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
SUCCESS_STATUS = "PARITY_PUSHFORWARD_VERIFIED"
EXPECTED_KIND = "parity_pushforward_formal_super_vector_space"
DEFAULT_FIXTURE = Path("certificates/charge/parity_pushforward")
FORBIDDEN_TOKENS = frozenset({"mock", "placeholder", "todo", "unsupplied"})
REQUIRED_RELATIONS = frozenset(
    {
        "source_row_count",
        "pushforward_degree_count",
        "signed_shadow_rows",
        "zero_signed_not_zero_object",
        "parity_pushforward_preserves_blocks",
        "source_parity_not_proved",
        "gn_kac_parity_not_proved",
    }
)
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "source_parity_certification",
        "gn_kac_parity_equality",
        "compact_source",
        "primitive_recognition",
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
        "source_parity_rows.csv",
        (
            "source_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "parity",
            "dimension",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "pushforward_parity_sums.csv",
        (
            "pushforward_id",
            "degree_id",
            "degree_n",
            "degree_l",
            "degree_m",
            "source_ids",
            "even_dimension",
            "odd_dimension",
            "total_dimension",
            "parity_defect_rank",
            "source_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "signed_shadow.csv",
        (
            "shadow_id",
            "degree_id",
            "even_dimension",
            "odd_dimension",
            "signed_superdimension",
            "total_dimension",
            "hidden_zero_superdimension_excluded",
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


Triple = tuple[int, int, int]


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
    if not row.get("source_reference", "").strip():
        raise ValueError(f"{table_name}: missing source_reference: {row}")
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


def triple_from_row(row: dict[str, str]) -> Triple:
    return int_cell(row, "degree_n"), int_cell(row, "degree_l"), int_cell(row, "degree_m")


def split_ids(cell: str) -> list[str]:
    ids = [part.strip() for part in cell.split(";") if part.strip()]
    if not ids:
        raise ValueError(f"empty source_ids cell {cell!r}")
    return ids


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("charge_kind"), EXPECTED_KIND, "manifest charge_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(
        manifest.get("normal_ordered_parity_pushforward"),
        True,
        "manifest normal_ordered_parity_pushforward",
    )
    require_equal(manifest.get("source_parity_certification"), False, "manifest source_parity_certification")
    require_equal(manifest.get("gn_kac_parity_equality"), False, "manifest gn_kac_parity_equality")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("pfaffian_orientation"), False, "manifest pfaffian_orientation")
    require_equal(manifest.get("protected_trace"), False, "manifest protected_trace")
    require_equal(manifest.get("tables"), [spec.path for spec in TABLE_SPECS], "manifest tables")


def verify_source_rows(rows: list[dict[str, str]]) -> dict[str, tuple[str, Triple, str, int]]:
    sources: dict[str, tuple[str, Triple, str, int]] = {}
    for row in rows:
        check_row(row, "source_parity_rows.csv")
        source_id = row["source_id"]
        if source_id in sources:
            raise ValueError(f"source_parity_rows.csv: duplicate source_id {source_id}")
        parity = row["parity"]
        if parity not in {"even", "odd"}:
            raise ValueError(f"source_parity_rows.csv: bad parity {parity!r}")
        dimension = int_cell(row, "dimension")
        if dimension <= 0:
            raise ValueError(f"source_parity_rows.csv: nonpositive dimension in {row}")
        sources[source_id] = (row["degree_id"], triple_from_row(row), parity, dimension)
    return sources


def verify_pushforward_rows(
    rows: list[dict[str, str]],
    sources: dict[str, tuple[str, Triple, str, int]],
) -> dict[str, tuple[int, int, int]]:
    profiles: dict[str, tuple[int, int, int]] = {}
    for row in rows:
        check_row(row, "pushforward_parity_sums.csv")
        degree_id = row["degree_id"]
        if degree_id in profiles:
            raise ValueError(f"pushforward_parity_sums.csv: duplicate degree_id {degree_id}")
        row_degree = triple_from_row(row)
        even_sum = 0
        odd_sum = 0
        for source_id in split_ids(row["source_ids"]):
            if source_id not in sources:
                raise ValueError(f"pushforward_parity_sums.csv: unknown source_id {source_id}")
            source_degree_id, source_degree, parity, dimension = sources[source_id]
            require_equal(source_degree_id, degree_id, f"{source_id} degree_id")
            require_equal(source_degree, row_degree, f"{source_id} degree")
            if parity == "even":
                even_sum += dimension
            else:
                odd_sum += dimension
        require_equal(int_cell(row, "even_dimension"), even_sum, f"{degree_id} even dimension")
        require_equal(int_cell(row, "odd_dimension"), odd_sum, f"{degree_id} odd dimension")
        require_equal(int_cell(row, "total_dimension"), even_sum + odd_sum, f"{degree_id} total dimension")
        require_zero(int_cell(row, "parity_defect_rank"), f"{degree_id} parity defect")
        profiles[degree_id] = (even_sum, odd_sum, even_sum + odd_sum)
    return profiles


def verify_signed_shadow(rows: list[dict[str, str]], profiles: dict[str, tuple[int, int, int]]) -> int:
    seen: set[str] = set()
    zero_signed_nonzero_total = 0
    for row in rows:
        check_row(row, "signed_shadow.csv")
        shadow_id = row["shadow_id"]
        if shadow_id in seen:
            raise ValueError(f"signed_shadow.csv: duplicate shadow_id {shadow_id}")
        seen.add(shadow_id)
        degree_id = row["degree_id"]
        if degree_id not in profiles:
            raise ValueError(f"signed_shadow.csv: unknown degree_id {degree_id}")
        even_dim, odd_dim, total_dim = profiles[degree_id]
        signed = even_dim - odd_dim
        require_equal(int_cell(row, "even_dimension"), even_dim, f"{degree_id} shadow even")
        require_equal(int_cell(row, "odd_dimension"), odd_dim, f"{degree_id} shadow odd")
        require_equal(int_cell(row, "signed_superdimension"), signed, f"{degree_id} signed shadow")
        require_equal(int_cell(row, "total_dimension"), total_dim, f"{degree_id} shadow total")
        require_equal(
            bool_cell(row, "hidden_zero_superdimension_excluded"),
            total_dim > abs(signed),
            f"{degree_id} hidden-zero flag",
        )
        if signed == 0 and total_dim > 0:
            zero_signed_nonzero_total += 1
    return zero_signed_nonzero_total


def verify_relations(
    rows: list[dict[str, str]],
    source_count: int,
    profile_count: int,
    shadow_count: int,
    zero_signed_nonzero_total: int,
) -> None:
    relation_values = {
        "source_row_count": source_count,
        "pushforward_degree_count": profile_count,
        "signed_shadow_rows": shadow_count,
        "zero_signed_not_zero_object": zero_signed_nonzero_total,
        "parity_pushforward_preserves_blocks": 1,
        "source_parity_not_proved": 1,
        "gn_kac_parity_not_proved": 1,
    }
    seen: set[str] = set()
    for row in rows:
        check_row(row, "formal_relations.csv")
        relation_id = row["relation_id"]
        if relation_id in seen:
            raise ValueError(f"formal_relations.csv: duplicate relation_id {relation_id}")
        seen.add(relation_id)
        if relation_id not in REQUIRED_RELATIONS:
            raise ValueError(f"formal_relations.csv: unexpected relation_id {relation_id}")
        require_equal(int_cell(row, "computed_value"), relation_values[relation_id], f"{relation_id} computed")
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
        sources = verify_source_rows(tables["source_parity_rows.csv"])
        profiles = verify_pushforward_rows(tables["pushforward_parity_sums.csv"], sources)
        zero_signed_nonzero_total = verify_signed_shadow(tables["signed_shadow.csv"], profiles)
        verify_relations(
            tables["formal_relations.csv"],
            len(sources),
            len(profiles),
            len(tables["signed_shadow.csv"]),
            zero_signed_nonzero_total,
        )
        verify_firewall(tables["scalar_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"PARITY_PUSHFORWARD_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
