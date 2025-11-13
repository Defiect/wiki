#!/usr/bin/env python3
"""Convert the English CachyOS wiki content into a single Markdown document."""
from __future__ import annotations

import re
import textwrap
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import yaml

try:
    from bs4 import BeautifulSoup  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover - handled at runtime
    raise SystemExit("beautifulsoup4 is required. Install it with `python -m pip install beautifulsoup4`." ) from exc

BASE_DOCS = Path("src/content/docs")
LANG_CODES = {"cs", "de", "es", "et", "fr", "id", "pl", "ru", "sk"}
EXCLUDED_FILES = {Path("support/donation.md"), Path("support/social.md")}
EXCLUDED_DIRS = {"policy"}

ADMONITION_TITLES = {
    "note": "Note",
    "tip": "Tip",
    "caution": "Caution",
    "warning": "Warning",
    "important": "Important",
    "danger": "Danger",
    "info": "Info",
}

ICON_MAP = {
    "approve-check": "✅",
    "close-x": "✖️",
}


@dataclass
class Page:
    path: Path
    rel: Path
    title: str
    slug: str
    category: Tuple[str, ...]
    order: float
    content: str


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    text = re.sub(r"-+", "-", text)
    return text


def path_slug(rel: Path) -> str:
    parts = []
    for part in rel.with_suffix("").parts:
        clean = part.replace("_", "-")
        clean = re.sub(r"[^a-zA-Z0-9-]", "-", clean)
        clean = re.sub(r"-+", "-", clean).strip("-")
        parts.append(clean.lower())
    return "-".join(filter(None, parts)) or "overview"


def humanize_segment(segment: str) -> str:
    segment = segment.replace("_", " ")
    return segment.replace("-", " ").title()


def parse_front_matter(raw: str) -> Tuple[Dict, str]:
    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            content = parts[2]
            data = yaml.safe_load(fm_text) or {}
            return data, content
    return {}, raw


def remove_imports(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if line.strip().startswith("import ") or line.strip().startswith("export "):
            continue
        lines.append(line)
    return "\n".join(lines)


def remove_style_blocks(text: str) -> str:
    return re.sub(r"<style>{.*?</style>", "", text, flags=re.DOTALL)


def convert_link_cards(text: str, slug_map: Dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        attrs = match.group(1)
        attr_pairs = re.findall(r"(\w+)=(\".*?\"|'[^']*')", attrs, flags=re.DOTALL)
        attr_dict = {name: value[1:-1] for name, value in attr_pairs}
        title = attr_dict.get("title", "")
        href = attr_dict.get("href", "")
        description = attr_dict.get("description", "")
        target = slug_map.get(href, href)
        bullet = "- "
        if title:
            bullet += f"[{title}]({target})"
        else:
            bullet += target or href
        if description:
            bullet += f" — {description.strip()}"
        return bullet

    text = re.sub(r"<LinkCard\s+([^>]*)>", repl, text, flags=re.DOTALL)
    text = text.replace("</LinkCard>", "")
    text = text.replace("<CardGrid>", "")
    text = text.replace("</CardGrid>", "")
    return text


def convert_image_component(text: str) -> str:
    def single_repl(match: re.Match[str]) -> str:
        path = match.group(1)
        return f"![Image](src/assets/images/{path})"

    text = re.sub(
        r"<ImageComponent[^>]*imgsrc=\{import\('~\/assets\/images\/([^']+)'\)\}[^>]*\/?>",
        single_repl,
        text,
    )

    def multi_repl(match: re.Match[str]) -> str:
        paths = match.group(1)
        images = []
        for raw in paths.split(","):
            raw = raw.strip()
            m = re.match(r"import\('~\/assets\/images\/([^']+)'\)", raw)
            if m:
                images.append(f"![Image](src/assets/images/{m.group(1)})")
        return "\n".join(images)

    text = re.sub(
        r"<MultipleImageComponent[^>]*images=\{\[(.*?)\]\}[^>]*\/?>",
        multi_repl,
        text,
        flags=re.DOTALL,
    )
    return text


def convert_tabs(text: str) -> str:
    text = text.replace("<Tabs>", "")
    text = text.replace("</Tabs>", "")

    def repl(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        return f"\n##### {label}\n\n"

    text = re.sub(r"<TabItem[^>]*label\s*=\s*\"([^\"]+)\"[^>]*>", repl, text)
    text = re.sub(r"<TabItem[^>]*label\s*=\s*'([^']+)'[^>]*>", repl, text)
    text = text.replace("</TabItem>", "\n")
    return text


def convert_steps(text: str) -> str:
    return text.replace("<Steps>", "").replace("</Steps>", "")


def convert_details(text: str) -> str:
    text = text.replace("<details>", "")
    text = text.replace("</details>", "")

    def repl(match: re.Match[str]) -> str:
        title = match.group(1).strip()
        return f"**{title}:**"

    text = re.sub(r"<summary>(.*?)</summary>", repl, text, flags=re.DOTALL)
    return text


def convert_icons(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        name = match.group(1)
        return ICON_MAP.get(name, "")

    return re.sub(r"<Icon\s+[^>]*name=\"([^\"]+)\"[^>]*/?>", repl, text)


def convert_kbd(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        keys = match.group(1)
        return f"`{keys}`"

    return re.sub(r"<Kbd\s+[^>]*linux=\"([^\"]+)\"[^>]*/?>", repl, text)


def convert_br(text: str) -> str:
    return text.replace("<br />", "\n").replace("<br>", "\n")


def convert_tables(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        html = match.group(0)
        soup = BeautifulSoup(html, "html.parser")
        headers: List[str] = []
        rows: List[List[str]] = []

        if (thead := soup.find("thead")):
            header_cells = thead.find_all("th")
            headers = [clean_table_cell(cell) for cell in header_cells]
        if not headers:
            first_row = soup.find("tr")
            if first_row:
                headers = [clean_table_cell(cell) for cell in first_row.find_all("th")]
                if headers:
                    first_row.extract()

        for tr in soup.find_all("tr"):
            if tr.find_parent("thead"):
                continue
            cells = [clean_table_cell(cell) for cell in tr.find_all(["td", "th"])]
            if cells:
                rows.append(cells)

        if headers:
            widths = max(len(headers), max((len(r) for r in rows), default=0))
        else:
            widths = max((len(r) for r in rows), default=0)
            headers = ["" for _ in range(widths)]

        def pad(row: List[str]) -> List[str]:
            return row + [""] * (widths - len(row))

        md_lines = []
        md_lines.append("| " + " | ".join(headers) + " |")
        md_lines.append("| " + " | ".join(["---"] * widths) + " |")
        for row in rows:
            md_lines.append("| " + " | ".join(pad(row)) + " |")
        return "\n".join(md_lines)

    return re.sub(r"<table.*?</table>", repl, text, flags=re.DOTALL)


def clean_table_cell(cell) -> str:
    for tag in cell.find_all("br"):
        tag.replace_with("\n")
    text = cell.get_text("\n", strip=True)
    text = text.replace("\u200b", "")
    return text.replace("\n", "<br>")


def convert_admonitions(text: str) -> str:
    lines = text.splitlines()
    result: List[str] = []
    in_admon = False
    prefix = ""
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(":::"):
            if not in_admon:
                m = re.match(r":::([A-Za-z]+)(?:\[(.*?)\])?", stripped)
                if m:
                    kind = m.group(1).lower()
                    title = m.group(2) or ""
                    label = ADMONITION_TITLES.get(kind, kind.title())
                    heading = f"> **{label}"
                    if title:
                        heading += f" – {title}"
                    heading += ":**"
                    result.append(heading)
                    in_admon = True
                    prefix = "> "
                else:
                    continue
            else:
                in_admon = False
                prefix = ""
            continue
        if in_admon:
            if stripped:
                result.append(f"{prefix}{line.strip()}")
            else:
                result.append(">")
        else:
            result.append(line)
    return "\n".join(result)


def collapse_blank_lines(text: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", text)


def normalize_placeholders(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        inner = match.group(1)
        if inner.lower() in {"tr", "td", "th", "thead", "tbody", "table", "strong", "em", "li", "ul", "code", "br"}:
            return match.group(0)
        return f"&lt;{inner}&gt;"

    return re.sub(r"<([A-Za-z0-9_\-\/ ]+?)>", repl, text)


def adjust_headings(text: str, page_slug: str) -> str:
    lines = text.splitlines()
    result: List[str] = []
    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue
        if not in_code and re.match(r"^#{1,6} ", stripped):
            level = len(stripped.split()[0])
            heading_text = stripped[level:].strip()
            new_level = min(level + 1, 6)
            anchor = f"{page_slug}-{slugify(heading_text)}" if heading_text else page_slug
            result.append(f"<a id=\"{anchor}\"></a>")
            result.append(f"{'#' * new_level} {heading_text}")
        else:
            result.append(line)
    return "\n".join(result)


def dedent_content(text: str) -> str:
    lines = text.splitlines()
    result: List[str] = []
    in_code = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_code = not in_code
            result.append(line)
            continue
        if in_code:
            result.append(line)
            continue
        if line.startswith("    "):
            line = line[4:]
        if re.match(r"^\s{2,}[-*+] ", line):
            line = line.lstrip()
        result.append(line)
    return "\n".join(result)


def convert_links(text: str, slug_map: Dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        if url.startswith("/"):
            base, _, fragment = url.partition("#")
            normalized = base.rstrip("/") or "/"
            target = slug_map.get(normalized, slug_map.get(normalized + "/index", normalized))
            if fragment:
                frag_slug = slugify(fragment)
                if target.startswith("#"):
                    target = f"{target}-{frag_slug}" if frag_slug else target
                else:
                    target = f"{target}#{frag_slug}" if frag_slug else target
            return f"[{label}]({target})"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, text)


def convert_page_content(raw: str, slug_map: Dict[str, str], page_slug: str) -> str:
    _, content = parse_front_matter(raw)
    content = remove_imports(content)
    content = remove_style_blocks(content)
    content = convert_link_cards(content, slug_map)
    content = convert_image_component(content)
    content = convert_tabs(content)
    content = convert_steps(content)
    content = convert_details(content)
    content = convert_icons(content)
    content = convert_kbd(content)
    content = convert_br(content)
    content = convert_tables(content)
    content = convert_admonitions(content)
    content = convert_links(content, slug_map)
    content = dedent_content(content)
    content = collapse_blank_lines(content)
    content = normalize_placeholders(content)
    content = adjust_headings(content, page_slug)
    content = collapse_blank_lines(content)
    return content.strip()


def build_slug_map(paths: Iterable[Path]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for rel in paths:
        slug = path_slug(rel)
        key = "/" + rel.with_suffix("").as_posix()
        mapping[key] = f"#{slug}"
        parts = rel.with_suffix("").parts
        for depth in range(1, len(parts)):
            prefix = Path(*parts[:depth])
            mapping.setdefault("/" + prefix.as_posix(), f"#{path_slug(prefix)}")
    mapping.setdefault("/", "#overview")
    return mapping


def load_pages() -> List[Page]:
    paths: List[Path] = []
    for path in sorted(BASE_DOCS.rglob("*.md")) + sorted(BASE_DOCS.rglob("*.mdx")):
        rel = path.relative_to(BASE_DOCS)
        if rel.parts and rel.parts[0] in LANG_CODES:
            continue
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if rel in EXCLUDED_FILES:
            continue
        paths.append(rel)

    slug_map = build_slug_map(paths)

    pages: List[Page] = []
    for rel in paths:
        path = BASE_DOCS / rel
        raw = path.read_text(encoding="utf-8")
        front_matter, _ = parse_front_matter(raw)
        title = front_matter.get("title")
        if not title:
            m = re.search(r"^#\s+(.+)$", raw, flags=re.MULTILINE)
            title = m.group(1).strip() if m else humanize_segment(rel.stem)
        slug = path_slug(rel)
        category = tuple(rel.with_suffix("").parts[:-1])
        order = float(front_matter.get("sidebar", {}).get("order", 0)) if isinstance(front_matter.get("sidebar"), dict) else 0.0
        content = convert_page_content(raw, slug_map, slug)
        pages.append(Page(path, rel, title, slug, category, order, content))
    return pages


def build_table_of_contents(pages: List[Page]) -> str:
    tree: Dict[Tuple[str, ...], List[Page]] = defaultdict(list)
    for page in pages:
        tree[page.category].append(page)

    lines: List[str] = []
    lines.append("## Table of Contents")

    root_pages = sorted(tree.get((), []), key=lambda p: (p.order, p.title.lower()))
    lines.append("- [Overview](#overview)")
    for page in root_pages:
        lines.append(f"  - [{page.title}](#{page.slug})")

    def build_entries(prefix: Tuple[str, ...], level: int) -> None:
        children = sorted(
            (cat for cat in tree.keys() if len(cat) == level + 1 and cat[:level] == prefix),
            key=lambda parts: [p.lower() for p in parts],
        )
        for child in children:
            name = humanize_segment(child[level])
            indent = "  " * level
            anchor = f"#{path_slug(Path(*child))}" if child else "#overview"
            lines.append(f"{indent}- [{name}]({anchor})")
            build_entries(child, level + 1)
        if prefix:
            for page in sorted(tree.get(prefix, []), key=lambda p: (p.order, p.title.lower())):
                page_indent_level = level if level > 0 else 1
                indent = "  " * page_indent_level
                lines.append(f"{indent}- [{page.title}](#{page.slug})")

    build_entries((), 0)
    return "\n".join(lines)


def assemble_document(pages: List[Page]) -> str:
    pages = sorted(pages, key=lambda p: (p.category, p.order, p.title.lower()))
    toc = build_table_of_contents(pages)
    parts: List[str] = []
    parts.append("# CachyOS Wiki Offline")
    parts.append("This document consolidates the English CachyOS wiki into a single offline-friendly Markdown file.")
    parts.append("")
    parts.append(toc)
    parts.append("")
    parts.append("<a id=\"overview\"></a>")
    parts.append("## Overview")
    parts.append("")

    current_category: Tuple[str, ...] = ()
    for page in pages:
        if page.category != current_category:
            for depth in range(len(current_category), len(page.category)):
                segment = page.category[depth]
                heading = "#" * (depth + 2)
                parts.append("")
                parts.append(f"<a id=\"{path_slug(Path(*page.category[: depth + 1]))}\"></a>")
                parts.append(f"{heading} {humanize_segment(segment)}")
            current_category = page.category
        parts.append("")
        parts.append(f"<a id=\"{page.slug}\"></a>")
        page_heading_level = len(page.category) + 3 if page.category else 3
        heading = "#" * page_heading_level
        parts.append(f"{heading} {page.title}")
        parts.append("")
        parts.append(page.content)
    parts.append("")
    return "\n".join(parts)


def main() -> None:
    pages = load_pages()
    document = assemble_document(pages)
    output = Path("CachyOS_Wiki_Offline.md")
    output.write_text(document, encoding="utf-8")
    print(f"Wrote {output} with {len(pages)} sections.")


if __name__ == "__main__":
    main()
