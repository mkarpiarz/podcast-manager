FROM python:3
MAINTAINER Mariusz Karpiarz

RUN apt-get update
RUN apt-get install -y supervisor
ADD supervisord.conf /etc/supervisor/supervisord.conf

ARG PROJECT_DIR=./podcastmanager
WORKDIR /opt
ADD $PROJECT_DIR project
WORKDIR /opt/project
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["/usr/bin/supervisord", "-n"]
