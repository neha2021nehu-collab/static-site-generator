# import time
# import click

# from staticsg import parsers, renderers, themes  # triggers auto-registration
# from staticsg.models import BuildContext
# from staticsg.pipeline import BuildPipeline
# from pathlib import Path


# @click.group()
# def cli():
#     """SSG — a simple static site generator."""
#     pass


# @cli.command()
# @click.option("--theme",  default="light", show_default=True, help="Theme name to apply.")
# @click.option("--source", default="content", show_default=True, help="Source content directory.")
# @click.option("--out",    default="dist",    show_default=True, help="Output directory.")
# def build(theme: str, source: str, out: str) -> None:
#     """Build the site from SOURCE into OUT using THEME."""
#     ctx = BuildContext(
#         theme=theme,
#         source_dir=Path(source),
#         output_dir=Path(out),
#     )

#     click.echo(f"Building with theme='{theme}', source='{source}', out='{out}'")
#     pipeline = BuildPipeline()
#     pipeline.run(ctx)


import time
import click

from staticsg import parsers, renderers, themes
from staticsg.models import BuildContext
from staticsg.pipeline import BuildPipeline
from pathlib import Path


@click.group()
def cli():
    """SSG — a simple static site generator."""
    pass


@cli.command()
@click.option("--theme",  default="light", show_default=True, help="Theme name to apply.")
@click.option("--source", default="content", show_default=True, help="Source content directory.")
@click.option("--out",    default="dist",    show_default=True, help="Output directory.")
def build(theme: str, source: str, out: str) -> None:
    """Build the site from SOURCE into OUT using THEME."""
    ctx = BuildContext(
        theme=theme,
        source_dir=Path(source),
        output_dir=Path(out),
    )
    click.echo(f"Building with theme='{theme}', source='{source}', out='{out}'")
    BuildPipeline().run(ctx)


@cli.command()
@click.option("--theme",  default="light", show_default=True, help="Theme name to apply.")
@click.option("--source", default="content", show_default=True, help="Source content directory.")
@click.option("--out",    default="dist",    show_default=True, help="Output directory.")
def watch(theme: str, source: str, out: str) -> None:
    """Watch SOURCE for changes and rebuild automatically."""
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    ctx = BuildContext(
        theme=theme,
        source_dir=Path(source),
        output_dir=Path(out),
    )

    # Run an initial build so dist/ is populated before watching
    click.echo(f"Initial build...")
    BuildPipeline().run(ctx)
    click.echo(f"Watching '{source}' for changes. Press Ctrl+C to stop.\n")

    class RebuildHandler(FileSystemEventHandler):
        def __init__(self):
            self._last_run = 0.0

        def on_modified(self, event):
            self._trigger(event.src_path)

        def on_created(self, event):
            self._trigger(event.src_path)

        def _trigger(self, src_path: str):
            # Debounce — ignore events within 0.5s of the last build
            now = time.time()
            if now - self._last_run < 0.5:
                return
            self._last_run = now

            changed = Path(src_path).name
            click.echo(f"\nChange detected in '{changed}' — rebuilding...")
            try:
                BuildPipeline().run(ctx)
            except Exception as e:
                click.echo(f"Build error: {e}")

    observer = Observer()
    observer.schedule(RebuildHandler(), path=source, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        click.echo("\nWatcher stopped.")

    observer.join()