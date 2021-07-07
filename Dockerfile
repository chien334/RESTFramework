FROM python:3.8-buster

LABEL Andrew Le
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY  ./app /app
RUN  adduser --disabled-password user
USER user
