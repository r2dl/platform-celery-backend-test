FROM python:3-slim

WORKDIR /app

ENV FLASK_APP=main.py

ENV FLASK_ENV=development

RUN apt-get update

RUN apt-get install -y curl

RUN curl -sSL https://install.python-poetry.org | python3 - --version 1.1.13

RUN apt-get purge -y curl

ENV PATH="${PATH}:/root/.local/bin"

COPY pyproject.toml ./

RUN poetry lock

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$FLASK_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . .

EXPOSE 8000

#CMD export WORKERS=`expr $(nproc) \* 2 + 1` && gunicorn main:app -b 0.0.0.0:8000 --workers=$WORKERS --threads=4 --worker-class=gthread