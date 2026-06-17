"""Adoption tooling tests: LMS export validity + document renderer degradation."""

import sys
import xml.dom.minidom as minidom
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import export_lms  # noqa: E402
import render_document  # noqa: E402

SAMPLE = {
    "title": "Test Quiz",
    "questions": [
        {"type": "multiple_choice", "prompt": "1+1?", "choices": ["1", "2", "3"], "answer": 1},
        {"type": "multiple_answer", "prompt": "evens?", "choices": ["1", "2", "4"], "answer": [1, 2]},
        {"type": "true_false", "prompt": "Sky is blue.", "answer": True},
        {"type": "short_answer", "prompt": "Capital of France?", "answers": ["Paris"]},
        {"type": "essay", "prompt": "Discuss.", "points": 10},
    ],
}


@pytest.fixture()
def data():
    return export_lms.load_from_obj(SAMPLE) if hasattr(export_lms, "load_from_obj") else _prep(SAMPLE)


def _prep(obj):
    import copy
    d = copy.deepcopy(obj)
    for i, q in enumerate(d["questions"]):
        q.setdefault("id", f"q{i+1}")
        q.setdefault("points", 1)
    return d


def test_gift_export_covers_all_types(data):
    gift = export_lms.to_gift(data)
    assert "::q1::" in gift and "=2" in gift          # MC correct marked
    assert "TRUE" in gift                              # true_false
    assert "=Paris" in gift                            # short_answer
    assert gift.count("{") == 5                         # one block per question


def test_qti_zip_is_valid_and_wellformed(tmp_path):
    out = tmp_path / "q.zip"
    export_lms.to_qti_zip(_prep(SAMPLE), out)
    z = zipfile.ZipFile(out)
    assert z.testzip() is None
    assert "imsmanifest.xml" in z.namelist()
    for n in z.namelist():
        if n.endswith(".xml"):
            minidom.parseString(z.read(n))  # raises on malformed


def test_imscc_is_valid_package(tmp_path):
    out = tmp_path / "c.imscc"
    export_lms.to_imscc(_prep(SAMPLE), out, None)
    z = zipfile.ZipFile(out)
    assert z.testzip() is None
    assert "imsmanifest.xml" in z.namelist()
    assert any(n.endswith("syllabus.html") for n in z.namelist())
    minidom.parseString(z.read("imsmanifest.xml"))


def test_unsupported_type_rejected(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text('{"questions":[{"type":"matching","prompt":"x"}]}', encoding="utf-8")
    with pytest.raises(ValueError):
        export_lms.load(bad)


def test_renderer_degrades_honestly_without_pandoc(monkeypatch, tmp_path):
    # simulate no pandoc: render returns 0 (honest fallback), produces no file
    monkeypatch.setattr(render_document, "detect", lambda: {"pandoc": False, "pdf_engines": []})
    src = tmp_path / "syllabus.md"
    src.write_text("# Syllabus\n", encoding="utf-8")
    rc = render_document.render(src, "docx", tmp_path / "out.docx")
    assert rc == 0
    assert not (tmp_path / "out.docx").exists()
