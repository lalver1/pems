ARG ELASTIC_STACK_VERSION=8.16.1

FROM docker.elastic.co/beats/filebeat:${ELASTIC_STACK_VERSION}

USER root

COPY ./elasticstack/filebeat01/filebeat.yml filebeat.yml

RUN chmod go-w filebeat.yml
