#!/usr/bin/env python3
"""Basic quality checks for profile README content."""

from pathlib import Path
import re
import sys

README = Path("README.md")
PLACEHOLDER_PATTERNS = [
    r"your-linkedin",
    r"your\.email",
    r"your-kaggle",
    r"your-handle",
    r"Add one-line",
]
REQUIRED_SECTIONS = [
    "## ✨ About Me",
    "## 🧰 Tech Matrix",
    "## 🚀 Signature Projects",
    "## 🧪 Unique Feature: ML System Blueprint",
    "## ⚡ Innovation Radar",
]


def main() -> int:
    if not README.exists():
        print("❌ README.md not found")
        return 1

    content = README.read_text(encoding="utf-8")
    errors: list[str] = []

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, content, flags=re.IGNORECASE):
            errors.append(f"Found placeholder content matching: '{pattern}'")

    for header in REQUIRED_SECTIONS:
        if header not in content:
            errors.append(f"Missing required section: {header}")

    if "```mermaid" not in content:
        errors.append("Missing mermaid diagram block")

    if errors:
        print("❌ README guard checks failed:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("✅ README guard checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
