#!/usr/bin/env python3
from pathlib import Path
from typing import Dict, List, Tuple

NEWLINE = chr(10)
DOC_ROOT = Path('src/content/docs')
OUTPUT_PATH = Path('CACHYOS_OFFLINE_WIKI.md')

DOC_PATHS = [
    'index.mdx',
    'cachyos_basic/download.mdx',
    'cachyos_basic/why_cachyos.md',
    'cachyos_basic/navigation-guide.mdx',
    'cachyos_basic/faq.mdx',
    'cachyos_basic/changelogs/gui_installer.md',
    'cachyos_basic/changelogs/cli_installer.md',
    'installation/installation_prepare.mdx',
    'installation/installation_on_root.mdx',
    'installation/installation_t2macbook.mdx',
    'installation/installation_handheld.mdx',
    'installation/desktop_environments.mdx',
    'installation/boot_managers.mdx',
    'installation/filesystem.md',
    'configuration/post_install_setup.mdx',
    'configuration/general_system_tweaks.mdx',
    'configuration/automount_with_fstab.mdx',
    'configuration/dual_gpu.mdx',
    'configuration/secure_boot_setup.mdx',
    'configuration/enabling_hardware_acceleration_in_google_chrome.mdx',
    'configuration/sched-ext.mdx',
    'configuration/gaming.mdx',
    'configuration/boot_manager_configuration.mdx',
    'configuration/desktop_environments/hyprland.mdx',
    'configuration/desktop_environments/i3.mdx',
    'configuration/desktop_environments/kde.mdx',
    'configuration/desktop_environments/niri.mdx',
    'configuration/desktop_environments/qtile.mdx',
    'configuration/desktop_environments/switch_desktop.mdx',
    'features/optimized_repos.mdx',
    'features/kernel.mdx',
    'features/kernel_manager.mdx',
    'features/chwd/chwd.mdx',
    'features/chwd/gpu_migration.mdx',
    'features/cachy_chroot.mdx',
    'features/cachyos_settings.mdx',
]

ADMONITION_LABELS = {
    'note': 'Note',
    'tip': 'Tip',
    'caution': 'Caution',
    'danger': 'Warning',
}


def slugify(text: str) -> str:
    replacements = ['[', ']', '(', ')', '`', '/', '&', '#', ':', ',', '.', '"']
    for symbol in replacements:
        text = text.replace(symbol, ' ')
    text = text.replace("'", ' ')
    text = text.lower()
    result: List[str] = []
    last_dash = False
    for char in text:
        if char.isalnum():
            result.append(char)
            last_dash = False
        else:
            if not last_dash and result:
                result.append('-')
                last_dash = True
    slug = ''.join(result)
    return slug.strip('-')


def parse_frontmatter(raw: str) -> Tuple[Dict[str, str], str]:
    metadata: Dict[str, str] = {}
    if raw.startswith('---'):
        parts = raw.split('---', 2)
        if len(parts) == 3:
            body = parts[1]
            remainder = parts[2]
            for line in body.splitlines():
                stripped = line.strip()
                if not stripped or stripped.startswith('#'):
                    continue
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip().strip('"').strip("'")
            return metadata, remainder.lstrip('\n')
    return metadata, raw


def replace_imports(content: str) -> str:
    kept: List[str] = []
    for line in content.splitlines():
        if line.strip().startswith('import '):
            continue
        kept.append(line)
    return NEWLINE.join(kept)


def convert_admonitions(content: str) -> str:
    lines = content.splitlines()
    result: List[str] = []
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if stripped.startswith(':::'):
            token = stripped[3:].strip()
            kind = token
            title = ''
            if '[' in token and token.endswith(']'):
                kind, title = token.split('[', 1)
                title = title[:-1]
            kind = kind.lower()
            collected: List[str] = []
            index += 1
            while index < len(lines) and lines[index].strip() != ':::':
                collected.append(lines[index].rstrip())
                index += 1
            if index < len(lines):
                index += 1
            label = ADMONITION_LABELS.get(kind, kind.capitalize())
            if result and result[-1].strip():
                result.append('')
            header = f"> **{label}:**"
            if title:
                header = f"> **{label}:** {title.strip()}"
            result.append(header)
            for item in collected:
                if item.strip():
                    result.append(f"> {item.strip()}")
                else:
                    result.append('>')
            result.append('')
        else:
            result.append(line)
            index += 1
    return NEWLINE.join(result)


def extract_label(tag: str) -> str:
    marker = 'label='
    pos = tag.find(marker)
    if pos == -1:
        return 'Option'
    start = pos + len(marker)
    quote = tag[start]
    end = tag.find(quote, start + 1)
    if end == -1:
        return 'Option'
    return tag[start + 1:end]


def convert_tabs(content: str) -> str:
    content = content.replace('<Tabs>', '')
    content = content.replace('</Tabs>', '')
    content = content.replace('<Steps>', '')
    content = content.replace('</Steps>', '')
    result: List[str] = []
    index = 0
    while True:
        start = content.find('<TabItem', index)
        if start == -1:
            result.append(content[index:])
            break
        result.append(content[index:start])
        end = content.find('>', start)
        if end == -1:
            result.append(content[start:])
            break
        tag = content[start:end + 1]
        label = extract_label(tag)
        result.append(NEWLINE + '### ' + label + NEWLINE)
        index = end + 1
    content = ''.join(result)
    content = content.replace('</TabItem>', '')
    return content


def parse_attribute(tag: str, name: str) -> str:
    marker = name + '='
    pos = tag.find(marker)
    if pos == -1:
        return ''
    start = pos + len(marker)
    quote = tag[start]
    end = tag.find(quote, start + 1)
    if end == -1:
        return ''
    return tag[start + 1:end]


def convert_card_components(content: str) -> str:
    content = content.replace('<CardGrid>', '')
    content = content.replace('</CardGrid>', '')
    result: List[str] = []
    index = 0
    while True:
        start = content.find('<LinkCard', index)
        if start == -1:
            result.append(content[index:])
            break
        result.append(content[index:start])
        end = content.find('>', start)
        if end == -1:
            result.append(content[start:])
            break
        tag = content[start:end + 1]
        title = parse_attribute(tag, 'title') or 'Link'
        href = parse_attribute(tag, 'href') or '#'
        desc = parse_attribute(tag, 'description')
        line = f"- [{title}]({href})"
        if desc:
            line += f" — {desc}"
        result.append(line)
        index = end + 1
    content = ''.join(result)
    content = content.replace('</LinkCard>', '')
    return content


def make_alt_text(filename: str) -> str:
    base = Path(filename).stem
    base = base.replace('-', ' ').replace('_', ' ')
    base = ' '.join(part for part in base.split() if part)
    return base.title() if base else 'Image'


def convert_images(content: str) -> str:
    result: List[str] = []
    index = 0
    while True:
        start = content.find('<ImageComponent', index)
        if start == -1:
            result.append(content[index:])
            break
        result.append(content[index:start])
        end = content.find('/>', start)
        if end == -1:
            result.append(content[start:])
            break
        tag = content[start:end + 2]
        marker = "~/assets/images/"
        pos = tag.find(marker)
        if pos == -1:
            replacement = ''
        else:
            remainder = tag[pos + len(marker):]
            stop = remainder.find("'")
            if stop == -1:
                stop = remainder.find('"')
            filename = remainder[:stop]
            alt = make_alt_text(filename)
            replacement = f"![{alt}](src/assets/images/{filename})"
        result.append(replacement)
        index = end + 2
    content = ''.join(result)

    index = 0
    result = []
    while True:
        start = content.find('<MultipleImageComponent', index)
        if start == -1:
            result.append(content[index:])
            break
        result.append(content[index:start])
        end = content.find('/>', start)
        if end == -1:
            result.append(content[start:])
            break
        tag = content[start:end + 2]
        marker = "~/assets/images/"
        items: List[str] = []
        scan = 0
        while True:
            pos = tag.find(marker, scan)
            if pos == -1:
                break
            remainder = tag[pos + len(marker):]
            stop = remainder.find("'")
            if stop == -1:
                stop = remainder.find('"')
            filename = remainder[:stop]
            alt = make_alt_text(filename)
            items.append(f"![{alt}](src/assets/images/{filename})")
            scan = pos + len(marker) + stop
        replacement = NEWLINE.join(items)
        result.append(replacement)
        index = end + 2
    return ''.join(result)


def clean_extra_markup(content: str) -> str:
    return content.replace('<br />', NEWLINE)


def shift_headings_and_collect(content: str, doc_anchor: str) -> Tuple[str, Dict[str, str]]:
    lines = content.splitlines()
    new_lines: List[str] = []
    anchors: Dict[str, str] = {}
    in_code = False
    fence = ''
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            token = stripped[:3]
            if in_code and token == fence:
                in_code = False
                fence = ''
            else:
                in_code = True
                fence = token
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue
        if stripped.startswith('#'):
            count = 0
            while count < len(line) and line[count] == '#':
                count += 1
            text = line[count:].strip()
            level = min(count + 1, 6)
            slug = slugify(text)
            if slug:
                anchors[slug] = f"{doc_anchor}-{slug}"
                new_lines.append(f"<a id=\"{slug}\"></a>")
                new_lines.append(f"<a id=\"{doc_anchor}-{slug}\"></a>")
            new_lines.append('#' * level + ' ' + text)
        else:
            new_lines.append(line)
    return NEWLINE.join(new_lines), anchors


def convert_internal_links(content: str, anchor_map: Dict[str, str]) -> str:
    result: List[str] = []
    index = 0
    while True:
        start = content.find('](', index)
        if start == -1:
            result.append(content[index:])
            break
        result.append(content[index:start + 2])
        end = content.find(')', start + 2)
        if end == -1:
            result.append(content[start + 2:])
            break
        target = content[start + 2:end]
        prefix = ''
        suffix = ''
        if target.startswith('<') and target.endswith('>'):
            prefix = '<'
            suffix = '>'
            target = target[1:-1]
        if target.startswith('http://') or target.startswith('https://') or target.startswith('mailto:'):
            result.append(prefix + target + suffix)
        elif target.startswith('#'):
            result.append(prefix + target + suffix)
        else:
            norm = target.lstrip('/')
            norm = norm.rstrip('/')
            fragment = ''
            if '#' in norm:
                norm, fragment = norm.split('#', 1)
            key = norm
            if fragment:
                fragment_slug = slugify(fragment)
                if fragment_slug:
                    key = norm + '#' + fragment_slug
            anchor = anchor_map.get(key)
            if anchor:
                result.append(prefix + '#' + anchor + suffix)
            else:
                result.append(prefix + target + suffix)
        result.append(')')
        index = end + 1
    return ''.join(result)


def process_document(path: str) -> Tuple[Dict[str, str], str, Dict[str, str]]:
    raw_text = (DOC_ROOT / path).read_text(encoding='utf-8')
    metadata, content = parse_frontmatter(raw_text)
    content = replace_imports(content)
    content = convert_admonitions(content)
    content = convert_tabs(content)
    content = convert_card_components(content)
    content = convert_images(content)
    content = clean_extra_markup(content)
    content = content.strip()
    doc_anchor = slugify(path.replace('.mdx', '').replace('.md', ''))
    shifted, subanchors = shift_headings_and_collect(content, doc_anchor)
    return metadata, shifted, subanchors


def main() -> None:
    documents = []
    anchor_map: Dict[str, str] = {}

    for rel_path in DOC_PATHS:
        metadata, processed_content, subanchors = process_document(rel_path)
        title = metadata.get('title')
        if not title:
            raise ValueError(f"Missing title in {rel_path}")
        description = metadata.get('description', '').strip()
        doc_key = rel_path.replace('.mdx', '').replace('.md', '')
        doc_anchor = slugify(doc_key)
        anchor_map[doc_key] = doc_anchor
        for slug, anchor in subanchors.items():
            anchor_map[doc_key + '#' + slug] = anchor
            anchor_map.setdefault(slug, anchor)
        documents.append({
            'path': rel_path,
            'title': title,
            'description': description,
            'anchor': doc_anchor,
            'content': processed_content,
        })

    for doc in documents:
        doc['content'] = convert_internal_links(doc['content'], anchor_map)

    lines: List[str] = []
    lines.append('# CachyOS Wiki Offline Documentation')
    lines.append('')
    lines.append('This document consolidates the English-language CachyOS wiki into a single offline-friendly reference. Internal links now point to local anchors within this file.')
    lines.append('')
    lines.append('## Table of Contents')
    for doc in documents:
        lines.append(f"- [{doc['title']}](#{doc['anchor']})")
    lines.append('')

    for doc in documents:
        lines.append(f"<a id=\"{doc['anchor']}\"></a>")
        lines.append(f"<a id=\"{slugify(doc['title'])}\"></a>")
        lines.append(f"## {doc['title']}")
        if doc['description']:
            lines.append(f"*{doc['description']}*")
        if doc['content']:
            lines.append('')
            lines.append(doc['content'])
        lines.append('')

    OUTPUT_PATH.write_text(NEWLINE.join(lines).strip() + NEWLINE, encoding='utf-8')


if __name__ == '__main__':
    main()
