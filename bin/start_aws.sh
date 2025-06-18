#!/usr/bin/env bash
set -eu

#
# S3 bucket name is injected by Copilot as an environment variable
# since it was created via copilot storage init --name pems-db, the variable is 'PEMSDB_NAME'
S3_BUCKET_NAME="$PEMSDB_NAME"
S3_FIXTURE_PATH="fixtures.json"
LOCAL_FIXTURE_PATH="fixtures.json"

echo "Downloading $S3_FIXTURE_PATH from bucket $S3_BUCKET_NAME"
aws s3 cp "s3://${S3_BUCKET_NAME}/${S3_FIXTURE_PATH}" "${LOCAL_FIXTURE_PATH}"
echo "Download complete"

# initialize Django

bin/init.sh

# effectively reset database by loading downloaded fixtures into the database
echo "Loading data from ${LOCAL_FIXTURE_PATH}"
python manage.py loaddata "${LOCAL_FIXTURE_PATH}"
echo "Data loading complete"

# start the web server

nginx

# start the application server

python -m gunicorn -c $GUNICORN_CONF pems.wsgi
