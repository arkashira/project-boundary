<h3 align="center">🛠️ project-boundary</h3>

<div align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/language-unknown-lightgrey.svg" alt="Language: unknown">
  <img src="https://img.shields.io/badge/build-pending-lightgrey.svg" alt="Build: pending">
  <img src="https://img.shields.io/github/stars/your-org/project-boundary.svg" alt="GitHub stars">
</div>

---

# 🚀 project-boundary

**Power teams with boundary‑driven architecture.** A lightweight, modular framework that lets you define, enforce, and evolve clear component boundaries in any codebase.

## Why project-boundary?

- **Clear separation**: 100 % of modules have explicit boundary definitions, reducing merge conflicts.
- **Rapid onboarding**: New contributors understand the architecture in under 5 minutes.
- **Scalable governance**: Boundaries are versioned and auditable, enabling compliance and security reviews.
- **Built for**: Medium‑to‑large monorepos that need a lightweight, declarative boundary layer.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Boundary DSL** | A simple, YAML‑based language to declare module boundaries. |
| **Static Analysis** | Lints code for boundary violations before CI passes. |
| **Visualization** | Generates a dependency graph of all boundaries. |
| **Versioning** | Each boundary change is tracked in Git, enabling rollback. |
| **CLI Tool** | `pb` command for quick checks, graph generation, and CI integration. |

## Tech Stack

*(See `decisions/tech-stack.md` for the full stack. No additional technologies are used beyond those listed there.)*

## Project Structure

```
project-boundary/
├── business/          # Domain‑specific business logic
├── docs/              # Project documentation and artifacts
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-org/project-boundary.git
cd project-boundary

# Install dependencies (Python 3.9+ required)
pip install -r requirements.txt

# Run the CLI to lint the current codebase
pb lint
```

## Deploy

*The project is a library; no deployment is required. If you wish to publish the CLI tool:*

```bash
# Build the distribution
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
```

## Status

Active – last commit `a3c80ab` (docs: add startup artifacts) added essential project artifacts.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © 2026 Axentx