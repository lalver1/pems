ARG ELASTIC_STACK_VERSION=8.16.1

FROM docker.elastic.co/beats/metricbeat:${ELASTIC_STACK_VERSION}

USER root

COPY ./elasticstack/metricbeat01/metricbeat.yml metricbeat.yml

RUN chmod go-w metricbeat.yml
