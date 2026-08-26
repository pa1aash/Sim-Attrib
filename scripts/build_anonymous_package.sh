#!/usr/bin/env bash
# Build the anonymized public reproducibility package for Sim-Attrib.
#
# This is NOT the Overleaf submission package (scripts/build_overleaf_package.sh) and
# it is NOT this repository. It is a separate, clean artifact intended for upload to
# an anonymous code-hosting service as double-blind review supplementary material:
# src/, results/*.yaml, tests/, and a fresh standalone README/LICENSE/requirements.txt
# written for an anonymous reader -- nothing from audit/, docs/, GATES.md,
# DEVIATIONS.md, OUTSTANDING.md, PROVENANCE.md, or paper/, and no .git metadata of
# any kind.
#
# Session G16 finding, carried here as the reason the redaction pass below exists:
# results/*.yaml files carry this machine's local hostname (which contains the
# operator's name) and private-repo commit hashes (a residual re-identification risk
# if the private repository is ever found -- the same reasoning paper/main.tex's own
# provenance table applies to the hashes it shows a reader, per GATES.md G16 Phase
# 3.4) under MORE THAN ONE field name each -- `host`/`measured_on` for the hostname,
# `commit`/`p_sel_run_commit` for commit hashes, found by grepping the operator's own
# name across every results/ file rather than trusting a hand-enumerated key list.
# The redaction below is therefore VALUE-based, not key-based: any line whose value
# is a 40-hex-character string (git SHA-1 shape) or contains the operator's name,
# whatever key it sits under. Every other field (script, command, seed, timestamps,
# dirty flag, dependency versions) is left untouched because none of it identifies
# anyone.
#
# Re-run this any time after editing src/, results/, or scripts/anonymous_package/ --
# it is safe to run repeatedly and always rebuilds from the current working tree.

set -euo pipefail

REPO_ROOT="$HOME/Desktop/Sim-Attrib"
if [ "$(git -C "$REPO_ROOT" rev-parse --show-toplevel 2>/dev/null)" != "$REPO_ROOT" ]; then
  echo "FATAL: not the Sim-Attrib repo root ($REPO_ROOT). Refusing to run." >&2
  exit 1
fi
cd "$REPO_ROOT"

BUILD_DIR="$REPO_ROOT/build"
STAGE_DIR="$BUILD_DIR/_anon_stage"
ZIP_PATH="$BUILD_DIR/anonymous_package.zip"
TEMPLATE_DIR="$REPO_ROOT/scripts/anonymous_package"

echo "=== Sim-Attrib anonymized package build ==="
echo "Repo:   $REPO_ROOT"
echo "Output: $ZIP_PATH"
echo ""

rm -rf "$STAGE_DIR"
mkdir -p "$STAGE_DIR"

# --- src/ and tests/: copied whole, no exclusions beyond __pycache__ ---
for d in src tests; do
  mkdir -p "$STAGE_DIR/$d"
  ( cd "$REPO_ROOT/$d" && find . -type f -name '*.py' -print0 ) \
    | while IFS= read -r -d '' f; do
        mkdir -p "$STAGE_DIR/$d/$(dirname "$f")"
        cp "$REPO_ROOT/$d/$f" "$STAGE_DIR/$d/$f"
      done
done

# --- results/*.yaml, recursively, with hostname/commit-hash VALUES redacted
#     regardless of which key holds them ---
mkdir -p "$STAGE_DIR/results"
( cd "$REPO_ROOT/results" && find . -type f -name '*.yaml' -print0 ) \
  | while IFS= read -r -d '' f; do
      mkdir -p "$STAGE_DIR/results/$(dirname "$f")"
      sed -E \
        -e 's/^([A-Za-z_ ]*:[[:space:]]*)[0-9a-f]{40}[[:space:]]*$/\1REDACTED-FOR-ANONYMITY/' \
        -e 's/^([A-Za-z_ ]*:[[:space:]]*).*[Pp]alaash.*$/\1REDACTED-FOR-ANONYMITY/' \
        "$REPO_ROOT/results/$f" > "$STAGE_DIR/results/$f"
    done

# --- the anonymous-reader-facing README, LICENSE, requirements.txt ---
cp "$TEMPLATE_DIR/README.md" "$STAGE_DIR/README.md"
cp "$TEMPLATE_DIR/LICENSE" "$STAGE_DIR/LICENSE"
cp "$TEMPLATE_DIR/requirements.txt" "$STAGE_DIR/requirements.txt"

echo "Staged file count: $(find "$STAGE_DIR" -type f | wc -l | tr -d ' ')"
echo ""

# --- S1/S3: the operator's name/email/GitHub username, and the standing AI-token
#     pattern, must not appear anywhere in the staged tree. Assembled at runtime for
#     the same reason OUTSTANDING.md's own pattern is: a script that spells the
#     literal tokens would match itself. ---
NAME_PAT="$(printf 'pa%saash|pa1%sash|%s gang' l l Palaash)"
AI_PAT="$(printf 'c%saude|a%sthropic|co-auth%sred|generat%sd with' l n o e)"
echo "=== anonymity scan: operator name/username ==="
if grep -rliE "$NAME_PAT" "$STAGE_DIR"; then
  echo "FATAL: operator-identifying token found in staged package. Aborting." >&2
  rm -rf "$STAGE_DIR"
  exit 1
fi
echo "(clean)"
echo "=== anonymity scan: AI-authorship tokens ==="
if grep -rliE "$AI_PAT" "$STAGE_DIR"; then
  echo "FATAL: AI-authorship token found in staged package. Aborting." >&2
  rm -rf "$STAGE_DIR"
  exit 1
fi
echo "(clean)"
echo "=== anonymity scan: no .git metadata ==="
if find "$STAGE_DIR" -name '.git*' | grep -q .; then
  echo "FATAL: git metadata found in staged package. Aborting." >&2
  rm -rf "$STAGE_DIR"
  exit 1
fi
echo "(clean)"
echo ""

# --- Fixed timestamp on every staged file/dir, for reproducible zip entries and so
#     file mtimes do not leak when the underlying work was actually done. ---
FIXED_TS="202601010000.00"
find "$STAGE_DIR" -exec touch -t "$FIXED_TS" {} +

mkdir -p "$BUILD_DIR"
rm -f "$ZIP_PATH"
( cd "$STAGE_DIR" && zip -X -q -r "$ZIP_PATH" . )

rm -rf "$STAGE_DIR"

echo "Built: $ZIP_PATH"
echo ""
echo "Zip contents ($(unzip -l "$ZIP_PATH" | tail -1 | awk '{print $2}') files):"
unzip -l "$ZIP_PATH"
