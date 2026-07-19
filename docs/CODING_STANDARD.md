# AIRI Coding Standard

**Version:** 0.3.0  
**Last Updated:** July 2026

---

# Purpose

This document defines the coding standards used throughout the AIRI project.

The goal is to maintain a codebase that is simple, consistent, modular, and easy to evolve as AIRI continues to grow.

These guidelines apply to every module, package, and future contribution.

---

# Core Philosophy

The AIRI codebase follows a few fundamental principles:

- Simplicity over cleverness.
- Readability over brevity.
- Consistency over personal preference.
- Build incrementally.
- Refactor only when a clear pattern emerges.
- Every module should be easy to understand in isolation.

---

# Project Structure

Each folder represents one domain of responsibility.

Example:

airi/

├── brain/

├── personality/

├── relationship/

├── memory/

├── state/

├── speech/

└── ...

Avoid creating generic folders that contain unrelated responsibilities.

---

# Architecture Rules

## One Folder = One Domain

Each package should represent one domain.

Examples:

- Brain
- Personality
- Memory
- Relationship
- State

---

## One Class = One Responsibility

Each class should have one clear responsibility.

Avoid classes that manage multiple unrelated concerns.

---

## Composition Root

The `Airi` class is the Composition Root.

Its responsibilities include:

- Creating dependencies
- Loading configuration
- Injecting dependencies into modules

Core modules should never instantiate other core modules directly.

---

# Dependency Injection

Always inject dependencies through constructors.

Good:

```python
brain = Brain(
    personality=personality,
    relationship=relationship,
    llm=llm,
)
```

Avoid:

```python
class Brain:
    def __init__(self):
        self.personality = Personality.load()
```

Rule:

> Don't Create, Receive.

---

# Configuration Pattern

Each configuration belongs to exactly one domain object.

Example:

Personality
↕
personality.json

Relationship
↕
relationship.json

Settings
↕
settings.json

Avoid creating a global configuration object that knows everything.

---

# Imports

Prefer absolute imports.

Good:

```python
from airi.personality import Personality
```

Avoid:

```python
from personality import Personality
```

or

```python
from ..personality import Personality
```

---

# Public API

Every package should expose its public interface through `__init__.py`.

Example:

```python
from airi.brain import Brain
```

instead of

```python
from airi.brain.brain import Brain
```

---

# Dataclasses

Configuration objects should use dataclasses.

Preferred:

```python
@dataclass(slots=True)
```

Benefits:

- Cleaner code
- Better performance
- Reduced memory usage

---

# Type Hints

Always use type hints for:

- Function parameters
- Return values
- Public methods

Example:

```python
def think(self, message: str) -> str:
```

---

# Documentation

Every public class should include a docstring.

Every public method should explain its purpose when the behavior is not immediately obvious.

Write comments to explain **why**, not **what**.

Good:

```python
# Brain receives dependencies from the Composition Root
```

Avoid:

```python
# Create Brain object
```

---

# Naming Convention

## Classes

Use PascalCase.

Example:

- Brain
- Personality
- MemoryManager

---

## Functions

Use snake_case.

Example:

- load()
- think()
- remember()

---

## Variables

Use descriptive snake_case.

Good:

```python
conversation_history
```

Avoid:

```python
data
```

---

## Constants

Use UPPER_CASE.

Example:

```python
MAX_MEMORY_SIZE
```

---

# Design Principles

Whenever making architectural decisions, prefer the following:

- Prefer composition over inheritance.
- Keep modules small.
- Avoid premature abstraction.
- Write code for future maintainers.
- Minimize coupling.
- Maximize readability.
- Keep dependencies explicit.

---

# Evolution Before Optimization

Do not optimize code prematurely.

Implement a clear and simple solution first.

Only optimize when there is measurable evidence that the current design has become a limitation.

---

# Testing Philosophy

After each meaningful refactor:

- Ensure the application still runs.
- Prefer small, incremental changes.
- Avoid large refactors without verification.

Small improvements are safer than massive rewrites.

---

# Final Notes

AIRI is expected to evolve for a long time.

Every contribution should prioritize:

- Simplicity
- Readability
- Maintainability
- Modularity
- Long-term growth

Clean code today makes future growth easier.