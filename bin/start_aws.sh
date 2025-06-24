#!/usr/bin/env bash
set -eu

# S3 bucket name is injected by Copilot as an environment variable
# since it was created via copilot storage init --name pems-db, the variable is 'PEMSDB_NAME'
S3_BUCKET_NAME="$PEMSDB_NAME"
S3_FIXTURE_PATH="fixtures.json"
DJANGO_DB_FIXTURES="fixtures.json"

echo "Downloading $S3_FIXTURE_PATH from bucket $S3_BUCKET_NAME"
aws s3 cp "s3://${S3_BUCKET_NAME}/${S3_FIXTURE_PATH}" "${DJANGO_DB_FIXTURES}"
echo "Download complete"

# PostgreSQL database settings (username, host, dbname, password, port) are injected by Copilot as an environment variable
# called 'POSTGRESWEB_SECRET' since the database was created via
# copilot storage init -l workload -t Aurora -w web -n postgres-web --engine PostgreSQL --initial-db django

python manage.py migrate

# Load data fixtures (if any)
valid_fixtures=$(echo "$DJANGO_DB_FIXTURES" | grep -e fixtures\.json$ || test $? = 1)

if [[ -n "$valid_fixtures" ]]; then
    python manage.py loaddata $DJANGO_DB_FIXTURES
else
    echo "No JSON fixtures to load"
fi

bin/start.sh
