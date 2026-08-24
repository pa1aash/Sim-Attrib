#!/usr/bin/env bash
# Build the Overleaf submission package for Sim-Attrib -> Sim2Science.
#
# Assembles an EXPLICIT ALLOWLIST of submission files (not a directory glob
# with exclusions) into build/sim_attrib_overleaf_<short-hash>.zip. The
# relative layout inside the zip mirrors the repo's own layout exactly
# (paper/ one level below figures/ and audit/BIBLIOGRAPHY.bib) because
# paper/main.tex's \includegraphics and \bibliography calls use ../-relative
# paths and this script does not edit main.tex to change that.
#
# Re-run this any time after editing paper/ or figures/ -- it is safe to run
# repeatedly and always rebuilds from the current working tree.

set -euo pipefail

REPO_ROOT="$HOME/Desktop/Sim-Attrib"
if [ "$(git -C "$REPO_ROOT" rev-parse --show-toplevel 2>/dev/null)" != "$REPO_ROOT" ]; then
  echo "FATAL: not the Sim-Attrib repo root ($REPO_ROOT). Refusing to run." >&2
  exit 1
fi
cd "$REPO_ROOT"

HASH="$(git rev-parse --short HEAD)"
BUILD_DIR="$REPO_ROOT/build"
STAGE_DIR="$BUILD_DIR/_stage"
ZIP_PATH="$BUILD_DIR/sim_attrib_overleaf_${HASH}.zip"

# --- Explicit allowlist: relative-path source -> same relative path in zip ---
# Every entry here is a deliberate inclusion decision, not a directory scan.
ALLOWLIST=(
  "paper/main.tex"
  "paper/checklist.tex"
  "paper/appendix_tables.tex"
  "paper/appendix_claims_table.tex"
  "paper/neurips_2026_template/neurips_2026.sty"
  "audit/BIBLIOGRAPHY.bib"
)

# Figures are not hand-enumerated: they are PARSED from \includegraphics calls
# in paper/main.tex, so a leftover unused figure file can never silently enter
# the package and a newly-referenced figure can never silently be missed.
FIGURES=()
while IFS= read -r fig; do
  FIGURES+=("figures/$(basename "$fig")")
done < <(grep -oE '\\includegraphics(\[[^]]*\])?\{[^}]*\}' paper/main.tex \
          | sed -E 's/.*\{//; s/\}$//' | xargs -n1 basename)

ALLOWLIST+=("${FIGURES[@]}")

echo "=== Sim-Attrib Overleaf package build ==="
echo "Repo:   $REPO_ROOT"
echo "Commit: $HASH"
echo "Output: $ZIP_PATH"
echo ""
echo "Allowlisted files (${#ALLOWLIST[@]}):"
printf '  %s\n' "${ALLOWLIST[@]}"
echo ""

# --- Verify every allowlisted file exists before touching anything ---
for f in "${ALLOWLIST[@]}"; do
  if [ ! -f "$REPO_ROOT/$f" ]; then
    echo "FATAL: allowlisted file missing: $f" >&2
    exit 1
  fi
done

# --- Stage into a clean directory, preserving the repo's relative layout ---
rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR"
for f in "${ALLOWLIST[@]}"; do
  mkdir -p "$STAGE_DIR/$(dirname "$f")"
  cp "$REPO_ROOT/$f" "$STAGE_DIR/$f"
done

# --- Fixed timestamp on every staged file/dir, for reproducible zip entries ---
# Not the files' actual mtimes -- avoids leaking exactly when each file was
# last touched, and makes repeated builds of the same commit byte-identical.
FIXED_TS="202601010000.00"
find "$STAGE_DIR" -exec touch -t "$FIXED_TS" {} +

# --- Build the zip ---
mkdir -p "$BUILD_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE_DIR" && zip -X -q -r "$ZIP_PATH" . )

rm -rf "$STAGE_DIR"

echo "Built: $ZIP_PATH"
echo ""
echo "Zip contents:"
unzip -l "$ZIP_PATH"
