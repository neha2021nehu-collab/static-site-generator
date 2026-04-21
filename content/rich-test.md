---
title: Rich Markdown Test
author: Neha
date: 2025-04-21
tags: [test, markdown, rendering]
---

# Rich Markdown Test

This page tests every feature the renderer now supports.

## Text Formatting

This is **bold text**, this is *italic text*, and this is ***bold and italic***.

This is `inline code` inside a sentence.

This is ~~strikethrough~~ text.

## Lists

Unordered list:

- Python
- Architecture
- Static Site Generators

Ordered list:

1. Parse the Markdown
2. Render to HTML
3. Apply the theme
4. Write to disk

## Links and Images

[Visit my GitHub](https://github.com/neha2021nehu-collab)

![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## Blockquote

> The best way to learn architecture is to build something
> and then try to extend it without breaking it.

## Code Block

```python
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, path) -> Document:
        ...
```

## Table

| Feature        | Phase 1 | Phase 2 |
|----------------|---------|---------|
| Frontmatter    | No      | Yes     |
| Full Markdown  | No      | Yes     |
| Pico CSS       | No      | Yes     |
| File watcher   | No      | Yes     |

## Horizontal Rule

---

End of test.