from pathlib import Path
from staticsg.base import Parser
from staticsg.models import Document

class MarkdownParser(Parser):

    def can_parse(self, path: Path) -> bool:
        return path.suffix == ".md"
    def parse(self, path: Path) -> Document:
        raw = path.read_text(encoding="utf-8")
        title = self._extract_title(raw, fallback=path.stem)
        slug = path.stem
        return Document(
            title=title,
            content=raw,
            source_path=path,
            slug=slug,
        )
    def _extract_title(self, raw: str, fallback: str) -> str:
        for line in raw.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return fallback