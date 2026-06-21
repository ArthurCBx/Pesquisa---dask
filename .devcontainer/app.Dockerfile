# Linux dev environment with Python 3.13, uv, Node.js, and just
FROM mcr.microsoft.com/devcontainers/python:3.13

# Installation of uv
RUN pip install --upgrade pip
RUN pip install uv

# Configuration of VENV
ENV UV_LINK_MODE=copy
ENV TZ=America/Sao_Paulo

# Creation and Properties of VENV
RUN mkdir -p pesquisa-dask
WORKDIR /pesquisa-dask

COPY pyproject.toml uv.lock* ./

# Install system deps
RUN --mount=type=cache,target=/root/.cache/uv,uid=1000,gid=1000 \
    bash -c 'set -euo pipefail; \
    if [ -f uv.lock ]; then \
        uv sync --no-install-project --all-extras --frozen; \
    else \
        uv sync --no-install-project --all-extras; \
    fi'
