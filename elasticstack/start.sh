#!/usr/bin/env bash
set -u

docker compose up -d metricbeat01 filebeat01 logstash01
