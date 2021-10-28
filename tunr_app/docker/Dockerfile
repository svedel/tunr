FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get -y install netcat gcc postgresql && apt-get -y install libpq-dev gcc && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./tunr_app/requirements.txt /tunr/tunr_app/requirements.txt
RUN pip install -r /tunr/tunr_app/requirements.txt

COPY . /tunr

WORKDIR /tunr