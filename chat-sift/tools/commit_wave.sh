#!/bin/sh
# Validate results, rebuild outputs and progress, commit and push.
cd "$(dirname "$0")/.." || exit 1
for b in work/results/*.json; do python3 tools/check.py "$b" >/dev/null || echo "CHECK FAILED: $b"; done
python3 tools/build.py && python3 tools/progress.py || exit 1
cd .. && git add chat-sift && git commit -q -m "chat-sift: $1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01Aq7txTcfpUgzabiqqnXaKj" && git push -q origin chat-sift 2>&1 | tail -1
