#!/usr/bin/env python3
"""Validate the public Book 1 companion. MIT licensed; see ../LICENSE-CODE."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.2.0"
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
REQUIRED = (
    "README.md", "START-HERE.md", "INDEX.md", "CHANGELOG.md",
    "CITATION.cff", "EDITION-MAP.md", "ERRATA.md", "LICENSE",
    "LICENSE-CONTENT", "LICENSE-CODE", "COMMERCIAL-USE.md",
    "CONTRIBUTING.md", "SECURITY.md", "READER-USABILITY-PASS.md",
    ".github/ISSUE_TEMPLATE/reader-usability.yml",
)


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = unquote(target.split("#", 1)[0])
    return (source.parent / target).resolve()


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")

    if not (ROOT / "resources/human-centered-ai-design-practice.md").is_file():
        errors.append("missing human-centered AI design practice")

    resources = sorted((ROOT / "resources").glob("*.md"))
    if len(resources) != 7:
        errors.append(f"resources contains {len(resources)} worksheets; expected 7")

    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts:
            continue
        text = source.read_text(encoding="utf-8")
        lowered = text.lower()
        for forbidden in ("private companion source", "public-release decision pending"):
            if forbidden in lowered:
                errors.append(f"private production label in {source.relative_to(ROOT)}")
        for raw_target in LINK.findall(text):
            target = local_target(source, raw_target)
            if target is not None and not target.exists():
                errors.append(f"broken local link: {source.relative_to(ROOT)} -> {raw_target}")

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    edition = (ROOT / "EDITION-MAP.md").read_text(encoding="utf-8")
    if f"version: {VERSION}" not in citation:
        errors.append(f"CITATION.cff does not name {VERSION}")
    if f"## {VERSION} " not in changelog:
        errors.append(f"CHANGELOG.md does not name {VERSION}")
    if f"| {VERSION} |" not in edition:
        errors.append(f"EDITION-MAP.md does not name {VERSION}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated Book 1 companion v{VERSION}: 7 worksheets and all local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
