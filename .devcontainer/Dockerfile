# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
ARG VARIANT="3.12-bullseye"
FROM mcr.microsoft.com/devcontainers/python:1-${VARIANT}

# Poetry
ARG POETRY_VERSION="1.2.0"
RUN su vscode -c "curl -sSL https://install.python-poetry.org | POETRY_VERSION=${POETRY_VERSION} python3 -"