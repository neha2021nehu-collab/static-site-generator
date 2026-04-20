from staticsg.base import Theme
from staticsg.models import BuildContext

class LightTheme(Theme):
    @property
    def name(self) -> str:
        return "light"
    
    def apply(self, html: str, ctx: BuildContext) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>My Site</title>
<style>
body {{ font-family: sand-serif; max-width: 800px;
margin: 0 auto; padding: 2rem; background: #fff; color: #111;}}
</style>
</head>
<body>
{html}
</body>
</html>"""
    
class DarkTheme(Theme):
    @property
    def name(self) -> str:
        return "dark"
    
    def apply(self, html: str, ctx: BuildContext) -> str:
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>My Site</title>
  <style>
    body {{ font-family: sans-serif; max-width: 800px;
            margin: 0 auto; padding: 2rem; background: #1a1a1a; color: #e0e0e0; }}
    h1, h2, h3 {{ color: #ffffff; }}
  </style>
</head>
<body>
{html}
</body>
</html>"""