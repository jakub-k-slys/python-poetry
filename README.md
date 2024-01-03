# Python template with Poetry, FastAPI and SQLAlchemy
The template sets up a coding environment for Python language. It uses poetry for package and dependency management.

The following template uses:
* [Poetry](https://python-poetry.org) is the Python packaging and dependency management,
* [SQLAlchemy](https://www.sqlalchemy.org) is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL,
* [FastAPI](https://fastapi.tiangolo.com) is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

# Running the main module
To run the main module simply issue:
```python
poetry run main
```

# Devcontainer
The project contains devcontainer configuration and can be easily run on GitHub Codespaces. To use devcontainer, install the VSCode extension Remote - Containers.

In addition to the primary container, an additional container supporting PostgreSQL is launched.
