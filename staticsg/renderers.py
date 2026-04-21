from markdown_it import MarkdownIt

from staticsg.base import Renderer
from staticsg.models import BuildContext, Document

class HTMLRenderer(Renderer):
    # def render(self, doc: Document, ctx: BuildContext) -> str:
    #     lines = doc.content.splitlines()
    #     html_lines = []
    #     for line in lines:
    #         if line.startswith("# "):
    #             html_lines.append(f"<h1>{line[2:].strip()}</h1>")
    #         elif line.startswith("## "):
    #             html_lines.append(f"<h2>{line[3:].strip()}</h2>")
    #         elif line.startswith("### "):
    #             html_lines.append(f"<h3>{line[4:].strip()}</h4>")
    #         elif line.strip() == "":
    #             html_lines.append("")
    #         else:
    #             html_lines.append(f"<p>{line.strip()}</p>")
    #     return "\n".join(html_lines)

    def __init__(self):
        #enable tables and strikethrough on top of CommonMark
        self._md = MarkdownIt("commonmark").enable("table")
    
    def render(self, doc: Document, ctx: BuildContext) -> str:
        return self._md.render(doc.content)