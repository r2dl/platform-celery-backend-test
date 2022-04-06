FROM python:3-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev

RUN pip uninstall -y poetry

ENV FLASK_APP=main.py

COPY . .

EXPOSE 8000

CMD export WORKERS=`expr $(nproc) \* 2 + 1` && gunicorn main:app -b 0.0.0.0:8080 --workers=$WORKERS --threads=4 --worker-class=gthread
