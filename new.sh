#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
    echo "Usage: $0 <leetcode-url>" >&2
    exit 1
fi

URL="$1"

# Extract problem name from URL path
# Supports: leetcode.com/problems/<slug> and neetcode.io/problems/<slug>
PROBLEM=$(echo "$URL" | sed -E 's_.*(leetcode\.com|neetcode\.io)/problems/([^/?]+).*_\2_')

if [[ "$PROBLEM" == "$URL" ]]; then
    echo "Error: could not parse problem name from URL" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROBLEM_DIR="$SCRIPT_DIR/$PROBLEM"
DATE=$(date +%Y-%m-%d)
FILE="$PROBLEM_DIR/$DATE.py"

mkdir -p "$PROBLEM_DIR"

if [[ -f "$FILE" ]]; then
    echo "Already exists: $FILE"
else
    touch "$FILE"
    echo "Created: $FILE"
fi
