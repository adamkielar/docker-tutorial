FROM python:3.9.0-slim
LABEL maintainer="Adam Kielar"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

COPY ./app .

RUN pip install poetry==1.0.5 \
    && poetry config virtualenvs.create false \
    && poetry install -n --no-root --no-dev

WORKDIR /