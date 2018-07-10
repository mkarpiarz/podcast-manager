FROM python:3
MAINTAINER Mariusz Karpiarz

ARG PROJECT_DIR=./podcastmanager
WORKDIR /opt
ADD $PROJECT_DIR project
WORKDIR /opt/project
RUN pip install -r requirements.txt
