#!/bin/sh

until pg_isready -h db -p 5432; do
  echo "Waiting for PostgreSQL at db:5432..."
  sleep 2
done

exec "$@"
