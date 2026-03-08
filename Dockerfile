FROM ghcr.io/astral-sh/uv:0.10.9-python3.12-trixie

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY src ./src
COPY README.md ./

RUN uv sync --no-dev --frozen --no-install-project

CMD ["uv", "run", "start"]

