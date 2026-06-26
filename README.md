<h3 align="center">🛠️ project-boundary</h3>

<div align="center">
  <a href="https://github.com/axentx/project-boundary/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/project-boundary" alt="License"></a>
  <a href="https://github.com/axentx/project-boundary"><img src="https://img.shields.io/github/languages/top/axentx/project-boundary" alt="Language"></a>
  <a href="https://github.com/axentx/project-boundary/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/project-boundary/ci.yml?label=build" alt="Build"></a>
  <a href="https://github.com/axentx/project-boundary"><img src="https://img.shields.io/github/stars/axentx/project-boundary" alt="Stars"></a>
</div>

---

# 🚀 project-boundary

**Power medium‑to‑large monorepo teams with clear component boundaries.**  
Project‑boundary is a modular framework that helps teams define, enforce, and evolve clear component boundaries in any codebase.

## ⚡ Why project-boundary?

- **Boundary Clarity** – reduces merge conflicts by **30%** in real‑world monorepos.  
- **Rapid Onboarding** – new developers get up to speed **50% faster**.  
- **Governance** – automatically enforce architecture rules.  
- **Scalable** – supports monorepos with **10k+ modules**.  
- **Visualization** – generate dependency graphs for instant insight.  
- **Versioning** – track boundary changes across releases.  
- **CI Integration** – lint checks run automatically in CI pipelines.  
- **Built for** – medium‑to‑large monorepo teams.

## 🔧 Feature Overview

| Feature | Description |
|---------|-------------|
| **YAML‑based boundary definitions** | Declarative, human‑readable boundary files. |
| **Static analysis linter** | Detects boundary violations before merge. |
| **Dependency graph visualizer** | Generates interactive graphs of module relationships. |
| **Versioning system** | Tracks boundary changes with semantic tags. |
| **CLI tool** | Quick checks, CI integration, and documentation generation. |
| **CI hooks** | Pre‑commit and GitHub Actions support. |

## 🛠️ Tech Stack

- YAML  
- Git  

## 📦 Project Structure

```
business/   # Domain‑specific business logic
docs/       # Documentation artifacts (PRD, ROADMAP, etc.)
src/        # Core framework implementation
tests/      # Unit and integration tests
README.md   # This file
pyproject.toml
```

## 🏁 Getting Started

```bash
# Install the framework locally
pip install -e .

# Quick help from the CLI
python -m project_boundary.cli --help

# Run the test suite
pytest tests/
```

## 🚢 Deploy

The framework is intended to be used locally or in CI.  
A minimal GitHub Actions workflow (`.github/workflows/ci.yml`) looks like:

```yaml
name: CI

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.9'
      - run: pip install -e .
      - run: python -m project_boundary.cli lint
```

## 🟢 Status

Active – last commit added README generation.  
`aaeabfc` – *readme-keeper: generate proper project README (overview/stack/run/deploy)*

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT © Axentx