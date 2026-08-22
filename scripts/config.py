"""Shared paths for the Variational Principles MyST conversion."""

from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_2E = os.path.join(ROOT, "Variational_Principles_in_Classical_Mechanics_2e.pdf")
PDF_3E = os.path.join(ROOT, "Variational_Principles_in_Classical_Mechanics_3e.pdf")
OUTLINE = os.path.join(ROOT, "outline.json")
BUILD = os.path.join(ROOT, "build")
WORK = os.path.join(ROOT, "work")
HTML_CACHE = os.path.join(WORK, "html")
IMAGES = os.path.join(ROOT, "images")

LIBRETEXTS_BASE = (
    "https://phys.libretexts.org/Bookshelves/Classical_Mechanics/"
    "Variational_Principles_in_Classical_Mechanics_(Cline)"
)
SOURCE_HOME = "http://classicalmechanics.lib.rochester.edu/"
USER_AGENT = "QuadriviumPress-myst-converter/0.1 (OER CC BY-NC-SA reuse)"
