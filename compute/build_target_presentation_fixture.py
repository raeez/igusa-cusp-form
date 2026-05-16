#!/usr/bin/env python3
"""Build the A071 target-presentation fixture.

This is a target-only Delta_5 / Gritsenko--Nikulin / Kac reference
fixture.  It records currently justified target parity rows and the
signed-only rows that remain blocked.  It is not a compact source
verifier and it does not import source packets.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


HASH_FILE = "hashes.sha256"
HASHED_FILENAMES = (
    "manifest.yaml",
    "target_degrees.csv",
    "target_simple_generators.csv",
    "target_hall_lie_basis.csv",
    "target_relation_rows.csv",
    "target_pairing_blocks.csv",
    "target_radicals.csv",
    "target_dimensions.csv",
    "target_pbw.csv",
)
OUTPUT_FILENAMES = HASHED_FILENAMES + (HASH_FILE,)

ALLOWED_PARITY_SOURCES = {
    "gn_kac_base",
    "weyl_transport",
    "serre_zero",
    "target_presentation_computed",
    "signed_only_blocked",
}

GN_CITATION = "GN Sections 3--4, Proposition 3.1"
KAC_CITATION = "Kac 1990 real-root Weyl action, root strings, PBW"
BORCHERDS_CITATION = "Borcherds GKM presentation conventions"


DeltaDegree = tuple[int, int, int]


@dataclass(frozen=True)
class TargetRow:
    degree_id: str
    tex_label: str
    family: str
    beta: DeltaDegree
    smult: int
    fixture_status: str
    parity_source: str
    provenance_kind: str
    provenance_note: str
    citation: str
    relation_kind: str
    relation_input: str
    relation_output: str
    parity_effect: str
    chamber_rep: str
    weyl_word: str = ""
    full_even: int | None = None
    full_odd: int | None = None
    simple_even: int | None = None
    simple_odd: int | None = None
    signed_residual: int | None = None

    @property
    def gamma(self) -> DeltaDegree:
        c1, c2, c3 = self.beta
        return c1, c1 + c2 - c3, c2

    @property
    def height(self) -> int:
        return sum(self.beta)

    @property
    def norm(self) -> int:
        return delta_pair(self.beta, self.beta)

    @property
    def is_parity_fixture(self) -> bool:
        return self.full_even is not None and self.full_odd is not None

    @property
    def computation_hash(self) -> str:
        return stable_hash(
            self.degree_id,
            self.beta,
            self.gamma,
            self.norm,
            self.smult,
            self.full_even,
            self.full_odd,
            self.simple_even,
            self.simple_odd,
            self.signed_residual,
            self.fixture_status,
            self.parity_source,
            self.provenance_kind,
        )


def delta_pair(left: DeltaDegree, right: DeltaDegree) -> int:
    c1, c2, c3 = left
    d1, d2, d3 = right
    return (
        2 * c1 * d1
        + 2 * c2 * d2
        + 2 * c3 * d3
        - 2 * (c1 * d2 + c2 * d1)
        - 2 * (c1 * d3 + c3 * d1)
        - 2 * (c2 * d3 + c3 * d2)
    )


def stable_hash(*parts: Any) -> str:
    payload = "|".join("" if part is None else str(part) for part in parts)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return bool_text(value)
    return str(value)


def csv_content(fieldnames: tuple[str, ...], rows: list[dict[str, Any]]) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({field: cell(row.get(field)) for field in fieldnames})
    return buffer.getvalue()


def beta_with_entries(entries: dict[int, int]) -> DeltaDegree:
    return entries.get(1, 0), entries.get(2, 0), entries.get(3, 0)


def complement_pair(k: int) -> tuple[int, int]:
    pairs = {
        1: (2, 3),
        2: (1, 3),
        3: (1, 2),
    }
    return pairs[k]


def make_target_rows() -> list[TargetRow]:
    rows: list[TargetRow] = []

    for i, j in ((1, 2), (1, 3), (2, 3)):
        beta = beta_with_entries({i: 2, j: 2})
        rows.append(
            TargetRow(
                degree_id=f"2a_{i}{j}",
                tex_label=f"2a_{{{i}{j}}}",
                family="doubled_isotropic",
                beta=beta,
                smult=10,
                full_even=10,
                full_odd=0,
                simple_even=9,
                simple_odd=0,
                signed_residual=1,
                fixture_status="target_parity_fixture",
                parity_source="gn_kac_base",
                provenance_kind="gn_kac_affine_rank_two",
                provenance_note=(
                    "GN isotropic ray tau(2a_ij)=9 plus Kac A1^(1) "
                    "null-root residual 1"
                ),
                citation=f"{GN_CITATION}; {KAC_CITATION}; {BORCHERDS_CITATION}",
                relation_kind="rank_two_affine_null_plus_isotropic_simple",
                relation_input=f"delta_{i},delta_{j},a_{{{i}{j}}}",
                relation_output=f"2a_{{{i}{j}}}:10|0",
                parity_effect="even",
                chamber_rep=f"2a_{{{i}{j}}}",
            )
        )

    for k in (1, 2, 3):
        i, j = complement_pair(k)
        beta = beta_with_entries({i: 1, j: 1, k: 2})
        rows.append(
            TargetRow(
                degree_id=f"C_{k}_2",
                tex_label=f"C_{{{k},2}}",
                family="complementary_string_signed_only",
                beta=beta,
                smult=108,
                simple_even=90,
                simple_odd=0,
                signed_residual=18,
                fixture_status="signed_only_blocked",
                parity_source="signed_only_blocked",
                provenance_kind="signed_only",
                provenance_note=(
                    "signed target data smult=108 and m=90 only; full "
                    "parity split requires finite target presentation reducer"
                ),
                citation=f"{GN_CITATION}; {KAC_CITATION}",
                relation_kind="blocked_pending_finite_target_reducer",
                relation_input=f"a_{{{i}{j}}}+2delta_{k}",
                relation_output="no parity fixture",
                parity_effect="not_available",
                chamber_rep=f"C_{{{k},2}}",
            )
        )

    for k in (1, 2, 3):
        i, j = complement_pair(k)
        beta = beta_with_entries({i: 1, j: 1, k: 3})
        rows.append(
            TargetRow(
                degree_id=f"C_{k}_3",
                tex_label=f"C_{{{k},3}}",
                family="weyl_transport_delta123",
                beta=beta,
                smult=-64,
                full_even=29,
                full_odd=93,
                fixture_status="target_parity_fixture",
                parity_source="weyl_transport",
                provenance_kind="weyl_transport_from_delta123",
                provenance_note=(
                    "even real-root Weyl transport s_k(delta123)=C_{k,3}; "
                    "parity preserved from delta123:29|93"
                ),
                citation=f"{GN_CITATION}; {KAC_CITATION}",
                relation_kind="weyl_transport",
                relation_input="delta123:29|93",
                relation_output=f"C_{{{k},3}}:29|93",
                parity_effect="parity_preserving_even_real_reflection",
                chamber_rep="delta123",
                weyl_word=f"s_{k}",
            )
        )

    for k in (1, 2, 3):
        i, j = complement_pair(k)
        beta = beta_with_entries({i: 1, j: 1, k: 4})
        rows.append(
            TargetRow(
                degree_id=f"C_{k}_4",
                tex_label=f"C_{{{k},4}}",
                family="weyl_transport_isotropic",
                beta=beta,
                smult=10,
                full_even=10,
                full_odd=0,
                fixture_status="target_parity_fixture",
                parity_source="weyl_transport",
                provenance_kind="weyl_transport_from_a_ij",
                provenance_note=(
                    "even real-root Weyl transport s_k(a_ij)=C_{k,4}; "
                    "parity preserved from a_ij:10|0"
                ),
                citation=f"{GN_CITATION}; {KAC_CITATION}",
                relation_kind="weyl_transport",
                relation_input=f"a_{{{i}{j}}}:10|0",
                relation_output=f"C_{{{k},4}}:10|0",
                parity_effect="parity_preserving_even_real_reflection",
                chamber_rep=f"a_{{{i}{j}}}",
                weyl_word=f"s_{k}",
            )
        )

    rows.append(
        TargetRow(
            degree_id="2delta123",
            tex_label="2delta123",
            family="timelike_double_signed_only",
            beta=(2, 2, 2),
            smult=4016,
            simple_even=0,
            simple_odd=540,
            fixture_status="signed_only_blocked",
            parity_source="signed_only_blocked",
            provenance_kind="signed_only",
            provenance_note=(
                "signed target data smult=4016 and m=-540 only; full "
                "parity split requires finite target presentation reducer"
            ),
            citation=f"{GN_CITATION}; {KAC_CITATION}",
            relation_kind="blocked_pending_finite_target_reducer",
            relation_input="2delta123",
            relation_output="no parity fixture",
            parity_effect="not_available",
            chamber_rep="2delta123",
        )
    )

    for k in (1, 2, 3):
        i, j = complement_pair(k)
        beta = beta_with_entries({i: 1, j: 1, k: 5})
        rows.append(
            TargetRow(
                degree_id=f"C_{k}_5",
                tex_label=f"C_{{{k},5}}",
                family="complementary_string_terminal_zero",
                beta=beta,
                smult=0,
                full_even=0,
                full_odd=0,
                simple_even=0,
                simple_odd=0,
                signed_residual=0,
                fixture_status="target_parity_fixture",
                parity_source="serre_zero",
                provenance_kind="kac_root_string_terminal",
                provenance_note=(
                    "Kac real-root string through a_ij in the delta_k "
                    "direction terminates at C_{k,4}; C_{k,5} is zero"
                ),
                citation=f"{KAC_CITATION}; {GN_CITATION}",
                relation_kind="real_root_string_terminal_zero",
                relation_input=f"a_{{{i}{j}}}+5delta_{k}",
                relation_output=f"C_{{{k},5}}:0|0",
                parity_effect="terminal_zero",
                chamber_rep=f"C_{{{k},5}}",
            )
        )

    validate_rows(rows)
    return rows


def validate_rows(rows: list[TargetRow]) -> None:
    ids = [row.degree_id for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate target degree id")

    for row in rows:
        if row.parity_source not in ALLOWED_PARITY_SOURCES:
            raise ValueError(f"{row.degree_id}: bad parity_source")
        if row.is_parity_fixture:
            assert row.full_even is not None
            assert row.full_odd is not None
            if row.full_even - row.full_odd != row.smult:
                raise ValueError(f"{row.degree_id}: parity split mismatches smult")
            if row.fixture_status != "target_parity_fixture":
                raise ValueError(f"{row.degree_id}: active row has bad status")
        else:
            if row.fixture_status != "signed_only_blocked":
                raise ValueError(f"{row.degree_id}: blocked row has bad status")

    expected_blocked = {"C_1_2", "C_2_2", "C_3_2", "2delta123"}
    blocked = {row.degree_id for row in rows if not row.is_parity_fixture}
    if blocked != expected_blocked:
        raise ValueError(f"blocked rows mismatch: {sorted(blocked)}")

    expected_active = {
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
    active = {row.degree_id for row in rows if row.is_parity_fixture}
    if active != expected_active:
        raise ValueError(f"active rows mismatch: {sorted(active)}")


def degree_dict(row: TargetRow) -> dict[str, Any]:
    n, ell, m = row.gamma
    c1, c2, c3 = row.beta
    return {
        "degree_id": row.degree_id,
        "tex_label": row.tex_label,
        "family": row.family,
        "beta_c1": c1,
        "beta_c2": c2,
        "beta_c3": c3,
        "gamma_n": n,
        "gamma_l": ell,
        "gamma_m": m,
        "height": row.height,
        "norm": row.norm,
        "smult": row.smult,
        "is_parity_fixture": row.is_parity_fixture,
        "fixture_status": row.fixture_status,
        "parity_source": row.parity_source,
        "provenance_kind": row.provenance_kind,
        "provenance_note": row.provenance_note,
        "citation": row.citation,
        "chamber_rep": row.chamber_rep,
        "weyl_word": row.weyl_word,
        "computation_hash": row.computation_hash,
    }


def dimensions_dict(row: TargetRow) -> dict[str, Any]:
    return {
        "degree_id": row.degree_id,
        "tex_label": row.tex_label,
        "signed_dimension": row.smult,
        "full_even": row.full_even,
        "full_odd": row.full_odd,
        "simple_even": row.simple_even,
        "simple_odd": row.simple_odd,
        "signed_residual": row.signed_residual,
        "is_parity_fixture": row.is_parity_fixture,
        "dimension_status": (
            "target_parity_dimension"
            if row.is_parity_fixture
            else "signed_only_no_parity_split"
        ),
        "parity_source": row.parity_source,
        "provenance_kind": row.provenance_kind,
        "provenance_note": row.provenance_note,
        "citation": row.citation,
        "computation_hash": row.computation_hash,
    }


def simple_generator_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        if row.family == "doubled_isotropic":
            out.append(
                {
                    "degree_id": row.degree_id,
                    "tex_label": row.tex_label,
                    "generator_block": "gn_isotropic_simple_t2",
                    "parity": "even",
                    "count": 9,
                    "fixture_status": "target_simple_block",
                    "feeds_basis": True,
                    "parity_source": row.parity_source,
                    "provenance_kind": row.provenance_kind,
                    "provenance_note": row.provenance_note,
                    "citation": row.citation,
                    "computation_hash": row.computation_hash,
                }
            )
        elif row.family == "complementary_string_signed_only":
            out.append(
                {
                    "degree_id": row.degree_id,
                    "tex_label": row.tex_label,
                    "generator_block": "gn_timelike_simple_m_positive",
                    "parity": "even",
                    "count": 90,
                    "fixture_status": "signed_only_blocked",
                    "feeds_basis": False,
                    "parity_source": row.parity_source,
                    "provenance_kind": row.provenance_kind,
                    "provenance_note": row.provenance_note,
                    "citation": row.citation,
                    "computation_hash": row.computation_hash,
                }
            )
        elif row.degree_id == "2delta123":
            out.append(
                {
                    "degree_id": row.degree_id,
                    "tex_label": row.tex_label,
                    "generator_block": "gn_timelike_simple_m_negative",
                    "parity": "odd",
                    "count": 540,
                    "fixture_status": "signed_only_blocked",
                    "feeds_basis": False,
                    "parity_source": row.parity_source,
                    "provenance_kind": row.provenance_kind,
                    "provenance_note": row.provenance_note,
                    "citation": row.citation,
                    "computation_hash": row.computation_hash,
                }
            )
    return out


def basis_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        if not row.is_parity_fixture:
            continue
        assert row.full_even is not None
        assert row.full_odd is not None
        c1, c2, c3 = row.beta
        for parity, count in (("even", row.full_even), ("odd", row.full_odd)):
            for index in range(1, count + 1):
                basis_id = f"{row.degree_id}.{parity}.{index:03d}"
                out.append(
                    {
                        "basis_id": basis_id,
                        "degree_id": row.degree_id,
                        "tex_label": row.tex_label,
                        "beta_c1": c1,
                        "beta_c2": c2,
                        "beta_c3": c3,
                        "parity": parity,
                        "index_in_parity": index,
                        "basis_status": "target_reference_basis",
                        "parity_source": row.parity_source,
                        "provenance_kind": row.provenance_kind,
                        "provenance_note": row.provenance_note,
                        "computation_hash": stable_hash(
                            row.computation_hash, basis_id, parity, index
                        ),
                    }
                )
    return out


def relation_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        out.append(
            {
                "relation_id": f"rel.{row.degree_id}",
                "degree_id": row.degree_id,
                "tex_label": row.tex_label,
                "relation_kind": row.relation_kind,
                "relation_status": (
                    "recorded_target_relation"
                    if row.is_parity_fixture
                    else "blocked_no_relation_fixture"
                ),
                "relation_input": row.relation_input,
                "relation_output": row.relation_output,
                "parity_effect": row.parity_effect,
                "parity_source": row.parity_source,
                "provenance_kind": row.provenance_kind,
                "provenance_note": row.provenance_note,
                "citation": row.citation,
                "computation_hash": row.computation_hash,
            }
        )
    return out


def pairing_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        if row.is_parity_fixture:
            positive_even = row.full_even
            positive_odd = row.full_odd
            negative_even = row.full_even
            negative_odd = row.full_odd
            block_status = "target_negative_dual_formal_block"
        else:
            positive_even = positive_odd = negative_even = negative_odd = None
            block_status = "blocked_no_pairing_block"
        out.append(
            {
                "degree_id": row.degree_id,
                "tex_label": row.tex_label,
                "pairing_block_status": block_status,
                "positive_even": positive_even,
                "positive_odd": positive_odd,
                "negative_even": negative_even,
                "negative_odd": negative_odd,
                "source_pairing": False,
                "parity_source": row.parity_source,
                "provenance_kind": row.provenance_kind,
                "provenance_note": row.provenance_note,
                "citation": row.citation,
                "computation_hash": row.computation_hash,
            }
        )
    return out


def radical_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        if row.is_parity_fixture:
            radical_even = 0
            radical_odd = 0
            radical_status = "target_quotient_radical_zero"
        else:
            radical_even = None
            radical_odd = None
            radical_status = "blocked_no_radical_fixture"
        out.append(
            {
                "degree_id": row.degree_id,
                "tex_label": row.tex_label,
                "radical_status": radical_status,
                "radical_even": radical_even,
                "radical_odd": radical_odd,
                "source_radical": False,
                "parity_source": row.parity_source,
                "provenance_kind": row.provenance_kind,
                "provenance_note": row.provenance_note,
                "citation": row.citation,
                "computation_hash": row.computation_hash,
            }
        )
    return out


def pbw_rows(rows: list[TargetRow]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for row in rows:
        out.append(
            {
                "degree_id": row.degree_id,
                "tex_label": row.tex_label,
                "pbw_status": (
                    "target_reference_summary_no_source_pbw"
                    if row.is_parity_fixture
                    else "blocked_signed_only_no_pbw"
                ),
                "basis_vectors_even": row.full_even if row.is_parity_fixture else None,
                "basis_vectors_odd": row.full_odd if row.is_parity_fixture else None,
                "feeds_source_comparison": False,
                "parity_source": row.parity_source,
                "provenance_kind": row.provenance_kind,
                "provenance_note": row.provenance_note,
                "citation": row.citation,
                "computation_hash": row.computation_hash,
            }
        )
    return out


def manifest_content(rows: list[TargetRow]) -> str:
    active = [row for row in rows if row.is_parity_fixture]
    blocked = [row for row in rows if not row.is_parity_fixture]
    basis_count = sum(
        (row.full_even or 0) + (row.full_odd or 0)
        for row in active
    )
    simple_count = sum(
        count
        for row in rows
        for count in (
            row.simple_even if row.simple_even is not None else 0,
            row.simple_odd if row.simple_odd is not None else 0,
        )
    )
    lines = [
        "schema: a071_target_presentation_fixture",
        "target: delta5_gn_kac",
        "window: A071_Wle7_relation_closed_target_rows",
        "generator: compute/build_target_presentation_fixture.py",
        "deterministic: true",
        "target_only: true",
        "compact_source_firewall:",
        "  imports_compact_source_packets: false",
        "  provides_compact_source_verification: false",
        "  feeds_compact_source_comparison: false",
        "scope:",
        "  active_target_parity_rows: " + str(len(active)),
        "  signed_only_blocked_rows: " + str(len(blocked)),
        "  target_basis_vectors: " + str(basis_count),
        "  simple_generator_entries_total_count: " + str(simple_count),
        "active_rows:",
        "  doubled_isotropic: 2a_ij:10|0",
        "  complementary_weyl_delta123: C_{k,3}:29|93",
        "  complementary_weyl_isotropic: C_{k,4}:10|0",
        "  complementary_terminal_zero: C_{k,5}:0|0",
        "blocked_rows:",
        "  C_{k,2}: signed_only_blocked",
        "  2delta123: signed_only_blocked",
        "provenance_sources:",
        "  gn_kac_base: GN/Kac target presentation arithmetic",
        "  weyl_transport: parity-preserving even real-root Weyl transport",
        "  serre_zero: Kac real-root string terminal zero",
        "  signed_only_blocked: signed Delta_5/GN data only, no parity fixture",
        "citations:",
        "  - " + GN_CITATION,
        "  - " + KAC_CITATION,
        "  - " + BORCHERDS_CITATION,
        "limitations:",
        "  - no compact Hall representatives",
        "  - no compact source pairings",
        "  - no compact source radicals",
        "  - no source PBW or no-extra theorem",
        "  - C_{k,2} and 2delta123 do not feed target basis or PBW rows",
        "files:",
    ]
    lines.extend(f"  - {filename}" for filename in OUTPUT_FILENAMES)
    return "\n".join(lines) + "\n"


def build_fixture_contents() -> dict[str, str]:
    rows = make_target_rows()
    contents: dict[str, str] = {}
    contents["manifest.yaml"] = manifest_content(rows)
    contents["target_degrees.csv"] = csv_content(
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
            "smult",
            "is_parity_fixture",
            "fixture_status",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "chamber_rep",
            "weyl_word",
            "computation_hash",
        ),
        [degree_dict(row) for row in rows],
    )
    contents["target_simple_generators.csv"] = csv_content(
        (
            "degree_id",
            "tex_label",
            "generator_block",
            "parity",
            "count",
            "fixture_status",
            "feeds_basis",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        simple_generator_rows(rows),
    )
    contents["target_hall_lie_basis.csv"] = csv_content(
        (
            "basis_id",
            "degree_id",
            "tex_label",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "parity",
            "index_in_parity",
            "basis_status",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "computation_hash",
        ),
        basis_rows(rows),
    )
    contents["target_relation_rows.csv"] = csv_content(
        (
            "relation_id",
            "degree_id",
            "tex_label",
            "relation_kind",
            "relation_status",
            "relation_input",
            "relation_output",
            "parity_effect",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        relation_rows(rows),
    )
    contents["target_pairing_blocks.csv"] = csv_content(
        (
            "degree_id",
            "tex_label",
            "pairing_block_status",
            "positive_even",
            "positive_odd",
            "negative_even",
            "negative_odd",
            "source_pairing",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        pairing_rows(rows),
    )
    contents["target_radicals.csv"] = csv_content(
        (
            "degree_id",
            "tex_label",
            "radical_status",
            "radical_even",
            "radical_odd",
            "source_radical",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        radical_rows(rows),
    )
    contents["target_dimensions.csv"] = csv_content(
        (
            "degree_id",
            "tex_label",
            "signed_dimension",
            "full_even",
            "full_odd",
            "simple_even",
            "simple_odd",
            "signed_residual",
            "is_parity_fixture",
            "dimension_status",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        [dimensions_dict(row) for row in rows],
    )
    contents["target_pbw.csv"] = csv_content(
        (
            "degree_id",
            "tex_label",
            "pbw_status",
            "basis_vectors_even",
            "basis_vectors_odd",
            "feeds_source_comparison",
            "parity_source",
            "provenance_kind",
            "provenance_note",
            "citation",
            "computation_hash",
        ),
        pbw_rows(rows),
    )
    contents[HASH_FILE] = hashes_content(contents)
    return contents


def hashes_content(contents: dict[str, str]) -> str:
    lines = []
    for filename in HASHED_FILENAMES:
        lines.append(f"{sha256_text(contents[filename])}  {filename}")
    return "\n".join(lines) + "\n"


def write_fixture(out_dir: Path, force: bool) -> None:
    contents = build_fixture_contents()
    existing = [filename for filename in OUTPUT_FILENAMES if (out_dir / filename).exists()]
    if existing and not force:
        joined = ", ".join(existing)
        raise RuntimeError(f"refusing to overwrite existing fixture files: {joined}")

    out_dir.mkdir(parents=True, exist_ok=True)
    for filename in OUTPUT_FILENAMES:
        path = out_dir / filename
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(contents[filename])
    print(f"wrote {len(OUTPUT_FILENAMES)} fixture files to {out_dir}")


def parse_hashes(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line_number, raw_line in enumerate(text.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2:
            raise ValueError(f"bad hash line {line_number}: {raw_line!r}")
        digest, filename = parts
        entries[filename.strip()] = digest
    return entries


def check_hashes(out_dir: Path) -> list[str]:
    errors: list[str] = []
    hash_path = out_dir / HASH_FILE
    if not hash_path.exists():
        return [f"missing {HASH_FILE}"]
    try:
        entries = parse_hashes(hash_path.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [str(exc)]

    expected_names = set(HASHED_FILENAMES)
    actual_names = set(entries)
    if actual_names != expected_names:
        errors.append(
            "hash manifest entries mismatch: "
            f"expected {sorted(expected_names)}, got {sorted(actual_names)}"
        )

    for filename, expected_digest in entries.items():
        path = out_dir / filename
        if not path.exists():
            errors.append(f"hash target missing: {filename}")
            continue
        actual_digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_digest != expected_digest:
            errors.append(
                f"hash mismatch {filename}: {actual_digest} != {expected_digest}"
            )
    return errors


def check_fixture(out_dir: Path) -> None:
    expected = build_fixture_contents()
    errors: list[str] = []
    for filename in OUTPUT_FILENAMES:
        path = out_dir / filename
        if not path.exists():
            errors.append(f"missing {filename}")
            continue
        actual = path.read_text(encoding="utf-8")
        if actual != expected[filename]:
            errors.append(f"content mismatch {filename}")
    errors.extend(check_hashes(out_dir))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        raise RuntimeError("fixture check failed")

    print(f"fixture check passed: {len(OUTPUT_FILENAMES)} files")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build or check the target-only A071 presentation fixture."
    )
    parser.add_argument(
        "--out",
        required=True,
        type=Path,
        help="Output directory for the target presentation fixture.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated fixture files.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check the fixture without writing files.",
    )
    args = parser.parse_args(argv)
    if args.force and args.check:
        parser.error("--force and --check are mutually exclusive")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        if args.check:
            check_fixture(args.out)
        else:
            write_fixture(args.out, args.force)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
