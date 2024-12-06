#!/usr/bin/env bash
set -eu

if [ x${ELASTIC_PASSWORD} == x ]; then
    echo "Set the ELASTIC_PASSWORD environment variable in the .env file";
    exit 1;
elif [ x${KIBANA_PASSWORD} == x ]; then
    echo "Set the KIBANA_PASSWORD environment variable in the .env file";
    exit 1;
fi;

if [ ! -f config/certs/ca.zip ]; then
    echo "Creating CA";
    bin/elasticsearch-certutil ca --silent --pem -out config/certs/ca.zip;
    unzip config/certs/ca.zip -d config/certs;
fi;

if [ ! -f config/certs/certs.zip ]; then
    echo "Creating certs";
    cp /.local/config/instances.yml config/certs/instances.yml;
    bin/elasticsearch-certutil cert --silent --pem \
        -out config/certs/certs.zip \
        --in config/certs/instances.yml \
        --ca-cert config/certs/ca/ca.crt \
        --ca-key config/certs/ca/ca.key;
    unzip config/certs/certs.zip -d config/certs;
fi;

echo "Setting file permissions"
chown -R root:root config/certs;

find . -type d -exec chmod 755 \{\} \;;
find . -type f -exec chmod 644 \{\} \;;

TIMEOUT=10

until
    echo "Waiting for Elasticsearch availability (sleeping for ${TIMEOUT}s)";
    curl -s --cacert config/certs/ca/ca.crt https://es01:9200 | grep -q "missing authentication credentials";
do sleep $TIMEOUT; done;

until
    echo "Setting kibana_system password (sleeping for ${TIMEOUT}s)";
    curl -s -X POST \
        --cacert config/certs/ca/ca.crt \
        -u "elastic:${ELASTIC_PASSWORD}" \
        -H "Content-Type: application/json" https://es01:9200/_security/user/kibana_system/_password \
        -d "{\"password\":\"${KIBANA_PASSWORD}\"}" | grep -q "^{}";
do sleep $TIMEOUT; done;

echo "All done!";
