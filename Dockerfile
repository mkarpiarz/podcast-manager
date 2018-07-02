FROM python:3
MAINTAINER Mariusz Karpiarz
ARG DJANGO_VERSION=1.11
RUN pip install \
    Django==$DJANGO_VERSION \
    djangorestframework
