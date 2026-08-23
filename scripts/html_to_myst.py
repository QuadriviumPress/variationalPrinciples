"""Convert LibreTexts HTML content into MyST Markdown."""

from __future__ import annotations

import html as html_lib
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote

from bs4 import BeautifulSoup, NavigableString, Tag

SKIP_FOOTER_RE = re.compile(
    r"^(Contributors and Attributions|Footnotes|References|This page titled)",
    re.I,
)
PAGEINDEX_RE = re.compile(r"\\PageIndex\{(\d+)\}")


def scrub_pageindex(text: str, chapter: str | None = None) -> str:
    """Replace LibreTexts \\PageIndex{...} with chapter.n or n."""
    def repl(m: re.Match) -> str:
        n = (m.group(1) or m.group(2)).strip()
        return f"{chapter}.{n}" if chapter else n
    return re.sub(
        r"\$\\PageIndex\{([^}]+)\}\$|\\PageIndex\{([^}]+)\}",
        repl,
        text,
    )



def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:80] or "section"


def decode_entities(text: str) -> str:
    text = html_lib.unescape(text)
    text = text.replace("\xa0", " ")
    return text


def clean_math(tex: str) -> str:
    tex = decode_entities(tex)
    tex = tex.replace("\u200b", "")
    # LibreTexts often uses \[4pt] spacing in align — keep as-is (valid amsmath)
    return tex.strip()


def normalize_inline_math(text: str) -> str:
    """Turn \\( \\) / \\[ \\] into $ / $$ forms used by MyST."""

    def repl_display(m: re.Match) -> str:
        body = clean_math(m.group(1))
        if "\n" in body or body.startswith("\\begin"):
            return f"\n$$\n{body}\n$$\n"
        return f"\n$$\n{body}\n$$\n"

    def repl_inline(m: re.Match) -> str:
        return f"${clean_math(m.group(1))}$"

    text = re.sub(r"\\\[(.*?)\\\]", repl_display, text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", repl_inline, text, flags=re.S)
    return text


def figure_enumerator(caption: str, chapter: str | None) -> tuple[str, str]:
    """Return (enumerator, cleaned caption)."""
    cap = PAGEINDEX_RE.sub(r"\1", caption)
    cap = re.sub(r"^Figure\s+", "", cap, flags=re.I).strip()
    # "Figure 5.2.1: ..." already cleaned via PageIndex → "1: ..."
    m = re.match(r"^(\d+)\s*[:.]\s*(.*)$", cap, re.S)
    if m and chapter:
        enum = f"{chapter}.{m.group(1)}"
        return enum, m.group(2).strip()
    m2 = re.match(r"^(\d+(?:\.\d+)*)\s*[:.]\s*(.*)$", cap, re.S)
    if m2:
        return m2.group(1), m2.group(2).strip()
    return "", cap


def download_name_from_url(url: str) -> str:
    path = unquote(urlparse(url).path)
    name = Path(path).name
    name = re.sub(r"[^\w.\-]+", "_", name)
    if not name or name == "files":
        name = "image.png"
    return name.lower()


class HtmlToMyst:
    def __init__(
        self,
        *,
        page_url: str,
        chapter_num: str | None = None,
        image_dir: Path,
        image_url_prefix: str = "../images",
        image_map: dict[str, str] | None = None,
    ):
        self.page_url = page_url
        self.chapter_num = chapter_num
        self.image_dir = image_dir
        self.image_url_prefix = image_url_prefix
        self.image_map = image_map if image_map is not None else {}
        self.pending_downloads: list[tuple[str, Path]] = []

    def convert(self, html: str, *, heading_level: int = 2) -> str:
        soup = BeautifulSoup(html, "html.parser")
        main = (
            soup.select_one("#mt-content-container")
            or soup.select_one(".mt-content-container")
            or soup.select_one("#elm-main-content")
        )
        if main is None:
            return ""

        # Drop LibreTexts chrome inside content
        for sel in (
            "script",
            "style",
            "nav",
            ".lt-discussion",
            ".printfooter",
            "#printfooter",
            ".noprint",
            ".hidden",
            "footer",
        ):
            for el in main.select(sel):
                el.decompose()

        parts: list[str] = []
        for child in list(main.children):
            chunk = self._render_node(child, heading_level=heading_level)
            if chunk and chunk.strip():
                parts.append(chunk.strip())
        text = "\n\n".join(parts)
        text = normalize_inline_math(text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"

    def _render_node(self, node, heading_level: int = 2) -> str:
        if isinstance(node, NavigableString):
            s = str(node)
            if not s.strip():
                return ""
            return decode_entities(s.strip())

        if not isinstance(node, Tag):
            return ""

        name = node.name.lower()

        if name in ("script", "style", "nav"):
            return ""

        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(name[1])
            # remap: page section title → heading_level
            hashes = "#" * min(heading_level + level - 1, 6)
            title = decode_entities(node.get_text(" ", strip=True))
            title = PAGEINDEX_RE.sub(r"\1", title)
            if SKIP_FOOTER_RE.match(title):
                return ""
            return f"{hashes} {title}"

        if name == "p":
            text = self._inline(node)
            text = text.strip()
            if not text:
                return ""
            if SKIP_FOOTER_RE.match(text):
                return ""
            if text.startswith("Douglas Cline"):
                return ""
            return text

        if name in ("ul", "ol"):
            items = []
            ordered = name == "ol"
            for i, li in enumerate(node.find_all("li", recursive=False), 1):
                body = self._inline(li).strip()
                if not body:
                    continue
                prefix = f"{i}." if ordered else "-"
                items.append(f"{prefix} {body}")
            return "\n".join(items)

        if name == "blockquote":
            body = self._inline(node).strip()
            return "\n".join(f"> {ln}" if ln else ">" for ln in body.splitlines())

        if name == "figure":
            return self._figure(node)

        if name == "img":
            return self._image_only(node)

        if name == "table":
            return self._table(node)

        if name == "hr":
            return "---"

        if name in ("div", "section", "span", "article"):
            # unwrap containers
            parts = []
            for child in node.children:
                chunk = self._render_node(child, heading_level=heading_level)
                if chunk and chunk.strip():
                    parts.append(chunk.strip())
            return "\n\n".join(parts)

        if name in ("dl",):
            parts = []
            for child in node.children:
                if getattr(child, "name", None) == "dt":
                    parts.append(f"**{self._inline(child).strip()}**")
                elif getattr(child, "name", None) == "dd":
                    parts.append(self._inline(child).strip())
            return "\n\n".join(p for p in parts if p)

        # fallback: inline text
        return self._inline(node)

    def _inline(self, node: Tag) -> str:
        bits: list[str] = []
        for child in node.children:
            if isinstance(child, NavigableString):
                bits.append(decode_entities(str(child)))
                continue
            if not isinstance(child, Tag):
                continue
            n = child.name.lower()
            if n in ("br",):
                bits.append("\n")
            elif n in ("strong", "b"):
                bits.append(f"**{self._inline(child).strip()}**")
            elif n in ("em", "i"):
                bits.append(f"*{self._inline(child).strip()}*")
            elif n == "code":
                bits.append(f"`{child.get_text()}`")
            elif n == "a":
                href = child.get("href") or ""
                label = self._inline(child).strip() or href
                if href.startswith("http") or href.startswith("/"):
                    href = urljoin(self.page_url, href)
                    bits.append(f"[{label}]({href})")
                else:
                    bits.append(label)
            elif n == "sub":
                bits.append(f"<sub>{self._inline(child)}</sub>")
            elif n == "sup":
                bits.append(f"<sup>{self._inline(child)}</sup>")
            elif n == "img":
                bits.append(self._image_only(child))
            elif n == "span":
                bits.append(self._inline(child))
            else:
                bits.append(self._inline(child))
        text = "".join(bits)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"[ \t]{2,}", " ", text)
        return text

    def _register_image(self, src: str) -> str:
        abs_url = urljoin(self.page_url, src)
        # strip query for filename stability but keep URL with revision for fetch
        base_name = download_name_from_url(abs_url.split("?")[0])
        # uniquify by path hash fragment if collision
        if abs_url not in self.image_map:
            dest_name = base_name
            dest = self.image_dir / dest_name
            n = 1
            while dest.exists() and self.image_map.get(abs_url) != dest_name:
                # allow reuse if same file already mapped elsewhere with same name
                stem, suf = Path(base_name).stem, Path(base_name).suffix
                dest_name = f"{stem}-{n}{suf}"
                dest = self.image_dir / dest_name
                n += 1
                if any(v == dest_name for v in self.image_map.values()):
                    # already planned for another URL — keep looping
                    continue
                break
            # simpler: use content-derived unique name from file id
            m = re.search(r"/files/(\d+)/", abs_url)
            if m:
                dest_name = f"lt-{m.group(1)}-{base_name}"
            self.image_map[abs_url] = dest_name
            self.pending_downloads.append((abs_url, self.image_dir / dest_name))
        return f"{self.image_url_prefix}/{self.image_map[abs_url]}"

    def _figure(self, node: Tag) -> str:
        img = node.find("img")
        if img is None:
            return self._inline(node).strip()
        src = img.get("src") or ""
        alt = img.get("alt") or "Figure"
        path = self._register_image(src)
        cap_el = node.find("figcaption")
        caption = self._inline(cap_el).strip() if cap_el else ""
        caption = normalize_inline_math(caption)
        enum, cap_body = figure_enumerator(caption, self.chapter_num)
        label = ""
        if enum:
            label = "fig-" + enum.replace(".", "-")
        lines = [f":::{{figure}} {path}"]
        if label:
            lines.append(f":label: {label}")
        if enum:
            lines.append(f":enumerator: {enum}")
        lines.append(f":alt: {alt}")
        lines.append("")
        lines.append(cap_body or caption or alt)
        lines.append(":::")
        return "\n".join(lines)

    def _image_only(self, node: Tag) -> str:
        src = node.get("src") or ""
        if not src or "logo" in src.lower() or "favicon" in src.lower():
            return ""
        alt = node.get("alt") or "Illustration"
        path = self._register_image(src)
        return f":::{{figure}} {path}\n:alt: {alt}\n\n{alt}\n:::"

    def _table_cell_text(self, td: Tag) -> str:
        text = self._inline(td).strip()
        # Table cells must stay on one physical line: force any display math
        # (\[...\]) to render inline instead of as a $$ block, and turn any
        # remaining <br>-sourced or source newlines into <br> so multi-line
        # cell content (stacked equations, matrices) doesn't get split into
        # bogus extra table rows.
        text = re.sub(
            r"\\\[(.*?)\\\]", lambda m: f"${clean_math(m.group(1))}$", text, flags=re.S
        )
        text = re.sub(
            r"\\\((.*?)\\\)", lambda m: f"${clean_math(m.group(1))}$", text, flags=re.S
        )
        text = re.sub(r"\s*\n\s*", "<br>", text.strip())
        return text.replace("|", "\\|")

    def _table(self, node: Tag) -> str:
        rows = []
        for tr in node.find_all("tr"):
            cells = [self._table_cell_text(td) for td in tr.find_all(["th", "td"])]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        header = rows[0]
        body = rows[1:] or [[""] * width]
        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join("---" for _ in header) + " |",
        ]
        for r in body:
            lines.append("| " + " | ".join(r) + " |")
        return "\n".join(lines)
