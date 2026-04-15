from __future__ import annotations

import subprocess
from pathlib import Path


def _script_path() -> Path:
    repo = Path(__file__).resolve().parents[1]
    return repo / "scripts" / "install-cursorrules.sh"


def _file_base_url(repo: Path) -> str:
    return f"file://{repo.resolve()}"


def test_install_cursorrules_success(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    script = _script_path()
    proj = tmp_path / "proj"
    proj.mkdir()
    dest = proj / ".cursorrules"

    cmd = [
        "bash",
        str(script),
        "--template",
        "ruby",
        "--target",
        str(proj),
        "--owner-repo",
        "ignored/ignored",
        "--ref",
        "ignored",
        "--base-url",
        _file_base_url(repo),
        "--yes",
    ]
    subprocess.run(cmd, check=True, cwd=str(repo))
    assert dest.is_file()
    assert "cursor-rules-hub: generated" in dest.read_text(encoding="utf-8")


def test_install_cursorrules_backup(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    script = _script_path()
    proj = tmp_path / "proj"
    proj.mkdir()
    dest = proj / ".cursorrules"
    dest.write_text("old\n", encoding="utf-8")

    cmd = [
        "bash",
        str(script),
        "--template",
        "hono-workers",
        "--target",
        str(proj),
        "--owner-repo",
        "ignored/ignored",
        "--ref",
        "ignored",
        "--base-url",
        _file_base_url(repo),
        "--backup",
        "--yes",
    ]
    subprocess.run(cmd, check=True, cwd=str(repo))
    bak = proj / ".cursorrules.bak"
    assert bak.is_file()
    assert bak.read_text(encoding="utf-8") == "old\n"
    assert dest.read_text(encoding="utf-8") != "old\n"


def test_install_cursorrules_missing_template(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    script = _script_path()
    proj = tmp_path / "proj"
    proj.mkdir()

    cmd = [
        "bash",
        str(script),
        "--template",
        "does-not-exist",
        "--target",
        str(proj),
        "--owner-repo",
        "ignored/ignored",
        "--ref",
        "ignored",
        "--base-url",
        _file_base_url(repo),
        "--yes",
    ]
    proc = subprocess.run(cmd, cwd=str(repo), capture_output=True, text=True)
    assert proc.returncode == 1
    assert "unable to download template" in proc.stderr


def test_install_cursorrules_invalid_target(tmp_path: Path) -> None:
    repo = Path(__file__).resolve().parents[1]
    script = _script_path()
    bad_parent = tmp_path / "not_a_dir"
    bad_parent.write_text("x", encoding="utf-8")

    cmd = [
        "bash",
        str(script),
        "--template",
        "ruby",
        "--target",
        str(bad_parent / "nested"),
        "--owner-repo",
        "ignored/ignored",
        "--ref",
        "ignored",
        "--base-url",
        _file_base_url(repo),
        "--yes",
    ]
    proc = subprocess.run(cmd, cwd=str(repo), capture_output=True, text=True)
    assert proc.returncode == 2
    assert "cannot create destination directory" in proc.stderr
