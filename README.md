# Static Site Generator (SSG)

A command-line static site generator built in Python — designed to demonstrate
production-grade architecture using Abstract Base Classes, a plugin registry
with auto-registration, and a clean separation of concerns across parsing,
rendering, and theming.

## What it does

Takes `.md` files from a content directory, runs them through a configurable
pipeline, and produces themed `.html` files in an output directory.

```bash
python main.py build --theme dark --source content --out dist
```

## Architecture

The project is built around three plugin contracts, each enforced as an ABC:

- **Parser** — reads a source file and produces a `Document`
- **Renderer** — converts a `Document` into an HTML fragment
- **Theme** — wraps an HTML fragment in a full styled page

Plugins register themselves automatically via `__init_subclass__` the moment
they are defined. The `BuildPipeline` never references concrete classes — it
speaks only to the `PluginRegistry`.
