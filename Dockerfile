FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /djangoproject4
COPY ./djangoproject4 /djangoproject4
WORKDIR /djangoproject4