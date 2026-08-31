from __future__ import annotations

import re
from pathlib import Path


_META_KEYS = (
    "title",
    "description",
    "canonical",
    "ogTitle",
    "ogDescription",
    "ogUrl",
)


def _unescape_js_string(value: str) -> str:
    return (
        value.replace(r"\/", "/")
        .replace(r"\"", '"')
        .replace(r"\n", "\n")
        .replace(r"\t", "\t")
        .replace(r"\\", "\\")
    )


def parse_content_ts(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    meta: dict[str, str] = {}
    for key in _META_KEYS:
        match = re.search(
            rf'["\']?{key}["\']?\s*:\s*"((?:\\.|[^"\\])*)"',
            text,
        )
        if match:
            meta[key] = _unescape_js_string(match.group(1))

    html = ""
    tpl = re.search(r"export const mainHtml = `([\s\S]*?)`;", text)
    if tpl:
        html = tpl.group(1)
    else:
        quoted = re.search(r'export const mainHtml = "([\s\S]*?)";', text)
        if quoted:
            html = _unescape_js_string(quoted.group(1))

    return {"meta": meta, "main_html": html}
