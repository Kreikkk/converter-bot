FROM python:3.9-alpine

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN apk add build-base
RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY . .