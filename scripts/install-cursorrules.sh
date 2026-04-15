#!/usr/bin/env bash
set -euo pipefail

EXIT_VALIDATION=1
EXIT_FILE_ERROR=2

OWNER_REPO_DEFAULT="laurent/cursor-rules-hub"
REF_DEFAULT="main"
BASE_URL_DEFAULT="https://raw.githubusercontent.com"

template=""
target="."
ref="$REF_DEFAULT"
owner_repo="$OWNER_REPO_DEFAULT"
base_url="$BASE_URL_DEFAULT"
yes=0
backup=0

usage() {
  cat <<'EOF'
Install a generated .cursorrules template without cloning this repository.

Usage:
  install-cursorrules.sh --template NAME [--target PATH] [--ref REF] [--owner-repo OWNER/REPO]
                         [--base-url URL] [--backup] [--yes]

Options:
  --template NAME         Template short name (e.g. hono-cloudflare-workers) or file name.
  --target PATH           Project directory or explicit output file path. Default: .
  --ref REF               Git ref (branch/tag/SHA). Default: main
  --owner-repo OWNER/REPO GitHub owner/repo. Default: laurent/cursor-rules-hub
  --base-url URL          Base URL serving templates. Default: https://raw.githubusercontent.com
  --backup                Keep a .bak copy when overwriting.
  --yes, -y               Overwrite without prompting.
  -h, --help              Show this help.

Examples:
  install-cursorrules.sh --template hono-cloudflare-workers --target /path/to/new-project --yes
  install-cursorrules.sh --template ruby --target . --ref v1.0.0 --backup
EOF
}

die_validation() {
  echo "install-cursorrules: error: $*" >&2
  exit "$EXIT_VALIDATION"
}

die_file_error() {
  echo "install-cursorrules: file error: $*" >&2
  exit "$EXIT_FILE_ERROR"
}

is_output_file_path() {
  local p="$1"
  case "$p" in
    *.cursorrules) return 0 ;;
    *) return 1 ;;
  esac
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --template)
      shift
      [[ $# -gt 0 ]] || die_validation "--template requires a value"
      template="$1"
      ;;
    --target)
      shift
      [[ $# -gt 0 ]] || die_validation "--target requires a value"
      target="$1"
      ;;
    --ref)
      shift
      [[ $# -gt 0 ]] || die_validation "--ref requires a value"
      ref="$1"
      ;;
    --owner-repo)
      shift
      [[ $# -gt 0 ]] || die_validation "--owner-repo requires a value"
      owner_repo="$1"
      ;;
    --base-url)
      shift
      [[ $# -gt 0 ]] || die_validation "--base-url requires a value"
      base_url="$1"
      ;;
    --backup)
      backup=1
      ;;
    --yes|-y)
      yes=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die_validation "unknown argument: $1"
      ;;
  esac
  shift
done

[[ -n "$template" ]] || die_validation "--template is required"
[[ -n "$owner_repo" ]] || die_validation "--owner-repo must be non-empty"
[[ -n "$ref" ]] || die_validation "--ref must be non-empty"

template_file="$template"
if [[ "$template_file" != *.cursorrules ]]; then
  template_file="${template_file}.cursorrules"
fi
template_file="$(basename "$template_file")"

dest="$target"
if [[ -d "$target" ]]; then
  dest="${target%/}/.cursorrules"
elif ! is_output_file_path "$target"; then
  dest="${target%/}/.cursorrules"
fi

if [[ "$base_url" == file://* ]]; then
  url="${base_url%/}/templates/${template_file}"
else
  url="${base_url%/}/${owner_repo}/${ref}/templates/${template_file}"
fi

tmp="$(mktemp)"
cleanup() {
  rm -f "$tmp"
}
trap cleanup EXIT

if ! curl -fsSL "$url" -o "$tmp"; then
  die_validation "unable to download template from $url"
fi

if [[ -f "$dest" && "$yes" -eq 0 ]]; then
  read -r -p "Overwrite $dest? [y/N] " reply || reply=""
  reply="${reply,,}"
  if [[ "$reply" != "y" && "$reply" != "yes" ]]; then
    echo "Aborted."
    exit "$EXIT_VALIDATION"
  fi
fi

dest_dir="$(dirname "$dest")"
if ! mkdir -p "$dest_dir"; then
  die_file_error "cannot create destination directory: $dest_dir"
fi

if [[ -f "$dest" && "$backup" -eq 1 ]]; then
  if ! cp -f "$dest" "${dest}.bak"; then
    die_file_error "cannot create backup file: ${dest}.bak"
  fi
fi

if ! cp -f "$tmp" "$dest"; then
  die_file_error "cannot write destination file: $dest"
fi

echo "Installed ${template_file} to ${dest}"
