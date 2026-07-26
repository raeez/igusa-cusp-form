#!/usr/bin/env python3
"""Target-degree closure gate for the first target relation window.

This verifier checks the finite target degree set

    W_rel^+ = W_{<=3}^{act} union R_4 union I_4 union C_{<=7}
              union {2 delta_123}

as a degree-closure certificate.  It verifies the 35 expected degrees,
their delta-basis and (n,l,m) coordinates, signed Jacobi coefficients,
terminal real-Serre rows, complementary-string terminal rows, and the
boundary between target parity rows and signed-only rows.  It also
audits downward saturation: the audit records the three nonzero proper
subdegree defects under 2 delta_123.  After adjoining those defects it
audits the post-saturation real-string terminal layer, its 114
subdegree-defect incidences, and the 26-row saturation extension that
closes downward saturation for the displayed terminal layer.  It then
audits the real-root strings conditionally forced by those 26 rows and
records that the resulting 85-row set is not relation-closed.  The next
terminal layer, if adjoined, creates 546 nonzero proper-subdegree defect
incidences across 98 distinct subdegrees; adjoining those 98 rows gives
a 237-row target degree set with no remaining nonzero proper-subdegree
defect for that layer.  The real-root strings through the 98 rows then
force 206 terminal checks and another 624-incidence saturation defect
across 50 distinct subdegrees.  Adjoining those 206 terminals and 50
subdegrees gives a 469-row target degree set with no remaining nonzero
proper-subdegree defect for that layer.  The real-root strings through
the 50 rows then force 96 terminal checks and a 44-incidence saturation
defect across 12 distinct subdegrees; adjoining those rows gives a
571-row target degree set with no remaining nonzero proper-subdegree
defect for that layer.  The real-root strings through the 12 rows then
force 20 zero terminal checks and an 8-incidence saturation defect
across 6 distinct subdegrees; adjoining those rows gives a 597-row
    target degree set with no remaining nonzero proper-subdegree defect for
    that layer.  The real-root strings through the 6 rows then force 10
    zero terminal checks and an 18-incidence saturation defect across 6
    distinct subdegrees; adjoining those rows gives a 613-row target degree
    set with no remaining nonzero proper-subdegree defect for that layer.
    The real-root strings through the next 6 rows then force 10 zero
    terminal checks and an 8-incidence saturation defect across 6 distinct
    subdegrees; adjoining those rows gives a 629-row target degree set with
    no remaining nonzero proper-subdegree defect for that layer.  The
    real-root strings through the next 6 rows then force 10 zero terminal
    checks and an 18-incidence saturation defect across 6 distinct
    subdegrees; adjoining those rows gives a 645-row target degree set with
    no remaining nonzero proper-subdegree defect for that layer.

It does not construct compact source representatives, Hall brackets,
source pairings, radicals, PBW comparison, or primitive recognition.
"""

from __future__ import annotations

import argparse
import csv
import inspect
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


COMPUTE_DIR = Path(__file__).resolve().parent
if str(COMPUTE_DIR) not in sys.path:
    sys.path.insert(0, str(COMPUTE_DIR))

from verify_square_root import (
    additive_m_coefficient,
    delta_basis_to_gamma,
    delta_pair,
    phi_01_coefficients,
    real_string_exponent,
    signed_root_supermultiplicity,
)


_uncached_additive_m_coefficient = additive_m_coefficient
_uncached_phi_01_coefficients = phi_01_coefficients
_uncached_signed_root_supermultiplicity = signed_root_supermultiplicity
_additive_m_cache: dict[tuple[int, tuple[int, int, int]], int] = {}
_phi_01_cache: dict[str, dict] = {}
_proper_subdegree_cache: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
_signed_multiplicity_cache: dict[tuple[int, tuple[int, int, int]], int] = {}


def phi_01_coefficients() -> dict:
    if "phi_01" not in _phi_01_cache:
        _phi_01_cache["phi_01"] = _uncached_phi_01_coefficients()
    return _phi_01_cache["phi_01"]


def additive_m_coefficient(phi: dict, beta: tuple[int, int, int]) -> int:
    key = (id(phi), beta)
    if key not in _additive_m_cache:
        _additive_m_cache[key] = _uncached_additive_m_coefficient(phi, beta)
    return _additive_m_cache[key]


def signed_root_supermultiplicity(phi: dict, beta: tuple[int, int, int]) -> int:
    key = (id(phi), beta)
    if key not in _signed_multiplicity_cache:
        _signed_multiplicity_cache[key] = _uncached_signed_root_supermultiplicity(phi, beta)
    return _signed_multiplicity_cache[key]


SUCCESS_STATUS = "WREL_DEGREE_CLOSURE_VERIFIED"
DEFAULT_FIXTURE = Path("certificates/targets/delta5_gn_kac/wrel_degree_closure")
WLE3_FIXTURE = Path("certificates/targets/delta5_gn_kac/wle3_target_parity")
A071_FIXTURE = Path("certificates/targets/delta5_gn_kac/a071_target_presentation")
EXPECTED_KIND = "wrel_target_degree_closure_candidate"
REQUIRED_FIREWALL_ROWS = frozenset(
    {
        "compact_source_representatives",
        "source_relation_matrices",
        "source_pairing_radical",
        "source_pbw",
        "primitive_recognition",
    }
)


@dataclass(frozen=True)
class ExpectedDegree:
    degree_id: str
    tex_label: str
    family: str
    beta: tuple[int, int, int]
    target_status: str
    parity_packet_id: str
    closure_source: str
    proof_reference: str


@dataclass(frozen=True)
class TableSpec:
    path: str
    columns: tuple[str, ...]


TABLE_SPECS: tuple[TableSpec, ...] = (
    TableSpec(
        "target_window_rows.csv",
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
            "target_status",
            "parity_packet_id",
            "closure_source",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "closure_generators.csv",
        (
            "component_id",
            "definition",
            "expected_count",
            "actual_count",
            "max_height",
            "closure_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_relation_checks.csv",
        (
            "check_id",
            "terminal_kind",
            "real_root_id",
            "other_root_id",
            "terminal_degree_id",
            "pairing",
            "serre_exponent",
            "expected_exponent",
            "terminal_signed_dimension",
            "terminal_residual",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "downward_saturation.csv",
        (
            "parent_degree_id",
            "total_proper_subdegrees",
            "nonzero_proper_subdegrees",
            "wrel_proper_subdegrees",
            "missing_nonzero_subdegrees",
            "missing_nonzero_subdegree_ids",
            "missing_nonzero_signed_dimensions",
            "coverage_defect_rank",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "saturation_extension.csv",
        (
            "degree_id",
            "tex_label",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "additive_m",
            "target_status",
            "target_packet_id",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "post_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "simple_degree_id",
            "simple_beta_c1",
            "simple_beta_c2",
            "simple_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_wsat",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "post_saturation_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "additive_m",
            "terminal_in_wsat",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "additive_m",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_additive_m",
            "terminal_in_w85",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_w85_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer.csv",
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
            "signed_dimension",
            "additive_m",
            "parent_terminal_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "defect_degree_id",
            "defect_beta_c1",
            "defect_beta_c2",
            "defect_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_additive_m",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "additive_m",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "additive_m",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "twelve_row_saturation_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "twelve_row_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "twelve_row_saturation_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "twelve_row_saturation_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "six_row_saturation_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "six_row_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "six_row_saturation_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "six_row_saturation_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "second_six_row_saturation_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "second_six_row_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "second_six_row_saturation_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "second_six_row_saturation_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "third_six_row_saturation_real_string_summary.csv",
        (
            "summary_id",
            "base_degree_count",
            "generator_degree_count",
            "terminal_check_count",
            "distinct_terminal_degree_count",
            "terminal_degree_in_base_count",
            "new_terminal_degree_count",
            "nonzero_terminal_degree_count",
            "missing_nonzero_terminal_degree_count",
            "saturation_defect_parent_terminal_count",
            "saturation_defect_occurrence_count",
            "saturation_defect_distinct_degree_count",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "third_six_row_saturation_real_string_obligations.csv",
        (
            "check_id",
            "real_root_id",
            "extension_degree_id",
            "extension_beta_c1",
            "extension_beta_c2",
            "extension_beta_c3",
            "pairing",
            "serre_exponent",
            "terminal_beta_c1",
            "terminal_beta_c2",
            "terminal_beta_c3",
            "terminal_gamma_n",
            "terminal_gamma_l",
            "terminal_gamma_m",
            "terminal_height",
            "terminal_norm",
            "terminal_signed_dimension",
            "terminal_in_base",
            "relation_payload_status",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "third_six_row_saturation_real_string_terminal_layer.csv",
        (
            "terminal_degree_id",
            "source_check_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "terminal_in_base",
            "source_obligation_count",
            "missing_nonzero_subdegree_count",
            "missing_nonzero_subdegree_ids",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "third_six_row_saturation_real_string_saturation_extension.csv",
        (
            "degree_id",
            "parent_terminal_degree_ids",
            "beta_c1",
            "beta_c2",
            "beta_c3",
            "gamma_n",
            "gamma_l",
            "gamma_m",
            "height",
            "norm",
            "signed_dimension",
            "parent_terminal_count",
            "defect_occurrence_count",
            "coverage_role",
            "proof_reference",
            "check_status",
            "notes",
        ),
    ),
    TableSpec(
        "source_firewall.csv",
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


def complement_pair(k: int) -> tuple[int, int]:
    return {1: (2, 3), 2: (1, 3), 3: (1, 2)}[k]


def beta_with(entries: dict[int, int]) -> tuple[int, int, int]:
    return tuple(entries.get(i, 0) for i in (1, 2, 3))


def expected_degrees() -> dict[str, ExpectedDegree]:
    rows: list[ExpectedDegree] = []
    for i in (1, 2, 3):
        rows.append(ExpectedDegree(
            f"delta_{i}", f"delta_{i}", "wle3_real_simple",
            beta_with({i: 1}), "target_parity_verified",
            "wle3_target_parity", "W_le3_act",
            "wle3_target_parity target_degrees.csv",
        ))
    for i, j in ((1, 2), (1, 3), (2, 3)):
        rows.append(ExpectedDegree(
            f"a_{i}{j}", f"a_{{{i}{j}}}", "wle3_isotropic",
            beta_with({i: 1, j: 1}), "target_parity_verified",
            "wle3_target_parity", "W_le3_act",
            "wle3_target_parity target_degrees.csv",
        ))
    for i, j in ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)):
        rows.append(ExpectedDegree(
            f"2delta_{i}_delta_{j}", f"2delta_{i}+delta_{j}",
            "wle3_real_string", beta_with({i: 2, j: 1}),
            "target_parity_verified", "wle3_target_parity",
            "W_le3_act", "wle3_target_parity real_string_checks.csv",
        ))
    rows.append(ExpectedDegree(
        "delta123", "delta_{123}", "wle3_first_timelike",
        (1, 1, 1), "target_parity_verified", "wle3_target_parity",
        "W_le3_act", "wle3_target_parity decomposition.csv",
    ))
    for i, j in ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)):
        rows.append(ExpectedDegree(
            f"3delta_{i}_delta_{j}", f"3delta_{i}+delta_{j}",
            "real_serre_terminal", beta_with({i: 3, j: 1}),
            "terminal_zero_no_target_basis", "serre_terminal",
            "R4_real_serre_terminal", "Kac real-Serre exponent 3",
        ))
    for i, j in ((1, 2), (1, 3), (2, 3)):
        rows.append(ExpectedDegree(
            f"2a_{i}{j}", f"2a_{{{i}{j}}}", "doubled_isotropic",
            beta_with({i: 2, j: 2}), "target_parity_verified",
            "a071_target_presentation", "I4_doubled_isotropic",
            "A071 target_degrees.csv",
        ))
    for k in (1, 2, 3):
        i, j = complement_pair(k)
        for s in (2, 3, 4, 5):
            status = "target_parity_verified"
            if s == 2:
                status = "signed_only_blocked"
            rows.append(ExpectedDegree(
                f"C_{k}_{s}", f"C_{{{k},{s}}}", f"complementary_string_s{s}",
                beta_with({i: 1, j: 1, k: s}), status,
                "a071_target_presentation", "C_le7_complementary_string",
                "A071 target_degrees.csv",
            ))
    rows.append(ExpectedDegree(
        "2delta123", "2delta123", "double_timelike",
        (2, 2, 2), "signed_only_blocked", "a071_target_presentation",
        "double_delta123", "A071 target_degrees.csv",
    ))
    out = {row.degree_id: row for row in rows}
    if len(out) != 35:
        raise AssertionError(f"expected 35 rows, got {len(out)}")
    return out


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--wle3-fixture", type=Path, default=WLE3_FIXTURE)
    parser.add_argument("--a071-fixture", type=Path, default=A071_FIXTURE)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


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


def read_manifest(fixture: Path) -> dict:
    path = fixture / "manifest.json"
    if not path.exists():
        raise ValueError(f"missing manifest: {path}")
    readme = fixture / "README.md"
    if not readme.exists() or not readme.read_text(encoding="utf-8").strip():
        raise ValueError(f"missing nonempty README: {readme}")
    return json.loads(path.read_text(encoding="utf-8"))


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
    require_equal(row["check_status"], "verified", f"{table_name} check_status")
    if not row["proof_reference"].strip():
        raise ValueError(f"{table_name}: missing proof_reference in {row}")


def verify_manifest(manifest: dict) -> None:
    require_equal(manifest.get("target_kind"), EXPECTED_KIND, "manifest target_kind")
    require_equal(manifest.get("certified"), True, "manifest certified")
    require_equal(manifest.get("target_only"), True, "manifest target_only")
    require_equal(manifest.get("compact_source"), False, "manifest compact_source")
    require_equal(manifest.get("primitive_recognition"), False, "manifest primitive_recognition")
    require_equal(manifest.get("degree_count"), 35, "manifest degree_count")
    require_equal(manifest.get("downward_saturated"), False, "manifest downward_saturated")
    require_equal(manifest.get("saturation_defect_rank"), 3, "manifest saturation_defect_rank")
    require_equal(
        manifest.get("saturated_extension_degree_count"),
        38,
        "manifest saturated_extension_degree_count",
    )
    require_equal(
        manifest.get("saturated_extension_defect_rank"),
        0,
        "manifest saturated_extension_defect_rank",
    )
    require_equal(
        manifest.get("saturated_extension_relation_closed"),
        False,
        "manifest saturated_extension_relation_closed",
    )
    require_equal(
        manifest.get("post_saturation_real_string_obligation_count"),
        21,
        "manifest post_saturation_real_string_obligation_count",
    )
    require_equal(
        manifest.get("post_saturation_missing_terminal_count"),
        21,
        "manifest post_saturation_missing_terminal_count",
    )
    require_equal(
        manifest.get("post_saturation_nonzero_terminal_count"),
        10,
        "manifest post_saturation_nonzero_terminal_count",
    )
    require_equal(
        manifest.get("post_saturation_terminal_layer_degree_count"),
        21,
        "manifest post_saturation_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_defect_occurrence_count"),
        114,
        "manifest terminal_layer_saturation_defect_occurrence_count",
    )
    require_equal(
        manifest.get("terminal_layer_distinct_saturation_defect_count"),
        26,
        "manifest terminal_layer_distinct_saturation_defect_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_extension_degree_count"),
        26,
        "manifest terminal_layer_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturated_total_degree_count"),
        85,
        "manifest terminal_layer_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_extension_defect_rank"),
        0,
        "manifest terminal_layer_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_obligation_count"),
        55,
        "manifest terminal_layer_saturation_real_string_obligation_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_missing_terminal_count"),
        54,
        "manifest terminal_layer_saturation_real_string_missing_terminal_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_nonzero_terminal_count"),
        13,
        "manifest terminal_layer_saturation_real_string_nonzero_terminal_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_missing_nonzero_terminal_count"),
        12,
        "manifest terminal_layer_saturation_real_string_missing_nonzero_terminal_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_distinct_terminal_degree_count"),
        55,
        "manifest terminal_layer_saturation_real_string_distinct_terminal_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_new_terminal_degree_count"),
        54,
        "manifest terminal_layer_saturation_real_string_new_terminal_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_parent_count"),
        36,
        "manifest terminal_layer_saturation_real_string_defect_parent_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_occurrence_count"),
        546,
        "manifest terminal_layer_saturation_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_distinct_defect_count"),
        98,
        "manifest terminal_layer_saturation_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_degree_count"),
        98,
        "manifest terminal_layer_saturation_real_string_defect_layer_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_saturated_total_degree_count"),
        237,
        "manifest terminal_layer_saturation_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_defect_rank"),
        0,
        "manifest terminal_layer_saturation_real_string_defect_layer_defect_rank",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_check_count"),
        206,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_check_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_new_terminal_count"),
        182,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_missing_nonzero_count"),
        24,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_defect_occurrence_count"),
        624,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_distinct_defect_count"),
        50,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_degree_count"),
        206,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_in_base_count"),
        24,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_nonzero_count"),
        48,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_degree_count"),
        50,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturated_total_degree_count"),
        469,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_defect_rank"),
        0,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_check_count"),
        96,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_check_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_new_terminal_count"),
        90,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_missing_nonzero_count"),
        0,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_defect_occurrence_count"),
        44,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_distinct_defect_count"),
        12,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_degree_count"),
        96,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_in_base_count"),
        6,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_nonzero_count"),
        6,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_degree_count"),
        12,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturated_total_degree_count"),
        571,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_defect_rank"),
        0,
        "manifest terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_check_count"),
        20,
        "manifest twelve_row_saturation_real_string_check_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_new_terminal_count"),
        20,
        "manifest twelve_row_saturation_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_missing_nonzero_count"),
        0,
        "manifest twelve_row_saturation_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_defect_occurrence_count"),
        8,
        "manifest twelve_row_saturation_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_distinct_defect_count"),
        6,
        "manifest twelve_row_saturation_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_terminal_layer_degree_count"),
        20,
        "manifest twelve_row_saturation_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_terminal_layer_in_base_count"),
        0,
        "manifest twelve_row_saturation_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_terminal_layer_nonzero_count"),
        0,
        "manifest twelve_row_saturation_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_saturation_extension_degree_count"),
        6,
        "manifest twelve_row_saturation_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_saturated_total_degree_count"),
        597,
        "manifest twelve_row_saturation_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("twelve_row_saturation_real_string_saturation_extension_defect_rank"),
        0,
        "manifest twelve_row_saturation_real_string_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_check_count"),
        10,
        "manifest six_row_saturation_real_string_check_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_new_terminal_count"),
        10,
        "manifest six_row_saturation_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_missing_nonzero_count"),
        0,
        "manifest six_row_saturation_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_defect_occurrence_count"),
        18,
        "manifest six_row_saturation_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_distinct_defect_count"),
        6,
        "manifest six_row_saturation_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_terminal_layer_degree_count"),
        10,
        "manifest six_row_saturation_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_terminal_layer_in_base_count"),
        0,
        "manifest six_row_saturation_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_terminal_layer_nonzero_count"),
        0,
        "manifest six_row_saturation_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_saturation_extension_degree_count"),
        6,
        "manifest six_row_saturation_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_saturated_total_degree_count"),
        613,
        "manifest six_row_saturation_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("six_row_saturation_real_string_saturation_extension_defect_rank"),
        0,
        "manifest six_row_saturation_real_string_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_check_count"),
        10,
        "manifest second_six_row_saturation_real_string_check_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_new_terminal_count"),
        10,
        "manifest second_six_row_saturation_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_missing_nonzero_count"),
        0,
        "manifest second_six_row_saturation_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_defect_occurrence_count"),
        8,
        "manifest second_six_row_saturation_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_distinct_defect_count"),
        6,
        "manifest second_six_row_saturation_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_terminal_layer_degree_count"),
        10,
        "manifest second_six_row_saturation_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_terminal_layer_in_base_count"),
        0,
        "manifest second_six_row_saturation_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_terminal_layer_nonzero_count"),
        0,
        "manifest second_six_row_saturation_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_saturation_extension_degree_count"),
        6,
        "manifest second_six_row_saturation_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_saturated_total_degree_count"),
        629,
        "manifest second_six_row_saturation_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("second_six_row_saturation_real_string_saturation_extension_defect_rank"),
        0,
        "manifest second_six_row_saturation_real_string_saturation_extension_defect_rank",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_check_count"),
        10,
        "manifest third_six_row_saturation_real_string_check_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_new_terminal_count"),
        10,
        "manifest third_six_row_saturation_real_string_new_terminal_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_missing_nonzero_count"),
        0,
        "manifest third_six_row_saturation_real_string_missing_nonzero_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_defect_occurrence_count"),
        18,
        "manifest third_six_row_saturation_real_string_defect_occurrence_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_distinct_defect_count"),
        6,
        "manifest third_six_row_saturation_real_string_distinct_defect_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_terminal_layer_degree_count"),
        10,
        "manifest third_six_row_saturation_real_string_terminal_layer_degree_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_terminal_layer_in_base_count"),
        0,
        "manifest third_six_row_saturation_real_string_terminal_layer_in_base_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_terminal_layer_nonzero_count"),
        0,
        "manifest third_six_row_saturation_real_string_terminal_layer_nonzero_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_saturation_extension_degree_count"),
        6,
        "manifest third_six_row_saturation_real_string_saturation_extension_degree_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_saturated_total_degree_count"),
        645,
        "manifest third_six_row_saturation_real_string_saturated_total_degree_count",
    )
    require_equal(
        manifest.get("third_six_row_saturation_real_string_saturation_extension_defect_rank"),
        0,
        "manifest third_six_row_saturation_real_string_saturation_extension_defect_rank",
    )


def read_external_degree_ids(wle3_fixture: Path, a071_fixture: Path) -> tuple[set[str], set[str]]:
    wle3 = rows_by_id(read_table(wle3_fixture, TableSpec("target_degrees.csv", (
        "degree_id", "tex_label", "family", "beta_c1", "beta_c2", "beta_c3",
        "gamma_n", "gamma_l", "gamma_m", "height", "norm", "signed_dimension",
        "full_even", "full_odd", "parity_status", "parity_source",
        "source_formula_id", "proof_reference", "check_status", "notes",
    ))), "degree_id")
    a071 = rows_by_id(read_table(a071_fixture, TableSpec("target_degrees.csv", (
        "degree_id", "tex_label", "family", "beta_c1", "beta_c2", "beta_c3",
        "gamma_n", "gamma_l", "gamma_m", "height", "norm", "smult",
        "is_parity_fixture", "fixture_status", "parity_source",
        "provenance_kind", "provenance_note", "citation", "chamber_rep",
        "weyl_word", "computation_hash",
    ))), "degree_id")
    return set(wle3), set(a071)


def verify_window_rows(
    rows: dict[str, dict[str, str]],
    expected: dict[str, ExpectedDegree],
    wle3_ids: set[str],
    a071_ids: set[str],
) -> None:
    require_equal(set(rows), set(expected), "W_rel degree coverage")
    phi = phi_01_coefficients()
    for degree_id, row in rows.items():
        check_verified(row, "target_window_rows.csv")
        exp = expected[degree_id]
        require_equal(row["tex_label"], exp.tex_label, f"{degree_id} tex_label")
        require_equal(row["family"], exp.family, f"{degree_id} family")
        require_equal(beta(row), exp.beta, f"{degree_id} beta")
        gamma = delta_basis_to_gamma(exp.beta)
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma_n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma_l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma_m")
        require_equal(int_cell(row, "height"), sum(exp.beta), f"{degree_id} height")
        require_equal(int_cell(row, "norm"), delta_pair(exp.beta, exp.beta), f"{degree_id} norm")
        signed = signed_root_supermultiplicity(phi, exp.beta)
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(row["target_status"], exp.target_status, f"{degree_id} target_status")
        require_equal(row["parity_packet_id"], exp.parity_packet_id, f"{degree_id} parity packet")
        require_equal(row["closure_source"], exp.closure_source, f"{degree_id} closure_source")
        if exp.parity_packet_id == "wle3_target_parity":
            if degree_id not in wle3_ids:
                raise ValueError(f"{degree_id}: absent from W<=3 fixture")
        if exp.parity_packet_id == "a071_target_presentation":
            if degree_id not in a071_ids:
                raise ValueError(f"{degree_id}: absent from A071 fixture")
        if exp.target_status == "terminal_zero_no_target_basis":
            require_equal(signed, 0, f"{degree_id} terminal signed zero")


def verify_closure_generators(rows: list[dict[str, str]], window_rows: dict[str, dict[str, str]]) -> None:
    counts = Counter(row["closure_source"] for row in window_rows.values())
    heights: dict[str, int] = {}
    for row in window_rows.values():
        source = row["closure_source"]
        heights[source] = max(heights.get(source, 0), int_cell(row, "height"))
    expected_counts = {
        "W_le3_act": 13,
        "R4_real_serre_terminal": 6,
        "I4_doubled_isotropic": 3,
        "C_le7_complementary_string": 12,
        "double_delta123": 1,
    }
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "closure_generators.csv")
        component = row["component_id"]
        seen.add(component)
        require_equal(int_cell(row, "expected_count"), expected_counts[component], f"{component} expected_count")
        require_equal(int_cell(row, "actual_count"), counts[component], f"{component} actual_count")
        require_equal(int_cell(row, "max_height"), heights[component], f"{component} max_height")
    require_equal(seen, set(expected_counts), "closure component coverage")


def root_by_name(name: str) -> tuple[int, int, int]:
    if name.startswith("delta_"):
        i = int(name.split("_")[1])
        return beta_with({i: 1})
    if name.startswith("a_"):
        _, pair = name.split("_")
        i, j = int(pair[0]), int(pair[1])
        return beta_with({i: 1, j: 1})
    raise ValueError(f"unknown root name: {name}")


def verify_terminal_relations(rows: list[dict[str, str]], window_rows: dict[str, dict[str, str]]) -> None:
    expected_ids = {
        "rr_12", "rr_13", "rr_21", "rr_23", "rr_31", "rr_32",
        "ci_1", "ci_2", "ci_3",
    }
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "terminal_relation_checks.csv")
        check_id = row["check_id"]
        seen.add(check_id)
        real = root_by_name(row["real_root_id"])
        other = root_by_name(row["other_root_id"])
        pairing = delta_pair(real, other)
        exponent = real_string_exponent(real, other)
        terminal_id = row["terminal_degree_id"]
        terminal = window_rows[terminal_id]
        require_equal(int_cell(row, "pairing"), pairing, f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), exponent, f"{check_id} exponent")
        require_equal(int_cell(row, "expected_exponent"), exponent, f"{check_id} expected exponent")
        require_equal(int_cell(row, "terminal_signed_dimension"), int_cell(terminal, "signed_dimension"), f"{check_id} terminal signed")
        require_equal(int_cell(row, "terminal_residual"), int_cell(terminal, "signed_dimension"), f"{check_id} terminal residual")
        require_equal(int_cell(row, "terminal_residual"), 0, f"{check_id} terminal zero")
    require_equal(seen, expected_ids, "terminal relation coverage")


def proper_subdegrees(beta_value: tuple[int, int, int]) -> list[tuple[int, int, int]]:
    if beta_value in _proper_subdegree_cache:
        return _proper_subdegree_cache[beta_value]
    rows: list[tuple[int, int, int]] = []
    for c1 in range(beta_value[0] + 1):
        for c2 in range(beta_value[1] + 1):
            for c3 in range(beta_value[2] + 1):
                subdegree = (c1, c2, c3)
                if subdegree == (0, 0, 0) or subdegree == beta_value:
                    continue
                rows.append(subdegree)
    _proper_subdegree_cache[beta_value] = rows
    return rows


def saturation_defect_id(beta_value: tuple[int, int, int]) -> str:
    if sorted(beta_value) == [1, 2, 2]:
        singleton_index = beta_value.index(1) + 1
        return f"D_{singleton_index}"
    return "beta_" + "_".join(str(value) for value in beta_value)


def beta_degree_id(beta_value: tuple[int, int, int]) -> str:
    return "beta_" + "_".join(str(value) for value in beta_value)


def saturation_extension_degrees() -> dict[str, ExpectedDegree]:
    rows: list[ExpectedDegree] = []
    for k in (1, 2, 3):
        i, j = complement_pair(k)
        rows.append(
            ExpectedDegree(
                f"D_{k}", f"D_{{{k}}}", "saturation_defect_signed_only",
                beta_with({i: 2, j: 2, k: 1}), "signed_only_blocked",
                "a071_target_presentation", "minimal_downward_saturation_extension",
                "A071 target_degrees.csv",
            )
        )
    return {row.degree_id: row for row in rows}


def nonzero_subdegree_defects(
    phi: dict,
    degrees: dict[str, ExpectedDegree],
) -> dict[str, list[tuple[int, int, int]]]:
    window_betas = {degree.beta for degree in degrees.values()}
    defects: dict[str, list[tuple[int, int, int]]] = {}
    for degree_id, degree in degrees.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(degree.beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in window_betas
        ]
        if missing:
            defects[degree_id] = missing
    return defects


def real_root_degrees() -> dict[str, tuple[int, int, int]]:
    return {
        "delta_1": (1, 0, 0),
        "delta_2": (0, 1, 0),
        "delta_3": (0, 0, 1),
    }


def post_saturation_simple_degrees() -> dict[str, tuple[int, int, int]]:
    return {
        "2a_12": (2, 2, 0),
        "2a_13": (2, 0, 2),
        "2a_23": (0, 2, 2),
        "C_1_2": (2, 1, 1),
        "C_2_2": (1, 2, 1),
        "C_3_2": (1, 1, 2),
        "D_1": (1, 2, 2),
        "D_2": (2, 1, 2),
        "D_3": (2, 2, 1),
        "2delta123": (2, 2, 2),
    }


def post_saturation_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension = saturation_extension_degrees()
    wsat_betas = {degree.beta for degree in expected.values()}
    wsat_betas.update(degree.beta for degree in extension.values())
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for simple_id, simple_beta in sorted(
        post_saturation_simple_degrees().items(),
        key=lambda item: (sum(item[1]), item[0]),
    ):
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, simple_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, simple_beta)
            terminal = tuple(
                simple_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_wsat = terminal in wsat_betas
            check_id = f"ps_{real_id}_{simple_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "simple_degree_id": simple_id,
                "simple_beta": simple_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_wsat": terminal_in_wsat,
                "relation_payload_status": (
                    "terminal_codomains_in_Wsat"
                    if terminal_in_wsat
                    else "terminal_codomains_missing_from_Wsat"
                ),
            }
    return obligations


def terminal_layer_expected_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = post_saturation_expected_obligations(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    extension = saturation_extension_degrees()
    known_betas = {degree.beta for degree in expected.values()}
    known_betas.update(degree.beta for degree in extension.values())
    known_betas.update(by_beta)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in known_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "additive_m": additive_m_coefficient(phi, terminal_beta),
            "terminal_in_wsat": False,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def terminal_layer_saturation_extension_expected_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = terminal_layer_expected_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "additive_m": additive_m_coefficient(phi, beta_value),
            "coverage_role": "terminal_layer_downward_saturation_extension",
        }
    return rows


def terminal_layer_saturated_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    extension = saturation_extension_degrees()
    terminal_rows = terminal_layer_expected_rows(expected)
    saturation_rows = terminal_layer_saturation_extension_expected_rows(expected)
    betas = {degree.beta for degree in expected.values()}
    betas.update(degree.beta for degree in extension.values())
    betas.update(row["beta"] for row in terminal_rows.values())
    betas.update(row["beta"] for row in saturation_rows.values())
    return betas


def terminal_layer_saturation_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = terminal_layer_saturation_extension_expected_rows(expected)
    known_betas = terminal_layer_saturated_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_w85 = terminal in known_betas
            check_id = f"tlse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_additive_m": additive_m_coefficient(phi, terminal),
                "terminal_in_w85": terminal_in_w85,
                "relation_payload_status": (
                    "terminal_codomains_in_W85"
                    if terminal_in_w85
                    else "terminal_codomains_missing_from_W85"
                ),
            }
    return obligations


def terminal_layer_saturation_real_string_defect_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    w85_betas = terminal_layer_saturated_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - w85_betas
    extended_betas = w85_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        assert isinstance(terminal_beta, tuple)
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    nonzero_terminal_count = sum(
        1 for terminal_beta in terminal_betas
        if signed_root_supermultiplicity(phi, terminal_beta) != 0
    )
    missing_nonzero_terminal_count = sum(
        1 for terminal_beta in new_terminal_betas
        if signed_root_supermultiplicity(phi, terminal_beta) != 0
    )
    return {
        "base_degree_count": len(w85_betas),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_w85_count": len(terminal_betas & w85_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": nonzero_terminal_count,
        "missing_nonzero_terminal_degree_count": missing_nonzero_terminal_count,
        "saturation_defect_parent_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def terminal_layer_saturation_real_string_defect_layer_expected_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    w85_betas = terminal_layer_saturated_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
    }
    terminal_betas = {
        terminal_beta for terminal_beta in terminal_betas
        if isinstance(terminal_beta, tuple)
    }
    known_betas = w85_betas | terminal_betas
    phi = phi_01_coefficients()
    parents_by_beta: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        for subdegree in proper_subdegrees(terminal_beta):
            if signed_root_supermultiplicity(phi, subdegree) != 0 and subdegree not in known_betas:
                parents_by_beta.setdefault(subdegree, []).append(terminal_beta)

    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_betas in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "additive_m": additive_m_coefficient(phi, beta_value),
            "parent_terminal_count": len(parent_betas),
            "coverage_role": "terminal_layer_saturation_real_string_downward_extension",
        }
    return rows


def terminal_layer_saturation_real_string_defect_layer_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    w85_betas = terminal_layer_saturated_betas(expected)
    terminal_obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in terminal_obligations.values()
    }
    terminal_betas = {
        terminal_beta for terminal_beta in terminal_betas
        if isinstance(terminal_beta, tuple)
    }
    defect_rows = terminal_layer_saturation_real_string_defect_layer_expected_rows(expected)
    defect_betas = {
        row["beta"] for row in defect_rows.values()
        if isinstance(row["beta"], tuple)
    }
    base_betas = w85_betas | terminal_betas | defect_betas
    phi = phi_01_coefficients()
    real_string_terminals: set[tuple[int, int, int]] = set()
    terminal_check_count = 0
    for row in defect_rows.values():
        beta_value = row["beta"]
        assert isinstance(beta_value, tuple)
        for real_beta in real_root_degrees().values():
            pairing = delta_pair(real_beta, beta_value)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, beta_value)
            terminal = tuple(
                beta_value[index] + exponent * real_beta[index]
                for index in range(3)
            )
            real_string_terminals.add(terminal)
            terminal_check_count += 1

    new_terminal_betas = real_string_terminals - base_betas
    extended_betas = base_betas | real_string_terminals
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in real_string_terminals:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(defect_betas),
        "terminal_check_count": terminal_check_count,
        "distinct_terminal_degree_count": len(real_string_terminals),
        "terminal_degree_in_base_count": len(real_string_terminals & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in real_string_terminals
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def terminal_layer_saturation_real_string_defect_layer_base_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    w85_betas = terminal_layer_saturated_betas(expected)
    terminal_obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in terminal_obligations.values()
    }
    terminal_betas = {
        terminal_beta for terminal_beta in terminal_betas
        if isinstance(terminal_beta, tuple)
    }
    defect_rows = terminal_layer_saturation_real_string_defect_layer_expected_rows(expected)
    defect_betas = {
        row["beta"] for row in defect_rows.values()
        if isinstance(row["beta"], tuple)
    }
    return w85_betas | terminal_betas | defect_betas


def terminal_layer_saturation_real_string_defect_layer_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    defect_rows = terminal_layer_saturation_real_string_defect_layer_expected_rows(expected)
    base_betas = terminal_layer_saturation_real_string_defect_layer_base_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for defect_id, defect_row in sorted(
        defect_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        defect_beta = defect_row["beta"]
        assert isinstance(defect_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, defect_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, defect_beta)
            terminal = tuple(
                defect_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"dlrs_{real_id}_{defect_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "defect_degree_id": defect_id,
                "defect_beta": defect_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_additive_m": additive_m_coefficient(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W237"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W237"
                ),
            }
    return obligations


def terminal_layer_saturation_real_string_defect_layer_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = terminal_layer_saturation_real_string_defect_layer_real_string_expected_obligations(expected)
    base_betas = terminal_layer_saturation_real_string_defect_layer_base_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "additive_m": additive_m_coefficient(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = terminal_layer_saturation_real_string_defect_layer_real_string_terminal_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "additive_m": additive_m_coefficient(phi, beta_value),
            "coverage_role": "defect_layer_real_string_downward_saturation_extension",
        }
    return rows


def terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    base_betas = terminal_layer_saturation_real_string_defect_layer_base_betas(expected)
    terminal_rows = terminal_layer_saturation_real_string_defect_layer_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_rows = terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_rows(expected)
    extension_betas = {
        extension_row["beta"]
        for extension_row in extension_rows.values()
        if isinstance(extension_row["beta"], tuple)
    }
    return base_betas | terminal_betas | extension_betas


def terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_rows(expected)
    base_betas = terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"dlrsse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W469"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W469"
                ),
            }
    return obligations


def terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_expected_obligations(
            expected
        )
    )
    base_betas = terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
        if isinstance(obligation["terminal_beta"], tuple)
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - base_betas
    extended_betas = base_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(
            terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_rows(expected)
        ),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_base_count": len(terminal_betas & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_expected_obligations(
            expected
        )
    )
    base_betas = terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_rows(
            expected
        )
    )
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "coverage_role": "defect_layer_real_string_saturation_extension_downward_saturation_extension",
        }
    return rows


def twelve_row_saturation_base_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    base_betas = terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(expected)
    terminal_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_rows(
            expected
        )
    )
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_rows(
            expected
        )
    )
    extension_betas = {
        extension_row["beta"]
        for extension_row in extension_rows.values()
        if isinstance(extension_row["beta"], tuple)
    }
    return base_betas | terminal_betas | extension_betas


def twelve_row_saturation_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_rows(
            expected
        )
    )
    base_betas = twelve_row_saturation_base_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"trse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W571"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W571"
                ),
            }
    return obligations


def twelve_row_saturation_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = twelve_row_saturation_real_string_expected_obligations(expected)
    base_betas = twelve_row_saturation_base_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
        if isinstance(obligation["terminal_beta"], tuple)
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - base_betas
    extended_betas = base_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(
            terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_rows(
                expected
            )
        ),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_base_count": len(terminal_betas & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def twelve_row_saturation_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = twelve_row_saturation_real_string_expected_obligations(expected)
    base_betas = twelve_row_saturation_base_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def twelve_row_saturation_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = twelve_row_saturation_real_string_terminal_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "coverage_role": "twelve_row_real_string_downward_saturation_extension",
        }
    return rows


def six_row_saturation_base_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    base_betas = twelve_row_saturation_base_betas(expected)
    terminal_rows = twelve_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_rows = twelve_row_saturation_real_string_saturation_extension_rows(expected)
    extension_betas = {
        extension_row["beta"]
        for extension_row in extension_rows.values()
        if isinstance(extension_row["beta"], tuple)
    }
    return base_betas | terminal_betas | extension_betas


def six_row_saturation_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = twelve_row_saturation_real_string_saturation_extension_rows(expected)
    base_betas = six_row_saturation_base_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"srse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W597"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W597"
                ),
            }
    return obligations


def six_row_saturation_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = six_row_saturation_real_string_expected_obligations(expected)
    base_betas = six_row_saturation_base_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
        if isinstance(obligation["terminal_beta"], tuple)
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - base_betas
    extended_betas = base_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(twelve_row_saturation_real_string_saturation_extension_rows(expected)),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_base_count": len(terminal_betas & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def six_row_saturation_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = six_row_saturation_real_string_expected_obligations(expected)
    base_betas = six_row_saturation_base_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def six_row_saturation_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = six_row_saturation_real_string_terminal_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "coverage_role": "six_row_real_string_downward_saturation_extension",
        }
    return rows


def second_six_row_saturation_base_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    base_betas = six_row_saturation_base_betas(expected)
    terminal_rows = six_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_rows = six_row_saturation_real_string_saturation_extension_rows(expected)
    extension_betas = {
        extension_row["beta"]
        for extension_row in extension_rows.values()
        if isinstance(extension_row["beta"], tuple)
    }
    return base_betas | terminal_betas | extension_betas


def second_six_row_saturation_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = six_row_saturation_real_string_saturation_extension_rows(expected)
    base_betas = second_six_row_saturation_base_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"ssrse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W613"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W613"
                ),
            }
    return obligations


def second_six_row_saturation_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = second_six_row_saturation_real_string_expected_obligations(expected)
    base_betas = second_six_row_saturation_base_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
        if isinstance(obligation["terminal_beta"], tuple)
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - base_betas
    extended_betas = base_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(six_row_saturation_real_string_saturation_extension_rows(expected)),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_base_count": len(terminal_betas & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def second_six_row_saturation_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = second_six_row_saturation_real_string_expected_obligations(expected)
    base_betas = second_six_row_saturation_base_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def second_six_row_saturation_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = second_six_row_saturation_real_string_terminal_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "coverage_role": "second_six_row_real_string_downward_saturation_extension",
        }
    return rows


def third_six_row_saturation_base_betas(
    expected: dict[str, ExpectedDegree],
) -> set[tuple[int, int, int]]:
    base_betas = second_six_row_saturation_base_betas(expected)
    terminal_rows = second_six_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_rows = second_six_row_saturation_real_string_saturation_extension_rows(expected)
    extension_betas = {
        extension_row["beta"]
        for extension_row in extension_rows.values()
        if isinstance(extension_row["beta"], tuple)
    }
    return base_betas | terminal_betas | extension_betas


def third_six_row_saturation_real_string_expected_obligations(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    extension_rows = second_six_row_saturation_real_string_saturation_extension_rows(expected)
    base_betas = third_six_row_saturation_base_betas(expected)
    phi = phi_01_coefficients()
    obligations: dict[str, dict[str, object]] = {}
    for extension_id, extension_row in sorted(
        extension_rows.items(),
        key=lambda item: (item[1]["height"], item[1]["beta"], item[0]),
    ):
        extension_beta = extension_row["beta"]
        assert isinstance(extension_beta, tuple)
        for real_id, real_beta in real_root_degrees().items():
            pairing = delta_pair(real_beta, extension_beta)
            if pairing >= 0:
                continue
            exponent = real_string_exponent(real_beta, extension_beta)
            terminal = tuple(
                extension_beta[index] + exponent * real_beta[index]
                for index in range(3)
            )
            terminal_in_base = terminal in base_betas
            check_id = f"tsrse_{real_id}_{extension_id}"
            obligations[check_id] = {
                "real_root_id": real_id,
                "extension_degree_id": extension_id,
                "extension_beta": extension_beta,
                "pairing": pairing,
                "serre_exponent": exponent,
                "terminal_beta": terminal,
                "terminal_gamma": delta_basis_to_gamma(terminal),
                "terminal_height": sum(terminal),
                "terminal_norm": delta_pair(terminal, terminal),
                "terminal_signed_dimension": signed_root_supermultiplicity(phi, terminal),
                "terminal_in_base": terminal_in_base,
                "relation_payload_status": (
                    "terminal_codomains_in_W629"
                    if terminal_in_base
                    else "terminal_codomains_missing_from_W629"
                ),
            }
    return obligations


def third_six_row_saturation_real_string_summary(
    expected: dict[str, ExpectedDegree],
) -> dict[str, int]:
    obligations = third_six_row_saturation_real_string_expected_obligations(expected)
    base_betas = third_six_row_saturation_base_betas(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in obligations.values()
        if isinstance(obligation["terminal_beta"], tuple)
    }
    phi = phi_01_coefficients()
    new_terminal_betas = terminal_betas - base_betas
    extended_betas = base_betas | terminal_betas
    defects_by_parent: dict[tuple[int, int, int], list[tuple[int, int, int]]] = {}
    for terminal_beta in terminal_betas:
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        if missing:
            defects_by_parent[terminal_beta] = missing
    distinct_defects = {
        subdegree
        for missing in defects_by_parent.values()
        for subdegree in missing
    }
    return {
        "base_degree_count": len(base_betas),
        "generator_degree_count": len(second_six_row_saturation_real_string_saturation_extension_rows(expected)),
        "terminal_check_count": len(obligations),
        "distinct_terminal_degree_count": len(terminal_betas),
        "terminal_degree_in_base_count": len(terminal_betas & base_betas),
        "new_terminal_degree_count": len(new_terminal_betas),
        "nonzero_terminal_degree_count": sum(
            1 for terminal_beta in terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "missing_nonzero_terminal_degree_count": sum(
            1 for terminal_beta in new_terminal_betas
            if signed_root_supermultiplicity(phi, terminal_beta) != 0
        ),
        "saturation_defect_parent_terminal_count": len(defects_by_parent),
        "saturation_defect_occurrence_count": sum(len(missing) for missing in defects_by_parent.values()),
        "saturation_defect_distinct_degree_count": len(distinct_defects),
    }


def third_six_row_saturation_real_string_terminal_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    obligations = third_six_row_saturation_real_string_expected_obligations(expected)
    base_betas = third_six_row_saturation_base_betas(expected)
    by_beta: dict[tuple[int, int, int], list[str]] = {}
    for check_id, obligation in obligations.items():
        terminal_beta = obligation["terminal_beta"]
        assert isinstance(terminal_beta, tuple)
        by_beta.setdefault(terminal_beta, []).append(check_id)

    phi = phi_01_coefficients()
    extended_betas = base_betas | set(by_beta)
    rows: dict[str, dict[str, object]] = {}
    for terminal_beta, check_ids in by_beta.items():
        missing = [
            subdegree for subdegree in proper_subdegrees(terminal_beta)
            if signed_root_supermultiplicity(phi, subdegree) != 0
            and subdegree not in extended_betas
        ]
        degree_id = beta_degree_id(terminal_beta)
        rows[degree_id] = {
            "source_check_ids": sorted(check_ids),
            "beta": terminal_beta,
            "gamma": delta_basis_to_gamma(terminal_beta),
            "height": sum(terminal_beta),
            "norm": delta_pair(terminal_beta, terminal_beta),
            "signed_dimension": signed_root_supermultiplicity(phi, terminal_beta),
            "terminal_in_base": terminal_beta in base_betas,
            "missing_nonzero_subdegrees": missing,
        }
    return rows


def third_six_row_saturation_real_string_saturation_extension_rows(
    expected: dict[str, ExpectedDegree],
) -> dict[str, dict[str, object]]:
    terminal_rows = third_six_row_saturation_real_string_terminal_rows(expected)
    parents_by_beta: dict[tuple[int, int, int], list[str]] = {}
    for terminal_id, terminal_row in terminal_rows.items():
        missing = terminal_row["missing_nonzero_subdegrees"]
        assert isinstance(missing, list)
        for subdegree in missing:
            parents_by_beta.setdefault(subdegree, []).append(terminal_id)

    phi = phi_01_coefficients()
    rows: dict[str, dict[str, object]] = {}
    for beta_value, parent_ids in parents_by_beta.items():
        degree_id = beta_degree_id(beta_value)
        rows[degree_id] = {
            "parent_terminal_degree_ids": sorted(parent_ids),
            "beta": beta_value,
            "gamma": delta_basis_to_gamma(beta_value),
            "height": sum(beta_value),
            "norm": delta_pair(beta_value, beta_value),
            "signed_dimension": signed_root_supermultiplicity(phi, beta_value),
            "coverage_role": "third_six_row_real_string_downward_saturation_extension",
        }
    return rows


def verify_downward_saturation(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    by_parent = rows_by_id(rows, "parent_degree_id")
    require_equal(set(by_parent), set(expected), "downward saturation parent coverage")
    phi = phi_01_coefficients()
    window_betas = {degree.beta for degree in expected.values()}
    total_defect_rank = 0
    for degree_id, degree in expected.items():
        row = by_parent[degree_id]
        check_verified(row, "downward_saturation.csv")
        subdegrees = proper_subdegrees(degree.beta)
        nonzero = [
            subdegree for subdegree in subdegrees
            if signed_root_supermultiplicity(phi, subdegree) != 0
        ]
        wrel = [subdegree for subdegree in subdegrees if subdegree in window_betas]
        missing = [subdegree for subdegree in nonzero if subdegree not in window_betas]
        missing_ids = ";".join(saturation_defect_id(subdegree) for subdegree in missing)
        missing_signed = ";".join(
            f"{saturation_defect_id(subdegree)}:"
            f"{signed_root_supermultiplicity(phi, subdegree)}"
            for subdegree in missing
        )
        defect_rank = len(missing)
        total_defect_rank += defect_rank
        require_equal(
            int_cell(row, "total_proper_subdegrees"),
            len(subdegrees),
            f"{degree_id} total proper subdegrees",
        )
        require_equal(
            int_cell(row, "nonzero_proper_subdegrees"),
            len(nonzero),
            f"{degree_id} nonzero proper subdegrees",
        )
        require_equal(
            int_cell(row, "wrel_proper_subdegrees"),
            len(wrel),
            f"{degree_id} Wrel proper subdegrees",
        )
        require_equal(
            int_cell(row, "missing_nonzero_subdegrees"),
            defect_rank,
            f"{degree_id} missing nonzero subdegrees",
        )
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            missing_ids,
            f"{degree_id} missing nonzero subdegree ids",
        )
        require_equal(
            row["missing_nonzero_signed_dimensions"],
            missing_signed,
            f"{degree_id} missing nonzero signed dimensions",
        )
        require_equal(
            int_cell(row, "coverage_defect_rank"),
            defect_rank,
            f"{degree_id} coverage defect rank",
        )
    require_equal(total_defect_rank, 3, "total downward saturation defect rank")


def verify_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
    a071_ids: set[str],
) -> None:
    extension = saturation_extension_degrees()
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(extension), "saturation extension coverage")
    phi = phi_01_coefficients()
    for degree_id, degree in extension.items():
        if degree_id not in a071_ids:
            raise ValueError(f"{degree_id}: absent from A071 fixture")
        row = by_degree[degree_id]
        check_verified(row, "saturation_extension.csv")
        require_equal(row["tex_label"], degree.tex_label, f"{degree_id} tex_label")
        require_equal(beta(row), degree.beta, f"{degree_id} beta")
        gamma = delta_basis_to_gamma(degree.beta)
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma_n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma_l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma_m")
        require_equal(int_cell(row, "height"), sum(degree.beta), f"{degree_id} height")
        require_equal(int_cell(row, "norm"), delta_pair(degree.beta, degree.beta), f"{degree_id} norm")
        require_equal(
            int_cell(row, "signed_dimension"),
            signed_root_supermultiplicity(phi, degree.beta),
            f"{degree_id} signed dimension",
        )
        require_equal(
            int_cell(row, "additive_m"),
            additive_m_coefficient(phi, degree.beta),
            f"{degree_id} additive m",
        )
        require_equal(row["target_status"], degree.target_status, f"{degree_id} target_status")
        require_equal(row["target_packet_id"], degree.parity_packet_id, f"{degree_id} target packet")
        require_equal(row["coverage_role"], degree.closure_source, f"{degree_id} coverage role")

    base_defect_betas = {
        subdegree
        for missing in nonzero_subdegree_defects(phi, expected).values()
        for subdegree in missing
    }
    extension_betas = {degree.beta for degree in extension.values()}
    require_equal(base_defect_betas, extension_betas, "minimal saturation extension")
    extended = dict(expected)
    extended.update(extension)
    extended_defect_rank = sum(
        len(missing) for missing in nonzero_subdegree_defects(phi, extended).values()
    )
    require_equal(extended_defect_rank, 0, "saturated extension defect rank")


def verify_post_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = post_saturation_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "post-saturation obligation coverage")
    missing_terminal_count = 0
    nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "post_saturation_real_string_obligations.csv")
        simple_beta = obligation["simple_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(simple_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["simple_degree_id"], obligation["simple_degree_id"], f"{check_id} simple degree")
        require_equal(int_cell(row, "simple_beta_c1"), simple_beta[0], f"{check_id} simple beta c1")
        require_equal(int_cell(row, "simple_beta_c2"), simple_beta[1], f"{check_id} simple beta c2")
        require_equal(int_cell(row, "simple_beta_c3"), simple_beta[2], f"{check_id} simple beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        terminal_in_wsat = bool(obligation["terminal_in_wsat"])
        require_equal(bool_cell(row, "terminal_in_wsat"), terminal_in_wsat, f"{check_id} terminal in Wsat")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if not terminal_in_wsat:
            missing_terminal_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
    require_equal(missing_terminal_count, 21, "post-saturation missing terminal count")
    require_equal(nonzero_terminal_count, 10, "post-saturation nonzero terminal count")


def verify_post_saturation_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = terminal_layer_expected_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "post-saturation terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "post_saturation_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(int_cell(row, "additive_m"), expected_row["additive_m"], f"{degree_id} additive m")
        require_equal(bool_cell(row, "terminal_in_wsat"), False, f"{degree_id} terminal in Wsat")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if signed != 0:
            nonzero_terminal_count += 1
    require_equal(len(expected_rows), 21, "terminal layer degree count")
    require_equal(nonzero_terminal_count, 10, "terminal layer nonzero signed count")
    require_equal(missing_occurrences, 114, "terminal layer saturation defect occurrences")
    require_equal(len(distinct_missing), 26, "terminal layer distinct saturation defects")


def verify_terminal_layer_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = terminal_layer_saturation_extension_expected_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "terminal-layer saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "terminal_layer_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(
            row["parent_terminal_degree_ids"],
            ";".join(parent_ids),
            f"{degree_id} parent terminal ids",
        )
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(
            int_cell(row, "signed_dimension"),
            expected_row["signed_dimension"],
            f"{degree_id} signed dimension",
        )
        require_equal(
            int_cell(row, "additive_m"),
            expected_row["additive_m"],
            f"{degree_id} additive m",
        )
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    saturated_betas = terminal_layer_saturated_betas(expected)
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 26, "terminal-layer saturation extension degree count")
    require_equal(total_occurrences, 114, "terminal-layer saturation extension occurrence count")
    require_equal(len(saturated_betas), 85, "terminal-layer saturated total degree count")
    require_equal(len(remaining_defects), 0, "terminal-layer saturation extension defect rank")


def verify_terminal_layer_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "terminal-layer saturation real-string coverage")
    missing_terminal_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "terminal_layer_saturation_real_string_obligations.csv")
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(
            row["extension_degree_id"],
            obligation["extension_degree_id"],
            f"{check_id} extension degree",
        )
        require_equal(
            int_cell(row, "extension_beta_c1"),
            extension_beta[0],
            f"{check_id} extension beta c1",
        )
        require_equal(
            int_cell(row, "extension_beta_c2"),
            extension_beta[1],
            f"{check_id} extension beta c2",
        )
        require_equal(
            int_cell(row, "extension_beta_c3"),
            extension_beta[2],
            f"{check_id} extension beta c3",
        )
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(
            int_cell(row, "serre_exponent"),
            obligation["serre_exponent"],
            f"{check_id} exponent",
        )
        require_equal(
            int_cell(row, "terminal_beta_c1"),
            terminal_beta[0],
            f"{check_id} terminal beta c1",
        )
        require_equal(
            int_cell(row, "terminal_beta_c2"),
            terminal_beta[1],
            f"{check_id} terminal beta c2",
        )
        require_equal(
            int_cell(row, "terminal_beta_c3"),
            terminal_beta[2],
            f"{check_id} terminal beta c3",
        )
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} gamma m")
        require_equal(
            int_cell(row, "terminal_height"),
            obligation["terminal_height"],
            f"{check_id} terminal height",
        )
        require_equal(
            int_cell(row, "terminal_norm"),
            obligation["terminal_norm"],
            f"{check_id} terminal norm",
        )
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_w85 = bool(obligation["terminal_in_w85"])
        require_equal(
            int_cell(row, "terminal_signed_dimension"),
            terminal_signed,
            f"{check_id} terminal signed",
        )
        require_equal(
            int_cell(row, "terminal_additive_m"),
            obligation["terminal_additive_m"],
            f"{check_id} terminal additive m",
        )
        require_equal(bool_cell(row, "terminal_in_w85"), terminal_in_w85, f"{check_id} terminal in W85")
        require_equal(
            row["relation_payload_status"],
            obligation["relation_payload_status"],
            f"{check_id} relation status",
        )
        if not terminal_in_w85:
            missing_terminal_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_w85 and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 55, "terminal-layer saturation real-string obligation count")
    require_equal(missing_terminal_count, 54, "terminal-layer saturation missing terminal count")
    require_equal(nonzero_terminal_count, 13, "terminal-layer saturation nonzero terminal count")
    require_equal(
        missing_nonzero_terminal_count,
        12,
        "terminal-layer saturation missing nonzero terminal count",
    )


def verify_terminal_layer_saturation_real_string_defect_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "terminal-layer saturation real-string defect summary row count")
    row = rows[0]
    check_verified(row, "terminal_layer_saturation_real_string_defect_summary.csv")
    require_equal(row["summary_id"], "tlse_real_string_terminal_layer", "summary id")
    expected_summary = terminal_layer_saturation_real_string_defect_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"summary {key}")
    require_equal(expected_summary["base_degree_count"], 85, "summary base degree count")
    require_equal(expected_summary["terminal_check_count"], 55, "summary terminal check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 55, "summary terminal degree count")
    require_equal(expected_summary["terminal_degree_in_w85_count"], 1, "summary terminal degree in W85 count")
    require_equal(expected_summary["new_terminal_degree_count"], 54, "summary new terminal degree count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 13, "summary nonzero terminal degree count")
    require_equal(
        expected_summary["missing_nonzero_terminal_degree_count"],
        12,
        "summary missing nonzero terminal degree count",
    )
    require_equal(expected_summary["saturation_defect_parent_count"], 36, "summary defect parent count")
    require_equal(expected_summary["saturation_defect_occurrence_count"], 546, "summary defect occurrence count")
    require_equal(expected_summary["saturation_defect_distinct_degree_count"], 98, "summary distinct defect count")


def verify_terminal_layer_saturation_real_string_defect_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = terminal_layer_saturation_real_string_defect_layer_expected_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "terminal-layer saturation real-string defect layer coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "terminal_layer_saturation_real_string_defect_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(
            int_cell(row, "signed_dimension"),
            expected_row["signed_dimension"],
            f"{degree_id} signed dimension",
        )
        require_equal(
            int_cell(row, "additive_m"),
            expected_row["additive_m"],
            f"{degree_id} additive m",
        )
        parent_count = int(expected_row["parent_terminal_count"])
        require_equal(int_cell(row, "parent_terminal_count"), parent_count, f"{degree_id} parent count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += parent_count

    w85_betas = terminal_layer_saturated_betas(expected)
    terminal_obligations = terminal_layer_saturation_real_string_expected_obligations(expected)
    terminal_betas = {
        obligation["terminal_beta"]
        for obligation in terminal_obligations.values()
    }
    terminal_betas = {
        terminal_beta for terminal_beta in terminal_betas
        if isinstance(terminal_beta, tuple)
    }
    saturated_betas = w85_betas | terminal_betas | {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 98, "terminal-layer saturation real-string defect layer count")
    require_equal(total_occurrences, 546, "terminal-layer saturation real-string defect layer occurrence count")
    require_equal(len(saturated_betas), 237, "terminal-layer saturation real-string saturated total degree count")
    require_equal(len(remaining_defects), 0, "terminal-layer saturation real-string defect layer defect rank")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "defect-layer real-string summary row count")
    row = rows[0]
    check_verified(row, "terminal_layer_saturation_real_string_defect_layer_real_string_summary.csv")
    require_equal(row["summary_id"], "tlse_defect_layer_real_string", "defect-layer real-string summary id")
    expected_summary = terminal_layer_saturation_real_string_defect_layer_real_string_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"defect-layer real-string summary {key}")
    require_equal(expected_summary["base_degree_count"], 237, "defect-layer real-string base degree count")
    require_equal(expected_summary["generator_degree_count"], 98, "defect-layer real-string generator count")
    require_equal(expected_summary["terminal_check_count"], 206, "defect-layer real-string check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 206, "defect-layer real-string terminal count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 24, "defect-layer real-string in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 182, "defect-layer real-string new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 48, "defect-layer real-string nonzero count")
    require_equal(
        expected_summary["missing_nonzero_terminal_degree_count"],
        24,
        "defect-layer real-string missing nonzero count",
    )
    require_equal(
        expected_summary["saturation_defect_parent_terminal_count"],
        62,
        "defect-layer real-string defect parent count",
    )
    require_equal(
        expected_summary["saturation_defect_occurrence_count"],
        624,
        "defect-layer real-string defect occurrence count",
    )
    require_equal(
        expected_summary["saturation_defect_distinct_degree_count"],
        50,
        "defect-layer real-string distinct defect count",
    )


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = terminal_layer_saturation_real_string_defect_layer_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "defect-layer real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "terminal_layer_saturation_real_string_defect_layer_real_string_obligations.csv")
        defect_beta = obligation["defect_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(defect_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["defect_degree_id"], obligation["defect_degree_id"], f"{check_id} defect degree")
        require_equal(int_cell(row, "defect_beta_c1"), defect_beta[0], f"{check_id} defect beta c1")
        require_equal(int_cell(row, "defect_beta_c2"), defect_beta[1], f"{check_id} defect beta c2")
        require_equal(int_cell(row, "defect_beta_c3"), defect_beta[2], f"{check_id} defect beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 206, "defect-layer real-string obligation count")
    require_equal(in_base_count, 24, "defect-layer real-string obligation in-base count")
    require_equal(nonzero_terminal_count, 48, "defect-layer real-string obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 24, "defect-layer real-string obligation missing nonzero count")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = terminal_layer_saturation_real_string_defect_layer_real_string_terminal_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "defect-layer real-string terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 206, "defect-layer real-string terminal layer degree count")
    require_equal(in_base_count, 24, "defect-layer real-string terminal layer in-base count")
    require_equal(nonzero_terminal_count, 48, "defect-layer real-string terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 24, "defect-layer real-string terminal layer missing nonzero count")
    require_equal(missing_occurrences, 624, "defect-layer real-string terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 50, "defect-layer real-string terminal layer distinct saturation count")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "defect-layer real-string saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = terminal_layer_saturation_real_string_defect_layer_base_betas(expected)
    terminal_rows = terminal_layer_saturation_real_string_defect_layer_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 50, "defect-layer real-string saturation extension degree count")
    require_equal(total_occurrences, 624, "defect-layer real-string saturation extension occurrence count")
    require_equal(len(saturated_betas), 469, "defect-layer real-string saturated total degree count")
    require_equal(len(remaining_defects), 0, "defect-layer real-string saturation extension defect rank")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "defect-layer real-string saturation-extension summary row count")
    row = rows[0]
    check_verified(
        row,
        "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary.csv",
    )
    require_equal(row["summary_id"], "dlrsse_real_string", "defect-layer saturation-extension real-string summary id")
    expected_summary = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary(
            expected
        )
    )
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"defect-layer saturation-extension summary {key}")
    require_equal(expected_summary["base_degree_count"], 469, "defect-layer saturation-extension base degree count")
    require_equal(expected_summary["generator_degree_count"], 50, "defect-layer saturation-extension generator count")
    require_equal(expected_summary["terminal_check_count"], 96, "defect-layer saturation-extension check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 96, "defect-layer saturation-extension terminal count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 6, "defect-layer saturation-extension in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 90, "defect-layer saturation-extension new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 6, "defect-layer saturation-extension nonzero count")
    require_equal(
        expected_summary["missing_nonzero_terminal_degree_count"],
        0,
        "defect-layer saturation-extension missing nonzero count",
    )
    require_equal(
        expected_summary["saturation_defect_parent_terminal_count"],
        12,
        "defect-layer saturation-extension defect parent count",
    )
    require_equal(
        expected_summary["saturation_defect_occurrence_count"],
        44,
        "defect-layer saturation-extension occurrence count",
    )
    require_equal(
        expected_summary["saturation_defect_distinct_degree_count"],
        12,
        "defect-layer saturation-extension distinct defect count",
    )


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_expected_obligations(
            expected
        )
    )
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "defect-layer saturation-extension real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(
            row,
            "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_obligations.csv",
        )
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["extension_degree_id"], obligation["extension_degree_id"], f"{check_id} extension degree")
        require_equal(int_cell(row, "extension_beta_c1"), extension_beta[0], f"{check_id} extension beta c1")
        require_equal(int_cell(row, "extension_beta_c2"), extension_beta[1], f"{check_id} extension beta c2")
        require_equal(int_cell(row, "extension_beta_c3"), extension_beta[2], f"{check_id} extension beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 96, "defect-layer saturation-extension obligation count")
    require_equal(in_base_count, 6, "defect-layer saturation-extension obligation in-base count")
    require_equal(nonzero_terminal_count, 6, "defect-layer saturation-extension obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "defect-layer saturation-extension obligation missing nonzero count")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_rows(
            expected
        )
    )
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "defect-layer saturation-extension terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(
            row,
            "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer.csv",
        )
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 96, "defect-layer saturation-extension terminal layer degree count")
    require_equal(in_base_count, 6, "defect-layer saturation-extension terminal layer in-base count")
    require_equal(nonzero_terminal_count, 6, "defect-layer saturation-extension terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "defect-layer saturation-extension terminal layer missing nonzero count")
    require_equal(missing_occurrences, 44, "defect-layer saturation-extension terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 12, "defect-layer saturation-extension terminal layer distinct saturation count")


def verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension_rows(
            expected
        )
    )
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "defect-layer saturation-extension saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(
            row,
            "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension.csv",
        )
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = terminal_layer_saturation_real_string_defect_layer_real_string_saturated_betas(expected)
    terminal_rows = (
        terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_rows(
            expected
        )
    )
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 12, "defect-layer saturation-extension saturation extension degree count")
    require_equal(total_occurrences, 44, "defect-layer saturation-extension saturation extension occurrence count")
    require_equal(len(saturated_betas), 571, "defect-layer saturation-extension saturated total degree count")
    require_equal(len(remaining_defects), 0, "defect-layer saturation-extension saturation extension defect rank")


def verify_twelve_row_saturation_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "twelve-row real-string summary row count")
    row = rows[0]
    check_verified(row, "twelve_row_saturation_real_string_summary.csv")
    require_equal(row["summary_id"], "twelve_row_real_string", "twelve-row real-string summary id")
    expected_summary = twelve_row_saturation_real_string_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"twelve-row summary {key}")
    require_equal(expected_summary["base_degree_count"], 571, "twelve-row base degree count")
    require_equal(expected_summary["generator_degree_count"], 12, "twelve-row generator count")
    require_equal(expected_summary["terminal_check_count"], 20, "twelve-row terminal check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 20, "twelve-row terminal degree count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 0, "twelve-row terminal in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 20, "twelve-row new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 0, "twelve-row nonzero terminal count")
    require_equal(expected_summary["missing_nonzero_terminal_degree_count"], 0, "twelve-row missing nonzero count")
    require_equal(expected_summary["saturation_defect_parent_terminal_count"], 4, "twelve-row defect parent count")
    require_equal(expected_summary["saturation_defect_occurrence_count"], 8, "twelve-row defect occurrence count")
    require_equal(expected_summary["saturation_defect_distinct_degree_count"], 6, "twelve-row distinct defect count")


def verify_twelve_row_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = twelve_row_saturation_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "twelve-row real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "twelve_row_saturation_real_string_obligations.csv")
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["extension_degree_id"], obligation["extension_degree_id"], f"{check_id} extension degree")
        require_equal(int_cell(row, "extension_beta_c1"), extension_beta[0], f"{check_id} extension beta c1")
        require_equal(int_cell(row, "extension_beta_c2"), extension_beta[1], f"{check_id} extension beta c2")
        require_equal(int_cell(row, "extension_beta_c3"), extension_beta[2], f"{check_id} extension beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 20, "twelve-row obligation count")
    require_equal(in_base_count, 0, "twelve-row obligation in-base count")
    require_equal(nonzero_terminal_count, 0, "twelve-row obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "twelve-row obligation missing nonzero count")


def verify_twelve_row_saturation_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = twelve_row_saturation_real_string_terminal_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "twelve-row terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "twelve_row_saturation_real_string_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 20, "twelve-row terminal layer degree count")
    require_equal(in_base_count, 0, "twelve-row terminal layer in-base count")
    require_equal(nonzero_terminal_count, 0, "twelve-row terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "twelve-row terminal layer missing nonzero count")
    require_equal(missing_occurrences, 8, "twelve-row terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 6, "twelve-row terminal layer distinct saturation count")


def verify_twelve_row_saturation_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = twelve_row_saturation_real_string_saturation_extension_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "twelve-row saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "twelve_row_saturation_real_string_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = twelve_row_saturation_base_betas(expected)
    terminal_rows = twelve_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 6, "twelve-row saturation extension degree count")
    require_equal(total_occurrences, 8, "twelve-row saturation extension occurrence count")
    require_equal(len(saturated_betas), 597, "twelve-row saturated total degree count")
    require_equal(len(remaining_defects), 0, "twelve-row saturation extension defect rank")


def verify_six_row_saturation_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "six-row real-string summary row count")
    row = rows[0]
    check_verified(row, "six_row_saturation_real_string_summary.csv")
    require_equal(row["summary_id"], "six_row_real_string", "six-row real-string summary id")
    expected_summary = six_row_saturation_real_string_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"six-row summary {key}")
    require_equal(expected_summary["base_degree_count"], 597, "six-row base degree count")
    require_equal(expected_summary["generator_degree_count"], 6, "six-row generator count")
    require_equal(expected_summary["terminal_check_count"], 10, "six-row terminal check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 10, "six-row terminal degree count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 0, "six-row terminal in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 10, "six-row new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 0, "six-row nonzero terminal count")
    require_equal(expected_summary["missing_nonzero_terminal_degree_count"], 0, "six-row missing nonzero count")
    require_equal(expected_summary["saturation_defect_parent_terminal_count"], 10, "six-row defect parent count")
    require_equal(expected_summary["saturation_defect_occurrence_count"], 18, "six-row defect occurrence count")
    require_equal(expected_summary["saturation_defect_distinct_degree_count"], 6, "six-row distinct defect count")


def verify_six_row_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = six_row_saturation_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "six-row real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "six_row_saturation_real_string_obligations.csv")
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["extension_degree_id"], obligation["extension_degree_id"], f"{check_id} extension degree")
        require_equal(int_cell(row, "extension_beta_c1"), extension_beta[0], f"{check_id} extension beta c1")
        require_equal(int_cell(row, "extension_beta_c2"), extension_beta[1], f"{check_id} extension beta c2")
        require_equal(int_cell(row, "extension_beta_c3"), extension_beta[2], f"{check_id} extension beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 10, "six-row obligation count")
    require_equal(in_base_count, 0, "six-row obligation in-base count")
    require_equal(nonzero_terminal_count, 0, "six-row obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "six-row obligation missing nonzero count")


def verify_six_row_saturation_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = six_row_saturation_real_string_terminal_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "six-row terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "six_row_saturation_real_string_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 10, "six-row terminal layer degree count")
    require_equal(in_base_count, 0, "six-row terminal layer in-base count")
    require_equal(nonzero_terminal_count, 0, "six-row terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "six-row terminal layer missing nonzero count")
    require_equal(missing_occurrences, 18, "six-row terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 6, "six-row terminal layer distinct saturation count")


def verify_six_row_saturation_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = six_row_saturation_real_string_saturation_extension_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "six-row saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "six_row_saturation_real_string_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = six_row_saturation_base_betas(expected)
    terminal_rows = six_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 6, "six-row saturation extension degree count")
    require_equal(total_occurrences, 18, "six-row saturation extension occurrence count")
    require_equal(len(saturated_betas), 613, "six-row saturated total degree count")
    require_equal(len(remaining_defects), 0, "six-row saturation extension defect rank")


def verify_second_six_row_saturation_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "second six-row real-string summary row count")
    row = rows[0]
    check_verified(row, "second_six_row_saturation_real_string_summary.csv")
    require_equal(row["summary_id"], "second_six_row_real_string", "second six-row real-string summary id")
    expected_summary = second_six_row_saturation_real_string_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"second six-row summary {key}")
    require_equal(expected_summary["base_degree_count"], 613, "second six-row base degree count")
    require_equal(expected_summary["generator_degree_count"], 6, "second six-row generator count")
    require_equal(expected_summary["terminal_check_count"], 10, "second six-row terminal check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 10, "second six-row terminal degree count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 0, "second six-row terminal in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 10, "second six-row new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 0, "second six-row nonzero terminal count")
    require_equal(expected_summary["missing_nonzero_terminal_degree_count"], 0, "second six-row missing nonzero count")
    require_equal(expected_summary["saturation_defect_parent_terminal_count"], 4, "second six-row defect parent count")
    require_equal(expected_summary["saturation_defect_occurrence_count"], 8, "second six-row defect occurrence count")
    require_equal(expected_summary["saturation_defect_distinct_degree_count"], 6, "second six-row distinct defect count")


def verify_second_six_row_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = second_six_row_saturation_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "second six-row real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "second_six_row_saturation_real_string_obligations.csv")
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["extension_degree_id"], obligation["extension_degree_id"], f"{check_id} extension degree")
        require_equal(int_cell(row, "extension_beta_c1"), extension_beta[0], f"{check_id} extension beta c1")
        require_equal(int_cell(row, "extension_beta_c2"), extension_beta[1], f"{check_id} extension beta c2")
        require_equal(int_cell(row, "extension_beta_c3"), extension_beta[2], f"{check_id} extension beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 10, "second six-row obligation count")
    require_equal(in_base_count, 0, "second six-row obligation in-base count")
    require_equal(nonzero_terminal_count, 0, "second six-row obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "second six-row obligation missing nonzero count")


def verify_second_six_row_saturation_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = second_six_row_saturation_real_string_terminal_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "second six-row terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "second_six_row_saturation_real_string_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 10, "second six-row terminal layer degree count")
    require_equal(in_base_count, 0, "second six-row terminal layer in-base count")
    require_equal(nonzero_terminal_count, 0, "second six-row terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "second six-row terminal layer missing nonzero count")
    require_equal(missing_occurrences, 8, "second six-row terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 6, "second six-row terminal layer distinct saturation count")


def verify_second_six_row_saturation_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = second_six_row_saturation_real_string_saturation_extension_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "second six-row saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "second_six_row_saturation_real_string_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = second_six_row_saturation_base_betas(expected)
    terminal_rows = second_six_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 6, "second six-row saturation extension degree count")
    require_equal(total_occurrences, 8, "second six-row saturation extension occurrence count")
    require_equal(len(saturated_betas), 629, "second six-row saturated total degree count")
    require_equal(len(remaining_defects), 0, "second six-row saturation extension defect rank")


def verify_third_six_row_saturation_real_string_summary(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    require_equal(len(rows), 1, "third six-row real-string summary row count")
    row = rows[0]
    check_verified(row, "third_six_row_saturation_real_string_summary.csv")
    require_equal(row["summary_id"], "third_six_row_real_string", "third six-row real-string summary id")
    expected_summary = third_six_row_saturation_real_string_summary(expected)
    for key, expected_value in expected_summary.items():
        require_equal(int_cell(row, key), expected_value, f"third six-row summary {key}")
    require_equal(expected_summary["base_degree_count"], 629, "third six-row base degree count")
    require_equal(expected_summary["generator_degree_count"], 6, "third six-row generator count")
    require_equal(expected_summary["terminal_check_count"], 10, "third six-row terminal check count")
    require_equal(expected_summary["distinct_terminal_degree_count"], 10, "third six-row terminal degree count")
    require_equal(expected_summary["terminal_degree_in_base_count"], 0, "third six-row terminal in-base count")
    require_equal(expected_summary["new_terminal_degree_count"], 10, "third six-row new terminal count")
    require_equal(expected_summary["nonzero_terminal_degree_count"], 0, "third six-row nonzero terminal count")
    require_equal(expected_summary["missing_nonzero_terminal_degree_count"], 0, "third six-row missing nonzero count")
    require_equal(expected_summary["saturation_defect_parent_terminal_count"], 10, "third six-row defect parent count")
    require_equal(expected_summary["saturation_defect_occurrence_count"], 18, "third six-row defect occurrence count")
    require_equal(expected_summary["saturation_defect_distinct_degree_count"], 6, "third six-row distinct defect count")


def verify_third_six_row_saturation_real_string_obligations(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    obligations = third_six_row_saturation_real_string_expected_obligations(expected)
    by_check = rows_by_id(rows, "check_id")
    require_equal(set(by_check), set(obligations), "third six-row real-string obligation coverage")
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for check_id, obligation in obligations.items():
        row = by_check[check_id]
        check_verified(row, "third_six_row_saturation_real_string_obligations.csv")
        extension_beta = obligation["extension_beta"]
        terminal_beta = obligation["terminal_beta"]
        terminal_gamma = obligation["terminal_gamma"]
        assert isinstance(extension_beta, tuple)
        assert isinstance(terminal_beta, tuple)
        assert isinstance(terminal_gamma, tuple)
        require_equal(row["real_root_id"], obligation["real_root_id"], f"{check_id} real root")
        require_equal(row["extension_degree_id"], obligation["extension_degree_id"], f"{check_id} extension degree")
        require_equal(int_cell(row, "extension_beta_c1"), extension_beta[0], f"{check_id} extension beta c1")
        require_equal(int_cell(row, "extension_beta_c2"), extension_beta[1], f"{check_id} extension beta c2")
        require_equal(int_cell(row, "extension_beta_c3"), extension_beta[2], f"{check_id} extension beta c3")
        require_equal(int_cell(row, "pairing"), obligation["pairing"], f"{check_id} pairing")
        require_equal(int_cell(row, "serre_exponent"), obligation["serre_exponent"], f"{check_id} exponent")
        require_equal(int_cell(row, "terminal_beta_c1"), terminal_beta[0], f"{check_id} terminal beta c1")
        require_equal(int_cell(row, "terminal_beta_c2"), terminal_beta[1], f"{check_id} terminal beta c2")
        require_equal(int_cell(row, "terminal_beta_c3"), terminal_beta[2], f"{check_id} terminal beta c3")
        require_equal(int_cell(row, "terminal_gamma_n"), terminal_gamma[0], f"{check_id} terminal gamma n")
        require_equal(int_cell(row, "terminal_gamma_l"), terminal_gamma[1], f"{check_id} terminal gamma l")
        require_equal(int_cell(row, "terminal_gamma_m"), terminal_gamma[2], f"{check_id} terminal gamma m")
        require_equal(int_cell(row, "terminal_height"), obligation["terminal_height"], f"{check_id} terminal height")
        require_equal(int_cell(row, "terminal_norm"), obligation["terminal_norm"], f"{check_id} terminal norm")
        terminal_signed = int(obligation["terminal_signed_dimension"])
        terminal_in_base = bool(obligation["terminal_in_base"])
        require_equal(int_cell(row, "terminal_signed_dimension"), terminal_signed, f"{check_id} terminal signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{check_id} terminal in base")
        require_equal(row["relation_payload_status"], obligation["relation_payload_status"], f"{check_id} relation status")
        if terminal_in_base:
            in_base_count += 1
        if terminal_signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and terminal_signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(obligations), 10, "third six-row obligation count")
    require_equal(in_base_count, 0, "third six-row obligation in-base count")
    require_equal(nonzero_terminal_count, 0, "third six-row obligation nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "third six-row obligation missing nonzero count")


def verify_third_six_row_saturation_real_string_terminal_layer(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = third_six_row_saturation_real_string_terminal_rows(expected)
    by_degree = rows_by_id(rows, "terminal_degree_id")
    require_equal(set(by_degree), set(expected_rows), "third six-row terminal layer coverage")
    missing_occurrences = 0
    distinct_missing: set[tuple[int, int, int]] = set()
    in_base_count = 0
    nonzero_terminal_count = 0
    missing_nonzero_terminal_count = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "third_six_row_saturation_real_string_terminal_layer.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        missing = expected_row["missing_nonzero_subdegrees"]
        source_check_ids = expected_row["source_check_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(missing, list)
        assert isinstance(source_check_ids, list)
        require_equal(row["source_check_ids"], ";".join(source_check_ids), f"{degree_id} source checks")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        signed = int(expected_row["signed_dimension"])
        terminal_in_base = bool(expected_row["terminal_in_base"])
        require_equal(int_cell(row, "signed_dimension"), signed, f"{degree_id} signed")
        require_equal(bool_cell(row, "terminal_in_base"), terminal_in_base, f"{degree_id} terminal in base")
        require_equal(int_cell(row, "source_obligation_count"), len(source_check_ids), f"{degree_id} source count")
        require_equal(int_cell(row, "missing_nonzero_subdegree_count"), len(missing), f"{degree_id} missing count")
        require_equal(
            row["missing_nonzero_subdegree_ids"],
            ";".join(beta_degree_id(subdegree) for subdegree in missing),
            f"{degree_id} missing ids",
        )
        missing_occurrences += len(missing)
        distinct_missing.update(missing)
        if terminal_in_base:
            in_base_count += 1
        if signed != 0:
            nonzero_terminal_count += 1
        if not terminal_in_base and signed != 0:
            missing_nonzero_terminal_count += 1
    require_equal(len(expected_rows), 10, "third six-row terminal layer degree count")
    require_equal(in_base_count, 0, "third six-row terminal layer in-base count")
    require_equal(nonzero_terminal_count, 0, "third six-row terminal layer nonzero count")
    require_equal(missing_nonzero_terminal_count, 0, "third six-row terminal layer missing nonzero count")
    require_equal(missing_occurrences, 18, "third six-row terminal layer saturation occurrence count")
    require_equal(len(distinct_missing), 6, "third six-row terminal layer distinct saturation count")


def verify_third_six_row_saturation_real_string_saturation_extension(
    rows: list[dict[str, str]],
    expected: dict[str, ExpectedDegree],
) -> None:
    expected_rows = third_six_row_saturation_real_string_saturation_extension_rows(expected)
    by_degree = rows_by_id(rows, "degree_id")
    require_equal(set(by_degree), set(expected_rows), "third six-row saturation extension coverage")
    total_occurrences = 0
    for degree_id, expected_row in expected_rows.items():
        row = by_degree[degree_id]
        check_verified(row, "third_six_row_saturation_real_string_saturation_extension.csv")
        beta_value = expected_row["beta"]
        gamma = expected_row["gamma"]
        parent_ids = expected_row["parent_terminal_degree_ids"]
        assert isinstance(beta_value, tuple)
        assert isinstance(gamma, tuple)
        assert isinstance(parent_ids, list)
        require_equal(row["parent_terminal_degree_ids"], ";".join(parent_ids), f"{degree_id} parent terminal ids")
        require_equal(int_cell(row, "beta_c1"), beta_value[0], f"{degree_id} beta c1")
        require_equal(int_cell(row, "beta_c2"), beta_value[1], f"{degree_id} beta c2")
        require_equal(int_cell(row, "beta_c3"), beta_value[2], f"{degree_id} beta c3")
        require_equal(int_cell(row, "gamma_n"), gamma[0], f"{degree_id} gamma n")
        require_equal(int_cell(row, "gamma_l"), gamma[1], f"{degree_id} gamma l")
        require_equal(int_cell(row, "gamma_m"), gamma[2], f"{degree_id} gamma m")
        require_equal(int_cell(row, "height"), expected_row["height"], f"{degree_id} height")
        require_equal(int_cell(row, "norm"), expected_row["norm"], f"{degree_id} norm")
        require_equal(int_cell(row, "signed_dimension"), expected_row["signed_dimension"], f"{degree_id} signed")
        require_equal(int_cell(row, "parent_terminal_count"), len(parent_ids), f"{degree_id} parent count")
        require_equal(int_cell(row, "defect_occurrence_count"), len(parent_ids), f"{degree_id} occurrence count")
        require_equal(row["coverage_role"], expected_row["coverage_role"], f"{degree_id} coverage role")
        total_occurrences += len(parent_ids)

    base_betas = third_six_row_saturation_base_betas(expected)
    terminal_rows = third_six_row_saturation_real_string_terminal_rows(expected)
    terminal_betas = {
        terminal_row["beta"]
        for terminal_row in terminal_rows.values()
        if isinstance(terminal_row["beta"], tuple)
    }
    extension_betas = {
        expected_row["beta"]
        for expected_row in expected_rows.values()
        if isinstance(expected_row["beta"], tuple)
    }
    saturated_betas = base_betas | terminal_betas | extension_betas
    phi = phi_01_coefficients()
    remaining_defects = [
        subdegree
        for degree in saturated_betas
        for subdegree in proper_subdegrees(degree)
        if signed_root_supermultiplicity(phi, subdegree) != 0
        and subdegree not in saturated_betas
    ]
    require_equal(len(expected_rows), 6, "third six-row saturation extension degree count")
    require_equal(total_occurrences, 18, "third six-row saturation extension occurrence count")
    require_equal(len(saturated_betas), 645, "third six-row saturated total degree count")
    require_equal(len(remaining_defects), 0, "third six-row saturation extension defect rank")


def verify_firewall(rows: list[dict[str, str]]) -> None:
    seen: set[str] = set()
    for row in rows:
        check_verified(row, "source_firewall.csv")
        substitute = row["forbidden_substitute"]
        seen.add(substitute)
        require_equal(bool_cell(row, "excluded"), True, f"{substitute} excluded")
        require_equal(int_cell(row, "defect_rank"), 0, f"{substitute} defect_rank")
    missing = REQUIRED_FIREWALL_ROWS - seen
    if missing:
        raise ValueError(f"source_firewall.csv missing rows: {sorted(missing)}")


_runtime_layer_cache: dict[tuple[str, int], object] = {}


def install_runtime_layer_cache() -> None:
    """Memoize deterministic one-argument layer constructors during a verifier run."""
    cacheable_suffixes = (
        "_base_betas",
        "_expected_obligations",
        "_rows",
        "_saturated_betas",
        "_summary",
    )
    for name, func in list(globals().items()):
        if name.startswith("verify_") or not name.endswith(cacheable_suffixes):
            continue
        if not callable(func) or getattr(func, "_uses_runtime_layer_cache", False):
            continue
        try:
            parameters = list(inspect.signature(func).parameters.values())
        except (TypeError, ValueError):
            continue
        if len(parameters) != 1 or parameters[0].name != "expected":
            continue

        def cached(expected: dict[str, ExpectedDegree], *, _name=name, _func=func):
            key = (_name, id(expected))
            if key not in _runtime_layer_cache:
                _runtime_layer_cache[key] = _func(expected)
            return _runtime_layer_cache[key]

        cached._uses_runtime_layer_cache = True  # type: ignore[attr-defined]
        globals()[name] = cached


def main() -> int:
    args = parse_args()
    try:
        manifest = read_manifest(args.fixture)
        verify_manifest(manifest)
        tables = {spec.path: read_table(args.fixture, spec) for spec in TABLE_SPECS}
        expected = expected_degrees()
        install_runtime_layer_cache()
        wle3_ids, a071_ids = read_external_degree_ids(args.wle3_fixture, args.a071_fixture)
        window_rows = rows_by_id(tables["target_window_rows.csv"], "degree_id")
        verify_window_rows(window_rows, expected, wle3_ids, a071_ids)
        verify_closure_generators(tables["closure_generators.csv"], window_rows)
        verify_terminal_relations(tables["terminal_relation_checks.csv"], window_rows)
        verify_downward_saturation(tables["downward_saturation.csv"], expected)
        verify_saturation_extension(tables["saturation_extension.csv"], expected, a071_ids)
        verify_post_saturation_real_string_obligations(
            tables["post_saturation_real_string_obligations.csv"], expected
        )
        verify_post_saturation_terminal_layer(
            tables["post_saturation_terminal_layer.csv"], expected
        )
        verify_terminal_layer_saturation_extension(
            tables["terminal_layer_saturation_extension.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_obligations(
            tables["terminal_layer_saturation_real_string_obligations.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_summary(
            tables["terminal_layer_saturation_real_string_defect_summary.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer(
            tables["terminal_layer_saturation_real_string_defect_layer.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_summary(
            tables["terminal_layer_saturation_real_string_defect_layer_real_string_summary.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_obligations(
            tables["terminal_layer_saturation_real_string_defect_layer_real_string_obligations.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer(
            tables["terminal_layer_saturation_real_string_defect_layer_real_string_terminal_layer.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension(
            tables["terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension.csv"], expected
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary(
            tables[
                "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_summary.csv"
            ],
            expected,
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_obligations(
            tables[
                "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_obligations.csv"
            ],
            expected,
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer(
            tables[
                "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_terminal_layer.csv"
            ],
            expected,
        )
        verify_terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension(
            tables[
                "terminal_layer_saturation_real_string_defect_layer_real_string_saturation_extension_real_string_saturation_extension.csv"
            ],
            expected,
        )
        verify_twelve_row_saturation_real_string_summary(
            tables["twelve_row_saturation_real_string_summary.csv"], expected
        )
        verify_twelve_row_saturation_real_string_obligations(
            tables["twelve_row_saturation_real_string_obligations.csv"], expected
        )
        verify_twelve_row_saturation_real_string_terminal_layer(
            tables["twelve_row_saturation_real_string_terminal_layer.csv"], expected
        )
        verify_twelve_row_saturation_real_string_saturation_extension(
            tables["twelve_row_saturation_real_string_saturation_extension.csv"], expected
        )
        verify_six_row_saturation_real_string_summary(
            tables["six_row_saturation_real_string_summary.csv"], expected
        )
        verify_six_row_saturation_real_string_obligations(
            tables["six_row_saturation_real_string_obligations.csv"], expected
        )
        verify_six_row_saturation_real_string_terminal_layer(
            tables["six_row_saturation_real_string_terminal_layer.csv"], expected
        )
        verify_six_row_saturation_real_string_saturation_extension(
            tables["six_row_saturation_real_string_saturation_extension.csv"], expected
        )
        verify_second_six_row_saturation_real_string_summary(
            tables["second_six_row_saturation_real_string_summary.csv"], expected
        )
        verify_second_six_row_saturation_real_string_obligations(
            tables["second_six_row_saturation_real_string_obligations.csv"], expected
        )
        verify_second_six_row_saturation_real_string_terminal_layer(
            tables["second_six_row_saturation_real_string_terminal_layer.csv"], expected
        )
        verify_second_six_row_saturation_real_string_saturation_extension(
            tables["second_six_row_saturation_real_string_saturation_extension.csv"], expected
        )
        verify_third_six_row_saturation_real_string_summary(
            tables["third_six_row_saturation_real_string_summary.csv"], expected
        )
        verify_third_six_row_saturation_real_string_obligations(
            tables["third_six_row_saturation_real_string_obligations.csv"], expected
        )
        verify_third_six_row_saturation_real_string_terminal_layer(
            tables["third_six_row_saturation_real_string_terminal_layer.csv"], expected
        )
        verify_third_six_row_saturation_real_string_saturation_extension(
            tables["third_six_row_saturation_real_string_saturation_extension.csv"], expected
        )
        verify_firewall(tables["source_firewall.csv"])
    except Exception as exc:  # noqa: BLE001 - command-line verifier
        print(f"WREL_DEGREE_CLOSURE_FAILED: {exc}", file=sys.stderr)
        return 1
    print(SUCCESS_STATUS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
