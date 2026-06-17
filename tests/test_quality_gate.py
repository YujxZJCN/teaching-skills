"""Executable Quality Gate (3.5) tests."""

import copy
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_quality_gate as qg  # noqa: E402

GOLDEN = ROOT / "examples" / "showcase" / "course_passport.yaml"


@pytest.fixture()
def passport():
    return yaml.safe_load(GOLDEN.read_text(encoding="utf-8"))


def checks(p, path=GOLDEN):
    f, _ = qg.gate_findings(p, path)
    f, _ = qg.suppress_dismissed(f, p)
    return {x["check_id"] for x in f}, f


def test_golden_has_no_block_findings(passport):
    ids, f = checks(passport)
    blocks = [x for x in f if x["severity"] == "BLOCK"]
    assert not blocks, f"golden fixture should pass Q1/Q2/T1: {blocks}"


def test_q1_empty_ai_policy_blocks(passport):
    p = copy.deepcopy(passport)
    p["policies"]["ai_use_policy"] = ""
    ids, _ = checks(p)
    assert "Q1" in ids


def test_q2_unreviewed_assessment_blocks(passport):
    p = copy.deepcopy(passport)
    p["assessment_plan"][0]["ai_resilience"] = "not_reviewed"
    ids, f = checks(p)
    assert "Q2" in ids
    assert any(x["severity"] == "BLOCK" for x in f if x["check_id"] == "Q2")


def test_verdict_is_pass_or_warn_on_golden():
    assert qg.run(str(GOLDEN))["verdict"] in ("PASS", "PASS-WITH-WARNINGS")


def test_cli_runs():
    assert qg.main([str(GOLDEN)]) == 0
