FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest || true

ENTRYPOINT ["python", "levenshtein_cli.py"]
