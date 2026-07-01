# ADR-001 — Configuration System

## Status

Accepted

---

## Context

The Football Intelligence Platform requires a centralized configuration system
to manage:

- API credentials
- Database settings
- Logging configuration
- Project paths

The configuration must be:

- Secure
- Typed
- Easy to maintain
- Suitable for research and production

---

## Decision

We use:

- Pydantic Settings
- Environment variables (.env)
- src layout
- uv as package manager

Project paths are centralized inside:

src/fip/config/paths.py

Application settings are centralized inside:

src/fip/config/settings.py

A singleton `settings` object is used throughout the project.

---

## Consequences

Advantages:

- Strong typing
- Easy configuration
- Secure API key management
- Scalable architecture
- Clean imports

Trade-offs:

- Slightly more initial setup
- Requires editable installation during development

---

## Date

2026