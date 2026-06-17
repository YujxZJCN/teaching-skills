"""Repo-integrity guards: internal links resolve, manifests/docs stay in sync,
and the showcase markdown agrees with its passport."""

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_links  # noqa: E402
import check_registry_consistency as crc  # noqa: E402

SHOWCASE = ROOT / "examples" / "showcase"


def test_internal_links_resolve():
    assert check_links.main([str(ROOT)]) == 0


def test_registry_and_manifests_consistent():
    # covers R1-R9: SKILL.md <-> MODE_REGISTRY <-> filesystem <-> plugin/marketplace JSON <-> ARCHITECTURE version
    assert crc.main([str(ROOT)]) == 0


def test_showcase_syllabus_matches_passport():
    p = yaml.safe_load((SHOWCASE / "course_passport.yaml").read_text(encoding="utf-8"))
    syllabus = (SHOWCASE / "syllabus.md").read_text(encoding="utf-8")
    assert p["course"]["code"] in syllabus
    # every confirmed outcome statement appears verbatim in the syllabus
    for o in p["learning_outcomes"]:
        assert o["statement"] in syllabus, f"syllabus missing outcome {o['id']}"


def test_showcase_artifact_refs_exist_on_disk():
    p = yaml.safe_load((SHOWCASE / "course_passport.yaml").read_text(encoding="utf-8"))
    for a in p.get("artifacts", []):
        if a.get("path"):
            assert (SHOWCASE / a["path"]).exists(), f"ledger lists missing file {a['path']}"
