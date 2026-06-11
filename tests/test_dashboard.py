"""Dashboard generator tests — built from the golden fixture."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_dashboard  # noqa: E402

GOLDEN = ROOT / "examples" / "showcase" / "course_passport.yaml"


def test_dashboard_builds_and_covers_passport(tmp_path):
    out = build_dashboard.build(GOLDEN, tmp_path / "dash.html")
    doc = out.read_text(encoding="utf-8")
    p = yaml.safe_load(GOLDEN.read_text(encoding="utf-8"))
    # every id in the passport appears in the dashboard
    for o in p["learning_outcomes"]:
        assert o["id"] in doc
    for a in p["assessment_plan"]:
        assert a["id"] in doc
    for w in p["schedule"]:
        assert w["id"] in doc
    assert p["course"]["code"] in doc
    # golden fixture is clean: no missing-file flags, live re-check clean
    assert "⚠ missing" not in doc
    assert "clean right now" in doc


def test_dashboard_flags_missing_artifacts(tmp_path):
    p = yaml.safe_load(GOLDEN.read_text(encoding="utf-8"))
    p["artifacts"].append({"path": "nonexistent_file.md", "type": "lesson",
                           "produced_by": "lesson-builder", "stage": 2,
                           "confirmed_by_professor": False})
    mutated = tmp_path / "course_passport.yaml"
    mutated.write_text(yaml.safe_dump(p, allow_unicode=True), encoding="utf-8")
    doc = build_dashboard.build(mutated).read_text(encoding="utf-8")
    assert "⚠ missing" in doc and "nonexistent_file.md" in doc


def test_dashboard_surfaces_live_issues(tmp_path):
    p = yaml.safe_load(GOLDEN.read_text(encoding="utf-8"))
    p["learning_outcomes"][0]["assessed_by"] = []  # break alignment (A1)
    for a in p["assessment_plan"]:
        if p["learning_outcomes"][0]["id"] in a["outcomes_assessed"]:
            a["outcomes_assessed"].remove(p["learning_outcomes"][0]["id"])
    mutated = tmp_path / "course_passport.yaml"
    mutated.write_text(yaml.safe_dump(p, allow_unicode=True), encoding="utf-8")
    doc = build_dashboard.build(mutated).read_text(encoding="utf-8")
    assert "Live re-check found open issues" in doc and "A1" in doc
