#!/usr/bin/env bash

set -e

if [ -z "${DB_HOST}" ]; then
  echo "Please set the DB_HOST environment variable"
  exit 1
 fi

 if [ -z "${DB_USER}" ]; then
  echo "Please set the DB_USER environment variable"
  exit 1
 fi

 if [ -z "${DB_PASSWORD}" ]; then
  echo "Please set the DB_PASSWORD environment variable"
  exit 1
 fi

 if [ -z "${DB_NAME}" ]; then
  echo "Please set the DB_NAME environment variable"
  exit 1
 fi


 if [ -z "${DB_TABLE}" ]; then
  echo "Please set the DB_TABLE environment variable"
  exit 1
 fi

PGPASSWORD="${DB_PASSWORD}" pg_dump --column-inserts --data-only  -h "${DB_HOST}" -U "${DB_USER}" "${DB_NAME}" -t "${DB_TABLE}"
