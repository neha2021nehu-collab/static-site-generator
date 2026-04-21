# from staticsg.base import Theme
# from staticsg.models import BuildContext

# class LightTheme(Theme):
#     @property
#     def name(self) -> str:
#         return "light"
    
#     def apply(self, html: str, ctx: BuildContext) -> str:
#         return f"""<!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <title>My Site</title>
# <style>
# body {{ font-family: sand-serif; max-width: 800px;
# margin: 0 auto; padding: 2rem; background: #fff; color: #111;}}
# </style>
# </head>
# <body>
# {html}
# </body>
# </html>"""
    
# class DarkTheme(Theme):
#     @property
#     def name(self) -> str:
#         return "dark"
    
#     def apply(self, html: str, ctx: BuildContext) -> str:
#         return f"""<!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8">
#   <title>My Site</title>
#   <style>
#     body {{ font-family: sans-serif; max-width: 800px;
#             margin: 0 auto; padding: 2rem; background: #1a1a1a; color: #e0e0e0; }}
#     h1, h2, h3 {{ color: #ffffff; }}
#   </style>
# </head>
# <body>
# {html}
# </body>
# </html>"""



from staticsg.base import Theme
from staticsg.models import BuildContext


_BASE = """<!DOCTYPE html>
<html lang="en" data-theme="{theme}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css"
  >
  <style>
    body {{ max-width: 860px; margin: 0 auto; }}
    pre code {{ font-size: 0.875rem; }}
    table {{ width: 100%; }}
    .meta {{ color: var(--pico-muted-color); font-size: 0.875rem; margin-bottom: 2rem; }}
    .tags span {{
      display: inline-block;
      background: var(--pico-primary-background);
      color: var(--pico-primary-inverse);
      border-radius: 4px;
      padding: 2px 8px;
      margin-right: 4px;
      font-size: 0.75rem;
    }}
  </style>
</head>
<body>
  <main class="container">
    {meta_block}
    {html}
  </main>
</body>
</html>"""


def _meta_block(ctx: BuildContext, doc_metadata: dict) -> str:
    """Build the author / date / tags block from frontmatter metadata."""
    if not doc_metadata:
        return ""

    parts = []
    author = doc_metadata.get("author")
    date = doc_metadata.get("date")
    tags = doc_metadata.get("tags", [])

    if author or date:
        line = []
        if author:
            line.append(f"By {author}")
        if date:
            line.append(date.strftime("%B %d, %Y"))
        parts.append(" · ".join(line))

    if tags:
        tag_html = " ".join(f"<span>{t}</span>" for t in tags)
        parts.append(f'<div class="tags">{tag_html}</div>')

    if not parts:
        return ""

    return f'<div class="meta">{"<br>".join(parts)}</div>'


class LightTheme(Theme):

    @property
    def name(self) -> str:
        return "light"

    def apply(self, html: str, ctx: BuildContext, metadata: dict = None) -> str:
        meta = _meta_block(ctx, metadata or {})
        title = (metadata or {}).get("title", "My Site")
        return _BASE.format(
            theme="light",
            title=title,
            meta_block=meta,
            html=html,
        )


class DarkTheme(Theme):

    @property
    def name(self) -> str:
        return "dark"

    def apply(self, html: str, ctx: BuildContext, metadata: dict = None) -> str:
        meta = _meta_block(ctx, metadata or {})
        title = (metadata or {}).get("title", "My Site")
        return _BASE.format(
            theme="dark",
            title=title,
            meta_block=meta,
            html=html,
        )