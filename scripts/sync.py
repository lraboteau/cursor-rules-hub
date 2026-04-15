#!/usr/bin/env python3
"""
Cross-platform sync: copy a generated template into a consumer .cursorrules file.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
COMPOSE_SCRIPT = REPO_ROOT / "scripts" / "compose.py"

EXIT_VALIDATION = 1
EXIT_FILE_ERROR = 2


def resolve_template(arg: str) -> Path:
    raw = arg.strip()
    p = Path(raw)
    if p.is_file():
        return p.resolve()
    name = raw
    if not name.endswith(".cursorrules"):
        name = f"{name}.cursorrules"
    candidate = (TEMPLATES_DIR / Path(name).name).resolve()
    if candidate.is_file():
        return candidate
    raise FileNotFoundError(f"template not found: {arg}")


def list_templates() -> list[Path]:
    if not TEMPLATES_DIR.is_dir():
        return []
    return sorted(TEMPLATES_DIR.glob("*.cursorrules"))


def parse_target(target: str) -> Path:
    t = Path(target)
    if t.is_dir():
        return (t / ".cursorrules").resolve()
    return t.resolve()


def run_compose_first() -> None:
    cmd = [sys.executable, str(COMPOSE_SCRIPT), "--all"]
    subprocess.run(cmd, check=True, cwd=str(REPO_ROOT))


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Sync a template into a .cursorrules file.")
    parser.add_argument("target", nargs="?", help="project directory or output file path")
    parser.add_argument("template", nargs="?", help="template name or path to .cursorrules")
    parser.add_argument("--list", action="store_true", help="list available templates")
    parser.add_argument("--yes", "-y", action="store_true", help="overwrite without prompting")
    parser.add_argument("--backup", action="store_true", help="keep a .bak copy when overwriting")
    parser.add_argument("--no-backup", action="store_true", help="do not write a backup file")
    parser.add_argument(
        "--compose-first",
        action="store_true",
        help="run compose --all before resolving the template",
    )
    args = parser.parse_args(argv)

    if args.backup and args.no_backup:
        print("sync: error: --backup and --no-backup are mutually exclusive", file=sys.stderr)
        return EXIT_VALIDATION

    try:
        if args.compose_first:
            run_compose_first()
    except subprocess.CalledProcessError as exc:
        print(f"sync: compose failed with exit code {exc.returncode}", file=sys.stderr)
        return EXIT_VALIDATION
    except OSError as exc:
        print(f"sync: compose file error: {exc}", file=sys.stderr)
        return EXIT_FILE_ERROR

    if args.list:
        paths = list_templates()
        if not paths:
            print("No templates found. Run: python scripts/compose.py --all", file=sys.stderr)
            return EXIT_VALIDATION
        for p in paths:
            print(p.stem)
        return 0

    if not args.target or not args.template:
        parser.error("target and template are required unless using --list")

    try:
        dest = parse_target(args.target)
        src = resolve_template(args.template)
    except (ValueError, FileNotFoundError) as exc:
        print(f"sync: error: {exc}", file=sys.stderr)
        return EXIT_VALIDATION

    if dest.exists() and not args.yes:
        try:
            reply = input(f"Overwrite {dest}? [y/N] ").strip().lower()
        except EOFError:
            reply = ""
        if reply not in ("y", "yes"):
            print("Aborted.")
            return EXIT_VALIDATION

    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and args.backup and not args.no_backup:
            bak = dest.with_suffix(dest.suffix + ".bak")
            shutil.copy2(dest, bak)
        shutil.copy2(src, dest)
    except OSError as exc:
        print(f"sync: file error: {exc}", file=sys.stderr)
        return EXIT_FILE_ERROR

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
