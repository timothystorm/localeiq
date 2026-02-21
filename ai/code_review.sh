#!/bin/bash

# Ensure we're in the project root
cd "$(dirname "$0")/.." || exit 1

REPORT_FILE="code_review_$(date +%Y%m%d_%H%M).md"
DIFF_CONTENT=$(git diff main...HEAD)

if [ -z "$DIFF_CONTENT" ]; then
    echo "No differences found. Are you sure you're on the PR branch?"
    exit 1
fi

echo "# Code Review Report - $(date +%Y-%m-%d)" > "$REPORT_FILE"
echo "Branch: $(git rev-parse --abbrev-ref HEAD) against main" >> "$REPORT_FILE"
echo "---" >> "$REPORT_FILE"

AGENTS=("architect" "code-reviewer")
for AGENT in "${AGENTS[@]}"; do
    echo "## 🤖 Agent: ${AGENT} Review" >> "$REPORT_FILE"
    echo "Processing ${AGENT} review..."

    # Use the /agent command to invoke specific personas
    # We pipe the diff into the suggest command
    echo "$DIFF_CONTENT" | copilot -p "Review this diff" --agent "$AGENT" >> "$REPORT_FILE"

    echo -e "\n\n" >> "$REPORT_FILE"
done

echo "Review complete! See $REPORT_FILE"