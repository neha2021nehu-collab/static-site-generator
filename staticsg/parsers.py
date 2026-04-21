import frontmatter
from pathlib import Path

from staticsg.base import Parser
from staticsg.models import Document

class MarkdownParser(Parser):

    def can_parse(self, path: Path) -> bool:
        return path.suffix == ".md"
    def parse(self, path: Path) -> Document:
        post = frontmatter.load(str(path))

        #Title priority: frontmatter > first # heading > filename stem
        title = (
            post.metadata.get("title")
            or self._extract_title(post.content, fallback=path.stem)
        )

        # raw = path.read_text(encoding="utf-8")
        # title = self._extract_title(raw, fallback=path.stem)
        # slug = path.stem
        slug = post.metadata.get("slug") or path.stem

        return Document(
            title=title,
            content=post.content,
            source_path=path,
            slug=slug,
            metadata=dict(post.metadata),
        )
    def _extract_title(self, raw: str, fallback: str) -> str:
        for line in raw.splitlines():
            if line.startswith("# "):
                return line[2:].strip()
        return fallback