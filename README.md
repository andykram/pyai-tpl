# Trajnor

An LLM-Agent Framework for Trajectory Modeling using pydantic-ai.

## Features

- Python 3.14 support
- Built with `uv` for fast package management
- Interactive CLI REPL powered by pydantic-ai
- Comprehensive test suite with pytest

## Installation

This project uses `uv` for dependency management. To install dependencies:

```bash
uv sync
```

## Usage

### Running the REPL

To start the interactive REPL:

```bash
uv run python main.py
```

Or directly run the REPL module:

```bash
uv run python -m src.trajnor.repl
```

In the REPL, you can interact with the AI agent:
- Type your messages and press Enter
- Type `exit` or `quit` to exit
- Press Ctrl+C to exit

## Development

### Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

#### Linting

Check code for issues:

```bash
uv run ruff check .
```

Auto-fix issues:

```bash
uv run ruff check --fix .
```

#### Formatting

Check code formatting:

```bash
uv run ruff format --check .
```

Format code:

```bash
uv run ruff format .
```

### Running Tests

Run all tests:

```bash
uv run pytest
```

Run tests with verbose output:

```bash
uv run pytest -v
```

Run tests with coverage:

```bash
uv run pytest --cov=src/trajnor
```

### CI/CD

This project uses GitHub Actions for continuous integration:

- **Tests**: Runs on all PRs and pushes to main
- **CodeQL Security Analysis**: Runs on all PRs and pushes to main, plus weekly scans
- **Lint and Format**: Runs on all PRs and pushes to main

### Project Structure

```
trajnor/
├── src/
│   └── trajnor/
│       ├── __init__.py
│       └── repl.py          # CLI REPL implementation
├── tests/
│   ├── __init__.py
│   └── test_repl.py         # REPL tests
├── main.py                   # Entry point
├── pyproject.toml            # Project configuration
└── README.md                 # This file
```

## License

MIT
