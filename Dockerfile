# BASE STAGE
FROM python:3.11 AS base_image

ENV POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y curl gcc libpq-dev && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --only main

COPY fastapi_hello_world fastapi_hello_world

COPY env.toml env.toml



# STAGE "image_for_running_tests_in_github_actions"
FROM base_image AS image_for_running_tests_in_github_actions

COPY pytest.ini pytest.ini

RUN poetry install --only tests



# STAGE "prod_image"
FROM base_image AS prod_image

COPY static static

# needed for google app engine (you should not change it)
EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "fastapi_hello_world.app:app", "--host", "0.0.0.0", "--port", "8080"]
