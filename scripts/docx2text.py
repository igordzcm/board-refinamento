#!/usr/bin/env python3
"""Extract plain paragraph text from one or more .docx files (word/document.xml only —
no headers/footers/tracked-changes markup). No external dependencies.

Usage:
    python docx2text.py file1.docx [file2.docx ...]

Prints each file's text to stdout under a "===== <path> =====" header.
"""
import sys
import zipfile
import xml.etree.ElementTree as ET

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract(path):
    with zipfile.ZipFile(path) as z:
        with z.open("word/document.xml") as f:
            tree = ET.parse(f)
    root = tree.getroot()
    lines = []
    for p in root.iter(f"{W_NS}p"):
        line = "".join(t.text or "" for t in p.iter(f"{W_NS}t"))
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docx2text.py <file.docx> [more.docx ...]", file=sys.stderr)
        sys.exit(1)
    for path in sys.argv[1:]:
        print(f"===== {path} =====")
        try:
            print(extract(path))
        except Exception as e:
            print(f"[erro ao extrair {path}: {e}]", file=sys.stderr)
        print()
