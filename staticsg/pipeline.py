from pathlib import Path

from staticsg.base import PluginRegistry
from staticsg.models import BuildContext


class BuildPipeline:

    def run(self, ctx: BuildContext) -> None:
        ctx.output_dir.mkdir(parents=True, exist_ok=True)

        # For now we use the first registered renderer.
        # A future phase can select renderers the way we select parsers.
        renderers = PluginRegistry.all_renderers()
        if not renderers:
            raise RuntimeError("No renderers registered. Did you import ssg.renderers?")
        renderer = renderers[0]

        theme = PluginRegistry.get_theme(ctx.theme)

        source_files = list(ctx.source_dir.iterdir())
        if not source_files:
            print(f"Warning: no files found in '{ctx.source_dir}'")
            return

        built = 0
        skipped = 0

        for path in source_files:
            try:
                parser = PluginRegistry.get_for_path(path)
            except ValueError:
                print(f"  Skipping '{path.name}' — no parser registered for '{path.suffix}'")
                skipped += 1
                continue

            doc = parser.parse(path)
            html_fragment = renderer.render(doc, ctx)
            full_page = theme.apply(html_fragment, ctx)

            out_path = ctx.output_dir / f"{doc.slug}.html"
            out_path.write_text(full_page, encoding="utf-8")
            print(f"  Built '{doc.slug}.html' ← '{path.name}'")
            built += 1

        print(f"\nDone. {built} built, {skipped} skipped.")