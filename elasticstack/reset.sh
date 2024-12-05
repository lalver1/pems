#!/usr/bin/env bash
set -u

docker compose down

docker volume ls -q | grep pems_ | xargs docker volume rm

docker compose build metricbeat01 filebeat01 logstash01
