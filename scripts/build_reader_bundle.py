#!/usr/bin/env python3
"""Build a deterministic reader ZIP. MIT licensed; see ../LICENSE-CODE."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.3.0"
DIST = ROOT / "dist"
EXCLUDED = {".git", "dist", "__pycache__"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def included_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in EXCLUDED for part in path.parts)
        and not path.name.startswith(".DS_Store")
        and path.suffix != ".pyc"
    )


def main() -> int:
    files = included_files()
    prefix = f"the-amplified-engineer-companion-v{VERSION}"
    DIST.mkdir(exist_ok=True)
    archive_path = DIST / f"{prefix}.zip"
    manifest_path = DIST / f"{prefix}-manifest.json"
    checksums_path = DIST / "SHA256SUMS.txt"
    manifest = {
        "title": "The Amplified Engineer Reader Companion",
        "version": VERSION,
        "fileCount": len(files),
        "files": [{"path": str(path.relative_to(ROOT)), "sha256": digest(path)} for path in files],
    }
    manifest_bytes = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for source in files:
            info = zipfile.ZipInfo(f"{prefix}/{source.relative_to(ROOT).as_posix()}", (2026, 8, 29, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = (0o100755 if source.suffix == ".py" else 0o100644) << 16
            archive.writestr(info, source.read_bytes())
        info = zipfile.ZipInfo(f"{prefix}/BUNDLE-MANIFEST.json", (2026, 8, 29, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.create_system = 3
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest_bytes)
    manifest_path.write_bytes(manifest_bytes)
    checksums_path.write_text(
        f"{digest(archive_path)}  {archive_path.name}\n{digest(manifest_path)}  {manifest_path.name}\n",
        encoding="utf-8",
    )
    print(f"Built {archive_path.name} with {len(files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
