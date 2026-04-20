from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Document:
    title: str
    content: str
    source_path: Path
    slug: str
    metadata: dict = field(default_factory=dict)

@dataclass
class BuildContext:
    theme: str
    source_dir: Path
    output_dir: Path
    options: dict = field(default_factory=dict)