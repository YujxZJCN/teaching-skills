"""Validator tests.

The showcase passport (examples/showcase/course_passport.yaml) is the golden
fixture: it was hand-verified for cross-file consistency and must always pass
both validators cleanly. Mutation tests then break it in targeted ways and
assert that the specific check fires — so a regression in a check shows up as
a named failure, not a silent pass.
"""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_passport  # noqa: E402
import check_alignment_gate  # noqa: E402

GOLDEN = ROOT / "examples" / "showcase" / "course_passport.yaml"


@pytest.fixture()
def passport():
    return yaml.safe_load(GOLDEN.read_text(encoding="utf-8"))


def passport_checks(p):
    findings = check_passport.schema_findings(p, check_passport.DEFAULT_SCHEMA)
    findings += check_passport.crossref_findings(p)
    return {f["check_id"] for f in findings}, findings


def gate_checks(p):
    findings, nev = check_alignment_gate.gate_findings(p)
    findings, _ = check_alignment_gate.suppress_dismissed(findings, p)
    return {f["check_id"] for f in findings}, findings, nev


# --- golden fixture ---------------------------------------------------------

def test_golden_passport_is_valid(passport):
    ids, findings = passport_checks(passport)
    assert not findings, f"golden fixture should be clean, got: {findings}"


def test_golden_passport_passes_gate(passport):
    ids, findings, _ = gate_checks(passport)
    blocks = [f for f in findings if f["severity"] == "BLOCK"]
    assert not blocks, f"golden fixture must have no BLOCK findings: {blocks}"


def test_cli_end_to_end():
    assert check_passport.main([str(GOLDEN)]) == 0
    assert check_alignment_gate.main([str(GOLDEN)]) == 0


# --- schema mutations -------------------------------------------------------

def test_schema_catches_bad_bloom_level(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][0]["bloom_level"] = "memorize"
    ids, _ = passport_checks(p)
    assert "SCHEMA" in ids


def test_schema_catches_bad_gate_status(passport):
    p = copy.deepcopy(passport)
    p["gates"]["alignment_gate"]["status"] = "skipped"
    ids, _ = passport_checks(p)
    assert "SCHEMA" in ids


def test_schema_catches_bad_id_pattern(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][0]["id"] = "OUTCOME-1"
    ids, _ = passport_checks(p)
    assert "SCHEMA" in ids


# --- cross-reference mutations ----------------------------------------------

def test_p4_mirror_break_fires(passport):
    p = copy.deepcopy(passport)
    # remove one side of the LO<->assessment mirror
    lo = p["learning_outcomes"][0]
    removed = lo["assessed_by"].pop()
    ids, findings = passport_checks(p)
    assert "P4" in ids
    assert any(removed in f["affected_ids"] for f in findings if f["check_id"] == "P4")


def test_p2_missing_assessment_ref_fires(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][0]["assessed_by"].append("A99")
    ids, _ = passport_checks(p)
    assert "P2" in ids


def test_p7_schedule_mirror_break_fires(passport):
    p = copy.deepcopy(passport)
    for w in p["schedule"]:
        if w.get("outcomes"):
            w["outcomes"].pop()
            break
    ids, _ = passport_checks(p)
    assert "P7" in ids


def test_p9_weight_sum_fires(passport):
    p = copy.deepcopy(passport)
    p["assessment_plan"][0]["weight"] += 5
    ids, _ = passport_checks(p)
    assert "P9" in ids


def test_p1_duplicate_id_fires(passport):
    p = copy.deepcopy(passport)
    p["assessment_plan"][1]["id"] = p["assessment_plan"][0]["id"]
    ids, _ = passport_checks(p)
    assert "P1" in ids


# --- alignment gate mutations -------------------------------------------------

def test_a1_unassessed_outcome_blocks(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][0]["assessed_by"] = []
    ids, findings, _ = gate_checks(p)
    assert "A1" in ids
    assert any(f["severity"] == "BLOCK" for f in findings if f["check_id"] == "A1")


def test_a2_untaught_outcome_blocks(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][2]["taught_in"] = []
    ids, _, _ = gate_checks(p)
    assert "A2" in ids


def test_a4_uncovered_week_warns(passport):
    p = copy.deepcopy(passport)
    for w in p["schedule"]:
        if w.get("outcomes"):
            w["outcomes"] = []
            w.pop("tag", None)
            break
    ids, _, _ = gate_checks(p)
    assert "A4" in ids


def test_a4_logistics_week_does_not_warn(passport):
    ids, _, _ = gate_checks(passport)
    assert "A4" not in ids  # golden has logistics-tagged empty weeks


def test_b1_banned_verb_warns(passport):
    p = copy.deepcopy(passport)
    p["learning_outcomes"][0]["statement"] = "Understand the basics of machine learning"
    ids, _, _ = gate_checks(p)
    assert "B1" in ids


def test_c1_weight_sum_blocks(passport):
    p = copy.deepcopy(passport)
    p["assessment_plan"][0]["weight"] = 90
    ids, findings, _ = gate_checks(p)
    assert "C1" in ids
    assert "C2" in ids  # 90 also exceeds the single-assessment cap


def test_c4_create_outcome_on_exam_only_warns(passport):
    p = copy.deepcopy(passport)
    create_lo = next(o for o in p["learning_outcomes"] if o["bloom_level"] == "create")
    exam_ids = [a["id"] for a in p["assessment_plan"] if a["type"] in ("exam", "quiz")]
    create_lo["assessed_by"] = exam_ids[:1]
    for a in p["assessment_plan"]:
        if a["id"] in exam_ids[:1]:
            if create_lo["id"] not in a["outcomes_assessed"]:
                a["outcomes_assessed"].append(create_lo["id"])
        elif create_lo["id"] in a["outcomes_assessed"]:
            a["outcomes_assessed"].remove(create_lo["id"])
    ids, _, _ = gate_checks(p)
    assert "C4" in ids


def test_d1_missing_workload_blocks(passport):
    p = copy.deepcopy(passport)
    p["workload_audit"]["estimated_hours_per_week"] = None
    ids, _, _ = gate_checks(p)
    assert "D1" in ids


def test_d2_overload_warns(passport):
    p = copy.deepcopy(passport)
    p["workload_audit"]["estimated_hours_per_week"] = 12.0
    ids, _, _ = gate_checks(p)
    assert "D2" in ids


def test_d3_deliverable_collision_warns(passport):
    p = copy.deepcopy(passport)
    # move the final exam due-week onto the project's final milestone week
    for w in p["schedule"]:
        if "A6" in (w.get("assessments_due") or []):
            w["assessments_due"].remove("A6")
    for w in p["schedule"]:
        if "A4" in (w.get("assessments_due") or []):
            w["assessments_due"].append("A6")
            break
    ids, _, _ = gate_checks(p)
    assert "D3" in ids


def test_dismissed_findings_are_suppressed(passport):
    p = copy.deepcopy(passport)
    # create a C2 violation, then dismiss exactly that finding
    p["assessment_plan"][3]["weight"] = 45
    p["assessment_plan"][0]["weight"] -= 15  # keep C1 quiet
    findings, _ = check_alignment_gate.gate_findings(p)
    c2 = next(f for f in findings if f["check_id"] == "C2")
    p["gates"]["alignment_gate"]["findings"].append({**c2, "dismissed": "professor accepted"})
    kept, _, _ = gate_checks(p)
    assert "C2" not in kept


def test_verdict_states():
    result = check_alignment_gate.run(str(GOLDEN))
    assert result["verdict"] in ("PASS", "PASS-WITH-WARNINGS")
