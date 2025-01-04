ARG NEXUS_REGISTRY
FROM $NEXUS_REGISTRY/base/cg-python-3.11:latest as builder

WORKDIR /src

ENV TZ Europe/Moscow
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=.
ENV PYTHONUNBUFFERED 1
ENV TESTING 0

COPY poetry.lock pyproject.toml ./

RUN  pip install poetry \
&& poetry config virtualenvs.create false \
&& poetry install --no-root

COPY . ./.

ENTRYPOINT bash -c "uvicorn src.application:app --host 0.0.0.0 --port 8000 --reload"
