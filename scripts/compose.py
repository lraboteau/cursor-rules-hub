#!/usr/bin/env python3
"""
Deterministic compose: manifests + modules -> templates/*.cursorrules
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def layout(root: Path | None = None) -> tuple[Path, Path, Path, Path]:
    r = root or REPO_ROOT
    return r / "modules", r / "manifests", r / "templates", r / "core" / "identity.md"


MODULES_DIR, MANIFESTS_DIR, TEMPLATES_DIR, CORE_FILE = layout()

LAYER_RANK: dict[str, int] = {
    "stack-base": 0,
    "stack-extension": 1,
    "cross-cutting": 2,
}
CORE_RANK = -1

ALLOWED_TYPES = frozenset(LAYER_RANK.keys())


class ComposeError(Exception):
    """Validation or IO error during compose (exit code 1)."""


def normalize_title(title: str) -> str:
    return " ".join(title.strip().split())


def parse_sections(text: str, *, source: str) -> list[tuple[str, str]]:
    """Split markdown into (title, body) using level-1 ATX headings only."""
    lines = text.splitlines()
    # Trim leading blank lines; first non-empty line must start a level-1 section
    while lines and not lines[0].strip():
        lines.pop(0)
    first = lines[0] if lines else ""
    if not first.startswith("# ") or first.startswith("##"):
        raise ComposeError(
            f"{source}: first non-empty line must be a level-1 heading (# Title), not {first!r}"
        )

    sections: list[tuple[str, str]] = []
    current_title: str | None = None
    current_body: list[str] = []

    for line in lines:
        if line.startswith("# ") and not line.startswith("##"):
            if current_title is not None:
                sections.append((current_title, "\n".join(current_body).rstrip()))
            current_title = line[2:].strip()
            current_body = []
        else:
            current_body.append(line)

    if current_title is not None:
        sections.append((current_title, "\n".join(current_body).rstrip()))
    elif text.strip():
        raise ComposeError(f"{source}: no level-1 heading (# Title); modules must start with a # section")

    if not sections:
        raise ComposeError(f"{source}: empty or whitespace-only module")

    return sections


def validate_manifest(data: Any, *, path: Path) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ComposeError(f"{path}: manifest root must be a mapping")
    if data.get("version") != 1:
        raise ComposeError(f"{path}: version must be 1")
    template = data.get("template")
    if not isinstance(template, dict):
        raise ComposeError(f"{path}: template must be a mapping")
    tid = template.get("id")
    if not isinstance(tid, str) or not tid.strip():
        raise ComposeError(f"{path}: template.id must be a non-empty string")
    title = template.get("title")
    if not isinstance(title, str):
        raise ComposeError(f"{path}: template.title must be a string")

    core = data.get("core", True)
    if not isinstance(core, bool):
        raise ComposeError(f"{path}: core must be a boolean when set")

    priority = data.get("priority")
    if not isinstance(priority, list) or not priority:
        raise ComposeError(f"{path}: priority must be a non-empty list")

    for i, block in enumerate(priority):
        if not isinstance(block, dict):
            raise ComposeError(f"{path}: priority[{i}] must be a mapping")
        btype = block.get("type")
        if btype not in ALLOWED_TYPES:
            raise ComposeError(
                f"{path}: priority[{i}].type must be one of {sorted(ALLOWED_TYPES)}"
            )
        mods = block.get("modules")
        if not isinstance(mods, list) or not all(isinstance(m, str) for m in mods):
            raise ComposeError(f"{path}: priority[{i}].modules must be a list of strings")

    return data  # type: ignore[return-value]


@dataclass
class _SectionWin:
    body: str
    stream_index: int
    rank: int


def _module_path(ref: str, modules_dir: Path) -> Path:
    ref = ref.strip().strip("/\\")
    if ".." in ref.split("/") or ref.startswith("."):
        raise ComposeError(f"invalid module ref: {ref!r}")
    return modules_dir / f"{ref}.md"


def iter_manifest_modules(manifest: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for block in manifest["priority"]:
        out.extend(block["modules"])
    return out


def compose_content(
    manifest: dict[str, Any],
    *,
    manifest_path: Path,
    root: Path | None = None,
) -> tuple[str, list[str]]:
    """Return (file_text, ordered_module_refs_for_fingerprint)."""
    modules_dir, _, _, core_file = layout(root)
    include_core = manifest.get("core", True)
    merged: dict[str, _SectionWin] = {}
    stream_index = 0
    fingerprint_refs: list[str] = []

    def ingest_file(path: Path, rank: int, ref_label: str) -> None:
        nonlocal stream_index
        if not path.is_file():
            raise ComposeError(f"missing module file for {ref_label}: {path}")
        text = path.read_text(encoding="utf-8")
        fingerprint_refs.append(f"{ref_label}\n{text}")
        for title, body in parse_sections(text, source=str(path)):
            stream_index += 1
            key = normalize_title(title)
            prev = merged.get(key)
            if prev is None or rank > prev.rank or (rank == prev.rank and stream_index > prev.stream_index):
                merged[key] = _SectionWin(body=body, stream_index=stream_index, rank=rank)

    if include_core:
        if not core_file.is_file():
            raise ComposeError(f"missing core file: {core_file}")
        ingest_file(core_file, CORE_RANK, "core/identity.md")

    for block in manifest["priority"]:
        btype = block["type"]
        rank = LAYER_RANK[btype]
        for ref in block["modules"]:
            path = _module_path(ref, modules_dir)
            ingest_file(path, rank, ref)

    # Deterministic section order by stream_index of winning occurrence
    ordered = sorted(merged.items(), key=lambda kv: kv[1].stream_index)
    sections_md: list[str] = []
    for title, win in ordered:
        sections_md.append(f"# {title}\n\n{win.body}".rstrip())

    body = "\n\n".join(sections_md) + "\n"

    tid = manifest["template"]["id"]
    fp = hashlib.sha256()
    for chunk in fingerprint_refs:
        fp.update(chunk.encode("utf-8"))
        fp.update(b"\n")
    digest = fp.hexdigest()

    header_lines = [
        "<!--",
        "cursor-rules-hub: generated — do not edit by hand",
        f"manifest: {tid}",
        f"manifest-path: {manifest_path.as_posix()}",
        f"fingerprint: sha256:{digest}",
        "-->",
        "",
    ]
    return "".join(line + "\n" for line in header_lines) + body, iter_manifest_modules(manifest)


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ComposeError(f"{path}: invalid YAML: {exc}") from exc
    return validate_manifest(raw, path=path)


def compose_manifest_path(manifest_path: Path, *, write: bool, root: Path | None = None) -> str:
    root = root or REPO_ROOT
    _, _, templates_dir, _ = layout(root)
    manifest = load_manifest(manifest_path)
    tid = manifest["template"]["id"]
    out_path = templates_dir / f"{tid}.cursorrules"
    try:
        rel_mp = manifest_path.resolve().relative_to(root.resolve())
    except ValueError:
        rel_mp = manifest_path
    content, _ = compose_content(manifest, manifest_path=rel_mp, root=root)
    if write:
        templates_dir.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content.replace("\r\n", "\n"), encoding="utf-8")
    return content


def manifest_paths(root: Path | None = None) -> list[Path]:
    _, manifests_dir, _, _ = layout(root or REPO_ROOT)
    if not manifests_dir.is_dir():
        return []
    return sorted(manifests_dir.glob("*.yml"))


def run_all(*, write: bool, root: Path | None = None) -> list[Path]:
    r = root or REPO_ROOT
    _, manifests_dir, _, _ = layout(r)
    paths = manifest_paths(r)
    if not paths:
        raise ComposeError(f"no manifests found in {manifests_dir}")
    for mp in paths:
        compose_manifest_path(mp, write=write, root=r)
    return paths


def run_check(root: Path | None = None) -> None:
    r = root or REPO_ROOT
    _, manifests_dir, templates_dir, _ = layout(r)
    paths = manifest_paths(r)
    if not paths:
        raise ComposeError(f"no manifests found in {manifests_dir}")
    for mp in paths:
        manifest = load_manifest(mp)
        tid = manifest["template"]["id"]
        out_path = templates_dir / f"{tid}.cursorrules"
        try:
            rel_mp = mp.resolve().relative_to(r.resolve())
        except ValueError:
            rel_mp = mp
        expected, _ = compose_content(manifest, manifest_path=rel_mp, root=r)
        if not out_path.is_file():
            raise ComposeError(f"missing template output {out_path} (run compose --all)")
        actual = out_path.read_text(encoding="utf-8")
        if actual != expected:
            raise ComposeError(
                f"drift detected for {tid}: re-run `python scripts/compose.py --all` ({out_path})"
            )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compose Cursor rule templates from manifests.")
    parser.add_argument("--all", action="store_true", help="process all manifests/*.yml")
    parser.add_argument("--manifest", type=Path, help="single manifest file")
    parser.add_argument("--check", action="store_true", help="fail if templates differ from sources")
    args = parser.parse_args(argv)

    try:
        if args.check:
            run_check()
            return 0
        if args.all:
            run_all(write=True)
            return 0
        if args.manifest:
            mp = args.manifest if args.manifest.is_absolute() else (Path.cwd() / args.manifest)
            if not mp.is_file():
                mp = REPO_ROOT / args.manifest
            compose_manifest_path(mp.resolve(), write=True)
            return 0
        parser.error("specify --all, --manifest PATH, or --check")
    except ComposeError as exc:
        print(f"compose: error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"compose: file error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
