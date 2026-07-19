# AIRI Architecture

**Version:** 0.3.0  
**Last Updated:** July 2026

---

# Introduction

AIRI is an AI companion project designed to grow naturally alongside Papah.

Rather than being built as a traditional chatbot, AIRI is designed as an independent AI with her own identity, memories, relationship, and personality. Every architectural decision aims to support long-term growth instead of simply adding more features.

The objective of this architecture is to keep the system modular, understandable, and easy to evolve over time.

---

# Core Philosophy

The architecture follows several core principles:

- Every module has exactly one responsibility.
- AIRI grows by adding new "organs", not by creating larger classes.
- Dependencies are created only once and injected where needed.
- Configuration belongs to its own domain object.
- Simplicity is preferred over unnecessary abstraction.

---

# Organ Architecture

Each package inside AIRI represents one part of AIRI herself.

| Module | Responsibility |
|---------|----------------|
| App | Application metadata |
| Personality | AIRI's identity |
| Relationship | AIRI's relationship with Papah |
| Settings | Runtime behaviour |
| Prompts | Frequently used dialogue |
| Brain | Thinking process |
| Memory | Experiences and memories |
| Listener | Voice input |
| State *(Future)* | Current internal condition |
| Emotion *(Future)* | Emotional system |

This architecture allows AIRI to evolve naturally by introducing new modules without affecting existing ones.

---

# Composition Root

The `Airi` class acts as the Composition Root.

Its responsibility is to create every dependency exactly once and inject them into the modules that require them.

Example:

Airi

↓

App

↓

Personality

↓

Relationship

↓

Settings

↓

Prompts

↓

Brain

↓

Memory

↓

Listener

No module should instantiate another core dependency directly.

Instead, every dependency is provided by `Airi`.

---

# Brain

The Brain coordinates AIRI's thinking process.

Current responsibilities:

- Receive user message
- Build context
- Build prompt
- Call LLM
- Return AIRI's response

Current dependencies:

- Personality
- Relationship
- BaseLLM

Future versions will also receive:

- State
- Memory

---

# Configuration Layer

Configuration is separated into independent domain objects.

Current configuration:

config/

├── app.json

├── personality.json

├── relationship.json

├── settings.json

└── prompts.json

Each JSON file is owned by exactly one domain object.

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

This prevents the project from relying on a large "God Config" object.

---

# Dependency Injection

Core dependencies are never instantiated inside feature modules.

Instead:

Airi

↓

Creates dependency

↓

Injects dependency

↓

Module uses dependency

This makes the project easier to test, maintain, and extend.

---

# Future Architecture

The next major architectural milestones are:

- State System
- PromptBuilder 2.0
- Memory Integration
- Emotion System
- Vision
- Speech Output
- Real LLM Integration

Each milestone should introduce a new module instead of expanding existing ones whenever possible.

---

# Final Notes

AIRI is designed to grow gradually.

The architecture should always prioritize:

- readability,
- maintainability,
- modularity,
- long-term evolution.

The goal is not simply to build a chatbot.

The goal is to build an AI that can continue growing together with Papah.