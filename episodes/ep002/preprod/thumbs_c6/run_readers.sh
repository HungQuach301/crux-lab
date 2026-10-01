#!/usr/bin/env bash
# Episode 2 · C6 blind pair test: one FRESH sonnet agent per (image, role). Protocol: review-c6/pack-test/intent.md.
# Each reader runs in its own temp folder that holds ONLY its one hex-named image (no key, no other images), tool = Read only.
#   bash episodes/ep002/preprod/thumbs_c6/run_readers.sh <scratch dir>
# Writes review-c6/pack-test/<id>/answer-<role>.md (raw reply, verbatim).
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; EP="$(cd "$HERE/../.." && pwd)"; DEST="$EP/review-c6/pack-test"; TMP="${1:?scratch dir}"
declare -A ROLE
ROLE[G]="You are an American starting a graduate program next year; federal loans will not cover the full cost, so you expect to need private student loans."
ROLE[P]="You are an American parent who may co-sign your child's private loan for graduate school."
ROLE[R]="You are an American who already has student loans and is looking at refinancing them with a private lender."
ROLE[C]="You are an American who watches personal-finance videos out of curiosity and has no student loans right now."
Q='You are scrolling YouTube search results for "private student loans". Open the image file %s in this folder with the Read tool: it shows two search results, labelled 1 (top) and 2 (bottom). Which one of these two videos would you click? Reply in exactly two lines: `ANSWER: 1` or `ANSWER: 2`, then `WHY: <one sentence>`.'
one() {
  local id="$1" r="$2" d="$TMP/$1-$2"
  [ -s "$DEST/$id/answer-$r.md" ] && return 0
  rm -rf "$d"; mkdir -p "$d"; cp "$DEST/$id/$id.png" "$d/"
  local prompt; prompt="${ROLE[$r]} $(printf "$Q" "$id.png")"
  ( cd "$d" && timeout 300 claude -p --model sonnet --tools Read --restricted --strict-mcp-config --setting-sources "" --no-session-persistence "$prompt" < /dev/null ) > "$d/out.txt" 2>"$d/err.txt"
  if grep -qE 'ANSWER: *[12]' "$d/out.txt"; then cp "$d/out.txt" "$DEST/$id/answer-$r.md"; else echo "FAILED $id $r" >&2; fi
}
export -f one; export DEST TMP Q
export ROLE_G="${ROLE[G]}" ROLE_P="${ROLE[P]}" ROLE_R="${ROLE[R]}" ROLE_C="${ROLE[C]}"
jobs=()
for dir in "$DEST"/*/; do id="$(basename "$dir")"; [[ "$id" =~ ^[0-9a-f]{10}$ ]] || continue; for r in G P R C; do jobs+=("$id $r"); done; done
printf '%s\n' "${jobs[@]}" | shuf | xargs -P 8 -L 1 bash -c 'declare -A ROLE=([G]="$ROLE_G" [P]="$ROLE_P" [R]="$ROLE_R" [C]="$ROLE_C"); one "$0" "$1"'
echo "answers: $(ls "$DEST"/*/answer-*.md 2>/dev/null | wc -l) / ${#jobs[@]}"
