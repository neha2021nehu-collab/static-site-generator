import click

from staticsg import parsers, renderers, themes  # triggers auto-registration
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
    pipeline = BuildPipeline()
    pipeline.run(ctx)