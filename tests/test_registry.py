"""Registry consistency lint must pass on the repo itself."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import check_registry_consistency  # noqa: E402


def test_repo_registry_is_consistent(capsys):
    assert check_registry_consistency.main([str(ROOT)]) == 0, capsys.readouterr().out
