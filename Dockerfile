FROM python:3-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

RUN pip uninstall -y poetry

COPY . .

EXPOSE 8000
