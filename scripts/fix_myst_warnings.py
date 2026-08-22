#!/usr/bin/env python3
"""Fix MyST build errors/warnings in converted chapter Markdown.

Idempotent: safe to re-run after convert.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_DIRS = [ROOT / "chapters", ROOT / "front", ROOT / "back"]

SUMMARY_HEADING = re.compile(r"^##\s+(?:\d+\.S:|.*Summary)", re.I)
CHAPTER_NUM = re.compile(r"^ch-(\d+)-")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")

AMBIGUOUS = {
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "m",
    "n",
    "A",
    "B",
    "C",
    "D",
    "a1",
    "b1",
    "c1",
    "d2",
    "b3",
    "alpha",
    "gamma",
    r"\beta",
    "beta",
}


def chapter_num(path: Path) -> str | None:
    m = CHAPTER_NUM.match(path.stem)
    return (m.group(1).lstrip("0") or "0") if m else None


def is_summary_heading(line: str) -> bool:
    if SUMMARY_HEADING.match(line):
        return True
    return bool(re.match(r"^##\s+\d+\.\d+:\s*Summary\b", line, re.I))


def fix_hard_errors(path: Path, text: str) -> str:
    name = path.name

    if name == "ch-02-review-of-newtonian-mechanics.md":
        text = text.replace(
            r"\Delta U_{a \rightarrow b} & = & -",
            r"\Delta U_{a \rightarrow b} &= -",
        )
        text = text.replace(r"\\ & = & -Gm_1m_0", r"\\ &= -Gm_1m_0")

    if name == "ch-04-nonlinear-systems-and-chaos.md":
        text = text.replace(r"\dddot{", r"\overset{\ldots}{")

    if name == "ch-07-symmetries-invariance-and-the-hamiltonian.md":
        text = text.replace(
            r"$L(q_{i},\dot{q_{i}% },\ddot{q_{i}},t)$",
            r"$L(q_{i},\dot{q_{i}},\ddot{q_{i}},t)$",
        )
        text = text.replace(r"\frac{% \partial L}", r"\frac{\partial L}")
        text = text.replace(
            r"a Lagrangian multiplier $% \lambda$ introduced.",
            r"a Lagrangian multiplier $\lambda$ introduced.",
        )
        text = text.replace(r"and mass $% m$ with", r"and mass $m$ with")

    if name == "ch-12-non-inertial-reference-frames.md":
        text = text.replace(
            r"\frac{d}{dt} (mr'' ^2 \omega )",
            r"\frac{d}{dt} (m r^{\prime\prime 2} \omega )",
        )
        text = text.replace(r"equation $\ref{alpha}$", r"equation {eq}`alpha`")

    if name == "ch-16-analytical-formulations-for-continuous-systems.md":
        text = text.replace(r"(q_{j-1} – q_j)", r"(q_{j-1} - q_j)")

    if "\u00ad" in text:
        text = text.replace("\u00ad", "")

    return text


def strip_summary_labels(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_summary = False
    for line in lines:
        if line.startswith("## "):
            in_summary = is_summary_heading(line.rstrip("\n"))
        if in_summary and r"\label{" in line:
            line = LABEL_RE.sub("", line)
        out.append(line)
    return "".join(out)


def rename_ch14_labels(text: str) -> str:
    text = re.sub(
        r"\\label\{12\.(\d+(?:\.\d+)*)\}",
        lambda m: rf"\label{{14.{m.group(1)}}}",
        text,
    )
    text = re.sub(
        r"\\(eqref|ref)\{12\.(\d+(?:\.\d+)*)\}",
        lambda m: rf"\{m.group(1)}{{14.{m.group(2)}}}",
        text,
    )
    return text


def make_new_id(ch: str, old: str, n: int, total: int) -> str:
    """Choose a unique replacement id for the n-th occurrence (1-based) of old."""
    base = old.replace("\\", "")
    if old in AMBIGUOUS:
        base = f"{ch}-{base}"
        if total == 1:
            return base
        return f"{base}-{n}"
    if total == 1:
        return old
    return old if n == 1 else f"{old}-{n}"


def uniquify_labels(path: Path, text: str) -> str:
    ch = chapter_num(path) or path.stem
    spans = [(m.start(), m.end(), m.group(1)) for m in LABEL_RE.finditer(text)]
    if not spans:
        return text

    totals: dict[str, int] = {}
    for _, _, old in spans:
        totals[old] = totals.get(old, 0) + 1

    # Only rewrite ids that are ambiguous across chapters or duplicated in-file
    needs_fix = {
        old
        for old, total in totals.items()
        if old in AMBIGUOUS or total > 1
    }
    if not needs_fix:
        return text

    seen: dict[str, int] = {}
    new_ids: list[str] = []
    old_to_news: dict[str, list[str]] = {}
    for _, _, old in spans:
        if old not in needs_fix:
            new_ids.append(old)
            old_to_news.setdefault(old, []).append(old)
            continue
        seen[old] = seen.get(old, 0) + 1
        new = make_new_id(ch, old, seen[old], totals[old])
        new_ids.append(new)
        old_to_news.setdefault(old, []).append(new)

    # Replace labels from the end so offsets stay valid
    parts: list[str] = []
    last = len(text)
    for (start, end, _), new in zip(reversed(spans), reversed(new_ids)):
        parts.append(text[end:last])
        parts.append(rf"\label{{{new}}}")
        last = start
    parts.append(text[:last])
    text = "".join(reversed(parts))

    # Positions of rewritten labels for nearest-preceding ref resolution
    old_pos_new: list[tuple[int, str, str]] = []
    for m, (_, _, old), new in zip(LABEL_RE.finditer(text), spans, new_ids):
        old_pos_new.append((m.start(), old, new))

    def nearest_new(old: str, at: int) -> str | None:
        best = None
        for pos, o, new in old_pos_new:
            if pos > at:
                break
            if o == old:
                best = new
        if best is None and old in old_to_news:
            return old_to_news[old][0]
        return best

    def repl_ref(m: re.Match) -> str:
        cmd, old = m.group(1), m.group(2)
        if old not in needs_fix:
            return m.group(0)
        new = nearest_new(old, m.start())
        if not new:
            return m.group(0)
        return rf"\{cmd}{{{new}}}"

    text = re.sub(r"\\(eqref|ref)\{([^}]+)\}", repl_ref, text)

    def repl_myst(m: re.Match) -> str:
        old = m.group(1)
        if old not in needs_fix:
            return m.group(0)
        new = nearest_new(old, m.start())
        if not new:
            return m.group(0)
        return "{eq}`" + new + "`"

    text = re.sub(r"\{eq\}`([^`]+)`", repl_myst, text)
    return text


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    text = original
    text = fix_hard_errors(path, text)
    if path.name == "ch-14-coupled-linear-oscillators.md":
        text = rename_ch14_labels(text)
    text = strip_summary_labels(text)
    text = uniquify_labels(path, text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for d in CONTENT_DIRS:
        if not d.is_dir():
            continue
        for path in sorted(d.glob("*.md")):
            if process_file(path):
                changed.append(path.relative_to(ROOT))
    print(f"Updated {len(changed)} files:")
    for p in changed:
        print(f"  {p}")


if __name__ == "__main__":
    main()
