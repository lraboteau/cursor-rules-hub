from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import yaml


def _template_ids(repo: Path) -> list[str]:
    ids: list[str] = []
    for manifest_path in sorted((repo / "manifests").glob("*.yml")):
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
        ids.append(data["template"]["id"])
    return ids


def test_sync_copies_all_templates(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    for template_id in _template_ids(repo):
        proj = tmp_path / f"proj-{template_id}"
        proj.mkdir()
        dest = proj / ".cursorrules"
        src = repo / "templates" / f"{template_id}.cursorrules"
        assert src.is_file()
        cmd = [
            sys.executable,
            str(repo / "scripts" / "sync.py"),
            "--yes",
            str(proj),
            str(src),
        ]
        subprocess.run(cmd, check=True, cwd=str(repo))
        assert dest.is_file()
        assert dest.read_text(encoding="utf-8") == src.read_text(encoding="utf-8")


def test_sync_backup_creates_bak(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    proj = tmp_path / "proj"
    proj.mkdir()
    dest = proj / ".cursorrules"
    dest.write_text("old\n", encoding="utf-8")
    cmd = [
        sys.executable,
        str(repo / "scripts" / "sync.py"),
        "--yes",
        "--backup",
        str(proj),
        "ruby",
    ]
    subprocess.run(cmd, check=True, cwd=str(repo))
    bak = dest.with_suffix(dest.suffix + ".bak")
    assert bak.is_file()
    assert "old" in bak.read_text(encoding="utf-8")
    assert dest.read_text(encoding="utf-8") != "old\n"
