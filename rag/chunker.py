"""RAG knowledge base — Markdown chunker."""

import re
import json
from pathlib import Path
from rag.config import SECTION_PATTERNS


def extract_title(text: str) -> str:
    """Extract H1 title from markdown text."""
    m = re.search(r"^#\s+\*\*(.+?)\*\*", text)
    return m.group(1).strip() if m else ""


def detect_language(filepath: Path) -> str:
    return "zh" if "zh-cn" in str(filepath) else "en"


def chunk_file(filepath: Path) -> list[dict]:
    """Split a markdown file into section-based chunks."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = filepath.read_text(encoding="gbk")

    title = extract_title(text)
    lang = detect_language(filepath)

    # Find all section headers with their positions
    sections = []
    for pattern in SECTION_PATTERNS:
        for m in re.finditer(pattern, text, re.MULTILINE):
            sections.append((m.start(), m.group(1), m.group(2).strip()))

    sections.sort(key=lambda x: x[0])

    if not sections:
        # No ## sections found — treat entire file as one chunk
        return [{
            "file": str(filepath.relative_to(filepath.parent.parent)),
            "title": title,
            "language": lang,
            "section_number": "",
            "section_title": title,
            "content": text.strip(),
        }]

    chunks = []
    for i, (pos, num, sec_title) in enumerate(sections):
        start = pos
        end = sections[i + 1][0] if i + 1 < len(sections) else len(text)
        content = text[start:end].strip()
        if len(content) < 50:
            continue

        chunks.append({
            "file": str(filepath.relative_to(filepath.parent.parent)),
            "title": title,
            "language": lang,
            "section_number": num,
            "section_title": sec_title,
            "content": content,
        })

    return chunks


def chunk_all(md_dir: Path, zh_dir: Path) -> list[dict]:
    """Chunk all markdown files in both directories."""
    all_chunks = []
    for directory in [md_dir, zh_dir]:
        if not directory.exists():
            continue
        for md_file in sorted(directory.glob("*.md")):
            chunks = chunk_file(md_file)
            all_chunks.extend(chunks)
    return all_chunks
