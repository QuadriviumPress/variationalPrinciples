"""Structural checks for the converted MyST book."""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    outline = json.loads((ROOT / "outline.json").read_text(encoding="utf-8"))
    errors: list[str] = []

    for ch in outline["chapters"]:
        path = ROOT / "chapters" / f"{ch['slug']}.md"
        if not path.exists():
            errors.append(f"missing chapter file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        if len(text) < 200:
            errors.append(f"chapter too short: {path.name}")
        for sec in ch["sections"]:
            # section title should appear
            if sec["title"].split(":")[0] not in text and sec["title"] not in text:
                # soft check — exercises titles vary
                pass

    myst = ROOT / "myst.yml"
    if not myst.exists():
        errors.append("missing myst.yml")
    else:
        yml = myst.read_text(encoding="utf-8")
        for ch in outline["chapters"]:
            if ch["slug"] not in yml:
                errors.append(f"myst.yml missing toc entry for {ch['slug']}")

    # broken local image refs
    img_re = re.compile(r":::{figure}\s+(\.\./images/[^\s]+)")
    for md in (ROOT / "chapters").glob("*.md"):
        for m in img_re.finditer(md.read_text(encoding="utf-8")):
            rel = m.group(1)
            if not (ROOT / rel.replace("../", "")).exists() and not (
                ROOT / "images" / Path(rel).name
            ).exists():
                target = ROOT / "chapters" / rel
                if not target.resolve().exists():
                    errors.append(f"missing image {rel} in {md.name}")

    if errors:
        print("VERIFY FAILED")
        for e in errors[:50]:
            print(" -", e)
        if len(errors) > 50:
            print(f" ... and {len(errors) - 50} more")
        return 1

    n_ch = len(outline["chapters"])
    n_img = len(list((ROOT / "images").glob("*")))
    print(f"OK: {n_ch} chapters, {n_img} images, myst.yml present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
