from __future__ import annotations

import textwrap
from collections import defaultdict
from pathlib import Path

import pytest

import compose


def _write(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(textwrap.dedent(content).lstrip("\n"), encoding="utf-8")


def test_parse_sections_requires_level_one_heading(tmp_path: Path) -> None:
    bad = tmp_path / "bad.md"
    bad.write_text("## Nope\n", encoding="utf-8")
    with pytest.raises(compose.ComposeError):
        compose.parse_sections(bad.read_text(encoding="utf-8"), source=str(bad))


def test_merge_cross_cutting_wins_duplicate_title(tmp_path: Path) -> None:
    root = tmp_path
    _write(
        root / "core/identity.md",
        """
        # CoreOnly

        core body        """,
    )
    _write(
        root / "modules/stacks/base/x.md",
        """
        # Shared

        from base
        """,
    )
    _write(
        root / "modules/cross-cutting/y.md",
        """
        # Shared

        from cross        """,
    )
    _write(
        root / "manifests/t.yml",
        """
        version: 1
        core: false
        template:
          id: t
          title: T
        priority:
          - type: stack-base
            modules:
              - stacks/base/x
          - type: stack-extension
            modules: []
          - type: cross-cutting
            modules:
              - cross-cutting/y
        """,
    )
    manifest = compose.load_manifest(root / "manifests/t.yml")
    out, _ = compose.compose_content(
        manifest,
        manifest_path=Path("manifests/t.yml"),
        root=root,
    )
    assert "from cross" in out
    assert "from base" not in out


def test_compose_end_to_end_writes_template(tmp_path: Path) -> None:
    root = tmp_path
    _write(
        root / "core/identity.md",
        """
        # ZCore

        z
        """,
    )
    _write(
        root / "modules/m.md",
        """
        # Only

        body
        """,
    )
    _write(
        root / "manifests/m.yml",
        """
        version: 1
        template:
          id: mini
          title: Mini
        priority:
          - type: stack-base
            modules:
              - m
          - type: stack-extension
            modules: []
          - type: cross-cutting
            modules: []
        """,
    )
    compose.compose_manifest_path(root / "manifests/m.yml", write=True, root=root)
    out = (root / "templates/mini.cursorrules").read_text(encoding="utf-8")
    assert "ZCore" in out
    assert "body" in out
    compose.run_check(root=root)


def test_validate_manifest_rejects_bad_version(tmp_path: Path) -> None:
    bad = tmp_path / "b.yml"
    bad.write_text("version: 2\n", encoding="utf-8")
    with pytest.raises(compose.ComposeError):
        compose.load_manifest(bad)


def test_repo_module_titles_are_unique() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    modules_dir = repo_root / "modules"
    title_sources: dict[str, list[str]] = defaultdict(list)

    for path in sorted(modules_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        sections = compose.parse_sections(text, source=str(path))
        for title, _ in sections:
            key = compose.normalize_title(title)
            title_sources[key].append(str(path.relative_to(repo_root)))

    duplicates = {k: v for k, v in title_sources.items() if len(v) > 1}
    assert not duplicates, f"Duplicate top-level section titles detected: {duplicates}"
