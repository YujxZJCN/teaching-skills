"""Content-marker finalization check tests."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_content_markers as ccm  # noqa: E402

GOLDEN = ROOT / "examples" / "showcase" / "course_passport.yaml"


def test_finds_markers_in_showcase_artifacts():
    files = ccm.artifact_paths(GOLDEN)
    assert files, "should resolve artifact paths from the passport"
    findings = ccm.scan(files)
    # the showcase deliberately carries [VERIFY] and [NEEDS PROFESSOR INPUT] markers
    assert any(f["marker"].startswith("[VERIFY") for f in findings)
    assert any(f["marker"].startswith("[NEEDS") for f in findings)


def test_strict_flags_markers(tmp_path):
    f = tmp_path / "draft.md"
    f.write_text("# Syllabus\nLate policy: [NEEDS PROFESSOR INPUT: faculty handbook]\n", encoding="utf-8")
    assert ccm.main(["--files", str(f), "--strict"]) == 1


def test_clean_file_passes_strict(tmp_path):
    f = tmp_path / "clean.md"
    f.write_text("# Syllabus\nLate policy: 10% per day, capped at 3 days.\n", encoding="utf-8")
    assert ccm.main(["--files", str(f), "--strict"]) == 0
