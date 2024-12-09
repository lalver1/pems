#!/usr/bin/env bash
set -eux

# run database migrations

python manage.py migrate
