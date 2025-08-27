FROM python:3.13-slim AS builder
LABEL maintainer="Simone Locci <simonelocci88@gmail.com>"

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /build
RUN pip install --no-cache-dir poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --only main

FROM python:3.13-slim
LABEL maintainer="Simone Locci <simonelocci88@gmail.com>"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY app ./app
COPY log_config.yml .

EXPOSE 8000

USER appuser
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "log_config.yml"]
