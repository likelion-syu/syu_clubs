FROM python:3

ENV PYTHONUNBUFFERED 0

RUN apt-get -y install \
    libpq-dev

WORKDIR /app

COPY . /app/

RUN    pip install -r requirements.txt

