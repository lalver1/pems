ARG ELASTIC_STACK_VERSION=8.16.1

FROM docker.elastic.co/logstash/logstash:${ELASTIC_STACK_VERSION}

USER root

COPY ./elasticstack/logstash01/logstash.conf pipeline/logstash.conf

RUN chmod go-w pipeline/logstash.conf
