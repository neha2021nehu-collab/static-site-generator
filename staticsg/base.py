from abc import ABC, abstractmethod
from pathlib import Path

from staticsg.models import Document


class PluginRegistry:
    _parsers: list = []
    _renderers: list = []
    _themes: list = []

    @classmethod
    def register_parser(cls, parser_instance):
        cls._parsers.append(parser_instance)

    @classmethod
    def register_renderer(cls, instance):
        cls._renderers.append(instance)

    @classmethod
    def register_theme(cls, instance):
        cls._themes.append(instance)

    @classmethod
    def get_for_path(cls, path: Path):
        for parser in cls._parsers:
            if parser.can_parse(path):
                return parser
        raise ValueError(
            f"No parser found for '{path.suffix}' files. "
            f"Registered parsers: {[type(p).__name__ for p in cls._parsers]}"

    
        )
    
    @classmethod
    def get_theme(cls, name:str):
        for theme in cls._themes:
            if theme.name == name:
                return theme
        raise ValueError(
            f"No theme named '{name}'."
            f"Registered: {[t.name for t in cls._themes]}"
        )
    

    @classmethod
    def all_parsers(cls):
        return list(cls._parsers)
    
    @classmethod
    def all_renderers(cls): return list(cls._renderers)

    @classmethod
    def all_themes(cls): return list(cls._themes)


class Parser(ABC):

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Only register concrete classes, not abstract intermediates.
        # A class is concrete when it has no remaining abstract methods.
        if not getattr(cls, "__abstractmethods__", None):
            PluginRegistry.register_parser(cls())

    @abstractmethod
    def can_parse(self, path: Path) -> bool: ...

    @abstractmethod
    def parse(self, path: Path) -> Document: ...

class Renderer(ABC):
    """Contract every renderer plugin must fulfill."""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "_-abstractmethods__", None):
            PluginRegistry.register_renderer(cls())
    @abstractmethod
    def render(self, doc: Document, ctx: "BuildContext") -> str:
        """Convert a Document into an HTML string."""
        ...

class Theme(ABC):
    """Contract every theme plugin must fulfill."""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "__abstractmethods__", None):
            PluginRegistry.register_theme(cls())
    @property
    @abstractmethod
    def name(self) -> str:
        """The theme's identifier, e.g. 'dark' or 'light' ."""
        ...
    @abstractmethod
    def apply(self, html:str, ctx:"BuildContext") -> str:
        """Wrap rendered HTML in a full page with this theme's styling."""
        ...